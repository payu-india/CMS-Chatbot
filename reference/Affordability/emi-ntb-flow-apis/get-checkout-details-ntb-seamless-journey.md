---
title: Get Checkout Details – NTB Seamless Journey
deprecated: false
hidden: true
metadata:
  robots: index
---
The Get Checkout Details (get_checkout_details) API is a generic API using which they can get information when you create the custom checkout pages, that will contain the payment options, offers, recommendations, and downtime details This section is for the **NTB Seamless Journey** flow.

**Environment**

|                        |                                                  |
| :--------------------- | :----------------------------------------------- |
| Test Environment       | https://test.payu.in/merchant/postservice?form=2 |
| Production Environment | https://info.payu.in/merchant/postservice?form=2 |

## Request parameters

| Parameter | Description                                                                                                                                                | Example              |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| key       | <code>String</code> Merchant key provided by PayU.                                                                                                         | JPM7Fg               |
| command   | <code>String</code> Must be <code>get_checkout_details</code> (name of the web-service).                                                                   | get_checkout_details |
| var1      | <code>String</code> JSON string containing requestId, transactionDetails, useCase, and optionally customerDetails and filters. See var1 JSON fields below. | See                  |

<br />

### var1 JSON Object fields description (inside var1)

| Parameter          | Description                                                                                                                                                                                                                                                                                                                                                                                       | Example                                        |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| requestId          | <code>String</code> Request ID.                                                                                                                                                                                                                                                                                                                                                                   | 12345678                                       |
| transactionDetails | <code>Object</code> Must contain <code>amount</code> (transaction amount) and optionally <code>txnid</code> (transaction ID).                                                                                                                                                                                                                                                                     | \{"amount": "100.00", "txnid": "TXN123"}       |
| useCase            | <code>Object</code> Flags for which information to return: <code>getExtendedPaymentDetails</code>, <code>getAdditionalCharges</code>, <code>getTaxSpecification</code>, <code>checkDownStatus</code>, <code>checkCustomerEligibility</code>. Optionally <code>filters</code> (e.g. <code>paymentOptions.emi.dc</code>, <code>cc</code>, <code>cardless</code>; <code>paymentOptions.bnpl</code>). | \{"getExtendedPaymentDetails": true}           |
| customerDetails    | <code>Object</code> Optional. Customer info (e.g. <code>mobile</code>) for eligibility checks.                                                                                                                                                                                                                                                                                                    | \{"mobile": "9098765432"}                      |
| filters            | <code>Object</code> Optional. Filter response by <code>paymentOptions</code> (emi.dc, cc, cardless; bnpl). Include "all" for all banks in a category.                                                                                                                                                                                                                                             | \{"paymentOptions": \{"emi": \{"dc": "ICIC"}}} |

### useCase JSON Object Fields Description

| Field                       | Description                                                                                                                                       |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| getExtendedPaymentDetails   | <code>Boolean</code> Set <code>true</code> to check EMI eligibility (mobile/card) and “Buy Now Pay Later” modes; returns title, EMI breakup, etc. |
| getAdditionalCharges        | <code>Boolean</code> Set <code>true</code> to return additional charges for all payment options.                                                  |
| getTaxSpecification         | <code>Boolean</code> Set <code>true</code> to return tax specification from backend for splitting additional charges.                             |
| checkDownStatus             | <code>Boolean</code> Set <code>true</code> to return downtime of payment options.                                                                 |
| checkCustomerEligibility    | <code>Boolean</code> Set <code>true</code> to return customer eligibility.                                                                        |
| checkNTBCustomerEligibility | <code>Boolean</code> Set <code>true</code> to return NTB customer eligibility.                                                                    |

## Sample request

```cUrl
curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
--form 'key="0d5aDh"' \
--form 'command="get_checkout_details"' \
--form 'var1="{\"requestId\":\"413088215\",\"transactionDetails\":{\"amount\":15001.0},\"customerDetails\":{\"mobile\":\"9910522063\"},\"filters\":{\"paymentOptions\":{\"emi\":{\"cardless\":\"all\"},\"bnpl\":\"all\"}},\"useCase\":{\"checkCustomerEligibility\":true,\"checkNTBCustomerEligibility\":true}}"' \
--form 'hash="5c4784472c10fab50be3730a923474925c477e0fdd9a4957d5b0e0469cca3144cb74670ddc5cbe0e3edcbcd04dae64792a93989e99fd17b1cb4ce561659ce24a"'

```

