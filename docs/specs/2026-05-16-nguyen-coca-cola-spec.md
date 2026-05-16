---
template: spec-template
purpose: Define the Excel ratio model and analytical work for Stage 5 execution
audience: LLM executing Stage 5 analysis (no prior context assumed)
stage: 4
author: Nguyen Bui Ngoc Linh
company: The Coca-Cola Company
ticker: KO
date: 2026-05-16
---

# Technical Specification — Coca-Cola Performance Ratio Analysis
**BUS 629 VEMBA · Stage 4 · Nguyen Bui Ngoc Linh**

---

## PART A — MODEL SPECIFICATION

### 1. Scope & Objective

Produce a fully quantified performance ratio analysis of The Coca-Cola Company (KO: NYSE) for fiscal year 2025, benchmarked against fiscal year 2024, using the populated Excel workbook at `models/builds/2026-05-10-coca-cola-financials.xlsx`. The analysis must:

- Compute and report all ratios defined in Section 6 using the named-range formulas in Section 5.
- Decompose return on equity via Du Pont and reconcile any discrepancy between the Du Pont and direct ROE calculations.
- Evaluate three pre-stated hypotheses (Section 8) with a verdict of CONFIRMED, REJECTED, or INCONCLUSIVE supported by the ratio evidence.
- Deliver a strategic recommendation (Section 10) grounded in the ratio findings.

The model is **read-only at Stage 5**: no formula modifications, only formula execution and interpretation.

---

### 2. Model Architecture

| Tab | Role | Key content |
|-----|------|-------------|
| Cover & Instructions | Documentation | Student metadata, reporting standard, source URL |
| Balance Sheet | Data input | FY2025 (current) + FY2024 (prior) side-by-side; formulas compute totals |
| Income Statement | Data input | FY2025 only; % of Sales column formula-driven |
| Cash Flow Statement | Data input | FY2025 only; reconciliation note in rows 34–36 |
| Ratios | Computation hub | Assumptions → Intermediates → Ratio outputs via named ranges |
| Notes | Provenance | Company metadata, data source, AI usage, self-check notes |

All cross-tab references use named ranges exclusively — no direct cell references (e.g., `Sheet!A1`) appear in the ratio formulas. This ensures the model is portable and refactorable.

---

### 3. Data Inputs — Numerical Values from Stage 3

All figures in USD millions unless otherwise noted. Source: Mergent 5-Year Financial Summary + KO FY2025 10-K (SEC EDGAR CIK 0000021344).

#### 3a. Income Statement (FY2025 — current year only)

| Named Range | Line Item | FY2025 |
|-------------|-----------|-------:|
| `INC_sales` | Net Operating Revenues | 47,941 |
| `INC_cost_goods_sold` | Cost of Goods Sold | 18,397 |
| `INC_sga` | Selling, General & Administrative Expenses | 14,521 |
| `INC_depreciation` | Depreciation | 1,050 |
| `INC_ebit` | EBIT (formula: sales − COGS − SGA − D&A) | 13,973 |
| `INC_other_income` | Other Income | 3,679 |
| `INC_interest_expense` | Interest Expense | 1,654 |
| `INC_taxable_income` | Taxable Income (formula) | 15,998 |
| `INC_taxes` | Provision for Income Taxes | 2,861 |
| `INC_net` | Net Income (formula) | 13,137 |
| `INC_dividends` | Dividends Paid | 8,779 |
| `INC_addition_retained_earnings` | Addition to Retained Earnings (formula) | 4,358 |

#### 3b. Balance Sheet — Current Year (FY2025, Dec 31)

| Named Range | Line Item | FY2025 |
|-------------|-----------|-------:|
| `BAL_cash_marketable_securities_curr` | Cash & Short-term Investments | 15,806 |
| `BAL_receivables_curr` | Total Receivables, Net | 3,038 |
| `BAL_inventories_curr` | Inventories | 4,425 |
| `BAL_other_current_assets_curr` | Other Current Assets | 7,775 |
| `BAL_assets_current_curr` | Total Current Assets (formula) | 31,044 |
| `BAL_ppe_gross_curr` | PP&E Gross | 20,429 |
| `BAL_accumulated_depreciation_curr` | Accumulated Depreciation | 9,119 |
| `BAL_fixed_assets_net_curr` | Net PP&E (formula) | 11,310 |
| `BAL_intangibles_curr` | Goodwill & Intangibles | 28,022 |
| `BAL_other_assets_curr` | Other Long-term Assets | 34,440 |
| `BAL_assets_total_curr` | Total Assets (formula) | 104,816 |
| `BAL_debt_short_term_curr` | Short-term Debt (incl. current LTD) | 3,373 |
| `BAL_accounts_payable_curr` | Accounts Payable | 5,649 |
| `BAL_other_current_liabilities_curr` | Other Current Liabilities | 12,259 |
| `BAL_liabilities_current_curr` | Total Current Liabilities (formula) | 21,281 |
| `BAL_debt_long_term_curr` | Long-term Debt | 42,119 |
| `BAL_other_long_term_liabilities_curr` | Other Long-term Liabilities | 9,247 |
| `BAL_liabilities_total_curr` | Total Liabilities (formula) | 72,647 |
| `BAL_common_stock_curr` | Common Stock & APIC | 22,341 |
| `BAL_retained_earnings_curr` | Retained Earnings (net of treasury & AOCI) | 9,828 |
| `BAL_equity_shareholders_curr` | Total Shareholders' Equity (formula) | 32,169 |

