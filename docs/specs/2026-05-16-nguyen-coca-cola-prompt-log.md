---
purpose: Prompt log for Stage 4 LLM-drafted technical specification
author: Nguyen Bui Ngoc Linh
spec-file: 2026-05-16-nguyen-coca-cola-spec.md
date: 2026-05-16
---

# Prompt Log — Stage 4 Technical Specification

**Company:** The Coca-Cola Company (KO)  
**LLM used:** Claude (claude-sonnet-4-6) via Claude Code  
**Session:** BUS-629 Stage 4 work session  

---

## Prompt 1 — Spec generation

**Intent:** Generate a complete 11-section technical specification for the Coca-Cola ratio model built in Stage 3, precise enough that a separate LLM instance can execute the Stage 5 analysis with no prior context.

**Prompt submitted:**

> Stage 4 please

**Context provided to the LLM at time of prompt:**
- Stage 3 Excel workbook: `models/builds/2026-05-10-coca-cola-financials.xlsx` (fully populated)
- Financial data reference: `analysis/validation/2026-05-10-coca-cola-financials-data-reference.md`
- Stage 3 data guide: `analysis/validation/2026-05-10-coca-cola-stage3-data-guide.md`
- Stage 2 memo with three hypotheses: `docs/decisions/2026-05-10-nguyen-coca-cola-selection.md`
- Stage 4 requirements: `_course-docs/stage4-technical-specification.md`
- All named ranges confirmed populated (0 empty cells, verified programmatically)
- Balance Sheet checks confirmed: FY2025 104,816 = 104,816; FY2024 100,549 = 100,549

**Output produced:** `docs/specs/2026-05-16-nguyen-coca-cola-spec.md` (this file's companion)

**LLM design decisions and rationale:**

| Decision | Rationale |
|----------|-----------|
| Expected ratio values included in spec | Enables the Stage 5 LLM to validate its computation against known-good anchors, not just check formulas exist |
| Time-period mismatch documented in Sections 6f and 9 | The Du Pont ROE ≠ direct ROE is a structural model feature, not a bug; must be explained not hidden |
| CFO reconciliation note in Section 3d | Template CFO ($5,181M) differs from reported CFO ($7,408M) by $2,227M; Stage 5 LLM needs this to avoid misquoting the cash flow figure |
| H3 phrasing directed to compare model result vs Mergent benchmark | The model uses prior-year assets as asset turnover denominator (0.477x) vs Mergent's own ratio (0.457x); both show decline from FY2024 0.468x, confirming H3 |
| Output format specifies exact file path | Prevents Stage 5 deliverable from landing in the wrong directory |
| Validation rules V1–V8 required before analysis proceeds | Forces the Stage 5 LLM to confirm data integrity before writing narrative — prevents analysis built on a broken model |

---

## Self-assessment of spec quality

| Rubric criterion | Self-score | Notes |
|-----------------|-----------|-------|
| Model spec — Data & Structure (Part A items 1–5) | Strong | All 90 named ranges tabulated with numerical values; architecture table maps all 6 tabs |
| Model spec — Ratios & Validation (Part A items 6–7) | Strong | All 29 ratio formulas stated with expected values; 8 validation rules with numeric pass conditions |
| Analysis spec (Part B items 8–11) | Strong | Three hypotheses with verdict framework; Du Pont with 4-step reconciliation requirement; output format specifies exact file path and length target |
| Spec craft + prompt log quality | Adequate | Prompt was terse ("stage 4 please") but rich context was available in-session; this log documents the intent and design choices that a bare prompt does not convey |

**Limitation to note:** The prompt submitted ("stage 4 please") is minimal. In a production spec-driven workflow, the prompt would explicitly enumerate the 11 required sections and state the output file path. The richness here came from the LLM's session context rather than the prompt itself. For Stage 5, the prompt to the executing LLM should be the spec document itself, not a conversational directive.
