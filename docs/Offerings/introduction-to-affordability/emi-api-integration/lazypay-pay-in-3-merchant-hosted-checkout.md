---
title: LazyPay Pay-in-3 - Merchant Hosted Checkout
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: LazyPay Pay-in-3 - Merchant Hosted Checkout Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Integrate LazyPay Pay-in-3 with Merchant Hosted Checkout
  description: >-
    Check PayInParts / LazyPay Pay-in-3 eligibility using Get Checkout Details,
    then initiate merchant-hosted payment and handle the PayU response.
  robots: index
next:
  description: ''
---

When your customer wants **LazyPay Pay-in-3** (PayInParts), use **Get Checkout Details** (`get_checkout_details`) to retrieve eligible payment options—including the **`payInParts`** catalogue—before you post the transaction to **`/_payment`**. If the customer is eligible, complete the merchant-hosted collect flow and verify the outcome.

<Callout icon="📘" theme="info">
  **Handle Guest Checkout Transaction**: You can handle Guest Checkout transactions for EMI and BNPL integrations where applicable. For more information, refer to [Cards Integration > Handling Guest Checkout Transactions](doc:collect-payments-with-cards-seamless#handling-guest-checkout-transactions).
</Callout>

**Steps to integrate**

<Cards columns={2}>
  <Card title="1. Check PayInParts / Pay-in-3 eligibility" href="#step-1-check-payinparts-and-lazypay-pay-in-3-eligibility">
    Call **Get Checkout Details** with PayInParts filters and interpret the GCD response (including **`LAZYPI3`**) before payment initiation.

    <br />
  </Card>

  <Card title="2. Initiate the Payment" href="#step-2-initiate-the-payment">
    Start the payment process using the merchant-hosted collect flow

    <br />
  </Card>

  <Card title="3. Check the Response from PayU" href="#step-3-check-the-response-from-payu">
    Handle and process the response received from PayU after payment initiation
  </Card>

  <Card title="4. Verify Payment" href="#step-4-verify-payment">
    Confirm the payment status and ensure successful transaction completion

    <br />
  </Card>
</Cards>

## Step 1: Check PayInParts and LazyPay Pay-in-3 eligibility

After you collect the customer’s mobile number and the amount to be paid, call **Get Checkout Details** on **`POST /merchant/postservice?form=2`** with the **`filters.paymentOptions.emi`** structure that includes cardless EMI (and **`payInParts`** when your pack requires Pay-in-parts lenders in the response). The sample request and ETB sample response below match [Get Checkout Details — PayInParts (GCD)](ref:gcd-payinparts-get-checkout-details).


| Environment | URL |
| :-- | :-- |
| Production | `https://info.payu.in/merchant/postservice?form=2` |
| Test | `https://test.payu.in/merchant/postservice?form=2` |


<Accordion title="Request Parameters" icon="fa-info-table">

<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>key<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Merchant key from the PayU Dashboard (masked test style: <code>JP***g</code> in samples).</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>JP***g</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>command<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Must be <code>get_checkout_details</code>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>get_checkout_details</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var1<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> JSON Object containing the fields to check eligibility. For more information, refer to  <a href="#var1-json-fields-description">var1 JSON Fields Description</a></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{"requestId":"abc123","transactionDetails":{"amount":500}}</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>hash<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> <code>sha512(key|command|var1|SALT)</code> — see <a href="doc:hashing-request-and-response">Hashing request and response</a>. Replace <code>{{info_hash}}</code> with the computed digest.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{info_hash}}</p></td>
</tr>
</tbody>
</table>

