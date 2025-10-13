---
title: 'Collect Payment for WealthTech '
deprecated: false
hidden: true
metadata:
  robots: index
---
This section provides API details for _payment  API used for collecting WealthTech payments, specifically designed for mutual fund transaction processing. The API introduces new parameters and validation rules to support wealth management payment flows.

* **Method**: `POST`
* **Content-Type**: `application/x-www-form-urlencoded`

<PaymentAPIEnvironment />

## Request Parameters

| Parameter                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Example                                                                                        |
| :---------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------- |
| key<br />`mandatory`                            | `String` This parameter is the unique merchant key provided by PayU for your merchant account. For more information, refer to [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard).                                                                                                                                                                                                                                                                                                                                                                                                                        | 8488225                                                                                        |
| txnid<br />`mandatory`                          | `varchar` This parameter is known as Transaction ID (or OrderID). It is the order reference number generated at your (Merchant's) end. It is an identifier which you(merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of same Transaction ID again would fail. Hence, it is essential that you post us a unique transaction ID for every new transaction (Please make sure that the transaction ID being sent to us hasn't been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID'). | fd3e847h2                                                                                      |
| amount<br />`mandatory`                         | `float` This parameter should contain the payment amount of the particular transaction. Note: Type-cast the amount to float type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 10                                                                                             |
| productinfo<br />`mandatory`                    | `varchar` This parameter should contain a brief product description. It should be a string describing the product (The description type is entirely your choice).                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | T-shirt                                                                                        |
| firstname<br />`mandatory`                      | `varchar` This parameter must contain the first name of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Ankit                                                                                          |
| email<br />`mandatory`                          | `varchar` This parameter must contain the email of the customer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [test@gmail.com](mailto:test@gmail.com)                                                        |
| phone<br />`mandatory`                          | `integer` Merchant needs to take the customer's GPay registered phone number and pass in this field. This field will be used for further mapping the customer VPA and initiate a collect request.                                                                                                                                                                                                                                                                                                                                                                                                                                            | 9876543210                                                                                     |
| pg<br />`mandatory`                             | `string` This parameter contains the payment method to be enabled to collect payment from your customer. For the list of payment methods and their codes, refer to [Payment Mode Codes](doc:payment-mode-codes). For Net Banking, use NB.                                                                                                                                                                                                                                                                                                                                                                                                    | NB                                                                                             |
| bankcode<br />`mandatory`                       | `string` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. For the list of bankcodes for Net Banking, refer to [Net Banking Codes](doc:net-banking-codes).                                                                                                                                                                                                                                                                                                                                                             | AXIB                                                                                           |
| surl<br />`mandatory`                           | `string` The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                             | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/) |
| furl<br />`mandatory`                           | `string` The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                                 | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/) |
| hash<br />`mandatory`                           | `string` The hash calculated by the merchant using the key and salt provided by PayU. The format for calculating the hash: sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|SALT) For more information, refer to [Generate Hash](doc:hashing-request-and-response).                                                                                                                                                                                                                                                                                                                         | a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0                                                       |
| lastname<br />`optional`                        | `string` The last name of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Sharma                                                                                         |
| address1<br />`optional`                        | `string` The first line of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 123 Main Street                                                                                |
| address2<br />`optional`                        | `string` The second line of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Apartment 4B                                                                                   |
| city<br />`optional`                            | `string` The city where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Mumbai                                                                                         |
| state<br />`optional`                           | `string` The state where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Maharashtra                                                                                    |
| country<br />`optional`                         | `string` The country where your customer resides.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | India                                                                                          |
| zipcode<br />`optional`                         | `string` Billing address zip code is mandatory for the cardless EMI option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 400001                                                                                         |
| udf1<br />`mandatory for Cross-Border Payments` | `string` This parameter has been made for you to keep any information corresponding to the transaction. **Note**: This parameter must contain buyer's PAN number for Cross-Border Payments.                                                                                                                                                                                                                                                                                                                                                                                                                                                  | ABCDE1234F                                                                                     |
| udf2<br />`optional`                            | `string` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 1                                                                              |
| udf3<br />`mandatory for Cross-Border Payments` | `string` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | GSTIN123456                                                                                    |
| udf4<br />`optional`                            | `string` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 2                                                                              |
| udf5<br />`optional`                            | `string` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 3                                                                              |

