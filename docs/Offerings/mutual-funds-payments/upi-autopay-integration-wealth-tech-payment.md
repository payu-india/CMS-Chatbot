---
title: UPI Autopay Integration - Mutual Funds
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
This section explains how to implement the **_payment** API for by Wealth Tech merchants to collect UPI recurring payments using seamless integration. The **_payment** API includes the _products_ parameter contains various fields including the Wealth Tech object (**wtParams**).

## Step 1: Initiate the Consent Transaction

<PaymentAPIEnvironment />

<Accordion title="Request Parameters" icon="fa-exchange">
  Now I'll create the cleaned table with only the necessary three columns and proper formatting:

  | Parameter                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Example                                                                                                                                                              |
  | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | key<br />`mandatory`                            | `String` This parameter is the unique merchant key provided by PayU for your merchant account. For more information, refer to Generate Merchant Key and Salt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 8488225                                                                                                                                                              |
  | txnid<br />`mandatory`                          | `Varchar` This parameter is known as Transaction ID (or OrderID). It is the order reference number generated at your (Merchant's) end. It is an identifier which you(merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of same Transaction ID again would fail. Hence, it is essential that you post us a unique transaction ID for every new transaction (Please make sure that the transaction ID being sent to us hasn't been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID'). | fd3e847h2                                                                                                                                                            |
  | amount<br />`mandatory`                         | `float` This parameter should contain the payment amount of the particular transaction. Note: Type-cast the amount to float type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 10                                                                                                                                                                   |
  | productinfo<br />`mandatory`                    | `Varchar` This parameter should contain a brief product description. It should be a string describing the product (The description type is entirely your choice).                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | T-shirt                                                                                                                                                              |
  | firstname<br />`mandatory`                      | `Varchar` This parameter must contain the first name of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Ankit                                                                                                                                                                |
  | email<br />`mandatory`                          | `Varchar` This parameter must contain the email of the customer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [test@gmail.com](mailto:test@gmail.com)                                                                                                                              |
  | phone<br />`mandatory`                          | `Integer` Merchant needs to take the customer's GPay registered phone number and pass in this field. This field will be used for further mapping the customer VPA and initiate a collect request.                                                                                                                                                                                                                                                                                                                                                                                                                                            | 9876543210                                                                                                                                                           |
  | pg<br />`mandatory`                             | `String` This parameter contains the payment method to be enabled to collect payment from your customer. For the list of payment methods and their codes, refer to Payment Mode Codes. For UPI, use UPI.                                                                                                                                                                                                                                                                                                                                                                                                                                     | NB                                                                                                                                                                   |
  | bankcode<br />`mandatory`                       | `string` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. For UPI Autopay, use INTTPV.                                                                                                                                                                                                                                                                                                                                                                                                                                | INTTPV  |
  | surl<br />`mandatory`                           | `string` The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                             | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                                       |
  | furl<br />`mandatory`                           | `String` The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                                 | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                                       |
  | api\_version<br />`mandatory`                   | API version must be posted as `21`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 21                                                                                                                                                                   |
  | si<br />`mandatory`                             | This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.<br />**Notes**: You can modify or cancel existing recurring payment registration as described in the following sections: <br />- Manage Recurring Payment for Cards <br />- Manage UPI Recurring Transaction                                                                                                                                                                                                                     | 1                                                                                                                                                                    |
  | free\_trial<br />`optional`                     | This is mandatory only if the merchant wants to support free trial use cases. In this case, PayU adjusts the transaction amount as INR 2.00 for cards and UPI and INR 0.00 for Net Banking irrespective of what amount is passed against the amount field in the request.                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                      |
  | si\_details<br />`mandatory`                    | This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.<br />**Note**: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers ( for more details refer [https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0) ) This is a JSON object and it includes a set of fields. For more information, refer to SI Parameter JSON Details                                      | \{"billingAmount": "100.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"} |
  | hash<br />`mandatory`                           | `String` The hash calculated by the merchant using the key and salt provided by PayU. The format for calculating the hash: sha(key\\\|txnid\\\|amount\\\|productinfo\\\|firstname\\\|email\\\|udf1\\\|udf2\\\|udf3\\\|udf4\\\|udf5\\\|\\\|\\\|\\\|\\\|\\\|beneficiarydetail\\\|si\_details\\\|\\\|\\\|\\\|\\\|products\\\|salt) For more information, refer to Generate Hash.                                                                                                                                                                                                                                                                | a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0                                                                                                                             |
  | products<br />`mandatory for Wealth Tech`        | `JSON` This parameter contains various fields including the Wealth Tech object (**wtParams**). For more information on wtParams object field, refer to Wealth Tech object wtparams fields description.                                                                                                                                                                                                                                                                                                                                                                                                                                       | Refer to Wealth Tech object wtparams fields description.                                                                                                             |
  | txn_s2s_flow <br />`mandatory`        | `String` This parameter must be passed with the value as 4 for Decoupled flow. | 4 |
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
  | beneficiarydetail<br />`mandatory`              | This is a JSON format text and there should be key named **beneficiaryAccountNumber** with the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key). You can post up to five account details in this parameter.                                                                                                                                                                                                                                                                                                                        | Refer to the beneficiarydetail JSON Object Fields section.                                                                                                           |

  <Accordion title="beneficiarydetail JSON Object Fields" icon="fa-code">
    It must contain the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key). You can post up to five account details in this parameter. For example:

    ```
    {"beneficiaryAccountNumber":"002001600674|00000031957292212|00000035955239352|00000035955239352",  
    "ifscCode":"KTKB0000046|KTKB0000023|KTKB0000035|KTKB0000035"}
    ```

    **Checksum Logic for Hash**

    The following hash logic must be used for the parameters posted:

    > 📘 si\_details parameter in Hashing:
    >
    > The **si\_details** parameter value will be at last or the last value to be appended.
    >
    > ```plaintext
    > ```

    sha(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail||||||products|salt)

    \>
  </Accordion>
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
              folio<br />
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
</Accordion>

