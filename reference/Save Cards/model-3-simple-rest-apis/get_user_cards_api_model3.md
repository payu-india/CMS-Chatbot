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

<Accordion title="Sample request" icon="fa-code">
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
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
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
</Accordion>

<Accordion title="Response parameters" icon="fa-list">
<Table>
  <thead>
    <tr>
      <th>**Field**</th>
      <th>**Description**</th>
      <th>**Example**</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>status</td>
      <td>The status of the response. Can be:<br/>• **1**: Success<br/>• **0**: Failure</td>
      <td>1</td>
    </tr>
    <tr>
      <td>msg</td>
      <td>The description of the response indicating whether cards were fetched successfully or not.</td>
      <td>Cards fetched Succesfully</td>
    </tr>
    <tr>
      <td>user_cards</td>
      <td>A JSON object containing all saved cards for the user. Each card is identified by its unique card token as the key.</td>
      <td>Refer to Card Object Parameters below</td>
    </tr>
  </tbody>
</Table>
</Accordion>

<Accordion title="Card Object Parameters" icon="fa-list">
<Table>
  <thead>
    <tr>
      <th>**Field**</th>
      <th>**Description**</th>
      <th>**Example**</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>one_click_status</td>
      <td>Status for one-click payment feature.</td>
      <td>""</td>
    </tr>
    <tr>
      <td>one_click_flow</td>
      <td>Flow type for one-click payment processing.</td>
      <td>""</td>
    </tr>
    <tr>
      <td>card_type</td>
      <td>The type of the card. Can be:<br/>• **CC**: Credit Card<br/>• **DC**: Debit Card</td>
      <td>CC</td>
    </tr>
    <tr>
      <td>expiry_year</td>
      <td>The expiry year of the card.</td>
      <td>2030</td>
    </tr>
    <tr>
      <td>expiry_month</td>
      <td>The expiry month of the card.</td>
      <td>11</td>
    </tr>
    <tr>
      <td>is_expired</td>
      <td>Indicates whether the card has expired:<br/>• **0**: Card is active<br/>• **1**: Card has expired</td>
      <td>0</td>
    </tr>
    <tr>
      <td>card_mode</td>
      <td>The payment mode of the card (CC for Credit Card, DC for Debit Card).</td>
      <td>CC</td>
    </tr>
    <tr>
      <td>card_no</td>
      <td>The masked card number showing only the last four digits for security.</td>
      <td>XXXXXXXXXXXX6937</td>
    </tr>
    <tr>
      <td>one_click_card_alias</td>
      <td>Alias name for the card used in one-click payments.</td>
      <td>""</td>
    </tr>
    <tr>
      <td>card_token</td>
      <td>The unique PayU token assigned to this saved card.</td>
      <td>a52aa1c09e11ac56926005</td>
    </tr>
    <tr>
      <td>card_name</td>
      <td>The name/label assigned to the saved card by the user.</td>
      <td>raghu_visa</td>
    </tr>
    <tr>
      <td>name_on_card</td>
      <td>The cardholder's name as it appears on the card.</td>
      <td>DUMMY</td>
    </tr>
    <tr>
      <td>card_brand</td>
      <td>The brand/network of the card (VISA, MASTERCARD, AMEX, etc.).</td>
      <td>VISA</td>
    </tr>
    <tr>
      <td>card_bin</td>
      <td>The Bank Identification Number (first 6-9 digits) of the card.</td>
      <td>439040621</td>
    </tr>
    <tr>
      <td>isDomestic</td>
      <td>Indicates whether the card is domestic or international:<br/>• **Y**: Domestic card<br/>• **N**: International card</td>
      <td>Y</td>
    </tr>
    <tr>
      <td>card_cvv</td>
      <td>Indicates whether CVV is required for transactions:<br/>• **0**: CVV not required<br/>• **1**: CVV required</td>
      <td>0</td>
    </tr>
    <tr>
      <td>PAR</td>
      <td>Payment Account Reference - a unique identifier for the card across all tokens, used for offers and risk checks.</td>
      <td>V0010013022320257414953977387</td>
    </tr>
    <tr>
      <td>network_token</td>
      <td>A JSON object containing network token details for secure payments.</td>
      <td>Refer to Network Token Parameters below</td>
    </tr>
  </tbody>
</Table>
</Accordion>

<Accordion title="Network Token Parameters" icon="fa-list">
<Table>
  <thead>
    <tr>
      <th>**Field**</th>
      <th>**Description**</th>
      <th>**Example**</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>token_bin</td>
      <td>The Bank Identification Number for the network token.</td>
      <td>439040</td>
    </tr>
    <tr>
      <td>is_expired</td>
      <td>Indicates whether the network token has expired:<br/>• **0**: Token is active<br/>• **1**: Token has expired</td>
      <td>0</td>
    </tr>
    <tr>
      <td>token_exp_yr</td>
      <td>The expiry year of the network token.</td>
      <td>2030</td>
    </tr>
    <tr>
      <td>token_exp_mon</td>
      <td>The expiry month of the network token.</td>
      <td>11</td>
    </tr>
    <tr>
      <td>token_value</td>
      <td>The actual network token value used for secure transactions.</td>
      <td>4390406210204342</td>
    </tr>
  </tbody>
</Table>
</Accordion>

## Request parameters

<Accordion title="Reference info for request parameters" icon="fa-flask">
<KeyHashForGeneralParametersDescription />
</Accordion>