# Workflow: <name>

> Copy this file to `workflows/<name>.md` when starting a new workflow.

## Objective
What this workflow accomplishes and why.

## Inputs
| Input | Required | Example | Notes |
|-------|----------|---------|-------|
|       |          |         |       |

## Tools
Run in this order:
1. `tools/<script>.py --arg ...` — what it does, what it writes to `.tmp/`
2. ...

## Outputs
- Deliverable: where the final result lives (Google Sheet, Slides, etc.)
- Intermediates: files in `.tmp/` (disposable)

## Edge cases & failure handling
- What to do if X fails / returns empty / hits a rate limit.
- Paid API calls: confirm with the user before re-running.

## Learnings log
Append dated notes as the workflow is run (quirks, limits, fixes).
- YYYY-MM-DD: ...
