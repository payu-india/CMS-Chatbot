---
title: verifyEsignOtp
excerpt: >-
  # **E-Sign Merged Document API Documentation**


  ## **API Overview**


  **Method:** `POST`  

  **Content-Type:** `multipart/form-data`  

  **Purpose:** Electronically sign a merged document using OTP verification for
  agreement completion.


  ---


  ## **Endpoints**


  | Environment | Endpoint | Description | Usage |

  | --- | --- | --- | --- |

  | **Test** |
  `https://test-onboarding.payu.in/api/v3/product_accounts/{product_account_uuid}/kyc_documents/{agreement_uuid}/esign_merged_document`
  | Testing/Sandbox environment | Development, testing, and integration purposes
  |

  | **Production** |
  `https://onboarding.payu.in/api/v3/product_accounts/{product_account_uuid}/kyc_documents/{agreement_uuid}/esign_merged_document`
  | Live production environment | Live transactions and production use |


  ---


  ## **Path Parameters**


  | Parameter | Data Type | Required | Description | Example |

  | --- | --- | --- | --- | --- |

  | `product_account_uuid` | String | ✅ Yes | Unique identifier for the product
  account | 13g7-37c9-d86cbbc0-afd2-02975f21e451 |

  | `agreement_uuid` | String | ✅ Yes | Unique identifier for the agreement
  document to be electronically signed. The agreement_uuid is returned in the
  response of the generate merchant agreement API |
  11f0-37c9-d86cbbc0-afd2-02975f21d323 |


  ---


  ## **Headers**


  | Header | Data Type | Required | Description | Example |

  | --- | --- | --- | --- | --- |

  | `Accept` | String | ✅ Yes | Response format specification |
  `application/json` |

  | `Authorization` | String | ✅ Yes | Bearer token for authentication | `Bearer
  {your_token_here}` ⚠️ **Missing in provided curl** |

  | `Cookie` | String | ❌ No | Session cookie for authentication (optional) |
  `_merchant_onboarding_session={session_data}` |


  ---


  ## **Form Data Parameters**


  | Parameter | Data Type | Required | Description | Example |

  | --- | --- | --- | --- | --- |

  | `otp` | String | ✅ Yes | One-Time Password for signatory verification |
  `9144` |


  ---


  ## **E-Sign Merged Document API Parameter Description Table**


  | Parameter | Field Name | Data Type | Example Value | Description |

  | --- | --- | --- | --- | --- |

  | **Path Parameters** |  |  |  |  |

  | `product_account_uuid` | Product Account UUID | String |
  {{productAccountuuid}} | Unique identifier for the merchant's product account
  (environment variable) |

  | `agreement_uuid` | Agreement UUID | String | {{agreement_UUID}} | Unique
  identifier for the agreement document to be electronically signed (environment
  variable). The agreement_uuid is returned in the response of the generate
  merchant agreement API. |

  | **Headers** |  |  |  |  |

  | `Accept` | Accept Header | String | application/json | Specifies the
  expected response format from the server |

  | `Authorization` | Bearer Token | String | Bearer {token} | Authentication
  token required for API access |

  | `Cookie` | Session Cookie | String |
  _merchant_onboarding_session={session_data} | Optional merchant onboarding
  session cookie for additional authentication |

  | **Form Data** |  |  |  |  |

  | `otp` | OTP Code | String | 9144 | One-Time Password received by signatory
  for document verification and signing |


  ---


  ## **Validation Rules**


  - Product account UUID must be valid and exist in the system.
      
  - Agreement UUID must correspond to an existing agreement document ready for
  signing
      
  - Bearer token for authentication
      

  ### **Format Validations**


  | Field | Rule | Description |

  | --- | --- | --- |

  | `product_account_uuid` | UUID Format | Must be a valid UUID format (36
  characters with hyphens) |

  | `agreement_uuid` | UUID Format | Must be a valid agreement document
  identifier in UUID format |

  | `otp` | Numeric Format | Must be 4-6 digit numeric code |

  | `Authorization` | Bearer Token Format | Must include 'Bearer ' prefix
  followed by valid token |


  ---


  ## **Expected Responses**


  - **Success:** `200 OK` with e-signature completion confirmation and signed
  document details
      
  - **Invalid OTP:** `400 Bad Request` (if OTP is incorrect, expired, or already
  used)
      
  - **Unauthorized:** `401 Unauthorized` (if bearer token is invalid or missing)
      

  ## **Sample Response**


  ``` json

  {
      "kyc_document": {
          "id": 33501,
          "document_category_id": 107,
          "document_type_id": null,
          "account_id": null,
          "remarks": null,
          "status": "Approved",
          "uuid": "11f0-37c9-d86cbbc0-afd2-02975f21d323",
          "active": true,
          "created_at": "2025-05-23T11:34:10.000Z",
          "updated_at": "2025-05-23T11:47:30.000Z",
          "kyc_document_type": "Agreement",
          "document_format": "Soft Copy",
          "e_stamp_number": "Dummy-1153",
          "temp_account_id": null,
          "error": null,
          "record_type": null,
          "record_id": null,
          "issue_date": null,
          "expiry_date": null,
          "product_record_id": 24380,
          "product_record_type": "ProductAccount",
          "document_number": null,
          "rekyc_doc": false,
          "auto_fetched": false,
          "processed_document": {
              "id": 41425,
              "metadata": {
                  "identified": true
              },
              "filename": "Service Agreement_33501_e_stamp.pdf",
              "byte_size": 1789261,
              "path": "/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBdWFkIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--cc8cbdf3f5992e2cca7e17a48c17f393a9221507/Service Agreement_33501_e_stamp.pdf",
              "kyc_document_uuid": "11f0-37c9-d86cbbc0-afd2-02975f21d323"
          },
          "document_category_name": "Service Agreement",
          "document_type_name": null,
          "doc_url": "https://test-dms.payu.in/merchants/11f0-37c5-29f10258-afd2-02975f21d323/documents/5eb38555288aa60c3376d9e1984c0b78",
          "uploaded_documents": [],
          "document_category": {
              "id": 107,
              "name": "Service Agreement",
              "name_on_frontend": "SERVICE_AGREEMENT"
          }
      }
  }

   ```
api:
  file: Enhanced_Merchant_Onboarding_APIs.json
  operationId: >-
    post_api-v3-product-accounts-productaccountuuid-kyc-documents-11f0-37c9-d86cbbc0-afd2-02975f21d323-esign-merged-document
hidden: false
---