---
name: V2_order_object
---
<HTMLBlock>{`
| Parameter | Description | Example |
|---|---|---|
| productInfo<br/><code>mandatory</code> | Product details. Type: <code>String</code> | Product details |
| orderedItem<br/><code>optional</code> | Details about the items ordered. Type: <code>Array of Objects</code> | |
| userDefinedFields<br/><code>optional</code> | Custom fields for additional information. Type: <code>Object</code>. Fields: udf1, udf2, udf3, udf4, udf5, udf6, udf7, udf8, udf9, udf10. | |
| paymentChargeSpecification<br/><code>mandatory</code> | Includes amount and charges. Type: <code>Object</code>. For more information, refer to [paymentChargeSpecification object fields description](#paymentChargeSpecification-object-fields-description) | |
`}</HTMLBlock>

##### paymentChargeSpecification object fields description

<HTMLBlock>{`
| Parameter | Description | Example |
|---|---|---|
| price<br/><code>mandatory</code> | The transaction amount. Type: <code>Number</code> | 1000 |
| netAmountDebit<br/><code>optional</code> | Net amount to be debited. Type: <code>Number</code> | 1000 |
| taxSpecification<br/><code>optional</code> | Tax details of the product/order. Type: <code>Object</code> | |
| convenienceFee<br/><code>optional</code> | Fees format. Type: <code>String</code> | CC:12 |
| offers<br/><code>optional</code> | Offers applied or available for the payment. Type: <code>Object</code> | |
`}</HTMLBlock>

##### userDefinedFields object fields description

| Field | Description         |
| ----- | ------------------- |
| udf1  | User defined field. |
| udf2  | User defined field. |
| udf3  | User defined field. |
| udf4  | User defined field. |
| udf5  | User defined field. |
| udf6  | User defined field. |
| udf7  | User defined field. |
| udf8  | User defined field. |
| udf9  | User defined field. |
| udf10 | User defined field. |
