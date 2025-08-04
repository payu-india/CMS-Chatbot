---
title: Steps to Integrate - Mobikwik Link & Pay
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU's Mobikwik Link & Pay integration is a streamlined one-click payment solution that enhances user experience by eliminating the need for repeated logins and multi-step wallet interactions. This integration guide provides step-by-step instructions for implementing Mobikwik Link & Pay payments on your platform.

## Step 1: Check User Balance and Link Status

Before initiating a payment, check if the user's Mobikwik wallet is linked and verify the available balance.

### Environment

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Environment</th>
      <th>Endpoint</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Test</td>
      <td><code>https://test.mobikwik.com/userbalance</code></td>
    </tr>
    <tr>
      <td>Production</td>
      <td><code>https://api.mobikwik.com/userbalance</code></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

<Accordion title="Sample request" icon="fa-table">
<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>mid<br/><code>mandatory</code></td>
      <td>Merchant ID assigned by Mobikwik</td>
    </tr>
    <tr>
      <td>cell<br/><code>mandatory</code></td>
      <td>User's mobile number</td>
    </tr>
    <tr>
      <td>msgcode<br/><code>mandatory</code></td>
      <td>Message code for the request</td>
    </tr>
    <tr>
      <td>checksum<br/><code>mandatory</code></td>
      <td>HMAC SHA256 hash for security</td>
    </tr>
    <tr>
      <td>aggregatedMerchantId<br/><code>optional</code></td>
      <td>Aggregated merchant identifier</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl --location 'https://test.mobikwik.com/userbalance' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'mid=YOUR_MERCHANT_ID' \
  --data-urlencode 'cell=9560012582' \
  --data-urlencode 'msgcode=CHECK_BALANCE' \
  --data-urlencode 'checksum=GENERATED_CHECKSUM'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  **Success Response:**

  ```json
  {
    "status": "success",
    "statusCode": "S001",
    "statusDescription": "Balance Retrieved Successfully",
    "availableBalance": "5000.00",
    "customerLinked": "true",
    "walletStatus": "active"
  }
  ```

  **Wallet Not Linked Response:**

  ```json
  {
    "status": "failure",
    "statusCode": "ERR002",
    "statusDescription": "Wallet not linked",
    "customerLinked": "false"
  }
  ```

  If `customerLinked` is `false`, proceed with the first-time user flow. If `true`, proceed with the repeat user flow.
</Accordion>

***

## Step 2: Payment Initiation API

The Payment Initiation API enables merchants to seamlessly initiate payment requests for transactions using the Mobikwik Link & Pay flow.

### Environment

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Environment</th>
      <th>Endpoint</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Test</td>
      <td><code>https://test.payu.in/v2/payments</code></td>
    </tr>
    <tr>
      <td>Production</td>
      <td><code>https://api.payu.in/v2/payments</code></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

### Required Parameters

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>merchantKey<br/><code>mandatory</code></td>
      <td>Merchant key from PayU Dashboard</td>
    </tr>
    <tr>
      <td>transactionId<br/><code>mandatory</code></td>
      <td>Unique transaction identifier</td>
    </tr>
    <tr>
      <td>amount<br/><code>mandatory</code></td>
      <td>Transaction amount (decimal format)</td>
    </tr>
    <tr>
      <td>productInfo<br/><code>mandatory</code></td>
      <td>Product description for the transaction</td>
    </tr>
    <tr>
      <td>firstName<br/><code>mandatory</code></td>
      <td>Customer first name</td>
    </tr>
    <tr>
      <td>email<br/><code>mandatory</code></td>
      <td>Customer email address</td>
    </tr>
    <tr>
      <td>phone<br/><code>mandatory</code></td>
      <td>Customer mobile number</td>
    </tr>
    <tr>
      <td>surl<br/><code>mandatory</code></td>
      <td>Success URL where user will be redirected after successful payment</td>
    </tr>
    <tr>
      <td>furl<br/><code>mandatory</code></td>
      <td>Failure URL where user will be redirected after failed payment</td>
    </tr>
    <tr>
      <td>bankcode<br/><code>mandatory</code></td>
      <td>Must be "MOBIKWIK" for Mobikwik payments</td>
    </tr>
    <tr>
      <td>hash<br/><code>mandatory</code></td>
      <td>SHA512 hash for security and data integrity</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

### Sample Request

<Accordion title="S2S Merchant Request" icon="fa-code">
  ```bash
  curl --location 'https://test.payu.in/v2/payments' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=YOUR_MERCHANT_KEY' \
  --data-urlencode 'txnid=TXN123456789' \
  --data-urlencode 'amount=1000.00' \
  --data-urlencode 'productinfo=Mobikwik Payment' \
  --data-urlencode 'firstname=John' \
  --data-urlencode 'email=john@example.com' \
  --data-urlencode 'phone=9560012582' \
  --data-urlencode 'surl=https://yoursite.com/success' \
  --data-urlencode 'furl=https://yoursite.com/failure' \
  --data-urlencode 'bankcode=MOBIKWIK' \
  --data-urlencode 'hash=GENERATED_HASH'
  ```
####Hosted Checkout Request" icon="fa-code"
  ```bash
  curl --location 'https://test.payu.in/_payment' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=YOUR_MERCHANT_KEY' \
  --data-urlencode 'txnid=TXN123456789' \
  --data-urlencode 'amount=1000.00' \
  --data-urlencode 'productinfo=Mobikwik Payment' \
  --data-urlencode 'firstname=John' \
  --data-urlencode 'email=john@example.com' \
  --data-urlencode 'phone=9560012582' \
  --data-urlencode 'surl=https://yoursite.com/success' \
  --data-urlencode 'furl=https://yoursite.com/failure' \
  --data-urlencode 'hash=GENERATED_HASH'
  ```
