---
title: 'Payment Consent Transaction for WealthTech '
deprecated: false
hidden: true
metadata:
  robots: index
---
This section provides **_payment**  API details used for payment consent WealthTech recurring payments, specifically designed for mutual fund transaction processing.

* **Method**: `POST`
* **Content-Type**: `application/x-www-form-urlencoded`

<PaymentAPIEnvironment />

## Request Parameters

| Parameter                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Example                                                                                                                                                              |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| key<br />`mandatory`                            | `String` This parameter is the unique merchant key provided by PayU for your merchant account. For more information, refer to Generate Merchant Key and Salt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 8488225                                                                                                                                                              |
| txnid<br />`mandatory`                          | `Varchar` This parameter is known as Transaction ID (or OrderID). It is the order reference number generated at your (Merchant's) end. It is an identifier which you(merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of same Transaction ID again would fail. Hence, it is essential that you post us a unique transaction ID for every new transaction (Please make sure that the transaction ID being sent to us hasn't been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID'). | fd3e847h2                                                                                                                                                            |
| amount<br />`mandatory`                         | `float` This parameter should contain the payment amount of the particular transaction. Note: Type-cast the amount to float type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 10                                                                                                                                                                   |
| productinfo<br />`mandatory`                    | `Varchar` This parameter should contain a brief product description. It should be a string describing the product (The description type is entirely your choice).                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | T-shirt                                                                                                                                                              |
| firstname<br />`mandatory`                      | `Varchar` This parameter must contain the first name of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Ankit                                                                                                                                                                |
| email<br />`mandatory`                          | `Varchar` This parameter must contain the email of the customer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [test@gmail.com](mailto:test@gmail.com)                                                                                                                              |
| phone<br />`mandatory`                          | `Integer` Merchant needs to take the customer's GPay registered phone number and pass in this field. This field will be used for further mapping the customer VPA and initiate a collect request.                                                                                                                                                                                                                                                                                                                                                                                                                                            | 9876543210                                                                                                                                                           |
| pg<br />`mandatory`                             | `String` This parameter contains the payment method to be enabled to collect payment from your customer. For the list of payment methods and their codes, refer to Payment Mode Codes. For Net Banking, use NB.                                                                                                                                                                                                                                                                                                                                                                                                                              | NB                                                                                                                                                                   |
| bankcode<br />`mandatory`                       | `string` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. For the list of bankcodes for Net Banking, refer to Net Banking Codes.                                                                                                                                                                                                                                                                                                                                                                                      | AXIB                                                                                                                                                                 |
| surl<br />`mandatory`                           | `string` The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                             | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                                       |
| furl<br />`mandatory`                           | `String` The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                                 | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                                       |
| api_version <br /> `mandatory`                  | API version must be posted as `21`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 21                                                                                                                                                                   |
| si<br />`mandatory`                             | This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.<br />**Notes**: You can modify or cancel existing recurring payment registration as described in the following sections: <br />- Manage Recurring Payment for Cards <br />- Manage UPI Recurring Transaction                                                                                                                                                                                                                     | 1                                                                                                                                                                    |
| free_trial<br />`optional`                      | This is mandatory only if the merchant wants to support free trial use cases. In this case, PayU adjusts the transaction amount as INR 2.00 for cards and UPI and INR 0.00 for Net Banking irrespective of what amount is passed against the amount field in the request.                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                      |
| si_details<br />`mandatory`                     | This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.<br />**Note**: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers ( for more details refer [https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668&Mode=0](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0) ) This is a JSON object and it includes a set of fields. For more information, refer to SI Parameter JSON Details                                       | \{"billingAmount": "100.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"} |
| hash<br />`mandatory`                           | `String` The hash calculated by the merchant using the key and salt provided by PayU. The format for calculating the hash: sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|SALT) For more information, refer to Generate Hash.                                                                                                                                                                                                                                                                                                                                                             | a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0                                                                                                                             |
| more_info<br />`mandatory for Wealth Tech`      | `JSON` This parameter contains various fields including the Wealth Tech object (**wtParams**). For more information on wtParams object field, refer to Wealth Tech object (wtParams) fields Description.                                                                                                                                                                                                                                                                                                                                                                                                                                     | Refer to Wealth Tech object (wtParams) fields Description                                                                                                            |
| lastname<br />`optional`                        | `String` The last name of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Sharma                                                                                                                                                               |
| address1<br />`optional`                        | `String` The first line of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 123 Main Street                                                                                                                                                      |
| address2<br />`optional`                        | `String` The second line of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Apartment 4B                                                                                                                                                         |
| city<br />`optional`                            | `String` The city where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Mumbai                                                                                                                                                               |
| state<br />`optional`                           | `String` The state where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Maharashtra                                                                                                                                                          |
| country<br />`optional`                         | `String` The country where your customer resides.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | India                                                                                                                                                                |
| zipcode<br />`optional`                         | `String` Billing address zip code is mandatory for the cardless EMI option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 400001                                                                                                                                                               |
| udf1<br />`mandatory for Cross-Border Payments` | `String` This parameter has been made for you to keep any information corresponding to the transaction. **Note**: This parameter must contain buyer's PAN number for Cross-Border Payments.                                                                                                                                                                                                                                                                                                                                                                                                                                                  | ABCDE1234F                                                                                                                                                           |
| udf2<br />`optional`                            | `string` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 1                                                                                                                                                    |
| udf3<br />`mandatory for Cross-Border Payments` | `String` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | GSTIN123456                                                                                                                                                          |
| udf4<br />`optional`                            | `String` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 2                                                                                                                                                    |
| udf5<br />`optional`                            | `String` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 3                                                                                                                                                    |
| additional_charges<br />`optional`              | `String` Collect additional charges for the transaction. For example, platform fee                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 10.00                                                                                                                                                                |

