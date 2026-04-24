---
title: 'Get Checkout Details API '
deprecated: false
hidden: true
metadata:
  robots: index
---
This API retrieves available payment options and eligibility details for a given transaction, including customer-specific limits and EMI options.

## Environment

| Environment    | Base URL                                               |
| -------------- | ------------------------------------------------------ |
| **Test**       | `https://test.payu.in/merchant/postservice.php?form=2` |
| **Production** | `https://info.payu.in/merchant/postservice.php?form=2` |

## Authentication

**HTTP Method**: Form-based POST with hash authentication

**Content-Type**: `application/x-www-form-urlencoded`

## Request Parameters

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
        key<br />`mandatory`
      </td>

      <td>
        `String`<br />Your merchant key provided by PayU.
      </td>

      <td>
        `JP***g`
      </td>
    </tr>

    <tr>
      <td>
        command<br />`mandatory`
      </td>

      <td>
        `String`<br />The API command name.
      </td>

      <td>
        `get_checkout`
      </td>
    </tr>

    <tr>
      <td>
        var1<br />`mandatory`
      </td>

      <td>
        `JSON String`<br />JSON object containing the transaction details. For more information, [var1 Object Parameters Description](#var1-object-parameters-description.)
      </td>

      <td>
        For more information, [var1 Object Parameters Description](#var1-object-parameters-description.)
      </td>
    </tr>

    <tr>
      <td>
        hash<br />`mandatory`
      </td>

      <td>
        `String`<br />The hash value generated using the following hash logic:  
        hash = sha512(key|command|var1|\SALT)
      </td>

      <td>
        `jbUS07Og8BToVZ`
      </td>
    </tr>
  </tbody>
</Table>

### var1 Object Parameters Description

| Field                                          | Description                                                                                   | Example                              |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------ |
| requestId<br /><code>mandatory</code>          | `String` Unique identifier for the request to track the API call.                             | `"9078698a15d746feadcffbdaf979a198"` |
| transactionDetails<br /><code>mandatory</code> | `Object` Contains transaction-specific information including amount and charges.              | See transactionDetails table below   |
| useCase<br /><code>mandatory</code>            | `Object` Configuration flags to control eligibility checks and limit information in response. | See useCase table below              |
| customerDetails<br /><code>mandatory</code>    | `Object` Customer information required for eligibility checks.                                | See customerDetails table below      |
| filters<br /><code>optional</code>             | `Object` Filter criteria to specify which payment options to retrieve.                        | See filters table below              |
| transactionDetails<br /><code>mandatory</code> | SHA512 hash of `key\|command\|var1\|salt`                                                     |                                      |

### transactionDetails Parameters

| Parameter                                     | Description                                                                  | Example |
| --------------------------------------------- | ---------------------------------------------------------------------------- | ------- |
| source<br /><code>optional</code>             | `String` \| `null` Source identifier for the transaction origin.             | `null`  |
| amount<br /><code>mandatory</code>            | `Number` Transaction amount in smallest currency unit (e.g., paise for INR). | `47990` |
| pre_authorize<br /><code>optional</code>      | `Boolean` \| `null` Whether the transaction should be pre-authorized.        | `null`  |
| additional_charges<br /><code>optional</code> | `Object` \| `null` Additional charges associated with the transaction.       | `null`  |

### useCase Parameters

| Parameter                                              | Description                                                                                                                                     | Example |
| :----------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- | :------ |
| checkNTBCustomerEligibility<br /><code>optional</code> | `Boolean` Whether to check new-to-bank (NTB) customer eligibility.                                                                              | `false` |
| checkCustomerEligibility<br /><code>optional</code>    | `Boolean` Whether to check general customer eligibility for payment options.                                                                    | `true`  |
| returnUserLimit<br /><code>optional</code>             | `Boolean` Whether to include per-user limit information in the response. When `true`, eligibility and maximumEligibleLimit fields are returned. | `true`  |
| getExtendedPaymentDetails<br /><code>optional</code>   | `Boolean`This field must be set to `true` to get the extended details such as ROI. The default value is `false`.                                | true    |

### customerDetails Parameters

| Parameter                          | Description                                                     | Example        |
| ---------------------------------- | --------------------------------------------------------------- | -------------- |
| mobile<br /><code>mandatory</code> | `String` Customer's mobile number for eligibility verification. | `"9123412345"` |

### filters Parameters

| Parameter                                 | Description                                                                       | Example                        |
| ----------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------ |
| paymentOptions<br /><code>optional</code> | `Object` Specify which payment options to retrieve (e.g., EMI, cardless options). | `{"emi": {"cardless": "all"}}` |

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

**Without Extended Payment Details**

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

**With Extended Payment Details**

```json
{
  "requestId": "9078612a15d746feadcffbdaf979a198",
  "transactionDetails": {
    "source": null,
    "amount": 47990,
    "pre_authorize": null,
    "additional_charges": null
  },
  "useCase": {
    "checkNTBCustomerEligibility": false,
    "checkCustomerEligibility": true,
    "returnUserLimit": true,
    "getExtendedPaymentDetails" : true
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
              "ZESTMON": {
                "tenureOptions": {
                  "ZEST09": {
                    "tenure": 9,
                    "minimumAmount": 3000.0,
                    "maximumAmount": 300000.0,
                    "interestRate": 0,
                    "monthlyEmi": 1111.11,
                    "paybackAmount": 0.0,
                    "bankCharge": 0.0,
                    "eligibility": {
                      "status": true
                    }
                  },
                  "ZEST06": {
                    "tenure": 6,
                    "minimumAmount": 3000.0,
                    "maximumAmount": 300000.0,
                    "interestRate": 0,
                    "monthlyEmi": 1666.67,
                    "interestCharged": 0.02,
                    "paybackAmount": 0.0,
                    "bankCharge": 0.0,
                    "eligibility": {
                      "status": true
                    }
                  },
                  "ZEST03": {
                    "tenure": 3,
                    "minimumAmount": 3000.0,
                    "maximumAmount": 300000.0,
                    "interestRate": 0,
                    "monthlyEmi": 3333.33,
                    "paybackAmount": 0.0,
                    "bankCharge": 0.0,
                    "eligibility": {
                      "status": true
                    }
                  },
                  "ZESTMON": {
                    "tenure": 0,
                    "minimumAmount": 3000.0,
                    "maximumAmount": 300000.0,
                    "interestRate": 0,
                    "monthlyEmi": 0,
                    "paybackAmount": 0.0,
                    "bankCharge": 0.0,
                    "eligibility": {
                      "status": true
                    }
                  },
                  "ZEST12": {
                    "tenure": 12,
                    "minimumAmount": 3000.0,
                    "maximumAmount": 300000.0,
                    "interestRate": 0,
                    "monthlyEmi": 833.33,
                    "paybackAmount": 0.0,
                    "bankCharge": 0.0,
                    "eligibility": {
                      "status": true
                    }
                  }
                },
                "title": "ZestMoney",
                "shortTitle": "ZestMoney",
                "priority": "100",
                "minimumAmount": 3000.0,
                "maximumAmount": 300000.0,
                "eligibility": {
                  "status": true
                }
              },
              "LPEMI": {
                "tenureOptions": {
                  "LPEMI12": {
                    "tenure": 12,
                    "minimumAmount": 3000.0,
                    "maximumAmount": 1000000.0,
                    "interestRate": 18,
                    "monthlyEmi": 916.8,
                    "interestCharged": 1001.6,
                    "paybackAmount": 0.0,
                    "bankCharge": 0.0,
                    "eligibility": {
                      "status": true
                    }
                  },
                  "LPEMI": {
                    "tenure": 0,
                    "minimumAmount": 3000.0,
                    "maximumAmount": 1000000.0,
                    "interestRate": 18,
                    "monthlyEmi": 0,
                    "paybackAmount": 0.0,
                    "bankCharge": 0.0,
                    "eligibility": {
                      "status": true
                    }
                  },
                  "LPEMI09": {
                    "tenure": 9,
                    "minimumAmount": 15000.0,
                    "maximumAmount": 1000000.0,
                    "interestRate": 18,
                    "monthlyEmi": 1196.1,
                    "interestCharged": 764.9,
                    "paybackAmount": 0.0,
                    "bankCharge": 0.0,
                    "eligibility": {
                      "status": false,
                      "reason": "Minimum required amount is 15000"
                    }
                  },
                  "LPEMI03": {
                    "tenure": 3,
                    "minimumAmount": 3000.0,
                    "maximumAmount": 60000.0,
                    "interestRate": 18,
                    "monthlyEmi": 3433.83,
                    "interestCharged": 301.49,
                    "paybackAmount": 0.0,
                    "bankCharge": 0.0,
                    "eligibility": {
                      "status": true
                    }
                  },
                  "LPEMI06": {
                    "tenure": 6,
                    "minimumAmount": 6000.0,
                    "maximumAmount": 1000000.0,
                    "interestRate": 18,
                    "monthlyEmi": 1755.25,
                    "interestCharged": 531.5,
                    "paybackAmount": 0.0,
                    "bankCharge": 0.0,
                    "eligibility": {
                      "status": true
                    }
                  }
                },
                "title": "LazyPay EMI",
                "shortTitle": "Lazypay",
                "priority": "100",
                "minimumAmount": 3000.0,
                "maximumAmount": 1000000.0,
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

| Parameter                                       | Description                                                                                      | Example                              |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------ |
| requestId<br /><code>mandatory</code>           | `String` Echoes the request identifier from the input.                                           | `"9078698a15d746feadcffbdaf979a198"` |
| transactionDetails<br /><code>mandatory</code>  | `Object` Echoes the transaction details from the request.                                        | Same as request transactionDetails   |
| useCase<br /><code>mandatory</code>             | `Object` Echoes the useCase flags from the request.                                              | Same as request useCase              |
| customerDetails<br /><code>mandatory</code>     | `Object` Echoes the customer details from the request.                                           | Same as request customerDetails      |
| filters<br /><code>optional</code>              | `Object` Echoes the filters from the request if provided.                                        | Same as request filters              |
| details<br /><code>mandatory</code>             | `Object` Core checkout details containing available payment options and eligibility information. | See details table below              |
| registeredAmtConvFee<br /><code>optional</code> | `Number` \| `null` Registered amount convenience fee if applicable.                              | `null`                               |
| recurringAmtConvFee<br /><code>optional</code>  | `Number` \| `null` Recurring amount convenience fee if applicable.                               | `null`                               |
| configData<br /><code>optional</code>           | `Object` \| `null` Additional configuration data if available.                                   | `null`                               |
| status<br /><code>mandatory</code>              | `Number` Response status code. `1` indicates success.                                            | `1`                                  |

### details.paymentOptions Parameters

| Parameter                      | Description                                                    | Example                              |
| ------------------------------ | -------------------------------------------------------------- | ------------------------------------ |
| emi<br /><code>optional</code> | `Object` Contains EMI payment options and eligibility details. | See EMI structure in sample response |

### EMI Tenure Options (when returnUserLimit = true)

| Parameter                                        | Description                                                                                                              | Example            |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| tenure<br /><code>mandatory</code>               | `Number` EMI tenure in months. `0` indicates pay later option.                                                           | `12`               |
| maximumAmount<br /><code>optional</code>         | `Number` \| `null` Maximum transaction amount allowed for this tenure.                                                   | `null`             |
| maximumEligibleLimit<br /><code>mandatory</code> | `Number` Maximum eligible limit for the customer for this tenure option. Only returned when `returnUserLimit` is `true`. | `1000000`          |
| eligibility<br /><code>mandatory</code>          | `Object` Customer eligibility status for this tenure option. Only returned when `returnUserLimit` is `true`.             | `{"status": true}` |
