---
title: 'Apple Pay - S2S Decoupled Flow Integration '
deprecated: false
hidden: true
metadata:
  robots: index
---
This section provides comprehensive documentation for integrating Apple Pay with PayU's Server-to-Server (S2S) Decoupled Flow using `txn_s2s_flow=4`. The Decoupled Flow enables asynchronous payment processing where the payment authorization and completion happen in separate stages, providing enhanced control and flexibility for complex payment scenarios.

## Implementation Flow

### High-Level Flow Steps

1. **Initialize Payment**: Create payment session with Apple Pay token
2. **Prepare Request**: Build S2S Decoupled Flow request parameters
3. **Generate Hash**: Create SHA-512 hash for request authentication
4. **Submit Authorization**: Send initial authorization request
5. **Process Response**: Handle asynchronous response processing
6. **Verify Status**: Confirm payment status via verification APIs
7. **Complete Transaction**: Finalize payment based on business logic

## Step 1: Post the Payment Request

|            |                                                 |
| :--------- | :---------------------------------------------- |
| Production | https://secure.payu.in/AuthorizeTransaction.php |

### Request Parameters

| Parameter                        | Description                               | Example                                                      |
| -------------------------------- | ----------------------------------------- | ------------------------------------------------------------ |
| key<br />`mandatory`             | `string` PayU merchant key                | "gtKFFx"                                                     |
| txnid<br />`mandatory`           | `string` Unique transaction ID            | "APPLEPAY_DECOUP_1703845200"                                 |
| amount<br />`mandatory`          | `string` Transaction amount               | "100.00"                                                     |
| productinfo<br />`mandatory`     | `string` Product description              | "Apple Pay Decoupled Payment"                                |
| firstname<br />`mandatory`       | `string` Customer first name              | "John"                                                       |
| email<br />`mandatory`           | `string` Customer email address           | "[john@example.com](mailto:john@example.com)"                |
| mobile<br />`mandatory`          | `string` Customer mobile number           | "9876543210"                                                 |
| txn_s2s_flow<br />`mandatory`    | `string` Set to "4" for decoupled flow    | "4"                                                          |
| pg<br />`mandatory`              | `string` Payment gateway identifier       | "APPLEPAY"                                                   |
| bankcode<br />`mandatory`        | `string` Bank/payment method code         | "CCAP"                                                       |
| apple_pay_token<br />`mandatory` | `string` JSON stringified Apple Pay token | '\{"paymentData":\{...}}'                                    |
| s2s_client_ip<br />`mandatory`   | `string` Client IP address                | "192.168.1.1"                                                |
| s2s_device_info<br />`mandatory` | `string` Device information JSON          | '\{"device_type":"web"}'                                     |
| hash<br />`mandatory`            | `string` SHA-512 request hash             | "calculated_hash"                                            |
| surl<br />`mandatory`            | `string` Success URL                      | "[https://yourapp.com/success](https://yourapp.com/success)" |
| furl<br />`mandatory`            | `string` Failure URL                      | "[https://yourapp.com/failure](https://yourapp.com/failure)" |
| lastname<br />`optional`         | `string` Customer last name               | "Doe"                                                        |
| address1<br />`optional`         | `string` Customer address line 1          | "123 Main St"                                                |
| address2<br />`optional`         | `string` Customer address line 2          | "Apt 4B"                                                     |
| city<br />`optional`             | `string` Customer city                    | "Mumbai"                                                     |
| state<br />`optional`            | `string` Customer state                   | "Maharashtra"                                                |
| country<br />`optional`          | `string` Customer country                 | "India"                                                      |
| zipcode<br />`optional`          | `string` Customer postal code             | "400001"                                                     |
| udf1<br />`optional`             | `string` User defined field 1             | "custom_value_1"                                             |
| udf2<br />`optional`             | `string` User defined field 2             | "custom_value_2"                                             |
| udf3<br />`optional`             | `string` User defined field 3             | "custom_value_3"                                             |
| udf4<br />`optional`             | `string` User defined field 4             | "custom_value_4"                                             |
| udf5<br />`optional`             | `string` User defined field 5             | "custom_value_5"                                             |
| phone<br />`optional`            | `string` Alternative phone number         | "9876543211"                                                 |

### Sample Request

