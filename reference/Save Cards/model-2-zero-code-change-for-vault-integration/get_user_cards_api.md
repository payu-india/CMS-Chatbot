---
title: Get User Cards API
excerpt: 'API Command: **get\_user\_cards**'
api:
  file: storecard-7.json
  operationId: GetUserCards
deprecated: false
hidden: false
metadata:
  title: Get User Cards API
  description: >-
    Learn how to use the PayU Get User Cards API to securely retrieve stored
    card details. This guide provides detailed instructions, request parameters,
    and sample responses for efficient card management
  keywords:
    - Get User Cards API
    - ' saved card retrieval'
    - ' secure card storage'
    - ' get tokenized card details'
    - ' card management'
    - ' retrieve card details'
  robots: index
next:
  description: ''
---
Use the **Get User Cards** API to get the card details of a customer in Model 2.

> 📘 Note
> 
> While PayU token is sent in payment response, the network/issuer token creation may fail. In this case, the subsequent transaction with the said PayU token may fail. Merchant can do a **get\_user\_cards API** to fetch only active/tokenized cards or listen to notification API (to be published) to maintain state at your end.

The Get User Cards API (**get\_user\_cards**) is used to fetch all the cards for a customer which were saved earlier. In this API, the card number and other sensitive information are not returned.

HTTP Method: **POST**

<GENERALAPIsEnvironment />

<details> <summary>Sample request</summary>

```curl
curl --request POST \
     --url 'https://test.payu.in/merchant/postservice.php?form=2' \
     --header 'Content-Type: application/x-www-form-urlencoded' \
     --header 'accept: text/html; charset=UTF-8' \
     --data key=JPM7Fg \
     --data command=get_user_cards \
     --data var1=JPM7Fg:abc \
     --data hash=3cba79d881a4f82daed99241d60142b1c6816b3c16c96f5a2d1cf2a09910a2e1eb440a5d70ffd232ef80cf9207f9e90378db43ad76f9f545e9dd3a3692c2de18
```

</details>

<details> <summary>Sample response</summary>

- Cards are found in the vault for PCI Compliant Merchants

```plaintext
{
    "status": 1,
    "msg": "Cards fetched Succesfully",
    "user_cards": {
        "0c186bdb8c0ebda30ab9d92816772cbfb946d027": {
            "card_no": "XXXXXXXXXXXX8548",
            "card_token": "0c186bdbXXXbda3XXXd92816772cbXXX46d027",
            "card_name": "nilesh2_card_name",
            "card_mode": "CC",
            "card_PAR": "RCKGgxEEFX1un19I",
            "card_type": "VISA",
            "issuer_token": {
                "token_value": "8koNvAdC1bT0Hv5a",
                "is_expired": 0,
                "token_exp_mon": "11",
                "token_exp_yr": "2021",
                "token_bin": "123456"
            },
            "network_token": {
                "token_value": "8koNvAdC1bT0Hv5a",
                "is_expired": 0,
                "token_exp_mon": "11",
                "token_exp_yr": "2021",
                "token_bin": "512345"
            }
        }
    }
}
```

- Response for Non-PCI Compliant Merchants

```plaintext
{
    "msg": "Cards fetched Succesfully",
    "status": 1,
    "user_cards": {
        "9e299603hd4g7201b9cf6": {
            "one_click_status": "",
            "one_click_flow": "",
            "card_type": "MAST",
            "expiry_year": "2024",
            "isDomestic": "Y",
            "issuer_name": null,
            "expiry_month": "02",
            "card_mode": "DC",
            "is_expired": "0",
            "card_cvv": 1,
            "card_no": "XXXXXXXXXXXX81",
            "one_click_card_alias": "",
            "card_token": "9e299603hd4g7201b9cf6",
            "card_name": "MASTERCARD****7781",
            "card_brand": "MAST",
            "name_on_card": "TEST",
            "card_bin": "519950"
        }
    }
}
```

- No cards are found for the user

