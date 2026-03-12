# Deep Reading: Elia 2025 - MQG4AI

## Bibliographic Information

**Title:** MQG4AI: Towards Responsible High-risk AI – Illustrated for Transparency Focusing on Explainability Techniques

**Authors:** 
- Miriam Elia (Faculty of Applied Computer Science, University of Augsburg)
- Alba Maria Lopez (Artificial Intelligence Department, ETSI Informaticos, Universidad Politécnica)
- Katherin Alexandra Corredor Páez (ETSI Informaticos, Universidad Politécnica)
- Bernhard Bauer (University of Augsburg)
- Esteban Garcia-Cuesta (Universidad Politécnica)

**Status:** Preprint version submitted for journal review (as of 2025)

**Funding:** German Federal Ministry of Education and Research (BMBF) under reference 031L9196B, and grant IAX from Comunidad de Madrid Young Investigators 2023/2024

**GitHub Repository:** https://github.com/miriamelia/MQG4AI

---

## Core Contribution (Executive Summary)

MQG4AI is a **generic, customizable methodology based on Quality Gates (QGs) designed to operationalize Responsible AI (RAI) implementation across the complete AI lifecycle**. The framework bridges the gap between abstract RAI guidelines and use case-specific technical requirements by introducing a structured Information Management (IM) approach that continuously links design decisions with AI risks, regulatory compliance, and ethics. The paper specifically illustrates this framework through the transparency requirement of **Explainability in Deep Neural Networks (DNNs)**, demonstrating how to evaluate the quality of LIME and SHAP explanations using fidelity-robustness metrics integrated into quality gate decision points.

---

## MQG4AI Framework Structure

### Overall Architecture

MQG4AI is built on **four fundamental design principles**:

1. **Quality by Design**: Integration of quality assurance throughout the AI lifecycle, not as an afterthought
2. **Information Management (IM) Integration**: Structured capture and linking of lifecycle design decisions with risk management and compliance requirements
3. **Knowledge Management (KM) Continuous Evolution**: Decentralized contribution to RAI knowledge base (MQG4DK) that feeds into individual project implementations (MQG4A)
4. **Flexibility for Use Case Specificity**: Generic templates that adapt to domain and application-specific contexts

### Three Core Template Sections

The MQG4AI template is organized into three interconnected sections:

#### 1. **AI System Information**
- Based on **AI Risk Ontology (AIRO)** framework
- Subsections: Application, Compliance, Documentation, Ethics_General, Stakeholder
- Additional: Ethics_Specific (application-tailored), Domain Knowledge
- **Stakeholder roles** stratified as: active, consulting, passive (for directed information management)

#### 2. **Risk Management Information**
- **Seven AI Trustworthiness (TAI) Criteria** from ALTAI Assessment List:
  - Human agency and oversight
  - Technical robustness and safety
  - Privacy and data governance
  - **Transparency** (primary focus for XAI in this paper)
  - Diversity, non-discrimination, fairness
  - Societal and environmental well-being
  - Accountability
- Links identified risks to lifecycle design decisions
- Organized per NIST AI Risk Management Framework structure (DEFINE, ASSESS, TREAT, GOVERN)

#### 3. **Lifecycle Information**
- Structured through **Quality Gates (QGs)** that mirror design decisions and process stages
- Organized in **six generic AI lifecycle phases**:
  1. **Conceptualization** (business analysis, system requirements, Inception)
  2. **Data** (data quality, transformation, preprocessing)
  3. **Development** (model creation, evaluation, refinement)
  4. **Deployment** (real-world integration, pipeline integration)
  5. **Maintenance** (monitoring, continuous validation, re-evaluation, model replacement)
  6. **Decommissioning** (model retirement, reversal of lifecycle steps)

### Two MQG4AI Interaction Scenarios

#### **MQG4DK (Design Knowledge Base)**
- Decentralized, evolving repository of RAI best practices
- Generic QGs linked with practical guidelines
- Grows continuously as new knowledge emerges
- Structured for intelligent search and retrieval via QG tags
- Provides reusable patterns for high-risk AI systems

#### **MQG4A (Application)**
- Project-specific instantiation of MQG4AI during individual AI projects
- Multiple versioned iterations reflecting lifecycle evolution
- Structured like Git branching (decentralized contributions → quality checks → central merge)
- Versions: **pre-selection, intra-selection, post-selection** reflecting iterative design decision-making phases
- Pulls customized content from MQG4DK based on QG-tags

---

## Quality Gate Definitions and Criteria

### Two Types of Quality Gates

#### **Collection-QGs (Hierarchical Process Organization)**
- Organize and summarize related sub-QGs
- Create vertical and horizontal interdependencies
- Identify generalizable process steps across AI lifecycle stages
- Can be nested (up to n sub-QG levels)
- Example: QG4Application (root node) summarizes all lifecycle QGs
- Enable stakeholder-specific scoring systems (e.g., stakeholder participation score)

#### **Leaf-QGs (Design Decision Specification)**
- Mirror **concrete design decisions** within the AI lifecycle
- Provide use case-specific technical guidance
- Structured around **three dimensions**:
  1. **Content**: Detailed explanation of the design decision
  2. **Method**: Design decision-making process and implementation steps
  3. **Representation**: Stakeholder-specific information formatting and communication
