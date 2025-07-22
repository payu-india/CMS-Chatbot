---
name: V2_authorization_cards
---
<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>eci</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Electronic Commerce Indicator.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">05</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>cavv</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Cardholder Authentication Verification Value.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">AAABAWFlmQAAAABjRWWZEEFgFz</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>flowType</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Flow type for 3D Secure.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Frictionless</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>threeDSTransID</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">3DS Transaction ID.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">67b4c71f-19bf-4d97-bd09-4e3687dc9e42</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>threeDSServerTransID</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">3DS Server Transaction ID.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">eea30d14-71cf-41af-b961-f95b7d67dc93</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>threeDSTransStatus</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">3DS transaction status.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Y</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>threeDSTransStatusReason</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Reason for 3DS transaction status.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">01</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>aquirer_bin</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Bank Identification Number of the acquirer.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">401200</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object containing authUdf1 and authUdf2.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>