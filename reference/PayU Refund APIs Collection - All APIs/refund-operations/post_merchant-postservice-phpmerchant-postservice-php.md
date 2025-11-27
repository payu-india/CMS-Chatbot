---
title: Get All Refunds from Transaction IDs API
excerpt: |-
  **📋 Get All Refunds from Transaction IDs API**

  Retrieve comprehensive refund details for a specific transaction ID.

  **🎯 Purpose:**
  - Get complete refund history for a transaction
  - Retrieve all refund attempts and their statuses
  - Transaction reconciliation and reporting
  - Customer service support and inquiry handling

  **🔧 Parameters:**
  - **var1**: Transaction ID for refund details
  - **Limitation**: Only one transaction ID per request

  **📊 Returns:**
  - All refund requests for the transaction
  - Refund amounts and current statuses
  - Refund timestamps and processing details
  - Success/failure information with reasons
  - Processing gateway information

  **💡 Use Cases:**
  - Customer inquiries: "What's my refund status?"
  - Reconciling refund records with bank statements
  - Auditing refund transactions for compliance
  - Comprehensive refund reporting for management
  - Troubleshooting refund discrepancies

  **🔐 Hash Calculation:** `sha512(key|command|var1|salt)`

  **🌐 URLs:**
  - **Test:** https://test.payu.in/merchant/postservice.php
  - **Production:** https://info.payu.in/merchant/postservice.php

  **📝 Sample Response:**
  ```json
  {
    "status": 1,
    "msg": "success",
    "result": [
      {
        "request_id": "req_123456789",
        "amount": "100.00",
        "status": "success",
        "created_at": "2025-09-24 10:30:00",
        "processed_at": "2025-09-24 11:45:00"
      }
    ]
  }
  ```
api:
  file: refund_apis.json
  operationId: post_merchant-postservice-phpmerchant-postservice-php
hidden: false
---