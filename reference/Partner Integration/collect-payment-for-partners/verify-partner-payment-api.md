---
title: Verify Partner Payment API
deprecated: false
hidden: false
metadata:
  robots: index
---
Always call the **Verify Partner Payment** API as the final source of truth for transaction status.

### Endpoint

| Environment | URL                                                                   |
| ----------- | --------------------------------------------------------------------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment` |
| Production  | `https://api.payu.in/partner/verifyPayment`                           |

## Request Parameters

### Request Headers

You must generate token using the Get Token API and used it as bearer token. For more information, refer to [Get Token API.](ref:get_token_partner_integration)

```
Content-Type: application/json
Authorization: Bearer <FINAL_ACCESS_TOKEN>
```

### Request Body

| Parameter   | Description                                              | Example             |
| :---------- | :------------------------------------------------------- | :------------------ |
| merchant_id | The unique ID of the merchant.                           | 8739528             |
| txnid       | The unique transaction ID of the payment to be verified. | HC_TPV_20240315_001 |

## Sample Request

```bash
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...' \
--data-raw '{
  "merchant_id": "8739528",
  "txnid": "HC_TPV_20240315_001"
}'
```
```python
import requests

url = "https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {final_access_token}"
}

payload = {
    "merchant_id": "8739528",
    "txnid": "HC_TPV_20240315_001"
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    verify_data = response.json()
    print(f"Payment Status: {verify_data.get('status')}")
    print(f"Bank Code: {verify_data.get('bankcode')}")
    print(f"Amount: {verify_data.get('amount')}")
    print(f"PayU ID: {verify_data.get('mihpayid')}")
    
    if verify_data.get('bankcode') == 'INTTPV':
        print("✅ UPI TPV payment confirmed")
```

## Sample Response

### Success Response

```json
{
  "status": "success",
  "mihpayid": "403993715529111111",
  "txnid": "HC_TPV_20240315_001",
  "amount": "1500.00",
  "productinfo": "Loan EMI Payment - March 2024",
  "firstname": "Rajesh",
  "email": "rajesh.kumar@example.com",
  "phone": "9876543210",
  "mode": "UPI",
  "bankcode": "INTTPV",
  "unmappedstatus": "captured",
  "payment_source": "payu",
  "merchant_id": "8739528"
}
```

## Response Parameters

| Field          | Description                                                                            |                                                 | Value
| -------------- | -------------------------------------------------------------------------------- | --------------------------------------|
| status         | Indidicates the status of payment                                                                |  `"success"`  | 
| bankcode       | Confirms UPI TPV validation passed                                                                        |  For INTTPV"  |
| mode           | Payment method                                                                          | `"UPI"` |
| unmappedstatus | Payment captured successfully                                                                    |  `"captured"`  |
| mihpayid       | PayU transaction ID                                                              | Unique PayU reference                                       |
| firstname      | The first name of the customer.                                                  | Rajesh                                                      |
| email          | The email address of the customer.                                               | [rajesh.kumar@example.com](mailto:rajesh.kumar@example.com) |
| phone          | The phone number of the customer.                                                | 9876543210                                                  |
| mode           | The payment mode used for the transaction.                                       | UPI                                                         |
| bankcode       | The bank code associated with the payment method used.                           | INTTPV                                                      |
| unmappedstatus | The raw internal status of the transaction as received from the payment gateway. | captured                                                    |
| payment_source | The payment platform through which the transaction was processed.                | payu                                                        |
| merchant_id    | The unique ID of the merchant.                                                   | 8739528                                                     |

***

##
