# PayU Product Documentation Coverage Tracker

Repo-sourced documentation coverage and prioritization for PayU Developer Docs.

## Deliverables

1. **Master Coverage Tracker** — [`PayU_Product_Documentation_Coverage_Tracker.xlsx`](./PayU_Product_Documentation_Coverage_Tracker.xlsx)  
   Lean 4-sheet workbook: summary, ranked priorities, slim inventory, scoring basis.

2. **FY26–27 Progress Report (sample format)** — [`PayU_Docs_Coverage_Progress_Report_26-27_Product_Docs.xlsx`](./PayU_Docs_Coverage_Progress_Report_26-27_Product_Docs.xlsx)  
   Checklist-style monthly progress report matching the sample layout.

## Coverage Tracker sheets (lean)

1. **Executive Summary** — KPIs, Top 10 priorities, short ranking basis, key gaps  
2. **Priority Ranked List** — all products ranked highest→lowest with why + action  
3. **Product Inventory** — slim fields only (coverage, status, priority, missing critical docs)  
4. **Scoring & Ranking Basis** — formula, weights, worked examples  

Removed for noise reduction: duplicate recommendation sheets, wide link matrices, charts, repository analysis dump.

## Priority ranking basis

**Priority Score** (higher = do sooner):

1. **Tier** — P0=1000, P1=700, P2=400, P3=100  
   (adoption, core journey, revenue, complexity, support dependency, DevEx)
2. **Gap severity** — `(100 − Coverage%) × 2`
3. **Core-journey boost** — up to +50 for Hosted/MH/S2S, Payment Links, CheckoutPro, Subscriptions, Payouts, Partner Onboarding, Tokenization, TPV, etc.
4. **IG need** — +30 if a dedicated Integration Guide is recommended
5. **Complexity** — +20 for S2S / TPV / Partner / Subscriptions / Tokenization / Split / Cross-Border

## Regenerating

```bash
python3 docs-coverage-tracker/generate_coverage_tracker.py
python3 docs-coverage-tracker/generate_progress_report.py
```

Requires `openpyxl`.

## Coverage score

Equal weight across applicable dimensions (N/A excluded):  
Overview · Integration Guide · API · SDK · Quick Start · Webhooks · Errors · Testing · Go Live · Troubleshooting · FAQs · Changelog  

Yes=1 · Partial=0.5 · No=0 · Complete≥85% · Partial 40–84.9% · Missing&lt;40%