- Include **four information layers**:
  1. **Input Information**: Required inputs from other QGs and system context
  2. **Output Information**: Impacts on other lifecycle stages and post-market monitoring
  3. **Evaluation Layer**: Open questions, drawbacks, risks of approach
  4. **Risk Management Layer**: Links to identified AI risks and residual risk analysis

### QG Naming Convention

```
QG_name_(view)
```

- **name**: Describes leaf-QG content/design decision
- **view**: AI technique applicability (e.g., SHAPLIME for SHAP and LIME explanations)
- **Tags**: Machine learning design patterns for intelligent search/retrieval

---

## High-Risk AI Handling

### Risk-Based Approach

**MQG4AI explicitly targets high-risk AI systems** as defined by the EU AI Act:

1. **Emphasis on Medical Domain**: Paper uses medical/healthcare AI as primary use case (aligned with ISO 14971 medical device risk management)
2. **Risk Identification and Mitigation by Design**: Every design decision is linked to identified AI risks and risk controls
3. **Iterative Risk Assessment**: Risk evaluation happens across MQG4A-version iterations (pre-, intra-, post-selection)
4. **Residual Risk Analysis**: Evaluation layer assesses residual risks after mitigation attempts

### High-Risk AI Specificity

- Mandatory inclusion of **AI Quality Management System (QMS)** requirements per EU AI Act Article 17
- Mandatory integration of **Risk Management System (RMS)** per Article 9
- Focus on "freedom from unacceptable risk" per ISO 14971
- Benefit-risk analysis consideration when residual risk cannot be further reduced
- **Traceability** of all design decisions and their risk implications for post-market monitoring

---

## Transparency/Explainability Requirements Mapping to Quality Gates

### Identified Explainability Risks

The paper identifies **two major explainability-related risks**:

1. **Incomprehensible Explanations to the User**
   - Risk Source: Methods/presentation not adapted to user comprehension capacity
   - Consequence: Confusion, misunderstanding, inability to apply results, reduced trust
   - Mitigation: Comprehensible explanation design with user interaction flows

2. **Unfaithful/Unreliable Explanations**
   - Risk Source: Explanation methods fail to accurately reflect true model reasoning
   - Consequence: Misguide stakeholders, harmful lifecycle decisions, eroded trust
   - Mitigation: Validation of explanations (mathematical properties + user understanding)

### Corresponding Best Practices (Risk Controls)

1. **Comprehensible Explanations of Model Output to User**
   - Informative interfaces at multiple complexity levels
   - User interaction flows designed for intended understanding
   - Notification protocols for system updates/changes
   - Domain-specific implementations (e.g., clinical decision support system pop-ups for demographic mismatches)

2. **Preferred Use of Interpretable Models (Ante-hoc)**
   - Intrinsically interpretable models when feasible
   - Examples: decision trees, neural networks with prototype layers
   - Reduces reliance on post-hoc explanation validation
   - Evaluation primarily through model performance metrics

3. **Validate Explanations**
   - **Usability Evaluation** (subjective/qualitative):
     - User surveys, case studies, focus groups
     - Assessed for: parsimony (conciseness), coverage (comprehensiveness), overlap (clarity)
   - **Quality Evaluation** (objective/quantitative):
     - Ground-truth methods (if available)
     - Unsupervised mathematical properties: **fidelity** and **robustness**

### Proposed Explanation Lifecycle Stage

**Three main collection-QG stages:**

1. **Configuration (Leaf-QG)**
   - Metadata and characteristics of ANY explanation method
   - Five defining factors:
     - **Purpose**: Why explanations generated (validate model, assess preprocessing, inform stakeholders, discover insights)
     - **Applicability**: Model-agnostic vs. model-specific
     - **Scope**: Global vs. local explanations
     - **Result**: Form of delivery (text, visualization, statistical summary)
     - **Stage**: Post-hoc vs. ante-hoc

2. **Evaluation (Collection-QG)**
   - **Usability** (subjective): User comprehension and trust assessment
   - **Quality** (objective): Accuracy and reliability of explanations
     - Ground-truth methods
     - Unsupervised mathematical properties (fidelity, robustness)
   - Challenges: Domain-specific constraints, property range, metric integration

3. **User Interaction (Collection-QG)**
   - User interface design
   - User studies and usability testing
   - Stakeholder-specific communication of decision-making process

---

## Formal Decision Logic

### NIST AI RMF Integration

MQG4AI aligns with **NIST AI Risk Management Framework's four steps**:

1. **DEFINE**: Identify risks through collection-QGs, AIROs, TAI criteria
2. **ASSESS**: Evaluate identified risks with respect to impact and likelihood
3. **TREAT**: Implement risk control measures via leaf-QG design decisions
4. **GOVERN**: Monitor through MQG4A-versions, post-market monitoring linkage

### Residual Risk Evaluation

The framework includes explicit evaluation of:
- Residual risk remaining after control measures
- New risks introduced by mitigation strategies
- Benefit-risk trade-off analysis (when residual risk cannot be further reduced)
- Iterative re-assessment across lifecycle phases

### Information Linking Logic

