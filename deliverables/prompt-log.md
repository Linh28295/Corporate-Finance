# BUS 629 Project Prompt Log

**Student:** Nguyen Bui Ngoc Linh  
**Company:** The Coca-Cola Company (KO: NYSE)  
**LLM:** Claude (claude-sonnet-4-6) via Claude Code  

---

| Date | Stage | Prompt | LLM Output | Files Created / Modified |
|------|-------|--------|-----------|--------------------------|
| 2026-05-10 | 0 | "check requirements (BIO, RESUME, CV) of Github of BUS 629, make it correct" | Audited repo; identified missing/wrong files | BIO.md, RESUME.md, README.md, LICENSE, _course-docs/, deleted BIO/RESUME/README |
| 2026-05-10 | 1 | "can you help to do the stage 1 assignment" | Template upload guidance; created skeleton | models/templates/README.md, models/builds/README.md, docs/README.md, analysis/README.md |
| 2026-05-10 | 2 | "move to stage 2" | Drafted company selection memo for Coca-Cola | docs/decisions/2026-05-10-nguyen-coca-cola-selection.md |
| 2026-05-10 | 3 | "stage 3" | Provided data population guidance | analysis/validation/2026-05-10-coca-cola-stage3-data-guide.md |
| 2026-05-10 | 3 | "@coca_cola_mergent.xlsx data here" | Extracted all FY2025 + FY2024 figures from Mergent | analysis/validation/2026-05-10-coca-cola-financials-data-reference.md, data/nguyen/sources.md |
| 2026-05-10 | 3 | "Nope, should be 2025 current and 2024 prior" | Corrected years throughout | Updated Stage 2 memo + data reference |
| 2026-05-10 | 0 | "check stage 0 feedback [98.22%]" | Fixed 3 instructor deductions | README trimmed to 2-sentence bio, _course-docs/ restructure, orphan files deleted |
| 2026-05-10 | 2 | "check stage 2 feedback [92%]" | Fixed 4 instructor deductions | Audience → Managing Director, exec summary close strengthened, H3 falsifiable, straight ASCII quotes |
| 2026-05-16 | 3 | "check stage 3 again and compare to requirements" | Full rubric audit; 3 gaps found and fixed | Cover tab student documentation, source URL, CFO reconciliation note, 29 ratio formulas, file renamed |
| 2026-05-16 | 4 | "stage 4 please" | Drafted 11-section technical specification | docs/specs/2026-05-16-nguyen-coca-cola-spec.md, docs/specs/2026-05-16-nguyen-coca-cola-prompt-log.md |
| 2026-05-16 | 5 | "sure" | Executed spec; raw + evaluated analysis | deliverables/2026-05-16-coca-cola-llm-raw.md, deliverables/2026-05-16-coca-cola-final-analysis.md |

---

## Reflection on LLM-assisted workflow

The spec-driven approach in BUS 629 mirrors professional analyst practice: a precise specification precedes execution, and the specification's quality determines the output's quality. The prompt log above shows that early prompts ("stage 3", "move to stage 2") were terse — the LLM compensated by drawing on session context. By Stage 4, the process inverted: the spec became the prompt, and output quality improved markedly because expectations were fully quantified in advance.

The most valuable LLM contributions were computational (named range population, balance checks, formula verification) and structural (YAML frontmatter, directory conventions, named range mapping). The most important human contributions were directional (selecting Coca-Cola, setting the three hypotheses, approving outputs, providing Mergent data) and evaluative (identifying the EBIT definitional mismatch, the CFO reconciliation gap, and the year correction from FY2023/2024 to FY2024/2025).
