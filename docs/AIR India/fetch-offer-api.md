---
title: Fetch Offer API
deprecated: false
hidden: false
metadata:
  robots: index
---
Fetches offers without an existing order context. Used for offer discovery before order creation. Requires Air India travel context in `offerParams`.

## Endpoint

| Environment | Base URL |
|-------------|----------|
| UAT / Test | `https://sandbox.payu.in/offers/transactions` |
| Production | `https://api.payu.in/offers/transactions` |

## Sample Request

```bash
curl -X POST 'https://sandbox.payu.in/offers/transactions' \
  -H 'Date: <rfc_1123_gmt_date>' \
  -H 'Digest: <base64_sha256_digest>' \
  -H 'Authorization: hmac username="<merchant_key>", algorithm="hmac-sha256", headers="date digest", signature="<base64_hmac_sha256_signature>"' \
  -H 'platformId: 1' \
  -H 'Content-Type: application/json' \
  -d '{
    "orderId": "PREVIEW_ORDER_001",
    "amount": 10000,
    "baseAmount": 9000,
    "userDetails": {
      "phoneNo": "8310300493",
      "email": "abc@gmail.com"
    },
    "offerParams": {
      "passengers": [
        {
          "passengerTypeCode": "ADT",
          "gender": "MALE",
          "dateOfBirth": "1996-01-01"
        }
      ],
      "itineraries": [
        {
          "departureAirportCode": "DEL",
          "arrivalAirportCode": "BLR",
          "departureDate": "2025-12-18",
          "segments": [
            {
              "flightNumber": "AI2849",
              "cabin": "Economy",
              "fareClass": "YTRQOU"
            }
          ]
        }
      ],
      "paxCount": 1,
      "journeyType": "AI",
      "itineraryType": "oneway",
      "flowId": "WBPB001",
      "userId": "AIR_INDIA_USER_ID",
      "bookingDateTime": "2025-12-18 11:15:18",
      "officeDetails": {
        "id": "DELAI08AA"
      },
      "customerType": "REGISTERED",
      "loyaltyDetails": {
        "loyaltyId": "LOYALCUST123",
        "membershipTier": "RED"
      }
    }
  }'
```

## Sample Response

```json
{
  "code": "200",
  "message": "Offer Retrieved Successfully",
  "status": 1,
  "result": {
    "offers": [
      {
        "offerKey": "OFFER_KEY_123",
        "title": "10% Cashback",
        "description": "Get 10% cashback on Air India bookings",
        "discountDetail": {
          "discountType": "PERCENTAGE",
          "discountPercentage": 10.00
        }
      }
    ]
  },
  "traceId": "uuid-trace-id"
}
```

## Headers

| Parameter | Description | Example |
|-----------|-------------|---------|
| Date<br/>`mandatory` | `string` Request date and time in RFC 1123 GMT format. | `Thu, 17 Feb 2022 08:17:59 GMT` |
| Digest<br/>`mandatory` | `string` Base64-encoded SHA-256 digest of the serialized JSON request body. | `vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=` |
| Authorization<br/>`mandatory` | `string` HMAC authorization value using the merchant key, the `hmac-sha256` algorithm, and the signed headers `date digest`. | `hmac username="<merchant_key>", algorithm="hmac-sha256", headers="date digest", signature="<base64_signature>"` |
| platformId<br/>`mandatory` | `string` Platform identifier. Set this value to `1`. | `1` |
| Content-Type<br/>`mandatory` | `string` Media type of the JSON request body. | `application/json` |

### Authentication

This API does not use `HeaderAuthentication`. Compute `Digest` as Base64(SHA-256(serialized JSON request body)). Then compute `signature` as Base64(HMAC-SHA256(`date: {Date}\ndigest: {Digest}`, merchant salt)) and send `Authorization` with `algorithm="hmac-sha256"` and `headers="date digest"`.

## Request Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| orderId<br/>`mandatory` | `string` Temporary/preview order ID. | `PREVIEW_ORDER_001` |
| amount<br/>`mandatory` | `number` Total transaction amount. | `10000` |
| baseAmount<br/>`mandatory` | `number` Base transaction amount. | `9000` |
| paymentId<br/>`optional` | `number` Payment identifier. | `123` |
| offerKeys<br/>`optional` | `array` Specific offer keys to evaluate (null for all). | `null` |
| userDetails<br/>`optional` | `object` User information. See [userDetails object parameters](#userdetails-object-parameters) for details. | - |
| offerParams<br/>`mandatory` | `object` Air India specific travel context. See [offerParams object parameters](#offerparams-object-parameters) for details. | - |

### userDetails object parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| userToken<br/>`optional` | `string` User token. | `abcd` |
| phoneNo<br/>`optional` | `string` User phone number. | `8310300493` |
| email<br/>`optional` | `string` User email. | `abc@gmail.com` |
| loggedInPhoneNumber<br/>`optional` | `string` Logged-in user's phone number. | `8310300493` |

### offerParams object parameters

Air India specific travel context:

| Parameter | Description | Example |
|-----------|-------------|---------|
| passengers<br/>`mandatory` | `array` List of passengers. Each passenger object contains passengerTypeCode (ADT/CHD/INF), gender, dateOfBirth. | - |
| itineraries<br/>`mandatory` | `array` Flight itineraries. Each itinerary contains departureAirportCode, arrivalAirportCode, departureDate, segments array. | - |
| paxCount<br/>`mandatory` | `number` Total passenger count. | `1` |
| journeyType<br/>`mandatory` | `string` Journey type. For Air India, use `AI`. | `AI` |
| itineraryType<br/>`mandatory` | `string` Type of itinerary: `oneway`, `roundtrip`, `multicity`. | `oneway` |
| flowId<br/>`mandatory` | `string` Flow identifier. | `WBPB001` |
| userId<br/>`optional` | `string` Air India user ID. | `AIR_INDIA_USER_ID` |
| bookingDateTime<br/>`mandatory` | `string` Booking timestamp. | `2025-12-18 11:15:18` |
| officeDetails<br/>`mandatory` | `object` Office/agent details with field: id. | `{"id": "DELAI08AA"}` |
| customerType<br/>`optional` | `string` Customer type: `REGISTERED` or `GUEST`. | `REGISTERED` |
| customerDetails<br/>`optional` | `object` Customer contact details with fields: customerEmail, customerPhone. | - |
| loyaltyDetails<br/>`optional` | `object` Loyalty program information with fields: loyaltyId, membershipTier, emailId, phoneNumber. | - |

## Response Parameters

The response structure is the same as [Fetch Offer (with Order ID) API](./02_Fetch_Offer_With_Order_ID_API_v1.md). Refer to that documentation for detailed response parameters.

| Parameter | Description | Example |
|-----------|-------------|---------|
| code | `string` Response code. | `200` |
| message | `string` Response message. | `Offer Retrieved Successfully` |
| status | `number` Status indicator. `1` = success, `0` = failure. | `1` |
| result | `object` Contains offer details including offers array. | - |
| traceId | `string` Unique trace ID for debugging. | `uuid-trace-id` |
