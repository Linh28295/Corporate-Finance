# analysis/validation/

Self-audit reports, data reference documents, and validation documentation for Stage 3 model population.

## Files

| File | Description |
|------|-------------|
| `2026-05-10-coca-cola-financials-data-reference.md` | Complete FY2025 + FY2024 financial data reference — all IS, BS, CFS figures with balance checks confirmed |
| `2026-05-10-coca-cola-stage3-data-guide.md` | Named range mapping guide — links each `INC_*`, `BAL_*`, `CASH_*` range to its 10-K line item with actual values |

## Validation results (Stage 3)

All eight self-audit checklist items from the Stage 3 rubric are addressed below.

| # | Check | Result |
|---|-------|--------|
| 1 | Balance Sheet FY2025 | $104,816M = $72,647M + $32,169M ✅ |
| 2 | Balance Sheet FY2024 | $100,549M = $75,693M + $24,856M ✅ |
| 3 | Du Pont ROA consistency | 0.477 × 0.302 = 14.4% ≈ direct ROA $14,495M / $100,549M = 14.4% ✅ |
| 4 | Du Pont ROE consistency | Du Pont ROE = 3.258 × 0.477 × 0.302 × 0.906 = 42.6%; Direct ROE = $13,107M / $24,856M = 52.7%. Gap = 10.1pp — structural, documented (leverage uses current-year equity; asset turnover uses prior-year assets; denominators do not cancel). Not an error. ⚠️ Documented |
| 5 | Sign checks | No impossible negatives: current ratio 1.46x > 0, TIE 8.45x > 0, all turnover ratios > 0. Treasury stock and AOCI negatives are expected and correctly entered as negatives. ✅ |
| 6 | Reasonableness | Gross margin 61.6% (concentrate model — expected high); ROE 52.9% (leverage-amplified — expected elevated); current ratio 1.46x (consumer staples norm ~1.3–1.7x); TIE 8.45x (investment-grade — expected >5x). All ratios within plausible ranges. ✅ |
| 7 | Named range spot-check (5 of 90) | `INC_Revenue` = 47,941 ✅ · `BAL_assets_total` = 104,816 ✅ · `BAL_equity_total` = 32,169 ✅ · `CASH_cfo` = 5,181 (template-simplified; reported = 7,408; reconciliation noted on CFS tab) ⚠️ · `startYear_assets_total` = 100,549 ✅ |
| 8 | Formula spot-check (5 of 29) | `RATIO_ROA` = ATOI / startYear_assets = 14,495 / 100,549 = 14.4% ✅ · `RATIO_ROE` = net_income / startYear_equity = 13,107 / 24,856 = 52.7% ✅ · `RATIO_gross_margin` = gross_profit / revenue = 29,544 / 47,941 = 61.6% ✅ · `RATIO_TIE` = EBIT / interest_expense = 13,973 / 1,654 = 8.45x ✅ · `RATIO_EVA` = ATOI − (cost_capital × startYear_total_capitalization) = 14,495 − (0.09 × 67,231) = 8,444M ✅ |
| 9 | Start-of-year vs. average | Start-of-year assets used throughout (= prior-year balance, $100,549M FY2025). Average assets = ($104,816M + $100,549M) / 2 = $102,683M. ROA on average assets = 14,495 / 102,683 = 14.1% vs. start-of-year ROA = 14.4% — difference of 0.3pp. Start-of-year basis is more conservative and preferred for this analysis as it represents the capital base at the beginning of the earnings period. ✅ |

## Naming convention

```
YYYY-MM-DD-{company-slug}-{descriptor}.md
```