```curl
curl --location 'https://secure.payu.in/AuthorizeTransaction.php' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key={{key}}' \
--data-urlencode 'txnid={{txnid}}' \
--data-urlencode 'authentication_info={{info}}' \
--data-urlencode 'hash={{hash1}}' \
--data-urlencode 'pg=ApplePay' \
--data-urlencode 'bankcode=CCAP' \
--data-urlencode 'firstname=John' \
--data-urlencode 'country=IN' \
--data-urlencode 'city=Banglore' \
--data-urlencode 'state=KA' \
--data-urlencode 'email=abc@gmail.com' \
--data-urlencode 'address1=street1 area' \
--data-urlencode 'udf1=appleTransactionIdentifier' \
--data-urlencode 'udf2=MAST:credit' \
--data-urlencode 'lastname=Bing' \
--data-urlencode 'zipcode=45678' \
--data-urlencode 'phone=9876543210' \
--data-urlencode 'productinfo=ABC info' \
--data-urlencode 'amount={{amt}}'
```

<br />

<br />

### Sample Response

#### Initial S2S Response

The S2S Decoupled Flow returns an initial response indicating the payment has been queued for processing:

```json
{
  "status": "pending",
  "txnid": "APPLEPAY_DECOUP_1703845200_a1b2c3d4",
  "amount": "100.00",
  "productinfo": "Apple Pay Decoupled Payment",
  "firstname": "John",
  "email": "john@example.com",
  "mihpayid": "403993715527623137",
  "mode": "APPLEPAY",
  "bankcode": "CCAP",
  "PG_TYPE": "APPLEPAY-PG",
  "bank_ref_num": "AP123456789",
  "unmappedstatus": "pending",
  "addedon": "2023-12-29 10:30:00",
  "payment_source": "s2sDecoupledFlow",
  "net_amount_debit": "100.00",
  "hash": "response_hash",
  "message": "Payment initiated successfully. Processing asynchronously.",
  "decoupled_flow_id": "DCF_123456789"
}
```

#### Success Response (After Processing)

```json
{
  "status": "success",
  "txnid": "APPLEPAY_DECOUP_1703845200_a1b2c3d4",
  "amount": "100.00",
  "productinfo": "Apple Pay Decoupled Payment", 
  "firstname": "John",
  "lastname": "Doe",
  "email": "john@example.com",
  "phone": "9876543210",
  "mihpayid": "403993715527623137",
  "mode": "APPLEPAY",
  "status": "success",
  "unmappedstatus": "captured",
  "key": "gtKFFx",
  "bankcode": "CCAP",
  "PG_TYPE": "APPLEPAY-PG",
  "bank_ref_num": "AP123456789",
  "bank_ref_no": "AP123456789",
  "cardnum": "XXXXXXXXXXXX1234",
  "card_hash": "card_hash_value",
  "name_on_card": "Apple Pay User",
  "issuing_bank": "HDFC Bank",
  "card_type": "VISA",
  "net_amount_debit": "100.00",
  "discount": "0.00",
  "addedon": "2023-12-29 10:30:00",
  "payment_source": "s2sDecoupledFlow",
  "udf1": "custom_field_1",
  "udf2": "custom_field_2", 
  "udf3": "custom_field_3",
  "udf4": "custom_field_4",
  "udf5": "custom_field_5",
  "field1": "transaction_date",
  "field2": "bank_name",
  "field3": "payment_gateway_name",
  "field4": "card_country",
  "field5": "pg_mid",
  "field6": "eci_value",
  "field7": "payment_gateway_capture_date",
  "field8": "auth_status",
  "field9": "final_capture_amount",
  "hash": "response_hash",
  "error": "No Error",
  "error_Message": "",
  "decoupled_flow_id": "DCF_123456789",
  "processing_time_ms": 2534
}
```

#### Failure Response

```json
{
  "status": "failure",
  "txnid": "APPLEPAY_DECOUP_1703845200_a1b2c3d4",
  "amount": "100.00",
  "productinfo": "Apple Pay Decoupled Payment",
  "firstname": "John",
  "email": "john@example.com",
  "mihpayid": "403993715527623137",
  "mode": "APPLEPAY",
  "unmappedstatus": "failed",
  "bankcode": "CCAP",
  "PG_TYPE": "APPLEPAY-PG",
  "bank_ref_num": "",
  "error": "Transaction declined by issuing bank",
  "error_Message": "Insufficient funds",
  "error_code": "E001",
  "hash": "response_hash",
  "addedon": "2023-12-29 10:30:00",
  "payment_source": "s2sDecoupledFlow",
  "decoupled_flow_id": "DCF_123456789"
}
```
