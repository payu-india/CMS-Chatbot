---
title: TWID Pay Redemption Integraiton
deprecated: false
hidden: true
metadata:
  robots: index
---
Integrate TWID pay to enable customers to redeem their TWID loyalty points during checkout. Follow these sequential steps to implement a complete TWID pay solution.

## **🔐 Authentication Method**

TWID pay APIs use **header-based authentication**. Include the following headers in all API requests:

```http
Authorization: Bearer {API_KEY}
Content-Type: application/json
X-Merchant-Key: {MERCHANT_KEY}
```

***

<Accordion title="Step 1: Fetch Balance API" icon="fa-wallet">
  Get the available TWID points balance for a specific customer before initiating any redemption process.
  The **Fetch Balance** API retrieves the current TWID points balance for a customer using their mobile number or user identifier.

  <Accordion title="Request Parameters" icon="fa-table">
<HTMLBlock>{`

<table> <thead> <tr> <th>Parameter</th> <th>Description</th> <th>Example</th> </tr> </thead> <tbody> <tr> <td>mobile <code>mandatory</code></td> <td>Customer's registered mobile number (10 digits). <code>String</code></td> <td>9876543210</td> </tr> <tr> <td>timestamp <code>mandatory</code></td> <td>Request timestamp in ISO 8601 format. <code>String</code></td> <td>2023-12-25T10:30:00Z</td> </tr> <tr> <td>userId <code>optional</code></td> <td>Alternative customer identifier. <code>String</code></td> <td>user_123456</td> </tr> <tr> <td>email <code>optional</code></td> <td>Customer's registered email address. <code>String</code></td> <td>customer@example.com</td> </tr> </tbody> </table> `}</HTMLBlock>
  </Accordion>

  <Accordion title="Sample Request/Response" icon="fa-code">
    **Sample Request:**

    ```json
    POST /api/twid/fetch-balance
    Headers:
    Authorization: Bearer your_api_key_here
    Content-Type: application/json
    X-Merchant-Key: JPM7Fg

    {
      "mobile": "9876543210",
      "timestamp": "2024-09-25T09:00:00Z",
      "email": "customer@example.com"
    }
    ```

    **Sample Success Response:**

    ```json
    {
      "status": "success",
      "message": "Balance fetched successfully",
      "data": {
        "mobile": "9876543210",
        "availableBalance": 2500,
        "currency": "TWID_POINTS",
        "expiryDate": "2024-12-31",
        "lastUpdated": "2024-09-25T08:45:00Z"
      }
    }
    ```

    **Sample Error Response:**

    ```json
    {
      "status": "failure",
      "message": "Customer not found",
      "errorCode": "CUSTOMER_NOT_FOUND",
      "data": null
    }
    ```
  </Accordion>
</Accordion>

***

<Accordion title="Step 2: Enquire Transaction API (Optional)" icon="fa-search">
  Query the status and details of TWID point transactions for tracking and reconciliation purposes.
    The **Enquire Transaction API** is an optional but recommended step for transaction management.

  <Accordion title="Request Parameters" icon="fa-table">
<HTMLBlock>{`

<table> <thead> <tr> <th>Parameter</th> <th>Description</th> <th>Example</th> </tr> </thead> <tbody> <tr> <td>transactionId <code>mandatory</code></td> <td>Unique transaction identifier from previous API calls. <code>String</code></td> <td>TXN_20231225_ABC123</td> </tr> <tr> <td>timestamp <code>mandatory</code></td> <td>Request timestamp in ISO 8601 format. <code>String</code></td> <td>2023-12-25T14:30:00Z</td> </tr> <tr> <td>mobile <code>optional</code></td> <td>Customer's mobile number for additional validation. <code>String</code></td> <td>9876543210</td> </tr> <tr> <td>includeDetails <code>optional</code></td> <td>Include detailed transaction breakdown (default: false). <code>Boolean</code></td> <td>true</td> </tr> </tbody> </table> `}</HTMLBlock>
  </Accordion>

  <Accordion title="Sample Request/Response" icon="fa-code">
    **Sample Request:**

    ```json
    POST /api/twid/enquire-transaction
    Headers:
    Authorization: Bearer your_api_key_here
    Content-Type: application/json
    X-Merchant-Key: JPM7Fg

    {
      "transactionId": "TXN_TWID_1695456789123",
      "timestamp": "2024-09-25T09:00:00Z",
      "mobile": "9876543210",
      "includeDetails": true
    }
    ```

    **Sample Success Response:**

    ```json
    {
      "status": "success",
      "message": "Transaction details retrieved successfully",
      "data": {
        "transactionId": "TXN_TWID_1695456789123",
        "status": "COMPLETED",
        "type": "REDEMPTION",
        "mobile": "9876543210",
        "pointsRedeemed": 500,
        "equivalentAmount": 500.00,
        "currency": "INR",
        "transactionDate": "2024-09-25T08:30:00Z",
        "details": {
          "categoryUsed": "CASHBACK",
          "balanceBefore": 2500,
          "balanceAfter": 2000,
          "merchantTransactionId": "MERCH_TXN_456789"
        }
      }
    }
    ```

    **Sample Pending Response:**

    ```json
    {
      "status": "success",
      "message": "Transaction is in progress",
      "data": {
        "transactionId": "TXN_TWID_1695456789123",
        "status": "PENDING",
        "type": "HOLD",
        "estimatedCompletionTime": "2024-09-25T09:05:00Z"
      }
    }
    ```
  </Accordion>