#### 3c. Balance Sheet — Prior Year (FY2024, Dec 31) — `startYear_*` inputs

| Named Range | Line Item | FY2024 |
|-------------|-----------|-------:|
| `BAL_cash_marketable_securities_prior` | Cash & Short-term Investments | 14,571 |
| `BAL_receivables_prior` | Total Receivables, Net | 3,569 |
| `BAL_inventories_prior` | Inventories | 4,728 |
| `BAL_other_current_assets_prior` | Other Current Assets | 3,129 |
| `BAL_assets_current_prior` | Total Current Assets (formula) | 25,997 |
| `BAL_ppe_gross_prior` | PP&E Gross | 21,055 |
| `BAL_accumulated_depreciation_prior` | Accumulated Depreciation | 9,570 |
| `BAL_fixed_assets_net_prior` | Net PP&E (formula) | 11,485 |
| `BAL_intangibles_prior` | Goodwill & Intangibles | 31,440 |
| `BAL_other_assets_prior` | Other Long-term Assets | 31,627 |
| `BAL_assets_total_prior` | Total Assets (formula) | 100,549 |
| `BAL_debt_short_term_prior` | Short-term Debt | 2,147 |
| `BAL_accounts_payable_prior` | Accounts Payable | 5,468 |
| `BAL_other_current_liabilities_prior` | Other Current Liabilities | 17,634 |
| `BAL_liabilities_current_prior` | Total Current Liabilities (formula) | 25,249 |
| `BAL_debt_long_term_prior` | Long-term Debt | 42,375 |
| `BAL_other_long_term_liabilities_prior` | Other Long-term Liabilities | 8,069 |
| `BAL_liabilities_total_prior` | Total Liabilities (formula) | 75,693 |
| `BAL_common_stock_prior` | Common Stock & APIC | 21,561 |
| `BAL_retained_earnings_prior` | Retained Earnings (net of treasury & AOCI) | 3,295 |
| `BAL_equity_shareholders_prior` | Total Shareholders' Equity (formula) | 24,856 |

#### 3d. Cash Flow Statement (FY2025 — current year only)

| Named Range | Line Item | FY2025 |
|-------------|-----------|-------:|
| `CASH_operating` | Cash Provided by Operations (formula) | 5,181 |
| `CASH_investments` | Cash Used for Investments (formula) | (67) |
| — | Cash Used for Financing (formula) | (8,140) |

> **Reconciliation note:** Template-computed CFO ($5,181M) differs from reported CFO ($7,408M) by $2,227M. The gap arises from non-cash operating items not captured in the simplified template (stock-based compensation, deferred taxes, pension adjustments). Interpret CASH_operating with this limitation in mind; use reported $7,408M for any free cash flow commentary.

#### 3e. Analyst Assumptions

| Named Range | Input | Value |
|-------------|-------|------:|
| `yearCurrent` | Fiscal year (current) | 2025 |
| `share_price` | KO closing price, Dec 31 2025 (NYSE) | $69.43 |
| `shares_outstanding` | Basic shares outstanding (millions) | 4,302 |
| `cost_capital` | Cost of capital (BUS-629 class default) | 9.00% |
| `tax_rate` | Effective tax rate (FY2025 actual) | 17.88% |

---

### 4. Named Range Conventions

