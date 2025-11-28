---
title: Refund ARN Callback (Example)
excerpt: >-
  **🔔 Refund ARN Callback (Example)**


  ⚠️ **Important:** This is NOT an API you call. This is an example of the
  webhook/callback that PayU sends to YOUR server.


  **🎯 Purpose:**

  - PayU sends this callback when refund is processed

  - Contains ARN (Acquirer Reference Number) for customer tracking

  - Provides refund completion notification

  - Enables automated customer communication


  **🏷️ ARN Details:**

  - **ARN**: Acquirer Reference Number

  - **Purpose**: Unique identifier from acquiring bank

  - **Customer Usage**: Track refund status with their issuing bank

  - **Importance**: Essential for customer service and dispute resolution


  **📋 Callback Parameters:**

  - **TransactionId**: Your merchant transaction ID

  - **PayuID**: PayU's unique transaction identifier

  - **RequestID**: Refund request ID from PayU

  - **RefundToken**: Your refund tracking token

  - **PaymentGateway**: Acquiring bank name

  - **Amount**: Refunded amount

  - **Status**: Refund status (success/failure)

  - **RefundCreationDate**: When refund was initiated

  - **bank_ref_no**: Bank reference number

  - **bank_arn**: 🎯 **Acquirer Reference Number (ARN)**

  - **success_at**: When refund was completed

  - **BaseTxnID**: Reserved for future use


  **🛠️ Implementation Steps:**

  1. **Set up endpoint** on your server (e.g., `/refund-arn-callback`)

  2. **Configure URL** in PayU merchant dashboard

  3. **Handle POST requests** from PayU servers

  4. **Extract ARN** and update your refund records

  5. **Notify customer** about refund completion with ARN

  6. **Log callback** for audit and troubleshooting


  **🔒 Security Considerations:**

  - **IP Whitelist**: Validate callback source (PayU IP ranges)

  - **Authentication**: Implement token-based auth if needed

  - **Logging**: Log all incoming callbacks for audit

  - **Validation**: Verify transaction details before processing

  - **Idempotency**: Handle duplicate callbacks gracefully


  **💬 Customer Communication Example:**

  ```

  "Your refund of ₹100.00 has been processed successfully!

  ARN: ARN12345678901234567890

  You can track this refund with your bank using the ARN number.

  Funds will reflect in your account within 3-7 business days."

  ```


  **🔄 Integration Flow:**

  1. Customer requests refund

  2. You call Refund Transaction API

  3. PayU processes refund

  4. PayU sends this callback with ARN

  5. You update records and notify customer

  6. Customer tracks with bank using ARN
api:
  file: refund_apis.json
  operationId: post_refund-arn-callback
hidden: false
---