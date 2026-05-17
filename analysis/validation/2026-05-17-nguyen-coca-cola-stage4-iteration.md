---
template: stage4-hil-iteration
purpose: Document one human-in-the-loop iteration on the Stage 4 spec — gap identified in LLM output, spec revision applied
audience: Stage 4 grader
stage: 4-hil
author: Nguyen Bui Ngoc Linh
company: The Coca-Cola Company
ticker: KO
date: 2026-05-17
spec-revised: docs/specs/2026-05-16-nguyen-coca-cola-spec.md (revised 2026-05-17)
stage5-output: deliverables/2026-05-16-nguyen-coca-cola-llm-raw.md
---

# Stage 4 — HIL Iteration Annotated Diff

## Context

The Stage 4 spec was authored on 2026-05-16 and executed against an LLM the same day to produce the Stage 5 raw output. During a rubric audit on 2026-05-17 (after Stage 3 instructor feedback was applied), four concrete gaps in the spec were identified by reviewing what the LLM did and did not produce. Each gap is documented below with a before/after diff and a one-line note explaining what was missing and how the revision closes it.

This file is the Stage 4 HIL evidence per the rubric ("at least one visible HIL iteration demonstrating identified gap and revision"). Three of the four revisions were applied to the live spec; the LLM raw output (`deliverables/2026-05-16-nguyen-coca-cola-llm-raw.md`) is preserved unedited as the executed-against-original artifact.

---

## Gap 1 — Color-coding convention missing from §2 (Model Architecture)

**Where it surfaced in the Stage 5 raw output:** The LLM never mentioned color coding in its model-architecture narrative, even though the workbook uses a Yellow/Blue/Green/Gray convention (documented on the Cover tab). The raw output described tabs and data flow but treated the workbook as a colorless schematic.

**Spec cause:** §2 Model Architecture (lines 32–43 of the original spec) had a single sentence about "named ranges only — no direct cell references" but no styling convention. The LLM had nothing to interpret about visual encoding.

**Before:**
```
All cross-tab references use named ranges exclusively — no direct cell references
(e.g., `Sheet!A1`) appear in the ratio formulas. This ensures the model is portable
and refactorable.
```

**After:**
```
All cross-tab references use named ranges exclusively — no direct cell references
(e.g., `Sheet!A1`) appear in the ratio formulas. This ensures the model is portable
and refactorable.

**Color-coding convention:**

| Style | Meaning |
|-------|---------|
| Yellow background | DATA INPUTS — figures pulled from the 10-K / financial statements |
| Light-blue background + blue text | ASSUMPTIONS — analyst inputs (share price, shares
                                       outstanding, WACC, tax rate, fiscal years) |
| Green text | FORMULAS — cross-sheet references and derived calculations; do not overwrite |
| Gray background | RATIO OUTPUTS — computed values on the Ratios tab; do not overwrite |
```

**Why the fix closes the gap:** The rubric's Part A item 2 explicitly calls for color-coding conventions. With the table in place, any future Stage 5 executor (or human reader) can validate the workbook visually against the spec.

---

## Gap 2 — Ratio interpretation guidance missing from §6 (Ratio Definitions)

**Where it surfaced in the Stage 5 raw output:** The LLM's Performance section reported "MVA of $266,458M" but offered no anchor for whether that magnitude is healthy, alarming, or unremarkable. Similar pattern in Liquidity ("Current ratio 1.46x") — the value was correct but the interpretation was bare.

**Spec cause:** §6 listed every ratio with its formula and an Expected FY2025 column but no "what does high/low mean?" guidance per category. The rubric (Section 6 line 323) requires this interpretation guidance alongside formulas.

**Before:** §6a–6f tables ended with just the Expected FY2025 column; no interpretation column or follow-on guide.

**After:** Added §6g Interpretation Guide — a single table giving "High signals / Low signals / KO FY2025 read" for each of the six ratio categories.

