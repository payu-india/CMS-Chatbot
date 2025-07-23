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
  <td style="border: 1px solid #ddd; padding: 8px;">eci<br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Electronic Commerce Indicator.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">05</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">cavv<br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Cardholder Authentication Verification Value.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">AAABAWFlmQAAAABjRWWZEEFgFz</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">pares<br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Payer Authentication Response for 3D Secure 1.0.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">eJzVWFmTokoWfrMABXXOtgSL...</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">bankData<br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Additional bank data for processing the payment.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">fGpDiuSMy8FjxQHDla5kFwVr</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">messageDigest<br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Security hash value for message verification.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">3a4df2b5c8e7f9a1d6b0c3e9</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">xid<br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Transaction identifier for 3D Secure authentication.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">MDAwMDAwMDAwMDAwMDAwMDEyMzQ=</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">threeDSenrolled<br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Indicates if the card is enrolled in 3D Secure.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Y</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">threeDSstatus<br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Status of the 3D Secure authentication.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">SUCCESS</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">flowType<br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Flow type for 3D Secure.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Frictionless</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">threeDSTransID<br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">3DS Transaction ID.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">67b4c71f-19bf-4d97-bd09-4e3687dc9e42</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">threeDSServerTransID<br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">3DS Server Transaction ID.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">eea30d14-71cf-41af-b961-f95b7d67dc93</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">threeDSTransStatus<br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">3DS transaction status.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Y</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">threeDSTransStatusReason<br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Reason for 3DS transaction status.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">01</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">aquirer_bin<br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Bank Identification Number of the acquirer.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">401200</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object containing additional authorization information including payment gateway identifier, authentication flow, 3DS2 request data, and user-defined fields.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo.paymentGatewayIdentifier</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Identifier for the payment gateway.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">gateway_123</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo.authenticationFlow</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Type of authentication flow used.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">3DS2</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo.threeDS2RequestData</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object containing 3DS2 request data.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">{}</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo.authUdf1</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">User-defined field 1 for additional authorization data.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">custom_value_1</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo.authUdf2</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">User-defined field 2 for additional authorization data.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">custom_value_2</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo.authUdf3</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">User-defined field 3 for additional authorization data.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">custom_value_3</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo.authUdf4</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">User-defined field 4 for additional authorization data.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">custom_value_4</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo.authUdf5</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">User-defined field 5 for additional authorization data.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">custom_value_5</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo.authUdf6</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">User-defined field 6 for additional authorization data.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">custom_value_6</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo.authUdf7</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">User-defined field 7 for additional authorization data.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">custom_value_7</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo.authUdf8</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">User-defined field 8 for additional authorization data.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">custom_value_8</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo.authUdf9</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">User-defined field 9 for additional authorization data.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">custom_value_9</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo.authUdf10</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">User-defined field 10 for additional authorization data.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">custom_value_10</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>