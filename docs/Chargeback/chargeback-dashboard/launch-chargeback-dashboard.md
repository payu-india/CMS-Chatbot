---
title: 'Launch Chargeback Dashboard '
deprecated: false
hidden: true
metadata:
  robots: index
---
## Access Dashboard

To find the chargeback details:

1. Log on to PayU Dashboard.
2. Select **Chargeback** from the left pane.

   The _Chargeback_ page is displayed in a new browser tab.

<Image align="center" src="https://files.readme.io/3045e4a-Bank_Portal_3_1.png" />

If you click a ID under the **id** column of the chargebacks table at the bottom.

<Image align="center" src="https://files.readme.io/06e3a15-Bank_Portal_5.png" />

<Callout icon="📘" theme="info">
  **Note**: You can enter the variables like PayU ID, Transaction ID, Bank Case, chargeback status, and the date entries to search the results.
</Callout>

### Chargeback Timeframes

<HTMLBlock>{`
<table>
<thead>
<tr>
<th>Chargeback Type</th>
<th>Response Timeframe</th>
</tr>
</thead>
<tbody>
<tr>
<td>1st Level Chargeback</td>
<td>1 Day to 5 Days (Calendar Days)</td>
</tr>
<tr>
<td>2nd Level Chargeback & Pre-arbitration</td>
<td>1 Day to 3 Days (Calendar Days)</td>
</tr>
<tr>
<td>Pre-Compliance, Arbitration</td>
<td>1 Day (Calendar Day)</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

<Callout icon="❗️" theme="error">
  **Note**: Each case displays a "Reply Before" date. Failure to respond before this deadline will result in automatic case closure and transaction reversal in favor of the customer.
</Callout>
