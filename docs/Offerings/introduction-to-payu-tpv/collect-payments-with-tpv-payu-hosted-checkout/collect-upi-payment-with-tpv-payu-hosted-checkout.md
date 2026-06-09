---
title: UPI TPV Integration - PayU Hosted Checkout
deprecated: false
hidden: false
metadata:
  robots: index
---
For UPI integration, you need to post transaction details to PayU with beneficiary details for validation, similar to Net-Banking integration.

The request parameters for UPI integration are the similar as in Net-Banking integration. The `beneficiarydetail` parameter should include the UPI beneficiary details.

<Callout icon="👍" theme="okay">
  Experience the end-to-end UPI TPV flow and instantly generate the complete code for seamless, zero-coding integration into your website

  <HTMLBlock>{`
                    <style>
                    .tooltip-btn {
                        position: relative;
                        background-color: #4CAF50;
                        color: white;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        font-weight: bold; /* Added this line */
                    }
                    .tooltip-btn:hover::after {
                        content: attr(data-tooltip);
                        position: absolute;
                        bottom: 125%;
                        left: 50%;
                        transform: translateX(-50%);
                        background-color: #333;
                        color: white;
                        padding: 5px 10px;
                        border-radius: 4px;
                        white-space: nowrap;
                        font-size: 12px;
                        z-index: 1;
                    }
                    </style>

                    <button onclick="window.open('https://payu.in/integrationlab/tpv', '_blank')" 
                            class="tooltip-btn" 
                            data-tooltip="Automatically generate code including hashing for your eCommerce website to integrate TPV - PayU Hosted Checkout with zero coding knowledge.">
                        Experience the flow and get the code
                    </button>
  `}</HTMLBlock>
</Callout>

**Steps to Integrate**

<Cards columns={2}>
  <Card title="1. Create Transaction" href="#step-1-create-transaction-with-beneficiary-details">
    Create transaction with beneficiary account details for validation

    <br />
  </Card>

  <Card title="2. Post Parameters" href="#step-2-post-the-parameters-to-payu">
    Post the required parameters to PayU payment endpoint

    <br />
  </Card>

  <Card title="3. Check Response" href="#step-3-check-the-response-from-payu">
    Check the transaction response from PayU

    <br />
  </Card>

  <Card title="4. Verify Payment" href="#step-4-verify-the-payment">
    Verify the payment using verify\_payment API
  </Card>
</Cards>

## Step 1: Create transaction with beneficiary details

Create a transaction by including a JSON object with beneficiary details (account numbers and IFSC codes). You can include up to 4 accounts for validation.

## Step 2: Post the parameters to PayU

<Accordion title="Request parameters" icon="fa-table">
  \***Environment**

  The following environments are available for TPV integration:

  |                            |                                                                     |
  | -------------------------- | ------------------------------------------------------------------- |
  | **Test Environment**       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
  | **Production Environment** | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |

  <HTMLBlock>{`
        <table class="request-parameters-table">
          <thead>
            <tr>
              <th>Parameter</th>
              <th>Description</th>
              <th>Example</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>key<br/><code>mandatory</code></td>
              <td><code>String</code> Merchant key provided by PayU during onboarding</td>
              <td>JPg***r</td>
            </tr>
            <tr>
              <td>txnid<br/><code>mandatory</code></td>
              <td><code>String</code> The transaction ID is a unique reference for each order. Duplicate transaction IDs are not allowed.</td>
              <td>ypl938459435</td>
            </tr>
            <tr>
              <td>amount<br/><code>mandatory</code></td>
              <td><code>String</code> Transaction amount</td>
              <td>100</td>
            </tr>
            <tr>
              <td>productinfo<br/><code>mandatory</code></td>
              <td><code>String</code> Product description</td>
              <td>Test Product</td>
            </tr>
            <tr>
              <td>firstname<br/><code>mandatory</code></td>
              <td><code>String</code> Customer's first name</td>
              <td>John</td>
            </tr>
            <tr>
              <td>email<br/><code>mandatory</code></td>
              <td><code>String</code> Customer's email address</td>
              <td>john@example.com</td>
            </tr>
            <tr>
              <td>phone<br/><code>mandatory</code></td>
              <td><code>String</code> Customer's phone number</td>
              <td>9999999999</td>
            </tr>
            <tr>
              <td>beneficiarydetail<br/><code>mandatory</code></td>
              <td><code>String</code> JSON object that contains account numbers and corresponding IFSC codes (max 4 accounts) in the same order</td>
              <td><a href="#beneficiarydetail-json-object-fields">beneficiarydetail JSON Object Fields</a></td>
            </tr>
            <tr>
              <td>surl<br/><code>mandatory</code></td>
              <td><code>String</code> Success URL - PayU will make a POST request with transaction response to this URL if the transaction is successful</td>
              <td>https://www.yoursurl.com</td>
            </tr>
            <tr>
              <td>furl<br/><code>mandatory</code></td>
              <td><code>String</code> Failure URL - PayU will make a POST request with transaction response to this URL if the transaction fails</td>
              <td>https://www.yourfurl.com</td>
            </tr>
            <tr>
              <td>api_version<br/><code>mandatory</code></td>
              <td><code>String</code> Version of the API</td>
              <td>6</td>
            </tr>
            <tr>
              <td>hash<br/><code>mandatory</code></td>
              <td><code>String</code> SHA512 hash calculated using the formula:<br/>sha512(key|txnid|amount|productinfo|<br/>
                firstname|email|udf1|udf2|udf3|udf4|udf5||||||<br/>
        beneficiarydetail|SALT)</td>
              <td></td>
            </tr>
          </tbody>
        </table>
  `}</HTMLBlock>

  > 📘 Hash calculation
  >
  > The hash is calculated using the following formula:
  >
  > ```
  > sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT)
  > ```
  >
  > Replace `SALT` with the salt value provided during onboarding.
