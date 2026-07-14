---
title: '[S2S] UPI Consent Transaction - Cross Border'
deprecated: false
hidden: false
metadata:
  robots: index
---
This section describes step-by-step procedure to implement UPI Consent Transaction (SI mandate registration) for recurring UPI payments using PayU's Server-to-Server (S2S) integration with the Legacy Decoupled flow.

## Prerequisites

Before starting the integration, ensure you have:

* Active PayU merchant account with UPI recurring payments enabled
* Merchant Key and Salt from PayU dashboard
* Test environment access for development
* Understanding of UPI payment flow (Collect vs Intent)

**Payment consent flow**

<Cards columns={2}>
  <Card title="1. Post the Request" href="#step-1-post-the-request">
    Send the UPI consent transaction request with S2S parameters.

    <br />
  </Card>

  <Card title="2. Check Response from PayU" href="#step-2-check-the-response-from-payu">
    Handle the response for UPI Collect and UPI Intent flows.

    <br />
  </Card>

  <Card title="3. Configure Webhooks" href="#step-3-configure-webhooks">
    Set up webhooks to receive transaction status updates.

    <br />
  </Card>

  <Card title="4. Verify Mandate Registration" href="#step-4-verify-mandate-registration">
    Confirm the mandate registration was successful.

    <br />
  </Card>
</Cards>

**Recurring Payments Flow**

<Cards columns={2}>
  <Card title="1. Pre-Debit SI Notification" href="#step-1-pre-debit-si-notification">
    Send pre-debit notifications for upcoming recurring debits.
  </Card>

  <Card title="2. Recurring Payment Transaction" href="#step-2-recurring-payment-transaction">
    Execute recurring payment transactions using the registered mandate.
  </Card>
</Cards>

***

## Payment Consent Transaction

### Workflow

<Accordion title="UPI Autopay Intent - Mandate Consent Registration Flow" icon="fa-list">
  <Image align="center" src="https://files.readme.io/f07cf9ed28593d2b28daf9d35ec72698f887bf408b8f09ec0d2da7e64ce7788d-UPI_Autopay_Intent_-_Mandate_Consent_Registration.png" />
</Accordion>

<Accordion title="UPI Autopay Collect - Mandate Consent Registration Flow" icon="fa-list">
  <Image align="center" src="https://files.readme.io/cd32192033c868d054eaf3cf8c9aef816edf6e78e7bd9b06ba5e3955ef3f305b-UPI_Autopay_Collect_-_Mandate_Consent_Registration.png" />
</Accordion>
<Accordion title="UPI Intent-based QR - Mandate Consent Registration Flow" icon="fa-list">
  <Image align="center" src="https://files.readme.io/43cbb4034e0c1d33fd19fdeb9de23b9a4f01d3af980dfe62a54fde35fa5675ea-UPI_Intent_based_QR_for_Autopay_-_Mandate_Consent_Registration.png" />
</Accordion>

### Step 1: Post the Request

Before implementing, familiarize yourself with the required parameters.

<Callout icon="📘" theme="info">
  **Reference**:  For the UPI Consent Transaction - Cross Border Payments API Reference, refer to[ UPI Consent Transaction - CB](ref:upi-consent-transaction-cross-border).
</Callout>

