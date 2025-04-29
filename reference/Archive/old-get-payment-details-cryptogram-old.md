---
title: OLD-Get Payment Details (Cryptogram)
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to get the payment details of an existing card stored on PayU Vault so that you can use it with third-party tokenization. The payment details include the cryptogram, PAR, card number, card token, issuer token details and network token details as listed in the [Response Parameters table](#response-parameters) of this section.

HTTP Method: **POST**

**Environment**

| Test Environment       | <https://test.payu.in/merchant>  |
| :--------------------- | :------------------------------- |
| Production Environment | <https://info.payu.in/merchant/> |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "key  \n**mandatory**",
    "0-1": "For more information on how to generate the Key and Salt, refer to any of the following:  \n\\- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  \n\\- **Test**:: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)",
    "0-2": "JF\\*\\*\\*g",
    "1-0": "command  \n**mandatory**",
    "1-1": "`varchar` The command name for this REST API call must be included in this parameter. For getting user cards details, use **get\\_payment\\_details** here.",
    "1-2": "get\\_payment\\_details",
    "2-0": "hash  \n**mandatory**",
    "2-1": "`varchar` The hash must be included in this parameter. The hash logic for is:  \nsha512(key|command|var1|salt) sha512",
    "2-2": " ",
    "3-0": "var1  \n**mandatory**",
    "3-1": "`varchar` The user credentials is posted in this parameter in the following format: MerchantKey:UserId",
    "3-2": "J\\*\\*\\*G:abc",
    "4-0": "var2  \n**mandatory**",
    "4-1": "`varchar` The card token of the card (cardToken) is specified in this parameter.",
    "4-2": "745d72e2fd9b7e88824fef4e7ed7dac1f",
    "5-0": "var3  \n**mandatory**",
    "5-1": "`float` The amount of the transaction",
    "5-2": "10.00",
    "6-0": "var4  \n**optional**",
    "6-1": "`varchar` The currency used for the transaction.  \n**Note**: If this parameter is left blank, the currency is considered as INR by default.",
    "6-2": "INR",
    "7-0": "var5  \n**optional**",
    "7-1": "`varchar` The cardToken type is specified in this parameter and can be any of the following:  \n**Note**: If this parameter is left blank, the default value will be PAYU.",
    "7-2": "PAYU"
  },
  "cols": 3,
  "rows": 8,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


## Sample request

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2"
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
“key=T****T&command=get_payment_details&var1=“merchant:user”&var2=60ac1025f09d1965b7dae2&var2=My_card&var3=10&var4=INR&
hash=e2f11b3818772b1851937ad6181c70b25f1dd296cb55ab507f0199c32239b76440889254e7f33c3fd111d87553d17ab4ee7a191e9cbb5d3484915ad00f4711e2”
```

## Response parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "status",
    "0-1": "The status of the response can be any of the following:  \n_ 1: Success  \n_. 2: Failure",
    "0-2": "1",
    "1-0": "msg",
    "1-1": "The description of the response whether the card details were stored successfully or not stored.",
    "1-2": "Instrument details",
    "2-0": "card details",
    "2-1": "(Array format) | The details are sent by PayU in Array format for the successful response. The next table describes the details in the Array format.",
    "2-2": "Refer the [sample response](#sample_response)."
  },
  "cols": 3,
  "rows": 3,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


The details on the Array format for a successful response is described in the following table:

[block:parameters]
{
  "data": {
    "h-0": "**Array Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "cryptogram",
    "0-1": "The cryptogram used for encryption is returned in this parameter. This can be also a TAVV. TAVV is a 20-byte Base64-encoded binary value that is used with tokens.",
    "0-2": "`0c186bdb8c0ebda30ab9d92816772cbfb946d027`",
    "1-0": "card PAR",
    "1-1": "This parameter returns the PAR (Payment Account Reference). This is a unique identity for the card across all the tokens. Typically, this will be used for offers and risk checks.",
    "1-2": "RCKGgxEEFX1un19I",
    "2-0": "card\\_no",
    "2-1": "This parameter returns a masked card number with only the last four digits.",
    "2-2": "xxxxxxxxxxxx858",
    "3-0": "card\\_token",
    "3-1": "This parameter returns the card token of the card.",
    "3-2": "745d72e2fd9b7e88824fef4e7ed7dac1fe624b7",
    "4-0": "issuer\\_token",
    "4-1": "This parameter returns the details of the issuer token in a JSON format.",
    "4-2": "{  \n  \n\"token_value\": \"512\\*\\*\\*6789012346\",  \n  \n\"is_expired\": 0,  \n  \n\"token_exp_mon\": \"11\",  \n  \n\"token_exp_yr\": \"2021\",  \n  \n\"token_bin\": \"512345\"  \n  \n}",
    "5-0": "network\\_token",
    "5-1": "This parameter returns the details of the network token in a JSON format.",
    "5-2": "{  \n  \n\"token_value\": \"512\\*\\*\\*6789012346\",  \n  \n\"is_expired\": 0,  \n  \n\"token_exp_mon\": \"11\",  \n  \n\"token_exp_yr\": \"2021\",  \n  \n\"token_bin\": \"512345\"  \n  \n}"
  },
  "cols": 3,
  "rows": 6,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


## Sample response

### Successful scenario

```plaintext
{
    "status": "1",
    "msg": "Instrument details",
    "details": {
        "one_click_status": "",
        "one_click_flow": "",
        "card_type": "VISA",
        "network_token": {
            "token_exp_yr": "2025",
            "token_value": "464***7450050615",
            "token_exp_mon": "01"
        },
        "trid": "400600",
        "card_mode": "",
        "token_refernce_id": "477***84a5079512934417214171fd01",
        "card_no": "XXXXXXXXXXXX0615",
        "card_PAR": "V0010013021031409361532",
        "one_click_card_alias": "",
        "card_token": "60ac1025f09d1965b7dae2",
        "card_name": "",
        "cryptogram": "/wAAAAoAtd1XnhwAmbHTgkUAAAA="
    }
}
```

### Failure scenario

```plaintext
{
"status": 0,
"msg": card not found
}
```