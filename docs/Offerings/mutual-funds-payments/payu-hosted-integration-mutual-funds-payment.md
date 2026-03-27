---
title: PayU Hosted Integration - Mutual Fund Payments
deprecated: false
hidden: true
metadata:
  robots: index
---
This section explains how to implement the **_payment** API for mutual fund payment using PayU Hosted Checkout integration. The _payment includes the _product_ parameter contains various fields including the Wealth Tech object (**wtParams**).

<Cards columns={3}>
  <Card title="1. Initiate the Payment to PayU" href="#step-1-initiate-the-payment-to-payu">
    Send payment request to PayU through POST endpoint with mandatory parameters include Wealth Tech specific wtParams object for mutual fund transactions

    <br />
  </Card>

  <Card title="2. Check Response from PayU" href="#step-2-check-response-from-payu">
    Handle the response from PayU after transaction processing and verify the reverse hash for data authenticity

    <br />
  </Card>

  <Card title="3. Verify the Payment" href="#step-3-verify-the-payment">
    Reconcile payment details through webhooks or Verify Payments API to ensure accuracy and completeness of each transaction
  </Card>

  <br />
</Cards>

## Step 1: Initiate the Payment to PayU

<PaymentAPIEnvironment />

<Accordion title="Request Parameters" icon="fa-exchange">
  | Parameter                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Example                                                                                                                                                                            |                                                                                                         |                                          |
  | :----------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
  | key<br />`mandatory`                       | `String` This parameter is the unique merchant key provided by PayU for your merchant account. For more information, refer to [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard).                                                                                                                                                                                                                                                                                                                                                                                                                        | 8488225                                                                                                                                                                            |                                                                                                         |                                          |
  | txnid<br />`mandatory`                     | `Varchar` This parameter is known as Transaction ID (or OrderID). It is the order reference number generated at your (Merchant's) end. It is an identifier which you(merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of same Transaction ID again would fail. Hence, it is essential that you post us a unique transaction ID for every new transaction (Please make sure that the transaction ID being sent to us hasn't been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID'). | fd3e847h2                                                                                                                                                                          |                                                                                                         |                                          |
  | amount<br />`mandatory`                    | `float` This parameter should contain the payment amount of the particular transaction. Note: Type-cast the amount to float type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 10.00                                                                                                                                                                              |                                                                                                         |                                          |
  | productinfo<br />`mandatory`               | `Varchar` This parameter should contain a brief product description. It should be a string describing the product (The description type is entirely your choice).                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | T-shirt                                                                                                                                                                            |                                                                                                         |                                          |
  | firstname<br />`mandatory`                 | `Varchar` This parameter must contain the first name of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Ankit                                                                                                                                                                              |                                                                                                         |                                          |
  | email<br />`mandatory`                     | `Varchar` This parameter must contain the email of the customer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [test@gmail.com](mailto:test@gmail.com)                                                                                                                                            |                                                                                                         |                                          |
  | phone<br />`mandatory`                     | `Integer` Merchant needs to take the customer's GPay registered phone number and pass in this field. This field will be used for further mapping the customer VPA and initiate a collect request.                                                                                                                                                                                                                                                                                                                                                                                                                                            | 9876543210                                                                                                                                                                         |                                                                                                         |                                          |
  | surl<br />`mandatory`                      | `string` The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                             | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                                                     |                                                                                                         |                                          |
  | furl<br />`mandatory`                      | `String` The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                                 | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                                                     |                                                                                                         |                                          |
  | api\_version <br /> `mandatory`            | API version must be posted as `21`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 21                                                                                                                                                                                 |                                                                                                         |                                          |
  | hash<br />`mandatory`                      | `String` The hash calculated by the merchant using the key and salt provided by PayU. The format for calculating the hash: sha(key\\\|txnid\\\|amount\\\|productinfo\\\|firstname\\\|email\\\|udf1\\\|udf2\\\|udf3\\\|udf4\\\|udf5\\\|\\\|\\\|\\\|\\\|                                                                                                                                                                                                                                                                                                                                                                                       | beneficiarydetail\\\|\\\|\\\|\\\|                                                                                                                                                  | \\\|products\\\|salt) For more information, refer to [Generate Hash](doc:hashing-request-and-response). | a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0 |
  | products <br />`mandatory for Wealth Tech` | `JSON` This parameter contains various fields including the Wealth Tech object (**wtParams**). For more information on wtParams object field, refer to [ Wealth Tech object (wtParams) fields Description](https://docs.payu.in/docs/payu-hosted-integration-mutual-funds-payment#wealth-tech-object-wtparams-fields-description).                                                                                                                                                                                                                                                                                                                                                                                 | Refer to [ Wealth Tech object (wtParams) fields Description](https://docs.payu.in/docs/payu-hosted-integration-mutual-funds-payment#wealth-tech-object-wtparams-fields-description) |                                                                                                         |                                          |
  | beneficiarydetail<br />`mandatory `        | `String` String JSON object that contains account numbers and corresponding IFSC codes (max 4 accounts) in the same order                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Sharma                                                                                                                                                                             |                                                                                                         |                                          |
  | lastname<br />`optional`                   | `String` The last name of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Sharma                                                                                                                                                                             |                                                                                                         |                                          |
  | address1<br />`optional`                   | `String` The first line of the billing address                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 123 Main Street                                                                                                                                                                    |                                                                                                         |                                          |
  | address2<br />`optional`                   | `String` The second line of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Apartment 4B                                                                                                                                                                       |                                                                                                         |                                          |
  | city<br />`optional`                       | `String` The city where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Mumbai                                                                                                                                                                             |                                                                                                         |                                          |
  | state<br />`optional`                      | `String` The state where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Maharashtra                                                                                                                                                                        |                                                                                                         |                                          |
  | country<br />`optional`                    | `String` The country where your customer resides.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | India                                                                                                                                                                              |                                                                                                         |                                          |
  | zipcode<br />`optional`                    | `String` Billing address zip code is mandatory for the cardless EMI option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 400001                                                                                                                                                                             |                                                                                                         |                                          |
  | udf1<br />`optional`                       | `String` This parameter has been made for you to keep any information corresponding to the transaction.<br /> **Note**: This parameter must contain buyer's PAN number for Cross-Border Payments.                                                                                                                                                                                                                                                                                                                                                                                                                                            | ABCDE1234F                                                                                                                                                                         |                                                                                                         |                                          |
  | udf2<br />`optional`                       | `string` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 1                                                                                                                                                                  |                                                                                                         |                                          |
  | udf3<br />`optional`                       | `String` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | GSTIN123456                                                                                                                                                                        |                                                                                                         |                                          |
  | udf4<br />`optional`                       | `String` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 4                                                                                                                                                                  |                                                                                                         |                                          |
  | udf5<br />`optional`                       | `String` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 5                                                                                                                                                                  |                                                                                                         |                                          |

  <Accordion title="beneficiarydetail JSON Object Fields" icon="fa-code">
    The `beneficiarydetail` parameter should be a JSON object with the following structure:

    <Table align={["left","left","left"]}>
      <thead>
        <tr>
          <th style={{ textAlign: "left" }}>
            Field
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
            beneficiaryAccountNumber
          </td>

          <td style={{ textAlign: "left" }}>
            `String` List of account numbers separated by pipe symbol (|). Maximum 4 accounts.
          </td>

          <td style={{ textAlign: "left" }}>
            "002001600674|
            00000031957292212|
            00000035955239352|
            00000035955239352"
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            ifscCode
          </td>

          <td style={{ textAlign: "left" }}>
            `String` List of corresponding IFSC codes separated by pipe symbol (|). Maximum 4 IFSC codes in the same order as account numbers.
          </td>

          <td style={{ textAlign: "left" }}>
            "KTKB0000046|
            KTKB0000023|
            KTKB0000035|
            KTKB0000035"
          </td>
        </tr>
      </tbody>
    </Table>

    **Example JSON**:

    ```json
    {
      "beneficiaryAccountNumber": "002001600674|00000031957292212|00000035955239352|00000035955239352",
      "ifscCode": "KTKB0000046|KTKB0000023|KTKB0000035|KTKB0000035"
    }
    ```

    > 📘 beneficiarydetail parameter in hashing:
    >
    > * The `beneficiarydetail` parameter must be included in the hash calculation.
    > * The format should be exactly as shown in the hash formula above.
    > * Replace SALT with the salt value provided to you during onboarding.
  </Accordion>

  <Mutual_Funds_Product_JSON />
</Accordion>

<Accordion title="Hash Calculation" icon="fa-key">
  Concatenate fields in this exact sequence, then
  <Glossary>SHA</Glossary>-512:

  ```plaintext
  hash = key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail||||||products|salt
  ```

  * Use empty strings for missing udf\*.
  * Compute on your server and include the lowercase hex digest as hash.

  For more information, refer to  <a href="generate-hash-payu-hosted" target="_blank"> Generate Hash</a>.
</Accordion>

<Accordion title="Sample Request" icon="fa-exchange">
  ```bash
  curl -i 'https://test.payu.in/_payment' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \
  -H 'content-type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=KOEfPI' \
  --data-urlencode 'txnid=7f41f520f71b' \
  --data-urlencode 'amount=50000' \
  --data-urlencode 'productinfo=Mutual Fund' \
  --data-urlencode 'firstname=John' \
  --data-urlencode 'email=john@example.com' \
  --data-urlencode 'phone=9876543210' \
  --data-urlencode 'surl=https://apiplayground-response.herokuapp.com/' \
  --data-urlencode 'furl=https://apiplayground-response.herokuapp.com/' \
  --data-urlencode 'api_version=21' \
  --data-urlencode 'hash=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0' \
  --data-urlencode 'product={"wtParams":[{"type":"mutual_fund","plan":"GD","amount":"50000","option":"G","scheme":"LT","receipt":"77407","mf_member_id":"123445","mf_user_id":"77407","mf_partner":"cams","mf_investment_type":"L","mf_amc_code":"UTB"}]}'
  ```
</Accordion>

## Step 2: Check Response from PayU

<Accordion title="Success Response" icon="fa-exchange">
  ```plaintext
  mihpayid=403993715537000168&mode=UPI&status=success&key=j6Bb3k&txnid=txn_7798908nnm008&amount=50000.00&addedon=2026-03-17 14:48:25&productinfo=iphone&firstname=Sumit&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test@gmail.com&phone=7715995865&udf1=&udf2=&udf3=&udf4=Executed Callback&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&card_token=&card_no=&field0=&field1=9999999999@upi&field2=&field3=ps@paytm&field4=&field5=403993715537000168&field6=&field7=00|APPROVED OR COMPLETED SUCCESSFULLY&field8=&field9=Transaction Successful|Completed Using Callback&payment_source=sist&cardToken=&authenticaticationMethod=&PG_TYPE=NB-PG&error=E000&error_Message=No Error&net_amount_debit=50000&discount=0.00&offer_key=&offer_availed=&unmappedstatus=captured&hash=833ca55940bf5fa7ef6d334872848d4ad2ec775966aba23a8c3e82ecf5292ea7bd3e9573202ee093fdbc91dedd1cd6ff919411d84bce76c8cb676921cc997191&bank_ref_no=ICI9TI0Y06S0HCGA1DDHTN3ZH7YL0MPYBRUQ&bank_ref_num=ICI9TI0Y06S0HCGA1DDHTN3ZH7YL0MPYBRUQ&bankcode=INTENT&surl=https://test.payu.in/admin/test_response&curl=https://test.payu.in/admin/test_response&furl=https://test.payu.in/admin/test_response&IsStandingInstructionSet=1
  ```
</Accordion>

<Accordion title="Hash Verification" icon="fa-key">
  Verify response using reverse hash calculation:

  ```
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  <Callout icon="👍" theme="okay">
    **Reference:** PayU recommends you to use the PayU Hash Verification Tool to validate the reverse hashing. For more information, refer to [Using PayU Hash Verification Tool](doc:using-payu-hash-verification-tool)
  </Callout>
</Accordion>

## Step 3: Verify the Payment

<Verify_Payment_Tabs />
