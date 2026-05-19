---
author: Nguyen Bui Ngoc Linh
company: The Coca-Cola Company
ticker: KO
stage: 5-final
date: 2026-05-16
revised: 2026-05-17  # ratios refreshed to workbook precision (14.42% / 52.85% / 42.57%); V9 added; NI $13,137 vs $13,107 footnote; 4/5 spec effectiveness rating
spec-version: "1.0 (docs/specs/2026-05-16-nguyen-coca-cola-spec.md) — revised 2026-05-17"
raw-output: deliverables/2026-05-16-nguyen-coca-cola-llm-raw.md
---

# Coca-Cola FY2025 Performance Ratio Analysis
## Evaluated Final Analysis — Nguyen Bui Ngoc Linh · BUS 629 VEMBA

---

## 1. Company & Data Summary

| Field | Detail |
|-------|--------|
| **Company** | The Coca-Cola Company |
| **Ticker / Exchange** | KO / NYSE |
| **Reporting standard** | U.S. GAAP |
| **Reporting currency** | USD Millions |
| **Current year** | FY2025 (ended December 31, 2025) |
| **Prior year** | FY2024 (ended December 31, 2024) |
| **Primary data source** | Mergent Online 5-Year Financial Summary (as originally reported), cross-referenced against KO 10-K via SEC EDGAR |
| **Market data** | Share price $69.43 (Dec 31, 2025, Yahoo Finance); diluted shares 4,313M |
| **Cost of capital assumption** | 9.0% (WACC; spec-specified) |
| **Accounting notes** | Treasury stock (−$56,423M FY2025) and AOCI (−$14,105M FY2025) are large negatives reducing book equity below economic equity. Equity method investments ($20,235M) are material non-current assets from bottling partner stakes. Retained earnings are POSITIVE ($80,382M). Template CFO ($5,181M) diverges from reported CFO ($7,408M) due to template simplification; reported figure used for FCF commentary. |
| **Net Income basis** | Workbook `INC_net` = $13,137M (consolidated Net Income = EBT $15,998M − Tax $2,861M, matching the Cash Flow Statement). Mergent's IS line shows $13,107M, which is Net Income *attributable to The Coca-Cola Company* after a $30M noncontrolling-interest deduction. This analysis uses the consolidated $13,137M throughout; the $30M difference does not materially affect any ratio (e.g., ROE shifts by less than 0.13pp). |

All nine spec validation rules (V1–V9) pass. The validation table is in the Appendix; the most important checks are: Total Assets = Total L + E both years (FY2025 $104,816M, FY2024 $100,549M), EBIT $13,973M and Net Income $13,137M tie to the formulas, Du Pont ROA equals direct ROA at 14.42%, and Du Pont ROE reconciles to direct ROE with the documented 10.28pp time-period denominator gap.

---

## Ratio Results by Category

**Performance.** Market cap $298,627M (share price $69.43 × 4,302M shares) → MVA $266,458M and M/B 9.28x — the gap between market value and book equity ($32,169M) reflects brand, distribution, and bottling-network intangibles. EVA $8,444M = ATOI $14,495M − 9% × $67,231M start-of-year capital ($6,051M charge): real economic profit, not just accounting profit.

**Profitability.** ATOI $14,495M (= net income $13,137M + tax-effected interest shield $1,358M) drives ROA 14.42% on prior-year assets, ROE 52.85% on prior-year equity ($24,856M — leverage amplification), and ROC 21.56% (2.4× cost of capital). YoY improvement vs. Mergent FY2024 benchmarks (ROA ~9.9%, ROE ~38.8%) tracks the absence of the $3.1B "Other Operating Expenses" restructuring charge that weighed on FY2024.

**Efficiency.** Asset turnover 0.477x (model) / 0.457x (Mergent) — both denominators show decline; revenue grew 1.9% against assets 4.2%. Receivables turnover 13.43x (ACP 27.2 days) reflects short distributor payment terms; days in inventory 93.8 supports concentrate manufacturing cycles. Operating margin 30.2% and net margin 27.40% are strong for consumer staples and signal sustained pricing power.