**Bidirectional information flow** between:
- **Upstream**: System context and requirements → Design decisions
- **Downstream**: Design decisions → Risk implications → Monitoring artifacts

Each leaf-QG specifies:
- **Input dependencies**: Which other QGs/system information must be available
- **Output impacts**: Which other lifecycle stages are affected
- **Horizontal interdependencies**: Same structural setting (e.g., model configuration affects explanation robustness)

### Decision Versioning

Multiple MQG4A-versions represent:
- Different design decision combinations
- Iterative refinement of design choices
- Comparison of baseline vs. modified approaches
- Branch structures for validation/testing scenarios

---

## Quality Gate Deliverables/Artifacts

### Information Management Artifacts

Each QG produces structured information artifacts including:

1. **Technical Specifications**
   - Method implementation details
   - Required assumptions and constraints
   - Computational requirements and resource needs

2. **Post-Market Monitoring Inputs**
   - Metrics to track in production
   - Trigger thresholds for re-evaluation
   - Data collection requirements

3. **Risk Documentation**
   - Identified risks and control measures
   - Residual risk assessment
   - Risk acceptability justification

4. **Stakeholder-Specific Representations**
   - Different views for: AI experts, domain experts, regulators, AI users
   - Comprehensiveness vs. accessibility trade-offs

### Fidelity-Robustness Score Artifact Example

The paper demonstrates a concrete leaf-QG deliverable (**QG_FidelityRobustnessScore_(SHAPLIME)**):

**Output Score** (0 to 1 scale):
- **0** = LIME/SHAP explanations not appropriate (cannot trust)
- **>0.8** = good quality (rule of thumb)
- **>0.9** = pretty good quality
- **1.0** = perfect explanations for task

**Calculation Method**:
- **Fidelity component**: Binary (0 or 1) based on sanity checks
  - Model randomization tests
  - Data randomization tests (class label shuffling)
  - Similar feature importance rankings = pass
- **Robustness component**: 0-1 score using NDCG metric
  - Explains generated from slightly different data distributions
  - Measures rank similarity of important features
- **Combined score** = fidelity × robustness

**Triggers**:
- Generated whenever model is retrained
- Integrated into post-market monitoring strategy

---

## EU AI Act Compliance Factoring

### Explicit AI Act Alignment

The paper positions MQG4AI as supporting **Article 17 (AI Quality Management System)** requirements:

#### **13 QMS Aspects Addressed by MQG4AI Structure:**

1. **Risk Management System (RMS)** ✓ (Article 9)
   - Central to MQG4AI design
   - Continuous iteration across lifecycle phases

2. **Data Management** ✓
   - Data lifecycle as component of generic MQG4AI concept
   - Data quality/preprocessing linked to downstream risks

3. **Post-Market Monitoring System (PMMS)** ✓ (Article 72)
   - Leaf-QG output information extraction
   - Links information for real-world monitoring

4. **Strategy for Regulatory Compliance** ✓
   - Configurable system information sections
   - TAI criteria mapping
   - AIRO-based compliance documentation

5. **Design, Design Control, Design Verification** ✓
   - QG structure mirrors design stages
   - Multiple MQG4A-versions test design decisions

6. **Development, Quality Control, Quality Assurance** ✓
   - QG evaluation layers
   - Design decision assessment

7. **Continuous Examination, Test, Validation** ✓
   - MQG4A-versions track evolution
   - Pre/intra/post-selection iterations
   - Continuous validation for data/concept drift detection

8-13. **Remaining aspects** (partially/future work):
   - Reporting serious incidents (Article 73)
   - Communication with authorities
   - Record keeping
   - Resource management
   - Accountability framework
   - Technical specifications

### Risk Categories

EU AI Act's **four-level risk classification**:
- MQG4AI focuses on **high-risk AI** (Category 3)
- Medical/healthcare domain as primary illustration
- Generalizable principles applicable across domains
- Emphasis on "freedom from unacceptable risk" alignment

### Regulatory Implementation Path

The paper envisions MQG4AI as:
- **Bridge** between regulatory text and technical implementation
- **Practical tool** for compliance teams during development
- **Documentation generator** for regulatory submission
- **Interoperable** with existing medical device QMS (ISO 13485)

---

## Empirical Basis

### Empirical Foundation

The framework draws on **retrospective analysis** of:
- Model development processes in medical domain
- Interdependencies during iterative design decision-making
- Performance evaluation methodology refinement

**Referenced empirical study** [11]:
- Reliable performance evaluation metrics for multi-label ECG classification
- Emergency medicine use case (fictional)
- Extracted design decision-making interdependencies
- Ground for MQG4A-version structure (pre-, intra-, post-selection)

### Validation Status

**Current paper**: 
- Conceptual/methodological illustration through Explainability case study
- No full empirical validation of complete MQG4AI framework
- Concrete implementation demonstrated only for one leaf-QG (Fidelity-Robustness Score)
- Paper notes validation pending: "the approach is tested across two different datasets [SVM, MLP, XGBoost models]" for the fidelity-robustness metric specifically

### Future Validation Indicated

Authors explicitly state need for:
- Testing through concrete medical AI projects
- Evaluation of perceived value as practical approach
- Diverse expert contributions to refine all sections
- Software development toward operational implementation

