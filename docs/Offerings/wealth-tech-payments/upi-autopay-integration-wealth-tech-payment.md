---
title: UPI Autopay Integration - Wealth Tech Payment
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
This section explains how to implement the **_payment** API for by Wealth Tech merchants to collect UPI recurring payments using Merchant Hosted Checkout integration. The **_payment** API includes the *_more_info_ parameter contains various fields including the Wealth Tech object (**wtParams**).

<Callout icon="📘" theme="info">
  **Note**: Currently, PayU supports only UPI, Netbanking, UPI autopay and Enach modes for Wealth Tech payments. You must note that cards are not supported.
</Callout>

## Step 1: Initiate the Consent Transaction

<Accordion title="Environment" icon="fa-plug">
<PaymentAPIEnvironment />
</Accordion>

<Accordion title="Request Parameters" icon="fa-exchange">
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
  | api\_version <br /> `mandatory`                 | API version must be posted as `21`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 21                                                                                                                                                                   |
  | si<br />`mandatory`                             | This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.<br />**Notes**: You can modify or cancel existing recurring payment registration as described in the following sections: <br />- Manage Recurring Payment for Cards <br />- Manage UPI Recurring Transaction                                                                                                                                                                                                                     | 1                                                                                                                                                                    |
  | free\_trial<br />`optional`                     | This is mandatory only if the merchant wants to support free trial use cases. In this case, PayU adjusts the transaction amount as INR 2.00 for cards and UPI and INR 0.00 for Net Banking irrespective of what amount is passed against the amount field in the request.                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                      |
  | si\_details<br />`mandatory`                    | This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.<br />**Note**: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers ( for more details refer [https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0) ) This is a JSON object and it includes a set of fields. For more information, refer to SI Parameter JSON Details                                      | \{"billingAmount": "100.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"} |
  | hash<br />`mandatory`                           | `String` The hash calculated by the merchant using the key and salt provided by PayU. The format for calculating the hash: sha512(key\\\|txnid\\\|amount\\\|productinfo\\\|firstname\\\|email\\\|udf1\\\|udf2\\\|udf3\\\|udf4\\\|udf5\\\|\\\|\\\|\\\|\\\|\\\|SALT) For more information, refer to Generate Hash.                                                                                                                                                                                                                                                                                                                             | a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0                                                                                                                             |
  | more\_info<br />`mandatory for Wealth Tech`     | `JSON` This parameter contains various fields including the Wealth Tech object (**wtParams**). For more information on wtParams object field, refer to Wealth Tech object (wtParams) fields Description.                                                                                                                                                                                                                                                                                                                                                                                                                                     | Refer to Wealth Tech object (wtParams) fields Description                                                                                                            |
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
  | additional\_charges<br />`optional`             | `String` Collect additional charges for the transaction. For example, platform fee                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 10.00                                                                                                                                                                |
</Accordion>

