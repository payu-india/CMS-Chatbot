---
title: Get Payment Details API (Crytogram)
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: Get Payment Details API
deprecated: false
hidden: false
metadata:
  robots: index
---

This API allows merchants to retrieve payment details (including the cryptogram for a network token) for a stored card token.

HTTP Method:  **POST**

**Environment**

|            |                                                                                                              |
| :--------- | :----------------------------------------------------------------------------------------------------------- |
| Test       | [https://apitest.payu.in/storecard/card/v1/cryptogram](https://apitest.payu.in/storecard/card/v1/cryptogram) |
| Production | [https://info.payu.in/storecard/card/v1/cryptogram](https://info.payu.in/storecard/card/v1/cryptogram)       |

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
        `String` Token for the card whose payment details are being fetched.
      </td>
    </tr>

    <tr>
      <td>
        amount
        `mandatory`
      </td>

      <td>
        `Number` Amount to validate or process for this payment.
      </td>
    </tr>

    <tr>
      <td>
        currency_type
        `mandatory`
      </td>

      <td>
        `String` Currency in which the payment is being processed (for example, `INR`).
      </td>
    </tr>

    <tr>
      <td>
        tokenType
        `optional`
      </td>

      <td>
        `String` Type of token. Possible values include `PAYU`, `NETWORK`, `ISSUER`, or `null`.
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```bash
curl --location --request POST 'https://apitest.payu.in/storecard/card/v1/cryptogram?userCredential=sms%3A123&cardToken=2d264984a4fa7253d4a4d9&amount=10&currency_type=INR&tokenType=PAYU' \
--header 'Content-Type: application/json' \
--header 'mid: 117256' \
--header 'date: Fri, 24 Apr 2026 09:32:42 GMT' \
--header 'Authorization: hmac username="PRiQvJ", algorithm="sha512", headers="date", signature="f65970652dcd74b0cbd00361636fe04fc340274fa4f86984580032182b7c1a8911d9c18c637504c5809f630dde189349f3aa49572274fa9e909e3edc3a19996c"' \
--header 'Cookie: PHPSESSID=krida5voc39gqosfud8tt6n8as' \
--data ''
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
            "tokenValue": "4489682380114436",
            "tokenExpiryMonth": 12,
            "tokenExpiryYear": 2034
        },
        "cardMode": "",
        "par": "V0010013021320427651459792018",
        "tokenReferenceId": "d708fb5c7273580e21d91faa506b4301",
        "cardNo": "XXXXXXXXXXXX1258",
        "oneClickCardAlias": "",
        "cardToken": "2d1e569bf1f6b150a32f70",
        "cardName": "",
        "cryptogram": "BAAAAAAAtZF+jUIAmbHTgnIAAAg="
    }
}
```

## Response parameters

| Parameter | Description                                                                                                                                              | Example              |
| :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------- |
| message   | Response message indicating the operation result.                                                                                                        | `Instrument details` |
| status    | Status code for the operation. `1` for success, `0` for failure.                                                                                         | `1`                  |
| result    | JSON object containing the payment instrument details. For more information, refer to [result JSON fields description](#result-json-fields-description). |                      |

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
        oneClickFlow
      </td>

      <td>
        A one-click flow in a saved card system is a fast, secure payment checkout experience that allows returning customers to finalize purchases with a single click or tap, without re-entering card details, CVV, or authentication codes like OTP.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        oneClickStatus
      </td>

      <td>
        Indicates whether the saved card allows the customer to complete a purchase with a single click or tap, without re-entering card details (card number, CVV, or expiry date) or undergoing additional 3D Secure authentication for every transaction.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        cardType
      </td>

      <td>
        Card type.
      </td>

      <td>
        `VISA`
      </td>
    </tr>

    <tr>
      <td>
        trid
      </td>

      <td>
        Token Reference ID assigned by the network.
      </td>

      <td>
        `400000340044`
      </td>
    </tr>

    <tr>
      <td>
        networkToken
      </td>

      <td>
        Object containing the network token details:

        * **tokenValue**: The actual card/network token.
        * **tokenExpiryMonth**: Token expiry month.
        * **tokenExpiryYear**: Token expiry year.
      </td>

      <td>
        `{ "tokenValue": "4761360000000009", "tokenExpiryMonth": 12, "tokenExpiryYear": 2026 }`
      </td>
    </tr>

    <tr>
      <td>
        cardMode
      </td>

      <td>
        Card mode (for example, `CC` for Credit Card or `DC` for Debit Card).
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        par
      </td>

      <td>
        Payment Account Reference – unique identifier for the card across environments.
      </td>

      <td>
        `ZCLY85YBYQ4Q8D6162O8M0V414GK7`
      </td>
    </tr>

    <tr>
      <td>
        tokenReferenceId
      </td>

      <td>
        Reference ID associated with the token.
      </td>

      <td>
        `3dc50cce023cf4d7dd243c9af272c5c6`
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
        `XXXXXXXXXXXX1258`
      </td>
    </tr>

    <tr>
      <td>
        oneClickCardAlias
      </td>

      <td>
        Non-sensitive, unique identifier (or token) that represents a customer's actual credit or debit card number (PAN), allowing them to make future purchases with a single click without re-entering card details.
      </td>

      <td>

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
        `9350516de374f7bab4cd2`
      </td>
    </tr>

    <tr>
      <td>
        cardName
      </td>

      <td>
        Nickname assigned to the card at the time of saving.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        cryptogram
      </td>

      <td>
        Generated encrypted string used for payment security.
      </td>

      <td>
        `AgAAAGQBdCZtW8sAmbHTg0UAAAA=`
      </td>
    </tr>
  </tbody>
</Table>
