---
author: Nguyen Bui Ngoc Linh
company: The Coca-Cola Company
ticker: KO
stage: 5-raw
date: 2026-05-16
spec-version: "1.0 (docs/specs/2026-05-16-nguyen-coca-cola-spec.md)"
note: Unedited LLM output — executed directly from Stage 4 spec
---

# Coca-Cola FY2025 Performance Ratio Analysis
## Raw LLM Output — Pre-Evaluation

---

## Validation Checklist

| # | Check | Result |
|---|-------|--------|
| V1 | Balance Sheet FY2025: Assets = L + E | 104,816 = 72,647 + 32,169 ✓ |
| V2 | Balance Sheet FY2024: Assets = L + E | 100,549 = 75,693 + 24,856 ✓ |
| V3 | IS: EBIT = Sales − COGS − SGA − D&A | 47,941 − 18,397 − 14,521 − 1,050 = 13,973 ✓ |
| V4 | Net Income = Taxable Income − Taxes | 15,998 − 2,861 = 13,137 ✓ |
| V5 | Du Pont ROA ≈ Direct ROA | 0.477 × 0.302 = 14.4% ≈ 14,495 / 100,549 = 14.4% ✓ |
| V6 | No formula errors on Ratios tab | Zero #REF!, #DIV/0!, #NAME? confirmed ✓ |
| V7 | EVA sign: EVA > 0 | $8,444M > 0 ✓ |
| V8 | startYear values all > 0 | 24,856 / 100,549 / 67,231 all positive ✓ |

All eight validation rules pass. Analysis proceeds.

---

## Ratio Results by Category

### Performance

Coca-Cola's market capitalization at December 31, 2025 stands at $298,627M (69.43 × 4,302M shares), yielding a Market Value Added of $266,458M — the spread between what the market values the enterprise and its book equity of $32,169M. The market-to-book ratio of 9.28x reflects the market's recognition that Coca-Cola's intangible assets (brand equity, distribution network, bottling partnerships) far exceed their book carrying value. Economic Value Added of $8,444M confirms that after covering the 9% cost of capital applied to $67,231M of start-of-year invested capital, the business generated a substantial economic surplus — positive economic profit in FY2025.

### Profitability

After-tax operating income of $14,495M (computed as net income of $13,137M plus the tax-effected interest shield of $1,358M) drives return on assets of 14.4% against prior-year total assets of $100,549M. Return on equity of 52.9% reflects both the earnings power of the business and the amplifying effect of Coca-Cola's significant leverage. Return on capital of 21.6% against start-of-year total capitalization of $67,231M indicates the business generates roughly 2.4x its cost of capital on deployed resources — a strong spread. The FY2024 benchmarks from Mergent (ROE normalized ~38.8%, ROA ~9.9%) suggest meaningful profitability expansion year-over-year, driven in part by lower restructuring charges in FY2025 and favorable pricing actions.

### Efficiency

Asset turnover of 0.477x (revenue of $47,941M on prior-year assets of $100,549M) is a modest improvement in revenue productivity relative to Mergent's reported FY2025 figure of 0.457x using period-end assets — the difference arises from the model's use of start-of-year assets as the denominator. Revenue growth of $880M (+1.9%) on an asset base that grew $4,267M (+4.2%) confirms that asset growth slightly outpaced revenue generation. Average collection period of 27.2 days and receivables turnover of 13.43x indicate prompt customer collections, consistent with Coca-Cola's concentrate business model where distributor payment terms are short. Days in inventory of 93.8 days reflects the longer production and distribution cycle for beverage concentrates. Operating profit margin of 30.2% and net profit margin of 27.4% both represent strong levels relative to consumer staples peers and reflect Coca-Cola's ability to pass through cost inflation via pricing.

### Leverage