---

## KEY QUOTES (Verbatim with Page Numbers)

### Framework Definition

> "MQG4AI's decentralized, and adaptable character is intended to respond to AI's novelty, inherent dynamics, and use case-specificity, so that methods for implementation can be structured, and continuously stay up-to-date – including future contributions." (p. 16)

### Information Management Principle

> "The purpose of the [IM] process is to generate, obtain, confirm, transform, retain, retrieve, disseminate, and dispose of information, to designated stakeholders. The [IM] process plans, executes, and controls the provision of unambiguous, complete, verifiable, consistent, modifiable, traceable, and presentable information to designated stakeholders." (p. 4, citing ISO 5338:2023)

### Quality Gates Foundation

> "Quality Gates (QG) along the AI lifecycle are at the core of the MQG4AI information structure, drawing from traditional software engineering and product development practices. Generally, QGs '[...] structure a process chain into phases and allow a periodical review of the process quality' [19, 206], reflecting a decision point within a project [14, 245], and ensuring consistent assessment and control of quality at various stages." (p. 6)

### Risk-Based Approach

> "Risk is interpreted as '[...] the combination of the probability of an occurrence of harm and the severity of that harm' in Article 3 [13]." (p. 2, EU AI Act definition)

### Transparency/Explainability Risks

> "Incomprehensible Explanations to the User: This risk arises when the methods of explanation and their presentation are not adapted to the user's capacity of comprehension confusion and misunderstanding. Explanations that are too vague, overly complex or are not well framed may prevent the user from understanding the model's reasoning on how to apply the results in a particular context, which may reduce trust in the system." (p. 9)

> "Unfaithful or Unreliable Explanations: This risk arises when explanation methods fail to accurately reflect a model's true reasoning, leading to misunderstandings of its decisions. Such explanations can misguide stakeholders, resulting in harmful actions throughout its lifecycle and eroding trust in the system." (p. 9)

### Best Practice Integration

> "The flip side of these risks are best practices, which support designing the intelligent system in a way that automatically mitigates risks. Linking best practices and risks highlights the interdependencies for monitoring risk controls." (p. 9-10)

### Ante-hoc Explainability Advantage

> "Ante-hoc models are intrinsically interpretable models designed to provide clear insights into their decision-making processes without relying on post-hoc explanation techniques. These models include models with simple decision boundaries, such as decision trees, and more complex ones with interpretability enhancements, like neural networks with prototype layers." (p. 10)

### Explanation Evaluation Complexity

> "The evaluation process is not without challenges. It is complex due to domain-specific constraints, the broad range of properties that can be evaluated, and the difficulty in integrating case-specific metrics. Additionally, the lack of generalizable methods for automating this evaluation further complicates the task [4]." (p. 11)

### Fidelity-Robustness Scoring Rationale

> "As noted by [30], explanations lacking fidelity risk misleading users by creating a false sense of understanding. To address this concern, the application-oriented contribution introduces a unified quality score that evaluates fidelity and robustness simultaneously, ensuring a more thorough assessment." (p. 14)

### Fidelity Definition

> "Fidelity evaluation outputs a score of either 0 or 1, and robustness evaluation a value between 0 and 1, both being afterwards combined by the multiplication operation." (p. 14)

### IEEE XAI Framework Alignment

> "Overall, our approach aligns with the IEEE guidelines and offers comprehensive mechanisms to address all relevant processes for achieving explainability, as detailed in this section." (p. 12)

### Post-Market Monitoring Output

> "A score of 0 indicates that LIME/SHAP explanations are not appropriate for the task, and should not be trusted, whereas a score of 1 indicates that LIME/SHAP explanations are perfect for the task, and any score in between can suggest that explanations are either appropriate or not. For the last cases, a suggested rule of thumb is that everything above 0.8 is good, and above 0.9 is pretty good." (p. 14)

### Lifecycle Planning Objective

> "Overall, we aim to contribute a generic and customizable methodology, that could be implemented as a tool, towards facilitating AI QM, as explained in the following sections." (p. 3)

---

## Relevance for D_GATE_INCLUSION_RULE

### Mapping to Dimension Framework

Based on the paper's structure and focus, MQG4AI serves the following dimensions:

#### **D1 (Responsibility/Governance Dimension)**
- ✓ **STRONG**: Entire framework centers on responsible AI through lifecycle-wide governance
- Links design decisions to ethical requirements and regulatory compliance
- Stakeholder role stratification (active, consulting, passive) addresses governance structure
- Knowledge management process for RAI literacy (Article 4, EU AI Act)

#### **D2 (Quality/Trustworthiness Dimension)**
- ✓ **STRONG**: Core focus on AI Quality Management System (Article 17)
- Integration of seven TAI criteria throughout lifecycle
- Quality gates as explicit quality assurance checkpoints
- Post-market monitoring linkage for continuous quality

#### **D3 (Transparency/Explainability Dimension)**
- ✓ **VERY STRONG** (explicit paper focus): Detailed illustration through Explanation lifecycle stage
- Two explainability risks and three mitigation best practices
- Concrete leaf-QG for explanation quality assessment (Fidelity-Robustness Score)
- Alignment with IEEE XAI Framework across content/communication/stakeholders

