---
name: CallbackActions_object
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
  <td style="border: 1px solid #ddd; padding: 8px;">successAction<br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">URL to be called on payment success.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">https://example.com/success</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">failureAction<br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">URL to be called on payment failure.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">https://example.com/failure</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">cancelAction<br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">URL to be called if user cancels the payment.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">https://example.com/cancel</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">codAction<br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">URL for Cash on Delivery (COD) action.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">https://example.com/cod</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>