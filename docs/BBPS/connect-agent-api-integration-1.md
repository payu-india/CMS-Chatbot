---
title: Connect Agent API Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
This section walks you through the complete integration workflow for implementing BBPS bill payments using PayU's Connect Agent APIs.

<Cards columns={3}>
  <Card title="1. Generate Access Token" href="#step-1-generate-access-token">
    Authenticate and obtain OAuth token for API access

    <br />
  </Card>

  <Card title="2. Fetch Biller Information" href="#step-2-fetch-biller-information">
    Get biller categories and biller details from MDM

    <br />
  </Card>

  <Card title="3. Fetch Bill Details" href="#step-3-fetch-bill-details">
    Retrieve customer bill information from the biller

    <br />
  </Card>

  <Card title="4. Validate Payment" href="#step-4-validate-payment-optional">
    Validate payment details before processing (if required)

    <br />
  </Card>

  <Card title="5. Process Payment" href="#step-5-process-payment">
    Submit bill payment transaction to the biller

    <br />
  </Card>

  <Card title="6. Verify the Transaction" href="#step-6-verify-transaction-status">
    Check payment status and handle responses

    <br />
  </Card>
</Cards>

***

<br />

## Step 1: Generate Access Token

<br />

Generate an OAuth 2.0 access token to authenticate all subsequent API calls. The token is valid for 2 hours.

<Accordion title="Request parameters" icon="fa-table">
  | Parameter                       | Description                                      | Example                          |
  | :------------------------------ | :----------------------------------------------- | :------------------------------- |
  | client\_id<br />`mandatory`     | `String` - Unique client ID shared by PayU       | client\_123                      |
  | client\_secret<br />`mandatory` | `String` - Secret key shared by PayU             | secret\_xyz                      |
  | grant\_type<br />`mandatory`    | `String` - Grant type (use client\_credentials)  | client\_credentials              |
  | scope<br />`mandatory`          | `String` - Space-separated scopes for API access | read\_bills create\_transactions |
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl -X POST \
    https://uat-accounts.payu.in/oauth/token \
    -H 'content-type: application/x-www-form-urlencoded' \
    -d 'client_id=<client_id>&client_secret=<client_secret>&grant_type=client_credentials&scope=read_bills read_billers create_transactions'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-check">
  ```json
  {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "Bearer",
    "expires_in": 7200,
    "scope": "read_bills read_billers create_transactions",
    "created_at": 1623456789
  }
  ```
</Accordion>

***

<br />

## Step 2: Fetch Biller Information

<br />

Retrieve biller categories and then fetch billers by category or region. This data can be cached and refreshed weekly.

