---
title: Edit a Saved Card API
excerpt: ''
api:
  file: storecard-6.json
  operationId: edit_payment_instrument
deprecated: false
hidden: true
metadata:
  title: Edit a Saved Card API
  description: >-
    Learn how to use the PayU Edit Saved Card API to update details of stored
    cards securely. This guide provides comprehensive instructions, request
    parameters, and sample responses for seamless card management.
  keywords:
    - Edit Saved Card API
    - ' card management API'
    - ' update saved card details API'
    - ' secure card storage'
    - ' tokenization'
  robots: index
next:
  description: ''
---
The **Edit a Card** API is used to edit the details of an existing stored card on the vault. In this case, along with all the parameters required to save to the card, the **cardToken** has to be posted. After successfully editing the card, it returns the **cardToken** of the card.

HTTP Method: **POST**

<GENERALAPIsEnvironment />

<details>
  <summary>Sample request</summary>

```curl
curl --request POST \
     --url 'https://test.payu.in/merchant/postservice.php?form=2' \
     --header 'Content-Type: application/x-www-form-urlencoded' \
     --header 'accept: text/html; charset=UTF-8' \
     --data key=JPM7Fg \
     --data command=edit_payment_instrument \
     --data 'var1=key;JPM7Fg ' \
     --data var2=12345 \
     --data var3=ashishAMEX \
     --data var4=CC \
     --data var5=AMEX \
     --data 'var6=Ashish Kumar' \
     --data var7=5506900480000008 \
     --data var8=9 \
     --data var9=2025 \
     --data hash=a3e9a52f62dbb53cd0ff87a613502bbf9b82091fe8c8f785254c2039e1803ddcd8b1646e365b235948ddae5e4d3a7e80a20ca9fa8f0fef6e7a75b73d5020f253
```

</details>

<details>
  <summary>Sample response</summary>

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
"status": 0,
"msg": Card not found to edit
}
```

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
"status": 0,
"msg": Card not found.
}
```

</details>

<details>
  <summary>Response parameters</summary>

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
        745d7XXXd9b7e88824fXXXe7ed7XXX1fe624b74
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
        1234 5XXX XXXX 3456
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
        3456 7XXX XXXX EFGH
      </td>
    </tr>
  </tbody>
</Table>

</details>

## Request Parameters

<details>
  <summary>Reference Info for Request Parameters</summary>

<KeyHashForGeneralParametersDescription />

</details>