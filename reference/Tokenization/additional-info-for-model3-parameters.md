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

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
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
        status
      </td>

      <td>
        The status of the response can be any of the following:  

        * 1: Success   
        * 0: Failure
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        msg
      </td>

      <td>
        The description of the response whether the card details were stored successfully or not stored.
      </td>

      <td>
        Card Stored Successfully.
      </td>
    </tr>

    <tr>
      <td>
        cardToken
      </td>

      <td>
        The cardToken is sent by PayU for the successful response.
      </td>

      <td>
        `74\*\*\*2e2fd9b7e\*\*\*24fef4e7ed7dac1fe624b7`
      </td>
    </tr>

    <tr>
      <td>
        network\_token
      </td>

      <td>
        The network token is returned in this parameter.
      </td>

      <td>
        `1234 5*** 9*** 3456`
      </td>
    </tr>

    <tr>
      <td>
        issuer\_token
      </td>

      <td>
        The parameter contains the issuer token that is returned by issuer.
      </td>

      <td>
        `3456 7*** A*** EFGH`
      </td>
    </tr>
  </tbody>
</Table>

## Sample Response for Save Card API

### Success scenarios

* VISA

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

* Mastercard

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

* American Express

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

* Rupay

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

* Diners

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

* If card Number is invalid

```plaintext
{
"status": 0
"msg": CardNumber is invalid
}
```

## Response parameters for Edit Card API

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
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
        status
      </td>

      <td>
        The status of the response can be any of the following:  

        * 1: Success  
        * 0: Failure
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        msg
      </td>

      <td>
        The description of the response whether the card details were stored successfully or not stored.
      </td>

      <td>
        My\_card Edited Successfully
      </td>
    </tr>

    <tr>
      <td>
        cardToken
      </td>

      <td>
        The card token is sent by PayU for the successful response.
      </td>

      <td>
        `745d7XXXd9b7e88824fXXXe7ed7XXX1fe624b74`
      </td>
    </tr>

    <tr>
      <td>
        networkToken
      </td>

      <td>
        The network token is sent by PayU for the successful response.
      </td>

      <td>
        `1234 5XXX XXXX 3456`
      </td>
    </tr>

    <tr>
      <td>
        issuerToken
      </td>

      <td>
        The issuer token is sent by PayU for the successful response.
      </td>

      <td>
        `3456 7XXX XXXX EFGH`
      </td>
    </tr>
  </tbody>
</Table>

### Sample response

* On successful update of card details

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

* If the wrong card token is provided to edit

```plaintext
{
"status": 0
"msg": Card not found to edit
}
```

## Response parameters for Get User Cards API

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
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
        status
      </td>

      <td>
        The status of the response can be any of the following:\
        1: Success  

        2: Failure
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        msg
      </td>

      <td>
        The description of the response whether the card details were stored successfully or not stored.
      </td>

      <td>
        Cards fetched Succesfully
      </td>
    </tr>

    <tr>
      <td>
        user\_cards
      </td>

      <td>
        (JSON format) | The details are sent by PayU in JSON format for the successful response. For more information, refer to the next table.
      </td>

      <td>
        Refer the [sample response](ref:get_user_cards_api_model3).
      </td>
    </tr>
  </tbody>
</Table>

The details on the JSON format for a successful response is described in the following table:

<Table>
  <thead>
    <tr>
      <th>
        **JSON Field**
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
        card\_name
      </td>

      <td>
        * \*Note\*\*: This parameter has been deprecated.
      </td>

      <td>
        NA
      </td>
    </tr>

    <tr>
      <td>
        card\_type
      </td>

      <td>
        This field returns the card type code. For the list of card type codes, refer to [Card Type Codes and Supported Banks for Cards](doc:card-type-codes-and-supported-banks-for-cards).
      </td>

      <td>
        CC
      </td>
    </tr>

    <tr>
      <td>
        card\_token
      </td>

      <td>
        This field returns the PayU Token for the card.
      </td>

      <td>
        745d72e2fXXX7e88824fef4e7ed7dXXXfe624b7
      </td>
    </tr>

    <tr>
      <td>
        network\_token
      </td>

      <td>
        This field returns the details of the network token in a JSON format.
      </td>

      <td>
        "token\_value": "51XXX56789012346",  

        "is\_expired": 0,  

        "token\_exp\_mon": "11",  

        "token\_exp\_yr": "2021",  

        "token\_bin": "512345"  

        }
      </td>
    </tr>

    <tr>
      <td>
        issuer\_token
      </td>

      <td>
        This field returns the details of the issuer token in a JSON format.
      </td>

      <td>
        \{  

        "token\_value": "51XXX567890XXX46",  

        "is\_expired": 0,  

        "token\_exp\_mon": "11",  

        "token\_exp\_yr": "2021",  

        "token\_bin": "512345"  

        }
      </td>
    </tr>

    <tr>
      <td>
        is\_expired
      </td>

      <td>
        This field returns any of the following values to signify whether the card is active or not:\
        1: Card has expired  

        0: Card is active
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        card\_mode
      </td>

      <td>
        This field returns the card mode.
      </td>

      <td>
        CC
      </td>
    </tr>

    <tr>
      <td>
        card\_no
      </td>

      <td>
        This field returns a masked card number with only the last four digits.
      </td>

      <td>
        xxxxxxxxxxxx2356
      </td>
    </tr>

    <tr>
      <td>
        card\_brand
      </td>

      <td>
        This field returns the card brand.
      </td>

      <td>
        VISA
      </td>
    </tr>

    <tr>
      <td>
        card\_bin
      </td>

      <td>
        * \*Note\*\*: This parameter has been deprecated.
      </td>

      <td>
        NA
      </td>
    </tr>

    <tr>
      <td>
        token\_bin
      </td>

      <td>
        This field returns the token bin information of respective token type (network or issuer).
      </td>

      <td>
        123456
      </td>
    </tr>

    <tr>
      <td>
        card\_PAR
      </td>

      <td>
        This field returns the PAR (Payment Account Reference). This is a unique identity for the card across all the tokens. Typically, this will be used for offers and risk checks.
      </td>

      <td>
        abcdefgh123456789123456789fgh
      </td>
    </tr>

    <tr>
      <td>
        card\_metadata
      </td>

      <td>
        This field returns the JSON object with all the metadata and card art.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        token\_exp\_yr
      </td>

      <td>
        This field returns the expiry year of the network token.
      </td>

      <td>
        2022
      </td>
    </tr>

    <tr>
      <td>
        token\_exp\_mon
      </td>

      <td>
        This field returns the expiry month of the network token.
      </td>

      <td>
        10
      </td>
    </tr>

    <tr>
      <td>
        token\_value
      </td>

      <td>
        The field returns the value of the network or issuer token.
      </td>

      <td>
        51XXX5678XXX2346
      </td>
    </tr>
  </tbody>
</Table>

### Sample response

* Cards are found in the vault for PCI Compliant Merchants

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

* Response for Non-PCI Compliant Merchants

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

* No cards are found for the user

```plaintext
{
"status": 0
"msg": Card not found.
}
```

## Sample Response for Delete Card API

* On successful deletion

```plaintext
{
        status: 1,
        msg: "My_card card deleted successfully",
}
```

* On failure of deletion

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