<Accordion title="Wealth Tech Object (wtParams) Fields" icon="fa-cog">
  ### Wealth Tech object wtparams fields description

  <Accordion title="Sample JSON Structure:" icon="fa-code">
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
  </Accordion>

  <Accordion title="Wealth Tech object (wtParams) fields Description" icon="fa-cog">
    <Accordion title="Sample JSON" icon="fa-code">
      ```
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
    </Accordion>

    <Accordion title="Fields description" icon="fa-table">
      These parameters are included within the `more_info` field as a JSON array under the fiedl `wtParams`:

      <Table align={["left","left","left"]}>
        <thead>
          <tr>
            <th style={{ textAlign: "left" }}>
              Parameter
            </th>

            <th style={{ textAlign: "left" }}>
              Description
            </th>

            <th style={{ textAlign: "left" }}>
              Example
            </th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td style={{ textAlign: "left" }}>
              type <br />
              `mandatory`
            </td>

            <td style={{ textAlign: "left" }}>
              `string` - Transaction type, must be "mutual\_fund"
            </td>

            <td style={{ textAlign: "left" }}>
              `"mutual_fund"`
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              amount <br />
              `mandatory`
            </td>

            <td style={{ textAlign: "left" }}>
              `numeric` - Amount in paise, must match order amount
            </td>

            <td style={{ textAlign: "left" }}>
              `50000`
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              receipt <br />
              `mandatory`
            </td>

            <td style={{ textAlign: "left" }}>
              `string` - Unique PG reference number (max 25 chars)
            </td>

            <td style={{ textAlign: "left" }}>
              `"77407"`
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              mf\_member\_id <br />
              `mandatory`
            </td>

            <td style={{ textAlign: "left" }}>
              `numeric` - Member ID issued by mutual fund platform (5-20 chars)
            </td>

            <td style={{ textAlign: "left" }}>
              `"123445"`
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              mf\_user\_id <br />
              `mandatory`
            </td>

            <td style={{ textAlign: "left" }}>
              `string` - Unique mutual fund user/client ID (max 10 chars)
            </td>

            <td style={{ textAlign: "left" }}>
              `"77407"`
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              mf\_partner <br />
              `mandatory`
            </td>

            <td style={{ textAlign: "left" }}>
              `string` - Mutual fund platform: cams, kfin, bse, nse (max 4 chars)
            </td>

            <td style={{ textAlign: "left" }}>
              `"cams"`
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              mf\_investment\_type <br /> `mandatory`
            </td>

            <td style={{ textAlign: "left" }}>
              `string` - Investment type: L (Lump Sum) or S (SIP) (single char)
            </td>

            <td style={{ textAlign: "left" }}>
              `"L"`
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              plan <br />
              `optional`
            </td>

            <td style={{ textAlign: "left" }}>
              `string` - Mutual fund plan name
            </td>

            <td style={{ textAlign: "left" }}>
              `"GD"`
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              folio
              `optional`
            </td>

            <td style={{ textAlign: "left" }}>
              `string` - Unique mutual fund account identifier
            </td>

            <td style={{ textAlign: "left" }}>
              `"12345678"`
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              option <br />
              `optional`
            </td>

            <td style={{ textAlign: "left" }}>
              `string` - Mutual fund plan option
            </td>

            <td style={{ textAlign: "left" }}>
              `"G"`
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              scheme <br />
              `optional`
            </td>

            <td style={{ textAlign: "left" }}>
              `string` - Mutual fund type/scheme
            </td>

            <td style={{ textAlign: "left" }}>
              `"LT"`
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              mf\_amc\_code <br />
              `optional`
            </td>

            <td style={{ textAlign: "left" }}>
              `string` - Asset Management Company code (max 5 chars)
            </td>

            <td style={{ textAlign: "left" }}>
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
    </Accordion>
  </Accordion>
</Accordion>

<Accordion title="Hash Calculation" icon="fa-key">
  Concatenate fields in this exact sequence, then
  <Glossary>SHA</Glossary>-512:

  ```plaintext
  key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|SALT
  ```

  * Use empty strings for missing udf\*.
  * Compute on your server and include the lowercase hex digest as hash.

  For more information, refer to  <a href="generate-hash-payu-hosted" target="_blank"> Generate Hash</a>.

  ### Sample Code for Hashing

  Concatenate fields in this exact sequence, then
  <Glossary>SHA</Glossary>-512:

  ```plaintext
  key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|SALT
  ```

  * Use empty strings for missing udf\*.
  * Compute on your server and include the lowercase hex digest as hash.

  For more information, refer to  <a href="generate-hash-payu-hosted" target="_blank"> Generate Hash</a>.

  ### Sample Code for Hashing

  <HashingSample />
</Accordion>

<Accordion title="Sample Request" icon="fa-exchange">
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
</Accordion>

## Step 2: Check Response from PayU

<Accordion title="Success Response" icon="fa-exchange">
  ```json
  {
      "status": 1,
      "message": "Transaction Processed successfully",
      "details": {
          "transactionid": "48101c0c-5265-4c2a-b6d0-e6e73d42809e",
          "authpayuid": "999990000005920",
          "amount": "50000.00",
          "txnid": "7f41f520f71b",
          "status": "success",
          "firstname": "John",
          "email": "john@example.com",
          "phone": "9876543210",
          "productinfo": "Mutual Fund",
          "hash": "reverse_hash_value",
          "key": "KOEfPI"
      }
  }
  ```
</Accordion>

<Accordion title="Failure Response" icon="fa-exchange">
  ```json
  {
      "status": 0,
      "message": "Invalid Parameter: mf_partner must be less than or equal to 4 characters."
  }
  ```
</Accordion>

<Accordion title="Response Parameters" icon="fa-exchange">
  | Parameter         | Description                    |
  | ----------------- | ------------------------------ |
  | **status**        | 1 for success, 0 for failure   |
  | **message**       | Transaction status message     |
  | **transactionid** | PayU transaction ID            |
  | **authpayuid**    | PayU authorization ID          |
  | **amount**        | Transaction amount             |
  | **txnid**         | Merchant transaction ID        |
  | **hash**          | Response hash for verification |
</Accordion>

<Accordion title="Hash Verification" icon="fa-key">
  Verify response using reverse hash calculation:

  ```
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```
</Accordion>

## Step 3: Verify the Payment

<Verify_Payment_Tabs />


## Step 4: Initiate Recurring Payment
<Accordion title="Environment" icon="fa-key">
|                        |                                                                      |
| :--------------------- | :------------------------------------------------------------------- |
| Production Environment | \<[https://info.payu.in/merchant/>](https://info.payu.in/merchant/>) |
| Test Environment       | \<[https://test.payu.in/merchant/>](https://test.payu.in/merchant/>) |
</Accordion>
<Accordion title="Request parameters" icon="fa-key">
<HTMLBlock>{`

