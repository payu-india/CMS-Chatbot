# PayU Product Documentation Coverage Tracker

Repo-sourced documentation coverage and prioritization for PayU Developer Docs.

## Deliverables

1. **Master Coverage Tracker** — [`PayU_Product_Documentation_Coverage_Tracker.xlsx`](./PayU_Product_Documentation_Coverage_Tracker.xlsx)
2. **FY26–27 Progress Report (sample format)** — [`PayU_Docs_Coverage_Progress_Report_26-27_Product_Docs.xlsx`](./PayU_Docs_Coverage_Progress_Report_26-27_Product_Docs.xlsx)

## Coverage Tracker sheets

1. **Executive Dashboard** — KPIs, maturity summary, P0/P1/P2 recommendations, key gaps
2. **Product Documentation Inventory** — full product coverage matrix with repo paths
3. **Gap Analysis** — missing docs, duplicates, inconsistencies, restructuring
4. **IG Prioritization** — dedicated Integration Guide recommendations
5. **Coverage Scoring** — coverage methodology **plus fix-first ranked queue** (what to fix first and why)
6. **Repository Analysis** — IA summary
7. **Executive Recommendations** — P0/P1/P2 rationale (DevEx, support, TAT)
8. **Coverage by Category** — category rollups

### Coverage Scoring — fix-first order

Products on the Coverage Scoring sheet are ranked by **Fix Priority Score**:

1. Tier weight (P0–P3) from adoption / core journey / revenue / complexity / support / DevEx  
2. Gap severity `(100 − Coverage%) × 2`  
3. Core-journey boost  
4. Dedicated Integration Guide need  
5. Complexity signal  

Columns include: Fix Priority Rank, Why fix first, What to fix, Recommended Action.

## Regenerating

```bash
python3 docs-coverage-tracker/generate_coverage_tracker.py
python3 docs-coverage-tracker/generate_progress_report.py
```

Requires `openpyxl`.
