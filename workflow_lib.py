#!/usr/bin/env python3
"""Shared helpers for local thesis workflow scripts."""

from __future__ import annotations

import json
import os
import re
import ssl
import subprocess
import hashlib
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib import request
from urllib.error import HTTPError, URLError

try:
    import yaml
except Exception:  # pragma: no cover
    yaml = None

REPO_ROOT = Path(__file__).resolve().parent
MEMORY_DIR = REPO_ROOT / ".memory"
INDEX_PATH = MEMORY_DIR / "index.json"
RESUME_PATH = MEMORY_DIR / "resume_context.txt"

TRACKED_EXTENSIONS = {".md", ".yaml", ".yml", ".csv", ".txt"}
EXCLUDE_DIRS = {".git", ".memory", "backups", "__pycache__"}
SUMMARY_DIRNAME = "session_summaries"
BLOB_SYNC_STATE_PATH = MEMORY_DIR / "blob_sync_state.json"
INPUT_BLOB_SYNC_STATE_PATH = MEMORY_DIR / "blob_input_sync_state.json"
INPUT_FILES_DIR = REPO_ROOT / "98_onedrive_migration" / "1_masterarbeit" / "00_input_files"

TOPIC_TO_DIR = {
    "architektur": "05_referenzarchitektur_RQ2/session_summaries",
    "anforderungen": "04_anforderungsanalyse_RQ1/session_summaries",
    "evaluation": "06_evaluation_RQ3/session_summaries",
    "methodik": "03_forschungsdesign_methodik/session_summaries",
    "theorie": "02_rigor_theorie_stand_forschung/session_summaries",
    "einleitung": "01_einleitung/session_summaries",
    "diskussion": "07_diskussion/session_summaries",
    "fazit": "08_fazit_ausblick/session_summaries",
    "general": "99_inbox_unsorted/session_summaries",
}

TOPIC_HINTS = {
    "architektur": ["architektur", "architecture", "rq2", "quality gate", "gate"],
    "anforderungen": ["anforderung", "requirement", "rq1", "muss", "soll"],
    "evaluation": ["evaluation", "rq3", "interview", "validierung", "coverage"],
    "methodik": ["methodik", "dsr", "forschungsdesign", "design science"],
    "theorie": ["theorie", "rigor", "literatur", "stand der forschung", "related work"],
    "einleitung": ["einleitung", "problemstellung", "motivation"],
    "diskussion": ["diskussion", "limitation", "kritik"],
    "fazit": ["fazit", "ausblick", "conclusion"],
}


@dataclass
class FileEntry:
    path: str
    size_bytes: int
    modified_utc: str
    lines: int


def load_dotenv(path: Path | None = None) -> None:
    env_file = path or (REPO_ROOT / ".env")
    if not env_file.exists():
        return
    for raw in env_file.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def _is_truthy_env(name: str) -> bool:
    return os.getenv(name, "").strip().lower() in {"1", "true", "yes", "on"}


def _build_tls_context(*insecure_env_names: str) -> ssl.SSLContext:
    if any(_is_truthy_env(name) for name in insecure_env_names):
        return ssl._create_unverified_context()

    ca_bundle = os.getenv("AZURE_CA_BUNDLE", "").strip() or os.getenv("SSL_CERT_FILE", "").strip()
    if ca_bundle:
        return ssl.create_default_context(cafile=ca_bundle)

    try:
        import certifi

        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        return ssl.create_default_context()


def _ssl_hint(error: Exception) -> str:
    reason = getattr(error, "reason", error)
    text = str(reason)
    if isinstance(reason, ssl.SSLCertVerificationError) or "CERTIFICATE_VERIFY_FAILED" in text:
        return (
            "TLS-Zertifikatspruefung fehlgeschlagen (CERTIFICATE_VERIFY_FAILED). "
            "macOS-Fix: '/Applications/Python 3.x/Install Certificates.command' ausfuehren "
            "oder AZURE_CA_BUNDLE/SSL_CERT_FILE auf ein gueltiges CA-Bundle setzen. "
            "Nur als Notfall: AZURE_SEARCH_INSECURE_TLS=1."
        )
    return ""


def _load_yaml(path: Path) -> dict:
    if yaml is None:
        return {}
    try:
        with path.open("r", encoding="utf-8") as f:
            value = yaml.safe_load(f)
        return value if isinstance(value, dict) else {}
    except Exception:
        return {}