#### **Q (Quantification/Metrics Dimension)**
- ✓ **MODERATE-TO-STRONG**: 
  - Quantitative metrics for explanation quality (0-1 fidelity-robustness score)
  - Mathematical properties evaluation (NDCG for rank similarity)
  - TAI criteria mapped to measurable QG outcomes
  - Scoring systems for stakeholder-specific dimensions (e.g., participation score)
  - **Gap**: Limited guidance for quantifying other TAI criteria (fairness, diversity, societal well-being)

### Specific D_GATE Contribution

MQG4AI directly supports **D_GATE_INCLUSION_RULE** by:

1. **Formalized Gate Structure**: Clear collection-QG and leaf-QG hierarchy enables gate definition
2. **Risk-Based Gate Criteria**: Each gate linked to identified AI risks and control measures
3. **Quantifiable Gate Outputs**: Leaf-QGs produce measurable artifacts (fidelity-robustness scores, monitoring metrics)
4. **Lifecycle Integration**: Gates positioned across all six lifecycle phases with interdependency mapping
5. **Stakeholder-Specific Communication**: Gate information tailored for different stakeholder views (satisfies communication aspect of gates)

---

## Comparison to Elia 2023 (Evolution)

### Elia 2023 Foundation

Paper references Elia & Bauer (2023): **"A methodology based on quality gates for certifiable AI in medicine: towards a reliable application of metrics in machine learning"** [10]

### Evolution from 2023 to 2025

#### **Scope Expansion**
- **2023**: Focus on medical AI certification through quality gates
- **2025**: Generic framework applicable across domains; medical used as illustration
- **2023**: Emphasized metrics reliability for performance evaluation
- **2025**: Extended to comprehensive AI lifecycle planning (conceptualization through decommissioning)

#### **Framework Maturation**
- **2023**: Initial QG concept for AI medicine
- **2025**: Formalized QG types (collection-QGs, leaf-QGs) with hierarchical structure
- **2023**: Implied lifecycle stages
- **2025**: Explicit six-stage lifecycle model with detailed phase definitions

#### **Knowledge Management Addition**
- **2023**: Not explicitly emphasized
- **2025**: Central principle—dual MQG4DK/MQG4A interaction scenarios for continuous RAI knowledge evolution

#### **Regulatory Alignment**
- **2023**: Medical device regulations (ISO 14971) focus
- **2025**: Comprehensive EU AI Act mapping (Article 9, 17, 72, 73 explicitly addressed)
- **2025**: NIST AI RMF, AIRO, and ISO 5338/42001 integration

#### **Explainability Detail**
- **2023**: Referenced in broader context
- **2025**: Dedicated Section 4 with detailed explanation lifecycle, specific risks/best practices, concrete scoring method

#### **Empirical Grounding**
- **2023**: Based on multi-label ECG classification use case
- **2025**: References updated empirical studies on XAI transferability [30], extends design decision-making framework

#### **Tool Perspective**
- **2023**: Methodology conceptualization
- **2025**: GitHub repository implementation, software development roadmap articulated

### Continuity
- **QG concept**: Core principle maintained and expanded
- **Medical domain**: Still primary illustration, but explicitly generalized
- **Risk-based approach**: Strengthened through formal RM processes (DEFINE/ASSESS/TREAT/GOVERN)
- **Lifecycle focus**: Deepened from certification point-of-view to holistic lifecycle planning

---

## Gaps and Limitations

### Explicitly Acknowledged Limitations

1. **Incomplete Framework**
   > "The present contribution outlines our proposed template-design workflow to enable decentralized contributions, since finalizing the template is an immense endeavor, and we believe novel AI knowledge will never stop." (p. 1)

2. **Partial QMS Coverage**
   - Currently focuses on AI RMS (Risk Management System)
   - Additional QMS aspects acknowledged as future work
   - Data Management section structure outlined but not fully detailed
   - Remaining QMS aspects (technical specifications, incident reporting, etc.) partially addressed

3. **Limited Empirical Validation**
   - No full framework validation on complete projects
   - Fidelity-robustness metric tested on only "two different datasets [SVM, MLP, XGBoost]"
   - Explanation lifecycle validated only conceptually against IEEE framework
   - MQG4A-version structure derived from single emergency medicine use case

4. **Explainability Scope**
   - Focus on feature importance explanations (SHAP/LIME)
   - May not apply equally to other explanation methods
   - Domain-specific constraint acknowledgment but limited mitigation strategies provided

5. **Sofware Development Status**
   > "Additionally, the current implementation on GitHub needs further development towards becoming a software that can be utilized. For instance, automating bidirectional information linking and creating an intelligent search feature to retrieve configurable MQG4AI-versions based on leaf QG-tags are essential improvements." (p. 17)
   - GitHub repository is template/conceptual, not operational software
   - Lacks automation for information linking
   - Lacks intelligent tag-based QG search

### Inherent Tensions and Trade-offs

1. **Generalizability vs. Specificity**
   - Generic lifecycle structure may oversimplify domain-specific complexities
   - Customization flexibility could lead to inconsistent implementations
   - No clear guidance on when to prioritize generic vs. domain-specific gates

