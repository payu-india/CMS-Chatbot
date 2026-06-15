---
title: Get EMI/BNPL Checkout Details API - LazyPay Pay-in-3
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Get Checkout Details — PayInParts (GCD)
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Get Checkout Details PayInParts GCD API
  description: >-
    Standalone Get Checkout Details (get_checkout_details) reference for
    PayInParts / LazyPay Pay-in-3 lenders — sample request and GCD response
    from PayInParts PRD materials.
  keywords:
    - get_checkout_details
    - payInParts
    - GCD
    - LAZYPI3
    - LazyPay Pay-in-3
  robots: index
next:
  description: ''
---

This reference describes **`command=get_checkout_details`** on **`POST /merchant/postservice?form=2`** when you use **`var1`** filters for **cardless EMI** and **PayInParts** lenders (including **LazyPay Pay-in-3**). It is **standalone** for PayInParts / Pay-in-3 workstreams only.

**Source for sample response:** Transcribed from **`Seamless-Response for GCD and GECD for PayInParts Lenders-120626-053241.pdf`** — same JSON as in [`PRDs/Lazypay/seamless-response-gcd-gecd-payinparts-lenders.md`](../../../../PRDs/Lazypay/seamless-response-gcd-gecd-payinparts-lenders.md) (section **GCD response — customer is ETB**).

## Endpoint

| Environment | URL |
| :-- | :-- |
| Production | `https://info.payu.in/merchant/postservice?form=2` |
| Test | `https://test.payu.in/merchant/postservice?form=2` |

Some gateways still accept **`postservice.php?form=2`**. Confirm with your **PayU Key Account Manager (KAM)**.

## Form body parameters

| Field | Description |
| :-- | :-- |
| **key** | Merchant key from the PayU Dashboard (masked test style: **`JP***g`** in samples). |
| **command** | Must be **`get_checkout_details`**. |
| **var1** | JSON string: **`requestId`**, **`transactionDetails`** (e.g. **`amount`**, **`source`**, **`pre_authorize`**, **`additional_charges`**), **`useCase`** (e.g. **`checkCustomerEligibility`**, **`checkNTBCustomerEligibility`**, **`returnUserLimit`**), **`customerDetails`** (e.g. **`mobile`**), **`filters.paymentOptions.emi`** (e.g. **`dc`**, **`cardless`**, and **`payInParts`** when you need Pay-in-parts lenders in the response). |
| **hash** | **`sha512(key|command|var1|SALT)`** — see [Hashing request and response](doc:hashing-request-and-response). Replace **`{{info_hash}}`** with the computed digest. |

Do **not** send browser **`Cookie`** headers on server-to-server calls.

## Sample request

The following matches the integration sample you provided (**`Cookie`** omitted; **`key`** shown as **`JP***g`** like other PayU API reference pages—substitute your real merchant key if different), with **`hash`** templated.

```bash
curl --location 'https://info.payu.in/merchant/postservice?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=JP***g' \
--data-urlencode 'command=get_checkout_details' \
--data-urlencode 'var1={"requestId":"9078698a15d746feadcffbdaf979a198","transactionDetails":{"source":null,"amount":16721,"pre_authorize":null,"additional_charges":null},"useCase":{"checkNTBCustomerEligibility":true,"checkCustomerEligibility":true,"returnUserLimit":true},"customerDetails":{"mobile":"9910522063"},"filters":{"paymentOptions":{"emi":{"dc":"all","cardless":"all"}}}}' \
--data-urlencode 'hash={{info_hash}}'
```

To surface **PayInParts** lenders in the response (as in the PRD), add **`"payInParts":"all"`** next to **`dc`** / **`cardless`** inside **`filters.paymentOptions.emi`** when your pack requires it.

## Sample response (ETB — from PayInParts lenders PDF)

**Scenario:** GCD response when the customer is **ETB** (`httpCode` **200**, `status` **1**). The payload is large; structure below is **verbatim** from the PRD transcription (cardless EMI catalogue + **`payInParts`** block including **`LAZYPI3`**).

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

## GCD response — customer is NTB

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

## GCD response — customer is not eligible

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