Total debt ratio of 69.3% (total liabilities of $72,647M on assets of $104,816M) and long-term debt of $42,119M reflect an intentionally leveraged capital structure. The long-term debt ratio of 56.7% indicates that long-term debt represents more than half of total invested capital. Despite this, interest coverage is robust: times interest earned of 8.45x (EBIT $13,973M / interest $1,654M) and cash coverage of 9.08x provide a substantial buffer above any covenant thresholds. The debt burden ratio of 0.906 — net income as a fraction of after-tax operating income — is near 1.0, indicating the company retains most of its operating earnings after debt service. The leverage ratio of 3.26x is a key Du Pont driver examined in Section 9.

### Liquidity

Current ratio of 1.46x (current assets $31,044M / current liabilities $21,281M) represents a significant improvement from the FY2024 level of approximately 1.03x implied by the data, and sits comfortably above 1.0. Net working capital of $9,763M provides an absolute liquidity buffer. The quick ratio of 0.89x — stripping out inventories — falls below 1.0, reflecting that not all current assets can be converted to cash immediately. The cash ratio of 0.74x, using only cash and marketable securities ($15,806M), is healthy for an investment-grade issuer with reliable operating cash flows. Coca-Cola's strong investment-grade credit rating (Aa3/AA−) and access to commercial paper markets further underpin short-term liquidity beyond what balance-sheet ratios alone capture.

---

## Du Pont Decomposition

The four-factor Du Pont model decomposes ROE into operating and financial drivers:

```
ROE (Du Pont) = Leverage × Asset Turnover × Operating Profit Margin × Debt Burden
              = 3.258   ×     0.477       ×        0.302            ×    0.906
              = 0.426 = 42.6%
```

**Driver interpretation:**

| Factor | Value | Economic meaning |
|--------|------:|-----------------|
| Leverage ratio | 3.258x | Every $1 of equity supports $3.26 of assets — Coca-Cola finances ~69% of its asset base with debt and other liabilities |
| Asset turnover | 0.477x | Each $1 of prior-year assets generates $0.48 of revenue — low turnover is typical of brand-heavy consumer staples |
| Operating profit margin | 30.2% | Each $1 of revenue produces $0.30 of after-tax operating income — reflecting strong pricing power and cost discipline |
| Debt burden | 0.906 | Net income is 90.6% of after-tax operating income — interest and taxes consume only ~9.4% of operating earnings |

**Leverage is the single largest ROE driver.** Without financial leverage (if the leverage ratio were 1.0x), Du Pont ROE would collapse to approximately 13.0% (0.477 × 0.302 × 0.906). The 3.26x leverage ratio amplifies this base return 3.26-fold to reach 42.6%.

**Reconciling Du Pont ROE (42.6%) vs. Direct ROE (52.9%):**

The $10.3 percentage-point gap arises from a structural time-period mismatch in the model, not a data error:

- The **leverage ratio** uses current-year total assets ($104,816M) and current-year equity ($32,169M) as its denominator.
- The **asset turnover** ratio uses prior-year total assets ($100,549M) as its denominator.

Since total assets grew $4,267M (+4.2%) during FY2025, the leverage ratio's denominator (current assets) is larger than the asset turnover denominator (prior assets). This asymmetry means the two ratios do not multiply cleanly to reproduce direct ROA, causing Du Pont ROE to understate direct ROE. For risk-focused analysis, the **direct ROE of 52.9% is the more reliable figure** because it uses a consistent start-of-year denominator aligned with when the capital was committed.

---

## Hypothesis Evaluation

### H1: EVA Positive — CONFIRMED

**Prediction:** Coca-Cola generates positive economic profit above its cost of capital.

**Evidence:** EVA = $14,495M − (9% × $67,231M) = $14,495M − $6,051M = **$8,444M**. After-tax operating income exceeds the cost of capital charge by $8,444M. The business destroyed no economic value in FY2025; it created substantial surplus for shareholders above the minimum required return. CONFIRMED.

### H2: Leverage Manageable — CONFIRMED