<table> <tr> <th>Parameter</th> <th>Description</th> <th>Example</th> </tr> <tr> <td>key <code>mandatory</code></td> <td><code>String</code> - The merchant key provided by PayU</td> <td>JPM7Fg</td> </tr> <tr> <td>command <code>mandatory</code></td> <td><code>String</code> - Command to execute the recurring transaction API. Must be si_transaction</td> <td>si_transaction</td> </tr> <tr> <td>var1 <code>mandatory</code></td> <td><code>JSON Object</code> - JSON-format object containing mandatory and optional fields for the request</td> <td>{"authpayuid": "6611192557","invoiceDisplayNumber":"12345678910","amount": 3,"txnid": "REC15113506209","phone": "9999999999","email": "chota.bheem@gmail.com"}</td> </tr> <tr> <td>var1.authpayuid <code>mandatory</code></td> <td><code>String</code> - Authorization PayU ID (within var1 object)</td> <td>6611192557</td> </tr> <tr> <td>var1.invoiceDisplayNumber <code>mandatory</code></td> <td><code>String</code> - Display invoice number (within var1 object)</td> <td>12345678910</td> </tr> <tr> <td>var1.amount <code>mandatory</code></td> <td><code>Float</code> - Transaction amount (within var1 object)</td> <td>3.00</td> </tr> <tr> <td>var1.txnid <code>mandatory</code></td> <td><code>String</code> - Transaction ID generated by the merchant (within var1 object)</td> <td>REC15113506209</td> </tr> <tr> <td>var1.phone <code>mandatory</code></td> <td><code>String</code> - Customer's phone number (within var1 object)</td> <td>9999999999</td> </tr> <tr> <td>var1.email <code>mandatory</code></td> <td><code>String</code> - Customer's email address (within var1 object)</td> <td>chota.bheem@gmail.com</td> </tr> <tr> <td>var1.udf2 <code>optional</code></td> <td><code>String</code> - User-defined field for additional information (within var1 object)</td> <td>""</td> </tr> <tr> <td>var1.udf3 <code>optional</code></td> <td><code>String</code> - User-defined field for additional information (within var1 object)</td> <td>""</td> </tr> <tr> <td>var1.udf4 <code>optional</code></td> <td><code>String</code> - User-defined field for additional information (within var1 object)</td> <td>""</td> </tr> <tr> <td>var1.udf5 <code>optional</code></td> <td><code>String</code> - User-defined field for additional information (within var1 object)</td> <td>""</td> </tr> <tr> <td>hash <code>mandatory</code></td> <td><code>String</code> - SHA512 hash generated by concatenating key|command|var1|salt for request authentication</td> <td>jbUS07Og8BToVZ</td> </tr> </table> `}</HTMLBlock>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
    curl -X POST "https://test.payu.in/merchant/postservice?form=2" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&command=si_transaction&var1={\"authpayuid\": \"6611192557\",\"invoiceDisplayNumber\":\"12345678910\",\"amount\": 3,\"txnid\": \"REC15113506209\",\"phone\": \"9999999999\",\"email\": \"chota.bheem@gmail.com\",\"udf2\": \"\",\"udf3\": \"\",\"udf4\": \"\",\"udf5\": \"\"}&hash=jbUS07Og8BToVZ"
  ```
  ```python
  import requests
  import urllib.parse

  # PayU API endpoint
  url = "https://test.payu.in/merchant/postservice?form=2"

  # Headers
  headers = {
      "accept": "application/json",
      "Content-Type": "application/x-www-form-urlencoded"
  }

  # Form data
  form_data = {
      "key": "JP***g",
      "command": "si_transaction",
      "var1": '{"authpayuid": "6611192557","invoiceDisplayNumber":"12345678910","amount": 3,"txnid": "REC15113506209","phone": "9999999999","email": "chota.bheem@gmail.com","udf2": "","udf3": "","udf4": "","udf5": ""}',
      "hash": "jbUS07Og8BToVZ"
  }

  # Make the POST request
  try:
      response = requests.post(url, headers=headers, data=form_data)
      print(f"Status Code: {response.status_code}")
      print(f"Response: {response.text}")
  except requests.exceptions.RequestException as e:
      print(f"Error: {e}")
  ```
  ```csharp
  using System;
  using System.Collections.Generic;
  using System.Net.Http;
  using System.Text;
  using System.Threading.Tasks;

  class Program
  {
      private static readonly HttpClient client = new HttpClient();

      static async Task Main(string[] args)
      {
          string url = "https://test.payu.in/merchant/postservice?form=2";
          
          // Set headers
          client.DefaultRequestHeaders.Add("accept", "application/json");
          
          // Prepare form data
          var formData = new List<KeyValuePair<string, string>>
          {
              new KeyValuePair<string, string>("key", "JP***g"),
              new KeyValuePair<string, string>("command", "si_transaction"),
              new KeyValuePair<string, string>("var1", "{\"authpayuid\": \"6611192557\",\"invoiceDisplayNumber\":\"12345678910\",\"amount\": 3,\"txnid\": \"REC15113506209\",\"phone\": \"9999999999\",\"email\": \"chota.bheem@gmail.com\",\"udf2\": \"\",\"udf3\": \"\",\"udf4\": \"\",\"udf5\": \"\"}"),
              new KeyValuePair<string, string>("hash", "jbUS07Og8BToVZ")
          };
          
          var formContent = new FormUrlEncodedContent(formData);
          
          try
          {
              HttpResponseMessage response = await client.PostAsync(url, formContent);
              string responseContent = await response.Content.ReadAsStringAsync();
              
              Console.WriteLine($"Status Code: {response.StatusCode}");
              Console.WriteLine($"Response: {responseContent}");
          }
          catch (HttpRequestException e)
          {
              Console.WriteLine($"Error: {e.Message}");
          }
      }
  }
  ```
  ```javascript
  // PayU API call using modern Async/Await Fetch
  async function makePayURequest() {
      const url = "https://test.payu.in/merchant/postservice?form=2";
      
      // Headers
      const headers = {
          "accept": "application/json",
          "Content-Type": "application/x-www-form-urlencoded"
      };
      
      // Form data
      const formData = new URLSearchParams({
          "key": "JP***g",
          "command": "si_transaction",
          "var1": '{"authpayuid": "6611192557","invoiceDisplayNumber":"12345678910","amount": 3,"txnid": "REC15113506209","phone": "9999999999","email": "chota.bheem@gmail.com","udf2": "","udf3": "","udf4": "","udf5": ""}',
          "hash": "jbUS07Og8BToVZ"
      });
      
      try {
          const response = await fetch(url, {
              method: "POST",
              headers: headers,
              body: formData
          });
          
          const responseText = await response.text();
          
          console.log(`Status: ${response.status}`);
          console.log(`Response: ${responseText}`);
          
          return {
              status: response.status,
              data: responseText
          };
          
      } catch (error) {
          console.error("Error:", error);
          throw error;
      }
  }

  // Call the function
  makePayURequest()
      .then(result => console.log("Success:", result))
      .catch(error => console.error("Failed:", error));
  ```
  ```java
  import java.io.IOException;
  import java.net.URI;
  import java.net.URLEncoder;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;
  import java.nio.charset.StandardCharsets;
  import java.time.Duration;
  import java.util.HashMap;
  import java.util.Map;
  import java.util.stream.Collectors;

  public class PayUApiClient {
      
      private static final HttpClient client = HttpClient.newBuilder()
              .connectTimeout(Duration.ofSeconds(30))
              .build();
      
      public static void main(String[] args) {
          try {
              makePayURequest();
          } catch (Exception e) {
              System.err.println("Error: " + e.getMessage());
          }
      }
      
      public static void makePayURequest() throws IOException, InterruptedException {
          String url = "https://test.payu.in/merchant/postservice?form=2";
          
          // Prepare form data
          Map<String, String> formData = new HashMap<>();
          formData.put("key", "JP***g");
          formData.put("command", "si_transaction");
          formData.put("var1", "{\"authpayuid\": \"6611192557\",\"invoiceDisplayNumber\":\"12345678910\",\"amount\": 3,\"txnid\": \"REC15113506209\",\"phone\": \"9999999999\",\"email\": \"chota.bheem@gmail.com\",\"udf2\": \"\",\"udf3\": \"\",\"udf4\": \"\",\"udf5\": \"\"}");
          formData.put("hash", "jbUS07Og8BToVZ");
          
          // Convert to URL encoded string
          String formBody = formData.entrySet().stream()
                  .map(entry -> URLEncoder.encode(entry.getKey(), StandardCharsets.UTF_8) + 
                               "=" + URLEncoder.encode(entry.getValue(), StandardCharsets.UTF_8))
                  .collect(Collectors.joining("&"));
          
          // Build request
          HttpRequest request = HttpRequest.newBuilder()
                  .uri(URI.create(url))
                  .header("accept", "application/json")
                  .header("Content-Type", "application/x-www-form-urlencoded")
                  .POST(HttpRequest.BodyPublishers.ofString(formBody))
                  .build();
          
          // Send request
          HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
          
          System.out.println("Status Code: " + response.statusCode());
          System.out.println("Response: " + response.body());
      }
  }
  ```
  ```php
  // PayU API endpoint
  $url = "https://test.payu.in/merchant/postservice?form=2";

  // Form data
  $postData = [
      'key' => 'JP***g',
      'command' => 'si_transaction',
      'var1' => '{"authpayuid": "6611192557","invoiceDisplayNumber":"12345678910","amount": 3,"txnid": "REC15113506209","phone": "9999999999","email": "chota.bheem@gmail.com","udf2": "","udf3": "","udf4": "","udf5": ""}',
      'hash' => 'jbUS07Og8BToVZ'
  ];

  // Initialize cURL
  $ch = curl_init();

  // Set cURL options
  curl_setopt_array($ch, [
      CURLOPT_URL => $url,
      CURLOPT_POST => true,
      CURLOPT_POSTFIELDS => http_build_query($postData),
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_HTTPHEADER => [
          'accept: application/json',
          'Content-Type: application/x-www-form-urlencoded'
      ],
      CURLOPT_TIMEOUT => 30,
      CURLOPT_FOLLOWLOCATION => true,
      CURLOPT_SSL_VERIFYPEER => false, // Only for testing
  ]);

  // Execute request
  $response = curl_exec($ch);
  $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
  $error = curl_error($ch);

  // Close cURL
  curl_close($ch);

  // Handle response
  if ($error) {
      echo "cURL Error: " . $error . PHP_EOL;
  } else {
      echo "Status Code: " . $httpCode . PHP_EOL;
      echo "Response: " . $response . PHP_EOL;
  }
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  **Success scenario**

  Here is a sample response object returned against recurring payment API when the transaction is successfully charged.

  ```json
  {
    "status": 1,
    "message": "Transaction Processed successfully",
    "details": {
        "REC15113506209": {
            "authpayuid": "25600342065",
            "transactionid": "REC15113506209",
            "amount": "1.00",
            "user_credentials": "",
            "card_token": "",
            "payuid": "",
            "status": "captured",
            "udf1": "",
            "field9": "Transaction Completed Successfully",
            "udf2": "",
            "udf3": "",
            "udf4": "",
            "udf5": "",
            "phone": "9999999999",
            "email": "chota.bheem@gmail.com"
        }
    }
  }
  ```

  **Failure scenarios**

  * Invalid hash

  ```json
  {
      "status": 0,
      "msg": "Invalid Hash."
  }
  ```

  * Basic authentication check failed

  ```json
  {
      "status": 1,
      "message": "Transaction Processed successfully",
      "details": {
          "REC9812123123": {
              "authpayuid": "6611192559",
              "transactionid": "REC9812123123",
              "amount": "1",
              "user_credentials": " ",
              "card_token": " ",
              "payuid": "",
              "status": "failed",
              "field9": "Basic authentication check failed",
              "phone": "",
              "email": ""
          }
      }
  }
  ```
</Accordion>