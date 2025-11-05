---
title: Seamless Debit Integration - CLW
deprecated: false
hidden: false
metadata:
  robots: index
---
This section describes the step-by-step procedure for the workflow involving checking wallet balance, loading money via Payment Gateway, and initiating seamless debit transactions.

## How It Works

The **Balance Check, Load & Seamless Debit API** workflow enables merchants to:

1. **Check Wallet Balance**: Query the current available balance in a customer's wallet.
2. **Load Money via PG**: Enable customers to add funds to their wallet through Payment Gateway.
3. **Seamless Debit**: Initiate instant debit transactions from the wallet for purchases.
4. **Unified Experience**: Provide a complete wallet management solution in a single integration.

This workflow is ideal for merchants who want to offer a comprehensive wallet experience with balance inquiry, top-up functionality, and instant payment capabilities.

## Step 1: Check Wallet Balance

Before any wallet operation, check the current balance using the Retrieve Customer Record API.

* **API Endpoint (Test)**: `https://apitest.payu.in/loyalty-points/v1/wallet/retrieveCustRecord`
* **Method**: `POST`

<Accordion title="Request Headers" icon="fa-table">
### Header authentication parameters
    This API uses HMAC-SHA512 authentication on the header.

    <HTMLBlock>{`
                                <table class="api-parameters">
                                  <thead>
                                    <tr>
                                      <th scope="col">Parameter</th>
                                      <th scope="col">Description</th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    <tr>
                                      <td>
                                        <strong>walletIdentifier</strong><br />
                                        <span class="required-badge">mandatory</span>
                                      </td>
                                      <td>
                                        <code>String</code> Program Type (e.g., CLW)
                                      </td>
                                    </tr>
                                    <tr>
                                      <td>
                                        <strong>date</strong><br />
                                        <span class="required-badge">mandatory</span>
                                      </td>
                                      <td>
                                        <code>String</code> GMT formatted date (e.g., Thu, 17 Feb 2022 08:17:59 GMT)
                                      </td>
                                    </tr>
                                    <tr>
                                      <td>
                                        <strong>Authorization</strong><br />
                                        <span class="required-badge">mandatory</span>
                                      </td>
                                      <td>
                                        <code>String</code> HMAC-SHA512-based authentication token
                                      </td>
                                    </tr>
                                    <tr>
                                      <td>
                                        <strong>Content-Type</strong><br />
                                        <span class="required-badge">mandatory</span>
                                      </td>
                                      <td>
                                        <code>String</code> application/json
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
    `}</HTMLBlock>

    <Callout icon="↩️" theme="default">
      If you do not post the authentication, you will get error in response. For the list of error codes, refer to [Status Codes](ref:status-codes-clw)
    </Callout>

### hmac authentication logic

    ```
    hmac username="smsplus", algorithm="sha512", headers="date", signature="7ff938849aa79265a3de63fe241dfecb1c680f58c6d11e9f9ca08512afea374705eb9f8995ef6c4584e16eca2e1dc688262bb0937a36cc0f75ec22a9eea33523"
    ```

    Where, the fields in this example are:

    * **username**: The merchant key of the merchant.
    * **algorithm**: This must have the value as hmac-sha512 that is used for this API.
    * **headers**: This must have the value as date digest.
    * **signature**: This must contain the hmacsha512 of (signing\_string, merchant\_secret), where:
    * **signing\_string**: It must be in the "date: \{dateValue}"format. Here, the dateValue is the same values in the fields listed in this table For example, "date: Thu, 17 Feb 2022 08:17:59 GMT"
    * **merchant\_secret**: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to Generate Merchant Key and Salt.

</Accordion>