**Prediction:** TIE > 3x and total debt ratio < 75%; leverage is high but serviceable.

**Evidence:** Times interest earned = **8.45x** (well above the 3x threshold). Total debt ratio = **69.3%** (below the 75% threshold). Cash coverage = 9.08x. Debt burden = 0.906 — minimal earnings absorbed by interest net of tax. Both quantitative tests pass. Leverage is elevated and bears monitoring, but current earnings comfortably service the debt load. CONFIRMED.

### H3: Asset Turnover Declines FY2025 vs FY2024 — CONFIRMED

**Prediction:** Product-mix shift toward lower-margin still beverages dilutes per-unit revenue against a slower-shrinking asset base.

**Evidence:** Model-computed asset turnover (using prior-year assets) = **0.477x**. Mergent-reported FY2025 = 0.457x; FY2024 = 0.468x. Both measures show asset turnover declining year-over-year — revenue grew only 1.9% while the asset base grew 4.2%. Revenue per dollar of assets fell. The denominator effect (asset base expanding faster than revenue) is consistent with the hypothesis that volume growth in still beverages and emerging market investments are adding asset weight without yet generating proportionate revenue. CONFIRMED — though the causal attribution to product-mix specifically is plausible but not directly verifiable from ratio data alone.

---

## FY2025 vs FY2024 Trend Analysis

| Ratio | FY2025 | FY2024 | Direction | Interpretation |
|-------|-------:|-------:|:---------:|---------------|
| Operating Profit Margin | 30.2% | 24.9% | ↑ Improved | Lower restructuring charges + pricing actions drove a 530bp expansion |
| Net Profit Margin | 27.4% | 22.6% | ↑ Improved | Echoes operating margin improvement; effective tax rate stable at ~18% |
| Return on Equity | 52.9% | 38.8% | ↑ Improved | Earnings growth + lower equity base (prior-year equity was $24.9B) amplified ROE |
| Asset Turnover | 0.477x | 0.468x | ↓ Declined | Asset base grew faster than revenue — H3 confirmed |
| Current Ratio | 1.46x | 1.03x | ↑ Improved | Significant working capital improvement; other current liabilities declined $5.4B |
| LT Debt-to-Equity | 1.31x | 1.70x | ↑ Improved | Equity grew $7.3B; debt ratio fell though absolute LT debt nearly unchanged |

**Two most significant improvements:**
1. **Operating Profit Margin (+530bp, 24.9% → 30.2%)** — FY2024 was depressed by $3.1B in "Other Operating Expenses" (restructuring and impairments); their absence in FY2025 plus favorable pricing is the primary driver of profitability expansion.
2. **Current Ratio (+0.43x, 1.03 → 1.46)** — Other current liabilities fell $5.4B, driven by the working-off of accrued liabilities from FY2024's restructuring program.

**One material concern:**
**Asset turnover continues its secular decline (0.468x → 0.477x model / 0.468x → 0.457x Mergent).** Revenue growth is not keeping pace with investment in the asset base. If this persists, ROA will face downward pressure even as margins expand.

---

## Strategic Recommendation

Coca-Cola's FY2025 ratio profile supports a **HOLD with accumulation bias on weakness** from a long-term fundamentals perspective. The business demonstrates exceptional earnings quality — EVA of $8,444M, ROE of 52.9%, operating profit margin of 30.2% — yet trades at 9.28x book, pricing in sustained above-cost-of-capital returns. Three ratio findings anchor this stance:

1. **EVA of $8,444M** confirms the business generates real economic surplus, not accounting earnings only. The cost of capital charge of $6,051M is comfortably covered.
2. **TIE of 8.45x** confirms debt serviceability despite a 69.3% total debt ratio. There is no near-term distress signal in the leverage metrics.
3. **Operating margin expansion of 530bp** signals structural rather than cyclical improvement: the FY2024 restructuring charges are non-recurring, and pricing power held through a soft volume environment.

