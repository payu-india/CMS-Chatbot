---
title: API Architecture
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU APIs are organized by **developer workflow and product capability**, not as a single monolithic REST surface. Understanding this architecture helps you pick the correct base URL, authentication model, request shape, and reference collection.

## Architectural Overview

PayU’s API surface has four common patterns:

| Pattern                        | Description                                                | Examples                                                  |
| :----------------------------- | :--------------------------------------------------------- | :-------------------------------------------------------- |
| **Collect Payment APIs**       | Create a payment or consent transaction                    | `_payment` (hosted, merchant-hosted, S2S), Payment Links  |
| **Command-based General APIs** | Server-to-server operations using `command` + `var1…var15` | Verify Payment, Refund, BIN Info, and transaction details |
| **OAuth resource APIs**        | Bearer/OAuth token against product hosts                   | Payouts and Partner onboarding                            |
| **Product-specific REST APIs** | Dedicated hosts and schemas per product                    | BBPS, Chargeback, Zion, Cross-border, and V2 payments     |

## Collect Payment APIs (`_payment`)

These API are built on `_payment` and used to collect payments. Below are built on this.

| Integration style        | Who hosts checkout UI  | Reference entry                                           |
| :----------------------- | :--------------------- | :-------------------------------------------------------- |
| PayU Hosted Checkout     | PayU                   | [PayU Hosted Checkout](ref:_payment_payu_hosted_checkout) |
| Merchant Hosted Checkout | Merchant               | [Merchant Hosted Checkout](ref:_payment_merchant_hosted)  |
| Server-to-Server         | Merchant orchestration | [S2S Collect Payment](ref:_payment_server_to_server)      |

### **Characteristics**

- **Base URL**
  <Tabs>
    <Tab title="Test" icon="🧪">
      `https://test.payu.in/_payment`
    </Tab>

    <Tab title="Production" icon="👨‍💻">
      `https://secure.payu.in/_payment`
    </Tab>
  </Tabs>
- **Authentication:** merchant `key` + SHA-512 `hash`
- **Request body:** form-urlencoded payment parameters (`txnid`, `amount`, `productinfo`, `surl`, `furl`, and more)
  ```curl cURL - Example Payload
  curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=JP***g" \
    -d "txnid=PQI6MqpYrjEefU" \
    -d "amount=10.00" \
    -d "firstname=PayU User" \
    -d "email=test@gmail.com" \
    -d "phone=9876543210" \
    -d "productinfo=iPhone" \
    -d "surl=https://apiplayground-response.herokuapp.com/" \
    -d "furl=https://apiplayground-response.herokuapp.com/" \
    -d "hash=HASH_VALUE"
  ```
- **Response:** The response can be redirect, callback, and/or S2S depending on the flow.
  ```json JSON - Example Payload
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

## General APIs

General APIs are server-to-server calls used **after** or **around** a payment such as verification, refunds, BIN checks, EMI eligibility, health checks, and similar operations.

### **Characteristics**

- **Base URL:**
  <Tabs>
    <Tab title="Test" icon="🧪">
      `https://test.payu.in/merchant/postservice.php?form=2`
    </Tab>

    <Tab title="Production" icon="👨‍💻">
      `https://info.payu.in/merchant/postservice.php?form=2`&#x20;
    </Tab>
  </Tabs>
- **Authentication:** `key` + `hash` where hash is usually `sha512(key|command|var1|salt)`
- **Request Body:** `key`, `command`, `hash`, `var1` to `var15`.
  ```curl cURL - Example Payload
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=JPM7Fg" \
    -d "command=verify_payment" \
    -d "var1=IhfgcZnXR4o4nB" \
    -d "hash=HASH_VALUE"
  ```
- **Response Body:** commonly includes `status`, `msg`, and command-specific fields such as `transaction_details`.
  ```json JSON - Example Payload
  {
    "status": 0,
    "msg": "0 out of 1 Transactions Fetched Successfully",
    "transaction_details": {
      "IhfgcZnXR4o4nB": {
        "mihpayid": "Not Found",
        "status": "Not Found"
      }
    }
  }
  ```

See [REST API Format](doc:rest-api-format) for the shared contract.

## OAuth and Partner Products

Some PayU products authenticate with OAuth rather than payment-hash logic:

| Product                 | Why OAuth                                                          | Entry points                                                                                                 |
| :---------------------- | :----------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| **Payouts**             | Disbursement APIs need scoped access tokens                        | [Payouts token API](ref:generate-token-using-merchants-credentials-api)                                      |
| **Partner integration** | Multi-merchant platforms need client credentials / auth code flows | [Partner Get Token](ref:get_token_api), [Partner API introduction](ref:partner-integration-api-introduction) |
| **Merchant onboarding** | KYC and account creation workflows                                 | [Partner Integration — Merchant Onboarding](ref:step-00-authentication)                                      |

## Versioning model

PayU versioning is **capability-driven**:

- Many Collect Payment enhancements are selected with an `api_version` request parameter.
- Some products expose path versions such as `/v2/payments`.
- Hash formulas can change when optional fields or versions are introduced.

Details: [API Versioning](doc:api-versioning).
