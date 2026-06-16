---
title: NEFT/RTGS Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - NEFT Integration for TPV
    - ' Third Party Validation NEFT Integration'
    - API Integration for NEFT TPV
    - ' PayU NEFT TPV Integration'
    - TPV NEFT Setup Guide
    - RTGS Integration for TPV
    - ' Third Party Validation RTGS Integration'
    - API Integration for RTGS TPV
    - ' PayU RTGS TPV Integration'
    - TPV RTGS Setup Guide
  robots: index
next:
  description: ''
---
Integrate <Glossary>TPV</Glossary> through NEFT/RTGS using the procedure described in this section.

**Steps to integrate**
<Cards columns={2}>
  <Card title="1. List Account Numbers" href="#step-1-list-the-account-numbers">
    Collect or prepare account numbers to post to PayU for TPV
  </Card>
  <Card title="2. Post Parameters" href="#step-2-post-the-parameters-to-payu">
    Post the Collect Payment (**_payment**) request with NEFT/RTGS parameters
  </Card>
  <Card title="3. Check Response" href="#step-3-check-the-response-from-payu">
    Validate the response hash and store **mihpayid** and **txnid**
  </Card>
</Cards>

## Step 1: List the Account Numbers

Collect or prepare a list of account numbers that must be posted to PayU for TPV at step 2.

## Step 2: Post the parameters to PayU

With the following additional parameters, make the transaction request with the customer's bank account number to the PayU using the Collect Payment (**\_payment**) API. For more information, refer to [Collect Payment API - Merchant Hosted Checkout](doc:_payment_merchant_hosted).

<PaymentAPIEnvironment />

<Accordion title="Request parameters" icon="fa-code">
<HTMLBlock>{`
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
        pg
      </td>

      <td>
        It defines the payment category for which you wish to perform TPV. For Net Banking, pg= 'NEFTRTGS.
      </td>

      <td>
        NEFTRTGS
      </td>
    </tr>

    <tr>
      <td>
        bankcode
      </td>

      <td>
        The bankcode for the NEFT/RTGS transaction. For more information, refer to [Bank Codes for TPV](doc:bank-codes-for-tpv).
        This parameter defines the bankcode for NEFT/RTGS. **EFTAXTPV** must be used as bankcode for NEFT/RTGS.
      </td>

      <td>
        EFTAXTPV
      </td>
    </tr>

    <tr>
      <td>
        beneficiarydetail
      </td>

      <td>
        This is a JSON format text and there should be key named beneficiaryAccountNumber with account number as value and ifscCode with customer IFSC code as value.
      </td>

      <td>
        \{"beneficiaryAccountNumber":"6612262_**5|323132312**_3123",  
        "ifscCode":"KKBK0006749|HDFC000231|SBIN213213213"}
      </td>
    </tr>

    <tr>
      <td>
        api\_version
      </td>

      <td>
        The api\_version "6" must be passed from this parameter.
      </td>

      <td>
        6
      </td>
    </tr>
  </tbody>
</Table>
`}</HTMLBlock>

<br />

<Accordion title="Checksum Logic for Hash" icon="fa-code">
The following hash logic must be used for the parameters posted:

> 📘 beneficiarydetail parameter in Hashing:
>
> The **beneficiarydetail** parameter value will be at last or the last value to be appended.
>
> ```plaintext
> key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT
> ```

> 📘 Notes:
>
> * For NEFT/RTGS TPV, merchant should always send both customer account no and customer IFSC Code in Request.
> * For NEFT/RTGS TPV, the flow will work for **txn_s2s_flow = 1** or **txn_s2s_flow =** 4 as is. For **txn_s2s_flow = 1**, the condition is **payus2s** flag needs to be enabled for that merchant
</Accordion>
</Accordion>

<Accordion title="Optional configuration" icon="fa-code">
PayU provides an optional **Back to Merchant** button on the payment challan of a NEFT/RTGS payment. This button enables your customer to go back to the merchant portal once the transaction is done.

_Sample challan of a NEFT/RTGS transaction_

<Image align="center" border={false} width="400px" src="https://files.readme.io/4f959a8-neftrtgs_challan.jpeg" />
</Accordion>

<Accordion title="Sample request" icon="fa-code">
```
curl -X POST "https://test.payu.in/_payment
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d

"key=JP***g&txnid=blMwz0rgz9udtp&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=&productinfo=iPhone&pg=NEFTRTGS&bankcode=EFTAXTPV&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&api_version=6&beneficiarydetail='{"beneficiaryAccountNumber":"002001600674","ifscCode":"KTKB0000046"}&hash="
```
</Accordion>

## Step 3: Check the response from PayU

<Accordion title="Hash validation logic for payment response (Reverse Hashing)" icon="fa-code">
While sending the response, PayU takes the exact same parameters that were sent in the request (in reverse order) to calculate the hash and returns it to you. You must verify the hash and then mark a transaction as a success or failure. This is to make sure the transaction has not tampered within the response.

The order of the parameters is similar to the following code block:

```
sha512(SALT|beneficiarydetail|status||||||udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```
</Accordion>

<Accordion title="Response parameters" icon="fa-code">
The following table describes the parameters in the response from PayU:

| **Param Name**   | **Description**                                                                                                                                                                                                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mihpayid         | It is a unique reference number created for each transaction at PayU's end. You must note this transaction ID as this will be used as a reference for all the future actions on this transaction like Inquiry or Refund.                                                                                                 |
| merchantid       | It is the unique ID of the merchant.                                                                                                                                                                                                                                                                                     |
| txnid            | This parameter would contain the transaction ID value posted by the merchant during the transaction request.                                                                                                                                                                                                             |
| transaction_fee  | The transaction fee for the TPV transaction. For Net Banking, INR 10 is charged by default.                                                                                                                                                                                                                              |
| discount         | The discount amount given by bank on the transaction fee (if any).                                                                                                                                                                                                                                                       |
| amount           | The net amount after discount (if any) is displayed in this parameter. For Net Banking, INR 10 is charged by default.                                                                                                                                                                                                    |
| paymentgatewayid | The payment gateway identifier for the bank sending the response.                                                                                                                                                                                                                                                        |
| pg               | The payment gateway used for the transaction. In case of NEFT/RTGS, it is "NEFTRTGS."                                                                                                                                                                                                                                    |
| status           | This parameter gives the status of the transaction as either success, failed or pending. Possible values: success, failure, pending If the value of the 'status' parameter is 'success', the transaction is successful. If the value of 'status' is 'failure' or 'pending', must be treated as a failed transaction only |
| PG_Type          | The bankcode (as in Merchant Hosted Checkout integration) of the bank is returned in the parameter.                                                                                                                                                                                                                      |
| key              | This parameter contains the merchant key for the merchant's account at PayU. It would be the same as the key used while the transaction request is being posted from the merchant's end to PayU.                                                                                                                         |
| riskactionStr    | This parameter contains risk action (if any) taken on the account holder.                                                                                                                                                                                                                                                |
| addedon          | The transaction timestamp is returned in this parameter.                                                                                                                                                                                                                                                                 |

> 📘 Store **mihpayid** and **txnid** parameter in response:
>
> PayU recommends you to make provisions to store the **mihpayid** and **txnid** parameter values (in the response) in your server as proof that TPV has been completed for a customer.

> 📘 Note on Response:
>
> For security reasons, the sample response or URL is not included here.

> 📘 Payment verification:
>
> PayU recommends you. to verify the transaction details using the **Verification Payment** API. For more information, For API reference, refer to <a href="verify_payment_api" target="_blank">Verify Payment API</a>.
</Accordion>

<br />
