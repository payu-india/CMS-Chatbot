---
title: Send OTp to signatory Email API
excerpt: >-
  # **Send Signatory OTP API Documentation**


  ## **API Overview**


  **Method:** `POST`  

  **Content-Type:** `application/json`  

  **Purpose:** Send OTP (One-Time Password) to signatory for agreement document
  verification and authentication process. The OTP is send to the registered
  email of the authorised signatory.


  ---


  ## **Endpoints**


  | Environment | Endpoint | Description | Usage |

  | --- | --- | --- | --- |

  | **Test** |
  `https://test-onboarding.payu.in/api/v3/product_accounts/{product_account_uuid}/kyc_documents/{agreement_uuid}/send_signatory_otp`
  | Testing/Sandbox environment | Development, testing, and integration purposes
  |

  | **Production** |
  `https://onboarding.payu.in/api/v3/product_accounts/{product_account_uuid}/kyc_documents/{agreement_uuid}/send_signatory_otp`
  | Live production environment | Live transactions and production use |


  ---


  ## **Path Parameters**


  | Parameter | Data Type | Required | Description | Example |

  | --- | --- | --- | --- | --- |

  | `product_account_uuid` | String | ✅ Yes | Unique identifier for the product
  account. The product_account_uuid is returned the response of the create
  merchant API | 14d8-37c9-d86cbbc0-afd2-02674f21d454 |

  | `agreement_uuid` | String | ✅ Yes | Unique identifier for the agreement
  document requiring signatory verification. Unique identifier for the agreement
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


  ## **Signatory OTP API Parameter Description Table**


  | Parameter | Field Name | Data Type | Example Value | Description |

  | --- | --- | --- | --- | --- |

  | **Path Parameters** |  |  |  |  |

  | `product_account_uuid` | Product Account UUID | String |
  14d8-37c9-d86cbbc0-afd2-02674f21d454 | Unique identifier for the product
  account. The product_account_uuid is returned the response of the create
  merchant API |

  | `agreement_uuid` | Agreement UUID | String |
  11f0-37c9-d86cbbc0-afd2-02975f21d323 | Unique identifier for the agreement
  document requiring signatory verification. Unique identifier for the agreement
  document to be electronically signed. The agreement_uuid is returned in the
  response of the generate merchant agreement API. |

  | **Headers** |  |  |  |  |

  | `Accept` | Accept Header | String | application/json | Specifies the
  expected response format from the server |

  | `Authorization` | Bearer Token | String | Bearer {token} | Authentication
  token required for API access |


  ---



  ## **Validation Rules**


  - Product account UUID must be valid and referred by the partner. 
      
  - Agreement UUID must correspond to an existing agreement document
          
  - Bearer token or valid session cookie required for authentication
      
  ---


  ## **Expected Responses**


  - **Success:** `200 OK` with OTP sent confirmation.
      
  - **Unauthorized:** `401 Unauthorized` (if bearer token is invalid or missing)
      
  - **Not Found:** `404 Not Found` (if product_account_uuid or agreement_uuid
  doesn't exist)
      

  ## **Sample Response**


  ``` json

  {
      "otp": {
          "message": "sent"
      }
  }

   ```
api:
  file: Enhanced_Merchant_Onboarding_APIs.json
  operationId: >-
    post_api-v3-product-accounts-productaccountuuid-kyc-documents-11f0-37c9-d86cbbc0-afd2-02975f21d323-send-signatory-otp
hidden: false
---