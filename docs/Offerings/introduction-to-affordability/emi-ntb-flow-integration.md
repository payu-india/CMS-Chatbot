---
title: EMI - NTB Flow Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
This section how to integrate New to Bank (NTB) flow using PayU’s **Get Checkout Details (NTB Seamless Journey)** and **Get EMI Checkout Details** APIs. Use these in order when building custom checkout pages that need payment options, EMI details, and customer eligibility.

### Flow overview

1. **Step 1** – Call Get Checkout Details to fetch payment options, offers, downtime, and (optionally) high-level eligibility for your transaction.
2. **Step 2** – Call Get EMI Checkout Details with customer and bank/lender details to get EMI tenure options and detailed eligibility (e.g. for cardless EMI / Link and Pay NTB).

***

## Step 1: Get Checkout Details

Use the **Get Checkout Details** API (`get_checkout_details`) to get information for custom checkout pages: payment options, extended payment details (e.g. EMI breakup), additional charges, tax specification, downtime, and optional customer eligibility.

| Environment | URL                                                    |
| :---------- | :----------------------------------------------------- |
| Test        | `https://test.payu.in/merchant/postservice.php?form=2` |
| Production  | `https://info.payu.in/merchant/postservice.php?form=2` |

**Method:** POST (form-encoded)

<Accordion title="Request parameters" icon="fa-list">

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
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key  <br/>  `mandatory`
      </td>

      <td>
        <code>String</code> Merchant key provided by PayU.
      </td>

      <td>
        JPM7Fg
      </td>
    </tr>

    <tr>
      <td>
        command<br/>  `mandatory`
      </td>

      <td>
        <code>String</code> Must be <code>get_checkout_details</code> (name of the web-service).
      </td>

      <td>
        get_checkout_details
      </td>
    </tr>

    <tr>
      <td>
        var1<br/>  `mandatory`
      </td>

      <td>
        <code>String</code> JSON string containing requestId, transactionDetails, useCase, and optionally customerDetails and filters. See var1 JSON fields below.
      </td>

      <td>
        See
      </td>
    </tr>

    <tr>
      <td>
        hash<br/>  `mandatory`
      </td>

      <td>
        <code>String</code> The hash must be calculated based on the following logic:  
        sha512(key\|command\|var1\|salt)
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>



### var1 JSON Object fields description (inside var1)

| Parameter          | Description                                                                                                                                                                                                                                                                                                                                                                                       | Example                                        |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| requestId          | <code>String</code> Request ID.                                                                                                                                                                                                                                                                                                                                                                   | 12345678                                       |
| transactionDetails | <code>Object</code> Must contain <code>amount</code> (transaction amount) and optionally <code>txnid</code> (transaction ID).                                                                                                                                                                                                                                                                     | \{"amount": "100.00", "txnid": "TXN123"}       |
| useCase            | <code>Object</code> Flags for which information to return: <code>getExtendedPaymentDetails</code>, <code>getAdditionalCharges</code>, <code>getTaxSpecification</code>, <code>checkDownStatus</code>, <code>checkCustomerEligibility</code>. Optionally <code>filters</code> (e.g. <code>paymentOptions.emi.dc</code>, <code>cc</code>, <code>cardless</code>; <code>paymentOptions.bnpl</code>). | \{"getExtendedPaymentDetails": true}           |
| customerDetails    | <code>Object</code> Optional. Customer info (e.g. <code>mobile</code>) for eligibility checks.                                                                                                                                                                                                                                                                                                    | \{"mobile": "9098765432"}                      |
| filters            | <code>Object</code> Optional. Filter response by <code>paymentOptions</code> (emi.dc, cc, cardless; bnpl). Include "all" for all banks in a category.                                                                                                                                                                                                                                             | \{"paymentOptions": \{"emi": \{"dc": "ICIC"}}} |

### useCase JSON Object Fields Description

| Field                     | Description                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| getExtendedPaymentDetails | <code>Boolean</code> Set <code>true</code> to check EMI eligibility (mobile/card) and “Buy Now Pay Later” modes; returns title, EMI breakup, etc. |
| getAdditionalCharges      | <code>Boolean</code> Set <code>true</code> to return additional charges for all payment options.                                                  |
| getTaxSpecification       | <code>Boolean</code> Set <code>true</code> to return tax specification from backend for splitting additional charges.                             |
| checkDownStatus           | <code>Boolean</code> Set <code>true</code> to return downtime of payment options.                                                                 |
| checkCustomerEligibility  | <code>Boolean</code> Set <code>true</code> to return customer eligibility.                                                                        |
</Accordion>

<Accordion title="Sample request (cURL)" icon="fa-code">
  ```cUrl
  curl --location 'https://info.payu.in/merchant/postservice.php?form=2' \
  --form 'key="merchant key"' \
  --form 'command="get_checkout_details"' \
  --form 'var1="{\"requestId\":\"Test212345\",\"transactionDetails\":{\"amount\":10000},\"customerDetails\":{\"mobile\":\"9368252248\"},\"useCase\":{\"checkCustomerEligibility\":true},\"filters\":{\"paymentOptions\":{\"emi\":{\"dc\":\"all\",\"cc\":\"all\",\"cardless\":\"all\"},\"bnpl\":\"all\"}}}"' \
  --form 'hash="hash value"'
  ```
