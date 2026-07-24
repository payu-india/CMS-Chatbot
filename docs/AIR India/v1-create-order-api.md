---
title: V1 Create Order API
deprecated: false
hidden: false
metadata:
  robots: index
---
Initiates the Air India checkout journey. Creates an order, returns available payment methods, and provides an access token for subsequent API calls. Supports pre-authorization via `additionalInfo.preAuthorize`.

## Endpoint

| Environment | Base URL |
|-------------|----------|
| Test | `https://apitest.payu.in/v1/checkout/l1` |
| Production | `https://api.payu.in/v1/checkout/l1` |

## Request Parameters

<HeaderAuthentication />

### Body Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| orderId<br/>`mandatory` | `string` Unique merchant order identifier. Maximum length: 255 characters. | `ORD123446789` |
| currency<br/>`mandatory` | `string` ISO 4217 currency code. | `INR` |
| paymentSource<br/>`mandatory` | `string` Payment source. Set this value to `direct`. | `direct` |
| order<br/>`mandatory` | `object` Order details container. | `{"amount":18902.00,"productinfo":"Tickets"}` |
| order.amount<br/>`mandatory` | `number` Final payable amount as a decimal value. | `18902.00` |
| order.productinfo<br/>`optional` | `string` Product or order description displayed for the payment. | `Tickets` |
| customer<br/>`optional` | `object` Customer details container. For more information, refer to [customer JSON Object Fields Description](customer-json-object-fields-description) |  |
| callBackActions<br/>`mandatory` | `object` Callback URL container. For more information, refer to [callBackActions JSON Fields Description](#callbackaction-json-fields-description) |  |
| additionalInfo<br/>`optional` | `object` Additional order and routing metadata. For more information, refer to [additionalInfo JSON Object Fields Description](#additionalinfo-json-object-fields-description) | |
| merchantCacheExpiry<br/>`conditional` | `number` Cache expiration time expressed as a Unix epoch timestamp. | `1798761599` |
| udf1 - udf5<br/>`optional` | `string` Merchant-defined values passed in `additionalInfo.routingParam`. | `User Defined Field 1` |

#### customer JSON Object Fields Description
| Field | Description | Example |
|-----------|-------------|---------|
| firstName<br/>`optional` | `string` Customer's first name. | `John` |
| lastName<br/>`optional` | `string` Customer's last name. | `Doe` |
| email<br/>`optional` | `string` Customer's valid email address. | `john.doe@example.com` |
| phoneNumber<br/>`optional` | `string` Customer's phone number. | `9886575652` |
| address<br/>`optional` | `object` Container for the customer's billing and shipping addresses. | `{"billingAddress":{"city":"New Delhi"}}` |
| address.billingAddress<br/>`optional` | `object` Customer's billing address. | `{"name":"John Doe","pincode":"110001","country":"IN"}` |
| address.shippingAddress<br/>`optional` | `object` Customer's shipping address. | `{"name":"John Doe","pincode":"110002","country":"IN"}` |
| deviceInfoDetails<br/>`optional` | `object` Customer device information. | `{"ipAddress":"192.168.1.100","screenResolution":"1920x1080"}` |
**JSON Example**
`{"firstName":"John","lastName":"Doe"}`


#### callBackActions JSON Object Fields Descriptions
| successUrl<br/>`mandatory` | `string` URL to which the customer is redirected after a successful payment. | `https://merchant.com/payment/success` |
| failureUrl<br/>`mandatory` | `string` URL to which the customer is redirected after a failed payment. | `https://merchant.com/payment/failure` |
| cancelUrl<br/>`optional` | `string` URL to which the customer is redirected after cancelling the payment. | `https://merchant.com/payment/cancel` |
| webhookUrl<br/>`optional` | `string` URL that PayU notifies when the transaction succeeds or fails. | `https://merchant.com/webhook/payment` |
**JSON Example**
`{"successUrl":"https://merchant.com/payment/success","failureUrl":"https://merchant.com/payment/failure"}`

#### additionalInfo JSON Object Fields Description 
| preAuthorize<br/>`optional` | `number` Set to `1` to enable pre-authorization for separate authorization and capture. | `1` |
| preAuthDetails<br/>`conditional` | `object` Pre-authorization settings. Required when configuring multiple captures. | `{"multiCapture":"Y"}` |
**JSON Example**
`{"preAuthorize":1}` 
### Sample JSON Example
```json
{
  "orderId": "ORD123446789",
  "currency": "INR",
  "paymentSource": "direct",
  "order": {
    "amount": 18902.00,
    "productinfo": "Tickets"
  },
  "customer": {
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com",
    "phoneNumber": "9886575652"
  },
  "callBackActions": {
    "successUrl": "https://merchant.com/payment/success",
    "failureUrl": "https://merchant.com/payment/failure"
  },
  "merchantCacheExpiry": 1798761599
}
```

### Sample JSON wiht Complete Request (with all optional parameters)
```json
{
  "orderId": "ORD123446789",
  "currency": "INR",
  "paymentSource": "direct",
  "order": {
    "amount": 18902.00,
    "productinfo": "Tickets"
  },
  "additionalInfo": {
    "baseAmount": 5000,
    "subventionAmount": "200",
    "subventionEligibility": true,
    "preAuthorize": 1,
    "preAuthDetails": {
      "multiCapture": "Y"
    },
    "orderAdditionalParams": {
      "paxCount": 6,
      "journeyType": "AI",
      "itineraryType": "oneway",
      "flowId": "WBPB001",
      "convFee": "true",
      "taxes": "true",
      "otherFees": "true",
      "ancillaryType": "EMD",
      "customerType": "REGISTERED",
      "userId": "AIR_INDIA_USER_ID",
      "customerDetails": {
        "customerEmail": "rohit@gmail.com",
        "customerPhone": "38047208323"
      },
      "loyaltyDetails": {
        "loyaltyId": "LOYALCUST123",
        "membershipTier": "RED",
        "emailId": "rohit@gmail.com",
        "phoneNumber": 9876543201
      },
      "officeDetails": {
        "id": "DELAI08AA",
        "locationCode": "DEL",
        "countryCode": "IN"
      },
      "bookingDetails": {
        "bookingDate": "2025-12-18",
        "bookingTimeStamp": "2025-12-18 11:15:18",
        "bookingTimeZone": "UTC+0530"
      },
      "bookingDateTime": "2025-01-01T15:13:00.000Z",
      "passengers": [
        {
          "passengerTypeCode": "ADT",
          "gender": "MALE",
          "dateOfBirth": "1996-01-01",
          "firstName": "John",
          "lastName": "Doe",
          "sex": "M",
          "age": "29",
          "code": "J2LQJL",
          "seat": "12A",
          "loyaltyNumber": "LOYALCUST123",
          "loyaltyLevel": "Red"
        }
      ],
      "itineraries": [
        {
          "fareClass": "YTRQOU",
          "departureAirportCode": "BOM",
          "arrivalAirportCode": "DEN",
          "departureDate": "2025-12-18",
          "arrivalDate": "2025-12-18",
          "segments": [
            {
              "cabin": "SAMPLE1",
              "bookingClass": "Economy",
              "fareClass": "YTRQOU",
              "flightNumber": "AI2849",
              "aircraftType": "A320",
              "departureAirportCode": "DEL",
              "arrivalAirportCode": "HYD",
              "flightDistance": "60",
              "flightDuration": "60",
              "operatorCarrierCode": "AI",
              "marketedCarrierCode": "AI",
              "departureDateTime": "2025-12-18T10:55:00+05:30",
              "arrivalDateTime": "2025-12-18T13:20:00+05:30"
            }
          ]
        }
      ]
    },
    "routingParam": {
      "udf1": "User Defined Field 1",
      "udf2": "User Defined Field 2",
      "udf3": "User Defined Field 3",
      "udf4": "User Defined Field 4",
      "udf5": "User Defined Field 5",
      "udf6": "User Defined Field 6",
      "udf7": "User Defined Field 7",
      "udf8": "User Defined Field 8",
      "udf9": "User Defined Field 9",
      "udf10": "User Defined Field 10",
      "param1": "Routing param 1",
      "param2": "Routing param 2",
      "param3": "Routing param 3",
      "param4": "Routing param 4",
      "param5": "Routing param 5"
    }
  },
  "customer": {
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com",
    "phoneNumber": "9886575652",
    "address": {
      "billingAddress": {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "addressLine": "123 Main Street, Apartment 4B",
        "addressLine2": "Near City Mall",
        "addressPhoneNumber": "9886575652",
        "landmark": "Opposite Central Park",
        "pincode": "110001",
        "city": "New Delhi",
        "state": "Delhi",
        "country": "IN",
        "tag": "Home",
        "version": "v1",
        "isDefault": true,
        "status": "active",
        "source": "web"
      },
      "shippingAddress": {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "addressLine": "456 Business Park, Floor 2",
        "addressLine2": "Tower B",
        "addressPhoneNumber": "9876543210",
        "landmark": "Near Tech Hub",
        "pincode": "110002",
        "city": "New Delhi",
        "state": "Delhi",
        "country": "IN",
        "tag": "Office",
        "version": "v1",
        "isDefault": false,
        "status": "active",
        "source": "mobile"
      }
    },
    "deviceInfoDetails": {
      "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
      "ipAddress": "192.168.1.100",
      "screenResolution": "1920x1080"
    }
  },
  "callBackActions": {
    "successUrl": "https://merchant.com/payment/success",
    "failureUrl": "https://merchant.com/payment/failure",
    "cancelUrl": "https://merchant.com/payment/cancel",
    "webhookUrl": "https://merchant.com/webhook/payment"
  },
  "merchantCacheExpiry": 1798761599
}
```

## Sample Request

```bash
curl -X POST 'https://apitest.payu.in/v1/checkout/l1' \
  -H 'Date: Wed, 15 Jan 2025 10:30:00 GMT' \
  -H 'Authorization: hmac username="merchantKey", algorithm="sha512", headers="date", signature="{hash}"' \
  -H 'Content-Type: application/json' \
  -d '{
    "orderId": "ORD123446789",
    "currency": "INR",
    "paymentSource": "direct",
    "order": {
      "amount": 18902.00,
      "productinfo": "Tickets"
    },
    "customer": {
      "firstName": "John",
      "lastName": "Doe",
      "email": "john.doe@example.com",
      "phoneNumber": "9886575652"
    },
    "callBackActions": {
      "successUrl": "https://merchant.com/payment/success",
      "failureUrl": "https://merchant.com/payment/failure"
    },
    "merchantCacheExpiry": 1798761599
  }'
```

## Sample Response

```jsonc
{
  "paymentMethods": {
    "emi": { /* EMI payment options */ },
    "nb": { /* Net banking options */ },
    "wallet": { /* Wallet options */ },
    "upi": { /* UPI options */ },
    "dc": { /* Debit card options */ },
    "cc": { /* Credit card options */ }
  },
  "downInfo": {
    "downIssuingBanks": []
  },
  "broker": "PAYU",
  "order": {
    "amount": 18902,
    "productinfo": "Tickets",
    "orderId": "orderId"
  },
  "transaction": {
    "accessToken": "A2B6154E-7160-70DA-5F46-850584046BAE",
    "retryAllowed": "0",
    "txnId": "mtx1754396543709",
    "orderid": "yiekt",
    "proceedButtonEnableTimer": "10000"
  },
  "customer": {
    "phone": "8318711012",
    "email": "sample@email.com"
  }
}
```

## Response Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| transaction.accessToken | `string` Access token to pass in the `accessToken` header of subsequent API calls. | `A2B6154E-7160-70DA-5F46-850584046BAE` |
| transaction.orderid | `string` Encrypted order ID to pass in the `orderId` header of subsequent API calls. | `yiekt` |
| transaction.txnId | `string` PayU transaction identifier. | `mtx1754396543709` |
| paymentMethods | `object` Available EMI, Net Banking, wallet, UPI, debit card, and credit card payment methods. | `{"emi":{},"nb":{},"wallet":{},"upi":{},"dc":{},"cc":{}}` |
| downInfo | `object` Information about issuing banks that are currently unavailable. | `{"downIssuingBanks":[]}` |

## Error Responses

Errors will be returned with appropriate HTTP status codes and error messages in the response body.

## Notes

- The `accessToken` and `orderid` from the response are **required** for all subsequent API calls
- Pre-authorization can be enabled by setting `additionalInfo.preAuthorize` to `1`
- The hash must be calculated using the complete request body JSON string
- Date header must match the date used in hash computation
- All Air India specific parameters should be passed in `additionalInfo.orderAdditionalParams`