#### var1 JSON Fields Description
<Accordion title=" var1 JSON Fields Description" icon="fa-info-circle">
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>requestId<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Unique identifier for this Get Checkout Details call.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>transactionDetails<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Transaction context (amount and optional metadata) used for eligibility.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>transactionDetails.source<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Optional payment-source hint; sample uses <code>null</code>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>null</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>transactionDetails.amount<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Number</code> Amount for which eligibility is evaluated.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>transactionDetails.pre_authorize<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Any</code> Pre-authorization context when applicable; sample uses <code>null</code>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>null</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>transactionDetails.additional_charges<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Any</code> Additional charges when applicable; sample uses <code>null</code>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>null</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>useCase<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Flags that control which eligibility checks GCD performs.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>useCase.checkNTBCustomerEligibility<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> When <code>true</code>, requests new-to-bank (NTB) style checks where supported.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>true</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>useCase.checkCustomerEligibility<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> When <code>true</code>, requests standard customer eligibility.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>true</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>useCase.returnUserLimit<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> When <code>true</code>, may return repeat-user / limit information where supported.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>true</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>customerDetails<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Customer attributes required for EMI / Pay-in-parts lookups.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>customerDetails.mobile<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Mobile number used for lender and Pay-in-parts eligibility.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>filters<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Limits which payment options are returned in the GCD payload.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>filters.paymentOptions<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Wrapper for payment-option filters.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>filters.paymentOptions.emi<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> EMI filters (debit card EMI, cardless EMI, Pay-in-parts).</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>filters.paymentOptions.emi.dc<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Debit-card EMI scope; sample uses <code>"all"</code>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>"all"</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>filters.paymentOptions.emi.cardless<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Cardless EMI scope; sample uses <code>"all"</code>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>"all"</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>filters.paymentOptions.emi.payInParts<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Set to <code>"all"</code> when your pack must return PayInParts lenders (for example LazyPay Pay-in-3 / <code>LAZYPI3</code>) in addition to cardless EMI.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>"all"</p></td>
</tr>
</tbody>
</table>
</Accordion>
</Accordion>


<Accordion title="Sample request" icon="fa-info-circle">


```bash
curl --location 'https://info.payu.in/merchant/postservice?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=JP***g' \
--data-urlencode 'command=get_checkout_details' \
--data-urlencode 'var1={"requestId":"9078698a15d746feadcffbdaf979a198","transactionDetails":{"source":null,"amount":16721,"pre_authorize":null,"additional_charges":null},"useCase":{"checkNTBCustomerEligibility":true,"checkCustomerEligibility":true,"returnUserLimit":true},"customerDetails":{"mobile":"9910522063"},"filters":{"paymentOptions":{"emi":{"dc":"all","cardless":"all"}}}}' \
--data-urlencode 'hash={{info_hash}}'
```

To surface **PayInParts** lenders in the response (as in the PRD), add **`"payInParts":"all"`** next to **`dc`** / **`cardless`** inside **`filters.paymentOptions.emi`** when your pack requires it.

</Accordion>

### Sample response 

<Accordion title="ETB — from PayInParts lenders PDF" icon="fa-info-circle">

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

</Accordion>

<Accordion title="GCD response — customer is NTB" icon="fa-info-circle">

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

</Accordion>

<Accordion title="GCD response — customer is not eligible" icon="fa-info-circle">

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

</Accordion>

## Step 2: Initiate the payment

Post the following additional parameters for using the Cardless EMI. Check the response when you try enter the values in API Reference. For complete list of parameters, refer to [Collect Payment API - EMI](ref:_payment_merchant_hosted_emi) for the complete list parameters with **Try It** experience.

### Request Parameters

