---
title: '[Internal Review]Lazypay 3Devguide Changes'
deprecated: false
hidden: true
metadata:
  robots: index
---
Use this section when you want **LazyPay** as a <Glossary>BNPL</Glossary> option on **your own checkout** (merchant hosted or seamless flow): you call PayU’s eligibility service, collect payment with the **`/_payment`** API, then verify the outcome on your servers. LazyPay lets customers pay later on their billing cycle while you settle with PayU as for other BNPL instruments.


## Benefits for your customers

* Pay later with LazyPay on eligible purchases, subject to lender rules and approval.
* Checkout stays on your experience (no full redirect to a separate PayU payment page for the whole journey).
* Eligibility can be checked up front so LazyPay is shown only when the customer can use it.

## Benefits for your business

* You control layout, fields, and when to surface LazyPay (based on eligibility API responses).
* Standard PayU **hash**, **redirect**, and **verification** patterns apply, consistent with other merchant-hosted modes.
* You can align LazyPay with your wider BNPL or affordability strategy using the same PayU keys and reconciliation tools.

## Refunds

**LazyPay supports both full and partial refunds** on settled BNPL transactions (subject to PayU and lender rules). At a high level:

1. You **initiate the refund** (full or partial) against the original PayU transaction.
2. **PayU forwards the refund** to LazyPay for the same amount.
3. **LazyPay credits** the customer’s LazyPay balance and adjusts their account or billing position per LazyPay’s policy.
4. The **merchant settlement** is adjusted accordingly (for example the refunded amount is recovered from your account or future settlement).

You may run **multiple partial refunds** until the cumulative refunded amount does not exceed the original transaction amount. **Processing fees, GST, and lender charges** may or may not be reversed depending on lender and PayU policy—see the detailed notes in [Refunds for BNPL](doc:refunds-for-bnpl).


<Callout icon="📘" theme="info">
  **Before you begin**

  * LazyPay and BNPL must be **enabled and configured** on your merchant account. For enablement, configuration, onboarding, and **test mobile whitelisting** for LazyPay, work with your **PayU Key Account Manager (KAM)**.
  * Use **HTTPS** for **`surl`** and **`furl`**. Plan for **server-side verification** of each transaction; do not treat the browser redirect alone as proof of payment.
  * For the **`bankcode`** value and other BNPL lenders, see [BNPL Codes](doc:bnpl-codes). For first-time vs repeat customer behaviour (linking, OTP, tokens) at the product level, see [BNPL Link and Pay](doc:collect-payments-with-bnpl-using-link-and-pay). For the BNPL product hub in this guide set, see [BNPL Integration](doc:payu-bnpl-integration-introduction).
</Callout>


> 🚧 Minimum amount for BNPL transaction
>
> Minimum amounts can vary by lender. Confirm allowed limits with your **PayU Key Account Manager (KAM)**.


## Sample request

```curl
curl --location 'https://test.payu.in/info/linkAndPay/get_emi_checkout_details' \
--header 'x-credential-username: smsplus' \
--header 'Content-Type: application/json' \
--header 'authorization: hmac username="x0i6r2", algorithm="sha512", headers="date", signature="0e0ebc518c085d8ff49058b7c232bfe2e8779e9e9cafd34a4cdf1c11114035eea75b0e404a9b9e152757dbcc4926f78b6f18ba7f6643e2bf687a65942d3bde38"' \
--header 'date: Mon, 28 Oct 2024 10:34:49 GMT' \
--data '{
  "Key": "yFbXg3",
  "amount": 21,
  "userCredentials": "yFbXg3:test_sud",
  "phone": "9999999999",
  "bankCode": "LAZYPAY",
  "payuToken": null,
  "requestId": "Testing_111"
}'
```

