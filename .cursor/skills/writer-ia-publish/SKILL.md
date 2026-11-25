---
name: writer-ia-publish
description: >-
  Plans navigation for a confirmed docs.payu.in page: _order.yaml, inbound
  links, and custom-block reuse. Use when placing a new page, updating the
  sidebar order, or checking that a revised page is linked from the right
  parent. Use writer-ia-publish. Does not commit or push. Never adds Writer OS
  files to the docs navigation.
---

# IA publish

## Purpose

Make a confirmed page findable: order file, parent links, and no second copy of a shared block. Stop before git unless the user asks to commit. Writer OS files stay out of the sidebar.

## Decision summary

- **Decision being made:** Where the page lives in the tree and which existing pages must link to it.
- **Decider:** Publisher.
- **Reversibility:** two-way low for order and links. Not a license to change the page's contract.
- **Cost if wrong:** a correct page nobody finds, or a link into the wrong product area.

## Inputs required

- Confirmed accuracy review with verdict **pass**.
- Confirmed scope canvas paths.
- The directory `_order.yaml` beside a new page. Read it before editing.

## Agentic workflow

1. Context check. Accuracy not passed and not waived: stop.
2. If the page is new, add it to `_order.yaml` in the same directory. Match the existing entry style in that file. Do not reorder unrelated entries. The page must live under `docs/`, `reference/`, or `recipes/`.
3. Do not add `writer-os/`, `.cursor/`, or any Writer OS note to `_order.yaml` or `_readme.yaml`.
4. List inbound links from parent or sibling pages named in the canvas. Edit those files only if they are in scope or the user adds them when you ask. If a needed parent is out of scope, ask before touching it.
5. If the draft pasted a hashing, error, or auth explanation that already exists in `custom_blocks/`, replace the paste with a link. That is reuse, not a rewrite of the contract.
6. Do not edit `RECYCLE BIN/`. Do not change `deprecated` or other frontmatter unless the canvas says this is a deprecation (that is `writer-release-note`).
7. Write `writer-os/work/<slug>/07-ia-publish.md` with the six rigor sections and the file list actually changed.
8. Do not commit or push.
9. Ask the publisher to confirm the parent link. Stop.

## Quantitative method

New `_order.yaml` entries, inbound links added, custom-block substitutions, files touched that were not in the canvas (must be zero unless the user just added them).

## Red-team pass

- **Wrong integrator:** page filed under the wrong product directory.
- **Stale contract:** not applicable — this skill does not change field definitions. Say why. Exception: a link that still points at a deprecated page without saying so.
- **Secret leakage:** not applicable if no samples are edited. If samples are touched, scan placeholders.
- **Support load:** a new page with no parent link, so the only path is a direct URL.

## Tripwires and rollback

`_order.yaml` entry whose file does not exist. A parent link to the wrong slug. An unrelated order entry moved. A Writer OS path added to the sidebar.

**Rollback owner:** Publisher. Revert the order file and links.

## Output

`writer-os/work/<slug>/07-ia-publish.md` and the order or link edits it lists.

`Writer-OS-Metrics: skill_id=writer-ia-publish, date=YYYY-MM-DD`

## Anti-patterns

- Publishing by committing without an explicit user request.
- Rewriting the page body while "fixing IA."
- Creating a new custom block when one already covers the text.
- Putting `writer-os/` into `docs/_order.yaml`.

## Handoff

**Content lead** — decision: ship the branch as-is, or require `writer-release-note` because reader-visible behavior or deprecation changed.

Next skill after confirmation: `writer-release-note` only when that decision is yes. Otherwise the chain stops.

## Frameworks applied

WR-3, WR-1