**Leverage.** Total debt ratio 69.3% and LT debt $42,119M characterize a deliberately leveraged capital structure consistent with investment-grade credit and predictable cash flows. TIE 8.45x and cash coverage 9.08x sit well above typical 3–4× covenant thresholds. Debt burden 0.906 means 90.6% of ATOI reaches net income after interest. LT-debt ratio improved 61.6% → 56.7% (Mergent) as equity expanded.

**Liquidity.** Current ratio 1.46x is a significant improvement from FY2024's ~1.03x, driven by the $5.4B decline in other current liabilities as restructuring accruals settled. NWC $9,763M provides an absolute buffer. Quick ratio 0.89x is below 1.0 in form but unconcerning given $15.8B cash; cash ratio 0.74x confirms adequate near-term coverage.

---

## Du Pont Decomposition

```
ROE (Du Pont) = Leverage × Asset Turnover × Operating Profit Margin × Debt Burden
              = 3.258   ×    0.4768       ×       0.3024            ×   0.9063
              = 42.57%
```

| Factor | Value | Role in ROE |
|--------|------:|------------|
| Leverage ratio | 3.258x | Amplifier — each dollar of equity supports $3.26 of assets |
| Asset turnover | 0.477x | Revenue engine — $0.48 of revenue per dollar of prior-year assets |
| Operating profit margin | 30.2% | Profit quality — $0.30 of ATOI per revenue dollar |
| Debt burden | 0.906 | Retention — 90.6% of ATOI flows to net income after interest |

**Leverage is the dominant driver.** Stripping leverage (= 1.0x) collapses Du Pont ROE to ~13.0%; the 3.26x multiplier amplifies the base return 3.3-fold.

**Reconciliation — Du Pont ROE 42.57% vs. Direct ROE 52.85%.** The 10.28pp gap is structural, not an error: the leverage factor uses current-year denominators (assets $104,816M / equity $32,169M) while asset turnover uses prior-year assets ($100,549M). Because total assets grew $4,267M during FY2025, the denominators don't cancel. For risk-focused analysis, **direct ROE 52.85% is the more reliable measure** — it applies a consistent prior-year denominator representing the capital base at the start of the earnings period.

---

## Hypothesis Evaluation

**H1: EVA Positive — CONFIRMED.** EVA = $14,495M − (9% × $67,231M) = **$8,444M > 0**. Capital charge $6,051M covered 2.4× by ATOI. Genuine value creator.

**H2: Leverage Manageable — CONFIRMED.** TIE 8.45x (threshold >3x ✓); total debt ratio 69.3% (threshold <75% ✓); cash coverage 9.08x; debt burden 0.906. Both quantitative thresholds pass comfortably. High absolute leverage ($42.1B LT debt) is structural capital-allocation strategy, not distress.

**H3: Asset Turnover Declines FY2025 vs FY2024 — CONFIRMED.** Model 0.477x vs. ~0.468x prior; Mergent 0.457x vs. 0.468x. Revenue +1.9% ($880M) vs. total assets +4.2% ($4,267M). Direction confirmed; whether the cause is transitional (FY2025 current-asset inflation, FY2024 intangible impairments) or structural (sustained investment outpacing organic revenue) is the key FY2026 question. The still-beverage mix-shift mechanism is plausible but not isolable from ratio data alone.

---

## FY2025 vs FY2024 Trend Analysis

| Ratio | FY2025 | FY2024 | Direction | Commentary |
|-------|-------:|-------:|:---------:|-----------|
| Operating Profit Margin | 30.2% | 24.9% | ↑ +530bp | Absence of $3.1B FY2024 restructuring charges; pricing actions held |
| Net Profit Margin | 27.40% | 22.6% | ↑ +480bp | Follows operating margin; tax rate stable ~18% |
| ROE (direct) | 52.85% | 38.8% | ↑ +1,405bp | Higher earnings + lower prior-year equity base |
| Current Ratio | 1.46x | 1.03x | ↑ +0.43 | Other current liabilities fell $5.4B (restructuring accruals settled) |
| Asset Turnover (Mergent) | 0.457x | 0.468x | ↓ −0.011 | Asset base growing faster than revenue |
| LT Debt-to-Equity | 1.31x | 1.70x | ↑ Improved | Equity grew $7.3B; absolute LT debt nearly flat |

