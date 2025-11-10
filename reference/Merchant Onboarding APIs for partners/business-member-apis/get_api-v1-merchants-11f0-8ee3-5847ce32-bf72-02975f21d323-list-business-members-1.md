---
title: List Business members API
excerpt: >-
  # **List Business Members API Documentation**


  ## **API Overview**


  **Method:** `GET`  

  **Endpoint:**
  `/api/v1/merchants/{product_account_uuid}/list_business_members`  

  **Content-Type:** `application/json`  

  **Purpose:** Retrieve a list of all business members associated with a
  merchant account


  ---


  ## **Path Parameters**


  | Parameter | Data Type | Required | Description | Example |

  | --- | --- | --- | --- | --- |

  | `product_account_uuid` | String | ✅ Yes | Unique identifier for the
  merchant's product account. The product_account_uuid is returned as `uuid` in
  the response of the create merchant API | `{{product_account_uuid}}` |


  ---


  ## **Headers**


  | Header | Data Type | Required | Description | Example |

  | --- | --- | --- | --- | --- |

  | `Authorization` | String | ✅ Yes | Bearer token for authentication. Get the
  token using the GET token API with the scope `refer_merchant` | `Bearer
  {{resellerToken}}` |

  | `Content-Type` | String | ✅ Yes | Request content type | `application/json`
  |


  ---


  ## **Response fields**


  | Field | Data Type | Format | Description |

  | --- | --- | --- | --- |

  | `id` | String | UUID | Unique identifier for the business member |

  | `name` | String | Full name | Full name of the business member |

  | `designation` | String | Job title | Position or designation in the company
  |

  | `doj` | String | MM/YYYY | Date of joining |

  | `dob` | String | DD/MM/YYYY | Date of birth |

  | `pincode` | String | 6 digits | Postal code |

  | `pan_number` | String | PAN format | PAN card number (masked for security) |

  | `created_at` | String | ISO 8601 | Timestamp when record was created |

  | `updated_at` | String | ISO 8601 | Timestamp when record was last updated |


  ---


  ## **Authentication**


  - **Required:** Bearer token authentication
      
  - **Header:** `Authorization: Bearer {token}`
      

  ---


  ## **Expected Responses**


  - **Success:** `200 OK` with business members data
      
  - **Empty List:** `200 OK` with empty `business_members` array if no members
  exist
      
  - **Unauthorized:** `401 Unauthorized` (if bearer token is invalid)
      
  - **Not Found:** `404 Not Found` (if product_account_uuid doesn't exist)
      
  - **Forbidden:** `403 Forbidden` (if token lacks read permissions)
      

  ---
api:
  file: Merchant Onboarding APIs for partners.postman_collection (5).json
  operationId: >-
    get_api-v1-merchants-11f0-8ee3-5847ce32-bf72-02975f21d323-list-business-members
hidden: false
---