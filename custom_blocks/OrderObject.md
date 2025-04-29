---
name: Order object
---
### order object fields description

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        productInfo
         `mandatory`
      </td>

      <td>
        `String`Details about the product being purchased. For more information, refer to[ userDefinedFields object fields description](#userdefinedfields-object-fields-description).
      </td>
    </tr>

    <tr>
      <td>
        userDefinedFields\
         `optional`
      </td>

      <td>
        `Object`Custom fields defined by the user for additional information.
      </td>
    </tr>

    <tr>
      <td>
        paymentChargeSpecification\
         `mandatory`
      </td>

      <td>
        `Object` Payment details including amount, additional charges and PayU offers to be applied. For more information, refer to [paymentChargeSpecification object fields description](#paymentchargespecification-object-fields-description).
      </td>
    </tr>
  </tbody>
</Table>

#### userDefinedFields object fields description

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

#### paymentChargeSpecification object fields description

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        price
        `mandatory`
      </td>

      <td>
        This field must contain the price or transaction amount to be posted.
      </td>

      <td>
        10.00
      </td>
    </tr>
  </tbody>
</Table>
