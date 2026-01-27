---
title: Apple Pay - Direct Authorization Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
This section provides a comprehensive guide for integrating Apple Pay Seamless Flow with PayU's Server-to-Server (S2S) Direct Authorization using `txn_s2s_flow=3`. This approach enables direct authorization of pre-authenticated Apple Pay transactions through server-to-server communication.

## Understanding S2S Direct Authorization Flow

### Key Characteristics of txn_s2s_flow=3

* **Direct Authorization**: Process pre-authenticated transactions
* **3DS Support**: Handle 3DS/3DS2 authentication data
* **Server-to-Server**: No browser redirects required
* **Real-time Response**: Immediate authorization results

### Flow Sequence

1. Merchant receives Apple Pay token with authentication data
2. Extract 3DS authentication information from Apple Pay token
3. Prepare Direct Authorization request with `txn_s2s_flow=3`
4. Send authorization request to PayU
5. Receive base64-encoded response
6. Decode and verify response hash
7. Process authorization result

## Step 1: S2S Direct Authorization Request

### Request Parameters

| Parameter                            | Description                                     | Example                                                        |
| ------------------------------------ | ----------------------------------------------- | -------------------------------------------------------------- |
| key<br />`mandatory`                 | `string` PayU merchant key                      | "your_merchant_key"                                            |
| txnid<br />`mandatory`               | `string` Unique transaction ID                  | "TXN123456789"                                                 |
| amount<br />`mandatory`              | `string` Transaction amount                     | "100.00"                                                       |
| productinfo<br />`mandatory`         | `string` Product description                    | "iPhone 15 Pro"                                                |
| firstname<br />`mandatory`           | `string` Customer first name                    | "John"                                                         |
| email<br />`mandatory`               | `string` Customer email                         | "[john@example.com](mailto:john@example.com)"                  |
| phone<br />`mandatory`               | `string` Customer phone number                  | "+1234567890"                                                  |
| pg<br />`mandatory`                  | `string` Payment gateway; set to "APPLEPAY"     | "APPLEPAY"                                                     |
| bankcode<br />`mandatory`            | `string` Bank code; set to "CCAP" or "APPLEPAY" | "CCAP"                                                         |
| ccnum<br />`mandatory`               | `string` Decrypted card number                  | "4111111111111111"                                             |
| ccname<br />`mandatory`              | `string` Cardholder name                        | "John Doe"                                                     |
| ccexpmon<br />`mandatory`            | `string` Expiry month (MM)                      | "12"                                                           |
| ccexpyr<br />`mandatory`             | `string` Expiry year (YYYY)                     | "2025"                                                         |
| ccvv<br />`mandatory`                | `string` CVV code                               | "123"                                                          |
| txn_s2s_flow<br />`mandatory`        | `string` Transaction flow type; set to "3"      | "3"                                                            |
| authentication_info<br />`mandatory` | `string` JSON with 3DS authentication data      | '\{"threeDSData":"..."}'                                       |
| s2s_client_ip<br />`mandatory`       | `string` Client IP address                      | "192.168.1.1"                                                  |
| s2s_device_info<br />`mandatory`     | `string` Device information JSON                | '\{"deviceId":"..."}'                                          |
| hash<br />`mandatory`                | `string` SHA512 request hash                    | "abc123def456..."                                              |
| surl<br />`mandatory`                | `string` Success URL                            | "[https://merchant.com/success](https://merchant.com/success)" |
| furl<br />`mandatory`                | `string` Failure URL                            | "[https://merchant.com/failure](https://merchant.com/failure)" |

<Accordion title="Understanding Hashing and sample code" icon="fa-code">
  <HashingRequestParameters />

  #### Hashing Sample Code

  <HashingSample />
</Accordion>

### Authentication Info JSON Structure

```json
{
  "eci": "05",
  "cavv": "base64_encoded_cavv",
  "flowType": "APPLEPAY",
  "threeDSTransID": "apple_transaction_id",
  "threeDSServerTransID": "server_transaction_id",
  "threeDSTransStatus": "Y",
  "threeDSTransStatusReason": "01",
  "acquirer_bin": "000000",
  "additionalinfo": "{"appleTransactionId":"...","network":"Visa"}"
}
```

### 3DS2 Request Data JSON (when applicable)

```json
{
  "threeDSVersion": "2.2.0",
  "deviceChannel": "BRW",
  "userAgent": "Mozilla/5.0...",
  "acceptHeader": "text/html,application/xhtml+xml...",
  "language": "en-US",
  "colorDepth": 24,
  "screenHeight": 1080,
  "screenWidth": 1920,
  "timeZone": 330,
  "javaEnabled": false
}
```

### Sample Request

```bash
curl -X POST "https://test.payu.in/_payment"   
-H "Content-Type: application/x-www-form-urlencoded"   
-H "Accept: application/json"   
-d "key=your_merchant_key"   
-d "txnid=APPLEPAY_DA_$(date +%s)_$(openssl rand -hex 4)"   
-d "amount=100.00"   
-d "productinfo=Apple Pay Direct Authorization"   
-d "firstname=John"   
-d "email=john@example.com"   
-d "phone=9876543210"   
-d "pg=APPLEPAY"   
-d "bankcode=CCAP"   
-d "ccnum=4111111111111111"   
-d "ccname=Apple Pay User"   
-d "ccexpmon=12"   
-d "ccexpyr=2025"   
-d "ccvv=123"   
-d "txn_s2s_flow=3"   
-d "authentication_info={"eci":"05","cavv":"AAABCIEFEwAAAAECAwQFBgc=","flowType":"APPLEPAY","threeDSTransID":"$(openssl rand -hex 16)","threeDSTransStatus":"Y","acquirer_bin":"000000"}"   -d "threeDS2RequestData={"threeDSVersion":"2.2.0","deviceChannel":"BRW"}"   
-d "s2s_client_ip=192.168.1.1"   
-d "s2s_device_info={"device_type":"web","user_agent":"Mozilla/5.0"}"   
-d "surl=https://yourapp.com/success"   
-d "furl=https://yourapp.com/failure"   -d "hash=calculated_hash"
```

## Step 2: Check Response from PayU

The Direct Authorization API returns a **base64-encoded** response that needs to be decoded:

```json
{
  "status": "success",
  "result": {
    "mihpayid": "403993715527623137",
    "mode": "APPLEPAY",
    "status": "success",
    "key": "your_merchant_key",
    "txnid": "APPLEPAY_DA_1703845200_a1b2c3d4", 
    "amount": "100.00",
    "addedon": "2023-12-29 10:30:00",
    "productinfo": "Apple Pay Direct Authorization",
    "firstname": "John",
    "lastname": "",
    "email": "john@example.com",
    "phone": "9876543210",
    "udf1": "",
    "udf2": "",
    "udf3": "",
    "udf4": "",
    "udf5": "",
    "card_no": "XXXXXXXXXXXX1111",
    "card_token": "token_value",
    "net_amount_debit": "100.00",
    "discount": "0.00",
    "unmappedstatus": "captured",
    "payment_source": "dirAuthS2S",
    "PG_TYPE": "APPLEPAY-PG",
    "error": "No Error",
    "error_Message": "",
    "bank_ref_no": "AP123456789",
    "bankcode": "CCAP",
    "card_hash": "hash_value",
    "hash": "response_hash"
  }
}
```

## Step 3: Verify the Payment

<Verify_Payment_Tabs />
