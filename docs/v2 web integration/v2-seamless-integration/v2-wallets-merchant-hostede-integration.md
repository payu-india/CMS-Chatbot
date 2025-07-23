---
title: v2 Wallets Integration
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
You can collect payments from customers with leading wallets using the Merchant Hosted integration. You need to ensure that **Wallet** for the **paymentMethod.name** field and wallet code based on the desired wallet for the **paymentMethod.bankCode** parameter is posted.

**Steps to Integrate**

1. [Initiate the payment with PayU](#step-1-initiate-the-payment-with-payu)
2. [Verify Payment](#step-2-verify-the-payment)

> 👍 Before you begin:
>
> Register for an account with PayU before you start integration. For more information, refer to <a href="https://docs.payu.in/v1/docs/register-for-a-merchant-account-on-dashboard" target="_blank"> Register for a Merchant Account</a>.

## Step 1: Initiate the payment with PayU

The following parameters vary for the Wallet payment mode in the **Collect Payment** API (**v2/payments** API).

<V2_payment_envrionment />

> 📘 Reference:
>
> For the API reference, refer to <a href="https://docs.payu.in/v2/reference/collect_v2_payment_wallet" target="_blank">Collect Payments API</a> under API Reference.

### Request Header

<V2_payment_header_params />

### Request Body

The following table describes the request body parameters:



#### order object

<V2_order_object />

#### callBackActions object

<CallbackActions_object />

#### billingDetails object

<BillingDetails_object />

### Sample request

```curl
curl --location 'https://apitest.payu.in/v2/payments' \\
--header 'date: Thu, 27 Mar 2025 10:12:27 GMT' \\
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="<signature>"' \\
--header 'Content-Type: application/json' \\
--data-raw '{
    "accountId": "smsplus",
    "referenceId": "b5f2d8785768087678fn4",
    "currency": "INR",
    "paymentSource": "WEB",
    "paymentMethod": {
        "name": "Wallet",
        "bankCode": "PAYTM"
    },
    "order": {
        "productInfo": "qwertyuiopasdfghjkl",
        "userDefinedFields": {
            "udf1": "",
            "udf2": ""
        },
        "paymentChargeSpecification": {
            "price": "10"
        }
    },
    "callBackActions": {
        "successAction": "https://pp78admin.payu.in/test_response",
        "failureAction": "https://pp78admin.payu.in/test_response",
        "cancelAction": "https://pp78admin.payu.in/test_response"
    },
    "billingDetails": {
        "firstName": "sartaj",
        "lastName": "",
        "phone": "9876543210",
        "email": "testv2@example.in",
        "city": "Bharatpur",
        "state": "Rajasthan",
        "country": "India",
        "zipCode": "321028"
    }
}'
```

### Sample response

<V2_payment_response_params />

```json
{
    "referenceId": "b5f2d8785768087678fm9",
    "paymentId": "1999110000001769",
    "message": "Please call verify api to get the transaction status"
}
```

## Step 2: Verify the payment

After initiating the payment, you must verify the payment status using the **Verify Payment** API. For more information, refer to [Verify Payment API](https://docs.payu.in/v2/reference/verify_payment_api).

The customer will be redirected to the wallet provider (e.g., Paytm) to complete the payment, and you can verify the transaction status to confirm the payment.

> 📘 Note:
>
> - The wallet transaction may take some time to complete
> - Always verify the payment status before providing the service to the customer
> - Use the referenceId from the initial request to track the transaction
> - For supported wallet codes, refer to [Wallet Codes](https://docs.payu.in/v1/docs/wallet-codes)