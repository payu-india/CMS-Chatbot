---
title: Get User Cards API - Model 3
excerpt: ''
api:
  file: storecard-10.json
  operationId: GetUserCards
deprecated: false
hidden: false
metadata:
  title: Get User Cards API - Model 3
  description: >-
    Discover how to use the PayU Get User Cards API (Model 3) to retrieve stored
    card details securely. This guide includes detailed instructions, request
    parameters, and sample responses for efficient card management.
  keywords:
    - Get User Cards API
    - ' saved card retrieval'
    - ' get secured cards'
    - ' card tokenization'
    - ' get user saved cards'
  robots: index
next:
  description: ''
---
The **Get User Cards** API is used to fetch all the cards corresponding to the user. In this API, the card number and other sensitive information are not returned.

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
     --data command=get_payment_instrument \
     --data var1=JPM7Fg:abc \
     --data hash=750351ed44241b9739d2e374de45dd0be3c2f6d68305ceb81084960387b71722b0f8d224900f57202488a557ecfa6f2e22895f27585a413388684a142bb8e41e
```

</details>

<details>
  <summary>Sample response</summary>

```
{
  "status": 1,
  "msg": "Cards fetched Succesfully",
  "user_cards": {
    "a52aa1c09e11ac56926005": {
      "one_click_status": "",
      "one_click_flow": "",
      "card_type": "CC",
      "expiry_year": "2030",
      "network_token": {
        "token_bin": "439040",
        "is_expired": "0",
        "token_exp_yr": "2030",
        "token_exp_mon": "11",
        "token_value": "4390406210204342"
      },
      "expiry_month": "11",
      "is_expired": "0",
      "card_mode": "CC",
      "card_no": "XXXXXXXXXXXX6937",
      "one_click_card_alias": "",
      "card_token": "a52aa1c09e11ac56926005",
      "card_name": "raghu_visa",
      "name_on_card": "DUMMY",
      "card_brand": "VISA",
      "card_bin": "439040621",
      "isDomestic": "Y",
      "card_cvv": 0,
      "PAR": "V0010013022320257414953977387"
    }
  }
}
```

</details>

## Request parameters

<details>
  <summary>Reference info for request parameters</summary>

<KeyHashForGeneralParametersDescription />

</details>