---
title: Initiate payment API
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
POST /partner/initiatePayment. Headers required by PartnerController are X-PayU-Reseller-UUID, X-Partner-Token, and Authorization. extractAccountId requires accountId (merchant key, or a numeric merchant id). PartnerService reads txnId, amount, and callBackActions.successAction and failureAction when they are present, and does not reject the call when they are absent. The body is forwarded to Core Payments POST /v2/payments.

## Environment

| Environment    | Method | URL |
| :------------- | :----- | :-- |
| **Test**       | `POST` | `https://test-partnerapilayer.payu.in/apilayer/partner/initiatePayment` |
| **Production** | `POST` | `https://api.payu.in/partner/initiatePayment` |

## Request parameters

### Request headers

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| Content-Type<br />**mandatory** | `String` Send the body as `application/json`. | application/json |
| X-PayU-Reseller-UUID<br />**mandatory** | `String` X-PayU-Reseller-UUID | YOUR_RESELLER_UUID |
| X-Partner-Token<br />**mandatory** | `String` Partner access token. The Partner QR guides send this as `Bearer <token>`. | Bearer YOUR_ACCESS_TOKEN |
| Authorization<br />**mandatory** | `String` HMAC value. Partner QR guides use `hmac username="<client_id>", algorithm="sha512", headers="date", signature="<signature>"`. | Bearer YOUR_ACCESS_TOKEN |
| date<br />**optional** | `String` GMT timestamp used by the Partner QR HMAC examples. | Wed, 25 Nov 2026 06:00:00 GMT |

### Request body

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| accountId<br />**mandatory** | `String` Merchant key, or a numeric merchant id. Required by extractAccountId. | YOUR_MERCHANT_KEY |
| txnId<br />**optional** | `String` TxnId | PARTNER_TXN_001 |
| amount<br />**optional** | `Integer` Amount in paise on the Partner QR page (10000 = ₹100.00). | 1000.00 |
| currency<br />**optional** | `String` Currency | INR |
| order<br />**optional** | `Object` Order | {"productInfo": "Product purchase", "paymentChargeSpecification": {"price": 100000}} |
| order.productInfo<br />**optional** | `String` ProductInfo | Product purchase |
| order.paymentChargeSpecification | `Object` Order.paymentChargeSpecification | {"price": 100000} |
| order.paymentChargeSpecification.price<br />**optional** | `Integer` Price | 100000 |
| additionalInfo<br />**optional** | `Object` AdditionalInfo | {"txnFlow": "nonseamless", "createOrder": "true"} |
| additionalInfo.txnFlow<br />**optional** | `String` TxnFlow | nonseamless |
| additionalInfo.createOrder<br />**optional** | `String` CreateOrder | true |
| callBackActions<br />**optional** | `Object` CallBackActions | {"successAction": "https://merchant.example.com/success", "failureAction": "https://merchant.example.com/failure", "cancelAction": "https://merchant.example.com/cancel", "returnAction": "https://merchant.example.com/return"} |
| callBackActions.successAction<br />**optional** | `String` SuccessAction | https://merchant.example.com/success |
| callBackActions.failureAction<br />**optional** | `String` FailureAction | https://merchant.example.com/failure |
| callBackActions.cancelAction<br />**optional** | `String` CancelAction | https://merchant.example.com/cancel |
| callBackActions.returnAction<br />**optional** | `String` ReturnAction | https://merchant.example.com/return |
| billingDetails<br />**optional** | `Object` BillingDetails | {"firstName": "John", "phone": "9999999999", "email": "customer@example.com", "address1": "123 Main Street", "city": "Mumbai", "state": "Maharashtra", "country": "India", "zipCode": "400001"} |
| billingDetails.firstName<br />**optional** | `String` FirstName | John |
| billingDetails.phone<br />**optional** | `String` Phone | 9999999999 |
| billingDetails.email<br />**optional** | `String` Email | customer@example.com |
| billingDetails.address1<br />**optional** | `String` Address1 | 123 Main Street |
| billingDetails.city<br />**optional** | `String` City | Mumbai |
| billingDetails.state<br />**optional** | `String` State | Maharashtra |
| billingDetails.country<br />**optional** | `String` Country | India |
| billingDetails.zipCode<br />**optional** | `String` ZipCode | 400001 |

## Sample request

```curl
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/initiatePayment' \
--header 'Content-Type: application/json' \
--header 'X-PayU-Reseller-UUID: YOUR_RESELLER_UUID' \
--header 'X-Partner-Token: Bearer YOUR_ACCESS_TOKEN' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--data '{
  "accountId": "YOUR_MERCHANT_KEY",
  "txnId": "PARTNER_TXN_001",
  "amount": "1000.00",
  "currency": "INR",
  "order": {
    "productInfo": "Product purchase",
    "paymentChargeSpecification": {
      "price": 100000
    }
  },
  "additionalInfo": {
    "txnFlow": "nonseamless",
    "createOrder": "true"
  },
  "callBackActions": {
    "successAction": "https://merchant.example.com/success",
    "failureAction": "https://merchant.example.com/failure",
    "cancelAction": "https://merchant.example.com/cancel",
    "returnAction": "https://merchant.example.com/return"
  },
  "billingDetails": {
    "firstName": "John",
    "phone": "9999999999",
    "email": "customer@example.com",
    "address1": "123 Main Street",
    "city": "Mumbai",
    "state": "Maharashtra",
    "country": "India",
    "zipCode": "400001"
  }
}'
```

## Response parameters

| HTTP status | Description |
| :---------- | :---------- |
| `200` | Core Payments V2 response, passed through. The Partner QR guide returns mihpayId for the next QR call. |
| `400` | accountId is missing or the JSON is invalid. |

## Sample response

### HTTP 200

Core Payments V2 response, passed through. The Partner QR guide returns mihpayId for the next QR call.

### HTTP 400 — error

```json
{
  "error": "accountId is required in request body"
}
```