<Accordion title="Request Body Parameters" icon="fa-table">
  <HTMLBlock>{`
              <table>
                <thead>
                  <tr>
                    <th>Parameter</th>
                    <th>Description</th>
                    <th>Example</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>messageCode <code>mandatory</code></td>
                    <td><code>Integer</code> - Numeric identifier for the API</td>
                    <td>1930</td>
                  </tr>
                  <tr>
                    <td>clientTxnId <code>mandatory</code></td>
                    <td><code>String</code> - Unique transaction ID</td>
                    <td>BALANCE_CHK_001</td>
                  </tr>
                  <tr>
                    <td>requestDateTime <code>mandatory</code></td>
                    <td><code>String</code> - Local timestamp in YYYYMMDDHHMMSS format</td>
                    <td>20230822183015</td>
                  </tr>
                  <tr>
                    <td>customerMobile <code>optional</code></td>
                    <td><code>String</code> - Customer mobile with country code (at least one customer identifier is required)</td>
                    <td>919876543210</td>
                  </tr>
                  <tr>
                    <td>customerId <code>optional</code></td>
                    <td><code>String</code> - Unique customer identifier (at least one customer identifier is required)</td>
                    <td>CUST_001</td>
                  </tr>
                  <tr>
                    <td>emailId <code>optional</code></td>
                    <td><code>String</code> - Customer email address (at least one customer identifier is required)</td>
                    <td>john@example.com</td>
                  </tr>
                  <tr>
                    <td>urn <code>optional</code></td>
                    <td><code>String</code> - Unique wallet reference number (at least one customer identifier is required)</td>
                    <td>12345678901</td>
                  </tr>
                </tbody>
              </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
  ```bash
  curl -X POST \
  https://apitest.payu.in/loyalty-points/v1/wallet/retrieveCustRecord \
  -H 'walletIdentifier: CLW' \
  -H 'date: Thu, 17 Feb 2022 08:17:59 GMT' \
  -H 'Authorization: HMAC <your_hmac_token>' \
  -H 'Content-Type: application/json' \
  -d '{
    "messageCode": 1930,
    "clientTxnId": "BALANCE_CHK_001",
    "requestDateTime": "20230822183015",
    "customerMobile": "919876543210"
  }'
  ```
</Accordion>

<Accordion title="Sample Response - Success" icon="fa-code">
  ```json
  {
    "responseCode": "0000",
    "responseMessage": "SUCCESS",
    "customerRecord": {
      "customerId": "CUST_001",
      "availableBalance": "1500.00",
      "walletStatus": "ACTIVE",
      "urn": "12345678901",
      "customerMobile": "919876543210"
    }
  }
  ```
</Accordion>

> **📘 Note**: Store the available balance to determine if additional funds need to be loaded before making a purchase.

## Step 2: Load Money to Wallet (if required)

If the wallet balance is insufficient, initiate a PG Load transaction to enable the customer to add funds.

* **API Endpoint (Test)**: `https://apitest.payu.in/loyalty-points/ppi/payment/pg-load/v1`
* **Method**: `PATCH`

<Accordion title="Request Headers" icon="fa-table">
  This API uses HMAC-SHA512 authentication on the header.

  <HTMLBlock>{`   <table class="api-parameters">
                <thead>
                  <tr>
                    <th scope="col">Parameter</th>
                    <th scope="col">Description</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>
                      <strong>walletIdentifier</strong><br />
                      <span class="required-badge">mandatory</span>
                    </td>
                    <td>
                      <code>String</code> Program Type (e.g., CLW)
                    </td>
                  </tr>
                  <tr>
                    <td>
                      <strong>date</strong><br />
                      <span class="required-badge">mandatory</span>
                    </td>
                    <td>
                      <code>String</code> GMT formatted date (e.g., Thu, 17 Feb 2022 08:17:59 GMT)
                    </td>
                  </tr>
                  <tr>
                    <td>
                      <strong>Authorization</strong><br />
                      <span class="required-badge">mandatory</span>
                    </td>
                    <td>
                      <code>String</code> HMAC-SHA512-based authentication token
                    </td>
                  </tr>
                  <tr>
                    <td>
                      <strong>Content-Type</strong><br />
                      <span class="required-badge">mandatory</span>
                    </td>
                    <td>
                      <code>String</code> application/json
                    </td>
                  </tr>
                </tbody>
              </table>
              `}</HTMLBlock>
</Accordion>

