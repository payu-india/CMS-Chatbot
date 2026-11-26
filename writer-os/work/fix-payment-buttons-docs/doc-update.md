# Doc update — Payment Buttons cleanup

Functional files: `docs/Self-Serve Products/payment-button/` (the request named `payment-buttons/`; that directory does not exist).

## 1. Decision summary

- **Decision being made:** Apply the pasted Payment Buttons cleanup (frontmatter, duplicate intro, grammar, Paid vs Expired, first-use links) on a branch and hand over a pull request.
- **Decider:** Technical writer for the edit. The user (Publisher) decides whether to merge.
- **Reversibility:** two-way low. Wording, HTML-entity cleanup, and links. No parameter, hash, error code, or endpoint was changed.
- **Cost if wrong:** doc rework. A merchant could open the wrong settlements page, or follow “Payment Links” in the add-button steps.

## 2. Cognitive pre-work

- **Reader base rate:** Merchant operator creating a no-code payment button. They know the Dashboard, not hash formulas.
- **Falsifiers:** `docs/getting started/payu-dashboard/settlements-dashboard/index.md` (`doc:settlements-dashboard`), `docs/getting started/payu-dashboard/transactions/index.md` (`doc:transactions`), `docs/Offerings/split-settlments/index.md` (published slug `split-settlments`, not `split-settlements`). No payment-button page says a successful payment becomes Expired.
- **Pre-mortem:** An integrator shipped the wrong flow because this page sent “when does my money arrive” to Split Settlements, or left ReadMe character entities so a step read as “clic k Payment Links”.
- **Inversion:** A page that restates the title and links Settlements at the misspelled split-settlements slug. This draft replaces the workflow intro and points those Settlements links at the settlements dashboard.

## 3. Quantitative method

- Files named / files changed: 6 / 6. Path on disk is `payment-button/`, not `payment-buttons/`.
- `updatedAt` and `agentTools`: 0 / 0 present. Nothing to remove.
- Parameters, hash, error codes: not applicable. The request is wording and links, and names no field, hash, or error.
- Internal links checked: `doc:transactions`, `doc:settlements-dashboard`, `doc:set-up-your-account`, `https://docs.payu.in/docs/manage-webhooks-using-dashboard`, `https://docs.payu.in/docs/webhook-events-and-sample-payloads#payment-successful`, `https://onboarding.payu.in/`.
- `partial payment`, `split settlement` as a phrase, `MID`, `KAM`, `DND`: not on these six pages.

## 4. Red-team pass

- **Wrong integrator:** Edits stay on the Payment Button pages. Payment Links and Invoices were not edited, even where they share the `split-settlments` href.
- **Stale contract:** No hash or error-code claim was added. Paid vs Expired was checked; these pages do not say a paid button becomes Expired.
- **Secret leakage:** Placeholders only. No keys, salts, or account numbers added.
- **Support load:** `add-payment-button.md` still says click **Payment Links** after the character entities are decoded. The heading and screenshot caption say Payment Buttons. Left for review.

## 5. Tripwires and rollback

- A Settlements link that still points at `doc:split-settlments`.
- A second new link for a term that was already linked on the same page.
- A decoded entity that drops a letter (`Button Details page`, `Details tab`, `Generating Report pop-up`).
- The FAQ edit answer still saying settings cannot be changed.

**Rollback owner:** the user. Close the pull request or restore the previous markdown on this branch. The agent does not push `v1`.

## 6. Frameworks applied

- WR-2, WR-5, WR-6.
- Counter-metric: a support ticket that the add-button step points at Payment Links, or that Settlements opens Split Settlements.
- Decision requested of the Publisher: merge the pull request, or comment with the line that is wrong. In particular, confirm whether step 2 on Add a Payment Button should say **Payment Buttons** rather than **Payment Links**.

`Writer-OS-Metrics: skill_id=writer-doc-update, date=2026-11-24`
