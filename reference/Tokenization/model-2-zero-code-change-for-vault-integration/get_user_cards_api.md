---
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

<Callout icon="📘" theme="info">
  **Note**: While PayU token is sent in payment response, the network/issuer token creation may fail. In this case, the subsequent transaction with the said PayU token may fail. Merchant can do a **get_user_cards API** to fetch only active/tokenized cards or listen to notification API (to be published) to maintain state at your end.
</Callout>

<Callout icon="👍" theme="okay">
  Experience the end-to-end **Merchant Hosted Checkout** flow and instantly generate the complete code for seamless, zero-coding integration into your website. Select **Repeat Customer > Get User Cards** from left navigation pane after opening the following page

  <HTMLBlock>{`
                          <style>
                          .tooltip-btn {
                              position: relative;
                              background-color: #4CAF50;
                              color: white;
                              padding: 10px 20px;
                              border: none;
                              border-radius: 5px;
                              cursor: pointer;
                              font-weight: bold; /* Added this line */
                          }
                          .tooltip-btn:hover::after {
                              content: attr(data-tooltip);
                              position: absolute;
                              bottom: 125%;
                              left: 50%;
                              transform: translateX(-50%);
                              background-color: #333;
                              color: white;
                              padding: 5px 10px;
                              border-radius: 4px;
                              white-space: nowrap;
                              font-size: 12px;
                              z-index: 1;
                          }
                          </style>

                          <button onclick="window.open('https://payu.in/integrationlab/seamless/cards', '_blank')" 
                                  class="tooltip-btn" 
                                  data-tooltip="Click here to see the Merchant Hosted Checkout end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">
                              Experience the flow and get the code
                          </button>
  `}</HTMLBlock>
</Callout>

The Get User Cards API (**get_user_cards**) is used to fetch all the cards for a customer which were saved earlier. In this API, the card number and other sensitive information are not returned.

HTTP Method: **POST**

<GENERALAPIsEnvironment />

<br />

<Accordion title="Sample request" icon="fa-code">
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
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
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
</Accordion>

<Accordion title="Response parameters" icon="fa-list">
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

        <td />
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
</Accordion>

## Request parameters

<Accordion title="Reference info for request parameters" icon="fa-flask">
  `<KeyHashForGeneralParametersDescription />`
</Accordion>
