---
title: Save a Card API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Save a Card API
  description: >-
    The Save a Card API allows merchants to securely save customer card details
    to the PayU vault. This API returns a card token upon successful storage,
    ensuring compliance with RBI guidelines by requiring customer consent and
    additional authentication. Learn how to implement this API with detailed
    request parameters, sample requests, and environment configurations.
  keywords:
    - AEVV
    - save card
    - saved card API
    - authorization reference number
    - AMEX AEVV
    - American Express Verification Value
  robots: index
next:
  description: ''
---
The Save Card API is used for saving a card to the vault. After successfully storing a card, it returns the `cardToken`.

> 📘 Note
> 
> As per RBI guidelines, taking consent from the customer and doing an additional factor of authentication is mandatory to tokenize the card. You must ensure this is done before using this API.

HTTP Method: **POST** 

**Environment**

|                        |                                                           |
| :--------------------- | :-------------------------------------------------------- |
| Test Environment       | <https://apitest.payu.in/merchant/postservice.php?form=2> |
| Production Environment | <https://info.payu.in/merchant/postservice?form=2>        |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Reference",
    "h-2": "Example",
    "0-0": "key  \n`mandatory`",
    "0-1": "`String` The merchant key provided by PayU while onboarding.  \nFor more information on how to generate the Key and Salt, refer to any of the following:  \n  \n- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)\n- **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)",
    "0-2": "JP**\\***g",
    "1-0": "command  \n`mandatory`",
    "1-1": "`String`The command name for this REST API call must be included in this parameter. For getting user cards details, use **save_payment_instrument** here.",
    "1-2": "save_payment_instrument",
    "2-0": "hash  \n`mandatory`",
    "2-1": "`String`The hash must be included in this parameter. Hash logic for this API is:  \n`sha512(key\\|command\\|var1\\|salt) sha512 \n`",
    "2-2": "",
    "3-0": "var1  \n`mandatory`",
    "3-1": "`String`The user credentials are posted in this parameter in the following format: MerchantKey:UserId",
    "3-2": "JP\\*\\*\\*G:abc",
    "4-0": "var2  \n`mandatory`",
    "4-1": "`String`The nickname of the card is specified in this parameter.",
    "4-2": "My_card",
    "5-0": "var3  \nmandatory",
    "5-1": "`String`The card mode is specified in this parameter. For more information on card mode codes, refer to [Card Type Codes and Supported Banks for Cards](doc:card-type-codes-and-supported-banks-for-cards).",
    "5-2": "CC",
    "6-0": "var4  \n`mandatory`",
    "6-1": "`String`The card type of the card is specified in this parameter. For more information on card type codes, refer to [Card Type Codes and Supported Banks for Cards](doc:card-type-codes-and-supported-banks-for-cards)",
    "6-2": "AMEX",
    "7-0": "var5  \n`mandatory`",
    "7-1": "`String`The name on the card is specified in this parameter.",
    "7-2": "Ashish",
    "8-0": "var6  \n`mandatory`",
    "8-1": "`String`The card number is is specified in this parameter. For the **test cards** to do mock API calls, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).",
    "8-2": "",
    "9-0": "var7  \n`mandatory`",
    "9-1": "`String`The card expiry month is specified in this parameter.",
    "9-2": "9",
    "10-0": "var8  \n`mandatory`",
    "10-1": "`String`The card expiry year is specified in this parameter.",
    "10-2": "2021",
    "11-0": "var9  \n`mandatory for Rupay and AMEX cards`",
    "11-1": "`String`This parameter can be any of the following based on the Rupay or AMEX card used:  \n  \n- The authorization reference number received during authorization call of Rupay card transactions.\n- The <<glossary:AEVV>> received during authorization call of Amex card transactions.  \n  **Notes**:\n- This parameter is mandatory for Rupay cards. Authentication reference number will be sent by the PG in the authorization response. Currently, this check is skipped by Rupay.\n- This parameter is mandatory for AMEX cards. American Express Verification Value will be sent by the PG in the authorization response.",
    "11-2": "6381242223626382106105",
    "12-0": "var10  \n`optional`",
    "12-1": "`String`This parameter must be set to **true** if the transaction authentication has been done for the tokenisation.",
    "12-2": "true",
    "13-0": "var11  \n`optional`",
    "13-1": "`String`This parameter must be set to **true** if the user has given consent to tokenise the card.",
    "13-2": "true"
  },
  "cols": 3,
  "rows": 14,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Sample request

