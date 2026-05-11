---
template: company-selection-memo
purpose: Select and justify the company for BUS 629 ratio analysis project
audience: CFO / VP of Finance
stage: 2
author: Nguyen Bui Ngoc Linh
date: 2026-05-10
company: The Coca-Cola Company
ticker: KO
exchange: NYSE
---

# Company Selection Memo
## BUS 629: International Corporate Finance — Stage 2

**To:** Professor Adam W. Stauffer  
**From:** Nguyen Bui Ngoc Linh  
**Date:** May 10, 2026  
**Re:** Company Selection — The Coca-Cola Company (NYSE: KO)

---

## Executive Summary

I propose analyzing **The Coca-Cola Company (NYSE: KO)** for the BUS 629 ratio analysis project. Coca-Cola’s combination of exceptional brand equity, an asset-light franchise model, and an unusually leveraged capital structure makes it a compelling subject for all six ratio categories — particularly profitability, leverage, and efficiency. Its 10-K filings provide comprehensive, audited data readily accessible via SEC EDGAR.

---

## 1. Company Overview

| Field | Detail |
|-------|--------|
| **Company** | The Coca-Cola Company |
| **Ticker / Exchange** | KO / New York Stock Exchange (NYSE) |
| **Industry** | Beverages — Non-Alcoholic / Consumer Staples |
| **Business** | Global manufacturer, marketer, and licensor of beverage concentrates and syrups sold through a franchised bottling network across 200+ countries |
| **Market Capitalization** | ~USD 306 billion (as of Dec 31, 2025) |
| **Fiscal Year End** | December 31 |
| **Reporting Currency** | U.S. Dollar (USD) |
| **Reporting Standards** | U.S. GAAP |

---

## 2. Selection Rationale

Coca-Cola presents a textbook case of the tension between accounting presentation and economic reality. Its balance sheet carries large treasury stock (-$56,423M) and accumulated other comprehensive loss (-$14,105M), producing a debt-to-equity ratio that appears elevated in isolation but is entirely sustainable given the company’s operating cash flow consistency.

From a strategic lens, Coca-Cola mirrors the type of transformation challenge I work on at Prudential Vietnam: managing a global operating model through a franchised network requires the same discipline in governance, financial stewardship, and performance tracking that I apply daily. Analyzing Coca-Cola’s ratios will ground the theoretical frameworks from BUS 629 in a business I can interrogate with real strategic judgment.

The company also offers an analytically rich environment: revenue has shifted from carbonated soft drinks toward still beverages and health-oriented categories, creating pressure on margins and volume efficiency that should surface clearly in the ratio data.

---

## 3. Data Availability & Sources

| Source | Contents |
|--------|----------|
| **SEC EDGAR** (edgar.sec.gov) | 10-K filings for FY2025 and FY2024 — Income Statement, Balance Sheet, Cash Flow Statement, and Notes |
| **Coca-Cola Investor Relations** (ir.coca-colacompany.com) | Supplemental financial data, earnings releases, and historical annual reports |
| **Mergent Online** | 5-year financial summary used for data population |
| **Yahoo Finance** | Share price at fiscal year-end (Dec 31) for market-based ratios |

All financial statements are in English under U.S. GAAP. No translation or accounting-standard conversion is required. Two full fiscal years of comparable data (FY2025 and FY2024) are confirmed available.

---

## 4. Preliminary Observations

1. **Leverage will appear elevated but is structurally supported.** I expect a debt-to-equity ratio above 1.3x — driven by large treasury stock and AOCI — while interest coverage of ~7-9x remains healthy, reflecting the disconnect between accounting leverage and economic risk.

2. **Profitability ratios will reflect the franchise premium.** As a concentrate manufacturer rather than a bottler, Coca-Cola retains high gross and operating margins (~62% and ~30% respectively in FY2025) that significantly outperform beverage industry peers.

3. **Efficiency ratios may signal model stress.** The shift in product mix toward lower-margin still beverages — combined with inflationary cost pressures — may compress asset turnover and inventory efficiency relative to prior periods, revealing where the operating model is under strain.

---

## 5. Ratio Categories Preview

| Category | Relevance |
|----------|-----------|
| **Profitability** | Core strength — franchise model drives industry-leading margins |
| **Leverage / Solvency** | Most analytically interesting — large treasury stock and AOCI create unusual optics |
| **Liquidity** | Moderate relevance — stable cash flows offset relatively low current ratios |
| **Efficiency / Activity** | Important for assessing portfolio-mix shift impact on asset utilization |
| **Market / Valuation** | High P/E reflects brand premium; useful for benchmarking |
| **Coverage** | Interest and dividend coverage confirm sustainability of capital return policy |

---

## 6. Data Collection Plan

- **Primary statements needed:** Income Statement, Balance Sheet, Statement of Cash Flows (FY2025 and FY2024 from 10-K / Mergent)
- **Current year:** FY2025 (ended December 31, 2025)
- **Prior year:** FY2024 (ended December 31, 2024)
- **Market data:** Closing share price at December 31 each year and diluted shares outstanding for EPS and market-based ratios
- **No currency conversion required** — all figures reported in USD millions
- **GAAP considerations:** Revenue recognition under ASC 606 and lease obligations under ASC 842 noted where they affect ratio comparability
- **Timeline:** All data sourced from Mergent Online 5-year summary and entered into `models/builds/2026-05-10-coca-cola-financials.xlsx`