```plaintext
{
"status": 0
"msg": Card not found.
}
```

</details>

<details> <summary> Response parameters</summary> <details>

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "status",
    "0-1": "The status of the response can be any of the following:  \n1: Success  \n  \n2: Failure",
    "0-2": "1",
    "1-0": "msg",
    "1-1": "The description of the response whether the card details were stored successfully or not stored.",
    "1-2": "Cards fetched Succesfully",
    "2-0": "user\\_cards",
    "2-1": "(JSON format) | The details are sent by PayU in JSON format for the successful response. For more information, refer to the next table.",
    "2-2": "Refer the [sample response](ref:get_user_cards_api_model3)."
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


The details on the JSON format for a successful response is described in the following table:

[block:parameters]
{
  "data": {
    "h-0": "**JSON Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "card\\_name",
    "0-1": "**Note**: This parameter has been deprecated.",
    "0-2": "NA",
    "1-0": "card\\_type",
    "1-1": "This field returns the card type code. For the list of card type codes, refer to [Card Type Codes and Supported Banks for Cards](doc:card-type-codes-and-supported-banks-for-cards).",
    "1-2": "CC",
    "2-0": "card\\_token",
    "2-1": "This field returns the PayU Token for the card.",
    "2-2": "745d72e2fXXX7e88824fef4e7ed7dXXXfe624b7",
    "3-0": "network\\_token",
    "3-1": "This field returns the details of the network token in a JSON format.",
    "3-2": "\"token_value\": \"51XXX56789012346\",  \n  \n\"is_expired\": 0,  \n  \n\"token_exp_mon\": \"11\",  \n  \n\"token_exp_yr\": \"2021\",  \n  \n\"token_bin\": \"512345\"  \n  \n}",
    "4-0": "issuer\\_token",
    "4-1": "This field returns the details of the issuer token in a JSON format.",
    "4-2": "{  \n  \n\"token_value\": \"51XXX567890XXX46\",  \n  \n\"is_expired\": 0,  \n  \n\"token_exp_mon\": \"11\",  \n  \n\"token_exp_yr\": \"2021\",  \n  \n\"token_bin\": \"512345\"  \n  \n}",
    "5-0": "is\\_expired",
    "5-1": "This field returns any of the following values to signify whether the card is active or not:  \n1: Card has expired  \n  \n0: Card is active",
    "5-2": "1",
    "6-0": "card\\_mode",
    "6-1": "This field returns the card mode.",
    "6-2": "CC",
    "7-0": "card\\_no",
    "7-1": "This field returns a masked card number with only the last four digits.",
    "7-2": "xxxxxxxxxxxx2356",
    "8-0": "card\\_brand",
    "8-1": "This field returns the card brand.",
    "8-2": "VISA",
    "9-0": "card\\_bin",
    "9-1": "**Note**: This parameter has been deprecated.",
    "9-2": "NA",
    "10-0": "token\\_bin",
    "10-1": "This field returns the token bin information of respective token type (network or issuer).",
    "10-2": "123456",
    "11-0": "card\\_PAR",
    "11-1": "This field returns the PAR (Payment Account Reference). This is a unique identity for the card across all the tokens. Typically, this will be used for offers and risk checks.",
    "11-2": "abcdefgh123456789123456789fgh",
    "12-0": "card\\_metadata",
    "12-1": "This field returns the JSON object with all the metadata and card art.",
    "12-2": " ",
    "13-0": "token\\_exp\\_yr",
    "13-1": "This field returns the expiry year of the network token.",
    "13-2": "2022",
    "14-0": "token\\_exp\\_mon",
    "14-1": "This field returns the expiry month of the network token.",
    "14-2": "10",
    "15-0": "token\\_value",
    "15-1": "The field returns the value of the network or issuer token.",
    "15-2": "51XXX5678XXX2346"
  },
  "cols": 3,
  "rows": 16,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


</details>

## Request parameters

<details> <summary>Reference info for request parameters</summary>

<KeyHashForGeneralParametersDescription />

</details>