<Accordion title="Request Body Parameters" icon="fa-table">
  <HTMLBlock>{`
              <table>
                <thead>
                  <tr>
                    <th>Parameter</th>
                    <th>Description</th>
                    <th>Example</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>clientTxnId <code>mandatory</code></td>
                    <td><code>String</code> - Unique transaction ID (alphanumeric, max 14 characters)</td>
                    <td>Reload_V3_1234</td>
                  </tr>
                  <tr>
                    <td>requestDateTime <code>mandatory</code></td>
                    <td><code>String</code> - Timestamp in YYYYMMDDHHMMSS format</td>
                    <td>20230822183015</td>
                  </tr>
                  <tr>
                    <td>customerId <code>optional</code></td>
                    <td><code>String</code> - Unique customer ID (auto-generated if not passed)</td>
                    <td>89342546</td>
                  </tr>
                  <tr>
                    <td>customerMobile <code>mandatory</code></td>
                    <td><code>String</code> - Customer mobile with country code</td>
                    <td>919876543210</td>
                  </tr>
                  <tr>
                    <td>loadAmount <code>mandatory</code></td>
                    <td><code>String</code> - Amount to be loaded (minimum 1.00)</td>
                    <td>500.00</td>
                  </tr>
                  <tr>
                    <td>emailId <code>optional</code></td>
                    <td><code>String</code> - Customer email address</td>
                    <td>john@example.com</td>
                  </tr>
                  <tr>
                    <td>firstName <code>optional</code></td>
                    <td><code>String</code> - Customer first name</td>
                    <td>John</td>
                  </tr>
                  <tr>
                    <td>lastName <code>optional</code></td>
                    <td><code>String</code> - Customer last name</td>
                    <td>Doe</td>
                  </tr>
                  <tr>
                    <td>successUrl <code>mandatory</code></td>
                    <td><code>String</code> - URL for successful transaction redirect</td>
                    <td>https://merchant.com/success</td>
                  </tr>
                  <tr>
                    <td>failureUrl <code>mandatory</code></td>
                    <td><code>String</code> - URL for failed transaction redirect</td>
                    <td>https://merchant.com/failure</td>
                  </tr>
                </tbody>
              </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
  ```bash
  curl -X PATCH \
  https://apitest.payu.in/loyalty-points/ppi/payment/pg-load/v1 \
  -H 'walletIdentifier: CLW' \
  -H 'date: Wed, 12 Jun 2024 08:53:43 GMT' \
  -H 'Authorization: HMAC <your_hmac_token>' \
  -H 'Content-Type: application/json' \
  -d '{
    "clientTxnId": "Reload_V3_1234",
    "requestDateTime": "20230822183015",
    "customerMobile": "919876543210",
    "loadAmount": "500.00",
    "emailId": "john@example.com",
    "firstName": "John",
    "lastName": "Doe",
    "successUrl": "https://merchant.com/success",
    "failureUrl": "https://merchant.com/failure"
  }'
  ```
</Accordion>

<Accordion title="Sample Response - Success" icon="fa-code">
  ```json
  {
    "responseCode": "0000",
    "responseMessage": "SUCCESS",
    "paymentUrl": "https://test.payu.in/_payment",
    "txnId": "TXN123456789",
    "customerId": "89342546",
    "urn": "12345678901"
  }
  ```
</Accordion>

## Step 3: Check PG Load Status

Use the PG Load Enquiry API to verify the status of the load transaction.

* **API Endpoint (Test)**: `https://apitest.payu.in/loyalty-points/ppi/payment/pg-load-enquiry/v1`
* **Method**: `POST`