<Accordion title="Hash Calculation" icon="fa-code">
  The hash is calculated using SHA-512 algorithm with the following field sequence:

  ```
  key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|salt
  ```

  <Accordion title="Hash Generation Steps" icon="fa-code">
    1. Concatenate fields in the specified order using pipe (|) separator
    2. Append the salt at the end
    3. Apply SHA-512 hashing to the concatenated string
    4. Use the resulting hash as the `hash` parameter
  </Accordion>
</Accordion>

### Wealth Tech object (wtParams) fields Description

#### Sample JSON

### Sample JSON Payload Structure

```json
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
```

#### Field descriptions

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
        type <br />
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
        amount <br />
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
        receipt <br />
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
        mf_member_id <br />
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
        mf_user_id <br />
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
        mf_partner <br />
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
        mf_investment_type <br /> `mandatory`
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
        plan <br />
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
        folio <br />
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
        option <br />
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
        scheme <br />
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
        mf_amc_code <br />
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

<Accordion title="Validation Rules" icon="fa-code">
  <Accordion title="Mandatory Field Validations" icon="fa-code">
    * **type**: Must always be `"mutual_fund"`
    * **amount**: Must match the overall order amount and be in paise
    * **receipt**: Must be unique across transactions
    * **mf\_member\_id**: Must be numeric with length between 5-20 characters
    * **mf\_user\_id**: Maximum 10 characters allowed
    * **mf\_partner**: Must be one of: `"cams"`, `"kfin"`, `"bse"`, `"nse"`
    * **mf\_investment\_type**: Only `"L"` (Lump Sum) or `"S"` (SIP) allowed
  </Accordion>

  <Accordion title="Optional Field Validations" icon="fa-code">
    * **mf\_amc\_code**: Maximum 5 characters
    * **receipt**: Maximum 25 characters for SIP registration ID

    ***
  </Accordion>
</Accordion>

## Sample Request

```bash
curl -i 'https://test.payu.in/_payment' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \
  -H 'content-type: application/x-www-form-urlencoded' \
  --data-urlencode 'hash=fbc07b5517029242fd97b982816eb372d6501c1...' \
  --data-urlencode 'key=KOEfPI' \
  --data-urlencode 'txnid=7f41f520f71b' \
  --data-urlencode 'api_version=21' \
  --data-urlencode 'amount=50000' \
  --data-urlencode 'productinfo=Mutual Fund' \
  --data-urlencode 'firstname=John' \
  --data-urlencode 'email=john@example.com' \
  --data-urlencode 'phone=9876543210' \
  --data-urlencode 'si=1' \
  --data-urlencode 'free_trial=1' \
  --data-urlencode 'si_details={"billingAmount":"50000.00","billingCurrency":"INR","billingCycle":"MONTHLY","billingInterval":1,"paymentStartDate":"2024-11-01","paymentEndDate":"2025-11-01"}' \
  --data-urlencode 'surl=https://your-success-url.com' \
  --data-urlencode 'furl=https://your-failure-url.com' \
  --data-urlencode 'more_info={"wtParams":[{"type":"mutual_fund","plan":"GD","amount":"50000","option":"G","scheme":"LT","receipt":"77407","mf_member_id":"123445","mf_user_id":"77407","mf_partner":"cams","mf_investment_type":"L","mf_amc_code":"UTB"}]}'


```

## Sample response

### Response Handling

After the customer completes or abandons the payment, PayU POSTs back to your return URL with URL-encoded fields (form post). This payload includes the transaction status, txnid, mihpayid, and a hash you must verify (reverse hashing) before trusting the result.

Sample surl/furl payload:

```json Success
mihpayid=403993715531077182
mode=CC
status=success
unmappedstatus=captured
key=JPM7Fg
txnid=TXN12345
amount=1000.00
productinfo=Pro Plan
firstname=Aditi
email=aditi@example.com
phone=9999999999
udf1=
...
udf5=
PG_TYPE=CC-PG
bankcode=CC
bank_ref_num=896193988312194700
field1=...
field9=Transaction is Successful
hash=<response_hash>
```
```json Failure
mihpayid=403993715531077182
mode=CC
status=failure
unmappedstatus=failed
key=JPM7Fg
txnid=TXN12345
amount=1000.00
productinfo=Pro Plan
firstname=Aditi
email=aditi@example.com
phone=9999999999
udf1=
...
udf5=
PG_TYPE=CC-PG
bankcode=CC
bank_ref_num=
field1=
field2=
...
field9=Transaction Failed
error=E000
error_Message=Bank was unable to authenticate
hash=<response_hash>
```

### Response verification using reverse hashing

Verify the response received above by recomputing SHA-512 using the reverse sequence:

```json
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

* Compare the computed digest to hash from the POST payload (**case-sensitive**).
* Trust the result only if t

### Verify Payment

<Verify_Payment_Tabs />

<br />
