---
id: restructure
skill: writer-restructure
title: Restructure from an IA or reference doc
---

# When to use

You have an information architecture or a reference doc and want a new or rearranged page tree. Start an agent with this prompt. You review the pull request and merge it.

# Fill in

- `{{slug}}` — a few words for the branch, such as `merchant-hosted-checkout`
- `{{issue_key}}` — optional. Delete this line when you have no JIRA key.
- `{{outline}}` — the IA, or a repo path to the reference doc. Page list, order, and the job of each page.

# Prompt

```text
Using writer-restructure:

Build the doc tree from this information architecture or reference doc.

{{outline}}

Branch from v1. Name the branch v1_restructure-{{slug}} so it syncs to ReadMe.
If an issue key was provided, name it v1_{{issue_key}}-{{slug}} instead.
Create only the files the outline names. Update _order.yaml only for those files.
Do not add writer-os or .cursor to the docs navigation.
Commit with "Create doc: <tree name>".
Push that branch and open a pull request into v1.
Do not merge. Do not push v1.
Reply with the files created, the branch name, and the pull request URL.
```