</Accordion>

<Accordion title="Sample response (excerpt)" icon="fa-reply">
  <Callout icon="📘" theme="info">
    **Note**: You must look for the **eligibility** object is having **status=true**  inside the **ntb** JSON object similar to the following:

    ```json

       "ntb": {
                              "cardless": {
                                  "all": {
                                      "LPEMI": {
                                          "maximumAmount": null,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "hasEligible": true
                              }
                          }
                      }
    ```
  </Callout>

  ```json
  {
    "httpCode": "200",
    "message": "",
    "status": 1,
    "data": {
        "details": {
            "paymentOption": {
                "emi": {
                    "all": {
                        "cardless": {
                            "all": {
                                "BIMAPAY": {
                                    "tenureOptions": {
                                        "BIMAP03": {
                                            "tenure": 3,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                       .....
                    "ntb": {
                        "cardless": {
                            "all": {
                                "LPEMI": {
                                    "maximumAmount": null,
                                    "eligibility": {
                                        "status": true
                                    }
                                }
                            },
                            "hasEligible": true
                        }
                    }
                },
  ...
  ...
  ...
                        }
                    }
                }
            }
        }
    }
  }
  ```
</Accordion>

<br />

***

## Step 2: Get EMI Checkout Details API

Use the **Get EMI Checkout Details** API to check detailed EMI eligibility for a specific bank/lender and customer (e.g. cardless EMI / Link and Pay NTB). It returns tenure options, maximum amounts, and eligibility status per tenure.

| Environment | URL                                                             |
| :---------- | :-------------------------------------------------------------- |
| Test        | `https://test.payu.in/info/linkAndPay/get_emi_checkout_details` |
| Production  | `https://info.payu.in/linkAndPay/get_emi_checkout_details`      |

**Method:** POST (JSON body)  
**Content-Type:** `application/json`

<Accordion title="Authentication (headers)" icon="fa-lock">
  * **Date** (mandatory): Request time in GMT (e.g. `Thu, 17 Feb 2022 08:17:59 GMT`).
  * **Authorization** (mandatory): HMAC-SHA512 signature. Format:\
    `hmac username="<merchant_key>", algorithm="hmac-sha512", headers="date digest", signature="<signature>"`\
    Signing string: `Date + "\n" + Digest`. Use merchant **Salt** as secret.\
    For more information, referr to [Get EMI Checkout Details API > Authorization](ref:get-emi-checkout-details-api#required-parameters-for-calculating-authorization).
  * **Digest** (mandatory when required by spec): Base64(sha256(request body)).
  * **platformId** (mandatory): Set to `1`.
</Accordion>

<Accordion title="Request parameters" icon="fa-list">
  | Parameter                           | Description                                                  | Example      |
  | :---------------------------------- | :----------------------------------------------------------- | :----------- |
  | bankCode                            | Bank/lender code (e.g. `LPEMI` for cardless EMI).            | `LPEMI`      |
  | phone                               | Customer mobile number for eligibility.                      | `8178959206` |
  | amount                              | Transaction amount for eligibility check.                    | `10000.00`   |
  | pg                                  | Payment category; use `EMI` for EMI/Link and Pay NTB.        | `EMI`        |
  | checkCustomerEligibilityWithDetails | When `true`, eligibility is checked using `customerDetails`. | `true`       |
  | customerDetails                     | Customer onboarding details for NTB eligibility.             | See below    |

  **customerDetails (mandatory when checking eligibility with details):**

  * **panNumber**, **dob**, **zipcode**, **firstName**, **lastName** (mandatory).
  * **bureauPullConsent**, **gender**, **income**, **employeeType**, **abs** (optional as per API).
</Accordion>

<Accordion title="Sample request (cURL)" icon="fa-code">
  ```bash
  curl --location 'https://test.payu.in/info/linkAndPay/get_emi_checkout_details' \
  --header 'Content-Type: application/json' \
  --header 'authorization: hmac username="<merchant_key>", algorithm="sha512", headers="date", signature="<signature>"' \
  --header 'date: Mon, 28 Oct 2024 10:34:49 GMT' \
  --data '{
    "bankCode": "LPEMI",
    "phone": "8178959206",
    "amount": "10000.00",
    "pg": "EMI",
    "checkCustomerEligibilityWithDetails": true,
    "customerDetails": {
      "panNumber": "EIJPS1234R",
      "dob": "14-12-1996",
      "zipcode": "411014",
      "firstName": "Shray",
      "lastName": "Suri",
      "bureauPullConsent": "false",
      "gender": "Male",
      "income": "65000",
      "employeeType": "Salaried"
    }
  }'
  ```
</Accordion>

<Accordion title="Sample response (success excerpt)" icon="fa-reply">
  ```json
  {
    "httpCode": "200",
    "status": 1,
    "data": {
      "emi": {
        "ntb": {
          "cardless": {
            "all": {
              "LPEMI": {
                "tenureOptions": {
                  "LPEMI03": { "tenure": 3, "maximumAmount": 60000.0, "eligibility": { "status": true } },
                  "LPEMI06": { "tenure": 6, "maximumAmount": 100000.0, "eligibility": { "status": true } }
                },
                "eligibility": { "status": true }
              }
            },
            "hasEligible": true
          }
        }
      }
    }
  }
  ```
</Accordion>
