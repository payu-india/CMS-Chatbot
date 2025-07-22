---
name: V2_order_object
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
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>productInfo</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Product details.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Product details</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>orderedItem</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Details about the items ordered.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Array of Objects</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>userDefinedFields</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Custom fields for additional information. Fields: udf1, udf2, udf3, udf4, udf5, udf6, udf7, udf8, udf9, udf10.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>paymentChargeSpecification</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Includes amount and charges.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>