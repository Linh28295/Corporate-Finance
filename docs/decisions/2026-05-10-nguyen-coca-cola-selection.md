---
template: company-selection-memo
purpose: Select and justify the company for BUS 629 ratio analysis project
audience: Managing Director
stage: 2
author: Nguyen Bui Ngoc Linh
date: 2026-05-10
company: The Coca-Cola Company
ticker: KO
exchange: NYSE
---

# Company Selection Memo
## BUS 629: International Corporate Finance -- Stage 2

**To:** Professor Adam Stauffer (acting as MD)  
**From:** Nguyen Bui Ngoc Linh  
**Date:** May 10, 2026  
**Re:** Company Selection -- The Coca-Cola Company (NYSE: KO)

---

## Executive Summary

I propose **The Coca-Cola Company (NYSE: KO)** for the BUS 629 ratio analysis project. KO's asset-light franchise model and unusually leveraged capital structure make it a strong test case across profitability, leverage, and efficiency ratios. With this analytical structure and complete FY2024–FY2025 data, I recommend KO as the project subject and propose moving directly to Stage 3 build.

---

## 1. Company Overview

| Field | Detail |
|-------|--------|
| **Company** | The Coca-Cola Company |
| **Ticker / Exchange** | KO / New York Stock Exchange (NYSE) |
| **Industry** | Beverages -- Non-Alcoholic / Consumer Staples |
| **Business** | Global manufacturer, marketer, and licensor of beverage concentrates and syrups sold through a franchised bottling network across 200+ countries |
| **Market Capitalization** | ~USD 306 billion (as of Dec 31, 2025) |
| **Fiscal Year End** | December 31 |
| **Reporting Currency** | U.S. Dollar (USD) |
| **Reporting Standards** | U.S. GAAP |

---

## 2. Selection Rationale

KO illustrates the tension between accounting presentation and economic reality: large treasury stock (−$56,423M) and AOCI (−$14,105M) inflate apparent leverage that operating cash flow easily supports. Strategically, the franchised global-network governance challenge mirrors my Prudential Vietnam work, so the BUS 629 frameworks land in a business I can interrogate with judgment. The carbonated-to-still product-mix shift should produce measurable pressure on margins and asset efficiency — visible directly in the ratio data.

---

## 3. Data Availability & Sources

| Source | Contents |
|--------|----------|
| **SEC EDGAR** (edgar.sec.gov) | 10-K filings for FY2025 and FY2024 -- Income Statement, Balance Sheet, Cash Flow Statement, and Notes |
| **Coca-Cola Investor Relations** (ir.coca-colacompany.com) | Supplemental financial data, earnings releases, and historical annual reports |
| **Mergent Online** | 5-year financial summary used for data population |
| **Yahoo Finance** | Share price at fiscal year-end (Dec 31) for market-based ratios |

All statements are in English under U.S. GAAP; two full fiscal years (FY2025 + FY2024) are confirmed available.

---

## 4. Preliminary Observations

1. **Leverage will appear elevated but is structurally supported.** D/E above 1.3x driven by treasury stock and AOCI, while interest coverage of ~7–9x remains healthy — the disconnect between accounting leverage and economic risk.

2. **Profitability will reflect the franchise premium.** As a concentrate manufacturer (not a bottler), KO should retain gross margin ~62% and operating margin ~30% in FY2025 — well above beverage peers.

3. **Asset turnover will decline FY2025 vs. FY2024.** The mix shift toward lower-margin still beverages dilutes revenue against a slower-shrinking asset base — a falsifiable prediction directly testable in Stage 3.

---

## 5. Ratio Categories Preview

| Category | Relevance |
|----------|-----------|
| **Profitability** | Core strength -- franchise model drives industry-leading margins |
| **Leverage / Solvency** | Most analytically interesting -- large treasury stock and AOCI create unusual optics |
| **Liquidity** | Moderate relevance -- stable cash flows offset relatively low current ratios |
| **Efficiency / Activity** | Critical for testing hypothesis 3 on product-mix impact |
| **Market / Valuation** | High P/E reflects brand premium; useful for benchmarking |
| **Coverage** | Interest and dividend coverage confirm sustainability of capital return policy |

---

## 6. Data Collection Plan

- **Statements:** Income Statement, Balance Sheet, Cash Flow Statement — FY2025 (current) and FY2024 (prior), from 10-K / Mergent
- **Market data:** Dec 31 closing share price and diluted shares for market-based ratios
- **Currency:** USD millions throughout; no conversion required
- **GAAP considerations:** ASC 606 (revenue) and ASC 842 (leases) flagged where they affect ratio comparability
- **Build target:** `models/builds/2026-05-17-nguyen-coca-cola-financials.xlsx`