2. **Explainability-Performance Trade-off**
   - Acknowledged but not systematically addressed
   - Best practice for ante-hoc models may sacrifice performance
   - No quantitative framework for balancing trade-offs

3. **Stakeholder Role Coordination**
   - Active/consulting/passive stratification could create information silos
   - Communication protocols between stakeholder tiers not specified
   - Potential for role confusion in interdependent decisions

4. **Evaluation Subjectivity**
   - User/usability evaluation relies on qualitative methods (surveys, focus groups)
   - Subjectivity in gate pass/fail decisions unclear
   - No explicit calibration process for evaluation criteria

### Research Gaps Identified

1. **Ante-hoc vs. Post-hoc Integration**
   - Paper notes most current AI algorithms use post-hoc methods
   - Strategy for transitioning to ante-hoc approaches underspecified
   - Limited guidance on hybrid approaches

2. **Fair Representation and Diversity**
   - TAI criterion "Diversity, non-discrimination, fairness" addressed only indirectly
   - No specific QG structures proposed for fairness evaluation
   - Societal well-being criterion similarly underdeveloped

3. **Iterative Refinement Mechanisms**
   - MQG4A-version structure proposed but implementation details sparse
   - Merge criteria from parallel branches unclear
   - Conflict resolution between competing design decisions undefined

4. **Organizational Adoption**
   - Framework assumes certain organizational maturity
   - Resource requirements not quantified
   - Change management for integrating new QMS not addressed

### Missing from Current Paper

1. **Quantitative Cost-Benefit Analysis**
   - Implementation effort/resource requirements not estimated
   - ROI/value proposition not established

2. **Comparative Analysis with Alternatives**
   - Other AI QMS frameworks mentioned briefly but not compared in depth
   - Clear differentiation points vs. ISO/IEC 42001, NIST RMF limited

3. **Failure Mode Analysis**
   - What happens when QG criteria not met?
   - Decision logic for "gate failure" outcomes not provided

4. **Real-World Case Studies**
   - No demonstration on actual medical AI projects
   - No implementation timeline or resource data

---

## References and Key Concepts

### Foundational Frameworks Integrated

- **EU AI Act (2024)** – Article 9, 17, 72, 73; four-level risk classification
- **NIST AI Risk Management Framework (RMF)** – DEFINE/ASSESS/TREAT/GOVERN structure
- **ALTAI Assessment List** – Seven trustworthiness criteria
- **AI Risk Ontology (AIRO)** – System information extraction
- **ISO/IEC 5338:2023** – AI system lifecycle processes
- **ISO/IEC 42001:2023** – AI Management Systems
- **ISO 14971:2019** – Medical device risk management
- **ISO 13485:2016** – Medical device quality management
- **IEEE 2894-2024** – Guide for Explainable AI framework

### XAI-Specific References

- **SHAP and LIME** – Model-agnostic explanation methods
- **Fidelity and Robustness** – Core explanation quality metrics
- **Sanity Checks** – Randomization tests for explanation validity
- **NDCG (Normalized Discounted Cumulative Gain)** – Rank similarity metric

---

## Final Assessment

### Strengths

1. **Comprehensive Integration**: Successfully bridges regulatory requirements, technical implementation, and organizational governance through unified IM/KM framework

2. **Practical Operationalization**: Moves beyond abstract principles to concrete leaf-QG templates with measurable deliverables

3. **Lifecycle Holism**: Addresses all phases from conceptualization through decommissioning, not just development

4. **Flexibility by Design**: Generic collection-QG/leaf-QG architecture enables domain and use-case adaptation

5. **Transparent Risk Linkage**: Explicitly connects design decisions to identified risks and risk controls

6. **Standards Alignment**: Maps to multiple regulatory frameworks (EU AI Act, NIST, ISO standards) simultaneously

7. **Knowledge Evolution**: MQG4DK/MQG4A dual structure enables continuous improvement and decentralized contribution

### Limitations

1. **Incomplete Implementation**: Framework is conceptual with limited operational software; GitHub is template repository only

2. **Validation Gap**: No empirical demonstration on complete AI project; only single leaf-QG metric validation (fidelity-robustness)

3. **Partial QMS Coverage**: Risk management emphasized; data management, post-market monitoring, incident reporting less developed

4. **Explainability Scope Narrowness**: Detailed only for feature importance methods (SHAP/LIME); generalizability to other explanation types unclear

5. **Organizational Readiness Assumptions**: Framework assumes organizational capacity for multi-stakeholder coordination; adoption barriers not addressed

### Value Proposition

MQG4AI provides:
- **For Researchers**: Operationalized framework for RAI implementation and testing
- **For Regulators**: Demonstrated path to EU AI Act compliance through lifecycle planning
- **For Practitioners**: Structured approach to quality gate definition and risk-based decision-making
- **For Standards Bodies**: Template for future standardization in AI QMS

### Recommended Reading Path

1. **Overview**: Abstract, Introduction, Conclusion (5 min)
2. **Framework Architecture**: Section 3 (MQG4AI Setup) + Figure 1-3 (10 min)
3. **QG Structure**: Section 3.3 (Leaf-QG and Collection-QG details) + Figures 5-7 (15 min)
4. **Application Example**: Section 4-5 (Explainability case study) + Figures 6-7 (20 min)
5. **Regulatory Alignment**: Section 6 (Discussion) (10 min)