**Why the fix closes the gap:** The Stage 5 final analysis can now ground each category's findings in the spec's own interpretive frame rather than improvising. The "KO FY2025 read" column also acts as a sanity check — if a future Stage 5 run produced a contradictory read (e.g., "High — ROE 18% on ROA 22%"), the divergence from the spec's anchor would surface immediately.

---

## Gap 3 — Du Pont ROE validation rule absent from §7 (Validation Rules)

**Where it surfaced in the Stage 5 raw output:** The LLM correctly reported Du Pont ROE 42.6% and direct ROE 52.9% and described the time-period mismatch — but only because the mismatch was pre-documented in a callout under §6f. There was no V-level validation rule for Du Pont ROE; only Du Pont ROA was validated (V5).

**Spec cause:** §7 enumerated V1–V8 with V5 covering Du Pont ROA equality but no parallel V-rule for Du Pont ROE. A future Stage 5 executor running with a colder version of the spec might treat the gap as a model defect.

**Before:** Validation Rules table ended at V8 (positive startYear values).

**After:**
```
| V9 | Du Pont ROE (reconciliation, not equality) |
    RATIO_leverage × RATIO_asset_turnover × RATIO_operating_profit_margin × RATIO_debt_burden
    returns a finite positive value AND the gap vs. direct ROE
    (INC_net / startYear_equity) is explained by the documented start-of-year vs.
    current-year denominator mismatch (see callout under Section 6f).
    Pass = both Du Pont ROE and direct ROE are positive and finite;
    the magnitude of the gap is acknowledged in the Stage 5 narrative. |
```

**Why the fix closes the gap:** V9 makes the reconciliation requirement explicit — the executor must produce both numbers, must not treat the gap as a balance failure, and must acknowledge it in the narrative.

---

## Gap 4 — Reporting standard and recommendation count under-specified in §1 (Scope & Objective)

**Where it surfaced in the Stage 5 raw output:** The LLM's "Strategic Recommendations" section delivered three loose narrative paragraphs rather than 3–5 numbered recommendations with explicit evidence and counter-risk per item. Also, "U.S. GAAP" never appeared in the LLM output — it was implicit in the 10-K reference but never stated.

**Spec cause:** §1 said "Deliver a strategic recommendation (Section 10)" (singular, vague count) and never mentioned the reporting standard literally.

**Before:**
```
- Deliver a strategic recommendation (Section 10) grounded in the ratio findings.

The model is **read-only at Stage 5**.
```

**After:**
```
- Deliver 3–5 strategic recommendations (Section 10) grounded in the ratio findings.

**Reporting standard:** U.S. GAAP (Form 10-K filer, SEC EDGAR CIK 0000021344).
**Reporting currency:** USD, figures in $millions. **Fiscal year end:** December 31.
**Audience:** Managing Director, Corporate Strategy.

The model is **read-only at Stage 5**.
```

**Why the fix closes the gap:** The recommendation count is now enforced; the GAAP/currency/audience tags eliminate any ambiguity for the executor and surface the reporting standard as a search-indexable literal (the same hygiene Stage 3's instructor flagged on the Notes tab).

---

## Summary

| # | Gap | Spec section affected | Status |
|---|-----|-----------------------|--------|
| 1 | Color-coding convention missing | §2 Model Architecture | Applied — table added |
| 2 | Ratio interpretation guidance missing | §6 Ratio Definitions → new §6g | Applied — guide added |
| 3 | Du Pont ROE validation rule absent | §7 Validation Rules → new V9 | Applied — V9 added |
| 4 | Reporting standard / recommendation count under-specified | §1 Scope & Objective | Applied — both clarified |

The Stage 5 raw output was *not* re-run — the rubric is satisfied by showing the iteration loop (LLM output reveals gap → spec revised). Re-running would be the start of a Round 2, not part of HIL evidence for Round 1.
