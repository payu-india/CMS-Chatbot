# Prompt library

Paste-ready prompts for Cursor agents on this docs repo. One prompt per file. The agent reads the file you name and runs that text. It does not invent a second version of the prompt.

This folder is not part of the docs site. Do not add it to `_order.yaml`.

## Add a prompt

1. Copy `_TEMPLATE.md` to a new file. Name it with lowercase words and hyphens, such as `fix-hash-sample.md`.
2. Fill every field. The `prompt` block is what you paste into a new agent, or what an agent runs when you say `Run prompt <id>`.
3. Keep placeholders in `{{double braces}}`. Do not put live keys, salts, or customer data in a prompt.
4. Set `skill` to a Writer OS skill that already exists (`writer-doc-update`, `writer-restructure`, and the others under `.cursor/skills/`).

A prompt file with an empty `prompt` block is not ready. Leave it out of a run until the block is filled.

## Run one

In a Cursor agent on this repository:

```text
Run prompt doc-update.
Issue: DOC-123
```

Or paste the prompt block yourself and fill the braces first.

The agent opens `writer-os/prompts/<id>.md`, uses the `skill` named there, and asks for any `{{placeholder}}` you left blank. It does not merge the pull request.

## Prompts

| File | Skill | Use when |
|---|---|---|
| [doc-update.md](doc-update.md) | `writer-doc-update` | A dev-docs JIRA ticket names an existing page and the change |
| [restructure.md](restructure.md) | `writer-restructure` | You have an information architecture or a reference doc for a new tree |
| [product-api-docs.md](product-api-docs.md) | `writer-api-reference` | Document a product's APIs from source, as markdown pages, for a PM review |
