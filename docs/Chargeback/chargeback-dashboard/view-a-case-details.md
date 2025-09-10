---
title: View a Case Details
deprecated: false
hidden: false
metadata:
  robots: index
---
## Filter Cases

Use the available filters to efficiently locate specific cases:

* **PayU ID[s]**: Search using comma-separated PayU IDs
* **Transaction ID[s]**: Search using comma-separated transaction IDs
* **Bank Case[s]**: Search specific bank case numbers
* **Chargeback Status**: Filter by case status
* **Date Range**: Set "From" and "To" dates for chargeback cases

## Case Details

View comprehensive information for individual chargeback cases.

### Transaction Information

Each case displays detailed transaction data:

* **Merchant Transaction ID**: Your internal reference
* **PayU ID**: PayU system identifier
* **Transaction Details**: Date, amount, payment gateway
* **Card Information**: Masked card number for security
* **Settlement Data**: Bank reference, settlement date, UTR details
* **Product Information**: Associated product details and fees

### Chargeback Information

Detailed chargeback-specific data includes:

* **Chargeback Amount**: Disputed transaction amount
* **Important Dates**: Chargeback date and reply deadline
* **Reason Code**: Specific reason for the chargeback
* **Bank Case Number**: Reference for bank communications
* **Current Status**: Real-time case status
* **Debit Information**: Details if amount has been debited

### Customer Details

When available, customer information includes:

* Contact details (name, email, phone)
* Relevant customer communication history

## Chargeback Status Categories

The following chargeback status are listed in the **Chargeback Status** field of **Merchant Panel**. Understand the different chargeback statuses and how to review cases effectively.

<Image align="center" src="https://files.readme.io/fbfc3ad6f4a3e4955b2959e8ab205aa5b7f249c89837389b58f6fa5a26b8a1ad-case_details_chargeback_reasons_highlighted.png" />

<HTMLBlock>{`
<table>
<thead>
<tr>
<th>Status</th>
<th>Description</th>
<th>Action Required</th>
<th>Display</th>
</tr>
</thead>
<tbody>
<tr>
<td>NEW</td>
<td>Cases uploaded by PayU but not yet reviewed by the merchant</td>
<td>Review and respond to these cases first</td>
<td>Shows total count and amount for all NEW cases</td>
</tr>
<tr>
<td>PENDING RESPONSE</td>
<td>Cases already viewed by the user but awaiting merchant response</td>
<td>Provide response before the deadline</td>
<td>Shows total count and amount requiring immediate attention</td>
</tr>
<tr>
<td>PENDING DOC REVIEW</td>
<td>Cases with merchant responses submitted to the bank for review according to Visa/MasterCard chargeback guidelines</td>
<td>No action required - under bank review</td>
<td>Bank review process in progress</td>
</tr>
<tr>
<td>INSUFFICIENT DOCUMENT</td>
<td>Cases where submitted documentation was deemed insufficient</td>
<td>Urgent response needed with updated documentation before deadline</td>
<td>High priority - requires immediate attention</td>
</tr>
<tr>
<td>SUBMITTED TO BANK</td>
<td>Cases submitted to the bank as re-presentment by PayU Chargeback team</td>
<td>No action required - awaiting bank decision</td>
<td>Awaiting bank decision on the dispute</td>
</tr>
<tr>
<td>CLOSED IN CUSTOMER FAVOR</td>
<td>Cases settled in favor of the customer due to merchant acceptance or invalid documentation</td>
<td>No action required - case closed</td>
<td>Final status - customer refund processed</td>
</tr>
<tr>
<td>CLOSED</td>
<td>Cases reviewed and submitted to the acquiring bank</td>
<td>No action required - case closed</td>
<td>Considered closed in merchant's favor unless further disputes arise</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>
