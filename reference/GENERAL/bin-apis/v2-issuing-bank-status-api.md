---
title: ' Issuing Bank Status API'
deprecated: false
hidden: false
metadata:
  robots: index
---
**Environment**

<br />

|            |                                                                                      |
| :--------- | :----------------------------------------------------------------------------------- |
| Production | [https://info.payu.in/issuing-bank/v1/bin](https://info.payu.in/issuing-bank/v1/bin) |
| Test       | [https://test.payu.in/issuing-bank/v1/bin](https://test.payu.in/issuing-bank/v1/bin) |

# Request header

<V2_payment_header_params />

## Query parameters

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>bin<br/><code>mandatory</code></td>
      <td><code>String</code> The first 6 digits of the card number (Bank Identification Number) to get issuing bank information.</td>
      <td>512345</td>
    </tr>
    <tr>
      <td>issuing_bank_status<br/><code>optional</code></td>
      <td><code>Boolean</code> Flag to include issuing bank status information in the response.</td>
      <td>true</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Request body

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>bin<br/><code>mandatory</code></td>
      <td><code>String</code> The first six digits ofcard (card BIN) must be specified here.</td>
      <td>512345</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

<br />

## Sample request

```
curl --location 'https://info.payu.in/issuing-bank/v1/bin/?bin=512345&issuing_bank_status=true' \
--header 'Content-Type: application/json' \
--header 'date: {{date}}' \
--header 'Authorization: {{authorization}}' \
--data '{
    "bin": "512345"
  }'
```

## Response parameters

The response parameters for a bank code passed in **var1**, it returns a response for the specified bank alone with the parameters as explained in the following table. If the **default** value is passed in **var1**, it returns a array of all the banks in a JSON array format and each JSON has the list of fields similar to the parameter list:

<HTMLBlock>{`
  <table>
    <thead>
      <tr>
        <th>
          **Parameter/JSON Field**
        </th>

        <th>
          **Description**
        </th>

        <th>
          **Example**
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          ibibo\_code
        </td>

        <td>
          This parameter contains the bank code for which the Net Banking status is displayed.
        </td>

        <td>
          AXIB
        </td>
      </tr>

      <tr>
        <td>
          title
        </td>

        <td>
          This parameter contains the bank name and service.
        </td>

        <td>
          AXIS Bank NetBanking
        </td>
      </tr>

      <tr>
        <td>
          up\_status
        </td>

        <td>
          This parameter contains the status of the NetBanking service and can be any of the following:

          * 0 - signifies that the particular Bank option is down at the moment
          * 1 - signifies that the particular Banking option is up at the moment
        </td>

        <td>
          1
        </td>
      </tr>

      <tr>
        <td>
          mode
        </td>

        <td>
          This parameter contains the mode of payment for which the status is displayed.
        </td>

        <td>
          NB
        </td>
      </tr>
    </tbody>
  </table>
</details>
`}</HTMLBlock>

## Sample response

```
{
    "message": "Success",
    "status": 1,
    "result": {
        "status": 0,
        "category": "creditcard",
        "bin": "512345",
        "is_domestic": false,
        "card_type": "MAST",
        "issuing_bank": "UNKNOWN",
        "otp_on_fly": false,
        "issuing_bank_status": 1,
        "is_atmpin_card": 1,
        "oobEligible": false
    }
}
```