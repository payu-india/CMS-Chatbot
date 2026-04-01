---
title: Get Payment Details API
deprecated: false
hidden: false
metadata:
  robots: index
---
This API allows merchants to retrieve payment details for a stored card token.

HTTP Method:  **GET**

**Environment**

|            |                                                                                                        |
| :--------- | :----------------------------------------------------------------------------------------------------- |
| Test       | [https://test.payu.in/storecard/card/v1/cryptogram](https://test.payu.in/storecard/card/v1/cryptogram) |
| Production | [https://info.payu.in/storecard/card/v1/cryptogram](https://info.payu.in/storecard/card/v1/cryptogram) |

## Request header

### Authorization header

<HeaderAuthentication />

### Header parameters

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        mid
        `mandatory`
      </td>

      <td>
        Merchant ID provided by PayU. Use the value provided in your PayU dashboard.
      </td>
    </tr>

    <tr>
      <td>
        date  
        `mandatory`
      </td>

      <td>
        The current date and time. For example, format of the date is Wed, 28 Jun 2023 11:25:19 GMT.
      </td>
    </tr>
  </tbody>
</Table>

### Query parameters

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        userCredential
        `mandatory`
      </td>

      <td>
        `String` Encrypted user credentials, typically `<username>:<password>`.
      </td>
    </tr>

    <tr>
      <td>
        cardToken
        `mandatory`
      </td>

      <td>
        `String`Token for the card whose payment details are being fetched.
      </td>
    </tr>

    <tr>
      <td>
        amount
        `mandatory`
      </td>

      <td>
        `String`Amount to validate or process for this payment.
      </td>
    </tr>

    <tr>
      <td>
        currency_type
        `mandatory`
      </td>

      <td>
        `String`Currency in which the payment is being processed.
      </td>
    </tr>

    <tr>
      <td>
        tokenType
        `mandatory`
      </td>

      <td>
        `String`Type of token.
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```bash
curl --location --request GET 'https://test.payu.in/storecard/card/v1/cryptogram?userCredential=testuser%3Atestuser123&cardToken=9350516de374f7bab4cd2&amount=10&currency_type=INR&tokenType=null' \
  --header 'date: {{date}}' \
  --header 'Authorization: {{authorization}}' \
```

## Sample response

```json
{
  "message": "Instrument details",
  "status": 1,
  "result": {
    "oneClickFlow": "",
    "oneClickStatus": "",
    "cardType": "VISA",
    "trid": "400000340044",
    "networkToken": {
      "tokenValue": "4761360000000009",
      "tokenExpiryMonth": 12,
      "tokenExpiryYear": 2026
    },
    "cardMode": "",
    "par": "ZCLY85YBYQ4Q8D6162O8M0V414GK7",
    "tokenReferenceId": "3dc50cce023cf4d7dd243c9af272c5c6",
    "cardNo": "XXXXXXXXXXXX1258",
    "oneClickCardAlias": "",
    "cardToken": "9350516de374f7bab4cd2",
    "cardName": "",
    "cryptogram": "AgAAAGQBdCZtW8sAmbHTg0UAAAA="
  }
}
```

## Response parameters

| Parameter | Description                                                                                                                         | Example              |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| message   | Response message indicating the operation result.                                                                                   | `Instrument details` |
| status    | Status code for the operation. `1` for success, `0` for failure.                                                                    | `1`                  |
| result    | Result of response in JSON format. For more information, refer to [result JSON fields description](#result-josn-fields-description) |                      |

### result JSON fields description

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
        cardType
      </td>

      <td>
        Card type.
      </td>

      <td>
        `AMEX`
      </td>
    </tr>

    <tr>
      <td>
        trid
      </td>

      <td>
        Transaction ID.
      </td>

      <td>
        `400000340055`
      </td>
    </tr>

    <tr>
      <td>
        networkToken
      </td>

      <td>
        The field contains the following fields:

        * **tokenValue**: The actual card/network token.
        * **tokenExpiryMonth**: Token expiry month.
        * **tokenExpiryYear**: Token expiry year.
      </td>

      <td>
        `3711110000000001`
      </td>
    </tr>

    <tr>
      <td>
        par
      </td>

      <td>
        Payment Account Reference.
      </td>

      <td>
        `LI0K7PL4VJNHJZ6LVQ7LWXHGD3LPS`
      </td>
    </tr>

    <tr>
      <td>
        cardNo
      </td>

      <td>
        Masked card number.
      </td>

      <td>
        `XXXXXXXXXXXX1114`
      </td>
    </tr>

    <tr>
      <td>
        cardToken
      </td>

      <td>
        Card token.
      </td>

      <td>
        `1817ca29b7cdd28a0e406`
      </td>
    </tr>

    <tr>
      <td>
        cryptogram
      </td>

      <td>
        Generated encrypted string for payment security.
      </td>

      <td>
        `AgAAAGQBdCZtW8sAmbHTg0UAAAA=`
      </td>
    </tr>
  </tbody>
</Table>
