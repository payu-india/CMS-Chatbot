---
title: NTB Eligibility Check API
deprecated: false
hidden: true
metadata:
  robots: index
---
<br />

The Get Checkout Details (**get_checkout_details**) API is a generic API using which they can get information when you create the custom checkout pages, that will contain the payment options, offers, recommendations, and downtime details. The API provides the following details: 

* **Payment option details**: The extended details for each payment option are available for the merchant.
* **Additional charges**: The additional charges are configured for all payment options.
* eligibility details
* **Downtime details**: The downtime status of the payment options.

<Callout icon="📮" theme="default">
  **Postman Collection**: Access the Get Checkout Details API Postman Collection from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/f1fv12l/getcheckoutdetails-paymodes](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/f1fv12l/getcheckoutdetails-paymodes)
</Callout>

**Environment**

|                        |                                                                                                      |
| :--------------------- | :--------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in-merchant/postservice?form=2](https://test.payu.in-merchant/postservice?form=2) |
| Production Environment | [https://info.payu.in-merchant/postservice?form=2](https://info.payu.in-merchant/postservice?form=2) |

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

<Accordion title="Sample request" icon="fa-code">
  ```cUrl
  curl --location 'https://info.payu.in/merchant/postservice.php?form=2' \
  --form 'key="0d5aDh"' \
  --form 'command="get_checkout_details"' \
  --form 'var1="{\"requestId\":\"9920371372_38\",\"transactionDetails\":{\"amount\":8000},\"useCase\":{\"getExtendedPaymentDetails\":true}}"' \
  --form 'hash="5c4784472c10fab50be3730a923474925c477e0fdd9a4957d5b0e0469cca3144cb74670ddc5cbe0e3edcbcd04dae64792a93989e99fd17b1cb4ce561659ce24a"'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
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
</Accordion>

<Accordion title="Response parameters" icon="fa-book">
  ### JSON Format

  ```bash
  {
      "requestId": "12345678", // random id - mandatory
      "transactionDetails": {
        "amount": 12345.12, // mandatory
        "...": "..."
      },
      "customerDetails": {
        // optional
        "mobile": "9098765432", // optional
        "...": "..."
      },
      "filters": {
        // optional - for limiting the data to be fetched
        "paymentOptions": {
          // optional - if not set, will return all payment options
          "emi": {
            // optional - only the requested fields will be returned
            "dc": "SBIN,KKBK,ICIC", // optional - all means, all options under that category, case insensitive
            "...": "..."
          },
          "...": "..."
        },
        "...": "..."
      },
      "useCase": {
        // optional
        "checkCustomerEligibility": true, // optional - default: false.
        "...": "..."
      }
    }
  ```

  ### JSON Fields Description

  | **JSON Field**                     | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **Example**                                                                                                    |
  | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
  | requestId   **mandatory**          | `String` This parameter must contain the request ID.                                                                                                                                                                                                                                                                                                                                                                                                             | 12345678                                                                                                       |
  | transactionDetails   **mandatory** | `JSON` This parameter must contain the following fields in a JSON format as in the example:      - **amount**: This field contains the transaction amount - ` **txnid**: This fields contains the transaction ID.`                                                                                                                                                                                                                                               |  `{       "amount": 12345.12     }`                                                                            |
  | useCase   **mandatory**            | `JSON` This field contains list of fields for which you want get information. For the list of fields and its description, refer to the [Additional Info for General APIs > useCase JSON Field Description](#usecase-json-field-descriptions). table.                                                                                                                                                                                                             | ` {     "getExtendedPaymentDetails": true     }`                                                               |
  | filters   **optional**             | `JSON`This parameter is used to filter the response of this API based on one or more following in the **paymentOptions** field:      - **cc**: Filter the credit cards. - **dc**: Filter the debit cards. - **nb**: Filter the Net Banking - **emi**:  Filter the EMI options. For list of EMI options, refer to [EMI Options for Get Checkout Details API](#emi-options-for-get-checkout-details-api). - **upi**: Filter the UPI - **cash**: Filter the wallets | `{ "paymentOptions":     {       "emi": {                     "dc": "SBIN,KKBK,ICIC"               }      } }` |

  ### useCase JSON Field Description

  | **useCase Field**                        | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                    |
  | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | getExtendedPaymentDetails   **optional** | `Boolean` This flag is posted as **true** to check EMI eligibility based on mobile number and-or card number depending on the payment method used. Also, checks the eligibility for “Buy Now Pay Later” payment modes.   **Example**: Title, EMI amount breakup, etc details are displayed in the response. For a sample request or response using this field, refer to the [Get Extended Payment Details](#get-extended-payment-details) section. |
  | getAdditionalCharges   **optional**      | `Boolean` This flag is posted as **true** to return the additional charges configured for all payment options. For a sample request or response using this field, refer to the [Get Additional Charges](#get-additional-charges) section.   **Note**: You need to use the **getTaxSpecification** field if you want to calculate the tax split of additional charges on their end.                                                                 |
  | getTaxSpecification` `**optional**       | `Boolean` This flag is posted as **true** to returns the tax specification configured on the backend. Clients can use the result to show the split of additional charges for each payment option. For a sample request or response using this field, refer to the [Get Tax Specification](#get-tax-specification) section.                                                                                                                         |
  | checkDownStatus` `**optional**           | `Boolean` This flag is posted as **true** to return the downtime of the payment options. For a sample request or response using this field, refer to [Check Down Status](#check-down-status) field.                                                                                                                                                                                                                                                |
  | checkCustomerEligibility   **optional**  | `Boolean` This flag is posted as **true** to return the customer eligibility. For a sample request or response using this field, refer to [Check Customer Eligibility](#check-customer-eligibility)  field.                                                                                                                                                                                                                                        |
</Accordion>

<Accordion title="Additional information for request parameters" icon="fa-book">
  | Parameter | Reference                                                                                                                                                                                                                                                                                        |           |        |                 |
  | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------- | ------ | --------------- |
  | **key**   | For more information on how to generate the Key and Salt, refer to any of the following:      - **Production**: [Generate Merchant Key and Salt](#generate-merchant-key-and-salt-on-payu-dashboard)      - **Test**: [Generate Test Merchant Key and Salt](#generate-test-merchant-key-and-salt) |           |        |                 |
  | **hash**  | Hash logic for this API is:   \`sha512(key\\                                                                                                                                                                                                                                                     | command\\ | var1\\ | salt) sha512 \` |
  | var1      | For JSON fields description, refer to [var1 JSON fields description](#var1-JSON-fields-description).                                                                                                                                                                                             |           |        |                 |

  ### var1 JSON fields description

  | **JSON Field**                     | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **Example**                                                                                                    |
  | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
  | requestId   **mandatory**          | `String` This parameter must contain the request ID.                                                                                                                                                                                                                                                                                                                                                                                                             | 12345678                                                                                                       |
  | transactionDetails   **mandatory** | `JSON` This parameter must contain the following fields in a JSON format as in the example:      - **amount**: This field contains the transaction amount - ` **txnid**: This fields contains the transaction ID.`                                                                                                                                                                                                                                               |  `{       "amount": 12345.12     }`                                                                            |
  | useCase   **mandatory**            | `JSON` This field contains list of fields for which you want get information. For the list of fields and its description, refer to the [useCase JSON field descriptions](#usecase-json-field-descriptions). table.                                                                                                                                                                                                                                               | ` {     "getExtendedPaymentDetails": true     }`                                                               |
  | filters   **optional**             | `JSON`This parameter is used to filter the response of this API based on one or more following in the **paymentOptions** field:      - **cc**: Filter the credit cards. - **dc**: Filter the debit cards. - **nb**: Filter the Net Banking - **emi**:  Filter the EMI options. For list of EMI options, refer to [EMI Options for Get Checkout Details API](#emi-options-for-get-checkout-details-api). - **upi**: Filter the UPI - **cash**: Filter the wallets | `{ "paymentOptions":     {       "emi": {                     "dc": "SBIN,KKBK,ICIC"               }      } }` |

  ### useCase JSON field descriptions

  | **useCase Field**                   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                |
  | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | getExtendedPaymentDetails`optional` | `Boolean` This flag is posted as **true** to check EMI eligibility based on mobile number and-or card number depending on the payment method used. Also, checks the eligibility for “Buy Now Pay Later” payment modes. **Example**: Title, EMI amount breakup, etc details are displayed in the response. For a sample request or response using this field, refer to the [Get Extended Payment Details](#getExtendedPaymentDetails)  section. |
  | getAdditionalCharges`optional`      | `Boolean` This flag is posted as **true** to return the additional charges configured for all payment options. For a sample request or response using this field, refer to the [Get Additional Charges](#getAdditionalCharges) section. **Note**: You need to use the **getTaxSpecification** field if you want to calculate the tax split of additional charges on their end.                                                                 |
  | getTaxSpecification`optional`       | `Boolean` This flag is posted as **true** to returns the tax specification configured on the backend. Clients can use the result to show the split of additional charges for each payment option. For a sample request or response using this field, refer to the [Get Tax Specification](#getTaxSpecification) section.                                                                                                                       |
  | checkDownStatus`optional`           | `Boolean` This flag is posted as **true** to return the downtime of the payment options. For a sample request or response using this field, refer to [Check Down Status](#checkDownStatus) field.                                                                                                                                                                                                                                              |
</Accordion>
