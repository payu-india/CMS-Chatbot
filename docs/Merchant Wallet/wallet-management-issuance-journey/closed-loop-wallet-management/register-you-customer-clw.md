---
title: Register you Customer - CLW
deprecated: false
hidden: false
metadata:
  robots: index
---

Registering your customers in your closed-loop wallet enables seamless payments, loyalty, and funding operations.  
Use the Register Customer API to quickly and securely provision wallet accounts for your users.
The Register Customer API is applicable for PayU closed-loop wallet integrations.  
Please ensure that you have wallet functionality enabled for your merchant account.

---


### Environment

**Production URL:**  
`POST https://api.payu.in/wallet/registerCustomer`

**Sandbox URL:**  
`POST https://sandboxapi.payu.in/wallet/registerCustomer`

---

### Step 1: Build the Request Payload

Send a JSON payload with your user’s details.  
Mandatory and optional fields are listed below.



#### Address Object:

```json
{
  "line1": "221B Baker Street",
  "line2": "",
  "city": "London",
  "state": "London",
  "country": "UK",
  "zip": "NW16XE"
}
```

---

### Step 2: Make the API Call

Below is a sample request using `curl`:

```bash
curl --request POST 'https://api.payu.in/wallet/registerCustomer'   --header 'Content-Type: application/json'   --header 'Authorization: Bearer <ACCESS_TOKEN>'   --data-raw '{
    "customer_id": "CUST2024001",
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@email.com",
    "phone": "9876543210",
    "address": {
      "line1": "221B Baker Street",
      "city": "London",
      "state": "London",
      "country": "UK",
      "zip": "NW16XE"
    }
  }'
```


- Ensure `Authorization` header uses a valid access token.
- The `customer_id` must be unique for each wallet user.
- Use only HTTPS for all API requests.


---

### Step 3: Check the API Response

#### Successful Response

```json
{
  "status": "SUCCESS",
  "message": "Customer registered successfully",
  "wallet_id": "WALLET987654"
}
```
- `status`: API call status  
- `wallet_id`: Unique identifier for customer’s wallet

#### Error Response

```json
{
  "status": "FAILED",
  "message": "Customer already registered",
  "code": "ERR_CUSTOMER_EXISTS"
}
```
- `message` and `code` will clarify the failure reason.

---
