---
name: writer-doc-update
description: >-
  Applies an existing docs.payu.in change from a dev-docs JIRA ticket. Creates
  a branch from v1, edits only the files the ticket names, commits, and opens
  a GitHub pull request for review. Use when the user gives a JIRA key, a docs
  change request, or asks to update an existing page and open a PR. Does not
  merge and does not push v1.
---

# Existing doc update

## Purpose

Turn one dev-docs JIRA change request into a reviewable pull request. The ticket is the scope. Production stays with the reviewer.

## Decision summary

- **Decision being made:** Apply only the change the ticket describes, on a branch, and hand over a PR.
- **Decider:** Technical writer for the edit. The user (Publisher) decides whether to merge.
- **Reversibility:** two-way low when the ticket is wording or a title. Two-way medium or one-way when the ticket changes a parameter, hash, error, or endpoint — say which, from the words in the ticket.
- **Cost if wrong:** the wrong page ships, or a field the ticket did not mention changes.

## Inputs required

- The JIRA issue key, or the ticket body pasted in chat.
- Ticket fields from [ticket-format.md](../writer-os/ticket-format.md): file path, the change, and any "do not change" limit.
- Latest `origin/v1`.

A connected JIRA tool may be used to fetch the issue. If none is connected, use the pasted body. Never reconstruct a ticket from the key alone.

## Agentic workflow

This skill is one delivery. Branch, edit, commit, and open the PR in the same run. Do not merge.

1. Read the ticket. If the issue key, the file path, or the change is missing, stop and ask. Do not pick a file by searching.
2. Open each named file. If a path does not exist, stop and say so. Do not create a replacement page on this skill. New trees belong to `writer-restructure`.
3. If the change adds or alters a parameter, hash, error code, or endpoint, open the spec path, `payment-error-codes.json`, or `custom_blocks/HashingSample.md` before editing. If the ticket contradicts that file, stop and quote both. Do not pick a winner.
4. Fetch `origin/v1`. Create `v1_<ISSUE-KEY>-<short-slug>` from `origin/v1`. That is the `v1_{branch}` name ReadMe syncs. The slug is a few lowercase words from the ticket title. Example: `v1_DOC-123-rename-payment-link`. Do not use `update/`. Do not commit on `v1`.
5. Edit only the named change in the named files. Honor "do not change anything else." Leave other frontmatter fields alone unless the ticket asks for that field.
6. Do not edit `RECYCLE BIN/`. Do not stage `writer-os/work/`. Do not add Writer OS paths to `_order.yaml`.
7. Write `writer-os/work/<issue-key>/doc-update.md` with the six rigor sections, and leave it unstaged.
8. One commit, message `Update doc: <doc-name>`. The message body may cite the issue key.
9. Push the feature branch only. Open a pull request into `v1` with `gh pr create`. PR body: issue key, files, what changed, what was left untouched, and the review ask. No merge command.
10. Reply with the file list, the branch, and the PR URL. Ask the user to merge or send it back. Stop.

## Quantitative method

Files named in the ticket / files changed (must match). Lines or sections changed / lines the ticket asked for. Spec files opened, when the change touches a contract. "Not applicable" only when the ticket is wording and names no field, hash, or error.

## Red-team pass

- **Wrong integrator:** the edit is applied to a sibling page the ticket did not name (hosted vs merchant-hosted, payouts vs checkout).
- **Stale contract:** the new sentence disagrees with `reference/` or `payment-error-codes.json`.
- **Secret leakage:** a sample gains a live key, salt, PAN, or real account number.
- **Support load:** a "do not change" line that was still edited, especially test vs live or a hash.

## Tripwires and rollback

A changed path that is not in the ticket. A frontmatter field edited when the ticket did not name it. A branch that does not match `v1_<ISSUE-KEY>-<short-slug>`. A PR whose base is not `v1`. A merge into `v1` performed by the agent.

**Rollback owner:** the user. Close the PR or restore the file on the branch. The agent does not push `v1`.

## Output

- Unstaged note: `writer-os/work/<issue-key>/doc-update.md` with `Writer-OS-Metrics: skill_id=writer-doc-update, date=YYYY-MM-DD`.
- One commit on `v1_<ISSUE-KEY>-<short-slug>`.
- A pull request into `v1`. The chat reply links it.

## Anti-patterns

- Editing a file because it "looks related."
- Creating new pages, moving the IA, or rewriting `_order.yaml` on this skill.
- A branch named `update/…`. ReadMe syncs `v1_{branch}`.
- Pushing or merging `v1`.
- A second commit that includes the work note or unrelated files.

## Handoff

**User (Publisher)** — decision: merge the pull request, or comment with the line that is wrong. Docs go live only after that merge. Next skill: none, until the user asks for another ticket.

## Frameworks applied

WR-2, WR-5, WR-6
