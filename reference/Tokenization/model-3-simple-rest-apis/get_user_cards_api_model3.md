---
excerpt: ''
api:
  file: storecard-10.json
  operationId: GetUserCards
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
      "msg": "Cards fetched Successfully",
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
  | **Field**   | **Description**                                                                                                                                                                                                          | **Example**                                                                        |
  | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
  | status      | The status of the response. Can be:<br />• **1**: Success<br />• **0**: Failure                                                                                                                                          | 1                                                                                  |
  | msg         | The description of the response indicating whether cards were fetched successfully or not.                                                                                                                               | Cards fetched Succesfully                                                          |
  | user\_cards | A JSON object containing all saved cards for the user. Each card is identified by its unique card token as the key. For more details, refer to [Card JSON object field description](#card-json-object-field-description) | Refer to [Card JSON object field description](#card-json-object-field-description) |

  ### Card JSON object field description

  | **Field**               | **Description**                                                                                                                                                                                | **Example**                                                                                          |
  | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
  | one\_click\_status      | Status for one-click payment feature.                                                                                                                                                          | ""                                                                                                   |
  | one\_click\_flow        | Flow type for one-click payment processing.                                                                                                                                                    | ""                                                                                                   |
  | card\_type              | The type of the card. Can be:<br />• **CC**: Credit Card<br />• **DC**: Debit Card                                                                                                             | CC                                                                                                   |
  | expiry\_year            | The expiry year of the card.                                                                                                                                                                   | 2030                                                                                                 |
  | expiry\_month           | The expiry month of the card.                                                                                                                                                                  | 11                                                                                                   |
  | is\_expired             | Indicates whether the card has expired:<br />• **0**: Card is active<br />• **1**: Card has expired                                                                                            | 0                                                                                                    |
  | card\_mode              | The payment mode of the card (CC for Credit Card, DC for Debit Card).                                                                                                                          | CC                                                                                                   |
  | card\_no                | The masked card number showing only the last four digits for security.                                                                                                                         | XXXXXXXXXXXX6937                                                                                     |
  | one\_click\_card\_alias | Alias name for the card used in one-click payments.                                                                                                                                            | ""                                                                                                   |
  | card\_token             | The unique PayU token assigned to this saved card.                                                                                                                                             | a52aa1c09e11ac56926005                                                                               |
  | card\_name              | The name/label assigned to the saved card by the user.                                                                                                                                         | raghu\_visa                                                                                          |
  | name\_on\_card          | The cardholder's name as it appears on the card.                                                                                                                                               | DUMMY                                                                                                |
  | card\_brand             | The brand/network of the card (VISA, MASTERCARD, AMEX, etc.).                                                                                                                                  | VISA                                                                                                 |
  | card\_bin               | The Bank Identification Number (first 6-9 digits) of the card.                                                                                                                                 | 439040621                                                                                            |
  | isDomestic              | Indicates whether the card is domestic or international:<br />• **Y**: Domestic card<br />• **N**: International card                                                                          | Y                                                                                                    |
  | card\_cvv               | Indicates whether CVV is required for transactions:<br />• **0**: CVV not required<br />• **1**: CVV required                                                                                  | 0                                                                                                    |
  | PAR                     | Payment Account Reference - a unique identifier for the card across all tokens, used for offers and risk checks.                                                                               | V0010013022320257414953977387                                                                        |
  | network\_token          | A JSON object containing network token details for secure payments. For more information, refer to [Network token JSON object field description](#network-token-json-object-field-description) | Refer to [Network token JSON object field description](#network-token-json-object-field-description) |

  ### Network token JSON object fields description

  | **Field**       | **Description**                                                                                                | **Example**      |
  | --------------- | -------------------------------------------------------------------------------------------------------------- | ---------------- |
  | token\_bin      | The Bank Identification Number for the network token.                                                          | 439040           |
  | is\_expired     | Indicates whether the network token has expired:<br />• **0**: Token is active<br />• **1**: Token has expired | 0                |
  | token\_exp\_yr  | The expiry year of the network token.                                                                          | 2030             |
  | token\_exp\_mon | The expiry month of the network token.                                                                         | 11               |
  | token\_value    | The actual network token value used for secure transactions.                                                   | 4390406210204342 |
</Accordion>

## Request parameters

<Accordion title="Reference info for request parameters" icon="fa-flask">
  <KeyHashForGeneralParametersDescription />
</Accordion>

<br />
