---
title: Update Merchant API
excerpt: >-
  # **Update Merchant API Documentation**


  ## **API Overview**


  **Method:** `PUT`  

  **Content-Type:** `multipart/form-data`  

  **Purpose:** Update comprehensive merchant information including business
  details, addresses, website information, and bank details


  ---


  ## **Endpoints**


  | Environment | Endpoint | Description | Usage |

  | --- | --- | --- | --- |

  | **Test** |
  `https://test-partner.payu.in/api/v1/merchants/{product_account_uuid}/update`
  | Testing/Sandbox environment | Development, testing, and integration purposes
  |

  | **Production** |
  `https://partner.payu.in/api/v1/merchants/{product_account_uuid}/update` |
  Live production environment | Live transactions and production use |


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

  | `Authorization` | String | ✅ Yes | Bearer token for authentication. |
  `{{vault:bearer-token}}` |


  ---


  ## **Merchant API Parameter Description Table**


  | Parameter | Field Name | Data Type | Example Value | Description |

  | --- | --- | --- | --- | --- |

  | **Basic Information** |  |  |  |  |

  | `merchant[pancard_number]` | PAN Card Number | String | XXXXXXXX1D |
  Merchant's PAN card number for tax identification |

  | `merchant[pancard_name]` | PAN Card Name | String | PAYU PAYMENTS PRIVATE
  LIMITED | Name as registered on the PAN card |

  | `merchant[business_entity]` | Business Entity Type | String | Public Limited
  | Type of business entity (e.g., Private Limited, Public Limited, Partnership)
  |

  | `merchant[business_category]` | Business Category | String | Food &
  Groceries | Primary business category |

  | `merchant[business_sub_category]` | Business Sub-category | String | Meat
  Stores | Specific sub-category within the main business category |

  | `merchant[monthly_expected_volume]` | Monthly Expected Volume | Number |
  78658 | Expected monthly transaction volume or revenue |

  | `merchant[gst_number]` | GST Number | String | XXXXXXXXXXXXXZY | Goods and
  Services Tax registration number |

  | `merchant[integration_type]` | Integration Type | String | ThirdParty | Type
  of integration ("ThirdParty"/"Tools" |

  | `merchant[cin_number]` | CIN Number | String | XXXXXXXXXXXXXXXXX3037 |
  Corporate Identification Number for companies |

  | `merchant[vkyc_exempt_status]` | vKYC Exempt Status | String/Number | "Opted
  for Skip" | Video KYC exemption status (see enum values below) |

  | **Registration Address** |  |  |  |  |

  | `merchant[registration_address][address_line]` | Registration Address Line |
  String | M1703, banashankari | Street address of registered office |

  | `merchant[registration_address][state]` | Registration State | String |
  Karnataka | State where business is registered |

  | `merchant[registration_address][city]` | Registration City | String |
  Bangalore | City where business is registered |

  | `merchant[registration_address][pincode]` | Registration Pincode | String |
  560001 | Postal code of registration address. The allowed character limit is 6
  |

  | **Operating Address** |  |  |  |  |

  | `merchant[operating_address][address_line]` | Operating Address Line |
  String | M1703, Banashankari | Street address of operating location |

  | `merchant[operating_address][state]` | Operating State | String | Karnataka
  | State where business operates |

  | `merchant[operating_address][city]` | Operating City | String | Bangalore |
  City where business operates |

  | `merchant[operating_address][pincode]` | Operating Pincode | String | 560001
  | Postal code of operating address. The allowed character limit is 6 |

  | **Website Details** |  |  |  |  |

  | `merchant[website_details][website_url]` | Website URL | String |
  [www.borosil.com](http://www.borosil.com) | Main website URL |

  | `merchant[website_details][android_url]` | Android App URL | String |
  [www.borosil.com](http://www.borosil.com) | Android application URL or
  download link |

  | `merchant[website_details][ios_url]` | iOS App URL | String |
  [www.borosil.com](http://www.borosil.com) | iOS application URL or download
  link |

  | **Bank Details** |  |  |  |  |

  | `merchant[bank_detail][bank_account_number]` | Bank Account Number | String
  | XXXXXXX4847 | Bank account number for settlements |

  | `merchant[bank_detail][holder_name]` | Account Holder Name | String | PAYU
  PAYMENTS PRIVATE LIMITED | Name of the bank account holder |

  | `merchant[bank_detail][ifsc_code]` | IFSC Code | String | SBIN0000093 |
  Indian Financial System Code for bank identification |


  ## **vKYC Exempt Status Enum Values**


  | Enum Value | Description |

  | --- | --- |

  | `not_applicable` | vKYC exemption is not applicable |

  | `Non face to face` | Non face-to-face verification method |

  | `Physical Verification Completed` | Physical verification has been completed
  |

  | `BH Approval` | 3 Business Head approval obtained |

  | `Whitelabeled` | 4 Whitelabeled merchant status |

  | `Opted for Skip` | **Current Value** - Merchant has opted to skip vKYC |


  ## Recommended order of the details update using the update merchant API


  1. PAN details
      
  2. Bank details
      
  3. GST no
      
  4. CIN no
      
  5. Website details
      

  ## **Validation Rules**


  - If GST number is passed, ensure that address in the GST details match with
  the operating address provided in the API.
      
  - Bank details, once added, can not be updated via API. Reach out to PayU
  merchant care to update the bank details.
      

  ---


  ### **Format Validations**


  | Field | Rule | Description |

  | --- | --- | --- |

  | `pancard_number` | PAN Format | Must follow Indian PAN card format (10
  alphanumeric characters) |

  | `gst_number` | GST Format | Must follow Indian GST number format (15
  characters) |

  | `cin_number` | CIN Format | Must follow Corporate Identity Number format (21
  characters) |

  | `pincode` | Length: 6 digits | Must be exactly 6 numeric characters |

  | `ifsc_code` | IFSC Format | Must follow Indian IFSC code format (11
  characters) |

  | `website_url` | URL Format | Must be a valid URL format |


  ### **Business Rules**


  | Rule | Description |

  | --- | --- |

  | **PAN-Name Match** | PAN card name should match the business entity name |

  | **Address Consistency** | Registration and operating addresses can be
  different |

  | **Bank Account** | Bank account holder name should match PAN card name |

  | **Integration Type** | Must be one of: Tools, ThirdParty |


  ---


  ## **Expected Responses**


  - **Success:** `200 OK` with updated merchant details
      
  - **Validation Error:** `422 Unprocessable Entity` with specific field errors
      
  - **Unauthorized:** `401 Unauthorized` (if bearer token is invalid)
      
  - **Not Found:** `404 Not Found` (if product_account_uuid doesn't exist)
      
  - **Bad Request:** `400 Bad Request` (if required parameters are missing)
api:
  file: Merchant Onboarding APIs for partners.postman_collection (5).json
  operationId: put_api-v1-merchants-11ef-d968-6b042d6c-9b94-02975f21d323-update
hidden: false
---