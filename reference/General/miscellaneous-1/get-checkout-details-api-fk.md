---
title: Get Checkout Details API -FK
deprecated: false
hidden: true
metadata:
  robots: index
---
This API retrieves available payment options and eligibility details for a given transaction, including customer-specific limits and EMI options.

## Environment

| Environment | Base URL |
|-------------|----------|
| **Test** | `https://test.payu.in/merchant/postservice.php?form=2` |
| **Production** | `https://info.payu.in/merchant/postservice.php?form=2` |

## Authentication

- **Method**: Form-based POST with hash authentication
- **Content-Type**: `application/x-www-form-urlencoded`
- **Required Fields**: 
  - `key`: Merchant key
  - `command`: `get_checkout_details`
  - `var1`: JSON request body
  - `hash`: SHA512 hash of `key|command|var1|salt`

## Request Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| requestId<br/><code>mandatory</code> | `String` Unique identifier for the request to track the API call. | `"9078698a15d746feadcffbdaf979a198"` |
| transactionDetails<br/><code>mandatory</code> | `Object` Contains transaction-specific information including amount and charges. | See transactionDetails table below |
| useCase<br/><code>mandatory</code> | `Object` Configuration flags to control eligibility checks and limit information in response. | See useCase table below |
| customerDetails<br/><code>mandatory</code> | `Object` Customer information required for eligibility checks. | See customerDetails table below |
| filters<br/><code>optional</code> | `Object` Filter criteria to specify which payment options to retrieve. | See filters table below |

### transactionDetails Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| source<br/><code>optional</code> | `String` &#124; `null` Source identifier for the transaction origin. | `null` |
| amount<br/><code>mandatory</code> | `Number` Transaction amount in smallest currency unit (e.g., paise for INR). | `47990` |
| pre_authorize<br/><code>optional</code> | `Boolean` &#124; `null` Whether the transaction should be pre-authorized. | `null` |
| additional_charges<br/><code>optional</code> | `Object` &#124; `null` Additional charges associated with the transaction. | `null` |

### useCase Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| checkNTBCustomerEligibility<br/><code>optional</code> | `Boolean` Whether to check new-to-bank (NTB) customer eligibility. | `false` |
| checkCustomerEligibility<br/><code>optional</code> | `Boolean` Whether to check general customer eligibility for payment options. | `true` |
| returnUserLimit<br/><code>optional</code> | `Boolean` Whether to include per-user limit information in the response. When `true`, eligibility and maximumEligibleLimit fields are returned. | `true` |

### customerDetails Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| mobile<br/><code>mandatory</code> | `String` Customer's mobile number for eligibility verification. | `"9123412345"` |

### filters Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| paymentOptions<br/><code>optional</code> | `Object` Specify which payment options to retrieve (e.g., EMI, cardless options). | `{"emi": {"cardless": "all"}}` |

## Sample Request

```json
{
  "requestId": "9078698a15d746feadcffbdaf979a198",
  "transactionDetails": {
    "source": null,
    "amount": 47990,
    "pre_authorize": null,
    "additional_charges": null
  },
  "useCase": {
    "checkNTBCustomerEligibility": false,
    "checkCustomerEligibility": true,
    "returnUserLimit": true
  },
  "customerDetails": {
    "mobile": "9123412345"
  },
  "filters": {
    "paymentOptions": {
      "emi": {
        "cardless": "all"
      }
    }
  }
}
```

## Sample Response

```json
{
  "requestId": "9078698a15d746feadcffbdaf979a198",
  "transactionDetails": {
    "source": null,
    "amount": 47990,
    "pre_authorize": null,
    "additional_charges": null
  },
  "useCase": {
    "checkNTBCustomerEligibility": false,
    "checkCustomerEligibility": true,
    "returnUserLimit": true
  },
  "customerDetails": {
    "mobile": "9123412345"
  },
  "filters": {
    "paymentOptions": {
      "emi": {
        "cardless": "all"
      }
    }
  },
  "details": {
    "paymentOptions": {
      "emi": {
        "all": {
          "cardless": {
            "all": {
              "LPEMI": {
                "tenureOptions": {
                  "LPEMI12": {
                    "tenure": 12,
                    "maximumAmount": null,
                    "maximumEligibleLimit": 1000000,
                    "eligibility": {
                      "status": true
                    }
                  },
                  "LPEMI": {
                    "tenure": 0,
                    "maximumAmount": null,
                    "maximumEligibleLimit": 1000000,
                    "eligibility": {
                      "status": true
                    }
                  },
                  "LPEMI09": {
                    "tenure": 9,
                    "maximumAmount": null,
                    "maximumEligibleLimit": 1000000,
                    "eligibility": {
                      "status": true
                    }
                  },
                  "LPEMI03": {
                    "tenure": 3,
                    "maximumAmount": null,
                    "maximumEligibleLimit": 1000000,
                    "eligibility": {
                      "status": true
                    }
                  },
                  "LPEMI06": {
                    "tenure": 6,
                    "maximumAmount": null,
                    "maximumEligibleLimit": 1000000,
                    "eligibility": {
                      "status": true
                    }
                  }
                },
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
    }
  },
  "registeredAmtConvFee": null,
  "recurringAmtConvFee": null,
  "configData": null,
  "status": 1
}
```

## Response Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| requestId<br/><code>mandatory</code> | `String` Echoes the request identifier from the input. | `"9078698a15d746feadcffbdaf979a198"` |
| transactionDetails<br/><code>mandatory</code> | `Object` Echoes the transaction details from the request. | Same as request transactionDetails |
| useCase<br/><code>mandatory</code> | `Object` Echoes the useCase flags from the request. | Same as request useCase |
| customerDetails<br/><code>mandatory</code> | `Object` Echoes the customer details from the request. | Same as request customerDetails |
| filters<br/><code>optional</code> | `Object` Echoes the filters from the request if provided. | Same as request filters |
| details<br/><code>mandatory</code> | `Object` Core checkout details containing available payment options and eligibility information. | See details table below |
| registeredAmtConvFee<br/><code>optional</code> | `Number` &#124; `null` Registered amount convenience fee if applicable. | `null` |
| recurringAmtConvFee<br/><code>optional</code> | `Number` &#124; `null` Recurring amount convenience fee if applicable. | `null` |
| configData<br/><code>optional</code> | `Object` &#124; `null` Additional configuration data if available. | `null` |
| status<br/><code>mandatory</code> | `Number` Response status code. `1` indicates success. | `1` |

### details.paymentOptions Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| emi<br/><code>optional</code> | `Object` Contains EMI payment options and eligibility details. | See EMI structure in sample response |

### EMI Tenure Options (when returnUserLimit = true)

| Parameter | Description | Example |
|-----------|-------------|---------|
| tenure<br/><code>mandatory</code> | `Number` EMI tenure in months. `0` indicates pay later option. | `12` |
| maximumAmount<br/><code>optional</code> | `Number` &#124; `null` Maximum transaction amount allowed for this tenure. | `null` |
| maximumEligibleLimit<br/><code>mandatory</code> | `Number` Maximum eligible limit for the customer for this tenure option. Only returned when `returnUserLimit` is `true`. | `1000000` |
| eligibility<br/><code>mandatory</code> | `Object` Customer eligibility status for this tenure option. Only returned when `returnUserLimit` is `true`. | `{"status": true}` |