```curl
curl --request POST \
     --url '
https://test.payu.in/merchant/postservice?form=2'
\
     --header 'Content-Type: application/x-www-form-urlencoded' \
     --header 'accept: text/html; charset=UTF-8' \
     --data key=JPM7Fg \
     --data command=save_payment_instrument \
     --data var1=JPM7Fg:abc \
     --data var2=visaraghu \
     --data var3=CC \
     --data var4=CC \
     --data var5=ashish \
     --data var6=4895370077346937 \
     --data var7=11 \
     --data var8=25 \
     --data var10=true \
     --data var11=true \
     --data hash=7487417efc1e8f1aadd72ac35b410d74c94dbc21b21e01d5ac7b91db0f0d01705986d2d2094ab12fab6e794a4b54bd9c7aaaca2648ce2916bb5c9365ff95f3a3
```

## Sample response

### Success scenarios

- VISA

```plaintext
{
status: 1,
msg: "Card Stored Successfully.",
cardToken: "917757449926e57ff2662",
card_number: "XXXXXXXXXXXX1165",
card_label: "My_card",
network_token: "44173XXX1000XXX1",
issuer_token: QQ3LkzgZOnEjY428,
}
```

- Mastercard

```plaintext
{
status: 1,
msg: "Card Stored Successfully.",
cardToken: "917e296b5b6da5d20fbfb",
card_number: "XXXXXXXXXXXX2346",
card_label: "Test_Card",
network_token: “3117328711111210”,
issuer_token: AQ3LkzgBNyEjY213,
}
```

- American Express

```plaintext
{
status: 1,
msg: "Card Stored Successfully.",
cardToken: "917e29XXX6da5XXCbfb",
card_number: "XXXXXXXXXXX1002",
card_label: "AMEX_Card",
network_token: “51273287XXX61215”,
issuer_token: Va3RaqBNyPnY673,
}
```

- Rupay

```plaintext
{
status: 1,
msg: "Card Stored Successfully.",
cardToken: "91XXX96b5b6da5dXXXbfb",
card_number: "XXXXXXXXXXXX0001",
card_label: “Rupay_Card",
network_token: “712XXX870976XX2”,
issuer_token: Ya4HawKgbLmr312,
}
```

- Diners

```plaintext
{
status: 1,
msg: "Card Stored Successfully.",
cardToken: "91XXX296b5b6da5XXXbfb",
card_number: "XXXXXXXXXXXX0009",
card_label: "Diner_Card",
"network_token": "8koNXXXC1bT0Hv5a",
"issuer_token": "LQ3QkzXXXnEjY428"
}
```

### Failure scenario

- If card Number is invalid

```plaintext
{
"status": 0
"msg": CardNumber is invalid
}
```

## Response parameters for Save a Card API

The following table describes the parameters in the response:

**Note**: For every successful payment transactions, PayU returns the **mihpayuid** and **cardToken** parameters to the merchants, but networkToken and issuer\_token are returned only if you are PCI-DSS compliant.

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "status",
    "0-1": "The status of the response can be any of the following:  \n_ 1: Success   \n_  0: Failure",
    "0-2": "1",
    "1-0": "msg",
    "1-1": "The description of the response whether the card details were stored successfully or not stored.",
    "1-2": "Card Stored Successfully.",
    "2-0": "cardToken",
    "2-1": "The cardToken is sent by PayU for the successful response.",
    "2-2": "`74\\*\\*\\*2e2fd9b7e\\*\\*\\*24fef4e7ed7dac1fe624b7`",
    "3-0": "network\\_token",
    "3-1": "The network token is returned in this parameter.",
    "3-2": "`1234 5*** 9*** 3456`",
    "4-0": "issuer\\_token",
    "4-1": "The parameter contains the issuer token that is returned by issuer.",
    "4-2": "`3456 7*** A*** EFGH`"
  },
  "cols": 3,
  "rows": 5,
  "align": [
    null,
    null,
    null
  ]
}
[/block]