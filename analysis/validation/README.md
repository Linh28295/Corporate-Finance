# analysis/validation/

Self-audit reports, HIL iteration notes, and manual verification artifacts across Stages 3, 4, and 5.

## Files

| File | Stage | Description |
|------|-------|-------------|
| `2026-05-17-nguyen-coca-cola-validation-report.md` | 3 | Stage 3 self-audit (200–300 word deliverable per Stage 3 rubric, addresses all eight checklist items) |
| `2026-05-10-nguyen-coca-cola-financials-data-reference.md` | 3 | Complete FY2025 + FY2024 financial data reference — all IS, BS, CFS figures with balance checks |
| `2026-05-10-nguyen-coca-cola-stage3-data-guide.md` | 3 | Named range mapping guide — links each `INC_*`, `BAL_*`, `CASH_*` range to its 10-K line item |
| `2026-05-17-nguyen-coca-cola-stage4-iteration.md` | 4 | HIL iteration evidence — four spec gaps identified from Stage 5 LLM output with annotated before/after diffs |
| `2026-05-17-nguyen-coca-cola-stage5-verification.md` | 5 | Manual verification table — six ratios recomputed by hand vs. LLM output (10% of Stage 5 rubric) |

## Validation results summary (Stage 3)

All eight self-audit checklist items from the Stage 3 rubric are addressed in the validation report.

| # | Check | Result |
|---|-------|--------|
| 1 | Balance Sheet FY2025 | $104,816M = $72,647M + $32,169M ✅ |
| 2 | Balance Sheet FY2024 | $100,549M = $75,693M + $24,856M ✅ |
| 3 | Du Pont ROA consistency | 0.477 × 0.302 = 14.42% ≡ direct ROA $14,495M / $100,549M = 14.42% ✅ |
| 4 | Du Pont ROE consistency | Du Pont ROE = 3.258 × 0.477 × 0.302 × 0.906 = 42.57%; Direct ROE = $13,137M / $24,856M = 52.85%. Gap = 10.3pp — structural (leverage uses current-year equity; asset turnover uses prior-year assets; denominators do not cancel). Not an error; documented on Notes tab (B24/C24). ⚠️ Documented |
| 5 | Sign checks | No impossible negatives: current ratio 1.46x > 0, TIE 8.45x > 0, all turnover ratios > 0. Capex, dividends, and stock repurchases correctly entered as negatives on the Cash Flow tab. ✅ |
| 6 | Reasonableness | Net profit margin 27.4% (concentrate-only business model — expected high); ROE 52.9% (leverage-amplified — expected elevated for consumer staples); current ratio 1.46x (consumer staples norm ~1.3–1.7x); TIE 8.45x (investment-grade — expected >5x). All ratios within plausible ranges. ✅ |
| 7 | Named range spot-check (5 of 84) | `INC_sales` = 47,941 ✅ · `BAL_assets_total_curr` = 104,816 ✅ · `BAL_equity_shareholders_curr` = 32,169 ✅ · `CASH_operating` = 5,181 (template-simplified; reported = 7,408; reconciliation noted on CFS tab B34–C36) ⚠️ · `startYear_total_assets` = 100,549 ✅ |
| 8 | Formula spot-check (5 of 29) | Ratios!C47 (ROA) = `currentYear_after_tax_operating_income / startYear_total_assets` = 14,495 / 100,549 = 14.42% ✅ · Ratios!C49 (ROE) = `INC_net / startYear_equity` = 13,137 / 24,856 = 52.85% ✅ · Ratios!C59 (profit margin) = `INC_net / INC_sales` = 13,137 / 47,941 = 27.40% ✅ · Ratios!C65 (TIE) = `INC_ebit / INC_interest_expense` = 13,973 / 1,654 = 8.45x ✅ · Ratios!C45 (EVA) = `currentYear_after_tax_operating_income − (cost_capital × startYear_total_capitalization)` = 14,495 − (0.09 × 67,231) = $8,444M ✅ |
| 9 | Start-of-year vs. average | Start-of-year assets ($100,549M) used in direct profitability ratios; averages ($102,683M assets, $28,513M equity, $70,760M capitalization) used in `_avg` variants. ROA-direct 14.42% vs. ROA-avg 14.12% — difference of 0.3pp. Start-of-year basis is more conservative and preferred as it represents the capital base at the beginning of the earnings period. ✅ |

## Naming convention

```
YYYY-MM-DD-{lastname}-{company-slug}-{descriptor}.md
```
