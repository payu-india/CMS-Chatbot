---
title: Error Codes for Offers Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## **Offers Error Codes**

[block:parameters]
{
  "data": {
    "h-0": "**Scenario**",
    "h-1": "**Response**",
    "0-0": "If amount is missing in cart\\_details",
    "0-1": "{  \n\"status\": 0,  \n\"message\": \"amount is mandatory in cart\\_details.\",  \n\"code\": 400  \n}",
    "1-0": "If items is missing in cart\\_details",
    "1-1": "{  \n\"status\": 0,  \n\"message\": \"items is mandatory in cart\\_details.\",  \n\"code\": 400  \n}",
    "2-0": " If sku\\_details is missing in cart\\_details",
    "2-1": "{  \n\"status\": 0,  \n\"message\": \"sku\\_details is mandatory in cart\\_details.\",  \n\"code\": 400  \n}",
    "3-0": "If sku\\_id is missing in sku\\_details under cart\\_details section",
    "3-1": "{  \n\"status\": 0,  \n\"message\": \"sku\\_id is mandatory in sku\\_details.\",  \n\"code\": 400  \n}",
    "4-0": "If sku\\_name is missing in sku\\_details under cart\\_details section",
    "4-1": "{  \n\"status\": 0,  \n\"message\": \"sku\\_name is mandatory in sku\\_details.\",  \n\"code\": 400  \n}",
    "5-0": "If amount\\_per\\_sku is missing in sku\\_details under cart\\_details section",
    "5-1": "{  \n\"status\": 0,  \n\"message\": \"amount\\_per\\_sku is mandatory in sku\\_details.\",  \n\"code\": 400  \n}",
    "6-0": "If quantity is missing in sku\\_details under cart\\_details section",
    "6-1": "{  \n\"status\": 0,  \n\"message\": \"quantity is mandatory in sku\\_details.\",  \n\"code\": 400  \n}",
    "7-0": "If user\\_token have special characters apart from alphanumeric",
    "7-1": "{  \n\"status\": 0,  \n\"message\": \"user\\_token should be alphanumeric.\",  \n\"code\": 400  \n}",
    "8-0": "Items should match with total sum of sku quantities",
    "8-1": "{  \n\"status\": 0,  \n\"message\": \"Mismatched cart\\_details items and total skus.\",  \n\"code\": 400  \n}",
    "9-0": "Amount in cart\\_details should match with total sum of sku details amount",
    "9-1": "{  \n\"status\": 0,  \n\"message\": \"Mismatched cart\\_details amount and total skus amount.\",  \n\"code\": 400  \n}",
    "10-0": "Amount in cart\\_details should match with invoice amount",
    "10-1": "{  \n\"status\": 0,  \n\"message\": \"Mismatched cart\\_details amount and invoice amount.\",  \n\"code\": 400  \n}"
  },
  "cols": 2,
  "rows": 11,
  "align": [
    null,
    null
  ]
}
[/block]