## Sample response

<Callout icon="👍" theme="okay">
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

### Sample response for NTB Customer

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
                                        "BIMAP06": {
                                            "tenure": 6,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                                        "BIMAPAY": {
                                            "tenure": 0,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": false,
                                                "reason": "This mobile number is not eligible. Please change the mobile number."
                                            }
                                        },
                                        "BIMAP09": {
                                            "tenure": 9,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                                        "BIMAP12": {
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
                                "ICICI_CL": {
                                    "tenureOptions": {
                                        "ICICIC12": {
                                            "tenure": 12,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                                        "ICICIC03": {
                                            "tenure": 3,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                                        "ICICIC09": {
                                            "tenure": 9,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                                        "ICICIC06": {
                                            "tenure": 6,
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
                "bnpl": {
                    "all": {
                        "LAZYPAY": {
                            "imageURL": null,
                            "imageUpdatedOn": null,
                            "maximumAmount": null,
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

### Sample response for Existing-to-Bank (ETB) Customer

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
                                        "BIMAP06": {
                                            "tenure": 6,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                                        "BIMAPAY": {
                                            "tenure": 0,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                                        "BIMAP09": {
                                            "tenure": 9,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                                        "BIMAP12": {
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
                                "ICICI_CL": {
                                    "tenureOptions": {
                                        "ICICIC12": {
                                            "tenure": 12,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                                        "ICICIC03": {
                                            "tenure": 3,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                                        "ICICIC09": {
                                            "tenure": 9,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                                        "ICICIC06": {
                                            "tenure": 6,
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
                                "LPEMI": {
                                    "tenureOptions": {
                                        "LPEMI12": {
                                            "tenure": 12,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                                        "LPEMI": {
                                            "tenure": 0,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                                        "LPEMI09": {
                                            "tenure": 9,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                                        "LPEMI03": {
                                            "tenure": 3,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                                        "LPEMI06": {
                                            "tenure": 6,
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
                    }
                },
                "bnpl": {
                    "all": {
                        "LAZYPAY": {
                            "imageURL": null,
                            "imageUpdatedOn": null,
                            "maximumAmount": null,
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

### Failure scenario

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
                                        "BIMAP06": {
                                            "tenure": 6,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                                        "BIMAPAY": {
                                            "tenure": 0,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": false,
                                                "reason": "This mobile number is not eligible. Please change the mobile number."
                                            }
                                        },
                                        "BIMAP09": {
                                            "tenure": 9,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                                        "BIMAP12": {
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
                                "ICICI_CL": {
                                    "tenureOptions": {
                                        "ICICIC12": {
                                            "tenure": 12,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                                        "ICICIC03": {
                                            "tenure": 3,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                                        "ICICIC09": {
                                            "tenure": 9,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": true
                                            }
                                        },
                                        "ICICIC06": {
                                            "tenure": 6,
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
                                "LPEMI": {
                                    "tenureOptions": {
                                        "LPEMI12": {
                                            "tenure": 12,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": false,
                                                "reason": "Use is not eligible for cof product"
                                            }
                                        },
                                        "LPEMI": {
                                            "tenure": 0,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": false,
                                                "reason": "Use is not eligible for cof product"
                                            }
                                        },
                                        "LPEMI09": {
                                            "tenure": 9,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": false,
                                                "reason": "Use is not eligible for cof product"
                                            }
                                        },
                                        "LPEMI03": {
                                            "tenure": 3,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": false,
                                                "reason": "Use is not eligible for cof product"
                                            }
                                        },
                                        "LPEMI06": {
                                            "tenure": 6,
                                            "maximumAmount": null,
                                            "eligibility": {
                                                "status": false,
                                                "reason": "Use is not eligible for cof product"
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
                    }
                },
                "bnpl": {
                    "all": {
                        "LAZYPAY": {
                            "imageURL": null,
                            "imageUpdatedOn": null,
                            "maximumAmount": null,
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
