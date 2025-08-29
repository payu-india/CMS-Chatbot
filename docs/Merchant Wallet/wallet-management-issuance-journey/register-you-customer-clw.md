---
title: Register you Customer - CLW
deprecated: false
hidden: true
metadata:
  robots: index
---
Registering your customers in your closed-loop wallet enables seamless payments, loyalty, and funding operations. Use the Register Customer API to quickly and securely provision wallet accounts for your users. The **Register Customer **API is applicable for PayU closed-loop wallet integrations. 

### Environment

**Production URL:**
`POST https://api.payu.in/wallet/registerCustomer`

**Sandbox URL:**
`POST https://sandboxapi.payu.in/wallet/registerCustomer`

## Step 1: Build the Request Payload

Send a JSON payload with your user’s details.

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>customer_id <br/><code>Mandatory</code></td>
      <td><code>string</code> Unique customer reference (your system)</td>
      <td>"CUST2024001"</td>
    </tr>
    <tr>
      <td>firstName <br/><code>Optional</code></td>
      <td><code>string</code> Customer's first name</td>
      <td>"John"</td>
    </tr>
    <tr>
      <td>lastName <br/><code>Optional</code></td>
      <td><code>string</code> Customer's last name</td>
      <td>"Doe"</td>
    </tr>
    <tr>
      <td>email <br/><code>Optional</code></td>
      <td><code>string</code> Email address</td>
      <td>"john.doe@email.com"</td>
    </tr>
    <tr>
      <td>phone <br/><code>Optional</code></td>
      <td><code>string</code> Mobile number (without country code)</td>
      <td>"9876543210"</td>
    </tr>
    <tr>
      <td>address <br/><code>Optional</code></td>
      <td><code>object</code> Address object (see below)</td>
      <td><code>{...}</code></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

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

***

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

* Ensure `Authorization` header uses a valid access token.
* The `customer_id` must be unique for each wallet user.
* Use only HTTPS for all API requests.

***

### Step 3: Check the API Response

#### Successful Response

```json
{
  "status": "SUCCESS",
  "message": "Customer registered successfully",
  "wallet_id": "WALLET987654"
}
```

* `status`: API call status
* `wallet_id`: Unique identifier for customer’s wallet

#### Error Response

```json
{
  "status": "FAILED",
  "message": "Customer already registered",
  "code": "ERR_CUSTOMER_EXISTS"
}
```

* `message` and `code` will clarify the failure reason.

***