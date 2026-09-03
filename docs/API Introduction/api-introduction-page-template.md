---
title: API Introduction Page Template
excerpt: >-
  Reusable template for PayU API Introduction pages — frontmatter, SEO intro,
  AI-friendly headings, workflows, cross-links, and related APIs.
deprecated: false
hidden: true
metadata:
  title: API Introduction Page Template (Internal)
  description: >-
    Internal authoring template for consistent, SEO-friendly, Ask AI-ready PayU
    API Introduction pages.
  robots: noindex
next:
  description: ''
---
Use this template for every new or substantially revised **API Introduction** page.

## Frontmatter template

```yaml
---
title: <Intent-based page title>
excerpt: >-
  <One or two sentences describing the page outcome for developers.>
deprecated: false
hidden: false
metadata:
  title: <SEO title including PayU + topic>
  description: >-
    <155–160 character summary with primary keywords.>
  keywords:
    - <primary keyword>
    - <secondary keyword>
    - <workflow keyword>
  robots: index
next:
  description: ''
---
```

## Body template

```md
<SEO-friendly introduction: what this page helps a developer do and why it matters.>

## <Primary intent H2>

<Short reusable section.>

## <Workflow or decision H2>

| Step / Option | Action | Docs / APIs |
| :------------ | :----- | :---------- |
| 1 | ... | ... |

## What to read next

* [Related concept page](doc:...)
* [Next workflow page](doc:...)

## Related APIs

* [Concrete API Reference link](ref:...)
```

## Authoring rules

1. **One job per page** — one primary developer question.
2. **Intent-based H1/title** — prefer “Making Your First API Request” over “Overview 2”.
3. **AI-friendly headings** — headings should answer Ask AI queries when read alone.
4. **Small sections** — keep sections scannable and reusable.
5. **Workflow first** — show sequence before deep reference detail.
6. **No duplicated formulas** — link to canonical pages (Generate Hash, Error Codes, product guides).
7. **Always include** — What to read next + Related APIs.
8. **Consistent terms** — use Collect Payment (`_payment`), General APIs, key, salt, hash, Verify Payment, surl/furl, webhook.
9. **Cross-link layers** — Guides ↔ API Introduction ↔ API Reference.
10. **SEO** — unique metadata title/description; natural keyword usage in H2s.