def _dump_yaml(path: Path, payload: dict) -> None:
    if yaml is None:
        raise RuntimeError("PyYAML fehlt. Bitte installieren: pip install pyyaml")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8")


def iter_source_files() -> Iterable[Path]:
    for p in REPO_ROOT.rglob("*"):
        if not p.is_file():
            continue
        if any(part in EXCLUDE_DIRS for part in p.parts):
            continue
        if p.suffix.lower() not in TRACKED_EXTENSIONS:
            continue
        yield p


def _slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "summary"


def detect_topic(text: str) -> str:
    lower = text.lower()
    best_topic = "general"
    best_score = 0
    for topic, hints in TOPIC_HINTS.items():
        score = sum(lower.count(h) for h in hints)
        if score > best_score:
            best_score = score
            best_topic = topic
    return best_topic


def summarize_text_to_bullets(text: str, max_bullets: int = 8) -> list[str]:
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    bullets = []

    for ln in lines:
        cleaned = re.sub(r"^[-*\d.)\s]+", "", ln).strip()
        if len(cleaned) < 18:
            continue
        if len(cleaned) > 220:
            cleaned = cleaned[:217].rstrip() + "..."
        if cleaned not in bullets:
            bullets.append(cleaned)
        if len(bullets) >= max_bullets:
            break

    if len(bullets) < max_bullets:
        joined = " ".join(lines)
        sentences = re.split(r"(?<=[.!?])\s+", joined)
        for sent in sentences:
            sent = sent.strip()
            if len(sent) < 24:
                continue
            if len(sent) > 220:
                sent = sent[:217].rstrip() + "..."
            if sent not in bullets:
                bullets.append(sent)
            if len(bullets) >= max_bullets:
                break

    return bullets[:max_bullets]


def extract_actions(text: str) -> tuple[list[str], list[str]]:
    decisions: list[str] = []
    next_steps: list[str] = []
    for raw in text.splitlines():
        line = raw.strip().lower()
        if not line:
            continue
        if any(k in line for k in ["entscheidung", "decision", "beschluss", "wir machen"]):
            decisions.append(raw.strip())
        if any(k in line for k in ["naechste", "nächste", "todo", "to-do", "next step", "offen"]):
            next_steps.append(raw.strip())
    return decisions[:6], next_steps[:8]


def azure_openai_configured() -> bool:
    load_dotenv()
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "").rstrip("/")
    key = os.getenv("AZURE_OPENAI_API_KEY", "") or os.getenv("AZURE_OPENAI_KEY", "")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT", "") or os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT", "")
    return bool(endpoint and key and deployment)


def _azure_openai_chat_complete(messages: list[dict]) -> dict:
    load_dotenv()
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "").rstrip("/")
    key = os.getenv("AZURE_OPENAI_API_KEY", "") or os.getenv("AZURE_OPENAI_KEY", "")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT", "") or os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT", "")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-10-21")
    max_tokens = int(os.getenv("AZURE_OPENAI_MAX_OUTPUT_TOKENS", "300"))
    temperature = float(os.getenv("AZURE_OPENAI_TEMPERATURE", "0.1"))

    if not endpoint or not key or not deployment:
        raise RuntimeError("AZURE_OPENAI_* Konfiguration fehlt.")

    url = f"{endpoint}/openai/deployments/{deployment}/chat/completions?api-version={api_version}"
    payload = {
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "response_format": {"type": "json_object"},
    }

    req = request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={"Content-Type": "application/json", "api-key": key},
    )
    context = _build_tls_context("AZURE_OPENAI_INSECURE_TLS", "AZURE_INSECURE_TLS", "AZURE_SEARCH_INSECURE_TLS")
    with request.urlopen(req, timeout=45, context=context) as resp:
        body = resp.read().decode("utf-8", errors="replace")
        return json.loads(body)


