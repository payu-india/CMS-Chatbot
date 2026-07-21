---
title: Net Banking Integration - TPV with S2S
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Net Banking Integration - TPV with S2S
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Net Banking TPV Integration - Merchant Hosted Checkout
  description: >-
    Learn how to integrate Net Banking with Third Party Validation (TPV) using
    PayU's comprehensive guide. This documentation provides step-by-step
    instructions, API details, and best practices for seamless and secure
    payment processing. Enhance your online payment solutions with efficient net
    banking integration."
  keywords:
    - Net Banking Integration for TPV
    - ' Third Party Validation Net Banking Integration'
    - API Integration for NetBanking TPV
    - ' PayU NetBanking TPV Integration'
    - TPV Net Banking Setup Guide
  robots: index
next:
  description: ''
---
---
Integrate <Glossary>TPV</Glossary> through Net Banking using the procedure described in this section.

<br />

<Callout icon="👍" theme="okay">
  Experience the end-to-end **Merchant Hosted Checkout** > **Net Banking** flow and instantly generate the complete code for seamless, zero-coding integration into your website.

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

                                        <button onclick="window.open('https://payu.in/integrationlab/seamless/sm-nb-tpv', '_blank')" 
                                                class="tooltip-btn" 
                                                data-tooltip="Click here to see the Merchant Hosted Checkout > Net Banking > TPV end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">
                                            Experience the flow and get the code
                                        </button>
  `}</HTMLBlock>
</Callout>

**Steps to integrate**

<Cards columns={2}>
  <Card title="1. List Account Numbers" href="#step-1-list-the-account-numbers">
    Collect account numbers and check bank network health
  </Card>

  <Card title="2. Post Parameters" href="#step-2-post-the-parameters-to-payu">
    Post transaction request with beneficiary details to PayU
  </Card>

  <Card title="3. Authrentication Flow" href="#step-3-authrentication-flow">
    Authenticate the payment with the customer's bank
  </Card>

  <Card title="4. Authorize Payment" href="#step-4-authorize-charge-the-payment">
    Authorize and charge the authenticated payment
  </Card>

  <Card title="5. Check Response" href="#step-5-check-the-response-from-payu">
    Validate the response and reverse hash from PayU
  </Card>

  <Card title="6. Verify Payment" href="#step-6-verify-the-payment">
    Verify the payment using verify\_payment API
  </Card>
</Cards>

**Prerequisites**: Seamless integration has to be done as per the standard kit. For more information, refer to  <a href="https://docs.payu.in/reference/_payment-merchant-hosted" target="_blank">Collect Payments API</a>  under API Reference.

***

## Step 1: List the account numbers

Collect or prepare a list of account numbers that must be posted to PayU for TPV at step 2. You can use the **Get Net Banking Status** API to check the bank network health.

<Accordion title="Sample request" icon="fa-code">
  ```
  curl -X POST "https://test.payu.in/merchant/postservice?form=2"-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d"key=JP***g&command=getNetbankingStatus&var1=AXIB&hash=11f17a5b7b3a93bd0391a0447706ebebd37ab11d8ec8aff18e7d0ca6267f44d6b0b56c4bee6a8b8998acec1491be17047d43ad3ef1b4677bf2504f48d3e779ea"
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-code">
  ```plaintext
  {
        "ibibo_code": "AXIB",
        "title": "AXIS Bank NetBanking",
        "up_status": 0,
        "mode": "NB"
  }
  ```

  To get the status of all Net Banking options pass (value “**default**” is passed in input):

  ```
  {
        "AXIB": {
              "ibibo_code": "AXIB",
              "title": "AXIS Bank NetBanking",
              "up_status": 0,
              "mode": "NB"
        },
        "SBIB": {
              "ibibo_code": "SBIB",
              "title": "State Bank of India",
              "up_status": 1,
              "mode": "NB"
        },
        "TESTPGNB": {
              "ibibo_code": "TESTPGNB",
              "title": "Test Net Banking",
              "up_status": 1,
              "mode": "NB"
        },
        "UPI": {
              "ibibo_code": "UPI",
              "title": "Test UPI",
              "up_status": 1,
              "mode": "UPI"
        },
        "CASH": {
              "ibibo_code": "CASH",
              "title": "Test Wallet",
              "up_status": 1,
              "mode": "CASH"
        }
  }
  ```