<Accordion title="Request parameters" icon="fa-info-circle">
  <HTMLBlock>{`
                    <table>
                      <thead>
                        <tr>
                          <th>Parameter</th>
                          <th>Description</th>
                          <th>Example</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td>key <code>mandatory</code></td>
                          <td><code>String</code> Merchant key provided by PayU during onboarding.</td>
                          <td>JP****g</td>
                        </tr>
                        <tr>
                          <td>txnid <code>mandatory</code></td>
                          <td><code>String</code> The transaction ID is a reference number for a specific order that is generated by the merchant.</td>
                          <td></td>
                        </tr>
                        <tr>
                          <td>amount <code>mandatory</code></td>
                          <td><code>String</code> The payment amount for the transaction.</td>
                          <td></td>
                        </tr>
                        <tr>
                          <td>productinfo <code>mandatory</code></td>
                          <td><code>String</code> A brief description of the product.</td>
                          <td></td>
                        </tr>
                        <tr>
                          <td>firstname <code>mandatory</code></td>
                          <td><code>String</code> The first name of the customer.</td>
                          <td>Ashish</td>
                        </tr>
                        <tr>
                          <td>email <code>mandatory</code></td>
                          <td><code>String</code> The email address of the customer.</td>
                          <td>abc@payu.in</td>
                        </tr>
                        <tr>
                          <td>panNumber <code>mandatory for ICICI, HDFC Bank, and Homecredit Cardless EMI. Not mandatory for other banks</code></td>
                          <td><code>String</code> PAN number of the customer.</td>
                          <td>ABCTY1234D</td>
                        </tr>
                        <tr>
                          <td>phone <code>mandatory</code></td>
                          <td><code>String</code> The phone number of the customer.</td>
                          <td></td>
                        </tr>
                        <tr>
                          <td>pg <code>mandatory</code></td>
                          <td><code>String</code> It defines the payment category that the merchant wants the customer to see by default on the PayU's payment page. In this integration, "EMI" must be specified.</td>
                          <td>EMI</td>
                        </tr>
                        <tr>
                          <td>bankcode <code>mandatory</code></td>
                          <td><code>String</code> Post this parameter to identify payment options with unique bank codes and use getEmiAmountAccordingToInterest API to check for EMI code for corresponding tenure. For the list of EMI codes, refer to EMI Codes.</td>
                          <td>HDFCCL06</td>
                        </tr>
                        <tr>
                          <td>ccnum <code>mandatory only for Bajaj Finserv</code></td>
                          <td><code>String</code> Use 13-19 digit card number for credit/debit cards (15 digits for AMEX, 13-19 for Maestro) and validate with LUHN algorithm. Refer to Card Number Formats and display error message on invalid input.</td>
                          <td>5123456789012346</td>
                        </tr>
                        <tr>
                          <td>ccname <code>optional</code></td>
                          <td><code>String</code> This parameter must contain the name on card – as entered by the customer for the transaction.</td>
                          <td>Ashish Kumar</td>
                        </tr>
                        <tr>
                          <td>ccvv <code>optional</code></td>
                          <td><code>String</code> Use 3-digit CVV number for credit/debit cards and 4-digit security code (4DBC/CID) for AMEX cards. Validate with BIN API.</td>
                          <td>123</td>
                        </tr>
                        <tr>
                          <td>ccexpmon <code>optional</code></td>
                          <td><code>String</code> This parameter must contain the card's expiry month – as entered by the user for the transaction. It must always be in 2 digits or in MM format. For months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – It should be 10,11 and 12 respectively.</td>
                          <td>10</td>
                        </tr>
                        <tr>
                          <td>ccexpyr <code>optional</code></td>
                          <td><code>String</code> This parameter must contain the card's expiry year – as entered by the customer for the transaction. It must be of four digits.</td>
                          <td>2021</td>
                        </tr>
                        <tr>
                          <td>furl <code>mandatory</code></td>
                          <td><code>String</code> The success URL, which is the page PayU will redirect to if the transaction is successful.</td>
                          <td></td>
                        </tr>
                        <tr>
                          <td>surl <code>mandatory</code></td>
                          <td><code>String</code> The Failure URL, which is the page PayU will redirect to if the transaction is failed.</td>
                          <td></td>
                        </tr>
                        <tr>
                          <td>hash <code>mandatory</code></td>
                          <td><code>String</code> It is the hash calculated by the merchant. The hash calculation logic is: <code>sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)</code></td>
                          <td></td>
                        </tr>
                        <tr>
                          <td>address1 <code>optional</code></td>
                          <td><code>String</code> The first line of the billing address. <em>For Fraud Detection</em>: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.</td>
                          <td></td>
                        </tr>
                        <tr>
                          <td>address2 <code>optional</code></td>
                          <td><code>String</code> The second line of the billing address.</td>
                          <td></td>
                        </tr>
                        <tr>
                          <td>city <code>optional</code></td>
                          <td><code>String</code> The city where your customer resides as part of the billing address.</td>
                          <td></td>
                        </tr>
                        <tr>
                          <td>state <code>optional</code></td>
                          <td><code>String</code> The state where your customer resides as part of the billing address.</td>
                          <td></td>
                        </tr>
                        <tr>
                          <td>country <code>optional</code></td>
                          <td><code>String</code> The country where your customer resides.</td>
                          <td></td>
                        </tr>
                        <tr>
                          <td>zipcode <code>optional</code></td>
                          <td><code>String</code> Billing address zip code is mandatory for the cardless EMI option. <code>Character Limit</code>-20</td>
                          <td></td>
                        </tr>
                        <tr>
                          <td>udf1 <code>optional</code></td>
                          <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.</td>
                          <td></td>
                        </tr>
                        <tr>
                          <td>udf2 <code>optional</code></td>
                          <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.</td>
                          <td></td>
                        </tr>
                        <tr>
                          <td>udf3 <code>optional</code></td>
                          <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td>
                          <td></td>
                        </tr>
                        <tr>
                          <td>udf4 <code>optional</code></td>
                          <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td>
                          <td></td>
                        </tr>
                        <tr>
                          <td>udf5 <code>optional</code></td>
                          <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td>
                          <td></td>
                        </tr>
                      </tbody>
                    </table>
  `}</HTMLBlock>

  > 📘 Notes for panNumber:
  >
  > * Only 4-digit number of the PAN\*\*: Pass the 4-digit numeral in a sequential order as in the PAN.
  > * This parameter is mandatory for ICICI Bank and HDFC Bank Cardless EMI. Not mandatory for other banks
  > * The data validation performed is either the whole PAN card number or 4-dig-t number of the PAN.
  >   * **Whole PAN card Number**: For validating the whole PAN Card number:
  >     * It should be ten characters long.
  >     * The first five characters should be any upper case alphabets.
  >     * The next four-characters should be any number from 0 to 9.
  >     * The last(tenth) character should be any upper case alphabet.   It should not contain any white spaces.
