---
title: PayU Hosted Checkout Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: >-
    PayU Hosted Checkout integration for International Payments or Dynamic
    Currency Conversion
  description: >-
    Learn how to integrate PayU’s Hosted Checkout feature with Dynamic Currency
    Conversion (DCC) to offer your customers a seamless and secure payment
    experience in their preferred currency. Follow the step-by-step procedure to
    set up your integration and start accepting international payments with
    PayU.
  keywords:
    - Dynamic Currency Conversion with PayU Hosted Checkout
    - DCC with Non-Seamless Integration
    - ' Currency Conversion with PayU Hosted Checkout'
    - Non-Seamless Integration for Currency Conversion
    - >-
      Multi-Currency Payment Integration with PayU Hosted Checkout.International
      Payments with PayU Hosted Integration
    - Foreign Currency Payment with PayU Hosted Integration
  robots: index
next:
  description: ''
---
The following diagram depicts the steps involved in the end-to-end integration process of International payments.

<Callout icon="📘" theme="info">
  **Notes**:

  * You need to contact your PayU Key Account Manager to enable international payments.
  * For the list of supported currencies, <a href="https://docs.payu.in/docs/supported-currencies-for-international-payments/" target="_blank">Supported Currencies for International Payments</a>.
</Callout>

<Callout icon="👍" theme="okay">
  **Before you begin**: Register for a account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Callout>

<Image border={false} src="https://devguide.payu.in/wordpress/wp-content/uploads/2021/07/International-Payments-E2E-Payment-Exp-1024x518.png" />

***

**Steps to integrate**

<Cards columns={3}>
  <Card title="1. Make the Transaction Request to PayU" href="https://docs.payu.in/docs/payu-hosted-checkout-integration-with-offers#step-1-make-the-transaction-request-to-payu">
    Send the transaction request to PayU and handle the initial response from the payment gateway

    <br />
  </Card>

  <Card title="2. Check the Response from PayU" href="https://docs.payu.in/docs/payu-hosted-checkout-integration-with-offers#step-2-check-the-response-from-payu">
    Process and validate the detailed response received from PayU after transaction submission

    <br />
  </Card>

  <Card title="3. Verify the Payment" href="https://docs.payu.in/docs/payu-hosted-checkout-integration-with-offers#step-3-verify-the-payment">
    Confirm the payment status and ensure successful transaction completion
  </Card>
</Cards>

## Step 1: Make the transaction request to PayU 

With the **POST REQUEST**, the customer will be redirected to the PayU's payment page. The customer now selects the credit card payment option on PayU's page and clicks the Pay Now button. PayU redirects the customer to the chosen payment method. The customer enters an international credit card number, and PayU displays the conversion. For the description of the request and response parameters, refer to Response Parameters section of [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout).

PayU marks the transaction status based on the response received from the bank. PayU provides the final transaction response string to the merchant through a POST RESPONSE. The parameters in this response are covered in the subsequent sections.

<Callout icon="📘" theme="info">
  **Reference**: For a list of card details for testing dynamic currency conversion, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).
</Callout>

> 📘 Notes:
>
> * For DCC eligible transactions, no changes are required in the existing integration of Query transactions or Refund transactions. In case of refunds, the merchant can initiate refunds in INR (original amount and currency) only. PayU will internally convert the same into the final amount and currency charged to the consumer using the FX rate, which was applied on the date of sale.
> * There is no change required in handling the response from PayU as the response parameters are similar to the regular transaction
> * It is recommended to collect the customer's e-mail address, phone, address, city, state, and country and then post those details along with the payment request with PayU. This will help in checking the risk of the transaction based on these data.

