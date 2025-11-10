---
title: Delete business members API
excerpt: >-
  # **Delete Business Member API Documentation**


  ## **API Overview**


  **Method:** `DELETE`  

  **Endpoint:**
  `/api/v1/merchants/{product_account_uuid}/delete_business_member/{business_member_id}`  

  **Content-Type:** `application/json`  

  **Purpose:** Delete a specific business member from a merchant account.


  ---


  ## **Endpoints**


  | Environment | Endpoint | Description | Usage |

  | --- | --- | --- | --- |

  | **Test** |
  `https://test-partner.payu.in/api/v1/merchants/{product_account_uuid}/delete_business_member/{business_member_id}`
  | Testing/Sandbox environment | Development, testing, and integration purposes
  |

  | **Production** |
  `https://partner.payu.in/api/v1/merchants/{product_account_uuid}/delete_business_member/{business_member_id}`
  | Live production environment | Live transactions and production use |


  ---


  ## **Path Parameters**


  | Parameter | Data Type | Required | Description | Example |

  | --- | --- | --- | --- | --- |

  | `product_account_uuid` | String | ✅ Yes | Unique identifier for the
  merchant's product account. The product_account_uuid is returned as `uuid` in
  the response of the create merchant API | `{{product_account_uuid}}` |

  | `business_member_id` | String | ✅ Yes | Unique identifier for the business
  member to be deleted. The business member id is returned in the submit
  business members API | `11f0-88aa-173e0da0-888a-02975f21d323` |


  ---


  ## **Headers**


  | Header | Data Type | Required | Description | Example |

  | --- | --- | --- | --- | --- |

  | `Authorization` | String | ✅ Yes | Bearer token for authentication. Get the
  token using the GET token API with the scope `refer_merchant` | `Bearer
  {{resellerToken}}` |

  | `Content-Type` | String | ✅ Yes | Request content type | `application/json`
  |


  ## **Expected Responses**


  - **Success:** `200 OK` or `204 No Content`
      
  - **Not Found:** `404 Not Found` (if business_member_id doesn't exist)
      
  - **Unauthorized:** `401 Unauthorized` (if bearer token is invalid)
      
  - **Forbidden:** `403 Forbidden` (if token lacks deletion permissions)
api:
  file: Merchant Onboarding APIs for partners.postman_collection (5).json
  operationId: >-
    delete_api-v1-merchants-11f0-8ee3-5847ce32-bf72-02975f21d323-delete-business-member-business-member-uuid
hidden: false
---