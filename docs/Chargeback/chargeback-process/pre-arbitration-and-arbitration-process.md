---
title: Pre-Arbitration and Arbitration Process
deprecated: false
hidden: false
metadata:
  robots: index
---
## Pre-Arbitration

After the merchant/acquirer has represented the case (submitted evidence) and the issuer still disagrees with the response. This offers a final opportunity to resolve the dispute based on new information or further clarification, potentially avoiding formal arbitration. The following happens with the case:

* The issuer (customer’s bank) initiates pre-arbitration, usually providing new evidence or arguments as to why the chargeback should stand.
* The acquirer (merchant’s bank through PayU) receives this and can:

  * Accept (agree with chargeback, absorbing the loss), or
  * Decline (dispute further, escalating to arbitration).

  All additional correspondence, documentation, and clarified arguments are exchanged between issuer and acquirer, often facilitated or relayed by the PayU.

## &#x20;Arbitration

If pre-arbitration does not resolve the dispute—that is, the acquirer declines to accept liability. Issuer now formally intervenes and reviews the complete dispute file. The following happens with the case:

* Both parties (issuer and acquirer) submit all documentation, correspondence, and a summary of their positions.
* Issuer dispute resolution team evaluates according to rules and evidence.
* Issuer issues a ruling: assigns financial liability (who bears the loss) and may impose administrative fees or penalties.
* The decision at this stage is **final and binding**.

## Workflow

<Image align="center" src="https://files.readme.io/592bbfb45335f652633a45c6c5859281a8beda598aa19ca1b2fbea029e462431-Representation.png" />

1. **Role of PayU:**
   * Acts as an intermediary, collecting all merchant evidence and forwarding it to the acquirer (merchant’s settling bank, e.g., ICICI, HDFC, etc.).
   * PayU assists in interpreting chargeback codes, compliance criteria, and documentation for the acquiring bank’s submission.

2. **If Pre-Arbitration Is Initiated:**
   * The issuing bank, after reviewing the merchant’s representment (initial defense), may still find the defense unsatisfactory or provide new evidence.
   * The issuer sends a pre-arbitration claim to the acquirer.
   * PayU coordinates with the merchant (if more evidence is required) and the acquiring bank decides whether to accept liability or pursue further.
   * If accepted, the merchant (indirectly, through acquirer/PayU) absorbs the financial loss.
   * If declined, the process moves to arbitration.

3. **During Arbitration:**
   * The dispute case file—including all prior evidence, chargeback codes, written arguments, and any newly exchanged materials—is sent to card issuer for adjudication.
   * Card issuer sets a deadline for both sides to submit any additional evidence/arguments.
   * Card issuer's ruling is communicated back to the acquiring and issuing banks.
   * Any imposed fees (arbitration costs, penalties for losing party) are charged to the losing side’s bank, which may then debit/credit the merchant via PayU.

4. **Timeline and Finality:**
   * Timeframes for responses and escalation are strictly governed by Card issuer's rules (often 45-60 days for each stage).
   * Once Card issuers has ruled, there is very limited scope for appeal.
   * The result is enforced through settlement systems, adjusting balances between acquirer, issuer, and, eventually, merchant.

|                 | PayU’s Role                        | Acquirer’s Role             | Merchant’s Part                                  |
| --------------- | ---------------------------------- | --------------------------- | ------------------------------------------------ |
| Pre-Arbitration | Forwards case, may request docs    | Accept/Decline liability    | May provide new/further supporting docs if asked |
| Arbitration     | Relays final case, informs outcome | Engages with Mastercard     | Accepts final outcome, no further recourse       |
| Compliance      | Advises on rules/guidelines        | Ensures rule adherence      | May need to provide docs for compliance cases    |
| Fees/Penalties  | Passes fees (if any) onward        | Pays/recovers from merchant | Pays/recovers if liable                          |
