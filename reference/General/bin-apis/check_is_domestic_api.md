---
title: Check is Domestic API
excerpt: ''
api:
  file: check-is-domestic-api-1.json
  operationId: checkisdomestic
deprecated: false
hidden: false
metadata:
  title: Check is Domestic API
  description: >-
    The document describes the Check is Domestic or Card BIN API, which is used
    to determine if a BIN number is international or domestic, along with other
    card details like issuing bank and card type.
  keywords:
    - check_isDomestic API Command
    - Check is Domestic API
    - Domestic transaction check API
    - Domestic transaction identification API
    - Check domestic payment API
    - Verify domestic transaction API
    - Integrating PayU Check is Domestic API
  robots: index
next:
  description: ''
---
The **Check is Domestic** or **Card BIN** API is used to detect whether a particular BIN number is international or domestic. It is also useful to determine: 

* card's issuing bank
* card type such as, Visa, Master, etc.,
* card category such as Credit/Debit, etc. 
* var1 is bin number which is the first 6 digits of a Credit/Debit card.

| Environment | URL |
| ----------- | --- |
| Test Environment | https://test.payu.in/merchant/postservice.php?form=2 |
| Production Environment | https://info.payu.in/merchant/postservice?form=2 |

<details>
  <summary>Sample request</summary>

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&command=check_isDomestic&var1=462273&hash=df4ff56008defd9d7f9bf09506061f5c790dbe1d011659d85b88d34323ff49a65181e522eddf3075285c17708566709c803d3b0b0979120804b00f62236062a2"
```

</details>

<details>
  <summary>Sample response</summary>

If the card is domestic

```json
{
      "isDomestic": "Y",
      "issuingBank": "SCB",
      "cardType": "VISA",
      "cardCategory": "CC"
}
```

If the card is international

```json
{
      "isDomestic": "N",
      "issuingBank": "UNKNOWN",
      "cardType": "Unknown",
      "cardCategory": "CC"
}
```

</details>

<details>
  <summary>Response parameters description</summary>

{/* Properly formatted JSX Table */}
<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        isDomestic
      </td>

      <td>
        Response value can contain any of the following:  

        * **Y** signifies that the particular BIN is domestic.
        * **N** signifies that the particular BIN is International.
      </td>
    </tr>

    <tr>
      <td>
        cardType
      </td>

      <td>
        Response value can contain any of the following:  

        * MAST
        * VISA
        * MAES
        * AMEX
        * DINER
        * Unknown
      </td>
    </tr>

    <tr>
      <td>
        issuingBank
      </td>

      <td>
        The issuing bank of the card used for the transaction.
      </td>
    </tr>

    <tr>
      <td>
        cardCategory
      </td>

      <td>
        Response value can contain any of the following:  

        * **CC** signifies that the particular bin is a credit card BIN
        * **DC** signifies that the particular bin is a debit card BIN
      </td>
    </tr>
  </tbody>
</Table>

To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).

</details>

## Request parameters

<details>
  <summary>Reference information</summary>

{/* Properly formatted JSX Table with align attribute */}
<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Reference
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        {/* Properly formatted JSX component */}
        <Glossary>key</Glossary>
      </td>

      <td>
        For more information on how to generate the Key and Salt, refer to any of the following:  

        - **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  
        - **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
      </td>
    </tr>

    <tr>
      <td>
        {/* Properly formatted JSX component */}
        <Glossary>hash</Glossary>
      </td>

      <td>
        Hash logic for this API is:
        ```
        sha512(key|command|var1|salt) sha512
        ```
      </td>
    </tr>

    <tr>
      <td>
        var1
      </td>

      <td>
        For JSON fields description, refer to [Additional Info for General APIs](ref:addl-info-general-apis)
      </td>
    </tr>
  </tbody>
</Table>

</details>

Use the following sample values while trying out the API:

**Example values**

* `var1` (first six digit of the card): 512345.
