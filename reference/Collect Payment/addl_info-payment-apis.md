---
title: Additional Info for Payment APIs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Request parameters for \_payment API
<HTMLBlock>{`
<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key<code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> This parameter is the unique Merchant Key provided by PayU for your merchant account.
      </td>

      <td>
        Your Test Key
      </td>
    </tr>

    <tr>
      <td>
        txnid<code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction. <code>Character limit</code>: 25

        - **Note**: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID.'
      </td>

      <td>
        fd3e847h2
      </td>
    </tr>

    <tr>
      <td>
        amount<code>mandatory</code>
      </td>

      <td>
        <code>float</code> This parameter should contain the payment amount of the particular transaction.

        - **Note**: Type-cast the amount to float type Depending upon the merchant use case, this value will vary.

        - It can be either 0 INR (for Net Banking) or min 1 INR (for Cards & UPI) in penny transaction use case.

        - In the case of first instalment use cases, this amount can be equal to initiate setup amount, but this use case will be supported only against selected Net Banking (ICICI and HDFC), all Credit / Debit Cards, and UPI
      </td>

      <td>
        1000
      </td>
    </tr>

    <tr>
      <td>
        productinfo



        <code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> This parameter should contain a brief product description. It should be a string describing the product. <code>Character limit</code>: 100
      </td>

      <td>
        Time Magazine Subscription
      </td>
    </tr>

    <tr>
      <td>
        firstname



        <code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> Must contain the first name of the customer. <code>Character limit</code>: 60
      </td>

      <td>
        Ashish
      </td>
    </tr>

    <tr>
      <td>
        email



        <code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> Must contain the email of the customer. This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information. Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions. Character limit: 50
      </td>

      <td>
        [Ashish@test.com](mailto:Ashish@test.com)
      </td>
    </tr>

    <tr>
      <td>
        phone



        <code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> Must contain the phone number of the customer.This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions. Character limit: 50
      </td>

      <td>
        9843176540
      </td>
    </tr>

    <tr>
      <td>
        surl



        <code>mandatory</code>
      </td>

      <td>
        surL is the acronym for Success URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is successful.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        furl



        <code>mandatory</code>
      </td>

      <td>
        furl is the acronym for for Failure URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is failed.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        api\_version



        <code>mandatory</code>
      </td>

      <td>
        This parameter must always needs to be passed as 7.
      </td>

      <td>
        7
      </td>
    </tr>

    <tr>
      <td>
        hash



        <code>mandatory</code>
      </td>

      <td>
        Hash is a crucial parameter used to ensure that any date is not tampered while redirecting customer from the merchant website to PayU's payment interface while registration transactions.It is SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si\_details by merchant salt.In the case of registration transaction, the formula is used to calculate this hash is similar to the following: <code>HASH = SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|SALT)</code>

        - **Note:Hash logic fo&#x72;_&#x70;ayment API version 19: The following hash logic must be used for_ payment API with api\_version=19**: <code>key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|user_token|offer_key|offer_auto_apply|cart_details|extra_charges|phone</code>
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        <h3>Seamless integration</h3>
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        pg



        <code>mandatory for seamless flow</code>
      </td>

      <td>
        <code>String</code> The pg parameter must contain the payment method. If no value is specified for this parameter 'CC' will be takes as default value. Refer to the following sections for integration with various payment modes:

        - Net Banking: **NB**
        - Card:
        - **DC**for Debit Card
        - **CC** for Credit Card
        - UPI: **UPI**
        - Wallets: **CASH**
        - EMI: **EMI**
        - BNPL:**BNPL**
        - EFTNET (NEFT/RTGS): **NEFTRTGS**
        - QR: **QR**
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        bankcode



        <code>mandatory for seamless flow</code>
      </td>

      <td>
        Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. For more information, refer to any of the following based on the payment mode used in the **pg** parameter:

        - For NetBanking: [Net Banking Codes](doc:net-banking-codes)
        - For Cards: [Card Number Formats](doc:card-number-formats) and [Card Type Codes and Supported Banks for Cards](doc:card-type-codes-and-supported-banks-for-cards).
        - For UPI: [UPI Handles](doc:upi-handles)
        - For Wallets: [Wallet Codes](doc:wallet-codes)
        - For EMI: [EMI Codes](doc:emi-codes)
        - For BNPL: [BNPL Codes](doc:bnpl-codes)
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf1



        <code>optional for seamless flow</code>
      </td>

      <td>
        User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5. <code>Character Limit-255</code>
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf2



        <code>optional for seamless flow</code>
      </td>

      <td>
        User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5. <code>Character Limit-255</code>
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf3



        <code>optional for seamless flow</code>
      </td>

      <td>
        User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5. <code>Character Limit-255</code>
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf4



        <code>optional for seamless flow</code>
      </td>

      <td>
        User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5. <code>Character Limit-255</code>
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        ud1f5



        <code>optional for seamless flow</code>
      </td>

      <td>
        User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5. <code>Character Limit-255</code>
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        ccnum



        <code>mandatory for cards in seamless flow</code>
      </td>

      <td>
        <code>String</code> Use 13-19 digit card number for credit/debit cards (15 digits for AMEX, 13-19 for Maestro) and validate with LUHN algorithm. Refer to[Card Number Formats](doc:card-number-formats)and display.error message for an invalid input.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        ccvv



        <code>mandatory for cards in seamless flow</code>
      </td>

      <td>
        <code>String</code> This parameter must contain the name on card – as entered by the customer for the transaction.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        ccexpmon



        <code>mandatory for cards in seamless flow</code>
      </td>

      <td>
        <code>String</code> This parameter must contain the card's expiry month – as entered by the user for the transaction. It must always be in 2 digits or in MM format. For months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – It should be 10,11 and 12 respectively.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        ccexpyr



        <code>mandatory for cards in seamless flow</code>
      </td>

      <td>
        <code>String</code> This parameter must contain the card's expiry year – as entered by the customer for the transaction. It must be of four digits.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        threeDS2RequestData



        <code>mandatory for cards in seamless flow</code>
      </td>

      <td>
        <code>String</code> This parameter must contain the card's expiry year – as entered by the customer for the transaction. It must be of four digits.. For more information, refer to Request Parameter for[3DS Secure 2.0 Transaction](doc:collect-payments-with-cards-seamless#request-parameter-for-3ds-secure-20-transaction).
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        <h3>Server-to-Server Integration</h3>
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        s2s\_client\_ip



        <code>mandatory for S2S</code>
      </td>

      <td>
        <code>String</code>This parameter must have the source IP of the customer.

        - **Note**: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        s2s\_device\_info



        <code>mandatory for S2S</code>
      </td>

      <td>
        <code>String</code>This parameter must have the customer agent's device. Note: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        txn\_s2s\_flow



        <code>mandatory for S2S</code>
      </td>

      <td>
        <code>String</code> This parameter must be passed with any of the following values:

        - **4** for S2S
        - **3** for Direct Authorization
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        authentication\_flow



        <code>mandatory for S2S</code>
      </td>

      <td>
        This parameter must be passed with the value as **REDIRECT** for classic S2S integration.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        <strong>Webhooks</strong>
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        partner\_webhook\_success
      </td>

      <td>
        Parameter to pass the Webhook URL for Success transaction response, Multiple URLs can be passed by separating the URLs using (,) Comma. Use HTTP secure URLs. Pass the non URL encoded URL Only
      </td>

      <td>
        <a href="https://test.payu.in/admin/test_response">[https://test.payu.in/admin/test_response](https://test.payu.in/admin/test_response)</a>
      </td>
    </tr>

    <tr>
      <td>
        partner\_webhook\_failure
      </td>

      <td>
        Parameter to pass the Webhook URL for failure transaction response,  Multiple URLs can be passed by separating the URLs using (,) Comma. Use HTTP secure URLs. Pass the non URL encoded URL Only
      </td>

      <td>
        <a href="https://test.payu.in/admin/test_response">[https://test.payu.in/admin/test_response](https://test.payu.in/admin/test_response)</a>
      </td>
    </tr>
  </tbody>
</Table>
`}</HTMLBlock>