Perfect! ✨ Now each parameter name is on its own line, followed by the mandatory/optional status on the next line, making the table much more readable and organized.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key
        `mandatory`
      </td>

      <td>
        `string` - PayU provided unique API key
      </td>

      <td>
        `"KOEfPI"`
      </td>
    </tr>

    <tr>
      <td>
        txnid
        `mandatory`
      </td>

      <td>
        `string` - Unique transaction identifier
      </td>

      <td>
        `"7f41f520f71b"`
      </td>
    </tr>

    <tr>
      <td>
        api_version `mandatory`
      </td>

      <td>
        `integer` - API version number
      </td>

      <td>
        `21`
      </td>
    </tr>

    <tr>
      <td>
        salt_version `mandatory`
      </td>

      <td>
        `integer` - Salt version for hash calculation
      </td>

      <td>
        `1`
      </td>
    </tr>

    <tr>
      <td>
        amount
        `mandatory`
      </td>

      <td>
        `numeric` - Transaction amount in paise
      </td>

      <td>
        `50000`
      </td>
    </tr>

    <tr>
      <td>
        productinfo
        `mandatory`
      </td>

      <td>
        `string` - Product information
      </td>

      <td>
        `"Mutual Fund Investment"`
      </td>
    </tr>

    <tr>
      <td>
        firstname
        `mandatory`
      </td>

      <td>
        `string` - Customer first name
      </td>

      <td>
        `"John"`
      </td>
    </tr>

    <tr>
      <td>
        email `
                                mandatory`
      </td>

      <td>
        `string` - Customer email address
      </td>

      <td>
        `"john@example.com"`
      </td>
    </tr>

    <tr>
      <td>
        phone
        `mandatory`
      </td>

      <td>
        `string` - Customer phone number
      </td>

      <td>
        `"9876543210"`
      </td>
    </tr>

    <tr>
      <td>
        hash `
                                mandatory`
      </td>

      <td>
        `string` - SHA-512 secured hash for request validation. the
      </td>

      <td>
        `"fbc07b5517029..."`
      </td>
    </tr>

    <tr>
      <td>
        additional_charges `optional`
      </td>

      <td>
        `string` - Additional charges/fees
      </td>

      <td>
        `"CC:100
      </td>
    </tr>

    <tr>
      <td>
        more_info
      </td>

      <td>
        
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

### Wealth Tech object (wtParams) fields Description

These parameters are included within the `more_info` field as a JSON array under the fiedl `wtParams`:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        type
        `mandatory`
      </td>

      <td>
        `string` - Transaction type, must be "mutual_fund"
      </td>

      <td>
        `"mutual_fund"`
      </td>
    </tr>

    <tr>
      <td>
        amount
        `mandatory`
      </td>

      <td>
        `numeric` - Amount in paise, must match order amount
      </td>

      <td>
        `50000`
      </td>
    </tr>

    <tr>
      <td>
        receipt
        `mandatory`
      </td>

      <td>
        `string` - Unique PG reference number (max 25 chars)
      </td>

      <td>
        `"77407"`
      </td>
    </tr>

    <tr>
      <td>
        mf_member_id
        `mandatory`
      </td>

      <td>
        `numeric` - Member ID issued by mutual fund platform (5-20 chars)
      </td>

      <td>
        `"123445"`
      </td>
    </tr>

    <tr>
      <td>
        mf_user_id
        `mandatory`
      </td>

      <td>
        `string` - Unique mutual fund user/client ID (max 10 chars)
      </td>

      <td>
        `"77407"`
      </td>
    </tr>

    <tr>
      <td>
        mf_partner
        `mandatory`
      </td>

      <td>
        `string` - Mutual fund platform: cams, kfin, bse, nse (max 4 chars)
      </td>

      <td>
        `"cams"`
      </td>
    </tr>

    <tr>
      <td>
        mf_investment_type `mandatory`
      </td>

      <td>
        `string` - Investment type: L (Lump Sum) or S (SIP) (single char)
      </td>

      <td>
        `"L"`
      </td>
    </tr>

    <tr>
      <td>
        plan
        `optional`
      </td>

      <td>
        `string` - Mutual fund plan name
      </td>

      <td>
        `"GD"`
      </td>
    </tr>

    <tr>
      <td>
        folio
        `optional`
      </td>

      <td>
        `string` - Unique mutual fund account identifier
      </td>

      <td>
        `"12345678"`
      </td>
    </tr>

    <tr>
      <td>
        option
        `optional`
      </td>

      <td>
        `string` - Mutual fund plan option
      </td>

      <td>
        `"G"`
      </td>
    </tr>

    <tr>
      <td>
        scheme
        `optional`
      </td>

      <td>
        `string` - Mutual fund type/scheme
      </td>

      <td>
        `"LT"`
      </td>
    </tr>

    <tr>
      <td>
        mf_amc_code
        `optional`
      </td>

      <td>
        `string` - Asset Management Company code (max 5 chars)
      </td>

      <td>
        `"UTB"`
      </td>
    </tr>
  </tbody>
</Table>

## Response Parameters

### Success scenario

| Parameter                       | Description                                                                       | Example                                  |
| ------------------------------- | --------------------------------------------------------------------------------- | ---------------------------------------- |
| status **`mandatory`**          | `integer` - Response status (1 for success, 0 for failure)                        | `1`                                      |
| message **`mandatory`**         | `string` - Response message describing the result                                 | `"Transaction Processed successfully"`   |
| details **`mandatory`**         | `object` - Transaction details object containing specific transaction information | `{}`                                     |
| authpayuid **`mandatory`**      | `string` - PayU authorization ID                                                  | `"999990000005920"`                      |
| transactionid **`mandatory`**   | `string` - Unique transaction identifier                                          | `"48101c0c-5265-4c2a-b6d0-e6e73d42809e"` |
| amount **`mandatory`**          | `string` - Transaction amount in decimal format                                   | `"500.00"`                               |
| user_credentials **`optional`** | `string` - Encrypted user credentials for future transactions                     | `"o0dEBA:11b341595c..."`                 |
| card_token **`optional`**       | `string` - Tokenized card information                                             | `"195748c0f4ec4b3093af"`                 |
| payuid **`mandatory`**          | `string` - PayU transaction reference ID                                          | `"999990000006473"`                      |
| field9 **`optional`**           | `string` - Additional transaction information                                     | `"Transaction is Successful"`            |

### **Error Response Fields**

| Parameter               | Description                                   | Example                                                                       |
| ----------------------- | --------------------------------------------- | ----------------------------------------------------------------------------- |
| status **`mandatory`**  | `integer` - Response status (0 for error)     | `0`                                                                           |
| message **`mandatory`** | `string` - Error message describing the issue | `"Invalid Parameter: mf_partner must be less than or equal to 4 characters."` |

***

## **Validation Rules**

### **Mandatory Field Validations**

* **type**: Must always be `"mutual_fund"`
* **amount**: Must match the overall order amount and be in paise
* **receipt**: Must be unique across transactions
* **mf_member_id**: Must be numeric with length between 5-20 characters
* **mf_user_id**: Maximum 10 characters allowed
* **mf_partner**: Must be one of: `"cams"`, `"kfin"`, `"bse"`, `"nse"`
* **mf_investment_type**: Only `"L"` (Lump Sum) or `"S"` (SIP) allowed

### **Optional Field Validations**

* **mf_amc_code**: Maximum 5 characters
* **receipt**: Maximum 25 characters for SIP registration ID

***

## **Hash Calculation**

The hash is calculated using SHA-512 algorithm with the following field sequence:

```
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|salt
```

### **Hash Generation Steps**

1. Concatenate fields in the specified order using pipe (|) separator
2. Append the salt at the end
3. Apply SHA-512 hashing to the concatenated string
4. Use the resulting hash as the `hash` parameter

***

## Sample Request

```bash
curl -i 'https://test.payu.in/_payment' \
-H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \
-H 'content-type: application/x-www-form-urlencoded' \
--data-raw 'hash=fbc07b5517029242fd97b982816eb372d6501c1...&key=KOEfPI&txnid=7f41f520f71b&api_version=21&amount=50000&productinfo=Mutual Fund&firstname=John&email=john@example.com&phone=9876543210'
```

### Sample JSON Payload Structure

```json
{
  "hash": "fbc07b5517029242fd97b982816eb372d6501c1...",
  "key": "KOEfPI",
  "txnid": "7f41f520f71b",
  "api_version": "21",
  "salt_version": "1",
  "amount": "50000",
  "productinfo": "Mutual Fund Investment",
  "firstname": "John",
  "email": "john@example.com",
  "phone": "9876543210",
  "more_info": {
    "wtParams": [
      {
        "type": "mutual_fund",
        "plan": "GD",
        "amount": "50000",
        "option": "G",
        "scheme": "LT",
        "receipt": "77407",
        "mf_member_id": "123445",
        "mf_user_id": "77407",
        "mf_partner": "cams",
        "mf_investment_type": "L",
        "mf_amc_code": "UTB"
      }
    ]
  }
}
```

## Recurring payments

## Sample response

### Success scenario

```json
{
  "status": 1,
  "message": "Transaction Processed successfully",
  "details": {
    "48101c0c-5265-4c2a-b6d0-e6e73d42809e": {
      "authpayuid": "999990000005920",
      "transactionid": "48101c0c-5265-4c2a-b6d0-e6e73d42809e",
      "amount": "500.00",
      "user_credentials": "o0dEBA:11b341595c...",
      "card_token": "195748c0f4ec4b3093af",
      "payuid": "999990000006473",
      "status": "captured",
      "udf1": "Y",
      "field9": "Transaction is Successful"
    }
  }
}
```

### Failure scenario

```json
{
  "status": 0,
  "message": "Invalid Parameter: mf_partner must be less than or equal to 4 characters."
}
```

***