def summarize_with_azure_openai(text: str, max_bullets: int = 8) -> tuple[list[str], list[str], list[str], str]:
    max_input_chars = int(os.getenv("AZURE_OPENAI_MAX_INPUT_CHARS", "6000"))
    safe_text = text[:max_input_chars]
    prompt = (
        "Fasse die Session fuer eine Masterarbeit kompakt zusammen. "
        "Gib NUR gueltiges JSON zurueck mit den Schluesseln: "
        "title (string), summary_bullets (array), decisions (array), next_steps (array). "
        f"summary_bullets max {max_bullets} Eintraege, jeweils kurze, klare Stichpunkte."
    )
    messages = [
        {"role": "system", "content": "Du strukturierst wissenschaftliche Arbeitsnotizen praezise und knapp."},
        {"role": "user", "content": f"{prompt}\n\nSESSION:\n{safe_text}"},
    ]
    result = _azure_openai_chat_complete(messages)
    content = (
        result.get("choices", [{}])[0]
        .get("message", {})
        .get("content", "{}")
    )
    parsed = json.loads(content)

    bullets = parsed.get("summary_bullets", []) or []
    decisions = parsed.get("decisions", []) or []
    next_steps = parsed.get("next_steps", []) or []
    title = parsed.get("title", "") or ""

    def _clean(items: list, limit: int) -> list[str]:
        out: list[str] = []
        for i in items:
            s = str(i).strip()
            if not s:
                continue
            if len(s) > 220:
                s = s[:217].rstrip() + "..."
            if s not in out:
                out.append(s)
            if len(out) >= limit:
                break
        return out

    return _clean(bullets, max_bullets), _clean(decisions, 6), _clean(next_steps, 8), title


def summary_output_path(topic: str, title: str | None = None) -> Path:
    rel_dir = TOPIC_TO_DIR.get(topic, TOPIC_TO_DIR["general"])
    target_dir = REPO_ROOT / rel_dir
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    suffix = _slugify(title or topic)
    return target_dir / f"{ts}_{suffix}.yaml"


def save_session_summary(
    text: str,
    topic: str = "auto",
    title: str | None = None,
    source: str = "manual",
    tags: list[str] | None = None,
    use_llm: bool = True,
) -> tuple[Path, dict]:
    resolved_topic = detect_topic(text) if topic == "auto" else topic.lower().strip()
    if resolved_topic not in TOPIC_TO_DIR:
        resolved_topic = "general"

    llm_used = False
    llm_error = ""
    llm_title = ""
    bullets: list[str] = []
    decisions: list[str] = []
    next_steps: list[str] = []

    if use_llm and azure_openai_configured():
        try:
            bullets, decisions, next_steps, llm_title = summarize_with_azure_openai(text)
            llm_used = True
        except Exception as e:
            llm_error = str(e)

    if not bullets:
        bullets = summarize_text_to_bullets(text)
    if not decisions or not next_steps:
        local_decisions, local_next = extract_actions(text)
        if not decisions:
            decisions = local_decisions
        if not next_steps:
            next_steps = local_next

    path = summary_output_path(resolved_topic, title)
    final_title = title or llm_title or "Session Summary"

    payload = {
        "id": f"SUM-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "topic": resolved_topic,
        "target_folder": str(path.parent.relative_to(REPO_ROOT)),
        "title": final_title,
        "summary_bullets": bullets,
        "decisions": decisions,
        "next_steps": next_steps,
        "tags": tags or [],
        "source": source,
        "summary_engine": "azure_openai" if llm_used else "local_rules",
    }
    if llm_error:
        payload["summary_engine_error"] = llm_error[:300]
    _dump_yaml(path, payload)
    return path, payload


def load_session_summaries(limit: int | None = None) -> list[dict]:
    rows: list[dict] = []
    for p in sorted(REPO_ROOT.rglob(f"{SUMMARY_DIRNAME}/*.yaml"), reverse=True):
        doc = _load_yaml(p)
        if not doc:
            continue
        doc["path"] = str(p.relative_to(REPO_ROOT))
        rows.append(doc)
        if limit and len(rows) >= limit:
            break
    return rows


