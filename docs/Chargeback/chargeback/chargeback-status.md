---
title: Chargeback Status List
deprecated: false
hidden: false
metadata:
  robots: index
---
| Chargeback Status         | Description                                                                                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ME Comm Sent              | New chargeback notification has been submitted to the merchant for his response.                                                                              |
| ME Comm Received          | The merchant has accepted/disputed the chargeback raised with relevant documentation (if applicable).                                                         |
| Bank Comm Sent            | The chargeback has been submitted to the acquiring bank as a part of the representment package.                                                               |
| Doc Rejected              | The chargeback has been rejected for lack of sufficient documentation for representment.                                                                      |
| Closed in Customer favour | The chargeback has been closed in the customer favour. The money has been returned to the customer.                                                           |
| Closed in Merchant favour | The chargeback has been closed in the merchant favour. No money is debited; if any money was debited, then the same is reversed back to the merchant account. |

<br />

<br />

### Chargeback Status Categories

Understand the different chargeback statuses and how to review cases effectively.

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
