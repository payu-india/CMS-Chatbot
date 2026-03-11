---
title: PayU Hosted Integration
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  title: PayU Hosted Subscription Integration with Cross-Border Payments
  description: >-
    PayU Hosted subscription integration for Cross-Border Payments. Recurring
    payments with hosted checkout.
  keywords:
    - Cross-Border Payments PayU hosted subscription
    - PayU hosted subscription integration for CB
    - recurring payment hosted checkout
    - PayU Hosted Subscription Integration with Cross-Border Payments
  robots: index
---
This section describes steps to integrate Subscriptions using the PayU Hosted Checkout integration.

<Callout icon="📘" theme="info">
  **Note**: The PayU Hosted or non-seamless integration for Subscriptions involves only the **Collect Payment** API (**_payment**).
</Callout>
Based on the content about PayU Hosted Checkout integration for Subscriptions, I'll create organized cards for you:

<Cards columns={3}>
  <Card title="1. Post the Consent Transaction" href="https://docs.payu.in/docs/integrate-with-hosted-checkout-for-subscriptions#step-1-post-the-consent-transaction">
    Send a POST request to PayU with required parameters including key, txnid, amount, productinfo, firstname, email, phone, surl, furl, hash, and subscription details (si_details) formatted as JSON

    <br />
  </Card>

  <Card title="2. Check the Response from PayU" href="https://docs.payu.in/docs/integrate-with-hosted-checkout-for-subscriptions#step-2-check-the-response-from-payu">
    Capture and validate the response from PayU containing mihpayid, transaction ID, status, amount, payment mode, email, and other transaction details

    <br />
  </Card>

  <Card title="3. Verify the Payment" href="https://docs.payu.in/docs/integrate-with-hosted-checkout-for-subscriptions#step-3-verify-the-payment">
    Verify the payment transaction from PayU to ensure the subscription payment has been successfully processed and confirmed
  </Card>

  <br />
</Cards>

**Additional Resources** 📚