def build_index() -> dict:
    entries = []
    for path in sorted(iter_source_files()):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
            lines = text.count("\n") + (1 if text else 0)
            stat = path.stat()
            entries.append(
                FileEntry(
                    path=str(path.relative_to(REPO_ROOT)),
                    size_bytes=stat.st_size,
                    modified_utc=datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
                    lines=lines,
                ).__dict__
            )
        except Exception:
            continue

    chapter_states = []
    for p in sorted(REPO_ROOT.rglob("chapter_state.yaml")):
        meta = _load_yaml(p)
        chapter_states.append(
            {
                "path": str(p.relative_to(REPO_ROOT)),
                "chapter": meta.get("chapter", ""),
                "status": meta.get("status", ""),
                "current_focus": meta.get("current_focus", ""),
            }
        )

    requirements = []
    req_dir = REPO_ROOT / "04_anforderungsanalyse_RQ1" / "requirements"
    if req_dir.exists():
        for p in sorted(req_dir.glob("R*.yaml")):
            req = _load_yaml(p)
            requirements.append(
                {
                    "id": req.get("id", p.stem),
                    "title": req.get("title", ""),
                    "type": req.get("type", ""),
                    "phase": req.get("lifecycle_phase", ""),
                    "linked_gates": req.get("linked_gates", []),
                    "path": str(p.relative_to(REPO_ROOT)),
                }
            )

    gates = []
    gate_dir = REPO_ROOT / "05_referenzarchitektur_RQ2" / "05_03_quality_gates"
    if gate_dir.exists():
        for p in sorted(gate_dir.rglob("G*.yaml")):
            gate = _load_yaml(p)
            gates.append(
                {
                    "id": gate.get("id", p.stem),
                    "name": gate.get("name", ""),
                    "dimension": gate.get("dimension", ""),
                    "decision": gate.get("decision", ""),
                    "path": str(p.relative_to(REPO_ROOT)),
                }
            )

    summaries = load_session_summaries(limit=None)

    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "repo_root": str(REPO_ROOT),
        "files": entries,
        "chapter_states": chapter_states,
        "requirements": requirements,
        "gates": gates,
        "session_summaries": summaries,
    }


def write_index(index: dict) -> Path:
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    return INDEX_PATH


def _latest_session_file() -> Path | None:
    session_dir = REPO_ROOT / "91_progress_log"
    if not session_dir.exists():
        return None
    sessions = sorted([p for p in session_dir.glob("*_session.md") if p.name != "_session_template.md"])
    return sessions[-1] if sessions else None


def build_resume_text(index: dict) -> str:
    lines = []
    lines.append("Hier ist mein aktueller Thesis-Stand - bitte nutze das als Kontext:")
    lines.append("")
    lines.append(f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"Repo: {index.get('repo_root','')}")
    lines.append(f"Artefakte indexiert: {len(index.get('files', []))} Dateien")
    lines.append("")

    lines.append("Kapitelstatus:")
    chapter_states = index.get("chapter_states", [])
    if not chapter_states:
        lines.append("- Keine chapter_state.yaml gefunden.")
    else:
        for c in chapter_states:
            chapter = c.get("chapter") or c.get("path")
            status = c.get("status") or "unknown"
            focus = c.get("current_focus") or ""
            suffix = f" | Fokus: {focus}" if focus else ""
            lines.append(f"- {chapter}: {status}{suffix}")

    lines.append("")
    lines.append("Requirements (RQ1):")
    requirements = index.get("requirements", [])
    if not requirements:
        lines.append("- Keine R*.yaml gefunden.")
    else:
        for r in requirements:
            rid = r.get("id", "")
            title = r.get("title", "") or "(noch ohne Titel)"
            lines.append(f"- {rid}: {title}")

    lines.append("")
    lines.append("Quality Gates (RQ2):")
    gates = index.get("gates", [])
    if not gates:
        lines.append("- Keine G*.yaml gefunden.")
    else:
        for g in gates:
            gid = g.get("id", "")
            dim = g.get("dimension", "")
            name = g.get("name", "") or "(noch ohne Name)"
            lines.append(f"- {gid} [{dim}]: {name}")

    lines.append("")
    lines.append("Letzte Session-Summaries:")
    summaries = index.get("session_summaries", [])[:5]
    if not summaries:
        lines.append("- Keine Session-Summaries vorhanden.")
    else:
        for s in summaries:
            topic = s.get("topic", "general")
            title = s.get("title", "Session Summary")
            bullets = s.get("summary_bullets", [])
            first = bullets[0] if bullets else "(ohne Stichpunkte)"
            lines.append(f"- [{topic}] {title}: {first}")

    session_file = _latest_session_file()
    lines.append("")
    if session_file:
        lines.append(f"Letztes Session-Log: {session_file.relative_to(REPO_ROOT)}")
    else:
        lines.append("Letztes Session-Log: keines gefunden")

    return "\n".join(lines).strip() + "\n"


def write_resume_text(text: str) -> Path:
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    RESUME_PATH.write_text(text, encoding="utf-8")
    return RESUME_PATH