<Accordion title="Request Headers" icon="fa-table">
  <HTMLBlock>{`
              <table>
                <thead>
                  <tr>
                    <th>Parameter</th>
                    <th>Description</th>
                    <th>Example</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>walletIdentifier <code>mandatory</code></td>
                    <td><code>String</code> - Program type</td>
                    <td>CLW</td>
                  </tr>
                  <tr>
                    <td>date <code>mandatory</code></td>
                    <td><code>String</code> - GMT-formatted date</td>
                    <td>Wed, 12 Jun 2024 08:53:43 GMT</td>
                  </tr>
                  <tr>
                    <td>Authorization <code>mandatory</code></td>
                    <td><code>String</code> - HMAC-SHA512-based authentication token</td>
                    <td>HMAC token</td>
                  </tr>
                  <tr>
                    <td>Content-Type <code>mandatory</code></td>
                    <td><code>String</code> - Request content type</td>
                    <td>application/json</td>
                  </tr>
                </tbody>
              </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Request Body Parameters" icon="fa-table">
  <HTMLBlock>{`
              <table>
                <thead>
                  <tr>
                    <th>Parameter</th>
                    <th>Description</th>
                    <th>Example</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>clientTxnId <code>mandatory</code></td>
                    <td><code>String</code> - Original transaction ID from PG Load request</td>
                    <td>Reload_V3_1234</td>
                  </tr>
                  <tr>
                    <td>requestDateTime <code>mandatory</code></td>
                    <td><code>String</code> - Timestamp in YYYYMMDDHHMMSS format</td>
                    <td>20230822183015</td>
                  </tr>
                </tbody>
              </table>
  `}</HTMLBlock>
</Accordion>

## Step 4: Collect Payment - Seamless Debit Transaction

Once sufficient balance is available, initiate a seamless debit transaction using the Collect Payment API.

* **API Endpoint (Test)**: `https://test.payu.in/_payment`
* **API Endpoint (Production)**: `https://secure.payu.in/_payment`
* **Method**: `POST`

<Accordion title="Request Headers" icon="fa-table">
  <HTMLBlock>{`
              <table>
                <thead>
                  <tr>
                    <th>Parameter</th>
                    <th>Description</th>
                    <th>Example</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Content-Type <code>mandatory</code></td>
                    <td><code>String</code> - Request content type</td>
                    <td>application/x-www-form-urlencoded</td>
                  </tr>
                </tbody>
              </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Request Body Parameters" icon="fa-code">
  The request body contains an encrypted parameter `encdata` which includes all the transaction details.

  <Accordion title="Encrypted Parameter" icon="fa-code">
    <HTMLBlock>{`
                            <table>
                              <thead>
                                <tr>
                                  <th>Parameter</th>
                                  <th>Description</th>
                                  <th>Example</th>
                                </tr>
                              </thead>
                              <tbody>
                                <tr>
                                  <td>encdata <code>mandatory</code></td>
                                  <td><code>String</code> - Encrypted request body containing all transaction parameters</td>
                                  <td>h/0YSUd9jKOQ8+2Dc3Phr4s7vxyz123...</td>
                                </tr>
                              </tbody>
                            </table>
    `}</HTMLBlock>
  </Accordion>

  <Accordion title="Decrypted Parameters (inside encdata)" icon="fa-code">
    <HTMLBlock>{`
                            <table>
                              <thead>
                                <tr>
                                  <th>Parameter</th>
                                  <th>Description</th>
                                  <th>Example</th>
                                </tr>
                              </thead>
                              <tbody>
                                <tr>
                                  <td>txnId <code>mandatory</code></td>
                                  <td><code>String</code> - Unique transaction ID generated by merchant (max 25 characters)</td>
                                  <td>56882</td>
                                </tr>
                                <tr>
                                  <td>key <code>mandatory</code></td>
                                  <td><code>String</code> - Merchant key provided by PayU (max 50 characters)</td>
                                  <td>KPQwN8</td>
                                </tr>
                                <tr>
                                  <td>productinfo <code>mandatory</code></td>
                                  <td><code>String</code> - Brief product description (max 100 characters)</td>
                                  <td>iPhone</td>
                                </tr>
                                <tr>
                                  <td>Customer_id <code>optional</code></td>
                                  <td><code>String</code> - Unique customer ID (max 50 characters, alternative to walleturn)</td>
                                  <td>89342546</td>
                                </tr>
                                <tr>
                                  <td>walleturn <code>optional</code></td>
                                  <td><code>String</code> - Wallet URN from balance check (11 digits, alternative to Customer_id)</td>
                                  <td>70000000008</td>
                                </tr>
                                <tr>
                                  <td>firstName <code>mandatory</code></td>
                                  <td><code>String</code> - Customer first name (max 60 characters)</td>
                                  <td>Sourav</td>
                                </tr>
                                <tr>
                                  <td>lastName <code>optional</code></td>
                                  <td><code>String</code> - Customer last name (max 60 characters)</td>
                                  <td>Mishra</td>
                                </tr>
                                <tr>
                                  <td>phone <code>mandatory</code></td>
                                  <td><code>String</code> - Customer phone with ISD code (max 15 digits)</td>
                                  <td>919988776655</td>
                                </tr>
                                <tr>
                                  <td>email <code>mandatory</code></td>
                                  <td><code>String</code> - Customer email address (max 50 characters)</td>
                                  <td>sourav.mishra@gmail.com</td>
                                </tr>
                                <tr>
                                  <td>ws_online_response <code>mandatory</code></td>
                                  <td><code>String</code> - Success URL for transaction response (max 255 characters)</td>
                                  <td>https://success.url.com</td>
                                </tr>
                                <tr>
                                  <td>ws_failure_response <code>mandatory</code></td>
                                  <td><code>String</code> - Failure URL for transaction response (max 255 characters)</td>
                                  <td>https://failure.url.com</td>
                                </tr>
                                <tr>
                                  <td>amount <code>mandatory</code></td>
                                  <td><code>String</code> - Amount in paise (₹4.10 = 410)</td>
                                  <td>4100</td>
                                </tr>
                                <tr>
                                  <td>pg <code>mandatory</code></td>
                                  <td><code>String</code> - Payment gateway type for closed-loop wallet</td>
                                  <td>CLW</td>
                                </tr>
                                <tr>
                                  <td>txn_s2s_flow <code>mandatory</code></td>
                                  <td><code>String</code> - Constant value for seamless debit</td>
                                  <td>4</td>
                                </tr>
                                <tr>
                                  <td>bankcode <code>mandatory</code></td>
                                  <td><code>String</code> - Merchant-specific bank code</td>
                                  <td>PAY</td>
                                </tr>
                                <tr>
                                  <td>hash <code>mandatory</code></td>
                                  <td><code>String</code> - SHA512 hash for request verification</td>
                                  <td>6e640b...</td>
                                </tr>
                              </tbody>
                            </table>
    `}</HTMLBlock>

    <Callout icon="📘" theme="info">
      **Note**: Either `Customer_id` or `walleturn` must be provided to identify the customer wallet.
    </Callout>
  </Accordion>
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
  ```bash
  curl -X POST \
  https://test.payu.in/_payment \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'encdata=h/0YSUd9jKOQ8+2Dc3Phr4s7vxyz123...'
  ```

  **Decrypted Request Body:**

  ```
  txnId=56882&key=KPQwN8&productinfo=iPhone&Customer_id=89342546&firstName=Sourav&lastName=Mishra&phone=919988776655&email=sourav.mishra@gmail.com&ws_online_response=https://success.url.com&ws_failure_response=https://failure.url.com&amount=4100&pg=CLW&txn_s2s_flow=4&bankcode=PAY&hash=6e640b...
  ```
</Accordion>
<Accordion title="Sample Response" icon="fa-code">
<Accordion title="Success scenario" icon="fa-code">
  ```json
  {
    "mihpayid": "1735903830180094",
    "mode": "CLW",
    "status": "success",
    "key": "KPQwN8",
    "txnid": "56882",
    "amount": "41.00",
    "productinfo": "iPhone",
    "firstname": "Sourav",
    "lastname": "Mishra",
    "email": "sourav.mishra@gmail.com",
    "phone": "919988776655",
    "hash": "abc123def456...",
    "PG_TYPE": "CLW",
    "bank_ref_num": "123456789"
  }
  ```
</Accordion>

<Accordion title="Failure sceanario" icon="fa-code">
  ```json
  {
    "mihpayid": "1735903830180095",
    "mode": "CLW",
    "status": "failure",
    "key": "KPQwN8",
    "txnid": "56883",
    "amount": "41.00",
    "productinfo": "iPhone",
    "firstname": "Sourav",
    "lastname": "Mishra",
    "email": "sourav.mishra@gmail.com",
    "phone": "919988776655",
    "hash": "xyz789abc123...",
    "PG_TYPE": "CLW",
    "error": "Insufficient balance",
    "error_Message": "Wallet balance is insufficient for this transaction"
  }
  ```

  <br />
</Accordion>
</Accordion>
