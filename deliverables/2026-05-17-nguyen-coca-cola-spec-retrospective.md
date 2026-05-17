---
template: spec-retrospective
purpose: Structured self-evaluation of the Stage 4 spec — verdict, gaps, revisions, effectiveness rating
audience: Stage 5 grader
stage: 5-retrospective
author: Nguyen Bui Ngoc Linh
company: The Coca-Cola Company (KO: NYSE)
date: 2026-05-17
spec-file: docs/specs/2026-05-16-nguyen-coca-cola-spec.md (revised 2026-05-17)
stage5-llm-output: deliverables/2026-05-16-nguyen-coca-cola-llm-raw.md
stage5-final-analysis: deliverables/2026-05-16-nguyen-coca-cola-final-analysis.md
---

# Stage 4 Spec Retrospective — Coca-Cola FY2025

## 1. Section-by-section verdict

| Spec section | Verdict | Symptom in Stage 5 output |
|---|---|---|
| **A.1 Scope & Objective** | Vague (pre-revision) | LLM never named the reporting standard literally; delivered narrative recommendations instead of a 3–5 numbered list. Cause: §1 said "Deliver a strategic recommendation" (singular, vague count) and didn't surface "U.S. GAAP" as a literal. Revised on 2026-05-17 to specify 3–5 recommendations + U.S. GAAP / USD / FYE / audience tags. |
| **A.2 Model Architecture** | Vague (pre-revision) | LLM's architecture narrative never referenced color coding even though the workbook uses Yellow/Blue/Green/Gray. Cause: §2 had no styling convention table. Revised to add the four-row color-coding table. |
| **A.3 Data Inputs** | Clear | All ~40 numerical inputs were provided with named-range labels. LLM reproduced values without lookup errors. One late addition: `CF_depreciation_amortization` added to §3d on 2026-05-17 after Stage 3 instructor feedback. |
| **A.4 Named Range Conventions** | Clear | Six prefix patterns (`BAL_`, `INC_`, `CASH_`, `startYear_`, `currentYear_`, `RATIO_`) plus a worked example for each. No LLM confusion on naming. |
| **A.5 Derived Inputs** | Clear | After-tax operating income formula (`INC_net + (1 − tax_rate) × INC_interest_expense`) was correctly applied; LLM produced 14,495.26 in line with manual recomputation. |
| **A.6 Ratio Definitions & Formulas** | Vague (pre-revision) | LLM reported ratio values but interpretation was thin — "MVA $266,458M" had no anchor for whether that magnitude is healthy. Cause: §6 listed Expected FY2025 values but no "high signals / low signals" guide per category. Revised to add §6g interpretation guide. |
| **A.7 Validation Rules** | Vague (pre-revision) | LLM correctly handled Du Pont ROE mismatch because §6f had a callout, but §7 had no V-rule for it (only V5 covered Du Pont ROA). A future Stage 5 executor running on a colder spec could treat the gap as a model defect. Revised to add V9 (Du Pont ROE reconciliation, not equality). |
| **B.8 Analysis Requirements** | Clear | Three pre-stated hypotheses with CONFIRMED/REJECTED/INCONCLUSIVE verdict requirement worked exactly as intended; all three were evaluated against quantitative thresholds. |
| **B.9 Du Pont Decomposition** | Clear | Explicit instruction to reconcile Du Pont ROE vs. direct ROE produced the right output (LLM identified the time-period denominator mismatch and explained it). |
| **B.10 Strategic Recommendation Requirements** | Vague | The spec said "3–5 recommendations with evidence standards" but did not enforce an output format. LLM delivered narrative paragraphs labelled as "recommendation"; final analysis re-shaped these into numbered, evidence-cited items with per-item LLM assessment. Worst-graded section of the spec. |
| **B.11 Output Format** | Clear | Required sections, length targets, tone (Managing Director audience) all reflected in raw output. |

---

## 2. Top three gaps with evidence

### Gap 1 — Strategic recommendations under-specified for output structure

- **Where it surfaced:** Stage 5 raw output `deliverables/2026-05-16-nguyen-coca-cola-llm-raw.md` — the "Strategic Recommendations" section delivered three narrative paragraphs; the count was OK (3–5) but the format was prose, not a numbered list with explicit evidence cells and counter-risk per item.
- **Spec cause:** §B.10 said "3–5 recommendations, each with data support (cite specific ratio values) and actionable specificity (who does what by when)" — the *content* requirements were correct, but the *form* (numbered, structured, with sub-fields) was not enforced.
- **Fix (exact spec language to add):** Insert under §B.10: *"Format each recommendation as a numbered block with four labelled sub-fields: **Recommendation** (one sentence), **Evidence** (named-range values, ≥2 cited), **Counter-risk** (one sentence on what could falsify it), **Owner / horizon** (who acts, by when). Narrative paragraphs without these sub-fields do not satisfy the rubric."*

### Gap 2 — EBIT definitional mismatch never flagged in spec