</Accordion>

***

<Accordion title="Step 3: Hold TWID Points API" icon="fa-lock">
  Reserve TWID points temporarily to ensure availability during the checkout process without immediate redemption.
  The Hold TWID Points API creates a temporary reservation of points to secure them during checkout.

  <Accordion title="Request Parameters" icon="fa-table">
<HTMLBlock>{`

<table> <thead> <tr> <th>Parameter</th> <th>Description</th> <th>Example</th> </tr> </thead> <tbody> <tr> <td>mobile <code>mandatory</code></td> <td>Customer's registered mobile number (10 digits). <code>String</code></td> <td>9876543210</td> </tr> <tr> <td>pointsToHold <code>mandatory</code></td> <td>Number of TWID points to hold/reserve. <code>Integer</code></td> <td>100</td> </tr> <tr> <td>merchantTransactionId <code>mandatory</code></td> <td>Unique transaction ID from merchant system. <code>String</code></td> <td>MERCH_TXN_20231225_001</td> </tr> <tr> <td>timestamp <code>mandatory</code></td> <td>Request timestamp in ISO 8601 format. <code>String</code></td> <td>2023-12-25T14:30:00Z</td> </tr> <tr> <td>holdDuration <code>optional</code></td> <td>Hold duration in minutes (default: 15, max: 30). <code>Integer</code></td> <td>20</td> </tr> <tr> <td>categoryPreference <code>optional</code></td> <td>Preferred point category to hold ["CASHBACK", "REWARDS", "PROMOTIONAL"]. <code>String</code></td> <td>CASHBACK</td> </tr> </tbody> </table> `}</HTMLBlock>

  </Accordion>

  <Accordion title="Sample Request/Response" icon="fa-code">
    **Sample Request:**

    ```json
    POST /api/twid/hold-points
    Headers:
    Authorization: Bearer your_api_key_here
    Content-Type: application/json
    X-Merchant-Key: JPM7Fg

    {
      "mobile": "9876543210",
      "pointsToHold": 500,
      "merchantTransactionId": "MERCH_TXN_456789",
      "timestamp": "2024-09-25T09:00:00Z",
      "holdDuration": 20,
      "categoryPreference": "CASHBACK"
    }
    ```

    **Sample Success Response:**

    ```json
    {
      "status": "success",
      "message": "Points held successfully",
      "data": {
        "holdId": "HOLD_TWID_1695456789456",
        "mobile": "9876543210",
        "pointsHeld": 500,
        "categoryUsed": "CASHBACK",
        "holdExpiry": "2024-09-25T09:20:00Z",
        "availableBalance": 2000,
        "merchantTransactionId": "MERCH_TXN_456789"
      }
    }
    ```

    **Sample Insufficient Balance Response:**

    ```json
    {
      "status": "failure",
      "message": "Insufficient TWID points balance",
      "errorCode": "INSUFFICIENT_BALANCE",
      "data": {
        "requestedPoints": 500,
        "availableBalance": 300,
        "shortfall": 200
      }
    }
    ```
  </Accordion>
</Accordion>

***

<Accordion title="Step 4: Redeem TWID Points API" icon="fa-gift">
  Complete the final redemption of held TWID points and convert them to payment value for the transaction.

  <Accordion title="Purpose of API" icon="fa-info-circle">
    The Redeem TWID Points API finalizes the point redemption process and completes the payment. This final step:

    • **Converts points to payment** - Transforms held TWID points into actual payment value
    • **Completes the transaction** - Finalizes the redemption process and updates customer balance
    • **Generates receipt data** - Provides transaction confirmation and receipt information
    • **Updates loyalty records** - Reflects the redemption in customer's TWID account
    • **Enables split settlement** - Coordinates with other payment methods for hybrid transactions
    • **Triggers notifications** - Sends confirmation to customer via SMS/email
    • **Supports refund scenarios** - Enables point restoration if transaction needs to be reversed
  </Accordion>

  <Accordion title="Request Parameters" icon="fa-table">