---

**Document Generated**: 2026-03-12  
**Paper Status**: Preprint, under journal review  
**Total Paper Length**: 18 pages  
**Key Finding**: MQG4AI represents significant evolution from prior work toward operationalized RAI implementation through structured quality gates, with strong regulatory alignment but requiring empirical validation and software development for practical deployment.

---

## APPENDIX: Quick Reference Tables

### Table 1: MQG4AI vs. Elia 2023 - Key Evolution Dimensions

| Dimension | Elia 2023 | Elia 2025 | Evolution |
|-----------|-----------|----------|-----------|
| **Scope** | Medical AI certification | Generic + medical illustration | Domain agnostic |
| **Core Focus** | Performance metrics reliability | Complete AI lifecycle planning | Holistic quality management |
| **Lifecycle Phases** | Implied | Six explicit phases + iterations | Detailed stage definitions |
| **Framework Type** | Medical device-specific | Generic + customizable | Interoperable with ISO standards |
| **Knowledge Management** | Implicit | Explicit dual MQG4DK/MQG4A | Continuous evolution mechanism |
| **Regulatory Basis** | ISO 14971 (medical devices) | EU AI Act + NIST RMF + ISO | Multi-framework alignment |
| **Explainability Detail** | Mentioned | Detailed (Section 4-5, concrete metrics) | Operationalized with scoring |
| **Gate Hierarchy** | Simple structure | Collection-QGs + Leaf-QGs | Formal taxonomy |
| **Empirical Base** | ECG classification study | Extended + XAI studies | Broader evidence base |

### Table 2: Six AI Lifecycle Phases in MQG4AI

| Phase | Focus | Key Activities | Output to Next Phase |
|-------|-------|----------------|---------------------|
| **Conceptualization** | Business requirements, feasibility | Inception, system requirements, business analysis | MQG4AI contextual blocks populated |
| **Data** | Data quality, preprocessing | Quality assessment, transformation decisions, design choices | Data quality artifacts, preprocessing specs |
| **Development** | Model creation, evaluation, refinement | Configuration, evaluation, optimization iterations | Trained model, performance metrics, risk assessments |
| **Deployment** | Real-world integration | Environment adaptation, pipeline integration | Deployment specifications, monitoring parameters |
| **Maintenance** | Continuous validation, monitoring | Data drift detection, re-evaluation, concept drift monitoring | Updated models, monitoring reports |
| **Decommissioning** | Model retirement | Replacement decisions, system retrieval | Legacy documentation, retirement records |

### Table 3: Explainability Risk-Control Mapping

| Identified Risk | Risk Source | Consequence | Best Practice Control | Measurement Method |
|-----------------|-------------|-------------|---------------------|-------------------|
| **Incomprehensible Explanations to User** | Methods/presentation not adapted to comprehension | Confusion, reduced trust, inability to apply results | Design user-adapted interfaces, interaction flows, notification protocols | Usability testing, user surveys (qualitative) |
| **Unfaithful/Unreliable Explanations** | Explanation methods don't reflect true reasoning | Misguidance, harmful decisions, eroded trust | Prefer ante-hoc models; validate explanations (fidelity + robustness) | Sanity checks, mathematical properties (quantitative) |

### Table 4: Seven TAI Criteria and XAI Integration

| TAI Criterion | Definition | XAI Integration | MQG4AI Coverage |
|---------------|-----------|-----------------|-----------------|
| **Human Agency & Oversight** | Human control and monitoring | Explanations enable informed human decision-making | Implicit (stakeholder role design) |
| **Technical Robustness & Safety** | Reliable, predictable systems | Robustness of explanation methods tested | **Strong** (Robustness metric in Fidelity-Robustness Score) |
| **Privacy & Data Governance** | Data protection and quality | Explanation linkage to data preprocessing/quality | Moderate (data lifecycle referenced) |
| **Transparency** | System functioning clarity | **Core of explainability effort** | **Very Strong** (detailed Explanation lifecycle) |
| **Diversity, Non-Discrimination, Fairness** | Equitable outcomes | Explanations reveal potential bias sources | Limited (identified as gap) |
| **Societal & Environmental Well-being** | Broader impact considerations | Explanations support impact assessment | Limited (identified as gap) |
| **Accountability** | Responsibility assignment | Explanation documentation for traceability | Moderate (information linking structure) |

### Table 5: Leaf-QG Template Information Layers

| Layer | Purpose | Questions Answered | Stakeholder Use |
|-------|---------|-------------------|-----------------|
| **Input Information** | Define requirements from other lifecycle stages | What information is necessary to execute the method? | Development planners, domain experts |
| **Output Information** | Define impacts on other stages/monitoring | Which stages are impacted? What monitoring data needed? | Post-market monitoring teams, regulators |
| **Content Dimension** | Technical detail of design decision | How does this design decision work technically? | AI experts, data scientists |
| **Method Dimension** | Implementation process details | How do we implement this design decision? | Implementation teams, quality assurance |
| **Representation Dimension** | Stakeholder-specific communication | How is this presented to different audiences? | Active: AI experts; Consulting: domain experts; Passive: regulators, users |
| **Evaluation Layer** | Critical assessment of approach | What are limitations, drawbacks, open questions? | Risk assessment teams, quality reviewers |
| **Risk Management Layer** | Link to risk controls | Which AI risks does this control? What residual risks remain? | Risk managers, compliance officers |