<br />

### Additional parameters for Guest Checkout

| **Parameter**                | **Description**                                                                                                                           | **Example** |
| :--------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| alt\_id `mandatory`          | `String` This parameter must contain Alt ID for the guest checkout.                                                                       |             |
| ccexpmon `mandatory`         | `String` This parameter must contain the Alt ID expiry month. For VISA cards, Plain card's expiry month need to be posted this parameter. | 10          |
| ccexpyr `mandatory`          | `String` This parameter must contain the Alt ID expiry year. For VISA cards, Plain card's expiry year need to be posted this parameter.   | 2021        |
| additional\_info `mandatory` | `JSON`The fields which are included in this JSON are described in the next table.                                                         |             |

The description of the fields in the additional\_info JSON.

| Field            | Description                                                                                                                                                                   |
| :--------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| trid             | trid is the acronym for Token Requestor ID and it is the identity given by the networks for creating the tokens. You should be able to get the same from your token provider. |
| tokenReferenceID | The Token Reference ID is generated along with the network token. You should be able to get the same from your token provider.                                                |
| TAVV             | It is a token authentication verification value given by schemes or interchange. Also, known as cryptogram.                                                                   |

### Additional parameters for Saved Card

#### Using Network tokens

<HTMLBlock>{`
<div style={{ maxWidth: "85%", overflowX: "auto" }}>

<Table>
  <thead>
    <tr>
      <th>
        <strong>Parameter</strong>
      </th>

      <th>
        <strong>Description</strong>
      </th>

      <th>
        <strong>Example</strong>
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ccnum
        <br/>
        <code>optional</code>
      </td>

      <td>
        <code>varchar</code> This parameter must contain the 13 to 19-digit card number for credit or debit cards in general.
      </td>

      <td>
        512***6789012346
      </td>
    </tr>

    <tr>
      <td>
        ccname
        <br/>
        <code>optional</code>
      </td>

      <td>
        <code>varchar</code> It is the customer's name on card.
      </td>

      <td>
        Ashish
      </td>
    </tr>

    <tr>
      <td>
        ccvv
        <br/>
        <code>optional</code>
      </td>

      <td>
        <code>varchar</code> This parameter must contain the CVV number of the card – as entered by the customer for the transaction.
      </td>

      <td>
        123
      </td>
    </tr>

    <tr>
      <td>
        ccexpmon
        <br/>
        <code>mandatory</code>
      </td>

      <td>
        <code>integer</code> This parameter must contain the Expiry month that is mentioned under card validity.
      </td>

      <td>
        10
      </td>
    </tr>

    <tr>
      <td>
        ccexpyr
        <br/>
        <code>mandatory</code>
      </td>

      <td>
        <code>integer</code> This parameter must contain the Expiry year that is mentioned under card validity.
      </td>

      <td>
        2022
      </td>
    </tr>

    <tr>
      <td>
        store_card_token
        <br/>
        <code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> This must include the Network token generated at your end.
      </td>

      <td>
        1234 4567 2456 3566
      </td>
    </tr>

    <tr>
      <td>
        storecard_token_type
        <br/>
        <code>mandatory</code>
      </td>

      <td>
        <code>integer</code> This parameter is used to specify the store card token type. For this scenario, you must include 1.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        additional_info
        <br/>
        <code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> This parameter will contain the additional information in the following JSON format:
        {"last4Digits": "1234", "<Glossary>TAVV</Glossary>": "ABCDEFGH","<Glossary>trid</Glossary>":"1234567890", "<Glossary>tokenRefNo</Glossary>":"abcde123456"}
      </td>

      <td>
        {"last4Digits": "1234", "tavv": "ABCDEFGH","trid":"1234567890", "tokenRefNo":"abcde123456"}
      </td>
    </tr>
  </tbody>
</Table>
</div>
`}</HTMLBlock>

