---
title: Additional Info for Save Cards APIs
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


## Sample Response for Save Card API

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

## Response parameters for Edit Card API

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "status",
    "0-1": "The status of the response can be any of the following:  \n_ 1: Success  \n_ 0: Failure",
    "0-2": "1",
    "1-0": "msg",
    "1-1": "The description of the response whether the card details were stored successfully or not stored.",
    "1-2": "My\\_card Edited Successfully",
    "2-0": "cardToken",
    "2-1": "The card token is sent by PayU for the successful response.",
    "2-2": "`745d7XXXd9b7e88824fXXXe7ed7XXX1fe624b74`",
    "3-0": "networkToken",
    "3-1": "The network token is sent by PayU for the successful response.",
    "3-2": "`1234 5XXX XXXX 3456`",
    "4-0": "issuerToken",
    "4-1": "The issuer token is sent by PayU for the successful response.",
    "4-2": "`3456 7XXX XXXX EFGH`"
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


### Sample response

- On successful update of card details

```plaintext
{
    "status": 1,
    "msg": " edited Successfully.",
    "cardToken": "9175XXX60be0bXXX20dd8",
    "network_token": "40XXX010371XXX12",
    "issuer_token": "LQ3XXXgEOnEXXX8",
    "card_number": "XXXXXXXXXXXXX2346",
    "card_label": "testAll"
}
```

- If the wrong card token is provided to edit

```plaintext
{
"status": 0
"msg": Card not found to edit
}
```

## Response parameters for Get User Cards API

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


### Sample response

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

## Sample Response for Delete Card API

- On successful deletion

```plaintext
{
        status: 1,
        msg: "My_card card deleted successfully",
}
```

- On failure of deletion

```plaintext
{
"status": 0,
"msg": card not found
}
```

## Sample Response for Get Payment Details (Crytogram) API

### Successful Scenario

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
            "token_value": "464XXX7450050615",
            "token_exp_mon": "01"
        },
        "trid": "400600",
        "card_mode": "",
        "token_refernce_id": "4776af84a5079512934417214171fd01",
        "card_no": "XXXXXXXXXXXX0615",
        "card_PAR": "V0010013021031409361532",
        "one_click_card_alias": "",
        "card_token": "60ac10XXX09d1965b7dae2",
        "card_name": "",
        "cryptogram": "/wAAAAoAtd1XnhwAmbHTgkUAAAA="
    }
}
```

### Failure Scenario

```plaintext
{
"status": 0,
"msg": card not found
}
```