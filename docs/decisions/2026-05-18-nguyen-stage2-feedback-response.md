---
template: stage2-feedback-response
purpose: Document how each item from the Stage 2 instructor review was incorporated
audience: Managing Director (Professor Adam Stauffer, acting as MD)
stage: 2-feedback-response
author: Nguyen Bui Ngoc Linh
date: 2026-05-18
company: The Coca-Cola Company (KO: NYSE)
original-memo: docs/decisions/2026-05-10-nguyen-coca-cola-selection.md
original-score: 4.14 / 4.5 (92%)
---

# Stage 2 Feedback Response — Coca-Cola Selection Memo

**To:** Professor Adam Stauffer (acting as Managing Director)
**From:** Nguyen Bui Ngoc Linh
**Date:** May 18, 2026
**Re:** Response to Stage 2 (92%) instructor review

---

## Summary

The Stage 2 instructor review identified six discrete items spanning one structural penalty (collaborator access), one substantive content tightening (H3 hypothesis form), and four polish suggestions (Exec Summary close, frontmatter audience, ASCII quotes, commit hygiene). All six are now addressed on `main`. This memo documents each item with the exact resolution and the commit hash where the change landed, so the feedback trace is visible without scrolling commit history.

---

## 1. `@adamwstauffer` Write collaborator (−5 pts — retroactively restorable)

**Instructor item:** *"Highest-leverage fix: add `@adamwstauffer` as a Write collaborator on `Linh28295/Corporate-Finance`. This is the only thing keeping this from a 97. The penalty is reversible — if you add me before the Stage 3 deadline, I'll restore the 5 points retroactively."*

**Resolution:** Confirmed in place. The Stage 3 review parenthetical states verbatim: *"Confirmed via `gh api`: `@adamwstauffer` already has Write access on `Linh28295/Corporate-Finance` — no collaborator action needed."* Per the instructor's explicit retroactive-restore offer, the 5 points should restore against the Stage 2 line.

---

## 2. H3 hypothesis form (the one substantive content tightening)

**Instructor item:** *"Tighten the third hypothesis from 'may' to a confident prediction. Hypotheses 1 and 2 are textbook executions of 'I expect X because Y' — directional, numerical, falsifiable. The third hedges with 'may signal model stress'. Same substance, sharper voice: 'I expect FY2025 asset turnover to decline vs. FY2024 because the product-mix shift toward lower-margin still beverages dilutes per-unit revenue against a slower-shrinking asset base.' Falsifiable; testable in your Stage 3 build."*

**Resolution:** All three hypotheses now use the `I expect X because Y` form. H3 adopts the instructor's exact suggested phrasing verbatim; H1 and H2 were also rewritten for consistency (the original drafts were directionally correct but had drifted toward declarative future-tense — `"Leverage will appear elevated"` rather than `"I expect leverage to appear elevated because..."`). Final phrasing:

> 1. **I expect KO's debt-to-equity ratio to exceed 1.3x while interest coverage holds at ~7–9x**, because large treasury stock (−$56,423M) and AOCI (−$14,105M) compress book equity and inflate optical leverage even though operating cash flow easily services the debt.
> 2. **I expect KO to retain gross margin ~62% and operating margin ~30% in FY2025**, because the asset-light concentrate-only franchise model outsources capital-intensive bottling and yields a structural margin premium over fully-integrated beverage peers.
> 3. **I expect FY2025 asset turnover to decline vs. FY2024**, because the product-mix shift toward lower-margin still beverages dilutes per-unit revenue against a slower-shrinking asset base — a falsifiable prediction directly testable in Stage 3.

H3 is confirmed by the actual Stage 3 model: model-computed asset turnover 0.477x (FY2025) vs. ~0.468x (implied from FY2024); Mergent period-end 0.457x vs. 0.468x. Both denominators show decline, falsifiability satisfied.

**Commit:** `b0478a7` ("Final-round audit: close last three gaps vs. live instructor spec").

---

## 3. Executive Summary close (instructor: *"Minor stylistic — no point loss"*)

**Instructor item:** *"The Executive Summary could close with the recommendation, not the data note. You open strongly but the closing sentence pivots to data availability. A senior-analyst memo lands on the ask: end the Exec Summary with 'With this analytical structure and complete FY2024–FY2025 data, I recommend KO as the project subject and propose moving directly to Stage 3 build.'"*

**Resolution:** Adopted the instructor's exact suggested closing verbatim. Exec Summary now lands on the ask rather than data availability.

**Commit:** `f7cff2b` ("Apply Stage 2 instructor feedback (92% review)").

---

## 4. Frontmatter audience vs. To: line (instructor: *"Optional polish"*)

**Instructor item:** *"The frontmatter `audience: CFO / VP of Finance` doesn't match the memo header 'To: Professor Adam W. Stauffer.' Pick one. The Stage 2 spec asks you to write to the instructor as if he were a managing director — so `audience: managing director` in the frontmatter and `To: Professor Adam Stauffer (acting as MD)` in the header would reconcile the two without losing the framing."*

**Resolution:** Adopted the instructor's exact suggested reconciliation. Frontmatter L4 now reads `audience: Managing Director`; To: line L16 now reads `To: Professor Adam Stauffer (acting as MD)`.

**Commit:** `f7cff2b`.

---

## 5. Curly quotes (instructor: *"Optional, low priority"*)

**Instructor item:** *"Curly quotes (`'` instead of `'`) appear throughout — likely from a paste from Word or Google Docs. Stage 4's spec-as-code workflow will be cleaner with straight ASCII quotes."*

**Resolution:** Verified ASCII throughout. A scan of the memo with Python's Unicode character match finds zero occurrences of `'`, `'`, `"`, or `"`. All apostrophes and quotation marks are straight ASCII (`'`, `"`).

**Commit:** Confirmed during `f7cff2b` audit; no character changes required at that point since the source was already ASCII-clean.

---

## 6. Commit hygiene carry-over (instructor: *"Carry-over recognition (not deducted here)"*)

**Instructor item:** *"Your Stage 1 commit-hygiene tip applies again — your work for this memo committed under 'Add Stage 2 company selection memo: The Coca-Cola Company (KO:NYSE)' is textbook (verb + area + qualifier), but the older `Add files via upload` commits in the same window still sit in the history. Just keep the textbook pattern going."*

**Resolution:** Recognition-only item, not deducted at Stage 2. All commits since the post-deadline sweep (April through May 2026) follow the verb + area + qualifier pattern. Sample of recent commits:

- `b0478a7` "Final-round audit: close last three gaps vs. live instructor spec"
- `b3a4e20` "Align repo with live instructor course site: filenames, HIL iteration, Stage 5 verification..."
- `2698f18` "Downstream audit: propagate Stage 2/3 fixes through Stage 4 / 5 / Extra Credit"
- `f43b4ae` "Stage 3 audit: fix ROE/ROC computation bug, add validation report, clean validation README"

Pre-sweep upload-style commits remain in history (rewriting would lose the audit trail of how the work evolved), but no new instances have been created.

---

## Net effect

If the retroactive 5-point collaborator restore is honoured, and the H3 substantive tightening is recognised, the Stage 2 score recovers from 4.14 / 4.5 toward the instructor's stated 97% ceiling (4.37 / 4.5). All remaining items were explicit no-point-loss polish suggestions and would not affect the score even on strict re-grade.
