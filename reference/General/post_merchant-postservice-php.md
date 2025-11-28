---
title: Check Action Status (PayU ID)
excerpt: >-
  **🔎 Check Action Status (PayU ID)**


  Get complete transaction lifecycle and all actions for a specific PayU
  transaction ID.


  **🎯 Purpose:**

  - Track comprehensive transaction history

  - Get all capture and refund actions

  - Complete transaction reconciliation

  - Customer service support with full context


  **🔧 Parameters:**

  - **var1**: PayU transaction ID (mihpayid)

  - **var2**: `'payuid'` (indicates PayU ID method - required)


  **📊 Returns:**

  - All capture actions with status and amounts

  - All refund actions with status and refund modes

  - Complete transaction action history

  - Action IDs and timestamps

  - Processing gateway information


  **💡 Use Cases:**

  - Customer service inquiries with full transaction context

  - Transaction reconciliation and audit trails

  - Comprehensive status reporting for management

  - Understanding complete transaction lifecycle

  - Dispute resolution with complete history


  **🔍 Comparison with Request ID API:**

  - **Request ID**: Tracks specific actions

  - **PayU ID**: Shows complete transaction history

  - **Request ID**: Real-time action updates

  - **PayU ID**: Comprehensive lifecycle view


  **🔐 Hash Calculation:** `sha512(key|command|var1|salt)`


  **📝 Sample Response:**

  ```json

  {
    "status": 1,
    "msg": "1 out of 1 Transactions Fetched Successfully",
    "transaction_details": {
      "403993715521937565": {
        "131278418": {
          "mihpayid": "403993715521937565",
          "action": "capture",
          "status": "SUCCESS",
          "amt": "100.00",
          "refund_mode": "-"
        },
        "131278422": {
          "mihpayid": "403993715521937565",
          "action": "refund",
          "status": "success",
          "amt": "10.00",
          "refund_mode": "Back to Source"
        }
      }
    }
  }

  ```
api:
  file: refund_apis.json
  operationId: post_merchant-postservice-php
hidden: true
---