<Accordion title="Request parameters" icon="fa-code">
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
                <td>key <code>mandatory</code></td>
                <td><code>String</code> Merchant key provided by PayU during onboarding.</td>
                <td>JP***g</td>
              </tr>
              <tr>
                <td>txnid <code>mandatory</code></td>
                <td><code>String</code> The transaction ID is a reference number for a specific order that is generated by the merchant.</td>
                <td>PQI6MqpYrjEefU</td>
              </tr>
              <tr>
                <td>amount <code>mandatory</code></td>
                <td><code>String</code> The payment amount for the transaction.</td>
                <td>10.00</td>
              </tr>
              <tr>
                <td>productinfo <code>mandatory</code></td>
                <td><code>String</code> A brief description of the product.</td>
                <td>iPhone</td>
              </tr>
              <tr>
                <td>firstname <code>mandatory</code></td>
                <td><code>String</code> The first name of the customer.</td>
                <td>PayU User</td>
              </tr>
              <tr>
                <td>email <code>mandatory</code></td>
                <td><code>String</code> The email address of the customer.</td>
                <td>test@gmail.com</td>
              </tr>
              <tr>
                <td>phone <code>mandatory</code></td>
                <td><code>String</code> The phone number of the customer.</td>
                <td>9876543210</td>
              </tr>9
              <tr>
                <td>surl <code>mandatory</code></td>
                <td><code>String</code> The success URL, which is the page PayU will redirect to if the transaction is successful.</td>
                <td>https://apiplayground-response.herokuapp.com/</td>
              </tr>
              <tr>
                <td>furl <code>mandatory</code></td>
                <td><code>String</code> The failure URL, which is the page PayU will redirect to if the transaction is failed.</td>
                <td>https://apiplayground-response.herokuapp.com</td>
              </tr>
              <tr>
                <td>hash <code>mandatory</code></td>
                <td><code>String</code> It is the hash calculated by the merchant. The hash calculation logic is:<br><code>sha512(key|txnid|amount|productinfo|<br/>firstname|email|udf1|udf2|udf3|<br/>udf4|udf5||||||SALT)</code></td>
                <td>05a397501918ec5c36ae52<br/>daa3b3e49b43e986b86940e10<br/>9d060076e467c3ea7536617df742<br/>0e0e6863dced8c5b45f9ff<br/>f15c13bdf0335512c05f0210b31b072</td>
              </tr>
              <tr>
                <td>address1 <code>optional</code></td>
                <td><code>String</code> The first line of the billing address.<br><strong>For Fraud Detection</strong>: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.</td>
                <td>123 Main Street</td>
              </tr>
              <tr>
                <td>address2 <code>optional</code></td>
                <td><code>String</code> The second line of the billing address.</td>
                <td>Apt 4B</td>
              </tr>
              <tr>
                <td>city <code>optional</code></td>
                <td><code>String</code> The city where your customer resides as part of the billing address.</td>
                <td>New Delhi</td>
              </tr>
              <tr>
                <td>state <code>optional</code></td>
                <td><code>String</code> The state where your customer resides as part of the billing address.</td>
                <td>Delhi</td>
              </tr>
              <tr>
                <td>country <code>optional</code></td>
                <td><code>String</code> The country where your customer resides.</td>
                <td>India</td>
              </tr>
              <tr>
                <td>zipcode <code>optional</code></td>
                <td><code>String</code> Billing address zip code is mandatory for the cardless EMI option.<br><code>Character Limit</code>: 20</td>
                <td>110001</td>
              </tr>
              <tr>
                <td>udf1 <code>optional</code></td>
                <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.</td>
                <td>Custom Data 1</td>
              </tr>
              <tr>
                <td>udf2 <code>optional</code></td>
                <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.</td>
                <td>Custom Data 2</td>
              </tr>
              <tr>
                <td>udf3 <code>optional</code></td>
                <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td>
                <td>Custom Data 3</td>
              </tr>
              <tr>
                <td>udf4 <code>optional</code></td>
                <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td>
                <td>Custom Data 4</td>
              </tr>
              <tr>
                <td>udf5 <code>optional</code></td>
                <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td>
                <td>Custom Data 5</td>
              </tr>
            </tbody>
          </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```
  curl -X POST "https://test.payu.in/_payment"
  -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
  "key=JP***g&txnid=PQI6MqpYrjEefU&amount=10.00
  &firstname=PayU User&email=test@gmail.com&phone=9876543210
  &productinfo=iPhone&surl=
  https://apiplayground-response.herokuapp.com/
  &furl=https://apiplayground-response.herokuapp.com
  &hash=05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072"
  ```
</Accordion>

## Step 2: Check the response from PayU

<Accordion title="Sample response" icon="fa-code">
  The formatted response is similar to the following:

  ```
  Array
  (
      [mihpayid] => 403993715527769337
      [mode] => CC
      [status] => success
      [unmappedstatus] => captured
      [key] => smsplus
      [txnid] => 86e836b84be8dc6f7894
      [amount] => 10.00
      [cardCategory] => domestic
      [discount] => 0.00
      [net_amount_debit] => 10
      [addedon] => 2022-11-25 11:30:36
      [productinfo] => Product Info
      [firstname] => Payu-Admin
      [lastname] => 
      [address1] => 
      [address2] => 
      [city] => 
      [state] => 
      [country] => 
      [zipcode] => 
      [email] => test@example.com
      [phone] => 1234567890
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
      [hash] => df565fdcbdd0172c42bf1ba1429c3f48e7215933574f932f37bb133ec4ac89d93535a1bf7674ec4514ffd238ec36e39524142b8d2415554ac7ced49707ea6940
      [field1] => 
      [field2] => 
      [field3] => 
      [field4] => 
      [field5] => 
      [field6] => 
      [field7] => 
      [field8] => 
      [field9] => Transaction Completed Successfully
      [payment_source] => payu
      [PG_TYPE] => CC-PG
      [bank_ref_num] => e0e4a0ca-e356-412a-8f3a-9d69cede5a04
      [bankcode] => MASTCC
      [error] => E000
      [error_Message] => No Error
      [success_at] => 2022-11-25 11:33:41
      [cardnum] => XXXXXXXXXXXX1287
      [cardhash] => This field is no longer supported in postback params.
  )
  ```
</Accordion>

## Step 3: Verify the payment

<Verify_Payment_Tabs />