</Accordion>

### Sample Response
* Success scenario
  ```json
  {
    "status": "success",
    "data": {
      "paymentId": "PAY_12345",
      "transactionId": "TXN123456789",
      "amount": "1000.00",
      "status": "pending",
      "redirectUrl": "https://mobikwik.payment.url",
      "message": "Payment initiated successfully"
    }
  }
  ```

* Failure scenario
  ```json
  {
    "status": "error",
    "errorCode": "INVALID_AMOUNT",
    "message": "Invalid amount provided",
    "data": null
  }
  ```

### Payment Flow Types

The Payment Initiation API automatically determines the appropriate flow based on user status:

#### For Linked Users (Auto-debit Flow)

* API directly processes payment using stored token
* Faster checkout experience
* Immediate payment confirmation

#### For Unlinked Users (Redirect Flow)

* User redirected to Mobikwik authentication
* OTP verification for wallet linking
* Token generation for future transactions

<Accordion title="Important Notes" icon="fa-info-circle">
  • The Payment Initiation API handles flow determination automatically\
  • Ensure `bankcode=MOBIKWIK` is included in all requests\
  • User identification via mobile number is mandatory\
  • Hash/Checksum generation is required for security\
  • Test thoroughly in sandbox before production deployment
</Accordion>

***

## Step 3: Process Payment Based on User Status

After initiating the payment via the Payment Initiation API, the system will process the payment based on whether the user's wallet is linked or not.

## Step 4: Submit OTP and Generate Token

After the user enters the OTP, submit it to generate a wallet token for future transactions.

### Environment

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Environment</th>
      <th>Endpoint</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Test</td>
      <td><code>https://test.mobikwik.com/tokengenerate</code></td>
    </tr>
    <tr>
      <td>Production</td>
      <td><code>https://api.mobikwik.com/tokengenerate</code></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

<Accordion title="Request parameters" icon="fa-info-table">
<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>mid<br/><code>mandatory</code></td>
      <td>Merchant ID</td>
    </tr>
    <tr>
      <td>cell<br/><code>mandatory</code></td>
      <td>User's mobile number</td>
    </tr>
    <tr>
      <td>msgcode<br/><code>mandatory</code></td>
      <td>Message code</td>
    </tr>
    <tr>
      <td>otp<br/><code>mandatory</code></td>
      <td>OTP entered by user</td>
    </tr>
    <tr>
      <td>amount<br/><code>mandatory</code></td>
      <td>Transaction amount</td>
    </tr>
    <tr>
      <td>tokentype<br/><code>mandatory</code></td>
      <td>Token type identifier</td>
    </tr>
    <tr>
      <td>checksum<br/><code>mandatory</code></td>
      <td>HMAC SHA256 hash</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl --location 'https://test.mobikwik.com/tokengenerate' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'mid=YOUR_MERCHANT_ID' \
  --data-urlencode 'cell=9560012582' \
  --data-urlencode 'msgcode=TOKEN_GENERATE' \
  --data-urlencode 'otp=123456' \
  --data-urlencode 'amount=1000.00' \
  --data-urlencode 'tokentype=WALLET_LINK' \
  --data-urlencode 'checksum=GENERATED_CHECKSUM'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  **Success Response:**

  ```json
  {
    "status": "success",
    "statusCode": "S003",
    "statusDescription": "Token Generated Successfully",
    "token": "TKN_ABC123XYZ789",
    "tokenExpiry": "365",
    "orderid": "ORD123456"
  }
  ```

  **Invalid OTP Response:**

  ```json
  {
    "status": "failure",
    "statusCode": "ERR003",
    "statusDescription": "Invalid OTP"
  }
  ```
</Accordion>

<Accordion title="Note" icon="fa-info-circle">
  Store the generated token securely for future transactions. Tokens are valid for 365 days by default.
</Accordion>

***

<Callout icon="📘" theme="info">
  ## References:

  * When the wallet balance is insufficient, use the **Add Money & Debit** API to allow users to load money and complete the transaction in a single flow. For more information, refer to [Add Money to Wallet And Debit API](ref:add-money-to-wallet-and-debit-api-mobikwik)
  * Verify the transaction status using the **Check Status** API. For more information, refer to [Check Status API](ref:check-status-api).
  * Process refunds using the standard PayU refund mechanism. Refunds are processed in the T+1 settlement cycle. For more information, refer to [Refund Transaction API](ref:refund_transaction_api).
  * If a token expires or becomes invalid, regenerate it using the Token Regenerate API. For more information, refer to Regenerate Token API.
</Callout>

## Error handling

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Error Code</th>
      <th>Description</th>
      <th>Recommended Action</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ERR001</td>
      <td>Insufficient Balance</td>
      <td>Redirect to Add Money flow</td>
    </tr>
    <tr>
      <td>ERR002</td>
      <td>Wallet not linked</td>
      <td>Initiate first-time user flow</td>
    </tr>
    <tr>
      <td>ERR003</td>
      <td>Invalid OTP</td>
      <td>Allow OTP retry (max 3 attempts)</td>
    </tr>
    <tr>
      <td>ERR004</td>
      <td>Transaction Failed</td>
      <td>Show error message, offer retry</td>
    </tr>
    <tr>
      <td>ERR005</td>
      <td>Invalid Token</td>
      <td>Regenerate token</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>
