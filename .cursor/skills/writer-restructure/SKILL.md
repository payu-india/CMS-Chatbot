---
name: writer-restructure
description: >-
  Restructures docs.payu.in from an information architecture or a reference
  document. Branches from v1, creates only the files that outline names,
  updates _order.yaml for those files, and opens a GitHub pull request. Use
  when the user supplies an IA, a content structure, or a reference doc and
  asks for a restructure or a new page tree. Does not merge and does not push v1.
---

# Restructure

## Purpose

Build a new or rearranged doc tree from a structure the user supplied, and hand it over as a pull request. The outline is the scope. The agent does not invent pages.

## Decision summary

- **Decision being made:** Which pages exist, in which order, with which reader job, as stated in the IA or reference doc.
- **Decider:** Technical writer for the files. The user (Publisher) decides whether to merge.
- **Reversibility:** two-way medium for new pages. One-way if an existing page is removed, renamed as a new URL, or has its contract rewritten. Say which the outline does.
- **Cost if wrong:** integrators land on the wrong page, or a live path disappears.

## Inputs required

One of these, in the chat or as a repo path the user names:

- An information architecture: page list, parent section, order, and the job of each page.
- A reference document whose heading structure is the template to follow.

Also required: a short slug for the branch. The git name is `v1_{branch}` so it syncs to ReadMe. With a JIRA key, `{branch}` is `<ISSUE-KEY>-<slug>` and the full name is `v1_<ISSUE-KEY>-<slug>`. Without a key, `{branch}` is `restructure-<slug>` and the full name is `v1_restructure-<slug>`. Say in the PR when no issue key was supplied. Do not use `update/`.

If neither an IA nor a reference doc is present, stop and ask. Do not draft a structure from the product name.

## Agentic workflow

This skill is one delivery. Branch, create files, commit, and open the PR in the same run. Do not merge.

1. Read the IA or the reference doc. List every page it names. A page that is not on that list is out of scope.
2. For each page that documents an API field, hash, or error, open the matching file under `reference/`, `payment-error-codes.json`, or `custom_blocks/` before writing the claim. If the outline and the spec disagree, stop and quote both.
3. Search `custom_blocks/` before writing a new explanation of hashing, errors, auth, or test keys. Link the block.
4. Fetch `origin/v1`. Create `v1_{branch}` from `origin/v1`, using the slug rule in Inputs required. Example: `v1_restructure-merchant-hosted-checkout`. Do not commit on `v1`.
5. Create or edit only the listed files, and only under `docs/`, `reference/`, `recipes/`, or `custom_blocks/`. New pages use this frontmatter, with `title` and `excerpt` taken from the outline:

```yaml
---
title: Page title [New]
excerpt:
deprecated: false
hidden: true
metadata:
  robots: index
---
```

New pages are markdown like the neighboring pages. Set `hidden: true` and end the title with ` [New]`. A new category gets an `index.md` that overviews only the pages in that category, in the shape of `reference/Self-Serve Products/payment-links/index.md`. Put a page in an existing category when it belongs there.

6. Update `_order.yaml` only in directories where this skill added or moved a page. Match the existing entry style. Do not reorder unrelated entries. Never add `writer-os/` or `.cursor/` to an order file.
7. Do not edit `RECYCLE BIN/`. Do not delete an existing page unless the outline says to remove it. Do not set `deprecated: true` unless the outline says that page is deprecated.
8. Recipes stay in `recipes/`. Parameter tables stay in the page. Placeholders only: `YOUR_KEY`, `YOUR_SALT`.
9. Write `writer-os/work/<slug>/restructure.md` with the six rigor sections, and leave it unstaged.
10. One commit. New pages: `Create doc: <doc-name>`. A tree of several new pages: `Create doc: <tree name>`. A mix of edits to existing pages: `Update doc: <tree name>`.
11. Push the feature branch only. Open a pull request into `v1` with `gh pr create`. PR body: source outline, pages created, `_order.yaml` files touched, pages explicitly not created, and the review ask.
12. Reply with the file list, the branch, and the PR URL. Ask the user to merge or send it back. Stop.

## Quantitative method

Pages named in the outline / pages created or edited (must match). Outline headings with no source file, counted as UNVERIFIED and left out of contractual sentences. `_order.yaml` entries added / new pages (must match).

## Red-team pass

- **Wrong integrator:** a page filed under the wrong product directory, or two products blended because the outline listed them as neighbors.
- **Stale contract:** body text that states a field the opened spec does not have.
- **Secret leakage:** sample values that are not placeholders.
- **Support load:** a new page with no parent in `_order.yaml`, or a removed page with no replacement link when the outline required one.

## Tripwires and rollback

A file that is not on the outline. An `_order.yaml` entry whose file does not exist. A deleted page the outline did not name. A branch that does not start with `v1_`. A PR base other than `v1`. An agent merge into `v1`.

**Rollback owner:** the user. Close the PR. The agent does not push `v1`.

## Output

- Unstaged note: `writer-os/work/<slug>/restructure.md` with `Writer-OS-Metrics: skill_id=writer-restructure, date=YYYY-MM-DD`.
- The pages and order files the outline named, on the feature branch.
- A pull request into `v1`.

## Anti-patterns

- Inventing a section because a similar product has one. A new category is only for pages that do not fit an existing section, and its summary describes those pages.
- A category folder with no `index.md`.
- A new page left visible, or a title that does not end with ` [New]`.
- Rewriting pages the outline said to leave in place.
- Putting the rigor sections into a page under `docs/`.
- Merging the pull request.
- Listing Writer OS files in the docs sidebar.

## Handoff

**User (Publisher)** — decision: merge the pull request, or name the page that does not match the outline. The tree is live only after that merge.

## Frameworks applied

WR-1, WR-3, WR-5, WR-7