**Two most significant improvements:** (1) OPM +530bp is largely structural — absence of the FY2024 $3.1B restructuring charges plus ~4% pricing realisation; durable unless volume deterioration forces renewed restructuring. (2) Current ratio +0.43x reflects the $5.4B decline in other current liabilities as FY2024 restructuring accruals settled; FY2025 returns to a normalised working-capital position.

**Most material concern: asset-turnover decline (0.468x → 0.457x).** Total assets +4.2% outpaced revenue +1.9%; other current assets surged $4.6B (likely investment reclassification). If sustained — investment-led asset growth without proportionate revenue acceleration — ROA faces structural pressure even with margins held.

---

## Strategic Recommendations

Five actionable recommendations, each grounded in specific model ratios and assessed against the LLM raw output.

**R1. Maintain investment-grade discipline — do not expand leverage further.**
*Data:* Total debt ratio 69.3%, D/E 1.41x, TIE 8.45x, debt burden 0.906. A 20% EBIT contraction would compress TIE to ~6.8x — covenant-safe but with narrower margin of safety. Use incremental debt only for capital returns, not operational scaling.
*LLM:* Identified TIE and debt burden correctly, concluded leverage manageable, but did not run the stress scenario. **Mostly correct, missing stress arithmetic.**

**R2. Address asset turnover before it becomes a valuation headwind.**
*Data:* Asset turnover 0.477x (model) / 0.457x (Mergent). Revenue grew 1.9% vs. assets 4.2%. ROA = margin × turnover; declining turnover compresses ROA even if margins hold. Set an internal asset-productivity floor; screen capex against it.
*LLM:* Flagged declining turnover (H3 confirmed), noted $4.6B other-current-assets surge as transitional, but did not connect turnover decline to ROA sensitivity. **Directionally correct, incomplete causal chain.**

**R3. Deploy cash reserves into high-margin adjacencies, not scale acquisitions.**
*Data:* Cash $15.8B; cash ratio 0.74x; cash/debt 35% (vs. PEP 19%). Margin profile (gross 61.6%, net 27.40%) argues for premium non-alcoholic / functional-hydration adjacencies that preserve the asset-light model — not bottling or distribution M&A that would compress gross margin toward PEP's 54.5%.
*LLM:* Noted strong liquidity but drew no strategic conclusion. **Incomplete — required industry judgment.**

**R4. Protect the franchise model — resist backward integration into bottling.**
*Data:* OPM 30.2%, gross margin 61.6%. These margins exist because KO outsources bottling. Vertical integration would absorb capital into lower-margin operations and erode the $8,444M EVA. Primary structural risk to margin profile.
*LLM:* Did not raise this risk at all. **Silent — required human judgment about industry M&A dynamics.**

**R5. Monitor FY2026 OPM for structural vs. cyclical confirmation.**
*Data:* OPM +530bp YoY (24.9% → 30.2%); FY2024 carried $3.1B in restructuring charges. If FY2026 OPM holds >29%, improvement is structural; if it reverts to 26–27%, FY2024 charges were masking an underlying margin trend.
*LLM:* Correctly identified FY2024 restructuring as the driver and flagged the comparability issue. **Correct and well-reasoned on this point.**

---

## LLM Evaluation & Annotations

**Executed correctly:** all 8 validation checks; Du Pont decomposition matched spec expected value; H1/H2/H3 verdicts aligned with the Stage 3 analysis; FY2024 restructuring-charge context applied to the margin-trend reading; ratio organisation across the six categories matched the spec's required structure.

**Deviated / oversimplified:**
- **No stress testing.** Declared leverage "manageable" without quantifying a 20% EBIT-drop scenario.
- **No capital-deployment prescription.** Noted strong liquidity but didn't convert it into an actionable suggestion.
- **Recommendations were narrative, not numbered.** Raw output read as a paragraph; the final analysis re-shaped into five numbered items with per-item LLM assessment.
- **Vertical-integration risk not raised.** The LLM had no mechanism to surface backward integration into bottling as a structural margin risk — an industry-knowledge gap, not a spec gap.