def azure_configured() -> bool:
    load_dotenv()
    endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
    key = os.getenv("AZURE_SEARCH_ADMIN_KEY") or os.getenv("AZURE_SEARCH_KEY")
    index_name = os.getenv("AZURE_SEARCH_INDEX_NAME") or os.getenv("AZURE_SEARCH_INDEX")
    return bool(endpoint and key and index_name)


def blob_configured() -> bool:
    load_dotenv()
    account = os.getenv("AZURE_STORAGE_ACCOUNT")
    key = os.getenv("AZURE_STORAGE_KEY")
    return bool(account and key)


def input_blob_sync_enabled() -> bool:
    load_dotenv()
    return _is_truthy_env("AZURE_INPUT_BLOB_SYNC")


def _fetch_azure_index_schema(endpoint: str, key: str, index_name: str, api_version: str) -> tuple[dict, str]:
    url = f"{endpoint}/indexes/{index_name}?api-version={api_version}"
    req = request.Request(url, method="GET", headers={"api-key": key})
    context = _build_tls_context("AZURE_SEARCH_INSECURE_TLS", "AZURE_INSECURE_TLS")
    with request.urlopen(req, timeout=30, context=context) as resp:
        body = resp.read().decode("utf-8", errors="replace")
        schema = json.loads(body)
        return schema, body


def _summary_docs_for_azure(index: dict, schema: dict) -> tuple[list[dict], str]:
    fields = schema.get("fields", []) if isinstance(schema, dict) else []
    by_name = {f.get("name"): f for f in fields if isinstance(f, dict) and f.get("name")}
    string_fields = [f.get("name") for f in fields if f.get("type") == "Edm.String" and f.get("name")]
    key_candidates = [f.get("name") for f in fields if f.get("key") is True and f.get("name")]

    configured_key = os.getenv("AZURE_SEARCH_KEY_FIELD", "")
    if configured_key and configured_key in by_name:
        key_field = configured_key
    elif key_candidates:
        key_field = key_candidates[0]
    elif "id" in by_name:
        key_field = "id"
    else:
        return [], "Kein Key-Feld im Azure-Index gefunden."

    configured_content = os.getenv("AZURE_SEARCH_CONTENT_FIELD", "")
    content_priorities = [configured_content, "content", "text", "summary", "body", "chunk", "message"]
    content_field = ""
    for c in content_priorities:
        if c and c in by_name:
            content_field = c
            break
    if not content_field:
        for sf in string_fields:
            if sf != key_field:
                content_field = sf
                break
    if not content_field:
        return [], "Kein geeignetes Content-Feld (Edm.String) im Azure-Index gefunden."

    title_field = "title" if "title" in by_name else ("name" if "name" in by_name else "")
    topic_field = "topic" if "topic" in by_name else ("category" if "category" in by_name else "")
    source_field = "source_path" if "source_path" in by_name else ("source" if "source" in by_name else "")
    created_field = "created_at" if "created_at" in by_name else ("timestamp" if "timestamp" in by_name else "")

    docs = []
    for s in index.get("session_summaries", []):
        sid = s.get("id") or _slugify(s.get("path", "summary"))
        bullets = s.get("summary_bullets", [])
        content = "\n".join(f"- {b}" for b in bullets)
        doc = {"@search.action": "mergeOrUpload", key_field: sid, content_field: content}
        if title_field:
            doc[title_field] = s.get("title", "Session Summary")
        if topic_field:
            doc[topic_field] = s.get("topic", "general")
        if source_field:
            doc[source_field] = s.get("path", "")
        if created_field:
            doc[created_field] = s.get("created_at", "")
        docs.append(doc)

    return docs, f"Schema erkannt: key={key_field}, content={content_field}"