</Accordion>

## Step 2: Post the parameters to PayU

With the following additional parameters, make the transaction request with the customer's bank account number to the PayU using the Collect Payment (**_payment**) API. For more information, refer to [Collect Payment API - Merchant Hosted Checkout](ref:_payment_merchant_hosted) .

<PaymentAPIEnvironment />

<Accordion title="Request parameters" icon="fa-table">
  <HTMLBlock>{`
                  <Table>
                    <thead>
                      <tr>
                        <th>
                          Parameter
                        </th>

                        <th>
                          Description
                        </th>

                        <th>
                          ypl938459435
                        </th>
                      </tr>
                    </thead>

                    <tbody>
                      <tr>
                        <td>
                          key <br/>
                          <code>mandatory</code>
                        </td>

                        <td>
                          <code>String</code> The merchant key provided by PayU while onboarding.
                        </td>

                        <td>

                        </td>
                      </tr>

                      <tr>
                        <td>
                          txnid <br/>
                          <code>mandatory</code>
                        </td>

                        <td>
                          <code>String</code> The transaction ID is a reference number for<br/> a specific order that is generated by the merchant.
                        </td>

                        <td>

                        </td>
                      </tr>

                      <tr>
                        <td>
                          amount <br/>
                          <code>mandatory</code>
                        </td>

                        <td>
                          <code>String</code> The payment amount for the transaction.
                        </td>

                        <td>
                          10.00
                        </td>
                      </tr>

                      <tr>
                        <td>
                          productinfo <br/>
                          <code>mandatory</code>
                        </td>

                        <td>
                          <code>String</code> A brief description of the product.
                        </td>

                        <td>
                          iPhone
                        </td>
                      </tr>

                      <tr>
                        <td>
                          firstname <br/>
                          <code>mandatory</code>
                        </td>

                        <td>
                          <code>String</code> The first name of the customer.
                        </td>

                        <td>
                          Ashish
                        </td>
                      </tr>

                      <tr>
                        <td>
                          email <br/>
                          <code>mandatory</code>
                        </td>

                        <td>
                          <code>String</code> The email address of the customer.
                        </td>

                        <td>
                          [abc@payu.in](mailto:abc@payu.in)
                        </td>
                      </tr>

                      <tr>
                        <td>
                          phone <br/>
                          <code>mandatory</code>
                        </td>

                        <td>
                          <code>String</code> The phone number of the customer.
                        </td>

                        <td>

                        </td>
                      </tr>

                      <tr>
                        <td>
                          <Glossary>pg</Glossary> <br/>
                          <code>mandatory</code>
                        </td>

                        <td>
                          <code>String</code> It defines the payment category for which<br/> you wish to perform TPV. For Net Banking, pg= 'NB'.
                        </td>

                        <td>
                          NB
                        </td>
                      </tr>

                      <tr>
                        <td>
                          <Glossary>bankcode</Glossary> <br/>
                          <code>mandatory</code>
                        </td>

                        <td>
                          <code>String</code> It defines the bank with which you wish<br/> to perform TPV using the bank code.<br/> For more information on the list of bank codes,<br/> refer to [Bank Codes for TPV](doc:bank-codes-for-tpv)
                        </td>

                        <td>
                          AXNBTPV, SBINBTPV, ICINBTPV
                        </td>
                      </tr>

                      <tr>
                        <td>
                          beneficiarydetail <br/>
                          <code>mandatory</code>
                        </td>

                        <td>
                          This is a JSON format text and there should be key<br/> named **beneficiaryAccountNumber** with the list of account numbers<br/> and the ifscCode key with the list of corresponding IFSC codes<br/> (in the same order as provided in the beneficiaryAccountNumber key).<br/> You can post up to five account details in this parameter.
                        </td>

                        <td>
                          Refer to  beneficiarydetail JSON Object Fields section below the table</a>
                        </td>
                      </tr>

                      <tr>
                        <td>
                          api_version <br/>
                          <code>optional</code>
                        </td>

                        <td>
                          The api_version "6" must be passed for this parameter.
                        </td>

                        <td>

                        </td>
                      </tr>

                      <tr>
                        <td>
                          furl <br/>
                          <code>mandatory</code>
                        </td>

                        <td>
                          <code>String</code> The success URL, which is the page<br/> PayU will redirect to if the transaction is successful.
                        </td>

                        <td>

                        </td>
                      </tr>

                      <tr>
                        <td>
                          surl <br/>
                          <code>mandatory</code>
                        </td>

                        <td>
                          <code>String</code> The Failure URL, which is the page PayU<br/> will redirect to if the transaction is failed.
                        </td>

                        <td>

                        </td>
                      </tr>

                      <tr>
                        <td>
                          hash <br/>
                          <code>mandatory</code>
                        </td>

                        <td>
                          <code>String</code> It is the hash calculated by the merchant.<br/> The hash calculation logic is:
                          <code>sha512(key|txnid|amount|productinfo|firstname|<br/>email|udf1|udf2|udf3|udf4|udf5|||||||<br/>beneficiarydetail|SALT)</code>
                        </td>

                        <td>

                        </td>
                      </tr>

                      <tr>
                        <td>
                          s2s_client_ip <br/>
                          <code>mandatory</code>
                        </td>

                        <td>
                          <code>String</code> This parameter must have the source IP of the customer.
                        </td>

                        <td>
                        </td>
                      </tr>

                      <tr>
                        <td>
                          s2s_device_info <br/>
                          <code>mandatory</code>
                        </td>

                        <td>
                          <code>String</code> This parameter must have the customer agent's device.
                        </td>

                        <td>
                        </td>
                      </tr>

                      <tr>
                        <td>
                          txn_s2s_flow <br/>
                          <code>mandatory</code>
                        </td>

                        <td>
                          <code>String</code> This parameter must be passed with the value as <strong>4</strong> for Legacy Decoupled flow.
                        </td>

                        <td>
                          4
                        </td>
                      </tr>

                      <tr>
                        <td>
                          address1 <br/>
                          <code>optional</code>
                        </td>

                        <td>
                          <code>String</code> The first line of the billing address.

                          * *For Fraud Detection*: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is required to provide the correct information.
                        </td>

                        <td>

                        </td>
                      </tr>

                      <tr>
                        <td>
                          address2 <br/>
                          <code>optional</code>
                        </td>

                        <td>
                          <code>String</code> The second line of the billing address.
                        </td>

                        <td>

                        </td>
                      </tr>

                      <tr>
                        <td>
                          city <br/>
                          <code>optional</code>
                        </td>

                        <td>
                          <code>String</code> The city where your customer resides as part of the billing address.
                        </td>

                        <td>

                        </td>
                      </tr>

                      <tr>
                        <td>
                          state <br/>
                          <code>optional</code>
                        </td>

                        <td>
                          <code>String</code> The state where your customer resides as part of the billing address.
                        </td>

                        <td>

                        </td>
                      </tr>

                      <tr>
                        <td>
                          country <br/>
                          <code>optional</code>
                        </td>

                        <td>
                          <code>String</code> The country where your customer resides.
                        </td>

                        <td>

                        </td>
                      </tr>

                      <tr>
                        <td>
                          zipcode <br/>
                          <code>optional</code>
                        </td>

                        <td>
                          <code>String</code> Billing address zip code is mandatory for the cardless EMI option.<br/>
                          <code>Character Limit</code>-20
                        </td>

                        <td>

                        </td>
                      </tr>

                      <tr>
                        <td>
                          udf1 <br/>
                          <code>optional</code>
                        </td>

                        <td>
                          <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.
                        </td>

                        <td>

                        </td>
                      </tr>

                      <tr>
                        <td>
                          udf2 <br/>
                          <code>optional</code>
                        </td>

                        <td>
                          <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.
                        </td>

                        <td>

                        </td>
                      </tr>

                      <tr>
                        <td>
                          udf3 <br/>
                          <code>optional</code>
                        </td>

                        <td>
                          <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.
                        </td>

                        <td>

                        </td>
                      </tr>

                      <tr>
                        <td>
                          udf4 <br/>
                          <code>optional</code>
                        </td>

                        <td>
                          <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.
                        </td>

                        <td>

                        </td>
                      </tr>

                      <tr>
                        <td>
                          udf5 <br/>
                          <code>optional</code>
                        </td>

                        <td>
                          <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.
                        </td>

                        <td>

                        </td>
                      </tr>
                    </tbody>
                  </Table>
  `}</HTMLBlock>

  <Accordion title="beneficiarydetail JSON Object Fields" icon="fa-code">
    It must contain the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key). You can post up to five account details in this parameter. For example:

    ```
    {"beneficiaryAccountNumber":"002001600674|00000031957292212|00000035955239352|00000035955239352",  
    "ifscCode":"KTKB0000046|KTKB0000023|KTKB0000035|KTKB0000035"}
    ```
  </Accordion>

  <Accordion title="Checksum logic for Hash)" icon="fa-code">
    The following hash logic must be used for the parameters posted:

    > 📘 beneficiarydetail parameter in hashing:
    >
    > The **beneficiarydetail** parameter value will be at last or the last value to be appended.
    >
    > ```plaintext
    > key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3
    > |udf4|udf5||||||beneficiarydetail|SALT
    > ```
  </Accordion>
