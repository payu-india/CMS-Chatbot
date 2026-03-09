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

## Step 1: Initiate Payment Session

Initiate the payment session similar to the following cURL request:

```curl
curl --location 'https://secure.payu.in/seamless/Session' \
--header 'Content-Type: application/json' \
--header 'mid: 2' \
--data '{
    "validationUrl": "https://apple-pay-gateway.apple.com/paymentservices/paymentSession",
    "txnid": "06fb0aa23eaeb32772e18"
  }'
```

## Step 2: Authorize Transaction

<Apple_Pay_Step1 />

## Step 3: Check Response from PayU

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
