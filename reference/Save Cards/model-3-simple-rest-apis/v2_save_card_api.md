---
title: Save Card API
deprecated: false
hidden: false
metadata:
  robots: index
---
The v2 **Save Card** API is used for saving a card to the vault. After successfully storing a card, it returns the `cardToken`. This is Save

HTTP Method: **POST**

**Environment**

|                        |                                                                                  |
| :--------------------- | :------------------------------------------------------------------------------- |
| Production Environment | [https://info.payu.in/storecard/card/v1](https://info.payu.in/storecard/card/v1) |
|                        | [https://test.payu.in/storecard/card/v1](https://test.payu.in/storecard/card/v1) |

## Request Parameters

### Authentication header

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
        date  
        `mandatory`
      </td>

      <td>
        The current date and time. For example, format of the date is Wed, 28 Jun 2023 11:25:19 GMT.
      </td>
    </tr>
  </tbody>
</Table>

### Body parameters

| Parameter                                               | Reference                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Example                |
| :------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| userCredential<br />`mandatory`                         | `String` The user credentials are posted in this parameter in the following format: MerchantKey:UserId                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | JP***G:abc             |
| cardLabel<br />`mandatory`                              | `String` The nickname of the card is specified in this parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | My_card                |
| cardType<br />`mandatory`                               | `String` The card mode is specified in this parameter. For more information on card mode codes, refer to [Card Type Codes and Supported Banks for Cards](https://docs.payu.in/v1/docs/card-type-codes-and-supported-banks-for-cards).                                                                                                                                                                                                                                                                                                                                                                                              | CC                     |
| cardType<br />`mandatory`                               | `String` The card type of the card is specified in this parameter. For more information on card type codes, refer to [Card Type Codes and Supported Banks for Cards](https://docs.payu.in/v1/docs/card-type-codes-and-supported-banks-for-cards)                                                                                                                                                                                                                                                                                                                                                                                   | AMEX                   |
| nameOnCard<br />`mandatory`                             | `String` The name on the card is specified in this parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Ashish                 |
| cardNo<br />`mandatory`                                 | `String` The card number is specified in this parameter. For the **test cards** to do mock API calls, refer to [Test Cards, UPI ID and Wallets](https://docs.payu.in/v1/docs/test-cards-upi-id-and-wallets).                                                                                                                                                                                                                                                                                                                                                                                                                       |                        |
| cardExpiryMonth<br />`mandatory`                        | `String` The card expiry month is specified in this parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 9                      |
| cardExpiryYear<br />`mandatory`                         | `String` The card expiry year is specified in this parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 2021                   |
| authRefNumber<br />`mandatory for Rupay and AMEX cards` | `String` This parameter can be any of the following based on the Rupay or AMEX card used:<br />• The authorization reference number received during authorization call of Rupay card transactions.<br />• The AEVV received during authorization call of Amex card transactions.<br />**Notes**:<br />• This parameter is mandatory for Rupay cards. Authentication reference number will be sent by the PG in the authorization response. Currently, this check is skipped by Rupay.<br />• This parameter is mandatory for AMEX cards. American Express Verification Value will be sent by the PG in the authorization response. | 6381242223626382106105 |

## Sample request

```
curl --location 'https://test.payu.in/storecard/card/v1)' \
  --header 'authorization: {{authorization}}' \
  --header 'date: {{date}}'
  --data '{
    "userCredential":"sms:123",
    "cardName":"testAll",
    "cardMode":"CC",
    "cardType":"CC",
    "nameOnCard":"test",
    "cardNo":"4761360079851258",
    "cardExpiryMonth":12,
    "cardExpiryYear":2025,
    "authRefNumber":"asd"
}'
```

## Sample response

### Success scenario

```json
{
  "message": "Card Stored Successfully.",
  "status": 1,
  "result": {
    "cardToken": "18cc810671348c3d3241",
    "cardNo": "XXXXXXXXXXXX1258",
    "cardName": "testAll",
    "networkToken": "4761360000000009"
  }
}
```

### Success scenarios for various cards

#### VISA

```json
{
status: 1,
msg: "Card Stored Successfully.",
"result": {
   "cardToken": "917757449926e57ff2662",
   "cardNo": "XXXXXXXXXXXX1165",
   "cardLabel": "My_card",
   "networkToken": "44173XXX1000XXX1",
   "issuerToken": "QQ3LkzgZOnEjY428"
  }
}
```

#### Mastercard

```json
{
  "status": 1,
  "msg": "Card Stored Successfully.",
  "result": {
    "cardToken": "917e296b5b6da5d20fbfb",
    "cardNo": "XXXXXXXXXXXX2346",
    "cardLabel": "Test_Card",
    "networkToken": "3117328711111210",
    "issuerToken": "AQ3LkzgBNyEjY213"
  }
}
```

#### American Express

```json
{
  "status": 1,
  "msg": "Card Stored Successfully.",
  "result": {
    "cardToken": "917e29XXX6da5XXCbfb",
    "cardNo": "XXXXXXXXXXX1002",
    "cardLabel": "AMEX_Card",
    "networkToken": "51273287XXX61215",
    "issuerToken": "Va3RaqBNyPnY673"
  }
}
```

#### Rupay

```json
{
  "status": 1,
  "msg": "Card Stored Successfully.",
  "result": {
    "cardToken": "91XXX96b5b6da5dXXXbfb",
    "cardNo": "XXXXXXXXXXXX0001",
    "cardLabel": "Rupay_Card",
    "networkToken": "712XXX870976XX2",
    "issuerToken": "Ya4HawKgbLmr312"
  }
}
```

#### Diners

```json
{
  "status": 1,
  "msg": "Card Stored Successfully.",
  "result": {
    "cardToken": "91XXX296b5b6da5XXXbfb",
    "cardNo": "XXXXXXXXXXXX0009",
    "cardLabel": "Diner_Card",
    "networkToken": "8koNXXXC1bT0Hv5a",
    "issuerToken": "LQ3QkzXXXnEjY428"
  }
}
```

### Failure scenario

* If card Number is invalid

```plaintext
{
"status": 0
"msg": CardNumber is invalid
}
```

## Response parameters for Save a Card API

The following table describes the parameters in the response:

<Callout icon="📘" theme="info">
  **Note**: For every successful payment transactions, PayU returns the **mihpayuid** and **cardToken** parameters to the merchants, but networkToken and issuer_token are returned only if you are PCI-DSS compliant.
</Callout>

| Parameter | Description                                                                                                                                         | Example                   |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| message   | The description of the response whether the card details were stored successfully or not stored.                                                    | Card Stored Successfully. |
| status    | The status of the response can be any of the following:<br />• 1: Success<br />• 0: Failure                                                         | 1                         |
| result    | This contains the token details in a JSON format. For more information, refer to [result JSON fields description](#result-json-fields-description). |                           |

### result JSON fields description

| Parameter     | Description                                                         | Example               |
| ------------- | ------------------------------------------------------------------- | --------------------- |
| cardToken     | The cardToken is sent by PayU for the successful response.          | 18_**1067**_8c3d3241  |
| cardNo        | The redacted card number with last four digits that was saved.      | XXXXXXXXXXXX1258      |
| cardName      | The name on card that was saved.                                    | testAll               |
| network_token | The network token is returned in this parameter.                    | `1234 5*** 9*** 3456` |
| issuer_token  | The parameter contains the issuer token that is returned by issuer. | `3456 7*** A*** EFGH` |
