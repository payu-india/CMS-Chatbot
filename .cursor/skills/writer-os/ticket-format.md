# Dev-docs change request

Writer OS accepts a docs change request in this shape. The issue key comes from the dev-docs JIRA project. The body is what the agent is allowed to implement.

This shape is the one already used for change requests on this repository. If a live ticket uses different headings, map them only when the file path and the requested change are both explicit. If either is missing, stop and ask. Do not guess the body from the issue key alone.

```markdown
## Task
One sentence: what doc change to make.

## Change Request
File: docs/…/page.md

Change:
  [what to change, including the old and new text when the edit is a replacement]

Do not change anything else in this file — [name what stays: body, other frontmatter fields, other files].

## Git
Base branch: v1
Branch: v1_<ISSUE-KEY>-<short-slug>
Commit: Update doc: <doc-name>

## Report
- Files updated
- The line or section that changed
- Branch name
- Pull request URL
```

## Required before any edit

| Field | If missing |
|---|---|
| Issue key, such as `DOC-123` | Stop. The branch name is `v1_<ISSUE-KEY>-<short-slug>` so ReadMe can sync it. |
| At least one repo path under `docs/`, `recipes/`, `custom_blocks/`, or `reference/` | Stop. Do not search the repo and pick a file. |
| The change itself (old text and new text, or a described edit) | Stop. |
| "Do not change anything else" or an equivalent limit | Treat it as binding when present. When absent, still edit only the named files and only the named change. |

## Not part of the ticket

The agent does not merge the pull request and does not push `v1`. The reviewer pushes or merges to production.
