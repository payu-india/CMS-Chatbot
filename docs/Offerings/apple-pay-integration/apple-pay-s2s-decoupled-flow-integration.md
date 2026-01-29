---
title: 'Apple Pay - S2S Decoupled Flow Integration '
deprecated: false
hidden: true
metadata:
  robots: index
---
This section provides comprehensive documentation for integrating Apple Pay with PayU's Server-to-Server (S2S) Decoupled Flow using `txn_s2s_flow=4`.

## Implementation Flow

### High-Level Flow Steps

1. **Initialize Payment**: Create payment session with Apple Pay token
2. **Prepare Request**: Build S2S Decoupled Flow request parameters
3. **Generate Hash**: Create SHA-512 hash for request authentication
4. **Submit Authorization**: Send initial authorization request
5. **Process Response**: Handle asynchronous response processing
6. **Verify Status**: Confirm payment status via verification APIs
7. **Complete Transaction**: Finalize payment based on business logic

## Step 1: Post the Payment Request

|            |                                                                                                    |
| :--------- | :------------------------------------------------------------------------------------------------- |
| Production | [https://secure.payu.in/AuthorizeTransaction.php](https://secure.payu.in/AuthorizeTransaction.php) |

### Request Parameters

| Parameter                        | Description                                       | Example                                                      |
| -------------------------------- | ------------------------------------------------- | ------------------------------------------------------------ |
| key<br />`mandatory`             | `string` PayU merchant key                        | "gtKFFx"                                                     |
| txnid<br />`mandatory`           | `string` Unique transaction ID                    | "APPLEPAY_DECOUP_1703845200"                                 |
| amount<br />`mandatory`          | `string` Transaction amount                       | "100.00"                                                     |
| productinfo<br />`mandatory`     | `string` Product description                      | "Apple Pay Decoupled Payment"                                |
| firstname<br />`mandatory`       | `string` Customer first name                      | "John"                                                       |
| email<br />`mandatory`           | `string` Customer email address                   | "[john@example.com](mailto:john@example.com)"                |
| mobile<br />`mandatory`          | `string` Customer mobile number                   | "9876543210"                                                 |
| txn_s2s_flow<br />`mandatory`    | `string` Set to "4" for Direct Authorization flow | "4"                                                          |
| pg<br />`mandatory`              | `string` Payment gateway identifier               | "APPLEPAY"                                                   |
| bankcode<br />`mandatory`        | `string` Bank/payment method code                 | "CCAP"                                                       |
| s2s_client_ip<br />`mandatory`   | `string` Client IP address                        | "192.168.1.1"                                                |
| s2s_device_info<br />`mandatory` | `string` Device information JSON                  | '\{"device_type":"web"}'                                     |
| hash<br />`mandatory`            | `string` SHA-512 request hash                     | "calculated_hash"                                            |
| surl<br />`mandatory`            | `string` Success URL                              | "[https://yourapp.com/success](https://yourapp.com/success)" |
| furl<br />`mandatory`            | `string` Failure URL                              | "[https://yourapp.com/failure](https://yourapp.com/failure)" |
| lastname<br />`optional`         | `string` Customer last name                       | "Doe"                                                        |
| address1<br />`optional`         | `string` Customer address line 1                  | "123 Main St"                                                |
| address2<br />`optional`         | `string` Customer address line 2                  | "Apt 4B"                                                     |
| city<br />`optional`             | `string` Customer city                            | "Mumbai"                                                     |
| state<br />`optional`            | `string` Customer state                           | "Maharashtra"                                                |
| country<br />`optional`          | `string` Customer country                         | "India"                                                      |
| zipcode<br />`optional`          | `string` Customer postal code                     | "400001"                                                     |
| udf1<br />`optional`             | `string` User defined field 1                     | "custom_value_1"                                             |
| udf2<br />`optional`             | `string` User defined field 2                     | "custom_value_2"                                             |
| udf3<br />`optional`             | `string` User defined field 3                     | "custom_value_3"                                             |
| udf4<br />`optional`             | `string` User defined field 4                     | "custom_value_4"                                             |
| udf5<br />`optional`             | `string` User defined field 5                     | "custom_value_5"                                             |
| phone<br />`optional`            | `string` Alternative phone number                 | "9876543211"                                                 |

### Sample Request

```curl
  curl --location \
   --request \
   POST 'https://secure.payu.in/_payment' --header 'Content-Type: application/x-www-form-urlencoded' \
   --header 'Cookie: PHPSESSID=mj185cifujktpv1igu9tmuoaal; PAYUID=6b0d4cbbe43702a8a938a4d4c546ae01; PHPSESSID=6388ab6306272' \
   --data \
  -urlencode 'hash=5e0f040fb08759d621caf04baab4bd893e1d9f5d3edfc2aa42bea00c2ac7140b14b7883028a3b7fc5df6fb728f7542d85c2930c3f3dc4bab6a8b3da1ff33d9fe' --data \
  -urlencode 'key=smsplus' --data \
  -urlencode 'txnid=payuTestTransaction8169502' --data \
  -urlencode 'amount=1.1' --data \
  -urlencode 'firstname=Postman' --data \
  -urlencode 'email=test@payu.in' --data \
  -urlencode 'phone=9988776655' --data \
  -urlencode 'productinfo=Product Info' --data \
  -urlencode 'surl=https://admin.payu.in/test_response' --data \
  -urlencode 'furl=https://admin.payu.in/test_response' --data \
  -urlencode 'notifyurl=https://admin.payu.in/test_response' --data \
  -urlencode 'codurl=https://admin.payu.in/test_response' --data \
  -urlencode 'ipurl=https://admin.payu.in/test_response' --data \
  -urlencode 'lastname=' --data \
  -urlencode 'udf1=' --data \
  -urlencode 'udf2=' --data \
  -urlencode 'udf3=' --data \
  -urlencode 'udf4=' --data \
  -urlencode 'udf5=' --data \
  -urlencode 'pg=APPLEPAY' --data \
  -urlencode 'bankcode=CCAP' --data \
  -urlencode 'txn_s2s_flow=4' --data \
  -urlencode 'auth_only=1' --data \
  -urlencode 'termUrl=https://admin.payu.in/test_response' --data \
  -urlencode 'authentication_flow=REDIRECT' 
```

<br />

## Step 2: Redirect the customer

Basis a successful response of the authentication API, you need to redirect the user to the bank page using **acsTemplate**.  This API specifies the response that is posted to `termUrl` after the authentication for the transaction has been processed.

> 📘 Notes:
>
> * All callbacks POST form data on the merchant's `termUrl` that is passed in Initiate Transaction API.
> * Validation of the response happens on the basis of the hash value being returned in the hash value of the response.

<Accordion title="Request parameters" icon="fa-code">
  <HTMLBlock>{`
                   <style>
                   /* Target only the second column in the table */
                   .markdown-body table td:nth-child(2) {
                     word-break: break-word !important;
                   }
                   
                   /* Keep the first column from breaking unnecessarily */
                   .markdown-body table td:nth-child(1) {
                     word-break: normal;
                     white-space: nowrap;
                   }
                   </style>
                   <table style="width: 100%; border-collapse: collapse;">
                   <thead>
                   <tr>
                     <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
                     <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
                   </tr>
                   </thead>
                   <tbody>
                   <tr>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p>rawBankData<br><code>mandatory</code></p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter contains the raw response that is received from bank after authentication. The response is urlencoded and in query string format.</p>
                   </td>
                   </tr>
                   <tr>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p>referenceId<br><code>mandatory</code></p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter contains the reference id being returned for the transaction</p>
                   </td>
                   </tr>
                   <tr>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p>bankData<br><code>mandatory</code></p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON</code> This parameter contains the JSON string that is to be used for authorization call.This parameter is received in case of successful OTP submission of decoupled transactions. The postToBank contains messageDigest and pares that is to be posted back for authorization. For more information on the fields in this JSON, refer to bankData <a href="#bankdata-json-fields-description">JSON Fields Description</a>.</p>
                   </td>
                   </tr>
                   <tr>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p>authenticationStatus<br><code>mandatory</code></p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter contains the authentication status of the transaction</p>
                   </td>
                   </tr>
                   <tr>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p>hash<br><code>mandatory</code></p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter contains the calculated hash of the data that is posted to the merchant. For security purpose it is recommended to validate the hash value before consuming the response. The hash calculation logic is:<br><code>sha512(authenticationStatus\|bankData\|rawBankData\|referenceId\|salt)</code></p>
                   </td>
                   </tr>
                   </tbody>
                   </table>
  `}</HTMLBlock>

  #### bankData JSON fields description

  <HTMLBlock>{`
                   <table style="width: 100%; border-collapse: collapse;">
                   <thead>
                   <tr>
                     <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
                     <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
                     <th style="border: 1px solid #ddd; padding: 8px;"><strong>Applicable for EMV 3DS</strong></th>
                   </tr>
                   </thead>
                   <tbody>
                   <tr>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p>cres<br><code>mandatory</code></p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field contains the Base64 encoded value received from ACS as part of the authentication response.</p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p>Yes</p>
                   </td>
                   </tr>
                   <tr>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p>referenceId<br><code>mandatory</code></p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field is returned in case of decoupled flow. This field contains the reference id for the transaction</p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
                   </td>
                   </tr>
                   <tr>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p>messageDigest<br><code>mandatory</code></p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field is returned in case of decoupled flow. This field contains the MD value being returned by the bank.</p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
                   </td>
                   </tr>
                   <tr>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p>pares<br><code>mandatory</code></p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field is returned in case of decoupled flow. This field contains the pares being returned by the bank</p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
                   </td>
                   </tr>
                   <tr>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p>additionalInfo<br><code>mandatory</code></p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field is returned in case of decoupled flow. This field contains the data that is being used for the gateways that do not return pares.</p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
                   </td>
                   </tr>
                   <tr>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p>authorizationUrl<br><code>mandatory</code></p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This integration document assumes that you have opt-ed out for the particular configuration.<br>The authorization URL in legacy integrations are present basis the config at PayU. Please reach out to <a href="mailto:integration@payu.in">integration@payu.in</a> to know more about.</p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"></td>
                   </tr>
                   </tbody>
                   </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Sample response" icon="fa-code">
  ```plaintext
  { 
      "rawBankData" : ""  
      "referenceId":  "00c44a4c8306f9cbe5ecf6133afe08a7" 
      "bankData" : { 
      "referenceId": "00c44a4c8306f9cbe5ecf6133afe08a7", 
      "messageDigest": "c2e9e456037f033e5cc3d7b6e556189adf41eeabf706844dff70aac91f6b8e73bb1846286c8f99ea768cf38f7c12369c|523727493647950f32684bd6f1ab07aa6474016f", 
      "pares": "eNrVmdeS47i2pl+lo8+loje968jOCHojGtGLvKM3opHoyacfZmZVde06PWfOzMXEjCIUgkBiYRHAWv8H4s0phyzj7CyZh+z9TcvGMSqy36r0r99jFAfhGIT/gLE8/QNNM/IPEiGoP5CUgGEwAjGCSH9/f7vRVjZ+NvgsnTVLNoxV371D/wL/Bb8B3/+exoekjLrp/S1KXoysv6MkQhHYG/Dt71ubDTL3DkMwhZIgRoIIAoL4G/BV/Qb83f42f5TG0+GtSt9Dp5gMTkMMGzxCLtm1mik1zkV02PzrDfi44y2NpuwdBuHTNgj9BiF/IsSfyOnbZ/3b88Mc3fbzaRuCwDfg54q3c2SGrEv2dwQ7nfnx7y3bnn2XnXecdn6U34C/fXtG3Tv40wcFQeK0fda+Off3t6lqf/YJ/RMi/4ShN+Cz/m2comme34M34FvpLYmW5Z2maYYVTJqWzadhJqu+0t8/57N+3vKWJdU7eA7rx+9nK7op+qGayvbD1X+veAM+XAE+p+79za6K7uxsyH7b2qYb//q9nKbnnwCwruu/VuRf/VAA8PkgAEgB5w3pWBX/8ftXqyyVu7z/32rGRl3fVUnUVEc0nQtEy6ayT3/74ds/mXGsD0sQYPHsH6epPxII7f74qAERCDttAv9s9Kcn++/08quzwxj9MZYR9NHBL4be36wszz5WRPaba8l//f4f36OAq4psnP5Puvve1c8WvtvzombO3mc3DXRwZEp92R+80+1LH1P8RNQ4/9f3dl93vgE//Pvm/NdM/TQiXzc6RMf6GG04qXdxrxgV1PAQ4FJa38tkuNT", 
      "additionalInfo": 
      { 
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
  }, 
      "authenticationStatus"  :  "success", 
      "hash" : "664b8ddd1b5b2d1b68abb7eee5ea6e001a02773499ddcd86956ba0833315e7d4e69c641d7b0b3e7590532e21e71936da173f4eda716fc09f83cd1117f0d0c37c"} 
  ```
</Accordion>

## Step 3: Authorize (charge) the payment

The authorization request is the final step of transaction processing. This again needs to be an S2S call from the merchant's server to PayU server.

<Accordion title="Request parameters" icon="fa-code">
  **Post URL**: The data to be posted has to be exactly the same as the JSON response received in the authentication response in [Step 2](#step-2-redirect-the-customer). The data must include the following parameters.

  #### Environment

  |            |                                                                                                    |
  | ---------- | -------------------------------------------------------------------------------------------------- |
  | Test       | [https://test.payu.in/AuthorizeTransaction.php](https://test.payu.in/AuthorizeTransaction.php)     |
  | Production | [https://secure.payu.in/AuthorizeTransaction.php](https://secure.payu.in/AuthorizeTransaction.php) |

  <HTMLBlock>{`
                   <style>
                   /* Target only the second column in the table */
                   .markdown-body table td:nth-child(2) {
                     word-break: break-word !important;
                   }
                   
                   /* Keep the first column from breaking unnecessarily */
                   .markdown-body table td:nth-child(1) {
                     word-break: normal;
                     white-space: nowrap;
                   }
                   </style>
                   <table style="width: 100%; border-collapse: collapse;">
                   <thead>
                   <tr>
                     <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
                     <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
                   </tr>
                   </thead>
                   <tbody>
                   <tr>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p>key<br><code>mandatory</code></p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The merchant key is provided by PayU and acts as a unique identifier for a specific merchant account in PayU's database.</p>
                   </td>
                   </tr>
                   <tr>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p>txnid<br><code>mandatory</code></p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The transaction ID is the order reference number generated by the merchant to track a particular order. It can be used only once and PayU's system does not accept a duplicate Transaction ID.</p>
                   </td>
                   </tr>
                   <tr>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p>amount<br><code>mandatory</code></p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> It should contain the payment amount of the particular transaction. The amount must be greater than Rs. 8000 for the cardless EMI option.</p>
                   </td>
                   </tr>
                   <tr>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p>hash<br><code>mandatory</code></p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> It is used to avoid the possibility of transaction tampering. The hash must in the following structure:<br> <code>valueOf(key)\| valueOf(txnid) \| valueOf(amount) \|valueOf(authentication_info) \| valueOf(salt)</code></p>
                   </td>
                   </tr>
                   <tr>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p>authentication_info<br><code>mandatory</code></p>
                   </td>
                     <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON</code> The JSON value received in the bankData on the Term URL or pass the fields as in the <a href="#example-for-authentication_info-json">JSON example</a>.</p>
                   </td>
                   </tr>
                   </tbody>
                   </table>
  `}</HTMLBlock>

  #### Example for authentication\_info JSON

  ```plaintext
  {
     "referenceId": "00c44a4c8306f9cbe5ecf6133afe08a7",
     "cres": "eyJhY3NUcmFuc0lEIjoiODc3OTFjZWUtMjUxNC00MzZjLWJlZDgtYTYzYTg3YmJkZjAxIiwiY2hhbGxlbmdlQ29tcGxldGlvbkluZCI6IlkiLCJtZXNzYWdlVHlwZSI6IkNSZXMiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMS4wIiwidGhyZWVEU1NlcnZlclRyYW5zSUQiOiJkNDFmNjIwMC0wNDM1LTQ5ZWUtYWExMS1mMzY2ZjA2NjFjNmYiLCJ0cmFuc1N0YXR1cyI6IlkifQ==",
     "messageDigest": "",
     "pares": "",
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
  | referenceId    | This field contains the same referenceId which sent in response of the first call                      |                           |
  | additionalInfo | This field can be used in the case of schemes where different parameters may need from merchant side.  |                           |
  | messageDigest  | This field includes the Base 64 encoding of (sha56 hash of the JSON data (post to server).             |                           |
  | pares          | This parameter contains the pares being returned by the bank.                                          |                           |
</Accordion>

## Step 4: Check the response from PayU

The response from PayU for Merchant Hosted and S2S integration is similar.

<ReverseHashing />

<Accordion title="Response parameters" icon="fa-code">
  The parameters in the response for similar for all S2S flows. For more information, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis#response-for-initial-server-to-server-request).
</Accordion>

<Accordion title="Sample response" icon="fa-code">
  The formatted JSON response is similar to the following:

  ```plaintext
  {
     "metaData": {
        "message": "No Error",
        "referenceId": "b6035f64240b1862295bc571952cf984",
        "statusCode": "E000",
        "txnId": "payuTestTransaction2746829",
        "unmappedStatus": "success",
        "submitOtp": {
           "status": "success"
        }
     },
     "result": {
        "mihpayid": "15270336226",
        "mode": "CC",
        "status": "success",
        "key": "4wvMqy",
        "txnid": "payuTestTransaction2746829",
        "amount": "1.10",
        "addedon": "2022-06-01 17:39:29",
        "productinfo": "Product Info",
        "firstname": "Postman",
        "lastname": "",
        "address1": "",
        "address2": "",
        "city": "",
        "state": "",
        "country": "",
        "zipcode": "",
        "email": "test@payu.in",
        "phone": "9988776655",
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
        "card_token": "",
        "card_no": "XXXXXXXXXXXX8006",
        "field0": "",
        "field1": "6540854745166970506094",
        "field2": "947167",
        "field3": "1.10",
        "field4": "15270336226",
        "field5": "100",
        "field6": "",
        "field7": "AUTHPOSITIVE",
        "field8": "",
        "field9": "Transaction is Successful",
        "payment_source": "payuPureS2SAuth",
        "PG_TYPE": "CC-PG",
        "error": "E000",
        "error_Message": "No Error",
        "cardToken": "",
        "net_amount_debit": "1.1",
        "discount": "0.00",
        "offer_key": "",
        "offer_availed": "",
        "unmappedstatus": "captured",
        "hash": "cdc409dfd15a842b8d15d6627d0027619882ed800773fa413cef491ae8ff2ef0cdfa654680ba4c8f3567313c6a6b00b94cb3bb5e16bad21d26be01216a69af41",
        "bank_ref_no": "6540854745166970506094",
        "bank_ref_num": "6540854745166970506094",
        "bankcode": "CC",
        "surl": "",
        "curl": "",
        "furl": "",
        "card_hash": "fdb59253e36daf8b3969525ae3799ccb4bb41993a5d2fcaf22737ec3ac8b90ab"
     }
  }
  ```
</Accordion>

## Step 5. Verify the payment

<Verify_Payment_Tabs />

<br />
