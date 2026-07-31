# PayU Product Documentation Coverage Tracker

Leadership-ready inventory of PayU products documented in this repository, with coverage scoring, gap analysis, and Integration Guide prioritization.

## Deliverables

1. **FY26–27 Progress Report (sample format)** — [`PayU_Docs_Coverage_Progress_Report_26-27_Product_Docs.xlsx`](./PayU_Docs_Coverage_Progress_Report_26-27_Product_Docs.xlsx)  
   Same layout as the Docs Coverage Progress Report sample: Product → Content Coverage checklist → Recommendations → TW → monthly scores → Total / Docs Score → portfolio Coverage %.

2. **Master Coverage Tracker** — [`PayU_Product_Documentation_Coverage_Tracker.xlsx`](./PayU_Product_Documentation_Coverage_Tracker.xlsx)  
   Executive dashboard, inventory matrix, gap analysis, IG prioritization.

## Workbook sheets

1. **Executive Dashboard** — KPIs, maturity summary, P0/P1/P2 recommendations, key gaps, observations
2. **Product Documentation Inventory** — master product-by-product coverage matrix with repo path hyperlinks
3. **Gap Analysis** — missing overviews/IGs/APIs/SDKs, duplicates, inconsistencies, restructuring needs
4. **IG Prioritization** — dedicated Integration Guide recommendations with priority signals
5. **Coverage Scoring** — methodology + per-product dimension breakdown
6. **Repository Analysis** — IA summary and how to use the tracker
7. **Executive Recommendations** — detailed P0/P1/P2 rationale (DevEx, support, TAT)
8. **Coverage by Category** — rollup averages by category

## Source of truth

All findings are derived from the current PayU Developer Documentation repository:

- `docs/` (excluding `RECYCLE BIN` as non-canonical)
- `reference/`
- `recipes/`
- `custom_pages/`

The attached sample progress report was used only as a reference for reporting philosophy (coverage dimensions, recommendations, leadership presentation). Its data was **not** copied.

## Regenerating

```bash
python3 docs-coverage-tracker/generate_coverage_tracker.py
```

Requires `openpyxl`.

## Scoring (summary)

Equal weight across applicable dimensions:

Overview · Integration Guide · API Reference · SDK · Quick Start · Webhooks · Error Codes · Testing · Go Live · Troubleshooting · FAQs · Changelog

- **Yes** = 1.0 · **Partial** = 0.5 · **No** = 0.0 · **N/A** = excluded
- **Complete** ≥ 85% · **Partial** 40–84.9% · **Missing** < 40%

## DevEx alignment

Recommendations prioritize enabling developers to integrate PayU products **without support intervention**, focusing dedicated Integration Guides on high-adoption / high-complexity / high-support-dependency products—not every product in the catalog.