</Accordion>

<HashingRequestParameters />

### Sample request

<Accordion title="Sample request" icon="fa-info-circle">
  ```curl
  curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d"key=JP***g&txnid=EaE4ZO3vU4iPsp&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=EMI&bankcode=EMI03&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=1234&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=undefined&store_card_token=1234 4567 2456 3566&storecard_token_type=1&additional_info={“last4Digits”: “1234”, “tavv”: “ABCDEFGH”,”trid”:”1234567890”, “tokenRefNo”:”abcde123456”}&hash=fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304"
  ```
  ```javascript
  /**
   * PayU Cardless EMI Payment Integration using Fetch API
   * 
   * IMPORTANT: This should only be executed server-side (e.g., in Node.js), never in the browser,
   * as it contains sensitive payment information.
   */

  // Payment endpoint
  const url = 'https://test.payu.in/_payment';

  // Additional info as a JSON object
  const additionalInfo = {
    "last4Digits": "1234",
    "tavv": "ABCDEFGH",
    "trid": "1234567890",
    "tokenRefNo": "abcde123456"
  };

  // Form data parameters
  const formData = new URLSearchParams();
  formData.append('key', 'JP***g');                  // Your merchant key
  formData.append('txnid', 'EaE4ZO3vU4iPsp');       // Unique transaction ID
  formData.append('amount', '10.00');               // Payment amount
  formData.append('firstname', 'Ashish');           // Customer's name
  formData.append('email', 'test@gmail.com');       // Customer's email
  formData.append('phone', '9876543210');           // Customer's phone
  formData.append('productinfo', 'iPhone');         // Product information
  formData.append('pg', 'EMI');                     // Payment gateway (EMI)
  formData.append('bankcode', 'EMI03');             // Bank code (Cardless EMI provider)
  formData.append('surl', 'https://apiplayground-response.herokuapp.com/'); // Success URL
  formData.append('furl', 'https://apiplayground-response.herokuapp.com/'); // Failure URL
  // Token and card details
  formData.append('ccnum', '1234');                 // Limited card details for verification
  formData.append('ccexpmon', '05');                // Expiry month
  formData.append('ccexpyr', '2022');               // Expiry year 
  formData.append('ccvv', '123');                   // CVV
  formData.append('ccname', 'undefined');           // Cardholder name
  formData.append('store_card_token', '1234 4567 2456 3566'); // Tokenized card
  formData.append('storecard_token_type', '1');     // Token type
  formData.append('additional_info', JSON.stringify(additionalInfo)); // Tokenization details
  // Security hash
  formData.append('hash', 'fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304');

  // Request options
  const requestOptions = {
    method: 'POST',
    headers: {
      'accept': 'application/json',
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: formData
  };

  // Execute the request
  fetch(url, requestOptions)
    .then(response => {
      console.log('Status Code:', response.status);
      return response.text(); // or response.json() if you're sure it returns JSON
    })
    .then(data => {
      console.log('Response:', data);
      // Process payment response here
    })
    .catch(error => {
      console.error('Error:', error);
    });

  ```
  ```python
  import urllib.request
  import urllib.parse
  import json
  from typing import Dict, Any

  def process_cardless_emi_payment() -> Dict[str, Any]:
      """
      Process cardless EMI payment using PayU's Merchant Hosted Checkout
      
      IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
      
      Returns:
          Dictionary with response from PayU API
      """
      # API endpoint
      url = "https://test.payu.in/_payment"
      
      # Additional info as a dictionary
      additional_info = {
          "last4Digits": "1234",
          "tavv": "ABCDEFGH",
          "trid": "1234567890",
          "tokenRefNo": "abcde123456"
      }
      
      # Prepare the form data
      payload = {
          "key": "JP***g",                     # Your merchant key
          "txnid": "EaE4ZO3vU4iPsp",           # Unique transaction ID
          "amount": "10.00",                   # Payment amount
          "firstname": "Ashish",               # Customer's name
          "email": "test@gmail.com",           # Customer's email
          "phone": "9876543210",               # Customer's phone
          "productinfo": "iPhone",             # Product information
          "pg": "EMI",                         # Payment gateway (EMI)
          "bankcode": "EMI03",                 # Bank code (Cardless EMI provider)
          "surl": "https://apiplayground-response.herokuapp.com/", # Success URL
          "furl": "https://apiplayground-response.herokuapp.com/", # Failure URL
          # Token and card details
          "ccnum": "1234",                     # Limited card details for verification
          "ccexpmon": "05",                    # Expiry month
          "ccexpyr": "2022",                   # Expiry year
          "ccvv": "123",                       # CVV
          "ccname": "undefined",               # Cardholder name
          "store_card_token": "1234 4567 2456 3566", # Tokenized card
          "storecard_token_type": "1",         # Token type
          "additional_info": json.dumps(additional_info), # Tokenization details
          # Security hash
          "hash": "fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304"
      }
      
      # Convert dictionary to URL-encoded form data
      data = urllib.parse.urlencode(payload).encode('utf-8')
      
      # Set headers
      headers = {
          "accept": "application/json",
          "Content-Type": "application/x-www-form-urlencoded"
      }
      
      # Create a request object
      req = urllib.request.Request(url, data=data, headers=headers, method="POST")
      
      try:
          # Send the request and get the response
          with urllib.request.urlopen(req) as response:
              response_data = response.read().decode('utf-8')
              
              # Process and return response
              return {
                  "status_code": response.getcode(),
                  "response": response_data
              }
              
      except urllib.error.HTTPError as e:
          # Handle HTTP errors
          error_data = e.read().decode('utf-8')
          return {
              "status_code": e.code,
              "error": e.reason,
              "response": error_data
          }
          
      except Exception as e:
          # Handle other exceptions
          return {
              "status_code": 500,
              "error": str(e),
              "response": "An error occurred during payment processing"
          }

  # Example usage
  if __name__ == "__main__":
      result = process_cardless_emi_payment()
      print(f"Status Code: {result['status_code']}")
      if 'error' in result:
          print(f"Error: {result['error']}")
      print(f"Response: {result['response']}")

  ```
  ```php
  <?php
  /**
   * Process cardless EMI payment using PayU's Merchant Hosted Checkout
   * 
   * IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
   * 
   * @return array Response from PayU API
   */
  function processCardlessEmiPayment() {
      // API endpoint
      $url = "https://test.payu.in/_payment";
      
      // Additional info as an array
      $additionalInfo = [
          "last4Digits" => "1234",
          "tavv" => "ABCDEFGH",
          "trid" => "1234567890",
          "tokenRefNo" => "abcde123456"
      ];
      
      // Prepare the form data
      $payload = [
          "key" => "JP***g",                      // Your merchant key
          "txnid" => "EaE4ZO3vU4iPsp",            // Unique transaction ID
          "amount" => "10.00",                    // Payment amount
          "firstname" => "Ashish",                // Customer's name
          "email" => "test@gmail.com",            // Customer's email
          "phone" => "9876543210",                // Customer's phone
          "productinfo" => "iPhone",              // Product information
          "pg" => "EMI",                          // Payment gateway (EMI)
          "bankcode" => "EMI03",                  // Bank code (Cardless EMI provider)
          "surl" => "https://apiplayground-response.herokuapp.com/", // Success URL
          "furl" => "https://apiplayground-response.herokuapp.com/", // Failure URL
          // Token and card details
          "ccnum" => "1234",                      // Limited card details for verification
          "ccexpmon" => "05",                     // Expiry month
          "ccexpyr" => "2022",                    // Expiry year
          "ccvv" => "123",                        // CVV
          "ccname" => "undefined",                // Cardholder name
          "store_card_token" => "1234 4567 2456 3566", // Tokenized card
          "storecard_token_type" => "1",          // Token type
          "additional_info" => json_encode($additionalInfo), // Tokenization details
          // Security hash
          "hash" => "fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304"
      ];
      
      // Initialize cURL session
      $ch = curl_init($url);
      
      // Set cURL options
      curl_setopt($ch, CURLOPT_POST, true);
      curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
      curl_setopt($ch, CURLOPT_HTTPHEADER, [
          "accept: application/json",
          "Content-Type: application/x-www-form-urlencoded"
      ]);
      
      // For additional security in production
      curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);
      curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);
      
      // Execute the request
      $response = curl_exec($ch);
      $statusCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
      $error = curl_error($ch);
      $errno = curl_errno($ch);
      
      // Close cURL session
      curl_close($ch);
      
      // Handle response
      if ($errno) {
          return [
              "status_code" => 500,
              "error" => $error,
              "response" => "cURL Error: " . $error
          ];
      }
      
      return [
          "status_code" => $statusCode,
          "response" => $response
      ];
  }

  // Example usage
  $result = processCardlessEmiPayment();
  echo "Status Code: " . $result["status_code"] . "\n";
  if (isset($result["error"])) {
      echo "Error: " . $result["error"] . "\n";
  }
  echo "Response: " . $result["response"] . "\n";
  ?>

  ```
  ```java
  import java.io.BufferedReader;
  import java.io.DataOutputStream;
  import java.io.IOException;
  import java.io.InputStreamReader;
  import java.net.HttpURLConnection;
  import java.net.URL;
  import java.net.URLEncoder;
  import java.nio.charset.StandardCharsets;
  import java.util.HashMap;
  import java.util.Map;
  import java.util.StringJoiner;

  /**
   * PayU Cardless EMI Payment Processor for Merchant Hosted Checkout
   * 
   * IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
   */
  public class PayUCardlessEmiPaymentProcessor {
      
      // API endpoint
      private static final String PAYU_TEST_URL = "https://test.payu.in/_payment";
      
      /**
       * Process cardless EMI payment through PayU
       * @return PaymentResponse containing status and response data
       */
      public PaymentResponse processCardlessEmiPayment() {
          try {
              // Initialize URL
              URL url = new URL(PAYU_TEST_URL);
              
              // Additional info JSON
              String additionalInfo = "{"
                  + "\"last4Digits\": \"1234\","
                  + "\"tavv\": \"ABCDEFGH\","
                  + "\"trid\": \"1234567890\","
                  + "\"tokenRefNo\": \"abcde123456\""
                  + "}";
              
              // Prepare form parameters
              Map<String, String> params = new HashMap<>();
              params.put("key", "JP***g");                      // Your merchant key
              params.put("txnid", "EaE4ZO3vU4iPsp");            // Unique transaction ID
              params.put("amount", "10.00");                    // Payment amount
              params.put("firstname", "Ashish");                // Customer's name
              params.put("email", "test@gmail.com");            // Customer's email
              params.put("phone", "9876543210");                // Customer's phone
              params.put("productinfo", "iPhone");              // Product information
              params.put("pg", "EMI");                          // Payment gateway (EMI)
              params.put("bankcode", "EMI03");                  // Bank code (Cardless EMI provider)
              params.put("surl", "https://apiplayground-response.herokuapp.com/"); // Success URL
              params.put("furl", "https://apiplayground-response.herokuapp.com/"); // Failure URL
              // Token and card details
              params.put("ccnum", "1234");                      // Limited card details for verification
              params.put("ccexpmon", "05");                     // Expiry month
              params.put("ccexpyr", "2022");                    // Expiry year
              params.put("ccvv", "123");                        // CVV
              params.put("ccname", "undefined");                // Cardholder name
              params.put("store_card_token", "1234 4567 2456 3566"); // Tokenized card
              params.put("storecard_token_type", "1");          // Token type
              params.put("additional_info", additionalInfo);    // Tokenization details
              // Security hash
              params.put("hash", "fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304");
              
              // Convert parameters to URL-encoded form data
              StringJoiner formData = new StringJoiner("&");
              for (Map.Entry<String, String> entry : params.entrySet()) {
                  formData.add(URLEncoder.encode(entry.getKey(), "UTF-8") + "=" + 
                               URLEncoder.encode(entry.getValue(), "UTF-8"));
              }
              byte[] postData = formData.toString().getBytes(StandardCharsets.UTF_8);
              
              // Configure connection
              HttpURLConnection conn = (HttpURLConnection) url.openConnection();
              conn.setRequestMethod("POST");
              conn.setRequestProperty("accept", "application/json");
              conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
              conn.setRequestProperty("Content-Length", String.valueOf(postData.length));
              conn.setDoOutput(true);
              conn.setConnectTimeout(5000);
              conn.setReadTimeout(15000);
              
              // Send request
              try (DataOutputStream dos = new DataOutputStream(conn.getOutputStream())) {
                  dos.write(postData);
                  dos.flush();
              }
              
              // Get response
              int responseCode = conn.getResponseCode();
              
              // Read response data
              StringBuilder response = new StringBuilder();
              try (BufferedReader reader = new BufferedReader(
                      new InputStreamReader(
                          responseCode >= 400 ? conn.getErrorStream() : conn.getInputStream(), 
                          StandardCharsets.UTF_8))) {
                          
                  String line;
                  while ((line = reader.readLine()) != null) {
                      response.append(line);
                  }
              }
              
              return new PaymentResponse(responseCode, response.toString(), null);
              
          } catch (IOException e) {
              // Handle exception
              return new PaymentResponse(500, null, "Error: " + e.getMessage());
          }
      }
      
      /**
       * Payment response wrapper class
       */
      public static class PaymentResponse {
          private final int statusCode;
          private final String response;
          private final String error;
          
          public PaymentResponse(int statusCode, String response, String error) {
              this.statusCode = statusCode;
              this.response = response;
              this.error = error;
          }
          
          public int getStatusCode() {
              return statusCode;
          }
          
          public String getResponse() {
              return response;
          }
          
          public String getError() {
              return error;
          }
          
          public boolean isSuccess() {
              return statusCode >= 200 && statusCode < 300;
          }
      }
      
      // Example usage
      public static void main(String[] args) {
          PayUCardlessEmiPaymentProcessor processor = new PayUCardlessEmiPaymentProcessor();
          PaymentResponse result = processor.processCardlessEmiPayment();
          
          System.out.println("Status Code: " + result.getStatusCode());
          if (result.isSuccess()) {
              System.out.println("Response: " + result.getResponse());
          } else {
              System.out.println("Error: " + result.getError());
          }
      }
  }

  ```
  ```csharp
  using System;
  using System.Collections.Generic;
  using System.Net.Http;
  using System.Threading.Tasks;
  using System.Text;
  using System.Text.Json;

  namespace PayUCardlessEmiIntegration
  {
      /// <summary>
      /// PayU Cardless EMI Payment Processor for Merchant Hosted Checkout
      /// 
      /// IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
      /// </summary>
      public class PayUCardlessEmiPaymentProcessor
      {
          // API endpoint
          private const string PayuTestUrl = "https://test.payu.in/_payment";
          
          /// <summary>
          /// Process cardless EMI payment through PayU
          /// </summary>
          /// <returns>PaymentResponse containing status and response data</returns>
          public async Task<PaymentResponse> ProcessCardlessEmiPaymentAsync()
          {
              try
              {
                  // Create additional info object
                  var additionalInfo = new
                  {
                      last4Digits = "1234",
                      tavv = "ABCDEFGH",
                      trid = "1234567890",
                      tokenRefNo = "abcde123456"
                  };
                  
                  // Serialize additional info to JSON
                  string additionalInfoJson = JsonSerializer.Serialize(additionalInfo);
                  
                  // Prepare form parameters
                  var formData = new Dictionary<string, string>
                  {
                      { "key", "JP***g" },                       // Your merchant key
                      { "txnid", "EaE4ZO3vU4iPsp" },             // Unique transaction ID
                      { "amount", "10.00" },                     // Payment amount
                      { "firstname", "Ashish" },                 // Customer's name
                      { "email", "test@gmail.com" },             // Customer's email
                      { "phone", "9876543210" },                 // Customer's phone
                      { "productinfo", "iPhone" },               // Product information
                      { "pg", "EMI" },                           // Payment gateway (EMI)
                      { "bankcode", "EMI03" },                   // Bank code (Cardless EMI provider)
                      { "surl", "https://apiplayground-response.herokuapp.com/" }, // Success URL
                      { "furl", "https://apiplayground-response.herokuapp.com/" }, // Failure URL
                      // Token and card details
                      { "ccnum", "1234" },                       // Limited card details for verification
                      { "ccexpmon", "05" },                      // Expiry month
                      { "ccexpyr", "2022" },                     // Expiry year
                      { "ccvv", "123" },                         // CVV
                      { "ccname", "undefined" },                 // Cardholder name
                      { "store_card_token", "1234 4567 2456 3566" }, // Tokenized card
                      { "storecard_token_type", "1" },           // Token type
                      { "additional_info", additionalInfoJson }, // Tokenization details
                      // Security hash
                      { "hash", "fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304" }
                  };
                  
                  // Create HttpClient with timeout
                  using (var httpClient = new HttpClient())
                  {
                      httpClient.Timeout = TimeSpan.FromSeconds(30);
                      
                      // Convert form data to content
                      var content = new FormUrlEncodedContent(formData);
                      
                      // Add headers
                      content.Headers.ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue("application/x-www-form-urlencoded");
                      httpClient.DefaultRequestHeaders.Add("accept", "application/json");
                      
                      // Send POST request
                      var response = await httpClient.PostAsync(PayuTestUrl, content);
                      
                      // Get response content
                      var responseContent = await response.Content.ReadAsStringAsync();
                      
                      return new PaymentResponse(
                          (int)response.StatusCode,
                          responseContent,
                          null
                      );
                  }
              }
              catch (Exception ex)
              {
                  // Handle exception
                  return new PaymentResponse(
                      500,
                      null,
                      $"Error: {ex.Message}"
                  );
              }
          }
          
          /// <summary>
          /// Payment response wrapper class
          /// </summary>
          public class PaymentResponse
          {
              public int StatusCode { get; }
              public string Response { get; }
              public string Error { get; }
              
              public PaymentResponse(int statusCode, string response, string error)
              {
                  StatusCode = statusCode;
                  Response = response;
                  Error = error;
              }
              
              public bool IsSuccess => StatusCode >= 200 && StatusCode < 300;
          }
      }
      
      // Example usage
      class Program
      {
          static async Task Main(string[] args)
          {
              var processor = new PayUCardlessEmiPaymentProcessor();
              var result = await processor.ProcessCardlessEmiPaymentAsync();
              
              Console.WriteLine($"Status Code: {result.StatusCode}");
              if (result.IsSuccess)
              {
                  Console.WriteLine($"Response: {result.Response}");
              }
              else
              {
                  Console.WriteLine($"Error: {result.Error}");
              }
          }
      }
  }

  ```