<Accordion title="Request parameters" icon="fa-table">
  #### Get Biller Categories

  | Parameter                      | Description                         | Example            |
  | :----------------------------- | :---------------------------------- | :----------------- |
  | Authorization<br />`mandatory` | `String` - Bearer token from Step 1 | Bearer eyJhbGci... |

  #### Get Billers by Category

  | Parameter                           | Description                                  | Example     |
  | :---------------------------------- | :------------------------------------------- | :---------- |
  | billerCategoryName<br />`mandatory` | `String` - Category name from categories API | ELECTRICITY |
  | agentId<br />`mandatory`            | `String` - Your agent identifier             | AGT001      |
  | pageNumber<br />`optional`          | `Integer` - Page index (starts from 0)       | 0           |
  | pageSize<br />`optional`            | `Integer` - Records per page (max 1000)      | 100         |
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```bash
  # Get all categories
  curl -X GET \
    'https://bbps-sb.payu.in/payu-nbc/v1/nbc/getAllBillerCategory' \
    -H 'Authorization: Bearer <access_token>'

  # Get billers by category
  curl -X GET \
    'https://bbps-sb.payu.in/payu-nbc/v1/nbc/getBillerByBillerCategory?billerCategoryName=ELECTRICITY&agentId=AGT001' \
    -H 'Authorization: Bearer <access_token>'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-check">
  ```json
  {
    "code": 200,
    "status": "SUCCESS",
    "payload": {
      "billers": [
        {
          "billerId": "MSEL00000MUM01",
          "billerName": "Maharashtra State Electricity",
          "fetchOption": "MANDATORY",
          "isAdhoc": false,
          "supportBillValidation": "NOT_SUPPORTED",
          "billerMode": "ONLINE",
          "customerParams": [
            {
              "paramName": "Consumer Number",
              "dataType": "ALPHANUMERIC",
              "minLength": "2",
              "maxLength": "15"
            }
          ]
        }
      ]
    }
  }
  ```
</Accordion>

***

<br />

## Step 3: Fetch Bill Details

<br />

For billers with `fetchOption` as MANDATORY or OPTIONAL, fetch the customer's bill details before payment.

<Accordion title="Request parameters" icon="fa-table">
  | Parameter                       | Description                                        | Example                             |
  | :------------------------------ | :------------------------------------------------- | :---------------------------------- |
  | agentId<br />`mandatory`        | `String` - Your agent identifier                   | AGT001                              |
  | billerId<br />`mandatory`       | `String` - Biller ID from Step 2                   | MSEL00000MUM01                      |
  | customerParams<br />`mandatory` | `Object` - Customer parameters as per biller MDM   | \{"Consumer Number": "123456789"}   |
  | refId<br />`mandatory`          | `String` - Unique reference ID (35 chars for BBPS) | ABCDE12345ABCDE12345ABCDE1A01192345 |
  | timeStamp<br />`mandatory`      | `String` - Request timestamp                       | 2024-01-15 10:30:00                 |
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl -X POST \
    'https://bbps-sb.payu.in/payu-nbc/v1/nbc/fetchBill' \
    -H 'Authorization: Bearer <access_token>' \
    -H 'Content-Type: application/json' \
    -d '{
      "agentId": "AGT001",
      "billerId": "MSEL00000MUM01",
      "customerParams": {"Consumer Number": "123456789"},
      "refId": "ABCDE12345ABCDE12345ABCDE1A01192345",
      "timeStamp": "2024-01-15 10:30:00"
    }'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-check">
  ```json
  {
    "code": 200,
    "status": "SUCCESS",
    "payload": {
      "refId": "ABCDE12345ABCDE12345ABCDE1A01192345",
      "billerId": "MSEL00000MUM01",
      "customerName": "John Doe",
      "billAmount": "1500.00",
      "billDueDate": "2024-01-20",
      "billNumber": "BILL123456"
    }
  }
  ```
</Accordion>

***

<br />

## Step 4: Validate Payment (Optional)

<br />

For billers with `supportBillValidation` as MANDATORY or OPTIONAL, validate payment details before processing.

<Accordion title="Request parameters" icon="fa-table">
  | Parameter                            | Description                          | Example                                              |
  | :----------------------------------- | :----------------------------------- | :--------------------------------------------------- |
  | agentId<br />`mandatory`             | `String` - Your agent identifier     | AGT001                                               |
  | billerId<br />`mandatory`            | `String` - Biller ID                 | MSEL00000MUM01                                       |
  | customerParams<br />`mandatory`      | `Object` - Customer parameters       | \{"Consumer Number": "123456789"}                    |
  | customerPhoneNumber<br />`mandatory` | `String` - Customer mobile number    | 9876543210                                           |
  | paidAmount<br />`mandatory`          | `Numeric` - Amount (pass 0 for BBPS) | 0                                                    |
  | refId<br />`mandatory`               | `String` - Unique reference ID       | VAL123456789...                                      |
  | deviceDetails<br />`mandatory`       | `Object` - Device information        | \{"INITIATING\_CHANNEL": "INT", "IP": "192.168.1.1"} |
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl -X POST \
    'https://bbps-sb.payu.in/payu-nbc/v2/nbc/paymentValidation' \
    -H 'Authorization: Bearer <access_token>' \
    -H 'Content-Type: application/json' \
    -d '{
      "agentId": "AGT001",
      "billerId": "MSEL00000MUM01",
      "customerParams": {"Consumer Number": "123456789"},
      "customerPhoneNumber": "9876543210",
      "paidAmount": 0,
      "refId": "VAL123456789012345678901234567890",
      "deviceDetails": {"INITIATING_CHANNEL": "INT", "IP": "192.168.1.1"}
    }'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-check">
  ```json
  {
    "code": 200,
    "status": "SUCCESS",
    "payload": {
      "refId": "VAL123456789012345678901234567890",
      "timeStamp": "2024-01-15 10:30:05",
      "amount": "1500.00"
    }
  }
  ```
</Accordion>

***

<br />

## Step 5: Process Payment

<br />

Submit the bill payment transaction. Ensure you use a unique RefId for each payment request.

<Accordion title="Request parameters" icon="fa-table">
  | Parameter                            | Description                                  | Example                                      |
  | :----------------------------------- | :------------------------------------------- | :------------------------------------------- |
  | agentId<br />`mandatory`             | `String` - Your agent identifier             | AGT001                                       |
  | billerId<br />`mandatory`            | `String` - Biller ID                         | MSEL00000MUM01                               |
  | customerParams<br />`mandatory`      | `Object` - Customer parameters               | \{"Consumer Number": "123456789"}            |
  | customerName<br />`mandatory`        | `String` - Customer name                     | John Doe                                     |
  | customerPhoneNumber<br />`mandatory` | `String` - Customer mobile                   | 9876543210                                   |
  | paidAmount<br />`mandatory`          | `Numeric` - Payment amount                   | 1500.00                                      |
  | refId<br />`mandatory`               | `String` - Unique reference ID (35 chars)    | PAY123456789...                              |
  | isQuickPay<br />`mandatory`          | `Boolean` - Quick pay flag per biller config | false                                        |
  | deviceDetails<br />`mandatory`       | `Object` - Device information                | \{"INITIATING\_CHANNEL": "INT", "IP": "..."} |
  | paymentDetails<br />`mandatory`      | `Object` - Payment mode details              | \{"paymentMode": "Internet Banking"}         |
  | pgName<br />`mandatory`              | `String` - Payment gateway (PayU or Other)   | PayU                                         |
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl -X POST \
    'https://bbps-sb.payu.in/payu-nbc/v1/nbc/payBill' \
    -H 'Authorization: Bearer <access_token>' \
    -H 'Content-Type: application/json' \
    -d '{
      "agentId": "AGT001",
      "billerId": "MSEL00000MUM01",
      "customerParams": {"Consumer Number": "123456789"},
      "customerName": "John Doe",
      "customerPhoneNumber": "9876543210",
      "paidAmount": 1500.00,
      "refId": "PAY123456789012345678901234567890",
      "isQuickPay": false,
      "deviceDetails": {
        "INITIATING_CHANNEL": "INT",
        "IP": "192.168.1.1"
      },
      "paymentDetails": {"paymentMode": "Internet Banking"},
      "additionalParams": {"agentTxnID": "TXN123"},
      "pgName": "PayU",
      "paymentRefID": "PGREF123"
    }'
  ```
