---
title: v2 Get Payment Details API
deprecated: false
hidden: true
metadata:
  robots: index
---
This API allows merchants to retrieve payment details for a stored card token.

HTTP Method:  **GET**

**Endpoint**

* **Production Environment**: `<info.storecard.service.url>/storecard/card/v1/cryptogram`

## Request Headers

<V2_payment_header_params />

## Request parameters

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
        tokenType
        `mandatory`
      </td>

      <td>
        `String`Type of token.
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
        currencyType
        `mandatory`
      </td>

      <td>
        `String`Currency in which the payment is being processed.
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```bash
curl --location '<info.storecard.service.url>/storecard/card/v1/cryptogram' \
--header 'Content-Type: application/json' \
--header 'mid: 2' \
--data '{
    "userCredential": "sartaj:info",
    "tokenType": "PayUToken",
    "cardToken": "1817ca29b7cdd28a0e406",
    "amount": "10",
    "currencyType": "INR"
}'
```

## Sample response

```json
{
    "message": "Instrument details",
    "status": 1,
    "result": {
        "oneClickFlow": "",
        "oneClickStatus": "",
        "cardType": "AMEX",
        "trid": "400000340055",
        "networkToken": {
            "tokenValue": "3711110000000001",
            "tokenExpiryMonth": 10,
            "tokenExpiryYear": 2026
        },
        "cardMode": "",
        "par": "LI0K7PL4VJNHJZ6LVQ7LWXHGD3LPS",
        "tokenReferenceId": "a98d513e56cbc4ef2fdb603ceb1027b2",
        "cardNo": "XXXXXXXXXXXX1114",
        "oneClickCardAlias": "",
        "cardToken": "1817ca29b7cdd28a0e406",
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