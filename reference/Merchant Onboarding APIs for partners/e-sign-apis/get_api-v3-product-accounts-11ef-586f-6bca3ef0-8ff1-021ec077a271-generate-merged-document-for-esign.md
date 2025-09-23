---
title: Generate Merchant Agreement for E-sign API
excerpt: >-
  # **Generate Merged Document for E-Sign API Documentation**


  ## **API Overview**


  **Method:** `GET`  

  **Content-Type:** `application/json`  

  **Purpose:** Generate a merged document for electronic signature (e-sign)
  process for a specific product account.


  **Note that** E-agreement is only generated when the the Bank details, Website
  details ,KYC details, Video KYC details, Business Members Details are
  verified.


  ---


  ## **Endpoints**


  | Environment | Endpoint | Description | Usage |

  | --- | --- | --- | --- |

  | **Test** |
  `https://test-oneapi.payu.in/api/v3/product_accounts/{product_account_uuid}/generate_merged_document_for_esign`
  | Testing/Sandbox environment | Development, testing, and integration purposes
  |

  | **Production** |
  `https://oneapi.payu.in/api/v3/product_accounts/{product_account_uuid}/generate_merged_document_for_esign`
  | Live production environment | Live transactions and production use |


  ---


  ## **Path Parameters**


  | Parameter | Data Type | Required | Description | Example |

  | --- | --- | --- | --- | --- |

  | `product_account_uuid` | String | ✅ Yes | Unique identifier for the merchant
  account. The product account uuid is returned in the response of the create
  merchant API. | `11ef-586f-6bca3ef0-8ff1-021ec077a271` |


  ---


  ## **Headers**


  | Header | Data Type | Required | Description | Example |

  | --- | --- | --- | --- | --- |

  | `Accept` | String | ✅ Yes | Response format specification |
  `application/json` |

  | `Authorization` | String | ✅ Yes | Bearer token for authentication. Use the
  get token API with scope 'client_manage_agreement' to obtain the token. |
  `Bearer 23fe565db8ea0d9f5609852e09e0e69dc8876b076f8c67d29996c99c1c6a7996` |


  ---


  ## **E-Sign Document API Parameter Description Table**


  | Parameter | Field Name | Data Type | Example Value | Description |

  | --- | --- | --- | --- | --- |

  | **Path Parameters** |  |  |  |  |

  | `product_account_uuid` | Product Account UUID | String |
  11ef-586f-6bca3ef0-8ff1-021ec077a271 | Unique identifier for the merchant's
  product account requiring document merging |

  | **Headers** |  |  |  |  |

  | `Accept` | Accept Header | String | application/json | Specifies the
  expected response format from the server |

  | `Authorization` | Bearer Token | String | Bearer {token} | Authentication
  token required for API access and authorization |


  ## **Validation Rules**


  - Product account UUID must be valid and exist in the system
      
  - Account must have completed required document uploads
      
  - Bearer token must have permissions for document generation
      

  ---


  ### **Business Rules**


  | Rule | Description |

  | --- | --- |

  | **Account Eligibility** | Product account must be eligible for e-sign
  document generation |

  | **Document Completeness** | All required documents must be uploaded before
  generation |

  | **Verification Status** | Account must have passed initial verification
  checks |

  | **E-Sign Readiness** | Account must be ready for electronic signature
  process |


  ---


  ## **Expected Responses**


  - **Success:** `200 OK` with merged document details and download/access
  information
      
  - **Unauthorized:** `401 Unauthorized` (if bearer token is invalid)
      
  - **Bad Request:** `400 Bad Request` (if UUID format is invalid)
      
  - `422 Unprocessable Enitity`: "kyc_document": "Agreement Not Found"
      

  ## **Sample Response**


  ``` json

  {
    "kyc_document": {
      "id": 273,
      "document_category_id": 13,
      "document_type_id": null,
      "account_id": null,
      "remarks": null,
      "status": "accepted",
      "uuid": "11eb-de10-3a450888-a354-a483e7015be5",
      "active": true,
      "created_at": "2021-07-06T04:11:24.000Z",
      "updated_at": "2021-07-06T04:14:41.000Z",
      "kyc_document_type": "Agreement",
      "document_format": "Soft Copy",
      "e_stamp_number": null,
      "temp_account_id": null,
      "error": null,
      "record_type": "Merchant",
      "record_id": 1,
      "processed_document": {
        "id": 505,
        "metadata": {
          "identified": true
        },
        "filename": "merged_doc_6.pdf",
        "byte_size": 433824,
        "path": "/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBdG9CIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--206157392f9c6564fe16971b9783ef352030ac40/merged_doc_6.pdf",
        "kyc_document_uuid": "11eb-de10-3a450888-a354-a483e7015be5"
      },
      "document_category_name": "Service Agreement",
      "document_type_name": null,
      "uploaded_documents": [],
      "document_category": {
        "id": 13,
        "name": "Service Agreement",
        "name_on_frontend": "SERVICE_AGREEMENT"
      }
    }
  }

   ```
api:
  file: Enhanced_Merchant_Onboarding_APIs.json
  operationId: >-
    get_api-v3-product-accounts-11ef-586f-6bca3ef0-8ff1-021ec077a271-generate-merged-document-for-esign
hidden: false
---