| Prefix | Scope | Example |
|--------|-------|---------|
| `BAL_[item]_curr` | Balance sheet, current year (FY2025) | `BAL_assets_total_curr` |
| `BAL_[item]_prior` | Balance sheet, prior year (FY2024) | `BAL_assets_total_prior` |
| `INC_[item]` | Income statement, current year | `INC_sales`, `INC_net` |
| `CASH_[item]` | Cash flow, current year | `CASH_operating` |
| `startYear_[item]` | Alias → `BAL_[item]_prior` | `startYear_equity` ≡ `BAL_equity_shareholders_prior` |
| `currentYear_[item]` | Alias or derived current-year value | `currentYear_equity` ≡ `BAL_equity_shareholders_curr` |
| `avg_[item]` | Simple average: (start + current) / 2 | `avg_equity` |
| `RATIO_[name]` | Key ratios re-used in Du Pont | `RATIO_asset_turnover`, `RATIO_leverage` |
| `market_capitalization` | `share_price × shares_outstanding` | $298,627M |

No direct cell references (Sheet!$A$1 style) appear in any formula that feeds a ratio output.

---

### 5. Derived Inputs

Computed in the Ratios tab before ratio outputs are calculated. All formulas shown as Excel named-range expressions.

| Named Range | Formula | Expected Value (FY2025) |
|-------------|---------|------------------------:|
| `yearStart` | `yearCurrent - 1` | 2024 |
| `market_capitalization` | `share_price × shares_outstanding` | 298,627 |
| `startYear_equity` | `BAL_equity_shareholders_prior` | 24,856 |
| `startYear_inventory` | `BAL_inventories_prior` | 4,728 |
| `startYear_receivables` | `BAL_receivables_prior` | 3,569 |
| `startYear_total_assets` | `BAL_assets_total_prior` | 100,549 |
| `startYear_total_capitalization` | `BAL_debt_long_term_prior + BAL_equity_shareholders_prior` | 67,231 |
| `currentYear_after_tax_operating_income` | `INC_net + (1 − tax_rate) × INC_interest_expense` | 14,495 |
| `currentYear_daily_sales_average` | `INC_sales / 365` | 131.3 |
| `currentYear_equity` | `BAL_equity_shareholders_curr` | 32,169 |
| `currentYear_cash_marketable_securities` | `BAL_cash_marketable_securities_curr` | 15,806 |
| `currentYear_assets_current` | `BAL_assets_current_curr` | 31,044 |
| `currentYear_liabilities_current` | `BAL_liabilities_current_curr` | 21,281 |
| `currentYear_cost_goods_sold_daily` | `INC_cost_goods_sold / 365` | 50.4 |
| `currentYear_debt_long_term` | `BAL_debt_long_term_curr` | 42,119 |
| `currentYear_working_capital_net` | `BAL_assets_current_curr − BAL_liabilities_current_curr` | 9,763 |
| `currentYear_assets_total` | `BAL_assets_total_curr` | 104,816 |
| `currentYear_total_capitalization` | `BAL_debt_long_term_curr + BAL_equity_shareholders_curr` | 74,288 |
| `currentYear_liabilities_total` | `BAL_liabilities_total_curr` | 72,647 |
| `avg_equity` | `AVERAGE(startYear_equity, currentYear_equity)` | 28,513 |
| `avg_total_assets` | `AVERAGE(startYear_total_assets, currentYear_assets_total)` | 102,683 |
| `avg_total_capitalization` | `AVERAGE(startYear_total_capitalization, currentYear_total_capitalization)` | 70,760 |

---

### 6. Ratio Definitions & Formulas

All formulas use named ranges defined in Sections 4–5. Expected values are computed from Stage 3 inputs.

#### 6a. Performance

| Metric | Formula | Expected FY2025 |
|--------|---------|----------------:|
| Market Value Added (MVA) | `market_capitalization − currentYear_equity` | $266,458M |
| Market-to-Book (MTB) | `market_capitalization / currentYear_equity` | 9.28x |
| Economic Value Added (EVA) | `currentYear_after_tax_operating_income − (cost_capital × startYear_total_capitalization)` | $8,444M |

#### 6b. Profitability

| Metric | Named Range | Formula | Expected FY2025 |
|--------|-------------|---------|----------------:|
| Return on Assets (ROA) | — | `currentYear_after_tax_operating_income / startYear_total_assets` | 14.4% |
| Return on Capital (ROC) | — | `currentYear_after_tax_operating_income / startYear_total_capitalization` | 21.6% |
| Return on Equity (ROE) | — | `INC_net / startYear_equity` | 52.9% |
| ROA [avg assets] | — | `currentYear_after_tax_operating_income / avg_total_assets` | 14.1% |
| ROC [avg capital] | — | `currentYear_after_tax_operating_income / avg_total_capitalization` | 20.5% |
| ROE [avg equity] | — | `INC_net / avg_equity` | 46.1% |

#### 6c. Efficiency