### Table 6: Fidelity-Robustness Score Calculation

| Component | Definition | Calculation Method | Output Range | Interpretation |
|-----------|-----------|-------------------|---------------|-----------------|
| **Fidelity** | Do explanations capture true model reasoning? | Sanity checks: model randomization + data randomization tests | 0 or 1 (binary) | 0 = failed sanity checks; 1 = passed |
| **Robustness** | Do explanations remain consistent with data distribution changes? | NDCG metric on feature importance rank similarity across data splits | 0 to 1 (continuous) | 0 = very unstable; 1 = completely stable |
| **Combined Score** | Overall explanation quality | Fidelity × Robustness | 0 to 1 | <0.8: questionable; ≥0.8: good; ≥0.9: pretty good |

### Table 7: MQG4AI Coverage of EU AI Act Article 17 (QMS) Requirements

| QMS Aspect | Article | MQG4AI Coverage | Status |
|-----------|---------|-----------------|--------|
| Risk Management System | 9 | ✓ Central to design | **Strong** |
| Data Management | 17.1(c) | ✓ Data phase included | **Moderate** |
| Post-Market Monitoring System | 72 | ✓ Output information linkage | **Strong** |
| Regulatory Compliance Strategy | 17.1(a) | ✓ AIRO-based system information | **Strong** |
| Design, Design Control, Verification | 17.1(b) | ✓ QG structure mirrors design phases | **Strong** |
| Development, QC, QA | 17.1(b) | ✓ MQG4A-versions test iterations | **Strong** |
| Continuous Examination, Test, Validation | 17.1(d) | ✓ Multiple MQG4A-versions | **Strong** |
| Technical Specifications | 17.1(e) | ✓ Leaf-QG output information | **Moderate** |
| Serious Incident Reporting | 73 | ~ Envisioned in framework | **Future Work** |
| Authority Communication | 17.1(h) | ~ Documentation structure supports | **Future Work** |
| Record Keeping | 17.1(f) | ✓ Information management designed | **Moderate** |
| Resource Management | 17.1(i) | ~ Not explicitly addressed | **Limited** |
| Accountability Framework | 17.1(j) | ✓ Information traceability | **Moderate** |

### Table 8: Proposed XAI Configuration Decision Factors

| Factor | Definition | Choices | Impact |
|--------|-----------|---------|--------|
| **Purpose** | Why are explanations generated? | Validate model; Assess preprocessing; Inform stakeholders; Discover insights | Determines evaluation strategy |
| **Applicability** | Is method tailored to model type? | Model-agnostic; Model-specific | Affects computational resources & flexibility |
| **Scope** | Breadth of explanation coverage | Global (entire model); Local (individual predictions) | Affects detail level & stakeholder needs |
| **Result** | Form of explanation delivery | Text; Visualization; Statistical summary | Audience comprehension and actionability |
| **Stage** | When are explanations generated relative to model development? | Post-hoc (after training); Ante-hoc (during/integrated in training) | Affects validation intensity required |

---

## APPENDIX: Key Document Locations

**Primary Paper:**
- Multiple locations in thesis repository:
  - `/sessions/friendly-quirky-goodall/mnt/genaiops-thesis/00_admin/Literatur/SSOT_GLIEDERUNG_CLUSTER_2026-03-07/98_Taglogik_Relevanz/REL_ROT_CORE/Elia - 2025 - MQG4AI Towards Responsible High-Risk AI Transparency and Explainability.pdf`
  - `02_05_Quality_Gates_Definition_Konzepte_Einordnung/` (same filename)
  - `04_06_Requirements_Katalog_Traceability/` (same filename)
  - `02_07_Synthese_Forschungsluecke_und_Handlungsbedarf/` (same filename)

**GitHub Repository:**
- https://github.com/miriamelia/MQG4AI (template implementation, currently under development)

**Deep Reading Analysis:**
- `/sessions/friendly-quirky-goodall/mnt/genaiops-thesis/05_referenzarchitektur_RQ2/DEEP_READING_ELIA_2025.md`

---

## APPENDIX: Citation Format

**Standard Citation:**
Elia, M., Lopez, A.M., Corredor Páez, K.A., Bauer, B., & Garcia-Cuesta, E. (2025). MQG4AI: Towards responsible high-risk AI – illustrated for transparency focusing on explainability techniques. *Preprint submitted for journal review*.

**Bibtex:**
```bibtex
@article{elia2025mqg4ai,
  author = {Elia, Miriam and Lopez, Alba Maria and Corredor P\'{a}ez, Katherin Alexandra and Bauer, Bernhard and Garcia-Cuesta, Esteban},
  title = {{MQG}4{AI}: Towards responsible high-risk {AI} -- illustrated for transparency focusing on explainability techniques},
  note = {Preprint submitted for journal review},
  year = {2025}
}
```

