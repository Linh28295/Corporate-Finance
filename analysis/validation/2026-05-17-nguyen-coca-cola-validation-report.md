# Stage 3 — Validation Report

**Student:** Nguyen Bui Ngoc Linh
**Company:** The Coca-Cola Company (KO: NYSE) · FY2025 (current) + FY2024 (prior)
**Workbook:** `models/builds/2026-05-17-nguyen-coca-cola-financials.xlsx`
**Date:** 2026-05-17

## Self-audit checklist (eight items per Stage 3 rubric)

**1. Balance Sheet balances both years.** FY2025 Total Assets $104,816M = Total Liabilities $72,647M + Total Equity $32,169M. FY2024 Total Assets $100,549M = $75,693M + $24,856M. Both years tie exactly.

**2. Du Pont ROA consistency.** Du Pont ROA = Asset Turnover (0.4768) × Operating Margin (0.3024) = 14.42%, identical to direct ROA = After-Tax Operating Income $14,495M / Start-of-Year Total Assets $100,549M = 14.42%. The inline check on `Ratios!F75` confirms the match.

**3. Du Pont ROE consistency.** Du Pont ROE = 42.57% diverges from direct ROE = $13,137M / $24,856M = 52.85% (gap of 10.3pp). This is a known structural mismatch in the template: the leverage component uses current-year balances while asset turnover uses prior-year assets, so the denominators do not cancel. Documented on `Notes!C24` and acknowledged here — not an error.

**4. Sign checks.** All efficiency, liquidity, and coverage ratios are positive (current ratio 1.46x, TIE 8.45x, asset turnover 0.48x). Capex, dividends paid, and stock repurchases are correctly entered as negatives on the Cash Flow tab.

**5. Reasonableness.** Net profit margin 27.4% and ROE 52.9% are elevated but expected for a concentrate-only business with strong leverage; current ratio 1.46x sits in the consumer-staples norm of 1.3–1.7x; TIE 8.45x is investment-grade. All within plausible ranges.

**6. Named range spot-check.** `INC_sales` = 47,941 ✓; `BAL_assets_total_curr` = 104,816 ✓; `BAL_equity_shareholders_curr` = 32,169 ✓; `startYear_total_assets` = 100,549 ✓; `CASH_operating` = 5,181 (template-simplified vs. reported $7,408M; reconciliation note on `Cash Flow Statement!B34–C36`).

**7. Formula spot-check.** `Ratios!C47` ROA = ATOI / startYear_total_assets = 14.42% ✓; `Ratios!C49` ROE = INC_net / startYear_equity = 52.85% ✓; `Ratios!C59` profit margin = INC_net / INC_sales = 27.40% ✓; `Ratios!C65` TIE = INC_ebit / INC_interest_expense = 8.45x ✓; `Ratios!C45` EVA = ATOI − (cost_capital × startYear_total_capitalization) = $8,444M ✓.

**8. Start-of-year vs. average.** ROA-direct on start-of-year assets ($100,549M) = 14.42%; ROA on average assets ($102,683M) = 14.12% — divergence of 0.3pp. Start-of-year basis is the conservative choice and the model's primary convention; `_avg` variants are exposed alongside.