> 📘 Authorization calculation logic
>
> For authorization calculation logic, refer to [Get EMI Checkout Details API > Required parameters for calculating authorization](ref:get-emi-checkout-details-api#required-parameters-for-calculating-authorization).



### GCD request (var1 JSON body)

```json
{
  "requestId": "41308821598386875785",
  "transactionDetails": {
    "amount": 12000.0
  },
  "customerDetails": {
    "mobile": "8178959206"
  },
  "filters": {
    "paymentOptions": {
      "emi": {
        "cardless": "all",
        "payInParts": "all"
      }
    }
  },
  "useCase": {
    "checkCustomerEligibility": true,
    "checkNTBCustomerEligibility": true,
    "returnUserLimit": true
  }
}
```

### GECD request (JSON body)

```json
{
  "bankCode": "LAZYPI3",
  "phone": "8178959206",
  "amount": "10000.00",
  "pg": "EMI",
  "checkCustomerEligibilityWithDetails": true,
  "customerDetails": {
    "panNumber": "KMEPS9053J",
    "dob": "14-12-1996",
    "zipcode": "411014",
    "firstName": "Shray",
    "lastName": "Suri",
    "bureauPullConsent": "false",
    "gender": "Male",
    "income": "100000",
    "employeeType": "Salaried"
  }
}
```

## Sample response

## Notes

- In the GCD response, if the merchant only wants 1A/1B or ETB customers, the merchant must only check lenders under **EMI → ALL → Cardless** and **EMI → PayInParts**.
- If the merchant also wants to show NTB lenders, the **EMI → NTB** section must be checked as well.
- There is a new `paymentOptions.emi` filter: **`payInParts`**.


### GCD response — customer is ETB

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
                "IDFCCL": {
                  "tenureOptions": {
                    "IDFCCL12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "IDFCCL03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "IDFCCL06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "IDFCCL09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "SMPI3": {
                  "tenureOptions": {
                    "SMPI03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": true
                  }
                },
                "ZESTMON": {
                  "tenureOptions": {
                    "ZEST09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZEST06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZEST03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZESTMON": {
                      "tenure": 0,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZEST12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "ICICCL": {
                  "tenureOptions": {
                    "ICICCL12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "ICICCL03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "ICICCL06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "ICICCL09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "HMECDT": {
                  "tenureOptions": {
                    "HMECDT03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT18": {
                      "tenure": 18,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": true
                  }
                },
                "LPEMI": {
                  "tenureOptions": {
                    "LPEMI12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "Journey Type is not allowed on merchant"
                      }
                    },
                    "LPEMI": {
                      "tenure": 0,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "Journey Type is not allowed on merchant"
                      }
                    },
                    "LPEMI09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "Journey Type is not allowed on merchant"
                      }
                    },
                    "LPEMI03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "Journey Type is not allowed on merchant"
                      }
                    },
                    "LPEMI06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "Journey Type is not allowed on merchant"
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Journey Type is not allowed on merchant"
                  }
                },
                "HDFC_CL": {
                  "tenureOptions": {
                    "HDFCCL09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL18": {
                      "tenure": 18,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL12": {
                      "tenure": 12,
                      "maximumAmount": null,
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
          },
          "payInParts": {
            "LAZYPI3": {
              "tenure": "3",
              "processingFee": 94.4,
              "processingFeeGst": 14.4,
              "maximumEligibleLimit": 120000.0,
              "eligibility": {
                "status": true
              },
              "repaymentSchedule": [
                {
                  "amount": 4000.0,
                  "serialNo": 0,
                  "dueDate": "2026-06-10"
                },
                {
                  "amount": 4000.0,
                  "serialNo": 1,
                  "dueDate": "2026-08-01"
                },
                {
                  "amount": 4000.0,
                  "serialNo": 2,
                  "dueDate": "2026-09-01"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

#$# GCD response — customer is NTB

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
                "IDFCCL": {
                  "tenureOptions": {
                    "IDFCCL12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "IDFCCL03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "IDFCCL06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "IDFCCL09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "SMPI3": {
                  "tenureOptions": {
                    "SMPI03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": true
                  }
                },
                "ZESTMON": {
                  "tenureOptions": {
                    "ZEST09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZEST06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZEST03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZESTMON": {
                      "tenure": 0,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZEST12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "ICICCL": {
                  "tenureOptions": {
                    "ICICCL12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "ICICCL03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "ICICCL06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "ICICCL09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "HMECDT": {
                  "tenureOptions": {
                    "HMECDT03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT18": {
                      "tenure": 18,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": true
                  }
                },
                "LPEMI": {
                  "tenureOptions": {
                    "LPEMI12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "LPEMI": {
                      "tenure": 0,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "LPEMI09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "Minimum required amount is 15000"
                      }
                    },
                    "LPEMI03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "LPEMI06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "HDFC_CL": {
                  "tenureOptions": {
                    "HDFCCL09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL18": {
                      "tenure": 18,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL12": {
                      "tenure": 12,
                      "maximumAmount": null,
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
          },
          "ntb": {
            "payInParts": {
              "all": {
                "LAZYPI3": {
                  "maximumAmount": null,
                  "eligibility": {
                    "status": true
                  }
                }
              },
              "hasEligible": true
            },
            "cardless": {
              "all": {},
              "hasEligible": false
            }
          }
        }
      }
    }
  }
}
```

### GCD response — customer is not eligible

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
                "IDFCCL": {
                  "tenureOptions": {
                    "IDFCCL12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "IDFCCL03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "IDFCCL06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "IDFCCL09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "SMPI3": {
                  "tenureOptions": {
                    "SMPI03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": true
                  }
                },
                "ZESTMON": {
                  "tenureOptions": {
                    "ZEST09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZEST06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZEST03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZESTMON": {
                      "tenure": 0,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZEST12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "ICICCL": {
                  "tenureOptions": {
                    "ICICCL12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "ICICCL03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "ICICCL06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "ICICCL09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "HMECDT": {
                  "tenureOptions": {
                    "HMECDT03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT18": {
                      "tenure": 18,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": true
                  }
                },
                "LPEMI": {
                  "tenureOptions": {
                    "LPEMI12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "LPEMI": {
                      "tenure": 0,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "LPEMI09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "Minimum required amount is 15000"
                      }
                    },
                    "LPEMI03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "LPEMI06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "HDFC_CL": {
                  "tenureOptions": {
                    "HDFCCL09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL18": {
                      "tenure": 18,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL12": {
                      "tenure": 12,
                      "maximumAmount": null,
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
          },
          "payInParts": {
            "LAZYPI3": {
              "tenure": "3",
              "eligibility": {
                "status": false,
                "reason": "This mobile number is not eligible. Please change the mobile number."
              }
            }
          }
        }
      }
    }
  }
}
```


### GECD response — registration success

```json
{
  "httpCode": "200",
  "message": "",
  "status": 1,
  "data": {
    "emi": {
      "ntb": {
        "payInParts": {
          "LAZYPI3": {
            "tenure": "3",
            "minimumAmount": 3000.0,
            "maximumAmount": 180000.0,
            "interestRate": 0,
            "processingFee": 78.67,
            "processingFeeGst": 12.0,
            "maximumEligibleLimit": 51000.0,
            "eligibility": {
              "status": true
            },
            "repaymentSchedule": [
              {
                "amount": 3333.33,
                "serialNo": 0,
                "dueDate": "2026-06-10"
              },
              {
                "amount": 3333.0,
                "serialNo": 1,
                "dueDate": "2026-08-01"
              },
              {
                "amount": 3333.67,
                "serialNo": 2,
                "dueDate": "2026-09-01"
              }
            ]
          }
        }
      }
    }
  }
}
```

### GECD response — registration failed

```json
{
  "httpCode": "200",
  "message": "",
  "status": 1,
  "data": {
    "emi": {
      "ntb": {
        "payInParts": {
          "LAZYPI3": {
            "eligibility": {
              "status": false,
              "reason": "This mobile number is not eligible. Please change the mobile number."
            }
          }
        }
      }
    }
  }
}
```


| Field | Description |
| :-- | :-- |
| status | Provider status in BNPL context. |
| kfsLink | Key Fact Statement or disclosure URL when applicable. |
| eligible | Whether LazyPay can be offered for this amount and user context. |
| customerLinked | Whether the user has completed linking for repeat / one-click style flows. |
| PayuToken | Token used on subsequent calls when supported by your integration. |

For additional success and failure shapes (including multi-lender responses), refer to [Get EMI Checkout Details API > Sample response](ref:get-emi-checkout-details-api#sample-response).