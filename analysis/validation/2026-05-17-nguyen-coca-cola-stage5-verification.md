---
template: stage5-verification
purpose: Manually recompute selected ratios from Stage 3 financials and compare to the LLM's stated values
audience: Stage 5 grader
stage: 5-verification
author: Nguyen Bui Ngoc Linh
company: The Coca-Cola Company
ticker: KO
date: 2026-05-17
stage3-workbook: models/builds/2026-05-17-nguyen-coca-cola-financials.xlsx
stage5-raw-output: deliverables/2026-05-16-nguyen-coca-cola-llm-raw.md
stage5-final-analysis: deliverables/2026-05-16-nguyen-coca-cola-final-analysis.md
---

# Stage 5 — Manual Verification Table

## Method

Six ratios recomputed by hand from the Stage 3 financials (`models/builds/2026-05-17-nguyen-coca-cola-financials.xlsx`). Ratios chosen deliberately to span all six categories and to hit the failure modes LLMs typically make on this kind of work: start-of-year vs. current-year denominators, after-tax operating income (not just net income), days-conversion arithmetic, and Du Pont reconciliation.

The "LLM value" column quotes the raw output at `deliverables/2026-05-16-nguyen-coca-cola-llm-raw.md` — unedited. The "Final analysis value" column reflects the precision tightening applied to the evaluated final analysis on 2026-05-17.

## Inputs used (from Stage 3 workbook)

| Symbol | Value | Source |
|---|---:|---|
| `INC_sales` | 47,941 | Income Statement |
| `INC_cost_goods_sold` | 18,397 | Income Statement |
| `INC_ebit` | 13,973 | Income Statement (formula) |
| `INC_interest_expense` | 1,654 | Income Statement |
| `INC_net` (consolidated) | 13,137 | Income Statement (formula = EBT − Tax) |
| `tax_rate` | 0.1788 | Ratios tab assumption |
| `startYear_total_assets` (FY2024) | 100,549 | Balance Sheet prior |
| `BAL_assets_total_curr` (FY2025) | 104,816 | Balance Sheet current |
| `startYear_equity` (FY2024 total equity) | 24,856 | Balance Sheet prior |
| `BAL_equity_shareholders_curr` (FY2025) | 32,169 | Balance Sheet current |
| `startYear_total_capitalization` | 67,231 | = LTD prior 42,375 + equity prior 24,856 |
| `startYear_receivables` (FY2024) | 3,569 | Balance Sheet prior |
| `cost_capital` | 0.09 | Ratios tab assumption |

Derived intermediate (not in workbook as a separate input):
- **After-tax operating income (ATOI)** = `INC_net + (1 − tax_rate) × INC_interest_expense`
  = 13,137 + (1 − 0.1788) × 1,654 = 13,137 + 0.8212 × 1,654 = 13,137 + 1,358.26 = **14,495.26**

---

## Verification table

| # | Ratio | Category | Formula (named-range) | Manual value (arithmetic shown) | LLM raw value | Final-analysis value | Match? | Note |
|---|---|---|---|---|---|---|:---:|---|
| 1 | **Return on Assets (ROA)** | Profitability | `currentYear_after_tax_operating_income / startYear_total_assets` | 14,495.26 / 100,549 = **0.14417** = **14.42%** | 14.4% | 14.42% | ✓ | LLM rounded to 1 decimal; final analysis tightened to workbook precision. Common LLM pitfall: using current-year assets denominator — checked, LLM correctly used start-of-year. |
| 2 | **Return on Equity (ROE) — direct** | Profitability | `INC_net / startYear_equity` | 13,137 / 24,856 = **0.52852** = **52.85%** | 52.9% | 52.85% | ✓ | Denominator is **total** prior-year equity (24,856), not the common-stock-plus-APIC line (21,561). LLM picked the right denominator on first run. |
| 3 | **Average Collection Period (days)** | Efficiency | `startYear_receivables / currentYear_daily_sales_average` where `currentYear_daily_sales_average = INC_sales / 365` | Daily sales = 47,941 / 365 = 131.345; ACP = 3,569 / 131.345 = **27.17 days** | 27.2 days | 27.2 days | ✓ | Unit-conversion ratio (days, not %). Common LLM pitfall: using 360-day banker's year. Checked — both LLM passes use 365, matching the workbook formula on `Ratios!C23`. |
| 4 | **Economic Value Added (EVA)** | Performance | `currentYear_after_tax_operating_income − (cost_capital × startYear_total_capitalization)` | 14,495.26 − (0.09 × 67,231) = 14,495.26 − 6,050.79 = **$8,444.47M** | $8,444M | $8,444M | ✓ | Two compounded LLM-pitfalls covered here: (a) use ATOI, not net income, for the numerator; (b) use **start-of-year** capitalization in the capital charge. LLM got both right. |
| 5 | **Times Interest Earned (TIE)** | Leverage / Coverage | `INC_ebit / INC_interest_expense` | 13,973 / 1,654 = **8.4480x** | 8.45x | 8.45x | ✓ | Simplest ratio in the set — chosen as a sanity-check anchor against the more complex four above. |
| 6 | **Du Pont ROE** | Du Pont | `RATIO_leverage × RATIO_asset_turnover × RATIO_operating_profit_margin × RATIO_debt_burden` | Leverage = 104,816 / 32,169 = 3.2583; Asset turnover = 47,941 / 100,549 = 0.47679; Op margin = 14,495.26 / 47,941 = 0.30236; Debt burden = 13,137 / 14,495.26 = 0.90630. Product: 3.2583 × 0.47679 × 0.30236 × 0.90630 = **0.42574** = **42.57%** | 42.6% | 42.57% | ✓ ⚠ | **Du Pont ROE 42.57% ≠ Direct ROE 52.85% (gap 10.28pp).** Not a calculation error — see Stage 4 spec §6f callout and Notes!C24. The leverage factor uses current-year denominators; asset turnover uses start-of-year. The denominators do not cancel, so the four-factor product does not reproduce direct ROA × leverage. LLM correctly identified and explained this in its raw output. |

---

## Categories covered

Performance (EVA), Profitability (ROA, ROE), Efficiency (ACP), Leverage/Coverage (TIE), Du Pont (Du Pont ROE). Five distinct categories; six ratios. Above the rubric minimum of five.

## Findings

- **No arithmetic discrepancies.** All six ratios tie to the workbook to four-decimal precision; the LLM raw output rounds to one decimal but does not introduce any wrong digits in those decimals.
- **The one ⚠ flag is structural, not an error.** Du Pont ROE legitimately differs from direct ROE in this template; the spec pre-documents the time-period mismatch and the LLM correctly carried that explanation through to the analysis.
- **High-risk pitfalls all cleared:** start-of-year vs. current-year denominators (rows 1–4), 365 vs. 360 day basis (row 3), ATOI vs. net income in EVA numerator (row 4), and Du Pont reconciliation (row 6) — all four were the failure modes specifically picked to stress-test. None failed.
- **Precision drift:** the LLM raw output uses 1-decimal precision (14.4%, 52.9%, 42.6%) where the workbook produces 2-decimal precision (14.42%, 52.85%, 42.57%). The evaluated final analysis tightened these to match the workbook; this is a cosmetic correction, not an analytical one.
