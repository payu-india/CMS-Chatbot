---
title: delete_business_member
excerpt: >-
  # **Delete Business Member API Documentation**


  ## **API Overview**


  **Method:** `DELETE`  

  **Endpoint:**
  `/api/v1/merchants/{product_account_uuid}/delete_business_member/{business_member_id}`  

  **Content-Type:** `application/json`  

  **Purpose:** Delete a specific business member from a merchant account.


  ---


  ## **Path Parameters**


  | Parameter | Data Type | Required | Description | Example |

  | --- | --- | --- | --- | --- |

  | `product_account_uuid` | String | ✅ Yes | Unique identifier for the
  merchant's product account. The product_account_uuid is returned in the
  response of the create merchant API | `{{product_account_uuid}}` |

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
  file: >-
    Merchant Onboarding APIs - Business members & signing authority
    details.postman_collection.json
  operationId: >-
    delete_api-v1-merchants-product-account-uuid-delete-business-member-11f0-88aa-173e0da0-888a-02975f21d323
hidden: false
---