def push_index_to_azure(index: dict) -> tuple[bool, str]:
    load_dotenv()
    endpoint = os.getenv("AZURE_SEARCH_ENDPOINT", "").rstrip("/")
    key = os.getenv("AZURE_SEARCH_ADMIN_KEY", "") or os.getenv("AZURE_SEARCH_KEY", "")
    index_name = os.getenv("AZURE_SEARCH_INDEX_NAME", "") or os.getenv("AZURE_SEARCH_INDEX", "")
    api_version = os.getenv("AZURE_SEARCH_API_VERSION", "2023-11-01")

    if not endpoint or not key or not index_name:
        return False, "Azure-Konfiguration fehlt (AZURE_SEARCH_ENDPOINT, AZURE_SEARCH_ADMIN_KEY, AZURE_SEARCH_INDEX_NAME)."

    try:
        schema, _ = _fetch_azure_index_schema(endpoint, key, index_name, api_version)
    except HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return False, f"Azure HTTP-Fehler beim Schema-Read {e.code}: {body[:400]}"
    except URLError as e:
        hint = _ssl_hint(e)
        suffix = f" Hinweis: {hint}" if hint else ""
        return False, f"Azure Netzwerkfehler beim Schema-Read: {e}.{suffix}"

    docs, schema_msg = _summary_docs_for_azure(index, schema)
    if not docs:
        return True, f"{schema_msg} Keine Session-Summaries vorhanden oder keine passenden Felder."

    url = f"{endpoint}/indexes/{index_name}/docs/index?api-version={api_version}"
    payload = json.dumps({"value": docs}).encode("utf-8")
    req = request.Request(
        url,
        data=payload,
        method="POST",
        headers={"Content-Type": "application/json", "api-key": key},
    )

    try:
        context = _build_tls_context("AZURE_SEARCH_INSECURE_TLS", "AZURE_INSECURE_TLS")
        with request.urlopen(req, timeout=30, context=context) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return True, f"{schema_msg}. Azure-Index aktualisiert ({len(docs)} Dokumente). Response: {body[:200]}"
    except HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return False, f"Azure HTTP-Fehler {e.code}: {body[:400]}"
    except URLError as e:
        hint = _ssl_hint(e)
        suffix = f" Hinweis: {hint}" if hint else ""
        return False, f"Azure Netzwerkfehler: {e}.{suffix}"


def _blob_container_name() -> str:
    return os.getenv("AZURE_BLOB_CONTAINER", "session-summaries")


def _input_blob_container_name() -> str:
    return os.getenv("AZURE_INPUT_BLOB_CONTAINER", "thesis-input-files")


def _list_summary_files() -> list[Path]:
    return sorted(REPO_ROOT.rglob(f"{SUMMARY_DIRNAME}/*.yaml"))