#### Using Issuer tokens

<HTMLBlock>{`
<div style={{ maxWidth: "85%", overflowX: "auto" }}>

<Table>
  <thead>
    <tr>
      <th>
        <strong>Parameter</strong>
      </th>

      <th>
        <strong>Description</strong>
      </th>

      <th>
        <strong>Example</strong>
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ccvv
        <br/>
        <code>optional</code>
      </td>

      <td>
        <code>varchar</code> This parameter must contain the CVV number of the card – as entered by the customer for the transaction.
      </td>

      <td>
        123
      </td>
    </tr>

    <tr>
      <td>
        ccexpmon
        <br/>
        <code>mandatory</code>
      </td>

      <td>
        <code>integer</code> This parameter must contain the network token expiry month.
      </td>

      <td>
        10
      </td>
    </tr>

    <tr>
      <td>
        ccexpyr
        <br/>
        <code>mandatory</code>
      </td>

      <td>
        <code>integer</code> This parameter must contain the network token expiry year.
      </td>

      <td>
        2024
      </td>
    </tr>

    <tr>
      <td>
        store_card_token
        <br/>
        <code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> This must include the token generated by PayU for the card.
      </td>

      <td>
        1234 4567 2456 3566
      </td>
    </tr>

    <tr>
      <td>
        storecard_token_type
        <br/>
        <code>mandatory</code>
      </td>

      <td>
        <code>integer</code> This parameter is used to specify the store card token type. For this scenario, you must include 0.
      </td>

      <td>
        0
      </td>
    </tr>

    <tr>
      <td>
        additional_info
        <br/>
        <code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> This parameter will contain the additional information in the following JSON format:
        {"trMerchantId":"INBANPAYUWIBPAY011","tokenReferenceId":"02ac786d-0081-4b1a-a2a6-b0755a83964c","tokenBank":"HDFC","last4Digits":"8179"}
      </td>

      <td>
        {"trMerchantId":"INBANPAYUWIBPAY011","tokenReferenceId":"02ac786d-0081-4b1a-a2a6-b0755a83964c","tokenBank":"HDFC","last4Digits":"8179"}
      </td>
    </tr>
  </tbody>
</Table>
</div>
`}</HTMLBlock>

<br />

#### Using card tokenized with PayU

<HTMLBlock>{`
<div style={{ maxWidth: "85%", overflowX: "auto" }}>

<Table>
  <thead>
    <tr>
      <th>
        <strong>Parameter</strong>
      </th>

      <th>
        <strong>Description</strong>
      </th>

      <th>
        <strong>Example</strong>
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ccvv
        <br/>
        <code>optional</code>
      </td>

      <td>
        <code>varchar</code> This parameter must contain the CVV number of the card – as entered by the customer for the transaction.
      </td>

      <td>
        123
      </td>
    </tr>

    <tr>
      <td>
        storecard_token_type
        <br/>
        <code>mandatory</code>
      </td>

      <td>
        <code>integer</code> This parameter is used to specify the store card token type. For this scenario, you must include 0.
      </td>

      <td>
        0
      </td>
    </tr>

    <tr>
      <td>
        user_credentials
        <br/>
        <code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> This parameter must contain the user credentials.
      </td>

      <td>
        a:b
      </td>
    </tr>

    <tr>
      <td>
        store_card_token
        <br/>
        <code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> This must include the token generated by PayU for the card.
      </td>

      <td>
        1234 4567 2456 3566
      </td>
    </tr>
  </tbody>
</Table>
</div>
`}</HTMLBlock>

<br />

## Using card on a decoupled Flow with Network token or other partner tokenization