<Accordion title="Key Parameters for UPI Mandate Registration" icon="fa-list">
  **Mandatory Parameters:**

  * `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `lastname`
  * `surl`, `furl`, `hash`
  * `pg` (must be `UPI`)
  * `bankcode` (`UPI` for Collect, `INTENT` for Intent)
  * `si` (must be `1`)
  * `si_details` (JSON object with mandate details)
  * `api_version` (must be `7`)

  **UPI-Specific Parameters:**

  * `vpa` (mandatory for UPI Collect - customer's VPA handle)

  **S2S Flow Parameters (for UPI Intent):**

  * `txn_s2s_flow` = `4` (Legacy Decoupled flow)
  * `s2s_client_ip` (customer's source IP)
  * `s2s_device_info` (customer's device/user agent)
</Accordion>

<Accordion title="Request Parameters" icon="fa-table">
  | Parameter                                                                             | Description                                                                                                                                                                                                                                                             | Example                                     |
  | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
  | `key`<br />`mandatory`                                                                | `String` Merchant key provided by PayU during onboarding.                                                                                                                                                                                                               | JPg\*\*\*\*f                                |
  | `txnid`<br />`mandatory`                                                              | `String` The transaction ID is a reference number for a specific order that is generated by the merchant.                                                                                                                                                               | ypl938459435                                |
  | `amount`<br />`mandatory`                                                             | `String` The payment amount for the transaction.                                                                                                                                                                                                                        | 10.00                                       |
  | `productinfo`<br />`mandatory`                                                        | `String` A brief description of the product.                                                                                                                                                                                                                            | iPhone                                      |
  | `firstname`<br />`mandatory`                                                          | `String` The first name of the customer.                                                                                                                                                                                                                                | Ashish                                      |
  | `lastname`<br />`mandatory`                                                           | `String` The last name of the customer.                                                                                                                                                                                                                                 | Kumar                                       |
  | `email`<br />`mandatory`                                                              | `String` The email address of the customer.                                                                                                                                                                                                                             | [abc@payu.in](mailto:abc@payu.in)           |
  | `phone`<br />`mandatory`                                                              | `String` The phone number of the customer.                                                                                                                                                                                                                              |                                             |
  | `address1`<br />`optional but recommended for higher approval rate`                   | `String` The first line of the billing address. H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai **Note**: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information. | 34 Saikripa-Estate, Tilak Nagar             |
  | `address2`<br />`optional but recommended for higher approval rate`                   | `String` The second line of the billing address.                                                                                                                                                                                                                        |                                             |
  | `city`<br />`optional but recommended for higher approval rate`                       | `String` The city where your customer resides as part of the billing address.                                                                                                                                                                                           | Mumbai                                      |
  | `state`<br />`optional but recommended for higher approval rate`                      | `String` The state where your customer resides as part of the billing address.                                                                                                                                                                                          | Maharashtra                                 |
  | `country`<br />`optional but recommended for higher approval rate`                    | `String` The country where your customer resides.                                                                                                                                                                                                                       | India                                       |
  | `zipcode`<br />`mandatory`                                                            | `String` Billing address zip code is mandatory for the cardless EMI option. Character Limit-20                                                                                                                                                                          | 400004                                      |
  | `pg`<br />`mandatory for seamless/s2s flow`                                           | `String` It defines the payment category and post **UPI**.                                                                                                                                                                                                              | UPI                                         |
  | `bankcode`<br />`mandatory for seamless/s2s flow`                                     | `String` Each payment option is identified with a unique bank code at PayU. For UPI Autopay, post **UPI**.                                                                                                                                                              | UPI                                         |
  | `surl`<br />`mandatory`                                                               | `String` The success URL, which is the page PayU will redirect to if the transaction is successful.                                                                                                                                                                     |                                             |
  | `furl`<br />`mandatory`                                                               | `String` The Failure URL, which is the page PayU will redirect to if the transaction is failed.                                                                                                                                                                         |                                             |
  | vpa `conditional`                                                                     | `String` Customer's VPA handle. Mandatory for UPI Collect flow.                                                                                                                                                                                                         | `customer@upi`                              |
  | si `mandatory`                                                                        | `String` Signifies successful consent taken from the user. Must be `1` for subscription setup.                                                                                                                                                                          | `1`                                         |
  | si\_details `mandatory`                                                               | `JSON String` JSON object containing mandate details (billingAmount, billingCurrency, billingCycle, etc.). Refer to si\_details JSON Object below.                                                                                                                      | See si\_details accordion                   |
  | txn\_s2s\_flow `conditional`                                                          | `Integer` Parameter to enable S2S flow. Must be `4` for Legacy Decoupled flow (UPI Intent).                                                                                                                                                                             | `4`                                         |
  | s2s\_client\_ip `conditional`                                                         | `String` Source IP of the customer. Required for UPI Intent flow.                                                                                                                                                                                                       | `10.200.12.12`                              |
  | s2s\_device\_info `conditional`                                                       | `String` Customer agent's device information. Required for UPI Intent flow.                                                                                                                                                                                             | `Mozilla/5.0 (Windows NT 10.0; Win64; x64)` |
  | `udf1`<br />`optional but recommended for higher approval rate`                                | `String` This parameter must contain the Buyer's PAN and date of birth in the following format (separated by two pipe characters): Buyer's PAN\\\|\\\|Buyer'sDOB                                                                                                        | AAAPZ1234C\\\|\\\|22/08/1972                |
  | `udf3`<br />`mandatory if AD bank request this detail`                                | `String` This parameter must contain the invoice ID of the transaction (generated by the merchant) and merchant name in the following format (separated by two pipe characters): Invoice ID\\\|\\\|MerchantName                                                         | INV-123\_1231\\\|\\\|MerchantName           |
  | buyer\_type\_business `optional in case of B2B transaction for cross-border payments` | `Binary` To be sent as "1" in case the buyer is a business. In case of individual buyers, it can be skipped. Default is "0". **Note**: This will be included in hash if posted (covered in next section                                                                 | 1                                           |
</Accordion>

<Accordion title="Hashing Logic" icon="fa-table">
  <PACB_Hashing />
</Accordion>

<Accordion title="si_details JSON Object" icon="fa-code">
  The `si_details` parameter is a JSON object containing mandate details:

  ```json
  {
    "billingAmount": "10.00",
    "billingCurrency": "INR",
    "billingCycle": "MONTHLY",
    "billingInterval": 1,
    "paymentStartDate": "2025-06-05",
    "paymentEndDate": "2025-12-01"
  }
  ```

  | Field                             | Description                                                                       | Example      |
  | --------------------------------- | --------------------------------------------------------------------------------- | ------------ |
  | billingAmount<br />`mandatory`    | `String`<br />Maximum amount for recurring transactions.                          | `10.00`      |
  | billingCurrency<br />`mandatory`  | `String`<br />Currency code.                                                      | `INR`        |
  | billingCycle<br />`mandatory`     | `String`<br />Billing frequency: `DAILY`, `WEEKLY`, `MONTHLY`, `YEARLY`, `ADHOC`. | `MONTHLY`    |
  | billingInterval<br />`mandatory`  | `Integer`<br />Interval between billing cycles.                                   | `1`          |
  | paymentStartDate<br />`mandatory` | `String`<br />Mandate start date (YYYY-MM-DD).                                    | `2025-06-05` |
  | paymentEndDate<br />`mandatory`   | `String`<br />Mandate end date (YYYY-MM-DD).                                      | `2025-12-01` |
</Accordion>

<Accordion title="Request Payload Structure" icon="fa-file-code">
  #### UPI Collect Flow

  ```json
  {
    "key": "JPM7Fg",
    "txnid": "upiConsentTxn12345",
    "amount": "10.00",
    "productinfo": "Monthly Subscription",
    "firstname": "Ashish",
      "lastname": "Kumar",
      "email": "abc@payu.in",
    "phone": "9988776655",
      "address1": "34 Saikripa-Estate, Tilak Nagar",
      "city": "Mumbai",
      "state": "Maharashtra",
      "country": "India",
      "zipcode": "400004",
    "surl": "https://example.com/success",
    "furl": "https://example.com/failure",
      "udf1": "AAAPZ1234C||22/08/1972",
      "udf3": "INV-123_1231||MerchantName",
      "buyer_type_business": "1",
    "pg": "UPI",
    "bankcode": "UPI",
    "vpa": "customer@upi",
    "api_version": "7",
    "si": "1",
    "si_details": "{\"billingAmount\":\"10.00\",\"billingCurrency\":\"INR\",\"billingCycle\":\"MONTHLY\",\"billingInterval\":1,\"paymentStartDate\":\"2025-06-05\",\"paymentEndDate\":\"2025-12-01\"}",
    "hash": "generated_hash_value"
  }
  ```

  #### UPI Intent Flow (with S2S Parameters)

  ```json
  {
    "key": "JPM7Fg",
    "txnid": "upiIntentTxn12345",
    "amount": "10.00",
    "productinfo": "Monthly Subscription",
    "firstname": "Ashish",
      "lastname": "Kumar",
      "email": "abc@payu.in",
    "phone": "9988776655",
      "address1": "34 Saikripa-Estate, Tilak Nagar",
      "city": "Mumbai",
      "state": "Maharashtra",
      "country": "India",
      "zipcode": "400004",
    "surl": "https://example.com/success",
    "furl": "https://example.com/failure",
      "udf1": "AAAPZ1234C||22/08/1972",
      "udf3": "INV-123_1231||MerchantName",
      "buyer_type_business": "1",
    "pg": "UPI",
    "bankcode": "INTENT",
    "api_version": "7",
    "si": "1",
    "si_details": "{\"billingAmount\":\"10.00\",\"billingCurrency\":\"INR\",\"billingCycle\":\"MONTHLY\",\"billingInterval\":1,\"paymentStartDate\":\"2025-06-05\",\"paymentEndDate\":\"2025-12-01\"}",
    "txn_s2s_flow": "4",
    "s2s_client_ip": "10.200.12.12",
      "s2s_device_info": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "hash": "generated_hash_value"
  }
  ```
</Accordion>

<Accordion title="Sample Requests" icon="fa-terminal" defaultOpen>
  <Accordion title="UPI Collect - cURL" icon="fa-code">
    ```bash
    curl --location --request POST 'https://test.payu.in/_payment' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'key=JPM7Fg' \
    --data-urlencode 'txnid=upiConsentTxn12345' \
    --data-urlencode 'amount=10.00' \
    --data-urlencode 'firstname=Ashish' \
    --data-urlencode 'lastname=Kumar' \
    --data-urlencode 'email=abc@payu.in' \
    --data-urlencode 'phone=9988776655' \
    --data-urlencode 'productinfo=Monthly Subscription' \
    --data-urlencode 'address1=34 Saikripa-Estate, Tilak Nagar' \
    --data-urlencode 'city=Mumbai' \
    --data-urlencode 'state=Maharashtra' \
    --data-urlencode 'country=India' \
    --data-urlencode 'zipcode=400004' \
    --data-urlencode 'surl=https://example.com/success' \
    --data-urlencode 'furl=https://example.com/failure' \
    --data-urlencode 'udf1=AAAPZ1234C||22/08/1972' \
    --data-urlencode 'udf3=INV-123_1231||MerchantName' \
    --data-urlencode 'buyer_type_business=1' \
    --data-urlencode 'pg=UPI' \
    --data-urlencode 'bankcode=UPI' \
    --data-urlencode 'vpa=customer@upi' \
    --data-urlencode 'api_version=7' \
    --data-urlencode 'si=1' \
    --data-urlencode 'si_details={"billingAmount":"10.00","billingCurrency":"INR","billingCycle":"MONTHLY","billingInterval":1,"paymentStartDate":"2025-06-05","paymentEndDate":"2025-12-01"}' \
    --data-urlencode 'hash=YOUR_CALCULATED_HASH'
    ```
  </Accordion>

  <Accordion title="UPI Intent - cURL" icon="fa-code">
    ```bash
    curl --location --request POST 'https://test.payu.in/_payment' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'key=JPM7Fg' \
    --data-urlencode 'txnid=upiIntentTxn12345' \
    --data-urlencode 'amount=10.00' \
    --data-urlencode 'firstname=Ashish' \
    --data-urlencode 'lastname=Kumar' \
    --data-urlencode 'email=abc@payu.in' \
    --data-urlencode 'phone=9988776655' \
    --data-urlencode 'productinfo=Monthly Subscription' \
    --data-urlencode 'address1=34 Saikripa-Estate, Tilak Nagar' \
    --data-urlencode 'city=Mumbai' \
    --data-urlencode 'state=Maharashtra' \
    --data-urlencode 'country=India' \
    --data-urlencode 'zipcode=400004' \
    --data-urlencode 'surl=https://example.com/success' \
    --data-urlencode 'furl=https://example.com/failure' \
    --data-urlencode 'udf1=AAAPZ1234C||22/08/1972' \
    --data-urlencode 'udf3=INV-123_1231||MerchantName' \
    --data-urlencode 'buyer_type_business=1' \
    --data-urlencode 'pg=UPI' \
    --data-urlencode 'bankcode=INTENT' \
    --data-urlencode 'api_version=7' \
    --data-urlencode 'si=1' \
    --data-urlencode 'si_details={"billingAmount":"10.00","billingCurrency":"INR","billingCycle":"MONTHLY","billingInterval":1,"paymentStartDate":"2025-06-05","paymentEndDate":"2025-12-01"}' \
    --data-urlencode 'txn_s2s_flow=4' \
    --data-urlencode 's2s_client_ip=10.200.12.12' \
    --data-urlencode 's2s_device_info=Mozilla/5.0 (Windows NT 10.0; Win64; x64)' \
    --data-urlencode 'hash=YOUR_CALCULATED_HASH'
    ```
    ```python
    import requests
    import json
    import hashlib

    url = 'https://test.payu.in/_payment'

    # SI Details
    si_details = {
        'billingAmount': '10.00',
        'billingCurrency': 'INR',
        'billingCycle': 'MONTHLY',
        'billingInterval': 1,
        'paymentStartDate': '2025-06-05',
        'paymentEndDate': '2025-12-01'
    }

    si_details_json = json.dumps(si_details)

    # UPI Intent Payload with S2S parameters
    payload = {
        'key': 'JPM7Fg',
        'txnid': 'upiIntentTxn12345',
        'amount': '10.00',
        'productinfo': 'Monthly Subscription',
        'firstname': 'Ashish',
        'lastname': 'Kumar',
        'email': 'abc@payu.in',
        'phone': '9988776655',
        'address1': '34 Saikripa-Estate, Tilak Nagar',
        'city': 'Mumbai',
        'state': 'Maharashtra',
        'country': 'India',
        'zipcode': '400004',
        'surl': 'https://example.com/success',
        'furl': 'https://example.com/failure',
        'udf1': 'AAAPZ1234C||22/08/1972',
        'udf3': 'INV-123_1231||MerchantName',
        'buyer_type_business': '1',
        'pg': 'UPI',
        'bankcode': 'INTENT',
        'api_version': '7',
        'si': '1',
        'si_details': si_details_json,
        'txn_s2s_flow': '4',
        's2s_client_ip': '10.200.12.12',
        's2s_device_info': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'hash': hash_value  # Generated hash
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        print('Response:', response_data)
        # Process the response
    else:
        print(f'Error: {response.status_code}')
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $si_details = json_encode([
        'billingAmount' => '10.00',
        'billingCurrency' => 'INR',
        'billingCycle' => 'MONTHLY',
        'billingInterval' => 1,
        'paymentStartDate' => '2025-06-05',
        'paymentEndDate' => '2025-12-01'
    ]);

    // UPI Intent with S2S parameters
    $data = [
        'key' => 'JPM7Fg',
        'txnid' => 'upiIntentTxn12345',
        'amount' => '10.00',
        'productinfo' => 'Monthly Subscription',
        'firstname' => 'Ashish',
        'lastname' => 'Kumar',
        'email' => 'abc@payu.in',
        'phone' => '9988776655',
        'address1' => '34 Saikripa-Estate, Tilak Nagar',
        'city' => 'Mumbai',
        'state' => 'Maharashtra',
        'country' => 'India',
        'zipcode' => '400004',
        'surl' => 'https://example.com/success',
        'furl' => 'https://example.com/failure',
        'udf1' => 'AAAPZ1234C||22/08/1972',
        'udf3' => 'INV-123_1231||MerchantName',
        'buyer_type_business' => '1',
        'pg' => 'UPI',
        'bankcode' => 'INTENT',
        'api_version' => '7',
        'si' => '1',
        'si_details' => $si_details,
        'txn_s2s_flow' => '4',
        's2s_client_ip' => $_SERVER['REMOTE_ADDR'],
        's2s_device_info' => $_SERVER['HTTP_USER_AGENT'],
        'hash' => $hash // Generated hash
    ];

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/x-www-form-urlencoded'
    ]);

    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    if ($httpCode == 200) {
        $responseData = json_decode($response, true);
        print_r($responseData);
    } else {
        echo "Error: " . $httpCode;
    }
    ?>
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const siDetails = JSON.stringify({
        billingAmount: '10.00',
        billingCurrency: 'INR',
        billingCycle: 'MONTHLY',
        billingInterval: 1,
        paymentStartDate: '2025-06-05',
        paymentEndDate: '2025-12-01'
    });

    // UPI Intent with S2S parameters
    const payload = {
        key: 'JPM7Fg',
        txnid: 'upiIntentTxn12345',
        amount: '10.00',
        productinfo: 'Monthly Subscription',
        firstname: 'Ashish',
        lastname: 'Kumar',
        email: 'abc@payu.in',
        phone: '9988776655',
        address1: '34 Saikripa-Estate, Tilak Nagar',
        city: 'Mumbai',
        state: 'Maharashtra',
        country: 'India',
        zipcode: '400004',
        surl: 'https://example.com/success',
        furl: 'https://example.com/failure',
        udf1: 'AAAPZ1234C||22/08/1972',
        udf3: 'INV-123_1231||MerchantName',
        buyer_type_business: '1',
        pg: 'UPI',
        bankcode: 'INTENT',
        api_version: '7',
        si: '1',
        si_details: siDetails,
        txn_s2s_flow: '4',
        s2s_client_ip: '10.200.12.12',
        s2s_device_info: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        hash: hash // Generated hash
    };

    axios.post(url, qs.stringify(payload), {
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => {
        console.log('Response:', response.data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
    ```
  </Accordion>
</Accordion>

<Callout icon="📘" theme="info">
  **Note**: Before you make payment request to PayU, it is recommended to validate the UPI handle provided by your customer is eligible for recurring payment using the validateVPA API. For more information, refer to [Validate VPA API](ref:validate_vpa_api).
</Callout>

***

### Step 2: Check the Response from PayU

The API returns different response structures for UPI Collect and UPI Intent flows.

<Accordion title="UPI Collect Response" icon="fa-check">
  For UPI Collect, the response is returned in URL-encoded format (application/x-www-form-urlencoded):

  ```plaintext
  eyJzdGF0dXMiOiJzdWNjZXNzIiwicmVzdWx0Ijp7Im1paHBheWlkIjoiNzYwMTI2NTU4NSIsIm1vZGUiOiJVUEkiLCJzdGF0dXMiOiJwZW5kaW5nIiwia2V5IjoiTWVyY2hhbnRLZXkiLCJ0eG5pZCI6IjZiMmYzZDY4NWVjMWJiYTdkZDRiIiwiYW1vdW50IjoiMTAuMDAiLCJhZGRlZG9uIjoiMjAxOC0xMS0wMSAxOTo1NjozMiIsInByb2R1Y3RpbmZvIjoiUHJvZHVjdCBJbmZvIiwiZmlyc3RuYW1lIjoiUGF5dS1Vc2VyIiwibGFzdG5hbWUiOiIiLCJhZGRyZXNzMSI6IiIsImFkZHJlc3MyIjoiIiwiY2l0eSI6IiIsInN0YXRlIjoiIiwiY291bnRyeSI6IiIsInppcGNvZGUiOiIiLCJlbWFpbCI6InRlc3RAZXhhbXBsZS5jb20iLCJwaG9uZSI6IjEyMzQ1Njc4OTAiLCJ1ZGYxIjoiIiwidWRmMiI6IiIsInVkZjMiOiIiLCJ1ZGY0IjoiIiwidWRmNSI6IiIsInVkZjYiOiIiLCJ1ZGY3IjoiIiwidWRmOCI6IiIsInVkZjkiOiIiLCJ1ZGYxMCI6IiIsImNhcmRfdG9rZW4iOiIiLCJjYXJkX25vIjoiIiwiZmllbGQwIjoiIiwiZmllbGQxIjoiYWJjZEB1cGkiLCJmaWVsZDIiOiIiLCJmaWVsZDMiOiIiLCJmaWVsZDQiOiIiLCJmaWVsZDUiOiIiLCJmaWVsZDYiOiIiLCJmaWVsZDciOiIiLCJmaWVsZDgiOiIiLCJmaWVsZDkiOiIiLCJwYXltZW50X3NvdXJjZSI6InBheXVQdXJlUzJTIiwiUEdfVFlQRSI6IkFYSVNVIiwiZXJyb3IiOiJFMDAwIiwiZXJyb3JfTWVzc2FnZSI6Ik5vIEVycm9yIiwibmV0X2Ftb3VudF9kZWJpdCI6IjAiLCJhZGRpdGlvbmFsQ2hhcmdlcyI6IjI5LjUiLCJ1bm1hcHBlZHN0YXR1cyI6ImluIHByb2dyZXNzIiwiaGFzaCI6IjU2NzQ3OGE5ZDUyMzhlZTIyZGFhMDM2ZWMwMjAxMzk0OGY2YjgwNGUzMWNhYzNkYmQyMDc1NmU5ZjFkNDFlMjI4ZTQxYzJkYjcwZmU4ZWRlZmMyNDBiOTQwODZlN2QzN2Y4ZDQ2OTA4MzU4Y2NjNzA4Y2JjNWVlNTJjMjlkYWEwIiwiYmFua19yZWZfbm8iOiJBWEk5MTEwMDAwMDAwMDQ5MTg0NzY2MTU0MTc5OTcwNTY5OCIsImJhbmtfcmVmX251bSI6IkFYSTkxMTAwMDAwMDAwNDkxODQ3NjYxNTQxNzk5NzA1Njk4IiwiYmFua2NvZGUiOiJVUEkiLCJzdXJsIjoiaHR0cHM6XC9cL2FkbWluLnBheXUuaW5cL3Rlc3RfcmVzcG9uc2UiLCJjdXJsIjoiaHR0cHM6XC9cL2FkbWluLnBheXUuaW5cL3Rlc3RfcmVzcG9uc2UiLCJmdXJsIjoiaHR0cHM6XC9cL2FkbWluLnBheXUuaW5cL3Rlc3RfcmVzcG9uc2UifX0
  ```

  **Base64 decoded response:**

  ```plaintext
  {"status":"success","result":{"mihpayid":"7601265585","mode":"UPI","status":"pending","key":"MerchantKey","txnid":"6b2f3d685ec1bba7dd4b","amount":"10.00","addedon":"2018-11-01
  19:56:32","productinfo":"ProductInfo","firstname":"PayuUser","lastname":"","address1":"","address2":"","city":"","state":"","country":"","zipcode":"","email":"test@example.com","phone":"1234567890","udf1":"","udf2":"","udf3":"","udf4":"","udf5":"","udf6":"","udf7":"","udf8":"","udf9":"","udf10":"","card_token":"","card_no":"","field0":"","field1":"abcd@upi","field2":"","field3":"","field4":"","field5":"","field6":"","field7":"","field8":"","field9":"","payment_source":"payuPureS2S","PG_TYPE":"AXISU","error":"E000","error_Message":"NoError","net_amount_debit":"0","additionalCharges":"29.5","unmappedstatus":"inprogress","hash":"567478a9d5238ee22daa036ec02013948f6b804e31cac3dbd20756e9f1d41e228e41c2db70fe8edefc240b94086e7d37f8d46908358ccc708cbc5ee52c29daa0","bank_ref_no":"AXI91100000000491847661541799705698","bank_ref_num":"AXI91100000000491847661541799705698","bankcode":"UPI","surl":"https:\/\/admin.payu.in\/test_response","curl":"https:\/\/admin.payu.in\/test_response","furl":"https:\/\/admin.payu.in\/test_response"}}
  ```
</Accordion>

<Accordion title="UPI Intent Response" icon="fa-check">
  For UPI Intent with S2S flow, the response is a JSON object containing the intent URI:

  ```json
  {
     "metaData": {
        "message": null,
        "referenceId": "5ae6e6d94b4b5f9dee282b95f6020c98",
        "statusCode": null,
        "txnId": "upiIntentTxn12345",
        "txnStatus": "pending",
        "unmappedStatus": "pending"
     },
     "result": {
        "paymentId": "15257049438",
        "merchantName": "Your Merchant Name",
        "merchantVpa": "merchant@hdfcbank",
        "amount": "10.00",
        "intentURIData": "upi://mandate?pa=merchant@hdfcbank&pn=MERCHANT NAME&mn=&tid=upiIntentTxn12345&validitystart=05062025&validityend=01122025&am=10.00&amrule=MAX&recur=MONTHLY&recurvalue=30&recurtype=&tr=15257049438&cu=INR&mc=5411&tn=UPI Transaction for upiIntentTxn12345&mode=13&purpose=14&orgid=159240&rev=Y&block=N&txnType=CREATE",
        "postToBank": {
           "token": "C6ABAA6A-F0CE-432A-61C1-CFA48EDE847B",
           "amount": "10.00",
           "mihpayid": "5ae6e6d94b4b5f9dee282b95f6020c98",
           "disableIntentSeamlessFailure": "0",
           "payeeVpa": "merchant@hdfcbank",
           "payeeName": "Your Merchant Name",
           "additionalCharges": 0,
           "transactionFee": "10.00"
        },
        "issuerUrl": "https://secure.payu.in/intentSeamlessHandler.php"
     }
  }
  ```
</Accordion>

<Accordion title="Response Handling Logic" icon="fa-info-circle">
  ### Handling UPI Intent Response

  1. Extract the `intentURIData` from the response
  2. Launch the UPI app using the intent URI
  3. Wait for the customer to approve the mandate
  4. Receive the final status via webhook or callback
</Accordion>

<Callout icon="📘" theme="info">
  If you want to use PayU's timer page for UPI collect, you can use the **result.acsTemplate** and **base64decode** it to redirect the customer on given HTML.
</Callout>

***

### Step 3: Configure Webhooks

Configure webhooks to receive real-time transaction status updates. PayU will send POST requests to your webhook URL.

<Accordion title="Webhook Configuration" icon="fa-cog">
  You can configure the webhook from Payu dashboard directly for payment success/failure events. For more information, refer to [Create a New Webhook](https://docs.payu.in/docs/create-a-new-webhook). Once configured, you will receive transaction updates via HTTP POST.
</Accordion>

<Accordion title="Webhook Payload Example" icon="fa-code">
  ```text
  unmappedstatus=success&phone=9988776655&txnid=upiConsentTxn12345&hash=84e335094bbcb2ddaa0f9a488eb338e143b273765d89c9dfa502402562d0b6f3c7935e28194ca92f380be7c84c3695415b106dcf52cb016a15fcf6adc98d724&status=success&firstname=Ashish&productinfo=Monthly Subscription&mode=UPI&amount=10.00&email=test@payu.in&mihpayid=403993715525317379&surl=https://example.com/success&payment_source=sist
  ```
</Accordion>

<Accordion title="Webhook Validation" icon="fa-lock">
  Always validate the webhook hash before processing:

  ```php
  function validateWebhookHash($response, $salt) {
      $hashSequence = "status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key";
      $hashVarsSeq = explode('|', $hashSequence);
      
      $hashString = $salt . '|';
      foreach(array_reverse($hashVarsSeq) as $hashVar) {
          $hashString .= isset($response[$hashVar]) ? $response[$hashVar] : '';
          $hashString .= '|';
      }
      $hashString = rtrim($hashString, '|');
      
      $calculatedHash = strtolower(hash('sha512', $hashString));
      $receivedHash = strtolower($response['hash']);
      
      return $calculatedHash === $receivedHash;
  }
  ```
</Accordion>

<Accordion title="Expected Values for Successful Registration" icon="fa-table">
  | Response Parameter | Expected Value | Description                                                               |
  | ------------------ | -------------- | ------------------------------------------------------------------------- |
  | status             | `success`      | Indicates that the transaction is successful with the UPI provider        |
  | payment\_source    | `sist`         | Indicates UPI details have been marked correctly for Standing Instruction |
  | mihpayid           | `<mihpayid>`   | PayU's transaction acknowledgment for a Consent transaction               |
</Accordion>

<Accordion title="Handling Mandate Status Updates" icon="fa-bell">
  If the mandate is not confirmed by the customer or is rejected by the bank, the status is communicated as "failure" over webhook.

  | Status    | Description                                       |
  | --------- | ------------------------------------------------- |
  | `success` | Mandate registered successfully                   |
  | `failure` | Mandate registration failed or rejected           |
  | `pending` | Mandate registration is pending customer approval |

  For more information, refer to [Set up WebHook to Receive Cancellation or Modification Update from the Issuer Bank](ref:set-up-webhook-to-receive-cancellation-or-modification-update-from-the-issuer-bank).
</Accordion>

***

### Step 4: Verify Mandate Registration

After successful registration, verify the mandate status:

<Accordion title="Verification Checklist" icon="fa-check-circle">
  1. **Check Response Parameters**:
     * `status` should be `success`
     * `payment_source` should be `sist`
     * `mihpayid` should not be null

  2. **Store Mandate Details**:
     * Save `mihpayid` for future recurring payments
     * Save mandate expiry dates from `si_details`
     * Store customer's VPA for reference

  3. **Test Subsequent Payment**:
     * Use the stored mandate details to initiate a subsequent recurring payment
     * Verify the payment processes successfully
</Accordion>

<PACB_Recurring_Payments_Flow />

## Related Documentation

* [UPI Consent Transaction API Reference](ref:upi-recurring-payment-consent-transaction)
* [SI Parameter JSON Details](ref:si-parameter-json-details)
* [Manage UPI Recurring Transaction](ref:api-commands-to-manage-upi-recurring-transaction)
* [Validate VPA API](ref:validate_vpa_api)
* [Bank Codes - Recurring Payments](doc:bank-codes-recurring-payments)