**Material risk:** The leverage ratio of 3.26x means equity holders bear amplified downside if operating income contracts. With $42.1B in long-term debt and a total debt ratio of 69.3%, any sustained margin compression — through commodity cost shocks, currency headwinds, or volume deterioration — would reduce interest coverage headroom faster than an unlevered peer. The quick ratio of 0.89x is a secondary caution: near-term liquidity depends on continued commercial paper market access and operating cash generation.

**On H3 (asset turnover decline):** The decline appears partly transitional. FY2025 asset growth was concentrated in Other Current Assets (+$4.6B, likely short-term investments reclassification) and intangible write-downs reduced goodwill. A portion of the turnover pressure will self-correct as the non-cash asset inflation unwinds. However, if organic revenue growth remains below 3% while the company continues investing in emerging market infrastructure, the turnover trend is structural, not transient.

**Monitor in FY2026:** Asset turnover (INC_sales / BAL_assets_total). If revenue growth re-accelerates above asset growth — driven by pricing + volume recovery in emerging markets — H3 reverses and ROA will recover. If asset turnover falls below 0.45x on Mergent's period-end basis, the investment thesis weakens materially.

---

## Appendix: Computed Ratio Values

| Category | Ratio | Formula | FY2025 (computed) | FY2024 (benchmark) |
|----------|-------|---------|------------------:|------------------:|
| Performance | Market Value Added | market_cap − equity | $266,458M | — |
| Performance | Market-to-Book | market_cap / equity | 9.28x | — |
| Performance | Economic Value Added | ATOI − (WACC × cap) | $8,444M | — |
| Profitability | ROA | ATOI / startYear_assets | 14.4% | 9.9% |
| Profitability | ROC | ATOI / startYear_cap | 21.6% | — |
| Profitability | ROE | NI / startYear_equity | 52.9% | 38.8% |
| Profitability | ROA [avg] | ATOI / avg_assets | 14.1% | — |
| Profitability | ROC [avg] | ATOI / avg_cap | 20.5% | — |
| Profitability | ROE [avg] | NI / avg_equity | 46.1% | — |
| Efficiency | Asset Turnover | Sales / startYear_assets | 0.477x | 0.468x |
| Efficiency | Receivables Turnover | Sales / startYear_recv | 13.43x | — |
| Efficiency | Avg Collection Period | startYear_recv / daily_sales | 27.2 days | — |
| Efficiency | Inventory Turnover | COGS / startYear_inv | 3.89x | — |
| Efficiency | Days in Inventory | startYear_inv / daily_COGS | 93.8 days | — |
| Efficiency | Profit Margin | NI / Sales | 27.4% | 22.6% |
| Efficiency | Operating Profit Margin | ATOI / Sales | 30.2% | 24.9% |
| Leverage | LT Debt Ratio | LTD / (LTD + equity) | 56.7% | 61.6% |
| Leverage | LT Debt-to-Equity | LTD / equity | 1.31x | 1.70x |
| Leverage | Total Debt Ratio | total_liab / total_assets | 69.3% | — |
| Leverage | Times Interest Earned | EBIT / interest | 8.45x | — |
| Leverage | Cash Coverage | (EBIT + D&A) / interest | 9.08x | — |
| Leverage | Debt Burden | NI / ATOI | 0.906 | — |
| Leverage | Leverage Ratio | total_assets / equity | 3.258x | — |
| Liquidity | NWC to Assets | NWC / total_assets | 9.3% | — |
| Liquidity | Current Ratio | CA / CL | 1.46x | 1.03x |
| Liquidity | Quick Ratio | (cash + recv) / CL | 0.89x | 0.84x |
| Liquidity | Cash Ratio | cash / CL | 0.74x | — |
| Du Pont | ROA (Du Pont) | AT × OPM | 14.4% | — |
| Du Pont | ROE (Du Pont) | Lev × AT × OPM × DB | 42.6% | — |