| Metric | Named Range | Formula | Expected FY2025 |
|--------|-------------|---------|----------------:|
| Asset Turnover | `RATIO_asset_turnover` | `INC_sales / startYear_total_assets` | 0.477x |
| Receivables Turnover | — | `INC_sales / startYear_receivables` | 13.43x |
| Avg Collection Period | — | `startYear_receivables / currentYear_daily_sales_average` | 27.2 days |
| Inventory Turnover | — | `INC_cost_goods_sold / startYear_inventory` | 3.89x |
| Days in Inventory | — | `startYear_inventory / currentYear_cost_goods_sold_daily` | 93.8 days |
| Profit Margin | — | `INC_net / INC_sales` | 27.4% |
| Operating Profit Margin | `RATIO_operating_profit_margin` | `currentYear_after_tax_operating_income / INC_sales` | 30.2% |

#### 6d. Leverage

| Metric | Named Range | Formula | Expected FY2025 |
|--------|-------------|---------|----------------:|
| Long-term Debt Ratio | — | `currentYear_debt_long_term / (currentYear_debt_long_term + currentYear_equity)` | 56.7% |
| LT Debt-to-Equity | — | `currentYear_debt_long_term / currentYear_equity` | 1.31x |
| Total Debt Ratio | — | `currentYear_liabilities_total / currentYear_assets_total` | 69.3% |
| Times Interest Earned | — | `INC_ebit / INC_interest_expense` | 8.45x |
| Cash Coverage | — | `(INC_ebit + INC_depreciation) / INC_interest_expense` | 9.08x |
| Debt Burden | `RATIO_debt_burden` | `INC_net / currentYear_after_tax_operating_income` | 0.906 |
| Leverage Ratio | `RATIO_leverage` | `currentYear_assets_total / currentYear_equity` | 3.258x |

#### 6e. Liquidity

| Metric | Formula | Expected FY2025 |
|--------|---------|----------------:|
| NWC to Assets | `currentYear_working_capital_net / currentYear_assets_total` | 9.3% |
| Current Ratio | `currentYear_assets_current / currentYear_liabilities_current` | 1.46x |
| Quick Ratio | `(currentYear_cash_marketable_securities + BAL_receivables_curr) / currentYear_liabilities_current` | 0.89x |
| Cash Ratio | `currentYear_cash_marketable_securities / currentYear_liabilities_current` | 0.74x |

#### 6f. Du Pont System

| Metric | Named Range | Formula | Expected FY2025 |
|--------|-------------|---------|----------------:|
| ROA (Du Pont) | — | `RATIO_asset_turnover × RATIO_operating_profit_margin` | 14.4% |
| ROE (Du Pont) | — | `RATIO_leverage × RATIO_asset_turnover × RATIO_operating_profit_margin × RATIO_debt_burden` | 42.6% |

> **Known time-period mismatch:** Du Pont ROE (42.6%) will not equal direct ROE (52.9%). The leverage ratio uses current-year total assets and current-year equity, while asset turnover uses prior-year total assets. This creates a denominator mismatch. The Stage 5 analysis must identify and explain this discrepancy rather than treat it as a data error.

---

### 7. Validation Rules

The following checks must pass before Stage 5 analysis proceeds. Fail any check — stop and report.

| # | Check | Pass condition |
|---|-------|---------------|
| V1 | Balance Sheet FY2025 | `BAL_assets_total_curr` = `BAL_liabilities_total_curr + BAL_equity_shareholders_curr` → 104,816 |
| V2 | Balance Sheet FY2024 | `BAL_assets_total_prior` = `BAL_liabilities_total_prior + BAL_equity_shareholders_prior` → 100,549 |
| V3 | IS arithmetic | `INC_ebit` = `INC_sales − INC_cost_goods_sold − INC_sga − INC_depreciation` → 13,973 |
| V4 | Net income | `INC_net` = `INC_taxable_income − INC_taxes` → 13,137 |
| V5 | Du Pont ROA | `RATIO_asset_turnover × RATIO_operating_profit_margin` ≈ `currentYear_after_tax_operating_income / startYear_total_assets` (within 0.01%) |
| V6 | No formula errors | Zero `#REF!`, `#DIV/0!`, or `#NAME?` cells on the Ratios tab |
| V7 | EVA sign | EVA > 0 (positive economic profit) — expected $8,444M; if negative, flag as unexpected |
| V8 | Positive startYear values | `startYear_equity`, `startYear_total_assets`, `startYear_total_capitalization` all > 0 |

---

## PART B — ANALYSIS SPECIFICATION

### 8. Analysis Requirements

The Stage 5 LLM analysis must address the following, using only the ratio outputs computed by the model (do not recalculate from raw financials):