def _list_input_files() -> list[Path]:
    if not INPUT_FILES_DIR.exists():
        return []
    return sorted([p for p in INPUT_FILES_DIR.rglob("*") if p.is_file()])


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _load_blob_sync_state() -> dict:
    if not BLOB_SYNC_STATE_PATH.exists():
        return {}
    try:
        return json.loads(BLOB_SYNC_STATE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _write_blob_sync_state(state: dict) -> None:
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    BLOB_SYNC_STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def _load_input_blob_sync_state() -> dict:
    if not INPUT_BLOB_SYNC_STATE_PATH.exists():
        return {}
    try:
        return json.loads(INPUT_BLOB_SYNC_STATE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _write_input_blob_sync_state(state: dict) -> None:
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    INPUT_BLOB_SYNC_STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def push_summaries_to_blob() -> tuple[bool, str]:
    load_dotenv()
    account = os.getenv("AZURE_STORAGE_ACCOUNT", "")
    key = os.getenv("AZURE_STORAGE_KEY", "")
    container = _blob_container_name()

    if not account or not key:
        return False, "Blob-Konfiguration fehlt (AZURE_STORAGE_ACCOUNT, AZURE_STORAGE_KEY)."

    files = _list_summary_files()
    if not files:
        return True, "Keine Session-Summaries vorhanden, nichts nach Blob zu pushen."

    state = _load_blob_sync_state()
    previous_container = state.get("container") if isinstance(state, dict) else None
    synced = state.get("synced_hashes", {}) if isinstance(state, dict) else {}
    if not isinstance(synced, dict):
        synced = {}

    # If the target container changed, force a one-time full upload to avoid cross-project cache skips.
    if previous_container and previous_container != container:
        synced = {}

    try:
        create_cmd = [
            "az",
            "storage",
            "container",
            "create",
            "--name",
            container,
            "--account-name",
            account,
            "--account-key",
            key,
            "--auth-mode",
            "key",
            "--output",
            "none",
        ]
        subprocess.run(create_cmd, check=True, capture_output=True, text=True)
    except FileNotFoundError:
        return False, "Azure CLI (az) nicht gefunden."
    except subprocess.CalledProcessError as e:
        return False, f"Container-Erstellung fehlgeschlagen: {(e.stderr or e.stdout).strip()[:300]}"

    uploaded = 0
    skipped = 0
    new_synced: dict[str, str] = {}
    for file_path in files:
        rel = file_path.relative_to(REPO_ROOT).as_posix()
        file_hash = _sha256_file(file_path)
        new_synced[rel] = file_hash
        if synced.get(rel) == file_hash:
            skipped += 1
            continue
        blob_name = rel
        cmd = [
            "az",
            "storage",
            "blob",
            "upload",
            "--container-name",
            container,
            "--account-name",
            account,
            "--account-key",
            key,
            "--auth-mode",
            "key",
            "--file",
            str(file_path),
            "--name",
            blob_name,
            "--overwrite",
            "true",
            "--output",
            "none",
        ]
        try:
            subprocess.run(cmd, check=True, capture_output=True, text=True)
            uploaded += 1
        except subprocess.CalledProcessError as e:
            return False, f"Blob-Upload fehlgeschlagen ({rel}): {(e.stderr or e.stdout).strip()[:300]}"

    _write_blob_sync_state(
        {
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "container": container,
            "synced_hashes": new_synced,
        }
    )
    return True, (
        f"Blob-Sync erfolgreich: {uploaded} hochgeladen, {skipped} unveraendert "
        f"(Container '{container}')."
    )


def push_input_files_to_blob() -> tuple[bool, str]:
    load_dotenv()
    account = os.getenv("AZURE_STORAGE_ACCOUNT", "")
    key = os.getenv("AZURE_STORAGE_KEY", "")
    container = _input_blob_container_name()

    if not account or not key:
        return False, "Blob-Konfiguration fehlt (AZURE_STORAGE_ACCOUNT, AZURE_STORAGE_KEY)."

    files = _list_input_files()
    if not files:
        return True, f"Keine Input-Dateien vorhanden in '{INPUT_FILES_DIR.relative_to(REPO_ROOT)}'."

    state = _load_input_blob_sync_state()
    previous_container = state.get("container") if isinstance(state, dict) else None
    synced = state.get("synced_hashes", {}) if isinstance(state, dict) else {}
    if not isinstance(synced, dict):
        synced = {}
    if previous_container and previous_container != container:
        synced = {}

    try:
        create_cmd = [
            "az",
            "storage",
            "container",
            "create",
            "--name",
            container,
            "--account-name",
            account,
            "--account-key",
            key,
            "--auth-mode",
            "key",
            "--output",
            "none",
        ]
        subprocess.run(create_cmd, check=True, capture_output=True, text=True)
    except FileNotFoundError:
        return False, "Azure CLI (az) nicht gefunden."
    except subprocess.CalledProcessError as e:
        return False, f"Container-Erstellung fehlgeschlagen: {(e.stderr or e.stdout).strip()[:300]}"

    uploaded = 0
    skipped = 0
    new_synced: dict[str, str] = {}
    prefix = INPUT_FILES_DIR.relative_to(REPO_ROOT).as_posix()
    for file_path in files:
        rel = file_path.relative_to(REPO_ROOT).as_posix()
        file_hash = _sha256_file(file_path)
        new_synced[rel] = file_hash
        if synced.get(rel) == file_hash:
            skipped += 1
            continue
        blob_name = f"{prefix}/{file_path.relative_to(INPUT_FILES_DIR).as_posix()}"
        cmd = [
            "az",
            "storage",
            "blob",
            "upload",
            "--container-name",
            container,
            "--account-name",
            account,
            "--account-key",
            key,
            "--auth-mode",
            "key",
            "--file",
            str(file_path),
            "--name",
            blob_name,
            "--overwrite",
            "true",
            "--output",
            "none",
        ]
        try:
            subprocess.run(cmd, check=True, capture_output=True, text=True)
            uploaded += 1
        except subprocess.CalledProcessError as e:
            return False, f"Blob-Upload fehlgeschlagen ({rel}): {(e.stderr or e.stdout).strip()[:300]}"

    _write_input_blob_sync_state(
        {
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "container": container,
            "synced_hashes": new_synced,
        }
    )
    return True, (
        f"Input-Blob-Sync erfolgreich: {uploaded} hochgeladen, {skipped} unveraendert "
        f"(Container '{container}')."
    )
