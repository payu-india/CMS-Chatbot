---
title: EMI - NTB Flow Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
This section describes how to integrate New-to-Bank (NTB) flow as described in the following steps. These steps will help you check whether the customer is eligible for NTB.

<Cards>
  <Card title=" Step 1: Get Checkout Details" href="#step-1-check-eligibility" icon="fa-rocket">
    Use Get Checkout Details API and look for ntb in the response.
  </Card>

  <Card title="Step 2: Get EMI Checkout Details" href="#step-2-get-emi-checkout-details" icon="fa-code">
    Use the Get EMI Checkout Details API to integrate.
  </Card>
</Cards>

***

## Step 1: Check Eligibility

Use the **Get Checkout Details** API (`get_checkout_details`) to get information for custom checkout pages: payment options, extended payment details (e.g. EMI breakup), additional charges, tax specification, downtime, and optional customer eligibility.

| Environment | URL                                                    |
| :---------- | :----------------------------------------------------- |
| Test        | `https://test.payu.in/merchant/postservice.php?form=2` |
| Production  | `https://info.payu.in/merchant/postservice.php?form=2` |

**Method:** POST (form-encoded)

<Callout icon="👍" theme="okay">
  ###

  **Reference:** For more information on using the **Get Checkout Details** API, refer to [Get Checkout Details API](ref:get-checkout-details-ntb-seamless-journey).
</Callout>

<Accordion title="Request parameters" icon="fa-list">
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
        <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Merchant key provided by PayU.</p></td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>JPM7Fg</p></td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>command<br><code>mandatory</code></p></td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Must be <code>get_checkout_details</code> (name of the web-service).</p></td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>get_checkout_details</p></td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>var1<br><code>mandatory</code></p></td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> JSON string containing requestId, transactionDetails, useCase, and optionally customerDetails and filters. See var1 JSON fields below.</p></td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>See var1 JSON Object fields description</p></td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>hash<br><code>mandatory</code></p></td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The hash must be calculated based on the following logic: sha512(key|command|var1|salt)</p></td>
        <td style="border: 1px solid #ddd; padding: 8px;"></td>
      </tr>
    </tbody>
  </table>

  <Accordion title="var1 JSON Object fields description" icon="fa-table">
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
          <td style="border: 1px solid #ddd; padding: 8px;"><p>requestId</p></td>
          <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Request ID.</p></td>
          <td style="border: 1px solid #ddd; padding: 8px;"><p>12345678</p></td>
        </tr>
        <tr>
          <td style="border: 1px solid #ddd; padding: 8px;"><p>transactionDetails</p></td>
          <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Must contain <code>amount</code> (transaction amount) and optionally <code>txnid</code> (transaction ID).</p></td>
          <td style="border: 1px solid #ddd; padding: 8px;"><p>{"amount": "100.00", "txnid": "TXN123"}</p></td>
        </tr>
        <tr>
          <td style="border: 1px solid #ddd; padding: 8px;"><p>useCase</p></td>
          <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Flags for which information to return: <code>getExtendedPaymentDetails</code>, <code>getAdditionalCharges</code>, <code>getTaxSpecification</code>, <code>checkDownStatus</code>, <code>checkCustomerEligibility</code>. Optionally <code>filters</code> (e.g. <code>paymentOptions.emi.dc</code>, <code>cc</code>, <code>cardless</code>; <code>paymentOptions.bnpl</code>).</p></td>
          <td style="border: 1px solid #ddd; padding: 8px;"><p>{"getExtendedPaymentDetails": true}</p></td>
        </tr>
        <tr>
          <td style="border: 1px solid #ddd; padding: 8px;"><p>customerDetails</p></td>
          <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Optional. Customer info (e.g. <code>mobile</code>) for eligibility checks.</p></td>
          <td style="border: 1px solid #ddd; padding: 8px;"><p>{"mobile": "9098765432"}</p></td>
        </tr>
        <tr>
          <td style="border: 1px solid #ddd; padding: 8px;"><p>filters</p></td>
          <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Optional. Filter response by <code>paymentOptions</code> (emi.dc, cc, cardless; bnpl). Include "all" for all banks in a category.</p></td>
          <td style="border: 1px solid #ddd; padding: 8px;"><p>{"paymentOptions": {"emi": {"dc": "ICIC"}}}</p></td>
        </tr>
      </tbody>
    </table>
  </Accordion>

  <Accordion title="useCase JSON Object Fields Description" icon="fa-table">
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
          <td style="border: 1px solid #ddd; padding: 8px;"><p>getExtendedPaymentDetails</p></td>
          <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> Set <code>true</code> to check EMI eligibility (mobile/card) and "Buy Now Pay Later" modes; returns title, EMI breakup, etc.</p></td>
          <td style="border: 1px solid #ddd; padding: 8px;"></td>
        </tr>
        <tr>
          <td style="border: 1px solid #ddd; padding: 8px;"><p>getAdditionalCharges</p></td>
          <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> Set <code>true</code> to return additional charges for all payment options.</p></td>
          <td style="border: 1px solid #ddd; padding: 8px;"></td>
        </tr>
        <tr>
          <td style="border: 1px solid #ddd; padding: 8px;"><p>getTaxSpecification</p></td>
          <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> Set <code>true</code> to return tax specification from backend for splitting additional charges.</p></td>
          <td style="border: 1px solid #ddd; padding: 8px;"></td>
        </tr>
        <tr>
          <td style="border: 1px solid #ddd; padding: 8px;"><p>checkDownStatus</p></td>
          <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> Set <code>true</code> to return downtime of payment options.</p></td>
          <td style="border: 1px solid #ddd; padding: 8px;"></td>
        </tr>
        <tr>
          <td style="border: 1px solid #ddd; padding: 8px;"><p>checkCustomerEligibility</p></td>
          <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> Set <code>true</code> to return customer eligibility.</p></td>
          <td style="border: 1px solid #ddd; padding: 8px;"></td>
        </tr>
      </tbody>
    </table>
  </Accordion>
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

