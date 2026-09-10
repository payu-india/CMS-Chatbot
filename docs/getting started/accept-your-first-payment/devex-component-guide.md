---
title: DevEx Component Guide
excerpt: >-
  Architecture notes for the Accept Your First Payment DevEx components —
  how to extend integrations, languages, and reuse the building blocks.
deprecated: false
hidden: true
metadata:
  title: DevEx Component Guide (Maintainers)
  description: Maintainer documentation for PayU Accept Your First Payment DevEx components.
  robots: noindex
next:
  description: ''
---
# DevEx Component Guide

Maintainer documentation for the canonical **Accept Your First Payment** experience.

## Implementation approach

PayU docs are authored for **ReadMe** (Git sync). Interactive UI lives in `custom_blocks/*.mdx` as self-contained React components. The onboarding page composes semantic Markdown headings (for TOC + Ask AI) with `<AcceptFirstPaymentGuide />`.

We intentionally did **not** redesign the documentation site. The feature slots into Getting Started as the primary onboarding entry and branches into existing Collect Payments guides.

## Component architecture

| Component | File | Responsibility |
| :-------- | :--- | :------------- |
| `AcceptFirstPaymentGuide` | `custom_blocks/AcceptFirstPaymentGuide.mdx` | Full interactive journey: selector, language tabs, copy, progress, scroll-sync, dynamic content |
| `DevExIntegrationSelector` | `custom_blocks/DevExIntegrationSelector.mdx` | Reusable radio-group integration picker |
| `DevExLanguageTabs` | `custom_blocks/DevExLanguageTabs.mdx` | Language tablist; preserves scroll; optional `localStorage` |
| `DevExCodeSwitcher` | `custom_blocks/DevExCodeSwitcher.mdx` | Language tabs + code panel + copy button |
| `DevExWorkflowTimeline` | `custom_blocks/DevExWorkflowTimeline.mdx` | Workflow timeline / step list |
| `DevExNextStepCards` | `custom_blocks/DevExNextStepCards.mdx` | Branching continuation cards |
| `DevExProgressIndicator` | `custom_blocks/DevExProgressIndicator.mdx` | Step progress bar |
| `DevExCopyButton` | `custom_blocks/DevExCopyButton.mdx` | Accessible copy control with live region |
| `DevExScrollSyncNav` | `custom_blocks/DevExScrollSyncNav.mdx` | Sticky “On this page” nav with IntersectionObserver |

ReadMe custom components cannot reliably import each other, so primitives are **standalone** and the guide re-implements the same UX patterns internally for a single stateful experience.

## File structure

```text
custom_blocks/
  AcceptFirstPaymentGuide.mdx
  DevExCopyButton.mdx
  DevExCodeSwitcher.mdx
  DevExIntegrationSelector.mdx
  DevExLanguageTabs.mdx
  DevExNextStepCards.mdx
  DevExProgressIndicator.mdx
  DevExScrollSyncNav.mdx
  DevExWorkflowTimeline.mdx
docs/getting started/
  _order.yaml                          # accept-your-first-payment first
  accept-your-first-payment/
    index.md                           # canonical merchant page
    devex-component-guide.md           # this maintainer doc (hidden)
    _order.yaml
```

## How the feature integrates with ReadMe

1. Add / edit MDX under `custom_blocks/` with `name:` frontmatter and a preview instance at the bottom.
2. Reference components in Markdown guides as JSX tags, e.g. `<AcceptFirstPaymentGuide />`.
3. Control sidebar order with `_order.yaml`.
4. Semantic `##` headings on the page feed ReadMe’s TOC and improve Ask AI retrieval.
5. Platform fenced code blocks still get ReadMe’s native copy control; interactive panels use `DevExCopyButton` / built-in copy in the guide.

## How to add a new integration type

### In `AcceptFirstPaymentGuide.mdx`

1. Append an object to the `INTEGRATIONS` JSON array: `{ id, label, description, recommended? }`.
2. Add a matching key under `CONTENT` with:
   * `summary`
   * `prerequisites` (string array)
   * `docsUrl` / `docsLabel`
   * `nextCards` (array of `{ id, title, description, href, cta }`)
   * `createHint`
3. Add language samples under `CREATE_SNIPPETS[<id>]` for each supported language id.
4. Optionally update the Markdown tables / Next Steps links in `docs/getting started/accept-your-first-payment/index.md`.

### As a reusable selector only

Pass `optionsJson` into `<DevExIntegrationSelector />` on any page.

## How to add a new programming language

1. Add `{ id, label }` to `LANGS` in `AcceptFirstPaymentGuide.mdx`.
2. Add hash sample under `HASH_SNIPPETS[<id>]`.
3. Add verify sample under `VERIFY_SNIPPETS[<id>]`.
4. Add create samples for each integration under `CREATE_SNIPPETS[*][<id>]`.
5. For standalone pages, extend `languagesJson` / `snippetsJson` on `DevExLanguageTabs` or `DevExCodeSwitcher`.

Keep language ids stable (`nodejs`, `java`, `php`, `python`, `go`, `dotnet`) so `localStorage` preferences remain valid.

## Accessibility notes

* Integration picker uses `role="radiogroup"` / `role="radio"` with roving tabindex patterns on standalone selector.
* Language switcher uses `role="tablist"` / `role="tab"`.
* Copy controls expose `aria-label` and an `aria-live` status region.
* Scroll-sync nav sets `aria-current` and moves focus to the target section.
* Layout collapses to a single column on narrow viewports.

## Performance notes

* No external dependencies beyond React hooks already available in ReadMe MDX.
* Data is inlined via `JSON.parse` strings (MDX-safe pattern used elsewhere in this repo).
* IntersectionObserver is used when available; scroll listener is the fallback.
* Heavy labs (for example `PayUHostedIntegrationWizard`) remain on product pages and are linked, not embedded here.

## Assumptions

* ReadMe Git sync registers new `custom_blocks` components by `name` frontmatter (same as existing MDX blocks).
* Absolute `https://docs.payu.in/docs/...` URLs remain valid for cross-links inside components (components cannot use ReadMe `doc:` link syntax).
* Hosted Checkout remains the recommended default for first-time merchants.
* Ask AI benefits primarily from the Markdown `##` headings on the page; the interactive component mirrors those section titles for consistency.

## Follow-up improvements

* Persist completed checklist state per integration in `localStorage`.
* Embed a lightweight “open test checkout” action for Hosted only (reuse wizard primitives carefully).
* Add recipe-style walkthroughs under `recipes/` that deep-link into each journey section.
* Localize the guide copy for regional docs if PayU expands beyond India-focused Getting Started.