</Accordion>

## Step 3: Authrentication Flow

On basis of a successful response of the Collect Payment (**\_payment**) API, you need to redirect the user to the bank page using **acsTemplate**. In case of Bank page authentication (Non-Native OTP), ACS server will redirect the customer to termUrl passed in the payment request during initiation and authenticationResult will be posted along "cres" over the termUrl.

> 📘 Notes:
>
> - All callbacks POST form data on the merchant's `termUrl` that is passed in Initiate Transaction API.
> - Validation of the response happens on the basis of the hash value being returned in the hash value of the response.

<Accordion title="Response parameters over termURL" icon="fa-table">
  | Parameter                                        | Description | Example |
  | ------------------------------------------------ | ----------- | ------- |
  | rawBankData<br /><code>mandatory</code>          | <code>String</code> This parameter contains the raw response that is received from bank after authentication. The response is urlencoded and in query string format. | bankRespId=123\&status=success\&amount=1000 |
  | referenceId<br /><code>mandatory</code>          | <code>String</code> This parameter contains the reference id being returned for the transaction. | TXN\_REF\_123456789 |
  | bankData<br /><code>mandatory</code>             | <code>JSON</code> This parameter contains the JSON string that is to be used for authorization call. This parameter is received in case of successful OTP submission of decoupled transactions. The postToBank contains messageDigest and pares that is to be posted back for authorization. For more information on the fields in this JSON, refer to [bankData JSON Fields Description](#bankdata-json-fields-description). | |
  | authenticationStatus<br /><code>mandatory</code> | <code>String</code> This parameter contains the authentication status of the transaction. | SUCCESS |
  | hash<br /><code>mandatory</code>                 | <code>String</code> This parameter contains the calculated hash of the data that is posted to the merchant. For security purpose it is recommended to validate the hash value before consuming the response. The hash calculation logic is: <code>sha512(authenticationStatus\\\|bankData\\\|rawBankData\\\|referenceId\\\|salt)</code> | 5d41402abc4b2a76b9719d911017c592b2d4c3ef45d0b9e1c9b5a7b2c8f9e0d3 |
</Accordion>

<Accordion title="bankData JSON fields description" icon="fa-table">
  #### bankData JSON Fields Description

  | Field                                        | Description | Applicable for EMV 3DS |
  | -------------------------------------------- | ----------- | ---------------------- |
  | cres<br /><code>mandatory</code>             | This field contains the Base64 encoded value received from ACS as part of the authentication response. <code>String</code> | Yes |
  | referenceId<br /><code>mandatory</code>      | This field is returned in case of decoupled flow. This field contains the reference id for the transaction. <code>String</code> | REF\_12345 |
  | messageDigest<br /><code>mandatory</code>    | This field is returned in case of decoupled flow. This field contains the MD value being returned by the bank. <code>String</code> | d41d8cd98f00b204e9800998ecf8427e |
  | pares<br /><code>mandatory</code>            | This field is returned in case of decoupled flow. This field contains the pares being returned by the bank. <code>String</code> | eJyrVkosLcmIz8nPS1WyUorPTFGyMjJQUkoD8ZNrAQytCFn |
  | additionalInfo<br /><code>mandatory</code>   | This field is returned in case of decoupled flow. This field contains the data that is being used for the gateways that do not return pares. <code>String</code> | transaction\_id=12345\&status=pending |
  | authorizationUrl<br /><code>mandatory</code> | This integration document assumes that you have opted out for the particular configuration. The authorization URL in legacy integrations is present based on the configuration at PayU. Contact your PayU Key Account Manager (KAM) to know more. <code>String</code> | [https://secure.payu.in/merchant/postservice?form=5ea3a2d](https://secure.payu.in/merchant/postservice?form=5ea3a2d) |
</Accordion>

## Step 4: Authorize (charge) the payment

The authorization request is the final step of transaction processing. This again needs to be an S2S call from the merchant's server to PayU server.

> 📘
>
> **Note:**
>
> - **For Redirection Based authentication from termUrl (if being sent by PayU)**: If `authenticationStatus=success`, use the `bankData` parameter value as it is under the **authentication\_info** parameter of the **Authorize Transaction API**.
> - **For Native OTP based Authentication**: If **metaData.txnStatus** is "Authenticated", use the `result.postToBank` object value in the authentication\_info parameter of the **Authorize Transaction API**.

#### Environment

|            |                                                                                                    |
| ---------- | -------------------------------------------------------------------------------------------------- |
| Test       | [https://test.payu.in/AuthorizeTransaction.php](https://test.payu.in/AuthorizeTransaction.php)     |
| Production | [https://secure.payu.in/AuthorizeTransaction.php](https://secure.payu.in/AuthorizeTransaction.php) |

<Accordion title="Request parameters" icon="fa-code">
  **Post URL**: The data to be posted has to be exactly the same as the JSON response received in the authentication response in [Step 3](#step-3-authrentication-flow). The data must include the following parameters.

  | Parameter                                        | Description | Example |
  | ------------------------------------------------ | ----------- | ------- |
  | key<br /><code>mandatory</code>                  | The merchant key is provided by PayU and acts as a unique identifier for a specific merchant account in PayU's database. <code>String</code> | gtKFFx |
  | txnid<br /><code>mandatory</code>                | The transaction ID is the order reference number generated by the merchant to track a particular order. It can be used only once and PayU's system does not accept a duplicate Transaction ID. <code>String</code> | ORD\_123456789 |
  | amount<br /><code>mandatory</code>               | It should contain the payment amount of the particular transaction. The amount must be greater than Rs. 8000 for the cardless EMI option. <code>String</code> | 10000.00 |
  | hash<br /><code>mandatory</code>                 | It is used to avoid the possibility of transaction tampering. The hash must be in the following structure: <code>valueOf(key)\\\|valueOf(txnid)\\\|valueOf(amount)\\\|valueOf(authentication\_info)\\\|valueOf(salt)</code> <code>String</code> | 3af7c2b8e6f9d4e1a9b7c5e2f8d3a6b9e1c4f7a2d5e8b1c3f6a9d2e5b8c1a4f7 |
  | authentication\_info<br /><code>mandatory</code> | The JSON value received in the bankData on the Term URL, or pass the fields as in the JSON example. <code>JSON</code> | |

  #### Example for authentication\_info JSON

  ```json
  {
    "referenceId": "4b6dcb255093a92dc38599b82ac0f796619410e322a2b68ba69a6c7aa5dfb78d",
    "cres": "eyJtZXNzYWdlVHlwZSI6IkNSZXMiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIiwidGhyZWVEU1NlcnZlclRyYW5zSUQiOiIxMDY3ZjkyNi00YTJjLTE2MGMtOWU0ZS1lZmIxNjBiNjkwMGYiLCJUcmFuc2FjdGlvbklkIjoiNWU4NDE4ZDYtMWI4Ny01NzVhLWJkMzUtYjRkOWU0NjUiLCJjcmVzIjoiZXlKMGFISmxaVVJUVTJWeWRtVnlWSEpoYm5OSlJDSTZJakV3TmpkbU9USTJMVFJoTW1NdE1UWXdZeTA1WlRSbExXVm1ZakUyTUdJMk9UQXdaaUlzSW1GamMxUnlZVzV6U1VRaU9pSm1Zems1WkdJNU1pMWhOVGczTFRNek5qUXRNRFEzTXkxaE1HUTVPR1kwTnpReFptTWlMQ0p0WlhOellXZGxWSGx3WlNJNklrTlNaWE1pTENKdFpYTnpZV2RsVm1WeWMybHZiaUk2SWpJdU1pNHdJaXdpWTJoaGJHeGxibWRsUTI5dGNHeGxkR2x2YmtsdVpDSTZJbGtpTENKMGNtRnVjMU4wWVhSMWN5STZJbGtpTENKbFkya2lPaUl3TWlKOSJ9",
    "additionalInfo": {
      "authUdf1": "",
      "authUdf2": "",
      "authUdf3": "",
      "authUdf4": "",
      "authUdf5": "",
      "authUdf6": "",
      "authUdf7": "",
      "authUdf8": "",
      "authUdf9": "",
      "authUdf10": ""
    }
  }
  ```

  #### authentication\_info JSON Fields Description

  | **Field**      | **Description**                                                                                        | **Applicable to EMV 3DS** |
  | -------------- | ------------------------------------------------------------------------------------------------------ | ------------------------- |
  | cres           | This field contains the Base 64 encoded value received from ACS as part of the authentication response | Yes                       |
  | referenceId    | This field contains the same referenceId which was sent in response to the first call                   |                           |
  | additionalInfo | This field can be used in the case of schemes where different parameters may be needed from the merchant side. |                    |
  | messageDigest  | This field includes the Base 64 encoding of the SHA-256 hash of the JSON data posted to the server.     |                           |
  | pares          | This parameter contains the pares being returned by the bank.                                           |                           |
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```
  curl POST 'https://test.payu.in/AuthorizeTransaction' \
    --header 'Cookie: PHPSESSID=ca4slgf2hlcc3a80tauvnh96cr; PHPSESSID=69c3e6c6a9ee8' \
    --form 'key=PRiQvJ' \
    --form 'txnid=my_order_75942' \
    --form 'amount=2' \
    --form 'authentication_info={
      "referenceId": "4b6dcb255093a92dc38599b82ac0f796619410e322a2b68ba69a6c7aa5dfb78d",
      "cres": "eyJtZXNzYWdlVHlwZSI6IkNSZXMiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIiwidGhyZWVEU1NlcnZlclRyYW5zSUQiOiIxMDY3ZjkyNi00YTJjLTE2MGMtOWU0ZS1lZmIxNjBiNjkwMGYiLCJUcmFuc2FjdGlvbklkIjoiNWU4NDE4ZDYtMWI4Ny01NzVhLWJkMzUtYjRkOWU0NjUiLCJjcmVzIjoiZXlKMGFISmxaVVJUVTJWeWRtVnlWSEpoYm5OSlJDSTZJakV3TmpkbU9USTJMVFJoTW1NdE1UWXdZeTA1WlRSbExXVm1ZakUyTUdJMk9UQXdaaUlzSW1GamMxUnlZVzV6U1VRaU9pSm1Zems1WkdJNU1pMWhOVGczTFRNek5qUXRNRFEzTXkxaE1HUTVPR1kwTnpReFptTWlMQ0p0WlhOellXZGxWSGx3WlNJNklrTlNaWE1pTENKdFpYTnpZV2RsVm1WeWMybHZiaUk2SWpJdU1pNHdJaXdpWTJoaGJHeGxibWRsUTI5dGNHeGxkR2x2YmtsdVpDSTZJbGtpTENKMGNtRnVjMU4wWVhSMWN5STZJbGtpTENKbFkya2lPaUl3TWlKOSJ9",
      "additionalInfo": {
        "authUdf1": "",
        "authUdf2": "",
        "authUdf3": "",
        "authUdf4": "",
        "authUdf5": "",
        "authUdf6": "",
        "authUdf7": "",
        "authUdf8": "",
        "authUdf9": "",
        "authUdf10": ""
      }
    }'
  ```
</Accordion>

## Step 5: Check the response from PayU

<Accordion title="Hash Validation Logic for Payment Response (Reverse Hashing)" icon="fa-code">
  While sending the response, PayU takes the exact same parameters that were sent in the request (in reverse order) to calculate the hash and returns it to you. You must verify the hash and then mark a transaction as a success or failure. This is to make sure the transaction has not tampered within the response.

  The order of the parameters is similar to the following:

  ```
  sha512(SALT|status||||||||udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  > 📘 beneficiarydetail parameter not required in reverse hashing:
  >
  > The **beneficiarydetail** parameter should not be present in reverse hashing and order of parameters is similar to the following:
  >
  > ```
  > sha512(SALT|status||||||||udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  > ```
</Accordion>

<Accordion title="Response Parameters" icon="fa-code">
  The following table describes the parameters in the response from PayU:

  | **Param Name**   | **Description**                                                                                                                                                                                                                                                                                                          |
  | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | mihpayid         | It is a unique reference number created for each transaction at PayU's end. You must note this transaction ID as this will be used as a reference for all the future actions on this transaction like Inquiry or Refund.                                                                                                 |
  | merchantid       | It is the unique ID of the merchant.                                                                                                                                                                                                                                                                                     |
  | txnid            | This parameter would contain the transaction ID value posted by the merchant during the transaction request.                                                                                                                                                                                                             |
  | transaction\_fee | The transaction fee for the TPV transaction. For Net Banking, INR 10 is charged by default.                                                                                                                                                                                                                              |
  | discount         | The discount amount given by bank on the transaction fee (if any).                                                                                                                                                                                                                                                       |
  | amount           | The net amount after discount (if any) is displayed in this parameter. For Net Banking, INR 10 is charged by default.                                                                                                                                                                                                    |
  | paymentgatewayid | The payment gateway identifier for the bank sending the response.                                                                                                                                                                                                                                                        |
  | pg               | The payment gateway used for the transaction. In case of Net Banking, it is "NB."                                                                                                                                                                                                                                        |
  | status           | This parameter gives the status of the transaction as either success, failed or pending. Possible values: success, failure, pending If the value of the 'status' parameter is 'success', the transaction is successful. If the value of 'status' is 'failure' or 'pending', must be treated as a failed transaction only |
  | PG\_Type         | The bankcode (as in Merchant Hosted Checkout integration) of the bank is returned in the parameter.                                                                                                                                                                                                                      |
  | key              | This parameter contains the merchant key for the merchant's account at PayU. It would be the same as the key used while the transaction request is being posted from the merchant's end to PayU.                                                                                                                         |
  | riskactionStr    | This parameter contains risk action (if any) taken on the account holder.                                                                                                                                                                                                                                                |
  | addedon          | The transaction timestamp is returned in this parameter.                                                                                                                                                                                                                                                                 |

  > 📘 Store the mihpayid and txnid parameter values in response:
  >
  > PayU recommends you to make provisions to store the **mihpayid** and **txnid** parameter values (in the response) in your server as proof that TPV has been completed for a customer.
</Accordion>

<Accordion title="Sample response" icon="fa-code">
  Formatted response:

  ```
  Array
  (
      [mihpayid] => 403993715524308236
      [mode] => NB
      [status] => success
      [unmappedstatus] => captured
      [key] => JP***g
      [txnid] => TtEmKjWF2uGliF
      [amount] => 10.00
      [discount] => 0.00
      [net_amount_debit] => 10
      [addedon] => 2021-10-05 12:44:06
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
      [hash] => 74d1039311528b4a7b699db7ce195d6a219d7442271dedb23e516e29490ec743a89c12448698178907e03d32fa05e8178694db8037bc0be53380099e47c3d63f
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
      [PG_TYPE] => NB-PG
      [bank_ref_num] => 30646df4-69b7-43f4-acdd-21e6a593c037
      [bankcode] => TESTPGNB
      [error] => E000
      [error_Message] => No Error
  )
  ```
</Accordion>

## Step 6. Verify the payment

<Verify_Payment_Tabs />