<Accordion title="Sample Request" icon="fa-exchange">
  ```curl
  
curl --location 'https://test.payu.in/_payment' \
--header 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \
--header 'content-type: application/x-www-form-urlencoded' \
--header 'Cookie: PHPSESSID=kdihrj6ld6mbevful3ii02rqme; USERTXNINFO=698071743e9724.85896500; PHPSESSID=69ba93505906f' \
--data-urlencode 'key=j6Bb3k' \
--data-urlencode 'txnid=Txn_098f7189' \
--data-urlencode 'amount=50000' \
--data-urlencode 'productinfo=Mutual Fund' \
--data-urlencode 'firstname=John' \
--data-urlencode 'email=john@example.com' \
--data-urlencode 'phone=9876543210' \
--data-urlencode 'pg=UPI' \
--data-urlencode 'bankcode=INTTPV' \
--data-urlencode 'surl=https://apiplayground-response.herokuapp.com/' \
--data-urlencode 'furl=https://apiplayground-response.herokuapp.com/' \
--data-urlencode 'api_version=21' \
--data-urlencode 'hash={{hash}}' \
--data-urlencode 'products={"wtParams":[{"type":"mutual_fund","plan":"GD","amount":"50000","option":"G","scheme":"LT","receipt":"77407","mf_member_id":"123445","mf_user_id":"77407","mf_partner":"cams","mf_investment_type":"L","mf_amc_code":"UTB"}]}' \
--data-urlencode 'txn_s2s_flow=4' \
--data-urlencode 'beneficiarydetail={"beneficiaryAccountNumber":"1111111111","ifscCode":"111111189HSBB001"}'
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
  key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|si_details|||||products|salt
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

<Accordion title="Predebit Notification" icon="fa-message">
  You should call the predebit notification API before initiating the recurring payment.

  <Accordion title="Sample request" icon="fa-code">
    ```cURL
    curl --location 'https://info.payu.in/merchant/postservice.php' \
    --header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642' \
    --form 'form="2"' \
    --form 'key="smsplus"' \
    --form 'command="pre_debit_SI"' \
    --form 					'hash="6e6a34a932bb56bc160cc6b3b40af72e7cfd6cfbf9153edce7b866fe9b87d6d03303e60f810bb7cf2559695bde8033c442e73a8adcfd0957bd8e6fee17b4df37"' \
    --form 'salt="1b1b0"' \
    --form 'var1="{\"authpayuid\":\"25600438037\",\"requestId\":\"c03f0265-b802-4cd9-8a09-1f679957e02e\",\"amount\":\"1.00\",\"debitDate\":\"2025-10-15\",\"invoiceDisplayNumber\":\"ad52cb45-76ae-4aad-8245-b2eb5e737f17\"}"'
    ```
  </Accordion>

  <Accordion title="Request parameters" icon="fa-table">
    | Parameter      | Description                                                                                            |           |        |                                                                                                  |
    | :------------- | :----------------------------------------------------------------------------------------------------- | --------- | ------ | ------------------------------------------------------------------------------------------------ |
    | key `string`   | `mandatory` This parameter is the unique Merchant Key provided by PayU                                 |           |        |                                                                                                  |
    | var1 `object`  | The variable 1 object details.                                                                         |           |        |                                                                                                  |
    | hash `string`  | `mandatory` It is used to avoid the possibility of transaction tampering. Hash formula: \`sha512(key\\ | command\\ | var1\\ | salt)\`. Please regenerate hash at the end everytime you make a change to the request parameters |
    | command `enum` | `mandatory` The command name for this REST API call is pre\_debit\_SI.                                 |           |        |                                                                                                  |

    <Accordion title="var1 Object parameters" icon="fa-table">
      | Parameter                     | Description                                                                                                                                                                                    |
      | :---------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | authPayuId `string`           | `mandatory` The value of mihpayid returned in the payment response of Registration transaction when transaction is successfully completed.                                                     |
      | requestId `string`            | `mandatory` Unique request value generated at merchant’s end to distinguish independent request call.                                                                                          |
      | debitDate `string`            | `mandatory` This field contains the date of debit when the recurring would be charged by merchant.                                                                                             |
      | invoiceDisplayNumber `string` | `optional` This field is required for cards. A unique display number by merchant for every subsequent invoice/recurring charge. This can be displayed on the merchant’s panel to the customer. |
      | amount `number`               | `mandatory` The transaction amount which will be deducted from the customer’s payment instrument.                                                                                              |
      | action `number`               | `optional` Pass "Retrieve" or "Delete" according to the action need to be performed. For more information, refer to Additional Information table.                                              |
    </Accordion>
  </Accordion>

  <Accordion title="Sample response" icon="fa-code">
    ```Json: Success Response
    {
    "status": 1,
    "action": "MANDATE_PRE_DEBIT",
    "message": "Request Processed Successfully"
    }
    ```
    ```Json: Faliure Response
    {
    "status":  “QC”   ----- >> Bank/NPCI Error Code
    "action": "MANDATE_PRE_DEBIT",
    "message": “MANDATE HAS BEEN REVOKED”. ---- >> Description against error code
    }
    ```
  </Accordion>
</Accordion>

<Accordion title="Request parameters" icon="fa-key">
  <HTMLBlock>{`
                                                                    <table> <tr> <th>Parameter</th> <th>Description</th> <th>Example</th> </tr> <tr> <td>key <code>mandatory</code></td> <td><code>String</code> - The merchant key provided by PayU</td> <td>JPM7Fg</td> </tr> <tr> <td>command <code>mandatory</code></td> <td><code>String</code> - Command to execute the recurring transaction API. Must be si_transaction</td> <td>si_transaction</td> </tr> <tr> <td>var1 <code>mandatory</code></td> <td><code>JSON Object</code> - JSON-format object containing transaction details and optional fields. For more information, refer to <a href="https://docs.payu.in/docs/upi-autopay-integration-wealth-tech-payment#var1-object-field-descriptions">var1 object field descriptions</a></td> <td>{"authpayuid": "6611192557","invoiceDisplayNumber":"12345678910","amount": 3,"txnid": "REC15113506209","phone": "9999999999","email": "ashish@gmail.com"}</td> </tr> <tr> <td>hash <code>mandatory</code></td> <td><code>String</code> - SHA512 hash generated by concatenating key|command|var1|salt for request authentication</td> <td>jbUS07Og8BToVZ</td> </tr> </table> 
  `}</HTMLBlock>

  <Accordion title="var1 object field descriptions" icon="fa-cog">
    ### var1 object field descriptions

    <HTMLBlock>{`
                                                                                                                          <table id="var1-parameters"> <tr> <th>Parameter</th> <th>Description</th> <th>Example</th> </tr> <tr> <td colspan="3"><strong>Fields within the var1 JSON object</strong> - <a href="#main-parameters">Back to main parameters</a></td> </tr> <tr> <td>authpayuid <br/><code>mandatory</code></td> <td><code>String</code> - Authorization PayU ID</td> <td>6611192557</td> </tr> <tr> <td>invoiceDisplayNumber <br/><code>mandatory</code></td> <td><code>String</code> - Display invoice number</td> <td>12345678910</td> </tr> <tr> <td>amount <br/><code>mandatory</code></td> <td><code>Float</code> - Transaction amount</td> <td>3.00</td> </tr> <tr> <td>txnid <br/><code>mandatory</code></td> <td><code>String</code> - Transaction ID generated by the merchant</td> <td>REC15113506209</td> </tr> <tr> <td>phone <br/><code>mandatory</code></td> <td><code>String</code> - Customer's phone number</td> <td>9999999999</td> </tr> <tr> <td>email <br/><code>mandatory</code></td> <td><code>String</code> - Customer's email address</td> <td>ashish@gmail.com</td> </tr> <tr> <td>more_info <br/><code>mandatory for Wealth Tech</code></td> <td><code>JSON</code> - This parameter contains various fields including the Wealth Tech object (wtParams). For more information on wtParams object field, refer to Wealth Tech object (wtParams) fields Description table (next table)</td> <td></td> </tr> <tr> <td>udf2 <br/><code>optional</code></td> <td><code>String</code> - User-defined field for additional information</td> <td>""</td> </tr> <tr> <td>udf3 <br/><code>optional</code></td> <td><code>String</code> - User-defined field for additional information</td> <td>""</td> </tr> <tr> <td>udf4 <br/><code>optional</code></td> <td><code>String</code> - User-defined field for additional information</td> <td>""</td> </tr> <tr> <td>udf5 <br/><code>optional</code></td> <td><code>String</code> - User-defined field for additional information</td> <td>""</td> </tr> </table> 
    `}</HTMLBlock>
  </Accordion>

  <Accordion title="Wealth Tech Object (wtParams) Fields" icon="fa-cog">
    ### Wealth Tech object wtparams fields description

    <Accordion title="Sample JSON Structure:" icon="fa-code">
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
              folio<br />
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

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'key=JP***g&command=si_transaction&var1={"authpayuid":"6611192557","invoiceDisplayNumber":"12345678910","amount":3,"txnid":"REC15113506209","phone":"9999999999","email":"chota.bheem@gmail.com","udf2":"","udf3":"","udf4":"","udf5":"","more_info":{"wtParams":[{"type":"mutual_fund","plan":"GD","amount":"50000","option":"G","scheme":"LT","receipt":"77407","mf_member_id":"123445","mf_user_id":"77407","mf_partner":"cams","mf_investment_type":"L","mf_amc_code":"UTB"}]}}&hash=jbUS07Og8BToVZ'

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

<br />
