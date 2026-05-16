# Data Sources — Nguyen Bui Ngoc Linh
## The Coca-Cola Company (KO) | BUS 629 Stage 3

This file documents the provenance of every data point used in the Stage 3 financial model.

---

## Primary Source

| Field | Detail |
|-------|--------|
| **Company** | The Coca-Cola Company |
| **Ticker** | KO |
| **Exchange** | NYSE |
| **Source** | Mergent Online — 5-Year Financial Summary (As Originally Reported) |
| **Accessed** | May 10, 2026 |
| **File** | `Coca_Cola._mergent_5_year.xlsx` |
| **Reporting Standard** | U.S. GAAP |
| **Reporting Currency** | USD Millions |
| **Fiscal Year End** | December 31 |

---

## Data by Statement

### Income Statement
| Years covered | FY2025 (current), FY2024 (prior) |
|---------------|----------------------------------|
| Source | Mergent Online — Income Statement Annual (As Originally Reported) |
| Verification | Cross-referenced against KO 10-K filed via SEC EDGAR |

### Balance Sheet
| Years covered | Dec 31, 2025 (current), Dec 31, 2024 (prior / `startYear_*`) |
|---------------|--------------------------------------------------------------|
| Source | Mergent Online — Balance Sheet Annual (As Originally Reported) |
| Verification | Balance sheet check: FY2025 $104,816M = $72,647M + $32,169M ✅; FY2024 $100,549M = $75,693M + $24,856M ✅ |

### Cash Flow Statement
| Years covered | FY2025, FY2024 |
|---------------|----------------|
| Source | Mergent Online — Cash Flow Annual (As Originally Reported) |

### Market Data
| Item | Value | Source | Date |
|------|-------|--------|------|
| KO share price Dec 31, 2025 | ~$71.00 | Yahoo Finance | Dec 31, 2025 |
| KO share price Dec 31, 2024 | ~$62.00 | Yahoo Finance | Dec 31, 2024 |
| Diluted shares FY2025 | 4,313M | KO 10-K EPS note | |
| Diluted shares FY2024 | 4,320M | KO 10-K EPS note | |

---

## SEC EDGAR Reference

KO 10-K filings: `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=KO&type=10-K`

---

## Extra Credit Source — Industry Peer Data

| Field | Detail |
|-------|--------|
| **Source** | Mergent Online — Industry Peers Report |
| **Report ID** | IndustryPeers_2026-04-04 |
| **SIC Code** | 2080 — Beverages |
| **Peer set** | KO, PEP, KDP, STZ, BF.B (plus 4 micro-caps excluded from analysis) |
| **Data vintage** | TTM as of April 2026 |
| **Accessed** | May 16, 2026 |
| **File** | `data/nguyen/2026-04-04-coca-cola-industry-peers-mergent.xlsx` |
| **Used in** | `deliverables/2026-05-16-coca-cola-peer-comparison.md` |

---

## Notes

- All figures reported in USD millions; no currency conversion required
- U.S. GAAP throughout; no IFRS or VAS adjustments needed
- Retained earnings (Reinvested earnings) are POSITIVE for KO
- Treasury stock (-$56,423M FY2025) and AOCI (-$14,105M FY2025) are large negatives that reduce total equity
- Equity method investments ($20,235M FY2025) are material non-current assets representing KO's stakes in its bottling partners