<HTMLBlock>{`

<table> <thead> <tr> <th>Parameter</th> <th>Description</th> <th>Example</th> </tr> </thead> <tbody> <tr> <td>holdId <code>mandatory</code></td> <td>Hold ID received from Hold TWID Points API. <code>String</code></td> <td>HOLD_20231225_XYZ789</td> </tr> <tr> <td>merchantTransactionId <code>mandatory</code></td> <td>Unique transaction ID from merchant system. <code>String</code></td> <td>MERCH_TXN_20231225_001</td> </tr> <tr> <td>timestamp <code>mandatory</code></td> <td>Request timestamp in ISO 8601 format. <code>String</code></td> <td>2023-12-25T14:30:00Z</td> </tr> <tr> <td>actualRedemptionAmount <code>optional</code></td> <td>Actual points to redeem (≤ held points). <code>Integer</code></td> <td>75</td> </tr> <tr> <td>orderDetails <code>optional</code></td> <td>Order information for receipt and records. <code>Object</code></td> <td>{"orderId": "ORD123", "amount": 500}</td> </tr> </tbody> </table> `}</HTMLBlock>
  </Accordion>

  <Accordion title="Sample Request/Response" icon="fa-code">
    **Sample Request:**

    ```json
    POST /api/twid/redeem-points
    Headers:
    Authorization: Bearer your_api_key_here
    Content-Type: application/json
    X-Merchant-Key: JPM7Fg

    {
      "holdId": "HOLD_TWID_1695456789456",
      "merchantTransactionId": "MERCH_TXN_456789",
      "timestamp": "2024-09-25T09:05:00Z",
      "actualRedemptionAmount": 500,
      "orderDetails": {
        "orderId": "ORD_123456",
        "orderValue": 1000.00,
        "currency": "INR"
      }
    }
    ```

    **Sample Success Response:**

    ```json
    {
      "status": "success",
      "message": "Points redeemed successfully",
      "data": {
        "redemptionId": "REDEEM_TWID_1695456789789",
        "holdId": "HOLD_TWID_1695456789456",
        "mobile": "9876543210",
        "pointsRedeemed": 500,
        "redemptionValue": 500.00,
        "currency": "INR",
        "newBalance": 2000,
        "transactionDate": "2024-09-25T09:05:00Z",
        "receipt": {
          "receiptNumber": "TWID_RCP_456789",
          "customerCopy": "Points redeemed: 500 | Value: ₹500.00 | Remaining balance: 2000"
        }
      }
    }
    ```

    **Sample Hold Expired Response:**

    ```json
    {
      "status": "failure",
      "message": "Hold has expired",
      "errorCode": "HOLD_EXPIRED",
      "data": {
        "holdId": "HOLD_TWID_1695456789456",
        "expiredAt": "2024-09-25T09:20:00Z",
        "currentTime": "2024-09-25T09:25:00Z"
      }
    }
    ```
  </Accordion>
</Accordion>

***

## Integration Checklist

Before going live with TWID pay integration, ensure you have completed:

* ✅ **Authentication Setup**: Configured API keys and merchant credentials
* ✅ **Step 1**: Implemented Fetch Balance API for balance validation
* ✅ **Step 2**: Integrated Fetch Balance All API for comprehensive balance display
* ✅ **Step 3**: Added Enquire Transaction API for transaction tracking (recommended)
* ✅ **Step 4**: Implemented Hold TWID Points API for secure point reservation
* ✅ **Step 5**: Integrated Redeem TWID Points API for final redemption
* ✅ **Error Handling**: Added comprehensive error handling for all API responses
* ✅ **Timeout Management**: Implemented proper timeout handling for hold operations
* ✅ **Testing**: Completed integration testing in sandbox environment

## Security Best Practices

* **API Key Security**: Store API keys securely and never expose in client-side code
* **Header Authentication**: Always include proper authentication headers
* **Secure Storage**: Never store customer mobile numbers or transaction data in logs
* **Timeout Handling**: Implement proper timeout for hold operations (max 30 minutes)
* **Error Logging**: Log errors without exposing sensitive customer information
* **HTTPS Only**: Ensure all API calls are made over secure HTTPS connections