---
name: V2_payment_response_params
---
<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
</tr>
</thead>
  <tbody><tr>
  <td style="border: 1px solid #ddd; padding: 8px;">message</td>
  <td style="border: 1px solid #ddd; padding: 8px;">This parameter contains the status message of the transaction.</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">status</td>
  <td style="border: 1px solid #ddd; padding: 8px;">This parameter returns the status of web service call. The status can be any of the following:<br/>
**0** - If web service call failed.<br/>
**1** - If web service call succeeded.</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">result</td>
  <td style="border: 1px solid #ddd; padding: 8px;">This parameter contains the payment status details in a JSON format including payment ID of the transaction.</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>
