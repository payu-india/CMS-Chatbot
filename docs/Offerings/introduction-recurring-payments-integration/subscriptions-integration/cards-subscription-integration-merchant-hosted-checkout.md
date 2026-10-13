---
title: 'Cards Subscriptions Integration - Merchant Hosted Checkout '
deprecated: false
hidden: false
metadata:
  title: Cross-Border Payments  - Card Subscriptions with Merchant-Hosted Checkout
  description: >-
    Cross-Border Payments  - Card Subscriptions with Merchant-Hosted Checkout.
    SI on cards integration.
  robots: index
---
PayU's Card Subscription Integration using the Merchant-Hosted Checkout method enables businesses to set up automated recurring payments through credit and debit cards with enhanced control over the payment flow. This section covers the complete process from capturing initial customer consent and mandate registration to executing seamless recurring transactions without requiring additional 2-factor authentication.

#### I. Payment Consent Flow

<Cards>
  <Card title="1. Consent Transaction" href="#step-1-consent-transaction">
    Initiate the recurring payment mandate by sending a POST request with mandatory parameters including key, txnid, amount, productinfo, customer details, pg='CC', bankcode, si=1, and si_details
  </Card>

  <Card title="2. Verify the Payment" href="#step-2-verify-the-payment">
    Use PayU's Verify Payment API or webhook setup to confirm successful consent transaction and mandate registration, handling any rejections or failures
  </Card>
</Cards>

#### II. Recurring Payments Flow

<Cards>
  <Card title="3. Pre-Debit Notification" href="#step-3-pre-debit-notification">
    Send advance notifications to customers 24-48 hours before recurring charges using authpayuid, invoiceDisplayNumber, and debit amount parameters
  </Card>

  <Card title="4. Recurring Payment Transaction" href="#step-4-recurring-payment-transaction">
    Execute automated recurring payments via server-to-server API without additional 2FA, using the registered mandate and billing schedule
  </Card>
</Cards>

## Enablement

To collect dynamic convenience fees on SI card transactions, the following merchant-level flags must be enabled on your MID. Contact your PayU Key Account Manager (KAM) to activate them before attempting the integration below.

| Flag                       | Description                                                          |
| -------------------------- | -------------------------------------------------------------------- |
| `enableCardsSiDynamicConv` | Enables dynamic convenience fee support for SI card transactions.    |
| `enableSIPredebitConvFee`  | Enables passing convenience fee at the pre-debit notification stage. |
| `DynamicConvFeeMerchant`   | Enables the merchant-level dynamic convenience fee capability.       |

## I. Payment Consent Flow

### Step 1: Consent Transaction

HTTP Method: **POST**

**Environment**

|                        |                                                                     |
| :--------------------- | :------------------------------------------------------------------ |
| Test Environment       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
| Production Environment | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |

<Accordion title="Request parameters" icon="fa-table">
  | Parameter                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Value                                                                                          |
  | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
  | `key`<br />`mandatory`                          | `String` The merchant key is a unique identifier for a merchant account in PayU's database. For more information, [Check your API Key and Salt](http://docs.payu.in/docs/check-api-key-and-salt).                                                                                                                                                                                                                                                                                                                                                                                                                 | Your Test Key                                                                                  |
  | `api_version`<br />`optional`                   | `String` The API version for this API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 7                                                                                              |
  | `txnid`<br />`mandatory`                        | `String` The transaction ID is a reference number for a specific order that is generated by the merchant. It is used to track the order and must be unique. PayU's system will not accept duplicate transaction IDs.                                                                                                                                                                                                                                                                                                                                                                                              | s7hhDQVWvbhBdN                                                                                 |
  | `amount`<br />`mandatory`                       | `String` This field should contain the payment amount for the transaction.<br />**Note**: The transaction limit are as per the card holders limit or Rs.10,00,000 (if the card limit is more than Rs.10,00,000).                                                                                                                                                                                                                                                                                                                                                                                                  | 10.00                                                                                          |
  | `productinfo`<br />`mandatory`                  | `String` It should be a string containing a brief description of the product. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | iPhone                                                                                         |
  | `firstname`<br />`mandatory`                    | `String` The first name of the customer. `Character Limit-60`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Ashish                                                                                         |
  | `email`<br />`mandatory`                        | `String` The email of the customer. `Character Limit-50`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | [test@gmail.com](mailto:test@gmail.com)                                                        |
  | `phone`<br />`mandatory`                        | `String` The phone number of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 9876543210                                                                                     |
  | `lastname`<br />`mandatory`                     | `String` The last name of the customer. `Character Limit-60`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Verma                                                                                          |
  | `address1`<br />`optional`                      | `String` The first line of the billing address. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai                                        |
  | `address2`<br />`optional`                      | `String` The second line of the billing address. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 34 Saikripa-Estate, Tilak Nagar                                                                |
  | `city`<br />`optional`                          | `String` The city where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Mumbai                                                                                         |
  | `state`<br />`optional`                         | `String` The state where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Maharashtra                                                                                    |
  | `country`<br />`optional`                       | `String` The country where your customer resides. `Character Limit-50`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | India                                                                                          |
  | `zipcode`<br />`optional`                       | `String` Billing address zip code is mandatory for the cardless EMI option. `Character Limit-20`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 400004                                                                                         |
  | `si`<br />`mandatory`                           | This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.<br />**Notes**: You can modify or cancel existing recurring payment registration as described in the following sections:<br />\- [Manage Recurring Payment for Cards](http://docs.payu.in/reference/manage-recurring-payment-for-cards)<br />\- [Manage UPI Recurring Transaction](http://docs.payu.in/reference/api-commands-to-manage-upi-recurring-transaction)                                    | 1                                                                                              |
  | `si_details`<br />`mandatory`                   | This parameter represents mandatory details which need to be passed during registration transaction from merchant system to PayU.<br />**Note**: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers (for more details refer – [RBI Notification](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0)).<br />This is a JSON object and it includes a set of fields. For more information, refer to [SI Parameter JSON Details](http://docs.payu.in/reference/si-parameter-json-details). |                                                                                                |
  | `hash`<br />`mandatory`                         | `String` It is used to avoid the possibility of transaction tampering. For more information on hash generation process, refer to [Hashing Request and Response](http://docs.payu.in/docs/generate-hash-merchant-hosted).<br />In the case of registration transaction, the formula used to calculate this hash is:<br />\`HASH = SHA512(key                                                                                                                                                                                                                                                                       | txnid                                                                                          |
  | `pg`<br />`mandatory`                           | `String` The pg parameter must include 'CC' for cards.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | CC                                                                                             |
  | `bankcode`<br />`mandatory`                     | `String` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. For more information, refer [Card Type Codes and Supported Banks for Cards](http://docs.payu.in/docs/card-type-codes-and-supported-banks-for-cards).                                                                                                                                                                                                                                                                             | AMEX                                                                                           |
  | `udf1 - udf5`<br />`optional`                   | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5. `Character Limit`-255                                                                                                                                                                                                                                                                                                                                                                                         | Payment Preference, Shipping Method, Shipping Address1, Shipping City, Shipping Zip Code, etc. |
  | `ccnum`<br />`conditional`                      | `Integer` This parameter must contain the card number.<br />This parameter is required if you are trying to create a mandate using the card details.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                |
  | `ccvv`<br />`mandatory`                         | `varchar` This parameter must contain the CVV number of the card – as entered by the customer for the transaction.<br />**Note**: If your customer is returning to your website to shop, you must fetch all the customer's stored cards from PayU, collect the CVV for the card the customer will be using to make payment and then post the CVV number to PayU.                                                                                                                                                                                                                                                  | 123                                                                                            |
  | `ccexpmon`<br />`mandatory`                     | `integer` This parameter must contain the network token expiry month. For stored card using network or issuer, enter the expiry month of the token.                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 10                                                                                             |
  | `ccexpyr`<br />`mandatory`                      | `integer` This parameter must contain the network token expiry year. For stored card using network or issuer, enter the expiry year of the token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 2022                                                                                           |
  | `store_card_token`<br />`conditional`           | `varchar` This must include the Network token generated at your end.<br />This parameter is required if you are using the stored card token to register the mandate.                                                                                                                                                                                                                                                                                                                                                                                                                                              | 1234 4567 2456 3566                                                                            |
  | `storecard_token_type`<br />`conditional`       | `integer` This parameter is used to specify the store card token type. It must include any of the following values:<br />\- **0**: If PayU token is used.<br />\- **1**: If Network token is used.<br />\- **2**: If Issuer token is used.<br />This parameter is required if you are using the stored card token to register the mandate.                                                                                                                                                                                                                                                                        | 1                                                                                              |
  | `additional_info`<br />`conditional`            | `varchar` This parameter will contain the additional information in the following JSON format: `{"last4Digits": "1234", "tavv": "ABCDEFGH","trid":"1234567890", "tokenRefNo":"abcde123456"}`<br />This parameter is required if you are using the stored card token to register the mandate, where network or issuer token is used.                                                                                                                                                                                                                                                                               | `{"last4Digits": "1234", "tavv": "ABCDEFGH","trid":"1234567890", "tokenRefNo":"abcde123456"}`  |
  | `free_trial`<br />`conditional`                 | This is mandatory only if the merchant wants to support free trial use case with card and net banking together that too on PayU Hosted Checkout integration.<br />In this case, PayU adjusts the transaction amount as INR 2.00 for cards. INR 0.00 for Net Banking and UPI registration irrespective of what amount is passed against the amount field in the request.<br />This parameter has no significance in the case of seamless flow.                                                                                                                                                                     |                                                                                                |
  | `additional_charges`<br />`optional`            | Flat convenience fee per SI card type for dynamic convenience fee on Standing Instruction card transactions. Expressed as a comma-separated string of `IBIBOCODE:value` pairs.<br />**Example**: `CCSI:10,DCSI:20,AMEXSI:30`<br />Allowed ibibocodes for registration:<br />\- **CCSI** — Credit Card Standing Instruction<br />\- **DCSI** — Debit Card Standing Instruction<br />\- **VISASI** — Visa Standing Instruction<br />\- **AMEXSI** — American Express Standing Instruction<br />Requires `enableCardsSiDynamicConv` and `DynamicConvFeeMerchant` flags to be active on the MID.                      | `CCSI:10,DCSI:20,AMEXSI:30`                                                                    |
  | `percentage_additional_charges`<br />`optional` | Percentage-based convenience fee per SI card type. Expressed as a comma-separated string of `IBIBOCODE:value` pairs using the same ibibocodes as `additional_charges`.<br />**Example**: `CCSI:100,DCSI:90,AMEXSI:80`                                                                                                                                                                                                                                                                                                                                                                                             | `CCSI:100,DCSI:90,AMEXSI:80`                                                                   |

  <Callout icon="📘" theme="info">
    ### Notes for **additional_info** parameter:

    The JSON format contains the following fields:<br />

    - **trid** (Token Requestor ID) is the identifier given by the networks for creating the tokens. You should be able to get the same from your token provider.
    - **tokenRefNo** (Token Reference Number) is generated along with the network token. You should be able to get the same from your token provider.
    - **TAVV** is a token authentication verification value given by schemes or interchange. Also, known as cryptogram.

    Additional notes:

    - The last 4 digits of cards is mandatory for all transactions.   
    - Some payment gateways require the Token Requester ID (trid) and Token Reference Number (tokenRefNo) to be passed for processing the transaction. Not passing these values will restrict the number of payment gateways available for processing the transaction.
    - Token Requester ID (trid) and Token Reference Number (tokenRefNo) are mandatory for Diners token transactions.
  </Callout>

  <Callout icon="📘" theme="info">
    ### Notes for bankcode

    Debit Card or Credit Card: There are different options like Visa Debit Card, Mastercard, Maestro, etc. For each option, a unique bank code exists and it would be returned in this bankcode parameter. For more information, refer to Card Type Codes. For example, VISA for VISA Debit Card.
  </Callout>

  Characters allowed for parameters

  For parameters address1, address2, city, state, country, product info, email, and phone following characters are allowed:

  - Characters: A to Z, a to z, 0 to 9
  - – (Minus)
  - \_ (Underscore)
  - @ ()
  - / (Slash)
  - (Space)
  - . (Dot)
</Accordion>

#### Sample request

The sample code block for cards Seamless integration (Merchant-Hosted Checkout) is similar to the following:

```curl
curl -X POST "https://test.payu.in/_payment-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d”key=Q*****U&txnid=56bb2e3fcb510f1c1521&amount=10000&firstname=Payu-Admin&email=test@example.com&phone=1234567890&productinfo=iPhone&api_version=7&si=1&pg=CC&bankcode=UTIBENCC&surl=https://test.payu.in/admin/test_response
/&furl=https://test.payu.in/admin/test_response
&ccnum=5123456789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=Test User&si_details={“billingAmount”: “100.00”,”billingCurrency”: “INR”,”billingCycle”: “MONTHLY”,”billingInterval”: 1,”paymentStartDate”: “2022-09-01″,”paymentEndDate”: “2022-12-01”}
&hash=e36568b2dfc460eab0eb3387fb7d90543ed861154f273b9593d6fcc152ed93a91e529c2f4be0965eeb57104e82d58889fa5efb52811ec78cbd1ad646e39c29a0”
```

#### Sample response

<Accordion title="Expected Values in Response" icon="fa-table">
  In the case of Cards, you must ensure that the payment response from PayU has the expected values as described in the following table so that they successfully registered for a recurring plan or subscription for the customer:

  | Response Parameter | Expected Value                   | Description                                                                     |
  | ------------------ | -------------------------------- | ------------------------------------------------------------------------------- |
  | status             | success                          | This indicates that the transaction is successful                               |
  | cardToken          | \<card_token> sent by PayU       | Indicates that card details are saved correctly in PayUBiz Database             |
  | payment_source     | sist                             | Indicates that card details have been marked correctly for Standing Instruction |
  | mihpayid           | \<mihpayid number> sent. by PayU | Indicates PayU’s transaction acknowledgment for a Consent transaction           |

  <Callout icon="📘" theme="info">
    **Notes**:

    - If any of the above four checks are not satisfied, that means the transaction has not been correctly authorized for Standing Instruction. The merchant must not consider this transaction eligible for the Recurring platform.
    - Registration transaction must be successful in making it eligible for the Recurring platform.
  </Callout>

  At this step, if the status of the consent transaction is returned as success along with the other three conditions explained above, you can consider that the subscription setup is completed successfully.
</Accordion>

<Accordion title="Sample response" icon="fa-code">
  The response URL returned from PayU is in the form URL format (application/x-www-form-urlencoded).

  #### Parsed response

  ```
  Array
  (
      [mihpayid] => 25600342065
      [mode] => CC
      [status] => success
      [unmappedstatus] => captured
      [key] => BmTY3G
      [txnid] => 1d1a28fe1281c04b1968
      [amount] => 1.00
      [cardCategory] => signature_premium
      [discount] => 0.00
      [net_amount_debit] => 1
      [addedon] => 2025-10-14 11:06:59
      [productinfo] => Product Info
      [firstname] => Payu-Admin
      [lastname] =>
      [address1] =>
      [address2] =>
      [city] =>
      [state] =>
      [country] =>
      [zipcode] =>
      [email] => test@example.com
      [phone] => 1234567890
      [udf1] =>
      [udf2] =>
      [udf3] =>
      [udf4] =>
      [udf5] =>
      [udf6] =>
      [udf7] =>
      [udf8] =>
      [udf9] =>
      [udf10] =>
      [hash] => f67284c77d6fe59b092ef98a735ba78bd8c484b14b364cad42520fb8724d5d72b6f3c05439a56c7fe921a262027699de14edb92b03ca2e6284e66b6a81d98bcc
      [field1] => 7604202397746612005910
      [field2] => 175975
      [field3] => 1.00
      [field4] =>
      [field5] => 00
      [field6] => 05
      [field7] => AUTHPOSITIVE
      [field8] => AUTHORIZED
      [field9] => Transaction is Successful
      [payment_source] => sist
      [meCode] => {"MID":"hdfc_89051842","TKey":"0wMbyodmbgzwIOejqyUOpAkCJdBC01zQGwHS+Pm1rGGxBki5xPR60G948KUmnPR5l7xDpxYOWIOLfE1q0z5ezIA7dG/yVAkp4nZmbddhWyNpdLusIKmiJzXH6ASAMJKZJ0dH3NyQypy9w51PfUKAz80I4y4Udq8zCKB+yiDP3JqkOfz366Y5SjKI/BWNMXCMXOXIvzVNSinDVi4bVW+WtimdJ1BS9WACx8zkYjPjTkuGB6TMYeJGYt0JJ6oSQce4xk4yW3al+fFABVC26S+2wNuHYMMFvhd09AK4nUvFMh9SHjhWWw6T81miW2kqxi0o+rdvCCYEO3Aa3R5kH8kmIw=="}
      [PG_TYPE] => CC-PG
      [bank_ref_num] => 7604202397746612005910
      [bankcode] => CC
      [error] => E000
      [error_Message] => No Error
      [cardToken] => 6a3b14bce0ae8634d70be
      [card_token] => 6a3b14bce0ae8634d70be
      [cardnum] => XXXXXXXXXXXX4879
  )
  ```
</Accordion>

### Step 2: Verify the payment

You can use the **Verify Payment** API and expose a webhook by requesting the PayU Integration team to configure the same against the **ws_online_response** parameter. If this webhook is configured, you will receive the above response object over HTTP form post method.

If the mandate is not confirmed by the customer or the mandate is confirmed by the customer, but the mandate registration is rejected from the banks, the status is communicated as a “failure” over webhook. For more information, refer to [Set up WebHook to Receive Cancellation or Modification Update from the Issuer Bank](ref:set-up-webhook-to-receive-cancellation-or-modification-update-from-the-issuer-bank).
The payment verification step ensures the transaction has been processed successfully before proceeding to subsequent recurring payments.

<Verify_Payment_Tabs />

## II. Recurring Payments Flow

### Step 1: Pre-Debit Notification

The **Pre-Debit Notification** API allows the merchants to send a pre-debit notification to the customer regarding an upcoming payment which will be deducted from the customer's account as part of the registration.

<Callout icon="❗️" theme="error">
  ### **Reminder**

  - Check the mandate status before calling the **Pre-Debit Notification** API.
  - Unless the Pre-Debit notification API is implemented, the **Recurring Payment Transaction** API will not work, and you will not be able to charge the customer for the given billing cycle.
</Callout>

**Environment**

|                        |                                                                  |
| :--------------------- | :--------------------------------------------------------------- |
| Production Environment | [https://info.payu.in/merchant/](https://info.payu.in/merchant/) |
| Test Environment       | [https://test.payu.in/merchant/](https://test.payu.in/merchant/) |

<Accordion title="Sample Request" icon="fa-upload">
  ```curl
  curl --location --request POST 'https://test.info.payu.in/merchant/postservice.php?form=2' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --form 'key="BmTY3G"' \
    --form 'command="pre_debit_SI"' \
    --form 'hash="{{hash_value}}"' \
    --form 'var1="{
      \"authpayuid\": \"25511473084\",
      \"requestId\": \"9a900b2f-85e2-4034-aaa9-9c71e1d2af14\",
      \"amount\": \"100.00\",
      \"debitDate\": \"2026-03-20\",
      \"invoiceDisplayNumber\": \"19976ec0-c01f-4f6f-886b-8ea614f5fd83\",
      \"additional_charges\": \"CCSI:10,DCSI:20,AMEXSI:30,HDFCDCSI:40,VISASI:50\",
      \"percentage_additional_charges\": \"CCSI:100,DCSI:90,AMEXSI:80,HDFCDCSI:70,VISASI:60\"
    }"'
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-download">
  **Successful scenario**

  ```json
  {
    "invoiceid": "76323425",
    "approvedStatus": "na",
    "invoiceStatus": "unpaid",
    "amount": "1.00",
    "status": 1,
    "message": "Invoice Created Successfully",
    "action": "MANDATE_PRE_DEBIT"
  }
  ```

  **Failure Scenarios**

  - Mandate is active in PayU DB and Pre-Debit gets declined from Bank/NPCI

  ```json
  {
    "status": "QC",
    "action": "MANDATE_PRE_DEBIT",
    "message": "MANDATE HAS BEEN REVOKED"
  }
  ```

  Where, the **message** parameter in the response will display error code according to the scenario

  - Mandate is already Paused/ Revoked in PayU DB

  ```json
  {
    "status": 0,
    "action": "MANDATE_PRE_DEBIT",
    "message": "Mandate is not active"
  }
  ```

  Where, the **message** parameter in the response will display according to the scenario.
</Accordion>

<Accordion title="Response Parameters" icon="fa-list">
  | Parameter Name                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                      |
  | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | status                               | Status defines acknowledgment from PayU. Possible values are :<br />• **1**- This value indicates that pre-debit notification is triggered successfully for customer or deleted successfully in case of action delete.<br /><br />• **0** – This value indicates pre-debit notification failed to get triggered and merchant should retry after some time to trigger the same or failed to get deleted in case of action delete. |
  | action                               | Always returned as "MANDATE_PRE_DEBIT" to highlight the type of action.                                                                                                                                                                                                                                                                                                                                                          |
  | message                              | Description of the pre-debit notification process                                                                                                                                                                                                                                                                                                                                                                                |
  | invoiceId<br />`only for cards`      | This is an acknowledgment ID that a pre debit notification has been sent for processing.                                                                                                                                                                                                                                                                                                                                         |
  | amount                               | The transaction amount for which the pre-debit notification has been sent.                                                                                                                                                                                                                                                                                                                                                       |
  | invoiceStatus<br />`only for cards`  | This is the status of the invoice whether it has been charged for recurring or not. Values can be:<br />\- Paid<br />\- Unpaid<br />\- Deleted<br />Since these statuses come from a third-party vendor, so these can vary if there is an addition of new status at the vendor end                                                                                                                                               |
  | approvedStatus<br />`only for cards` | This is for cases where the transaction is above 15000 as RBI guideline says approval is required through AFA (Additional Factor authentication). Values can be:<br />\- Pending<br />\- Approved<br />\- Not_applicable<br />Since these statuses come from third-party vendors, so these can vary if there is an addition of new status at the vendor end.                                                                     |

  **var1 JSON fields description**

  The **var1** variable is in JSON format and comprises of the following parameters:

  | JSON Field                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
  | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | authpayuid<br />**mandatory**                          | The value of mihpayid returned in the payment response of Registration transaction when transaction is successfully completed. As explained earlier in the document, you need to map this value against customer profile at his end so that correct authPayuid will be passed in the request.                                                                                                                                                                                                                                                                              |
  | requestId<br />**mandatory**                           | Unique request value generated at merchant's end to distinguish independent request call.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
  | debitDate<br />**mandatory for cards and UPI**         | This parameter contains the date of debit when the recurring would be charged by merchant.<br />**In UPI:** <ul><li>For all frequencies (other than Daily and Adhoc), the merchant must send the notification 48 hours before the debit.</li><li>For Daily and Adhoc frequency, the merchant must send the notification 24 hours before the debit. If the notification is sent after these durations, then the debit will fail.</li></ul>                                                                                                                                  |
  | invoiceDisplayNumber<br />**mandatory only for cards** | A unique display number by merchant for every subsequent invoice/recurring charge. This can be displayed on the merchant's panel to the customer. This same value needs to be sent in the recurring api also.                                                                                                                                                                                                                                                                                                                                                              |
  | amount<br />**mandatory for cards and UPI**            | The transaction amount which will be deducted from the customer's payment instrument.<br />**For Cards:** <ul><li>In case of Fixed billing plan, this amount should be same as billingAmount sent during Registration transaction.</li><li>In case of Adhoc billing plan, this amount should be equal to or lesser than billingAmount sent during the Registration transaction.<br />**Note**: The amount mentioned in the Pre-Debit notification API for UPI should be same as the next execution amount. Else, the next recurring execution request will fail.</li></ul> |
  | action<br />**optional**                               | Any of the following actions can be performed:<br />• **Retrieve**: Query the status of the pre-debit notification. Only authpayuid and invoice display numbers are mandatory for this action.<br />• **Delete**: Delete the already generated pre debit. Only authpayuid and invoice display numbers are mandatory for this action.                                                                                                                                                                                                                                       |
</Accordion>

***

### Step 2: Recurring Payment Transaction

All successful registration transactions are charged over the recurring interface with server-to-server API without any additional 2FA or the customers' involvement.

<Callout icon="📘" theme="info">
  ### **Notes**:

  - Check the mandate status, call the **Pre-Debit Notification** API before calling the **Recurring Payment Transaction** API to make a recurring payment transaction.
</Callout>

<Callout icon="🚧" theme="warn">
  ### **Assumptions**: If the merchant has already performed a successful registration transaction with Net Banking/UPI/Card and mihpayid is received in response to the registration transaction captured successfully and mapped to the customer at the merchant's end.
</Callout>

**Environment**

|                        |                                                                  |
| :--------------------- | :--------------------------------------------------------------- |
| Production Environment | [https://info.payu.in/merchant/](https://info.payu.in/merchant/) |
| Test Environment       | [https://test.payu.in/merchant/](https://test.payu.in/merchant/) |

<Accordion title="Sample Request" icon="fa-terminal">
  ```curl
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&command=si_transaction&var1={"authpayuid": "6611192557","invoiceDisplayNumber":"12345678910","amount": 3,"txnid": "REC15113506209","phone": "9999999999","email": "chota.bheem@gmail.com","udf2": "","udf3": "","udf4": "","udf5": ""}&hash=jbUS07Og8BToVZ"
  ```
  ```python
  import requests
  import urllib.parse

  # PayU API endpoint
  url = "https://test.payu.in/merchant/postservice?form=2"

  # Headers
  headers = {
      "accept": "application/json",
      "Content-Type": "application/x-www-form-urlencoded"
  }

  # Form data
  form_data = {
      "key": "JP***g",
      "command": "si_transaction",
      "var1": '{"authpayuid": "6611192557","invoiceDisplayNumber":"12345678910","amount": 3,"txnid": "REC15113506209","phone": "9999999999","email": "chota.bheem@gmail.com","udf2": "","udf3": "","udf4": "","udf5": ""}',
      "hash": "jbUS07Og8BToVZ"
  }

  # Make the POST request
  try:
      response = requests.post(url, headers=headers, data=form_data)
      print(f"Status Code: {response.status_code}")
      print(f"Response: {response.text}")
  except requests.exceptions.RequestException as e:
      print(f"Error: {e}")
  ```
  ```java
  import java.io.IOException;
  import java.net.URI;
  import java.net.URLEncoder;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;
  import java.nio.charset.StandardCharsets;
  import java.time.Duration;
  import java.util.HashMap;
  import java.util.Map;
  import java.util.stream.Collectors;

  public class PayUApiClient {
      
      private static final HttpClient client = HttpClient.newBuilder()
              .connectTimeout(Duration.ofSeconds(30))
              .build();
      
      public static void main(String[] args) {
          try {
              makePayURequest();
          } catch (Exception e) {
              System.err.println("Error: " + e.getMessage());
          }
      }
      
      public static void makePayURequest() throws IOException, InterruptedException {
          String url = "https://test.payu.in/merchant/postservice?form=2";
          
          // Prepare form data
          Map<String, String> formData = new HashMap<>();
          formData.put("key", "JP***g");
          formData.put("command", "si_transaction");
          formData.put("var1", "{\"authpayuid\": \"6611192557\",\"invoiceDisplayNumber\":\"12345678910\",\"amount\": 3,\"txnid\": \"REC15113506209\",\"phone\": \"9999999999\",\"email\": \"chota.bheem@gmail.com\",\"udf2\": \"\",\"udf3\": \"\",\"udf4\": \"\",\"udf5\": \"\"}");
          formData.put("hash", "jbUS07Og8BToVZ");
          
          // Convert to URL encoded string
          String formBody = formData.entrySet().stream()
                  .map(entry -> URLEncoder.encode(entry.getKey(), StandardCharsets.UTF_8) + 
                               "=" + URLEncoder.encode(entry.getValue(), StandardCharsets.UTF_8))
                  .collect(Collectors.joining("&"));
          
          // Build request
          HttpRequest request = HttpRequest.newBuilder()
                  .uri(URI.create(url))
                  .header("accept", "application/json")
                  .header("Content-Type", "application/x-www-form-urlencoded")
                  .POST(HttpRequest.BodyPublishers.ofString(formBody))
                  .build();
          
          // Send request
          HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
          
          System.out.println("Status Code: " + response.statusCode());
          System.out.println("Response: " + response.body());
      }
  }
  ```
  ```javascript
  // PayU API call using modern Async/Await Fetch
  async function makePayURequest() {
      const url = "https://test.payu.in/merchant/postservice?form=2";
      
      // Headers
      const headers = {
          "accept": "application/json",
          "Content-Type": "application/x-www-form-urlencoded"
      };
      
      // Form data
      const formData = new URLSearchParams({
          "key": "JP***g",
          "command": "si_transaction",
          "var1": '{"authpayuid": "6611192557","invoiceDisplayNumber":"12345678910","amount": 3,"txnid": "REC15113506209","phone": "9999999999","email": "chota.bheem@gmail.com","udf2": "","udf3": "","udf4": "","udf5": ""}',
          "hash": "jbUS07Og8BToVZ"
      });
      
      try {
          const response = await fetch(url, {
              method: "POST",
              headers: headers,
              body: formData
          });
          
          const responseText = await response.text();
          
          console.log(`Status: ${response.status}`);
          console.log(`Response: ${responseText}`);
          
          return {
              status: response.status,
              data: responseText
          };
          
      } catch (error) {
          console.error("Error:", error);
          throw error;
      }
  }

  // Call the function
  makePayURequest()
      .then(result => console.log("Success:", result))
      .catch(error => console.error("Failed:", error));
  ```
  ```csharp
  using System;
  using System.Collections.Generic;
  using System.Net.Http;
  using System.Text;
  using System.Threading.Tasks;

  class Program
  {
      private static readonly HttpClient client = new HttpClient();

      static async Task Main(string[] args)
      {
          string url = "https://test.payu.in/merchant/postservice?form=2";
          
          // Set headers
          client.DefaultRequestHeaders.Add("accept", "application/json");
          
          // Prepare form data
          var formData = new List<KeyValuePair<string, string>>
          {
              new KeyValuePair<string, string>("key", "JP***g"),
              new KeyValuePair<string, string>("command", "si_transaction"),
              new KeyValuePair<string, string>("var1", "{\"authpayuid\": \"6611192557\",\"invoiceDisplayNumber\":\"12345678910\",\"amount\": 3,\"txnid\": \"REC15113506209\",\"phone\": \"9999999999\",\"email\": \"chota.bheem@gmail.com\",\"udf2\": \"\",\"udf3\": \"\",\"udf4\": \"\",\"udf5\": \"\"}"),
              new KeyValuePair<string, string>("hash", "jbUS07Og8BToVZ")
          };
          
          var formContent = new FormUrlEncodedContent(formData);
          
          try
          {
              HttpResponseMessage response = await client.PostAsync(url, formContent);
              string responseContent = await response.Content.ReadAsStringAsync();
              
              Console.WriteLine($"Status Code: {response.StatusCode}");
              Console.WriteLine($"Response: {responseContent}");
          }
          catch (HttpRequestException e)
          {
              Console.WriteLine($"Error: {e.Message}");
          }
      }
  }
  ```
  ```php
  // PayU API endpoint
  $url = "https://test.payu.in/merchant/postservice?form=2";

  // Form data
  $postData = [
      'key' => 'JP***g',
      'command' => 'si_transaction',
      'var1' => '{"authpayuid": "6611192557","invoiceDisplayNumber":"12345678910","amount": 3,"txnid": "REC15113506209","phone": "9999999999","email": "chota.bheem@gmail.com","udf2": "","udf3": "","udf4": "","udf5": ""}',
      'hash' => 'jbUS07Og8BToVZ'
  ];

  // Initialize cURL
  $ch = curl_init();

  // Set cURL options
  curl_setopt_array($ch, [
      CURLOPT_URL => $url,
      CURLOPT_POST => true,
      CURLOPT_POSTFIELDS => http_build_query($postData),
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_HTTPHEADER => [
          'accept: application/json',
          'Content-Type: application/x-www-form-urlencoded'
      ],
      CURLOPT_TIMEOUT => 30,
      CURLOPT_FOLLOWLOCATION => true,
      CURLOPT_SSL_VERIFYPEER => false, // Only for testing
  ]);

  // Execute request
  $response = curl_exec($ch);
  $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
  $error = curl_error($ch);

  // Close cURL
  curl_close($ch);

  // Handle response
  if ($error) {
      echo "cURL Error: " . $error . PHP_EOL;
  } else {
      echo "Status Code: " . $httpCode . PHP_EOL;
      echo "Response: " . $response . PHP_EOL;
  }
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-check-circle">
  #### Success Scenario

  Here is a sample response object returned against recurring payment API when the transaction is successfully charged.

  ```json
  {
    "status": 1,
    "message": "Transaction Processed successfully",
    "details": {
        "REC15113506209": {
            "authpayuid": "25600342065",
            "transactionid": "REC15113506209",
            "amount": "1.00",
            "user_credentials": "",
            "card_token": "",
            "payuid": "",
            "status": "captured",
            "udf1": "",
            "field9": "Transaction Completed Successfully",
            "udf2": "",
            "udf3": "",
            "udf4": "",
            "udf5": "",
            "phone": "9999999999",
            "email": "chota.bheem@gmail.com"
        }
    }
  }
  ```

  #### Failure Scenarios

  - Invalid hash

  ```json
  {
      "status": 0,
      "msg": "Invalid Hash."
  }
  ```

  - Basic authentication check failed

  ```json
  {
      "status": 1,
      "message": "Transaction Processed successfully",
      "details": {
          "REC9812123123": {
              "authpayuid": "6611192559",
              "transactionid": "REC9812123123",
              "amount": "1",
              "user_credentials": " ",
              "card_token": " ",
              "payuid": "",
              "status": "failed",
              "field9": "Basic authentication check failed",
              "phone": "",
              "email": ""
          }
      }
  }
  ```
</Accordion>

<Accordion title="Response Parameters" icon="fa-list">
  **JSON fields description of the Details parameter**

  | JSON Field    | Description                                                                                                                                                                       |
  | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | transactionid | This field contains the value of transaction ID parameter which is echoed back in the response. This is unique transaction ID generated by merchant during calling recurring API. |
  | amount        | This field contains the requested transaction amount is echoed back in the payment response.                                                                                      |
  | payuid        | This field contains the PayU's transaction ID for processed recurring transaction. Merchant can use this field for reference point in the settlement report.                      |
  | status        | This field gives the status of the transaction. Hence, the value of this field depends on whether the transaction was successful or not.                                          |
  | field9        | This field returns the description of transaction status which can help the merchant in providing better customer communication.                                                  |
  | phone         | The mobile number of the customer echoed back.                                                                                                                                    |
  | email         | Email ID of the customer echoed back.                                                                                                                                             |
  | udf1          | Extra information received in the request echoed back.                                                                                                                            |
  | udf2          | Extra information received in the request echoed back.                                                                                                                            |
  | udf3          | Extra information received in the request echoed back.                                                                                                                            |
  | udf4          | Extra information received in the request echoed back.                                                                                                                            |
  | udf5          | Extra information received in the request echoed back.                                                                                                                            |

  #### status field description

  This field gives the status of the transaction. Hence, the value of this field depends on whether the transaction was successful or not.<br />You must map the order status using this parameter only. The possible values of this parameter are:

  - **captured**: If the transaction is successful, the value will be captured. In some cases, the response of Net banking recurring can be captured over real-time basis (ICICI bank in the specific scenario).
  - **pending**: This is common with most Net Banking (except ICICI in the specific scenario) or UPI recurring transaction. In that case, the merchant should consider this as successful initiation of payment with bank / NPCI. The status will be notified back to the merchant over payment processing with individual bank gets completed.<br />For UPI, "pending" transactions get usually get converted into captured or failed within 10 mins from the time of initiation. The Query API can be called post 10 mins from initiation, whereas for Net Banking, it can be called up to T+2 once a day. For more information, refer to Capture response of Recurring Transaction for Net Banking and UPI.<br />For Net Banking, "pending" transaction gets converted into "captured" or "failed" from the same day till T+2 anytime, depending upon the bank account used by the customer in setting up registration.
  - **failed**: The value of the status as "failed" or blank must be treated as a failed transaction only.
  - **in-progress**: The status of transaction is in progress.

  To capture the final status of "pending" transaction to either "captured" or "failed", PayU recommends merchants to either implement Webhook URL or call **verify_payment** API after regular intervals. For more information on:

  - Webhook: Refer to [Webhooks](doc:webhooks)
  - **verify_payment** API: Refer to [Verify Payment API](ref:verify_payment_api)

  <Callout icon="📘" theme="info">
    ### **Note**:

    For UPI, call the **verify_settlement** API after 10 mins from time of initiation whereas for Net Banking it can be called up to T+2 once in a day.
  </Callout>
</Accordion>

***

## Additional Resources

• [Manage Recurring Payment for Cards](https://docs.payu.in/docs/manage-recurring-payment-for-cards) - Handle card-based recurring transactions<br />• [SI Parameter JSON Details](https://docs.payu.in/reference/si-parameter-json-details) - Detailed subscription parameter specifications
• [RBI Guidelines](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0) - Regulatory compliance information

<br />
