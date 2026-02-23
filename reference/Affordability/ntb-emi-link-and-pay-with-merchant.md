---
title: 'NTB EMI - Link and Pay with Merchant '
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Get EMI Checkout Details (Link and Pay) API
excerpt: Accepts customer details from the merchant page and returns eligibility status. Calls EMI MS NTBPreEligibility downstream. Used for NTB Seamless Journey.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---

This API accepts customer details entered on the merchant page and returns the customer's eligibility status for EMI/NTB options. It is also referred to as the **Link and Pay API** in the NTB Seamless Journey.


## Request parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| key<br />`mandatory`         | `String` - This parameter contains the merchant key provided by PayU during onboarding.                                                                                         | JP***g                                                       |
| txnid<br />`mandatory`       | `String` - This parameter contains a unique transaction ID. You can generate this ID or use the PayU API to generate it. The maximum length of this parameter is 25 characters. | txn_applepay_001                                             |
| amount<br />`mandatory`      | `String` - This parameter contains the payment amount.                                                                                                                          | 100.00                                                       |
| productinfo<br />`mandatory` | `String` - This parameter contains a brief description of the product or service.                                                                                               | iPhone Case                                                  |
| firstname<br />`mandatory`   | `String` - This parameter contains the first name of the customer.                                                                                                              | John                                                         |
| email<br />`mandatory`       | `String` - This parameter contains the email address of the customer.                                                                                                           | [john@example.com](mailto:john@example.com)                  |
| phone<br/><code>mandatory</code> | <code>String</code> Customer mobile number. | `"8178959206"` |
| amount<br/><code>mandatory</code> | <code>String</code> Transaction amount. | `"10000.00"` |
| pg<br/><code>mandatory</code> | <code>String</code> Payment category; use `"EMI"` for EMI. | `"EMI"` |
| bankCode<br/><code>mandatory</code> | <code>String</code> Bank/lender code (e.g. LPEMI for cardless EMI). | `"LPEMI"` |
| checkCustomerEligibilityWithDetails<br/><code>mandatory</code> | <code>Boolean</code> When true, eligibility is checked using the provided customer details. | `true` |
| <br/>customerDetails<code>mandatory</code> | <code>Object</code> Customer onboarding details for NTB eligibility. | See example below |
| surl<br />`mandatory`        | `String` - This parameter contains the Success URL. PayU will redirect the customer to this URL after a successful payment.                                                     | [https://yoursite.com/success](https://yoursite.com/success) |
| furl<br />`mandatory`        | `String` - This parameter contains the Failure URL. PayU will redirect the customer to this URL after a failed payment.                                                         | [https://yoursite.com/failure](https://yoursite.com/failure) |
| hash<br />`mandatory`        | `String` - This parameter contains the hash value calculated using SHA-512 algorithm. Hash logic ensures the integrity of the transaction data.                                 | See hash generation                                          |
| lastname<br />`optional`     | `String` - This parameter contains the last name of the customer.                                                                                                               | Doe                                                          |
| address1<br />`optional`     | `String` - This parameter contains the first line of the billing address.                                                                                                       | 123 Main St                                                  |
| address2<br />`optional`     | `String` - This parameter contains the second line of the billing address.                                                                                                      | Apt 4B                                                       |
| city<br />`optional`         | `String` - This parameter contains the city of the billing address.                                                                                                             | Mumbai                                                       |
| state<br />`optional`        | `String` - This parameter contains the state of the billing address.                                                                                                            | Maharashtra                                                  |
| country<br />`optional`      | `String` - This parameter contains the country of the billing address.                                                                                                          | India                                                        |
| zipcode<br />`optional`      | `String` - This parameter contains the ZIP/postal code of the billing address.                                                                                                  | 400001                                                       |
| udf1<br />`optional`         | `String` - This parameter contains any additional information you want to pass. Maximum length is 255 characters.                                                               |                                                              |
| udf2<br />`optional`         | `String` - This parameter contains any additional information you want to pass. Maximum length is 255 characters.                                                               |                                                              |
| udf3<br />`optional`         | `String` - This parameter contains any additional information you want to pass. Maximum length is 255 characters.                                                               |                                                              |
| udf4<br />`optional`         | `String` - This parameter contains any additional information you want to pass. Maximum length is 255 characters.                                                               |                                                              |
| udf5<br />`optional`         | `String` - This parameter contains any additional information you want to pass. Maximum length is 255 characters.                                                               | 

#### customerDetails JSON Fields Description
| Field | Description | Example |
| panNumber<br/><code>mandatory</code> | <code>String</code> Customer PAN number. | `"EIJPS1234R"` |
| dob<br/><code>mandatory</code> | <code>String</code> Date of birth (DD-MM-YYYY). | `"14-12-1996"` |
| zipcode<br/><code>mandatory</code> | <code>String</code> Postal zip code. | `"411014"` |
| firstName<br/><code>mandatory</code> | <code>String</code> Customer first name. | `"Shray"` |
| lastName<br/><code>mandatory</code> | <code>String</code> Customer last name. | `"Suri"` |
| bureauPullConsent<br/><code>optional</code> | <code>String</code> Consent for bureau pull (e.g. "true"/"false"). | `"false"` |
| gender<br/><code>optional</code> | <code>String</code> Customer gender. | `"Male"` |
| income<br/><code>optional</code> | <code>String</code> Customer income. | `"65000"` |
| employeeType<br/><code>optional</code> | <code>String</code> Employment type (e.g. Salaried). | `"Salaried"` |
| abs<br/><code>optional</code> | <code>String</code> Additional business-specific field if required. | `"Asnw"` |

## Response parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| httpCode<br/><code>mandatory</code> | <code>String</code> HTTP status code of the response. | `"200"` |
| message<br/><code>optional</code> | <code>String</code> Message from the API. | `""` |
| status<br/><code>mandatory</code> | <code>Integer</code> Status indicator (1 for success). | `1` |
| data<br/><code>optional</code> | <code>Object</code> Response payload with EMI tenure options and eligibility. | See sample response |
| data.emi.ntb.cardless.all<br/><code>optional</code> | <code>Object</code> NTB cardless lender (e.g. LPEMI) with tenureOptions and eligibility. | See sample response |
| data.emi.ntb.cardless.all.LPEMI.tenureOptions<br/><code>optional</code> | <code>Object</code> Tenure options (e.g. LPEMI03, LPEMI06, LPEMI09, LPEMI12) with tenure, maximumAmount, eligibility. | `{"LPEMI03": {"tenure": 3, "maximumAmount": 60000.0, "eligibility": {"status": true}}}` |
| data.emi.ntb.cardless.all.LPEMI.eligibility<br/><code>optional</code> | <code>Object</code> Overall eligibility for the lender. | `{"status": true}` or `{"status": false, "reason": "..."}` |
| hasEligible<br/><code>optional</code> | <code>Boolean</code> Whether the customer has any eligible option. | `true` |

## Sample request



## Sample response 
###Success scenario (customer eligible)

```json
{
  "httpCode": "200",
  "message": "",
  "status": 1,
  "data": {
    "emi": {
      "ntb": {
        "cardless": {
          "all": {
            "LPEMI": {
              "tenureOptions": {
                "LPEMI12": { "tenure": 12, "maximumAmount": 100000.0, "eligibility": { "status": false, "reason": "Tenure not available" } },
                "LPEMI03": { "tenure": 3, "maximumAmount": 60000.0, "eligibility": { "status": true } },
                "LPEMI09": { "tenure": 9, "maximumAmount": 100000.0, "eligibility": { "status": false, "reason": "Tenure not available" } },
                "LPEMI06": { "tenure": 6, "maximumAmount": 100000.0, "eligibility": { "status": true } },
                "LPEMI": { "tenure": 0, "maximumAmount": 100000.0, "eligibility": { "status": false, "reason": "Tenure not available" } }
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

###Failure scenario (customer not eligible)

```json
{
  "httpCode": "200",
  "message": "",
  "status": 1,
  "data": {
    "emi": {
      "ntb": {
        "cardless": {
          "all": {
            "LPEMI": {
              "tenureOptions": {
                "LPEMI12": { "tenure": 12, "maximumAmount": 100000.0, "eligibility": { "status": false, "reason": "Tenure not available" } },
                "LPEMI03": { "tenure": 3, "maximumAmount": 60000.0, "eligibility": { "status": false, "reason": "Tenure not available" } },
                "LPEMI09": { "tenure": 9, "maximumAmount": 100000.0, "eligibility": { "status": false, "reason": "Tenure not available" } },
                "LPEMI06": { "tenure": 6, "maximumAmount": 100000.0, "eligibility": { "status": false, "reason": "Tenure not available" } },
                "LPEMI": { "tenure": 0, "maximumAmount": 100000.0, "eligibility": { "status": false, "reason": "Tenure not available" } }
              },
              "eligibility": { "status": false, "reason": "Use is not eligible for cof product" }
            }
          },
          "hasEligible": false
        }
      }
    }
  }
}
```
