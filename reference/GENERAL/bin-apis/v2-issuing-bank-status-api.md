---
title: ' Issuing Bank Status API'
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Get Issuing Bank Status** API (**getIssuingBankStatus**) is used to help you handle the credit card or debit card issuing bank downtime.

**Environment**

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
      <td><code>String</code> The first 6 digits of the card number (Bank Identification Number) to get issuing bank status.</td>
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
      <th>Parameter</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>message</td>
      <td><code>String</code> Response message indicating the status of the API call.</td>
      <td>Success</td>
    </tr>
    <tr>
      <td>status</td>
      <td><code>Integer</code> Overall status code of the API response.</td>
      <td>1</td>
    </tr>
    <tr>
      <td>result</td>
      <td><code>Object</code> Contains detailed information about the BIN and issuing bank details. For more information, refer to <a href="#result-object-fields-description"> result object fields description</a></td>
      <td>Refer to <a href="#result-object-fields-description">result object fields description</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

### result object fields description

Sample object

```
 {
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
```

Fields description

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Field</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>status</td>
      <td><code>Integer</code> Status code specific to the BIN lookup result.</td>
      <td>0</td>
    </tr>
    <tr>
      <td>category</td>
      <td><code>String</code> Category of the card (e.g., creditcard, debitcard).</td>
      <td>creditcard</td>
    </tr>
    <tr>
      <td>bin</td>
      <td><code>String</code> The Bank Identification Number (first 6 digits of the card).</td>
      <td>512345</td>
    </tr>
    <tr>
      <td>is_domestic</td>
      <td><code>Boolean</code> Indicates whether the card is domestic (true) or international (false).</td>
      <td>false</td>
    </tr>
    <tr>
      <td>card_type</td>
      <td><code>String</code> Type of card network (MAST, VISA, AMEX, etc.).</td>
      <td>MAST</td>
    </tr>
    <tr>
      <td>issuing_bank</td>
      <td><code>String</code> Name of the issuing bank or "UNKNOWN" if not identified.</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <td>otp_on_fly</td>
      <td><code>Boolean</code> Indicates if the card supports OTP on the fly authentication.</td>
      <td>false</td>
    </tr>
    <tr>
      <td>issuing_bank_status</td>
      <td><code>Integer</code> Status code for the issuing bank information.</td>
      <td>1</td>
    </tr>
    <tr>
      <td>is_atmpin_card</td>
      <td><code>Integer</code> Indicates if the card supports ATM PIN authentication (1 = yes, 0 = no).</td>
      <td>1</td>
    </tr>
    <tr>
      <td>oobEligible</td>
      <td><code>Boolean</code> Indicates if the card is eligible for out-of-band authentication.</td>
      <td>false</td>
    </tr>
  </tbody>
</table>
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