**Spec gaps vs. LLM limitations.** The CFO template-vs-reported gap ($5,181M vs. $7,408M) is a *spec gap* — the simplification wasn't explained in the spec, producing a dead-end metric. The missing stress test and integration risk are *LLM limitations* requiring industry judgment the spec cannot fully encode. The narrative-vs-numbered recommendation format is also a *spec gap* — the output format wasn't enforced; the spec retrospective (separate file) lists this as Gap 1 with the exact spec-language fix.

---

## Executive Justification

*My own thesis — not the LLM's.*

Coca-Cola is a textbook case of structurally superior business-model economics visible through ratio analysis. Gross margin 61.6%, net margin 27.40%, ROC 21.6% (2.4× cost of capital), and EVA $8,444M are not single-year outcomes; they are the direct consequence of owning the recipe and brand while outsourcing capital-intensive manufacturing and distribution to franchised bottlers. These metrics don't appear by accident.

The leverage profile — total debt ratio 69.3%, D/E 1.41x — is real but properly contextualised: a business generating $8,444M EVA with TIE 8.45x is using leverage deliberately to amplify shareholder returns, not signalling distress. The risk is tail-shaped: simultaneous volume decline and commodity-cost shock would expose the amplification working in both directions.

My one genuine concern, confirmed by the ratio data, is H3 — asset turnover declining as the asset base outgrows revenue (0.457x vs. 0.468x Mergent). KO's ability to grow revenue at a rate that justifies its $104B asset base and $330B market cap is the central long-term question. FY2026 turnover will tell us whether the FY2025 decline was transitional or structural.

**Verdict:** Hold with conviction for investors with a 3–5 year horizon. Franchise moat intact, EVA strongly positive, leverage manageable. The asset-turnover trend is the metric to watch — not because it threatens the business today, but because sustained erosion would pressure the premium valuation (9.28x book) the market currently assigns to KO's margin quality.

---

## Spec Retrospective

Moved to a standalone file per Stage 5 rubric: see [`2026-05-17-nguyen-coca-cola-spec-retrospective.md`](2026-05-17-nguyen-coca-cola-spec-retrospective.md) for the full six-section retrospective (verdict table for 11 spec sections, three gaps with evidence, three revisions, 1–5 effectiveness rating with anchored justification, forward link, and process feedback).

---

## Appendix A — Validation Checklist (V1–V9)

| # | Check | Result |
|---|-------|--------|
| V1 | Balance Sheet FY2025: Assets = L + E | 104,816 = 72,647 + 32,169 ✓ |
| V2 | Balance Sheet FY2024: Assets = L + E | 100,549 = 75,693 + 24,856 ✓ |
| V3 | IS: EBIT = Sales − COGS − SGA − D&A | 47,941 − 18,397 − 14,521 − 1,050 = 13,973 ✓ |
| V4 | Net Income = Taxable Income − Taxes | 15,998 − 2,861 = 13,137 ✓ |
| V5 | Du Pont ROA ≈ Direct ROA | 0.4768 × 0.3024 = 14.42% ≡ 14,495 / 100,549 = 14.42% ✓ |
| V6 | No formula errors on Ratios tab | Confirmed ✓ |
| V7 | EVA > 0 | $8,444M ✓ |
| V8 | All startYear values > 0 | Confirmed ✓ |
| V9 | Du Pont ROE reconciles | Du Pont ROE 42.57%; Direct ROE 52.85%; 10.28pp gap explained by start-of-year vs. current-year denominator mismatch ✓ |

## Appendix B — Prompt log reference

The full cross-stage prompt log lives at [`deliverables/prompt-log.md`](prompt-log.md). LLM used throughout: Claude (claude-sonnet-4-6) via Claude Code. The student's role was directing, reviewing, and approving — the spec-driven workflow the course is designed to teach.