</Accordion>

## Step 3: Check the response from PayU

<Accordion title="Sample response" icon="fa-info-circle">
  ```
  Array
  (
      [mihpayid] => 403993715523602563
      [status] => success
      [unmappedstatus] => captured
      [key] => smsplus
      [txnid] => v2tWbbdUOuacK9
      [amount] => 20000.00
      [discount] => 0.00
      [net_amount_debit] => 20000.00
      [addedon] => 2021-07-27 11:14:44
      [productinfo] => iPhone
      [firstname] => Ashish
      [lastname] => 
      [address1] => 
      [address2] => 
      [city] => 
      [state] => 
      [country] => 
      [zipcode] => 
      [email] => test@gmail.com
      [phone] => 1234567890
      [udf1] => 
      [udf2] => 
      [udf3] => 
      [udf4] => 
      [udf5] => 
      [udf6] => 
      [udf7] => 
      [udf8] => 
      [udf9] => 
      [udf10] => 
      [hash] => 10f8ead10cdf5f9b7bf9046987de046d63d62d6679dded9d5da8145f459066943570eec4aa184494ae77f99a8bcd55452af3c4eff0d7a7d3ba809c97b7c73045
  [field1] => 0608273386032718000015
      [field2] => 986987
      [field3] => 10.00
      [field4] => 403993715524069222
      [field5] => 100
      [field6] => 02
      [field7] => AUTHPOSITIVE
      [field8] => 
      [field9] => Transaction is Successful    [payment_source] => payu
      [PG_TYPE] => EMI-PG
      [bank_ref_num] => 3d7cc4a4-00c8-4705-a0e7-5708d2c2bb75
      [bankcode]=> EMIA3
      [error] => E000
      [error_Message] => No Error
      [name_on_card] => payu
      [cardnum] =>XXXXXXXXXXXX1234
  )
  ```
</Accordion>

## Step 4: Verify Payment

<Verify_Payment_Tabs />