---
name: AdditionalI_Info_object
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
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>enforcePaymethod</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Force a transaction with a specified method (e.g., CC, DC).</td>
  <td style="border: 1px solid #ddd; padding: 8px;">CC</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>forcePgid</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Forces identification for payment gateway.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">PG123</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>partnerHoldTime</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Time held by the partner for the transaction.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">60</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>userCredentials</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Credentials for user authentication.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">string</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>userToken</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Token for the customer.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">user_token_123</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>subventionAmount</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Amount paid through EMI subvention payments.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">100</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>authOnly</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Initiates an authentication-only payment (true/false).</td>
  <td style="border: 1px solid #ddd; padding: 8px;">false</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>createOrder</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">A flag to store the order details (true/false).</td>
  <td style="border: 1px solid #ddd; padding: 8px;">true</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>txnS2sFlow</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">For defining seamless/non-seamless flows in handling payments.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">seamless</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>