| **Parameter**                        | **Description**                                                                                                                                                                                                                                                 | **Example**                                                                                |
| :----------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ccvv **optional**                    | `varchar` This parameter must contain the CVV number of the card – as entered by the customer for the transaction.                                                                                                                                              | 123                                                                                        |
| storecard\_token\_type **mandatory** | `integer` This parameter is used to specify store card token type, that is, tokenization partner. For this scenario, you must include 1.                                                                                                                        | 1                                                                                          |
| store\_card\_token **mandatory**     | `varchar` This must include the token generated by PayU for the card.                                                                                                                                                                                           | 1234 4567 2456 3566                                                                        |
| additional\_info **mandatory**       | This parameter will contain the additional information in the following JSON format: {"{user.glossary:last4Digits}": "1234", "<Glossary>TAVV</Glossary>": "ABCDEFGH","<Glossary>trid</Glossary>":"1234567890", "<Glossary>tokenRefNo</Glossary>":"abcde123456"} | {“last4Digits": “1234", “tavv": “ABCDEFGH","trid":"1234567890", “tokenRefNo":"abcde123456" |

#### Using Card on a decoupled flow with PayU tokenization

| **Parameter**                        | **Description**                                                                                                                                                                                                                                                 | **Example**                                                                                |
| :----------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ccvv **optional**                    | `varchar` This parameter must contain the CVV number of the card – as entered by the customer for the transaction.                                                                                                                                              | 123                                                                                        |
| storecard\_token\_type **mandatory** | `integer` This parameter is used to specify store card token type, that is, tokenization partner. For this scenario, you must include 0.                                                                                                                        | 1                                                                                          |
| store\_card\_token **mandatory**     | `varchar` This must include the token generated by PayU for the card.                                                                                                                                                                                           | 1234 4567 2456 3566                                                                        |
| additional\_info **mandatory**       | This parameter will contain the additional information in the following JSON format: {"{user.glossary:last4Digits}": "1234", "<Glossary>TAVV</Glossary>": "ABCDEFGH","<Glossary>trid</Glossary>":"1234567890", "<Glossary>tokenRefNo</Glossary>":"abcde123456"} | {“last4Digits": “1234", “tavv": “ABCDEFGH","trid":"1234567890", “tokenRefNo":"abcde123456" |

## Character Limit for Request Parameters

| Parameter   | Production Environment | Test Environment |
| ----------- | ---------------------- | :--------------- |
| productinfo | 100                    | 100              |
| firstname   | 60                     | 20               |
| email       | 50                     | 50               |
| lastname    | 20                     | 20               |
| address1    | 100                    | 100              |
| address2    | 100                    | 100              |
| city        | 50                     | 50               |
| state       | 50                     | 50               |
| country     | 50                     | 50               |
| zipcode     | 20                     | 20               |
| surl        | 50                     | 50               |
| furl        | 50                     | 50               |
| curl        | 50                     | 50               |
| udf1 - udf5 | 255                    | 255              |

## Response parameters

## General response parameters for all Web Checkout integrations
<HTMLBlock>{`
<Table>
  <thead>
    <tr>
      <th>
        **Variable**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        mihpayid
      </td>

      <td>
        Transaction ID is a unique number assigned by PayU for each transaction. Keep note of it for future reference for inquiry or refund."
      </td>
    </tr>

    <tr>
      <td>
        mode
      </td>

      <td>
        This parameter describes the payment category by which the transaction was completed or attempted by the customer. For the payment categories, refer to

        [Payment Mode Codes](doc:payment-mode-codes)

        .
      </td>
    </tr>

    <tr>
      <td>
        status
      </td>

      <td>
        This parameter indicates the outcome of the transaction as 'success', 'failed' or 'pending'. A value of 'success' means the transaction was successful, 'failure' or 'pending' means the transaction failed.
      </td>
    </tr>

    <tr>
      <td>
        key
      </td>

      <td>
        This parameter is used to identify the merchant's PayU account. It is the same key used during the transaction request.
      </td>
    </tr>

    <tr>
      <td>
        txnid
      </td>

      <td>
        This parameter would contain the transaction ID value posted by the merchant during the transaction request.
      </td>
    </tr>

    <tr>
      <td>
        amount
      </td>

      <td>
        This parameter would contain the original amount which was sent in the transaction request by the merchant.
      </td>
    </tr>

    <tr>
      <td>
        productinfo
      </td>

      <td>
        This parameter would contain the same value of product information which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        firstname
      </td>

      <td>
        This parameter would contain the same value of first name which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        lastname
      </td>

      <td>
        This parameter would contain the same value of last name which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        email
      </td>

      <td>
        This parameter would contain the same value of email which was sent.
      </td>
    </tr>

    <tr>
      <td>
        phone
      </td>

      <td>
        This parameter would contain the same value of phone which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf
      </td>

      <td>
        This parameter would contain the same value of udf values that were sent in the transaction request from the merchant’s end to PayU. It ranges from udf1 to udf5.
      </td>
    </tr>

    <tr>
      <td>
        hash
      </td>

      <td>
        PayU calculates a hash using other parameters and returns it to the merchant. The merchant must verify it and then mark a transaction as success/failure. This is to ensure the integrity of the transaction. For more information, refer to

        [Generate Hash](doc:generate-hash-merchant-hosted)
      </td>
    </tr>

    <tr>
      <td>
        error
      </td>

      <td>
        This parameter provides the reason for failure for failed transactions.

        - _Note_\* that failure reasons may vary depending on the error codes from different banks.
      </td>
    </tr>

    <tr>
      <td>
        error\_message
      </td>

      <td>
        This parameter contains the error message. For the list of error message, refer to

        [Error Codes](ref:error-codes)

        .
      </td>
    </tr>

    <tr>
      <td>
        bankcode
      </td>

      <td>
        This parameter holds the code of the payment option used in the transaction, such as Visa Debit Card - VISA, Master Debit Card - MAST.
      </td>
    </tr>

    <tr>
      <td>
        PG\_TYPE
      </td>

      <td>
        This parameter indicates the payment gateway used for the transaction, such as 'CC-PG' for credit card payment gateway.
      </td>
    </tr>

    <tr>
      <td>
        bank\_ref\_num
      </td>

      <td>
        For each successful transaction – this parameter would contain the bank reference number generated by the bank.
      </td>
    </tr>

    <tr>
      <td>
        unmappedstatus
      </td>

      <td>
        This parameter holds the status of a transaction in PayU's internal database, which can include intermediate states. Possible values include: dropped, bounced, captured, auth, failed, usercancelled, or pending. For information, refer to

        [Payment State Explanations](ref:payment-state-explanations)

        .
      </td>
    </tr>
  </tbody>
</Table>
`}</HTMLBlock>
## Response for initial Server-to-Server request

| **Parameter**     | **Description**                                                                                                                                                                                                                                                              |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| result            | This parameter contains a JSON Object that includes **post\_uri** and **post\_data** fields.                                                                                                                                                                                 |
| result.post\_uri  | This field contains the redirect URL.                                                                                                                                                                                                                                        |
| result.post\_data | post\_data is a base64 encoded string. The merchant needs to decode post\_data, which is an HTML format with auto submit, which then needs to be shown on the customer’s browser. The HTML being auto submit, it will take the customer to the bank page for authentication. |
| status            | This field contains the status for the transaction.                                                                                                                                                                                                                          |
| error             | For the failed transactions, this parameter provides the reason for  failure.                                                                                                                                                                                                |
| message           | This field contains any additional message about the transaction.                                                                                                                                                                                                            |

<Callout icon="📘" theme="info">
  ### Note:

  The reason for failure depends upon the error codes provided by different banks and hence the detailing of error reasons may differ from one transaction to another. The merchant can use this parameter to retrieve the reason for failure for a particular transaction.
</Callout>

#### metaData JSON Fields Description

| **Field**      | **Description**                                                                                                                                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| message        | This field contains any additional message about the transaction.                                                                                       |
| referenceId    | This field contains the reference ID of the transaction.                                                                                                |
| statusCode     | This field contains the status code for the transaction.                                                                                                |
| txnId          | This field contains the transaction ID of the transaction that was posted in the request.                                                               |
| unmappedStatus | This field contains the unmapped status of the transaction. For more information, refer to [Payment State Explanations](ref:payment-state-explanations) |

#### result JSON Fields Description
<HTMLBlock>{`
<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        **Field**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        mihpayid
      </td>

      <td>
        It is a unique reference number created for each transaction at PayU’s end. You must note this transaction ID as this will be used as a reference for all the future actions on this transaction like Inquiry or Refund.
      </td>
    </tr>

    <tr>
      <td>
        mode
      </td>

      <td>
        This parameter describes the payment category by which the transaction was completed or attempted by the customer. For the payment categories, refer to

        [Payment Mode Codes](doc:payment-mode-codes)
      </td>
    </tr>

    <tr>
      <td>
        status
      </td>

      <td>
        This parameter gives the status of the transaction as either success, failed or pending. Possible values: success, failure, pending If the value of the ‘status’ parameter is ’success’, the transaction is successful. If the value of ‘status’ is ‘failure’ or ‘pending’, must be treated as a failed transaction only.
      </td>
    </tr>

    <tr>
      <td>
        key
      </td>

      <td>
        This parameter contains the merchant key for the merchant’s account at PayU. It would be the same as the key used while the transaction request is being posted from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        txnid
      </td>

      <td>
        This parameter would contain the transaction ID value posted by the merchant during the transaction request.
      </td>
    </tr>

    <tr>
      <td>
        amount
      </td>

      <td>
        This parameter would contain the original amount which was sent in the transaction request by the merchant.
      </td>
    </tr>

    <tr>
      <td>
        productinfo
      </td>

      <td>
        This parameter would contain the same value of product information which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        firstname
      </td>

      <td>
        This parameter would contain the same value of first name which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        lastname
      </td>

      <td>
        This parameter would contain the same value of last name which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        email
      </td>

      <td>
        This parameter would contain the same value of email which was sent.
      </td>
    </tr>

    <tr>
      <td>
        phone
      </td>

      <td>
        This parameter would contain the same value of phone which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf
      </td>

      <td>
        This parameter would contain the same value of udf values that were sent in the transaction request from the merchant’s end to PayU. It ranges from udf1 to udf5.
      </td>
    </tr>

    <tr>
      <td>
        hash
      </td>

      <td>
        PayU calculates the hash using a string of other parameters and returns it to the merchant. The merchant must verify the hash, and only then mark a transaction as success/failure. This is to make sure that the transaction hasn’t been tampered with. The calculation is as follows:  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)

        - _Note_\*: The handling of udf1 – udf5 parameters remains similar to the hash calculation when the merchant sends it in the transaction request to PayU. If any of the udf (udf1-udf5) was posted in the transaction request, it must be taken in hash calculation also. If none of the udf parameters were posted in the transaction request, they should be left empty in the hash calculation too.
      </td>
    </tr>

    <tr>
      <td>
        error
      </td>

      <td>
        For the failed transactions, this parameter provides the reason for  failure. 

        - _Note_\*: The reason for failure depends upon the error codes provided by different banks and hence the detailing of error reasons may differ from one transaction to another. The merchant can use this parameter to retrieve the reason for failure for a particular transaction.
      </td>
    </tr>

    <tr>
      <td>
        bankcode
      </td>

      <td>
        This parameter contains the code indicating the payment option used for the transaction. For example, in the Debit Card mode, there are different options like Visa Debit Card, Mastercard, Maestro etc. For each option, a unique bank code exists. It would be returned in this bank code parameter. For example, Visa Debit Card – VISA, Master Debit Card – MAST.
      </td>
    </tr>

    <tr>
      <td>
        PG\_TYPE
      </td>

      <td>
        This parameter gives information on the payment gateway used for the transaction. For example, if CC PG was used, it would contain the value CC-PG. Similarly, it would have a unique value for all different types of payment gateways.
      </td>
    </tr>

    <tr>
      <td>
        bank\_ref\_num
      </td>

      <td>
        For each successful transaction – this parameter would contain the bank reference number generated by the bank.
      </td>
    </tr>

    <tr>
      <td>
        unmappedstatus
      </td>

      <td>
        This parameter contains the status of a transaction as per the internal database of PayU. PayU’s system has several intermediate status which are used for tracking various activities internal to the system. For more information, refer to

        [Payment State Explanations](ref:payment-state-explanations)

        .
      </td>
    </tr>
  </tbody>
</Table>

#### binData fields description (applicable for only for Cards)

<Table>
  <thead>
    <tr>
      <th>
        **Field**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        pureS2SSupported
      </td>

      <td>
        This field contains contains any of the following to indicate whether the card supports S2S:

        - **true**: Card supports S2S
        - **false**: Card does not support S2S
      </td>
    </tr>

    <tr>
      <td>
        issuingBank
      </td>

      <td>
        This field contains the card issuing bank.
      </td>
    </tr>

    <tr>
      <td>
        cardType
      </td>

      <td>
        This field contains the card type such as VISA, MasterCard, etc.
      </td>
    </tr>

    <tr>
      <td>
        isDomestic
      </td>

      <td>
        This field contains contains any of the following to indicate whether the card is domestic or international:

        - **true**: It is a domestic card
        - **false**: It is an international card
      </td>
    </tr>
  </tbody>
</Table>
`}</HTMLBlock>
```
  {
  "mihpayid": "403993715531077182",
  "mode": "CC",
  "status": "success",
  "unmappedstatus": "captured",
  "key": "JPM7Fg",
  "txnid": "ypl938459435dfdfdf",
  "amount": "1000.00",
  "cardCategory": "domestic",
  "discount": "0.00",
  "net_amount_debit": "1000",
  "addedon": "2024-02-27 15:00:42",
  "productinfo": "iPhone",
  "firstname": "Ashish",
  "lastname": "",
  "address1": "",
  "address2": "",
  "city": "",
  "state": "",
  "country": "",
  "zipcode": "",
  "email": "ashish@gmail.com",
  "phone": "9876543210",
  "udf1": "",
  "udf2": "",
  "udf3": "",
  "udf4": "",
  "udf5": "",
  "udf6": "",
  "udf7": "",
  "udf8": "",
  "udf9": "",
  "udf10": "",
  "hash": "84bbbf0fa3ba2a39942f6c3deab234c4d00bc5b6aceee5cda3c8200d6e1714e19c224d47e24d0c4a9a0cce40eddbae1dc46455c69e5e7d5dd62f6636bfab337c",
  "field1": "896193988312194700",
  "field2": "857712",
  "field3": "1000.00",
  "field4": "",
  "field5": "00",
  "field6": "02",
  "field7": "AUTHPOSITIVE",
  "field8": "AUTHORIZED",
  "field9": "Transaction is Successful",
  "payment_source": "payu",
  "PG_TYPE": "CC-PG",
  "bank_ref_num": "896193988312194700",
  "bankcode": "CC",
  "error": "E000",
  "error_Message": "No Error",
  "cardnum": "XXXXXXXXXXXX2346",
  "cardhash": "This field is no longer supported in postback params.",
  "splitInfo": "{\"splitStatus\":\"splitNotReceived\",\"splitSegments\":[]}"
}
```

## Merchant Hosted Checkout

### Cards

#### Sample request

```curl
curl --location 'https://test.payu.in/_payment' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e' \
--data-urlencode 'key=JF****g' \
--data-urlencode 'firstname=Ashish' \
--data-urlencode 'email=test@example.com' \
--data-urlencode 'amount=10' \
--data-urlencode 'phone= 9876543210' \
--data-urlencode 'productinfo=Product_info' \
--data-urlencode 'surl=http://pp30admin.payu.in/test_response' \
--data-urlencode 'furl=http://pp30admin.payu.in/test_response' \
--data-urlencode 'pg=CC' \
--data-urlencode 'bankcode=CC' \
--data-urlencode 'lastname=Test' \
--data-urlencode 'ccname=Test User' \
--data-urlencode 'ccvv=123' \
--data-urlencode 'ccexpmon=06' \
--data-urlencode 'ccexpyr=2024' \
--data-urlencode 'txnid=jYhbOYH9o4' \
--data-urlencode 'hash=e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184' \
--data-urlencode 'ccnum=4012000000002004' \
--data-urlencode 'txn_s2s_flow=4' \
--data-urlencode 'threeDS2RequestData={
    "browserInfo": {
        "userAgent": "Mozilla\/5.0 (X11 Linux x86_64) AppleWebKit\/537.36 (KHTML, like Gecko) HeadlessChrome\/93.0.4577.0 Safari\/537.36",
        "acceptHeader": "*\/*",
        "language": "en-US",
        "colorDepth": "24",
        "screenHeight": "600",
        "screenWidth": "800",
        "timeZone": "-300",
        "javaEnabled": true,
        "ip": "10.248.2.71"
    }
}'
```

#### Sample response

**Formatted response**

```
Array
(
    [mihpayid] => 403993715524069222
    [mode] => CC
    [status] => success
    [unmappedstatus] => captured
    [key] => JF***g
    [txnid] => EaE4ZO3vU4iPsp
    [amount] => 10.00
    [cardCategory] => domestic
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2021-09-08 19:37:19
    [productinfo] => iPhone
    [firstname] => Ashish
    [lastname] =>
    [address1] =>
    [address2] =>
    [city] =>
    [state] =>
    [country] =>
    [zipcode] =>
    [email] => test@gmail.com
    [phone] => 9876543210
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
    [hash] => ed99957adb08fea56c907b88e8d158a79c3562c67f96c298461509826f77a7ae9e88b2a176b3234c25f50bcd451271728719656f3bb59c13a52bebabc468615a
    [field1] => 0608273386032718000015
    [field2] => 986987
    [field3] => 10.00
    [field4] => 403993715524069222
    [field5] => 100
    [field6] => 02
    [field7] => AUTHPOSITIVE
    [field8] =>
    [field9] => Transaction is Successful
    [payment_source] => payu
    [PG_TYPE] => CC-PG
    [bank_ref_num] => 0608273386032718000015
    [bankcode] => CC
    [error] => E000
    [error_Message] => No Error
    [name_on_card] => payu
    [cardnum] => 512345XXXXXX2346
)

```

### UPI

#### Sample request

```curl
curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=xdB9G7qYpfqszo&amount=10&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=UPI&bankcode=UPI&vpa=VPA-anything@payu&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb"
```
```
```

#### Sample response

```
Array
(
    [mihpayid] => 403993715523409521
    [mode] => UPI
    [status] => success
    [unmappedstatus] => captured
    [key] => JPM7Fg
    [txnid] => 5jJ9xRceXX1ydT
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 1000
    [addedon] => 2021-07-02 15:03:50
    [productinfo] => iPhone
    [firstname] => PayU User
    [lastname] =>
    [address1] =>
    [address2] =>
    [city] =>
    [state] =>
    [country] =>
    [zipcode] =>
    [email] => test@gmail.com
    [phone] => 9876543210
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
    [hash] => 716f92a6452adadba68d133ba7f5ca3f3403f03f554e3ef850911f3e6727ee73402b249054170ad276c8b55ca12368a5e27cc69ffb0642ef6403dae9a5708794
    [field1] => vpa-anything@payu
    [field2] => 5jJ9xRceXX1ydT
    [field3] =>
    [field4] => PayU User
    [field5] => AXIhh4ExnaJ9dKiJvPxsewHwxMMmT3ba7UY
    [field6] =>
    [field7] => Transaction completed successfully
    [field8] =>
    [field9] => Transaction completed successfully
    [payment_source] => payu
    [PG_TYPE] => UPI-PG
    [bank_ref_num] => 5jJ9xRceXX1ydT
    [bankcode] => UPI
    [error] => E000
    [error_Message] => No Error
)
```

### Wallets

#### Sample request

```
curl -X POST "https://test.payu.in/_payment-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d"key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cash&bankcode=paytm&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
```

#### Sample response

```
Array
(
    [mihpayid] => 403993715527518775
    [mode] => CASH
    [status] => success
    [unmappedstatus] => captured
    [key] => J*****g
    [txnid] => HC13glcAkssIkl
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2022-10-21 17:45:24
    [productinfo] => iPhone
    [firstname] => Ashish
    [lastname] =>
    [address1] =>
    [address2] =>
    [city] =>
    [state] =>
    [country] =>
    [zipcode] =>
    [email] => test@gmail.com
    [phone] => 9876543210
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
    [hash] => 007435a716982c7f5eec5cff95701f65eb1bdbff8f852e461224e3b5e17126ad26bb3a3ffdb95cded6a87d3515fe86fc58925cad024595a4a6825adfed2dc436
    [field1] =>
    [field2] =>
    [field3] =>
    [field4] =>
    [field5] =>
    [field6] =>
    [field7] =>
    [field8] =>
    [field9] => Transaction Completed Successfully
    [payment_source] => payu
    [PG_TYPE] => CASH-PG
    [bank_ref_num] => 540898ed-72e7-40a8-a96e-f17de621cbb4
    [bankcode] => CASH
    [error] => E000
    [error_Message] => No Error
    [splitInfo] => {"splitStatus":"splitNotReceived","splitSegments":[]}
)
```

### EMI

#### Sample request

```curl
curl -X POST "https://test.payu.in/_payment-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d"key=JP***g&txnid=H6mUfE0ccAY94j&amount=20000.00&firstname=Ashish&email=test@gmail.com&phone=9123412345&productinfo=iPhone&pg=EMI&bankcode=ICICID03&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=43754118*****12346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=&hash=782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36"
```

#### Sample response

```
Array
(
    [mihpayid] => 403993715523602563
    [status] => success
    [unmappedstatus] => captured
    [key] => JP***g
    [txnid] => v2tWbbdUOuacK9
    [amount] => 20000.00
    [discount] => 0.00
    [net_amount_debit] => 20000.00
    [addedon] => 2021-07-27 11:14:44
    [productinfo] => iPhone
    [firstname] => Ashish
    [lastname] =>
    [address1] =>
    [address2] =>
    [city] =>
    [state] =>
    [country] =>
    [zipcode] =>
    [email] => test@gmail.com
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
    [hash] => 10f8ead10cdf5f9b7bf9046987de046d63d62d6679dded9d5da8145f459066943570eec4aa184494ae77f99a8bcd55452af3c4eff0d7a7d3ba809c97b7c73045
    [field1] =>
    [field2] =>
    [field3] =>
    [field4] =>
    [field5] =>
    [field6] =>
    [field7] =>
    [field8] =>
    [field9] => Transaction Completed Successfully
    [payment_source] => payu
    [PG_TYPE] => EMI-PG
    [bank_ref_num] => 3d7cc4a4-00c8-4705-a0e7-5708d2c2bb75
    [bankcode]=> EMIA3
    [error] => E000
    [error_Message] => No Error
    [name_on_card] => payu
    [cardnum] =>512345XXXXXX2346
)
```

### BNPL

#### Sample request

```
curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=J****g&txnid=5jJ9xYceXX1ydT&amount=1000.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=BNPL&bankcode=LAZYPAY&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
```

#### Sample response

```
Array
(
    [mihpayid] => 403993715523409521
    [mode] => BNPL
    [status] => success
    [unmappedstatus] => captured
    [key] => J****g
    [txnid] => 5jJ9xYceXX1ydT
    [amount] => 1000.00
    [discount] => 0.00
    [net_amount_debit] => 1000
    [addedon] => 2021-07-02 15:03:50
    [productinfo] => iPhone
    [firstname] => PayU User
    [lastname] =>
    [address1] =>
    [address2] =>
    [city] =>
    [state] =>
    [country] =>
    [zipcode] =>
    [email] => test@gmail.com
    [phone] => 9876543210
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
    [hash] => 716f92a6452adadba68d133ba7f5ca3f3403f03f554e3ef850911f3e6727ee73402b249054170ad276c8b55ca12368a5e27cc69ffb0642ef6403dae9a5708794
    [field1] => 9876543210
    [field2] => 5jJ9xRceXX1ydT
    [field3] =>
    [field4] => PayU User
    [field5] => AXIhh4ExnaJ9dKiJvPxsewHwxMMmT3ba7UY
    [field6] =>
    [field7] => Transaction completed successfully
    [field8] =>
    [field9] => Transaction completed successfully
    [payment_source] => payu
    [PG_TYPE] => BNPL-PG
    [bank_ref_num] => 5jJ9xRceXX1ydT
    [bankcode] => LAZYPAY
    [error] => E000
    [error_Message] => No Error
)
```

### QR

#### Sample response

```curl
curl -X \
 POST "https://test.payu.in/_payment" -H \
 "accept: application/json" -H \
 "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=ewP8oRopzdHEtC&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=QR&bankcode=UPIQR&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
```

#### Sample response

```
(
    [mihpayid] => 403993715524045752
    [mode] => QR
    [status] => success
    [unmappedstatus] => captured
    [key] => JPM7Fg
    [txnid] => ewP8oRopzdHEtC
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2021-09-06 13:27:08
    [productinfo] => iPhone
    [firstname] => Ashish
    [lastname] =>
    [address1] =>
    [address2] =>
    [city] =>
    [state] =>
    [country] =>
    [zipcode] =>
    [email] => test@gmail.com
    [phone] => 9876543210
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
    [hash] => 1be7e6e97ab1ea9034b9a107e7cf9718308aa9637b4dbbd1a3343c91b0da02b34a40d00ac7267ebe81c20ea1129b931371c555d565bc6e11f470c3d2cf69b5a3
    [field1] =>
    [field2] =>
    [field3] =>
    [field4] =>
    [field5] =>
    [field6] =>
    [field7] =>
    [field8] =>
    [field9] => Transaction Completed Successfully
    [payment_source] => payu
    [PG_TYPE] => QR-PG
    [bank_ref_num] => 87d3b2a1-5a60-4169-8692-649f61923b3d
    [bankcode] => UPIQR
    [error] => E000
    [error_Message] => No Error
)
```

<br />