- **Where it surfaced:** TIE calculation in the LLM raw output (8.45x). The numerator `INC_ebit` is the workbook's formula-computed EBIT ($13,973M = Sales − COGS − SGA − D&A), which excludes Unusual Expense ($582M) and Other Operating Expenses ($47M) that the 10-K rolls into operating income ($14,394M). Gap of $421M (3%).
- **Spec cause:** §A.3 listed `INC_ebit` with the formula in parentheses but never explained that this is a *simplified* EBIT and that the 10-K reports a different operating-income line. The spec didn't ask the LLM to reconcile.
- **Fix:** Under §A.3a, add a note immediately under the `INC_ebit` row: *"Note: Model EBIT excludes Unusual Expense and Other Operating Expenses, which the 10-K reports inside operating income. 10-K operating income FY2025 = $14,394M; model EBIT = $13,973M; $421M gap. Use model EBIT consistently in this analysis; flag the reconciliation in TIE commentary."*

### Gap 3 — No stress test or capital-deployment recommendation instruction

- **Where it surfaced:** Leverage section of the raw output declared D/E 1.41x and TIE 8.45x "manageable" without quantifying what a downside scenario looks like (e.g., 20% EBIT drop → TIE under what threshold). Strong liquidity was noted but never converted into a capital-deployment action.
- **Spec cause:** §B.8 Analysis Requirements asked for "interpretation" of each category but didn't require any forward-looking stress arithmetic or any conversion of liquidity strength into an actionable prescription. The LLM had no instruction to do either.
- **Fix:** Add to §B.8 Leverage row: *"Compute and report a single-step stress test: what is TIE if EBIT drops 20%? Pass-threshold: TIE > 3x post-stress."* Add to §B.8 Liquidity row: *"If cash ratio > 0.5 and current ratio > 1.2, the recommendation set MUST include one capital-deployment recommendation (buyback, debt paydown, M&A, or accelerated capex). 'Maintain status quo' does not satisfy."*

---

## 3. Revisions (mapped to Gaps 1–3)

1. **Addresses Gap 1.** Rewrite §B.10 to enforce four-field numbered recommendation format. The four sub-fields (Recommendation / Evidence / Counter-risk / Owner-horizon) borrow from the executive-memo conventions in `docs/templates/memo-template.md` and prevent narrative drift even with a stylistic LLM.

2. **Addresses Gap 2.** Add the EBIT-reconciliation note under §A.3a. This is a one-paragraph fix; it produces a measurable downstream effect because TIE, debt-burden ratio, and EVA all reference EBIT or ATOI derivatives — naming the gap once propagates the awareness to the LLM's interpretation throughout.

3. **Addresses Gap 3.** Add the stress-test and capital-deployment instructions to §B.8. The single-step stress test ("EBIT −20%, what's TIE?") is a 30-second arithmetic exercise but transforms the leverage section from descriptive to risk-aware. The capital-deployment trigger removes the LLM's escape hatch of "the company is doing fine" when the liquidity ratios actually invite a capital-allocation decision.

---

## 4. Effectiveness rating: **4 / 5**

**Anchored justification (160 words).**

- **5/5 anchor (not achieved):** LLM produces output that needs only proofreading; recommendations have correct structure on first pass; every spec section earns a "Clear" verdict.
- **4/5 anchor (achieved):** LLM produces substantively correct analysis on first pass; minor structural rework needed in one or two sections; majority of spec sections earn "Clear". **Evidence:** All six validation rules passed without intervention; all 29 ratios matched expected values within rounding; three hypotheses were correctly evaluated; Du Pont reconciliation was handled cleanly because §6f pre-documented the mismatch. The structural rework needed was confined to §B.10 (recommendation formatting) and minor narrative additions for leverage stress and capital deployment.
- **3/5 anchor (not warranted):** Would require multiple sections to earn "Missing" verdicts or arithmetic errors in the raw output. Neither occurred.
- **2/5 and 1/5 anchors:** Spec would have to produce analysis that the LLM gets fundamentally wrong (sign errors, wrong company, missing categories). N/A.

Net: a high 4 — three concrete fixable spec gaps (Gaps 1–3 above), no analytical errors, output usable as a first-pass deliverable.

---

## 5. Forward link

Future specs will lead with output-structure enforcement (numbered sub-fields per deliverable) before content requirements, because the Stage 5 evidence shows the LLM follows formatting cues more reliably than it interprets analytical asks — a structural specification surfaces gaps that pure content specification leaves implicit.

---

## 6. Retrospective process feedback (≤150 words)

**What this template revealed vs. free-form writing.** The verdict-table format (Clear / Vague / Missing) pushed me to attach every "Vague" verdict to a *specific symptom in the Stage 5 output*, which is exactly the discipline the rubric is checking for. A free-form retrospective tends to list "things to improve" abstractly; this template forced each criticism to point at a concrete piece of LLM output and explain causality. The 1–5 rating with anchor descriptions also prevented the natural drift toward 5/5 self-assessment — the 4/5 anchor required me to name structural rework that actually happened, which I could not avoid.

**One structural template change.** Add a column to the §1 verdict table for "fix priority (P0 / P1 / P2)" so the top three gaps in §2 are visibly the P0 rows from §1. Currently the linkage exists in prose but is not visually enforced; a priority tag would make the spec → retrospective audit trail one glance shorter.
