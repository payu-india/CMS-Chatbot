---
title: eNACH Supported Banks and Verification Modes
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Recurring Payments Bank Codes
  description: >-
    Explore the comprehensive list of bank codes required for Net Banking and
    Debit Card recurring payment registrations. Stay updated with the latest
    supported banks and their specific codes for seamless transaction processing
  keywords:
    - ENACH Registration Bank Code
    - ENACH Registration BankCode
    - Consent Registration bankcode
    - Recurring Payments Bank Code
    - Subscription Bank Code
    - Recurring Payments bankcode
    - Subscription bankcode
    - Zion Platform bankcode
    - Zion Platform bank code
  robots: index
next:
  description: ''
---
This page provides the list of supported bank codes required for eNACH mandate registration. It also helps you identify the verification modes supported by each bank, including NetBanking, Debit Card, and Aadhaar-based authentication. Below are the available APIs:

- Use the [Get Enabled Banks API](https://docs.payu.in/docs/bank-codes-recurring-payments#get-enabled-banks) to retrieve the list of supported banks along with their consent transaction and TPV bank codes.
- Use the [Get Verification Methods for a Bank API](https://docs.payu.in/docs/bank-codes-recurring-payments#get-verification-modes-for-a-bank) to check the verification methods supported by a specific bank before initiating mandate registration flows.

> ⚠️ **Watch Out!**
>
> These APIs return only the banks enabled for the merchant. For example, if NPCI supports 300 banks and the merchant has enabled only 280 banks, the APIs return details of only those 280 enabled banks.

# Get Enabled Banks

Use this API to fetch a list of eNACH enabled banks. This API returns all supported banks for the merchant.

<Cards>
  <Card title="Method">
    GET
  </Card>

  <Card title="Endpoint">
    /enach/bank-supported-verification-modes?merchant_id=134220
  </Card>
</Cards>

## Environment

|                            |                                                |
| -------------------------- | ---------------------------------------------- |
| **Test Environment**       | [`https://test.payu.in`](https://test.payu.in) |
| **Production Environment** | [`https://info.payu.in`](https://info.payu.in) |

### Sample Request

<Accordion title="Request Payload" icon="fa-code">
  ```curl
  curl --location -g --request GET \
  'https://subscription_service/api/v1/enach/bank-supported-verification-modes?merchant_id=MERCHANT_ID' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer `{access_token}`'
  ```
</Accordion>

### Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Success Response
  {
  "status":"SUCCESS",
  "code":null,
  "message":"ENACH-enabled banks fetched successfully",
  "data":[
    {
      "bankCode":"BURX",
      "bankName":"THE BURDWAN CENTRAL CO OP BANK LTD",
      "netBankingSupported":false,
      "debitCardSupported":false,
      "aadhaarSupported":true
    },
    {
      "bankCode":"KRDX",
      "bankName":"THE KRISHNA DISTRICT CO OP BANK",
      "netBankingSupported":false,
      "debitCardSupported":true,
      "aadhaarSupported":true
    },
    {
      "bankCode":"DGBX",
      "bankName":"TELANGANA GRAMEENA BANK",
      "netBankingSupported":false,
      "debitCardSupported":true,
      "aadhaarSupported":true
    },
    {
      "bankCode":"KUKX",
      "bankName":"THE KUKARWADA NAGARIK SAHAKARI BANK LTD",
      "netBankingSupported":false,
      "debitCardSupported":false,
      "aadhaarSupported":true
    },
    {
      "bankCode":"AKOX",
      "bankName":"THE AKOLA URBAN CO OP BANK LTD",
      "netBankingSupported":true,
      "debitCardSupported":false,
      "aadhaarSupported":true
    },
    {
      "bankCode":"KCCB",
      "bankName":"THE KALUPUR COMMERCIAL CO OP BANK",
      "netBankingSupported":true,
      "debitCardSupported":true,
      "aadhaarSupported":true
    },
    {
      "bankCode":"IUCB",
      "bankName":"INTEGRAL URBAN CO OP BANK LTD",
      "netBankingSupported":false,
      "debitCardSupported":true,
      "aadhaarSupported":false
    },
    {
      "bankCode":"JSFB",
      "bankName":"JANA SMALL FINANCE BANK LTD",
      "netBankingSupported":true,
      "debitCardSupported":true,
      "aadhaarSupported":true
    },
    {
      "bankCode":"CGBX",
      "bankName":"CHHATTISGARH GRAMIN BANK",
      "netBankingSupported":false,
      "debitCardSupported":true,
      "aadhaarSupported":true
    },
    {
      "bankCode":"BRMX",
      "bankName":"BRAMHAPURI URBAN CO OP BANK LTD",
      "netBankingSupported":false,
      "debitCardSupported":false,
      "aadhaarSupported":true
    },
    {
      "bankCode":"NGSB",
      "bankName":"NAGPUR NAGARIK SAHAKARI BANK LTD",
      "netBankingSupported":false,
      "debitCardSupported":false,
      "aadhaarSupported":true
    },
    {
      "bankCode":"HPSX",
      "bankName":"THE HIMACHAL PRADESH STATE CO OP BANK LTD",
      "netBankingSupported":false,
      "debitCardSupported":false,
      "aadhaarSupported":true
    },
    {
      "bankCode":"MGBX",
      "bankName":"MAHARASHTRA GRAMIN BANK",
      "netBankingSupported":false,
      "debitCardSupported":true,
      "aadhaarSupported":true
    },
    {
      "bankCode":"HSBC",
      "bankName":"THE HONGKONG AND SHANGHAI BANKING CORPORATION LTD",
      "netBankingSupported":true,
      "debitCardSupported":false,
      "aadhaarSupported":false
    },
    {
      "bankCode":"PSIB",
      "bankName":"PUNJAB AND SIND BANK",
      "netBankingSupported":true,
      "debitCardSupported":true,
      "aadhaarSupported":true
    },
    {
      "bankCode":"SCBL",
      "bankName":"STANDARD CHARTERED BANK",
      "netBankingSupported":true,
      "debitCardSupported":true,
      "aadhaarSupported":false
    },
    {
      "bankCode":"UCUX",
      "bankName":"UNIVERSAL CO OP URBAN BANK LTD",
      "netBankingSupported":false,
      "debitCardSupported":false,
      "aadhaarSupported":true
    },
    {
      "bankCode":"ESAF",
      "bankName":"ESAF SMALL FINANCE BANK LTD",
      "netBankingSupported":true,
      "debitCardSupported":true,
      "aadhaarSupported":true
    },
    {
      "bankCode":"MDGX",
      "bankName":"RAJASTHAN GRAMIN BANK",
      "netBankingSupported":false,
      "debitCardSupported":true,
      "aadhaarSupported":true
    },
    {
      "bankCode":"ESFB",
      "bankName":"EQUITAS SMALL FINANCE BANK LTD",
      "netBankingSupported":true,
      "debitCardSupported":true,
      "aadhaarSupported":true
    },
    {
      "bankCode":"CNRB",
      "bankName":"CANARA BANK",
      "netBankingSupported":true,
      "debitCardSupported":true,
      "aadhaarSupported":true
    },
    {
      "bankCode":"KAYX",
      "bankName":"THE KANYAKUMARI DISTRICT CENTRAL CO OP BANK",
      "netBankingSupported":false,
      "debitCardSupported":false,
      "aadhaarSupported":true
    },
    {
      "bankCode":"DCKX",
      "bankName":"THE DISTRICT CO OP CENTRAL BANK LTD KURNOOL",
      "netBankingSupported":false,
      "debitCardSupported":false,
      "aadhaarSupported":true
    }
  ]
}
```
</Accordion>

### Query Parameter

> 📘 **Mandatory Parameters**
>
> <RequiredStar legend />

| **Parameter**                        | **Description**                                                                                        |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| <RequiredStar param="merchant_id" /> | `string` The unique merchant ID for which the supported bank list to be fetched. For example `134220`. |

### Response Parameters

| **Parameter** | **Description**                                                                                                                                                                 |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `status`      | `string` The status of the API. Possible values:<br /><ul><li>`SUCCESS`: The API fetched the list successfully.</li> <li>`FAILED`: The API could not fetch the list.</li></ul>  |
| `code`        | `string` The error code.                                                                                                                                                        |
| `message`     | `string` The response message.                                                                                                                                                  |
| `data`        | `array` The list of banks and details. Parameters are described in the [`data` Object](https://docs.payu.in/docs/bank-codes-recurring-payments#data-object-parameters) section. |

#### `data` Object Parameters

<Accordion title="Parameters and Description" icon="fa-table">
| **Parameter**         | **Description**                                                           |
| --------------------- | ------------------------------------------------------------------------- |
| `bankCode`            | `string` The unique bank identifier.                                      |
| `bankName`            | `string` The bank name.                                                   |
| `netBankingSupported` | `boolean` Determines whether the NetBanking verification is supported.    |
| `debitCardSupported`  | `boolean` Determines whether the debit card verification is supported.    |
| `aadhaarSupported`    | `boolean` Determines whether the Aadhaar-based verification is supported. |

</Accordion>

## Get Verification Methods for a Bank

Use this API to fetch supported verification modes for a specific bank.

<Cards>
  <Card title="Method">
    GET
  </Card>

  <Card title="Endpoint">
    /enach/bank-supported-verification-modes
  </Card>
</Cards>

### Sample Request

<Accordion title="Request Payload" icon="fa-code">
  ```curl
  curl --location -g --request GET \
  'https://subscription_service/api/v1/enach/bank-supported-verification-modes?merchant_id=134220&bank_code=HDFC' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer `{access_token}`'
  ```
</Accordion>

### Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Success Response
  {
  "status":"SUCCESS",
  "code":null,
  "message":"Verification mode fetched successfully",
  "data":{
    "bankCode":"HDFC",
    "bankName":"HDFC BANK LTD",
    "netBankingSupported":true,
    "debitCardSupported":true,
    "aadhaarSupported":true
    }
  }
  ```
  ```json Error Response
  {
  "status":"FAILED",
  "code":"BANK_NOT_FOUND",
  "message":"No ENACH-enabled bank found for code: EFGH",
  "data":null
  }
  ```
</Accordion>

### Query Parameters

> 📘 **Mandatory Parameters**
>
> <RequiredStar legend />

| **Parameters**                       | **Description**                                                     |
| ------------------------------------ | ------------------------------------------------------------------- |
| <RequiredStar param="merchant_id" /> | `number` A unique identifier of the merchant. For example `134220`. |
| <RequiredStar param="bank_code" />   | `string` The bank code. For example `HDFC`.                         |

### Response Parameters

| **Parameters** | **Description**                                                                                                                                                                   |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `status`       | `string` The status of the API. Possible values:<br /> <ul><li>`SUCCESS`: The API fetched the list successfully.</li> <li>`FAILED`: The API could not fetch the list. </li></ul>  |
| `code`         | `string` The error code.                                                                                                                                                          |
| `message`      | `string` The response message.                                                                                                                                                    |
| `data`         | `array` The list of banks and details. Parameters are described in the [`data` Object](https://docs.payu.in/docs/bank-codes-recurring-payments#data-object-parameters-1) section. |

#### `data` Object Parameters

<Accordion title="Parameters and Description" icon="fa-table">
| **Parameter**         | **Description**                                                           |
| --------------------- | ------------------------------------------------------------------------- |
| `bankCode`            | `string` The unique bank identifier.                                      |
| `bankName`            | `string` The bank name.                                                   |
| `netBankingSupported` | `boolean` Determines whether the NetBanking verification is supported.    |
| `debitCardSupported`  | `boolean` Determines whether the debit card verification is supported.    |
| `aadhaarSupported`    | `boolean` Determines whether the Aadhaar-based verification is supported. |
</Accordion>

<br />