````
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
                  \}
```
````

  </Callout>

  <Accordion title="Sample response for NTB Customer" icon="fa-reply">
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
                    ....
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

  <Accordion title="Sample response for Existing-to-Bank (ETB) Customer" icon="fa-reply">
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
  </Accordion>

</Accordion>

***

## Step 2: Get EMI Checkout Details

Use the **Get EMI Checkout Details** API to check detailed EMI eligibility for a specific bank/lender and customer (e.g. cardless EMI). In the Step 1 above, if **ntb** JSON object> **eligibility** > **status=true**, you need to follow this step and pass additional details. It returns tenure options, maximum amounts, and eligibility status per tenure.

| Environment | URL                                                             |
| :---------- | :-------------------------------------------------------------- |
| Test        | `https://test.payu.in/info/linkAndPay/get_emi_checkout_details` |
| Production  | `https://info.payu.in/linkAndPay/get_emi_checkout_details`      |

**Method:** POST (JSON body)<br />**Content-Type:** `application/json`

\> 👍
\>
\> **Reference:** For more information on using the **Get EMI Checkout Details** API, refer to [Get EMI Checkout Details API](ref:get-emi-checkout-details-api).

<Accordion title="Authentication (headers)" icon="fa-lock">
  * **Date** (mandatory): Request time in GMT (e.g. `Thu, 17 Feb 2022 08:17:59 GMT`).
  * **Authorization** (mandatory): HMAC-SHA512 signature. Format:\
    `hmac username="<merchant_key>", algorithm="hmac-sha512", headers="date digest", signature="<signature>"`\
    Signing string: `Date + "\n" + Digest`. Use merchant **Salt** as secret.\
    For more information, refer to [Get EMI Checkout Details API > Authorization](ref:get-emi-checkout-details-api#required-parameters-for-calculating-authorization).
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

<br />