</Accordion>

> **Note:** If you receive `payment_request_pending`, use the Transaction Status API to check the final status.

## Step 6: Verify Transaction Status

For pending transactions or reconciliation, check the transaction status using this API.

<Accordion title="Request parameters" icon="fa-table">
  | Parameter                      | Description                                  | Example         |
  | :----------------------------- | :------------------------------------------- | :-------------- |
  | agentId<br />`mandatory`       | `String` - Your agent identifier             | AGT001          |
  | refId<br />`mandatory`         | `String` - Reference ID from payment request | PAY123456789... |
  | txnReferenceId<br />`optional` | `String` - BBPS transaction reference        | BBPS123456789   |
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl -X POST \
    'https://bbps-sb.payu.in/payu-nbc/v2/nbc/paymentStatus' \
    -H 'Authorization: Bearer <access_token>' \
    -H 'Content-Type: application/json' \
    -d '{
      "agentId": "AGT001",
      "refId": "PAY123456789012345678901234567890"
    }'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-check">
  ```json
  {
    "code": 200,
    "status": "SUCCESS",
    "payload": {
      "refId": "PAY123456789012345678901234567890",
      "txnStatus": "PAYMENT_SUCCESS",
      "txnReferenceId": "BBPS123456789012345",
      "paidAmount": 1500.00,
      "billerId": "MSEL00000MUM01"
    }
  }
  ```
</Accordion>

***

<br />