• **[Manage Recurring Payment for Cards](https://docs.payu.in/docs/manage-recurring-payment-for-cards)** - Handle card-based recurring transactions
• **[Manage UPI Recurring Transaction](https://docs.payu.in/reference/api-commands-to-manage-upi-recurring-transaction)** - UPI recurring payment management
• **[SI Parameter JSON Details](https://docs.payu.in/reference/si-parameter-json-details)** - Detailed subscription parameter specifications
• **[RBI Guidelines](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668&Mode=0)** - Regulatory compliance information

**Environment URLs** 🌐
- **Production**: `https://secure.payu.in/_payment`
- **Test**: `https://test.payu.in/_payment`

This integration guide covers the complete flow for implementing PayU's hosted checkout solution specifically for subscription-based payments, ensuring proper consent handling and transaction verification.

## Step 1: Post the Consent Transaction

HTTP Method: **POST**

**Environment**

|                            |                                                                    |
| :------------------------- | :----------------------------------------------------------------- |
| **Production Environment** | [https://secure.payu.in/_payment](https://secure.payu.in/_payment) |
| **Test Environment**       | [https://test.payu.in/_payment](https://test.payu.in/_payment)     |

<Accordion title="Request parameters" icon="fa-table">
  In the merchant-initiated POST REQUEST, Hash is a mandatory parameter. It is critical to calculate the hash correctly and post it to PayU in the request.

  <HTMLBlock>{`
      <style>
      /* Target only the second column in the table */
      .markdown-body table td:nth-child(2) {
        word-break: break-word !important;
      }

      /* Keep the first column from breaking unnecessarily */
      .markdown-body table td:nth-child(1) {
        word-break: normal;
        white-space: nowrap;
      }
      </style>
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
              key <br/>
              <code>mandatory</code>
            </td>

            <td style={{ textAlign: "left" }}>
              <code>varchar</code> This parameter is the unique Merchant Key provided by PayU for your merchant account.
            </td>

            <td style={{ textAlign: "left" }}>
              Your Test Key
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              txnid <br/>
              <code>mandatory</code>
            </td>

            <td style={{ textAlign: "left" }}>
              <code>varchar</code> This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction. <code>Character limit</code>: 25 <br/><strong>Note</strong>: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID.'
            </td>

            <td style={{ textAlign: "left" }}>
              fd3e847h2
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              amount <br/>
              <code>mandatory</code>
            </td>

            <td style={{ textAlign: "left" }}>
              <code>float</code> This parameter should contain the payment amount of the particular transaction.
              <br/><strong>Note</strong>: Type-cast the amount to float type Depending upon the merchant use case, this value will vary. <br/>- It can be either 0 INR (for Net Banking) or min 1 INR (for Cards & UPI) in penny transaction use case. <br/>- In the case of first instalment use cases, this amount can be equal to initiate setup amount, but this use case will be supported only against selected Net Banking (ICICI and HDFC), all Credit / Debit Cards, and UPI
            </td>

            <td style={{ textAlign: "left" }}>
              1000
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              productinfo <br/>
              <code>mandatory</code>
            </td>

            <td style={{ textAlign: "left" }}>
              <code>varchar</code> This parameter should contain a brief product description. It should be a string describing the product. <code>Character limit</code>: 100
            </td>

            <td style={{ textAlign: "left" }}>
              Time Magazine Subscription
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              firstname <br/>
              <code>mandatory</code>
            </td>

            <td style={{ textAlign: "left" }}>
              <code>varchar</code> Must contain the first name of the customer. <code>Character limit</code>: 60
            </td>

            <td style={{ textAlign: "left" }}>
              Ashish
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              email <br/>
              <code>mandatory</code>
            </td>

            <td style={{ textAlign: "left" }}>
              <code>varchar</code> Must contain the email of the customer. This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information. Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions. <code>Character limit</code>: 50
            </td>

            <td style={{ textAlign: "left" }}>
              <a href="mailto:Ashish@test.com">Ashish@test.com</a>
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              phone <br/>
              <code>mandatory</code>
            </td>

            <td style={{ textAlign: "left" }}>
              <code>varchar</code> Must contain the phone number of the customer. This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions. <code>Character limit</code>: 50
            </td>

            <td style={{ textAlign: "left" }}>
              9843176540
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              surl <br/>
              <code>mandatory</code>
            </td>

            <td style={{ textAlign: "left" }}>
              surL is the acronym for Success URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is successful.
            </td>

            <td style={{ textAlign: "left" }}>

            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              furl <br/>
              <code>mandatory</code>
            </td>

            <td style={{ textAlign: "left" }}>
              furl is the acronym for for Failure URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is failed.
            </td>

            <td style={{ textAlign: "left" }}>

            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              api_version <br/>
              <code>mandatory</code>
            </td>

            <td style={{ textAlign: "left" }}>
              This parameter must always needs to be passed as 7.
            </td>

            <td style={{ textAlign: "left" }}>
              7
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              si <br/>
              <code>mandatory</code>
            </td>

            <td style={{ textAlign: "left" }}>
              This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.
              <br/><strong>Notes</strong>: You can modify or cancel existing recurring payment registration as described in the following sections: <br/>- <a href="http://docs.payu.in/docs/manage-recurring-payment-for-cards">Manage Recurring Payment for Cards</a> <br/>- <a href="http://docs.payu.in/reference/api-commands-to-manage-upi-recurring-transaction">Manage UPI Recurring Transaction</a>
            </td>

            <td style={{ textAlign: "left" }}>
              1
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              free_trial <br/>
              <code>optional</code>
            </td>

            <td style={{ textAlign: "left" }}>
              This is mandatory only if the merchant wants to support free trial use cases.
              In this case, PayU adjusts the transaction amount as INR 2.00 for cards and UPI and INR 0.00 for Net Banking irrespective of what amount is passed against the amount field in the request.
            </td>

            <td style={{ textAlign: "left" }}>

            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              si_details <br/>
              <code>mandatory</code>
            </td>

            <td style={{ textAlign: "left" }}>
              This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.
              <br/><strong>Note</strong>: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers ( for more details refer <a href="https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668&Mode=0">https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668&Mode=0</a> ) This is a JSON object and it includes a set of fields. For more information, refer to <a href="https://docs.payu.in/reference/si-parameter-json-details/">SI Parameter JSON Details</a>
            </td>

            <td style={{ textAlign: "left" }}>
              {"billingAmount": "100.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"}
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              hash <br/>
              <code>mandatory</code>
            </td>

            <td style={{ textAlign: "left" }}>
              Hash is a crucial parameter used to ensure that any date is not tampered while redirecting customer from the merchant website to PayU's payment interface while registration transactions. It is SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si_details by merchant salt. In the case of registration transaction. The formula is used to calculate this hash is similar to the following:<br/>
              <code>HASH = SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|SALT)</code>
            </td>

            <td style={{ textAlign: "left" }}>
              txnid
            </td>
          </tr>
        </tbody>
      </Table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X \
   POST "https://test.payu.in/_payment" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=fM3O2HnkpJ8XEC&amount=100.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cc#bankcode=AIRPENCC&si=1&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&si_details={\"billingAmount\": \"100.00\",\"billingCurrency\": \"INR\",\"billingCycle\": \"MONTHLY\",\"billingInterval\": 1,\"paymentStartDate\": \"2022-09-01\",\"paymentEndDate\": \"2022-12-01\"}&hash=2ad878f64de47c7c1149ff554cd00ee44555a8512a1d2cff9690d6ea3c9d9de0bc44b0e77c61dd60a3c64ef970612a9b71761559aa202d2a278d29dc87b998c5"
  ```

  Characters allowed for parameters

  For parameters address1, address2, city, state, country, product info, email, and phone following characters are allowed:

  * Characters: A to Z, a to z, 0 to 9
  * – (Minus)
  * \_ (Underscore)
  * @ ()
  * / (Slash)
  * (Space)
  * . (Dot)
</Accordion>

## Step 2: Check the response from PayU

The response URL returned from PayU is in the form URL format (application/x-www-form-urlencoded).

<Accordion title="Parsed response" icon="fa-code">
  ```
  Array
  (
      [mihpayid] => 403993715525331373
      [mode] => ENACH
      [status] => success
      [unmappedstatus] => captured
      [key] => JPM7Fg
      [txnid] => oRWSUMU4XSQBZn
      [amount] => 100.00
      [discount] => 0.00
      [net_amount_debit] => 0
      [addedon] => 2022-02-03 19:06:55
      [productinfo] => iPhone
      [firstname] => Ashish
      [lastname] => 
      [address1] => 
      [address2] => 
      [city] => 
      [state] => 
      [country] => 
      [zipcode] => 
      [email] => test@gmail.com
      [phone] => 9876543210
      [udf1] => 
      [udf2] => 
      [udf3] => 
      [udf4] => 
      [udf5] => 
      [udf6] => 
      [udf7] => 
      [udf8] => 
      [udf9] => 
      [udf10] => 
      [hash] => f3f8e4088231b190930fc4b87d3f39397d1a1d02622ef4683a983244e1cd5158f39adbb67c3d87dcb4da25ae4a941ebbf55918e4575fa1c39677a774d02c0d2d
      [field1] => ENACH285259747472911093
      [field2] => 337026657857179355
      [field3] => 
      [field4] => 
      [field5] => 
      [field6] => 
      [field7] => 
      [field8] => 
      [field9] => Mandate successfully scheduled at bank end: Your payment is scheduled successfully
      [payment_source] => sist
      [PG_TYPE] => ENACH-PG
      [bank_ref_num] => 450699821592111537
      [bankcode] => ICICENCC
      [error] => E000
      [error_Message] => No Error
  )
  ```
</Accordion>

## Step 3: Verify the Payment

<Verify_Payment_Tabs />

<br />