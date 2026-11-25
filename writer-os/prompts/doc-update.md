---
id: doc-update
skill: writer-doc-update
title: Existing doc update
---

# When to use

A dev-docs JIRA ticket already names the file and the change. Start an agent with this prompt. You review the pull request and merge it.

# Fill in

- `{{issue_key}}` — JIRA key, such as DOC-123
- `{{ticket_body}}` — the change request, or a link the agent can open. Include the file path and the change.

# Prompt

```text
Using writer-doc-update:

Apply the dev-docs change request {{issue_key}}.

{{ticket_body}}

Branch from v1. Name the branch v1_{{issue_key}}-<short-slug> so it syncs to ReadMe.
Edit only the files and the change named in the ticket.
Commit with "Update doc: <doc-name>".
Push that branch and open a pull request into v1.
Do not merge. Do not push v1.
Reply with the files changed, the branch name, and the pull request URL.
```