#### 8a. Ratio narrative by category

For each of the five ratio categories (Performance, Profitability, Efficiency, Leverage, Liquidity), write 2–3 sentences that:

1. State the computed ratio value(s).
2. Interpret what the value means for Coca-Cola's financial condition in FY2025.
3. Note the directional change vs FY2024 where a prior-year benchmark is available from the data reference.

#### 8b. Hypothesis evaluation

Evaluate each of the three pre-stated hypotheses from Stage 2 with a CONFIRMED / REJECTED / INCONCLUSIVE verdict, followed by a 2–3 sentence justification citing specific ratio values:

| # | Hypothesis | Stage 2 prediction |
|---|------------|--------------------|
| H1 | EVA > 0 | Coca-Cola generates positive economic profit above its cost of capital |
| H2 | Leverage increases risk but remains serviceable | TIE > 3x and total debt ratio < 75%; balance of debt burden and interest coverage confirms manageability |
| H3 | Asset turnover declines FY2025 vs FY2024 | Product-mix shift toward lower-margin still beverages dilutes per-unit revenue against a slower-shrinking asset base |

For H3, compare the model-computed FY2025 asset turnover (0.477x using prior-year assets as denominator) against the Mergent benchmark (0.457x FY2025, 0.468x FY2024) and explain the directional finding.

#### 8c. Trend commentary

Compare FY2025 ratios against FY2024 benchmarks from the data reference for at least six ratios. Identify the two most significant improvements and the one most significant concern, each supported by a ratio value and a one-sentence business explanation.

---

### 9. Du Pont Decomposition

Perform the full four-factor Du Pont decomposition using the four `RATIO_*` named ranges:

```
ROE (Du Pont) = RATIO_leverage × RATIO_asset_turnover × RATIO_operating_profit_margin × RATIO_debt_burden
             = 3.258 × 0.477 × 0.302 × 0.906
             ≈ 42.6%
```

The analysis must:

1. State each driver's value and its economic interpretation (what does a leverage ratio of 3.26x mean for KO's capital structure?).
2. Identify the single largest driver of ROE: leverage (3.26x) amplifies the operating return significantly.
3. Reconcile Du Pont ROE (42.6%) against direct ROE (52.9%) and explain the time-period mismatch: the leverage factor uses current-year denominator while asset turnover uses prior-year denominator, creating a structural difference in the model.
4. State which ROE figure (direct or Du Pont) is more conservative and why a risk-focused analyst would prefer the direct figure.

---

### 10. Strategic Recommendation Requirements

The recommendation section must:

1. Open with a one-sentence thesis: whether Coca-Cola's FY2025 ratios support a BUY, HOLD, or CAUTIOUS HOLD stance from a long-term fundamentals perspective.
2. Cite at least three distinct ratio findings as evidence (e.g., EVA of $8,444M, ROE of 52.9%, TIE of 8.45x).
3. Identify one material risk factor surfaced by the ratios (e.g., high leverage ratio of 3.26x, total debt ratio of 69.3%, or quick ratio of 0.89x below 1.0).
4. Connect to the Stage 2 hypothesis about asset turnover: if H3 is CONFIRMED (asset turnover declined), assess whether this is transient or structural.
5. Conclude with one forward-looking statement: what ratio or metric to monitor in FY2026 and why.

---

### 11. Output Format

The Stage 5 deliverable must be a single Markdown file saved at:

```
analysis/reports/2026-05-16-nguyen-coca-cola-analysis.md
```

Required structure:

```
---
[YAML frontmatter: author, company, ticker, stage, date, spec-version]
---

# Coca-Cola FY2025 Performance Ratio Analysis

## Validation Checklist
[Results of V1–V8]

## Ratio Results by Category
### Performance
### Profitability
### Efficiency
### Leverage
### Liquidity

## Du Pont Decomposition

## Hypothesis Evaluation
### H1: EVA Positive
### H2: Leverage Manageable
### H3: Asset Turnover Decline

## FY2025 vs FY2024 Trend Analysis

## Strategic Recommendation

## Appendix: Computed Ratio Values
[Table of all ratios with formula, computed value, and FY2024 benchmark]
```

The Appendix table is required and must list every ratio from Section 6 with its computed value and, where available, the FY2024 benchmark from the data reference file (`analysis/validation/2026-05-10-coca-cola-financials-data-reference.md`).

Length target: 1,200–1,800 words excluding the Appendix table. Tone: professional financial analyst memo, not a student essay. No hedging phrases ("I think", "it seems"). State findings directly.

---

## Revision Log

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-05-16 | Initial spec — all 11 sections complete |
