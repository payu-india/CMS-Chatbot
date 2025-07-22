---
name: V2_paymentCard
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
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>cardNumber</strong><br/><code>mandatory for physical card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Card number.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">5497774415170603</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>validThrough</strong><br/><code>mandatory for physical card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Expiry date in MM/YYYY format.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">05/2025</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>ownerName</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Name of the card owner.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Ashish</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>cvv</strong><br/><code>mandatory for physical card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">CVV number of the card.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">123</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>tavv</strong><br/><code>mandatory for saved card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Cryptogram of the card for tokenized payments.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">AAABAWFlmQAAAABjRWWZEEFgFz</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>last4Digits</strong><br/><code>mandatory for saved card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Last four digits of the card.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">0603</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>cardTokenType</strong><br/><code>mandatory for saved card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Card token type. Valid values: PAYU, NETWORK, ISSUER.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">PAYU</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>cardToken</strong><br/><code>mandatory for saved card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Card token of the stored card.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">b5f2d8785768087678fm9</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>