</Accordion>

<Accordion title="beneficiarydetail JSON object fields" icon="fa-code">
  The `beneficiarydetail` parameter should be a JSON object with the following structure:
<HTMLBlock>
{`
  <table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>beneficiaryAccountNumber</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> List of account numbers separated by pipe symbol (|). Maximum 4 accounts.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"002001600674|00000031957292212|00000035955239352|00000035955239352"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>ifscCode</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> List of corresponding IFSC codes separated by pipe symbol (|). Maximum 4 IFSC codes in the same order as account numbers.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"KTKB0000046|KTKB0000023|KTKB0000035|KTKB0000035"</p></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>
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

## Step 3: Check the response from PayU

After posting the parameters, PayU will return a response with transaction details.

<Accordion title="Hash Validation Logic for payment response (Reverse Hashing)" icon="fa-code">
  To validate the authenticity of the response, you can calculate the reverse hash using:

  ```
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  > 📘 beneficiarydetail parameter not required in reverse hashing:
  >
  > The `beneficiarydetail` parameter is not required when calculating the reverse hash.
</Accordion>

<Accordion title="Response parameters" icon="fa-code">
  | Param Name       | Description                                                                                                                    |
  | ---------------- | ------------------------------------------------------------------------------------------------------------------------------ |
  | mihpayid         | It is a unique reference number created for each transaction at PayU's end.                                                    |
  | merchantid       | It is the unique ID of the merchant.                                                                                           |
  | txnid            | Transaction ID provided by the merchant during the transaction request.                                                        |
  | transaction\_fee | Transaction fee for this transaction (e.g., fixed fee of INR 10 for Net Banking).                                              |
  | discount         | The discount/cashback amount provided by the bank, if applicable.                                                              |
  | amount           | The amount after discount (if any).                                                                                            |
  | paymentgatewayid | Identifier for the payment gateway/bank sending the response.                                                                  |
  | pg               | The payment gateway used for the transaction (e.g., "NB" for Net Banking).                                                     |
  | status           | Status of the transaction. Possible values: success, failure, pending. A pending status is considered as a failed transaction. |
  | key              | Merchant key.                                                                                                                  |
  | addedon          | Timestamp of the transaction (e.g., 2023-02-01 12:01:22).                                                                      |
  | bankcode         | Bank code used in the transaction.                                                                                             |
  | error            | Error code (e.g., "E000" indicates no error).                                                                                  |
  | error\_Message   | Description of any errors encountered.                                                                                         |

  > 📘 Store the mihpayid and txnid parameter values in response:
  >
  > Make sure to store the `mihpayid` and `txnid` parameter values from the response for future reference and reconciliation.
</Accordion>

<Accordion title="Sample response" icon="fa-code">
  ```
  Array
  (
      [mihpayid] => 99995401486671
      [status] => success
      [txnid] => 4245248agh5519827ec
      [amount] => 100.00
      [addedon] => 2025-01-28 18:36:35
      [productinfo] => Product Info
      [hash] => e9272f99eace0c7803834e94dd88f0b9d05f1e95cd86c84c7ef8e5670a39bf1ccde2222ed7e73c2a0e60eb8cd8d5457e0ebdef0d01c1c04c7d5b20b8a2d4901
      [bankcode] => SBITPV
      [error_Message] => No Error
  )
  ```
</Accordion>

## Step 4: Verify the payment

<Verify_Payment_Tabs />