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
  <td style="border: 1px solid #ddd; padding: 8px;">cardNumber<br/><code>mandatory for physical card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Card number.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">5497774415170603</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">validThrough<br/><code>mandatory for physical card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Expiry date in MM/YYYY format.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">05/2025</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">ownerName<br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Name of the card owner.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Ashish</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">cvv<br/><code>mandatory for physical card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">CVV number of the card.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">123</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">tavv<br/><code>mandatory for saved card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Cryptogram of the card for tokenized payments.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">AAABAWFlmQAAAABjRWWZEEFgFz</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">last4Digits<br/><code>mandatory for saved card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Last four digits of the card.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">0603</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">cardTokenType<br/><code>mandatory for saved card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Card token type. Valid values: PAYU, NETWORK, ISSUER.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">PAYU</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">cardToken<br/><code>mandatory for saved card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Card token of the stored card.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">b5f2d8785768087678fm9</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>