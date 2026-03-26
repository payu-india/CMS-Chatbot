---
title: Web Integration - PayU Hosted
deprecated: false
hidden: false
metadata:
  robots: index
---
## What you're building

A simple server-generated redirect that sends customers from your site/app to the PayU-hosted payment page, then returns them to your success/failure URLs. You pass payment details & customer fields + a server-generated <Glossary>SHA</Glossary>-512 hash for integrity; PayU handles the payment UI and authentication.

<PayU_Labs />

<Callout icon="❗️" theme="error">
  **Important UPI Integration Changes as per NPCI Mandate on UPI Collect Disablement**: If you are using PayU Hosted Checkout within a WebView inside your Android or iOS app, you must handle deeplink URL handling in your app. For implementation details, refer to [WebView for Mobile Apps](doc:webview-for-mobile-apps).
</Callout>

**The PayU Hosted Checkout integration involves the following steps:**

<Cards columns={3}>
  <Card title="1. Start Integration" href="#step-1--start-integration">
    Integrate pre-built checkout solution

    <br />
  </Card>

  <Card title="2. Test Integration" href="#step-2-test-integration">
    Test the integration by making a test transaction

    <br />
  </Card>

  <Card title="3. Go live Checklist" href="#step-3-going-live-your-final-checklist">
    Follow the production checklist to go live
  </Card>
</Cards>

<HTMLBlock>{`
<style>
.Card {
  display: block;
  padding: 1.5rem;
  color: white;
  text-decoration: none;
  border-radius: 0.75rem;
  box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
  border: 5px solid #047857;
  
  /* The gradient background */
  background-image: linear-gradient(to right, #34d399, #059669);
  
  /* A smooth transition for the hover effect */
  transition: all 0.3s ease-in-out;
}

/* This handles the hover effect */
.Card:hover {
  background-image: linear-gradient(to right, #10b981, #047857);
  box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
}

/* Basic styling for the text inside the card */
.Card h3 {
  margin: 0 0 0.5rem 0;
  font-family: sans-serif;
}

.Card p {
  margin: 0;
  font-family: sans-serif;
  font-weight: normal;
  opacity: 0.9;
}
</style>
`}</HTMLBlock>

<Callout icon="📘" theme="info">
  **Pre-requisite**

  * Create an <Anchor label="account with PayU" target="_blank" href="https://onboarding.payu.in/app/account/signup">account with PayU</Anchor>
  * Get your key and salt for test and production environment. For more information, refer to [Access Merchant Key and Salt](doc:generate-merchant-key-and-salt-copy).
  * Keep https success & failure URLs (surl, furl) ready,  reachable from the public internet.
  * Ability to generate
    <Glossary>SHA</Glossary>-512 on the server (not recommended to do it in browser).
</Callout>

## Step 1:  Start Integration

Follow the below steps to complete the integration:

<Callout icon="📘" theme="info">
  **Reference**: For **Try-It** experience on the API Reference with the sample code in 16 language bindings, refer to <Anchor label="Collect Payment API - PayU Hosted Checkout" target="_blank" href="https://docs.payu.in/reference/_payment_payu_hosted_checkout">Collect Payment API - PayU Hosted Checkout</Anchor>.
</Callout>

<PaymentAPIEnvironment />

<Accordion title="Step 1.1: Prepare the request parameters" icon="fa-list-check">
  First, you need to collect all the necessary information for the transaction. Below is the list of parameters where some are mandatory and others are optional.

  <HTMLBlock>{`
                                                                                                                                                                                                                                                                                            <div >
                                                                                                                                                                                                                                                                                              <table>
                                                                                                                                                                                                                                                                                                <thead>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <th style="width: 10%;">Parameter</th>
                                                                                                                                                                                                                                                                                                    <th style="width: 75%; white-space: normal; word-break: break-word;">Type & Description</th>
                                                                                                                                                                                                                                                                                                    <th style="width: 15%;">Example</th>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                </thead>
                                                                                                                                                                                                                                                                                                <tbody>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      key<br>
                                                                                                                                                                                                                                                                                                      <code>mandatory</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> Merchant key provided by PayU during onboarding.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>JPG****.k</td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      txnid<br>
                                                                                                                                                                                                                                                                                                     <code class="inline-block rounded-full bg-red-100 px-2 py-0.5 text-xs font-semibold text-red-800 ring-1 ring-inset ring-red-200">mandatory</code>

                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> The transaction ID is a reference number for a specific order generated by the merchant.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>ypl938459435</td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      amount<br>
                                                                                                                                                                                                                                                                                                      <code>mandatory</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> The payment amount for the transaction.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>10.00</td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      productinfo<br>
                                                                                                                                                                                                                                                                                                      <code>mandatory</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> A brief description of the product.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>iPhone</td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      firstname<br>
                                                                                                                                                                                                                                                                                                      <code>mandatory</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> The first name of the customer.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>Ashish</td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      email<br>
                                                                                                                                                                                                                                                                                                      <code>mandatory</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> The email address of the customer.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                        <a href="mailto:abc@payu.in">abc@payu.in</a>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      phone<br>
                                                                                                                                                                                                                                                                                                      <code>mandatory</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> The phone number of the customer.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td></td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      lastname<br>
                                                                                                                                                                                                                                                                                                      <code>optional</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> The last name of the customer.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>Kumar</td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      surl<br>
                                                                                                                                                                                                                                                                                                      <code>mandatory</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> The success URL, which is the page PayU will redirect to if the transaction is successful.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                        <a href="https://test-payment-middleware.payu.in/simulatorResponse" target="_blank">https://test-payment-middleware.payu.in/simulatorResponse</a>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      furl<br>
                                                                                                                                                                                                                                                                                                      <code>mandatory</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> The failure URL, which is the page PayU will redirect to if the transaction fails.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                        <a href="https://test-payment-middleware.payu.in/simulatorResponse" target="_blank">https://test-payment-middleware.payu.in/simulatorResponse</a>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                  </tr>
        <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      curl<br>
                                                                                                                                                                                                                                                                                                      <code>optional</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> The cancel URL, which is the page PayU will redirect to if the transaction is cancelled.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                        <a href="https://test-payment-middleware.payu.in/simulatorResponse" target="_blank">https://test-payment-middleware.payu.in/simulatorResponse</a>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      hash<br>
                                                                                                                                                                                                                                                                                                      <code>mandatory</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> It is the hash calculated by the merchant. The hash calculation logic is:<br>
                                                                                                                                                                                                                                                                                                      <code>sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)</code><br>
                                                                                                                                                                                                                                                                                                      Reference: For detailed information on hashing, refer to
                                                                                                                                                                                                                                                                                                      <a href="generate-hash-payu-hosted" target="_blank">Generate Hash</a>.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td></td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      address1<br>
                                                                                                                                                                                                                                                                                                      <code>optional</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> The first line of the billing address.<br>
                                                                                                                                                                                                                                                                                                      Fraud Detection: This information is helpful for fraud detection and chargebacks. Please provide the correct information.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai</td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      address2<br>
                                                                                                                                                                                                                                                                                                      <code>optional</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> The second line of the billing address.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>34 Saikripa-Estate, Tilak Nagar</td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      city<br>
                                                                                                                                                                                                                                                                                                      <code>optional</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> The city where your customer resides as part of the billing address.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>Mumbai</td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      state<br>
                                                                                                                                                                                                                                                                                                      <code>optional</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> The state where your customer resides as part of the billing address.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>Maharashtra</td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      country<br>
                                                                                                                                                                                                                                                                                                      <code>optional</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> The country where your customer resides.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>India</td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      zipcode<br>
                                                                                                                                                                                                                                                                                                      <code>optional</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> Billing address zip code is mandatory for the cardless EMI option.<br>
                                                                                                                                                                                                                                                                                                      Character Limit: 20
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>400004</td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      enforced_payment<br>
                                                                                                                                                                                                                                                                                                      <code>optional</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> This parameter is to customize the payment options for each transaction. You can enforce specific payment modes, card schemes, and specific banks under Net Banking using this method.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>creditcard|debitcard</td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      drop_category<br>
                                                                                                                                                                                                                                                                                                      <code>optional</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> This parameter is used if you want to hide one or multiple payment options. For example, if you consider the payment options such as credit card, debit card, and net banking, you can hide the credit card mode of payment.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>CC</td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      udf1<br>
                                                                                                                                                                                                                                                                                                      <code>optional</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>AELPR****E</td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      udf2<br>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td></td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      udf3<br>
                                                                                                                                                                                                                                                                                                      <code>optional</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>02-02-1980</td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      udf4<br>
                                                                                                                                                                                                                                                                                                      <code>optional</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>XYZ Pvt. Ltd.</td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      udf5<br>
                                                                                                                                                                                                                                                                                                      <code>optional</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>098450845</td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      custom_note<br>
                                                                                                                                                                                                                                                                                                      <code>optional</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> This parameter allows you to display a message on the PayU Payment page. This can be useful if you want to provide additional information to your customers, such as an extra charge for a particular product. The message specified in the custom_note parameter will be displayed below the payment options.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>You will be charged an extra amount of Rs 100 on this transaction</td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                  <tr>
                                                                                                                                                                                                                                                                                                    <td>
                                                                                                                                                                                                                                                                                                      note_category<br>
                                                                                                                                                                                                                                                                                                      <code>optional</code>
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td style="white-space: normal; word-break: break-word;">
                                                                                                                                                                                                                                                                                                      <code>String</code> This parameter allows you to specify which payment options the custom_note message will be displayed for. This parameter should contain a comma-separated list of the payment options that you want the custom_note displayed for. Example: "CC, NB" will show the custom_note for Credit Card & Net banking only.
                                                                                                                                                                                                                                                                                                    </td>
                                                                                                                                                                                                                                                                                                    <td>CC, NB</td>
                                                                                                                                                                                                                                                                                                  </tr>
                                                                                                                                                                                                                                                                                                </tbody>
                                                                                                                                                                                                                                                                                              </table>
                                                                                                                                                                                                                                                                                            </div>
  `}</HTMLBlock>

  <Callout icon="📘" theme="info">
    Swap the form action to the production endpoint: [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) when you go live.
  </Callout>
</Accordion>

<Accordion title="Step 1.2: Generate Hash" icon="fa-key">
  Concatenate fields in this exact sequence, then
  <Glossary>SHA</Glossary>-512:

  <HashingRequestParameters />

  * Use empty strings for missing udf\*.
  * Compute on your server and include the lowercase hex digest as hash.

  For more information, refer to  <a href="generate-hash-payu-hosted" target="_blank"> Generate Hash</a>.

  ### Sample Code for Hashing

  <HashingSample />
</Accordion>

<Accordion title="Step 1.3a: POST the html form (server renders)" icon="fa-code">
  <Accordion title="Sample HTML code" icon="fa-code">
    ```html
    <!doctype html>
    <html>
      <body onload="document.forms.payu.submit()">
        <form name="payu" method="post" action="https://test.payu.in/_payment">
          <input type="hidden" name="key" value="JP***g">
          <input type="hidden" name="txnid" value="t6svtqtjRdl4ws">
          <input type="hidden" name="amount" value="499.00">
          <input type="hidden" name="productinfo" value="Pro Plan">
          <input type="hidden" name="firstname" value="Aditi">
          <input type="hidden" name="email" value="test@example.com">
          <input type="hidden" name="phone" value="9999999999">
          <input type="hidden" name="surl" value="https://yourapp.com/payu/success">
          <input type="hidden" name="furl" value="https://yourapp.com/payu/failure">
          <input type="hidden" name="hash" value="sha512(...hash sequence...)">
          <input type="submit" value="Submit" />
        </form>
      </body>
    </html>
    ```

    <Callout icon="📘" theme="info">
      **Note**: Replace the value attributes with your actual data and the generated hash. You can add more parameters to this form as needed. <br />
    </Callout>

    <Callout icon="📘" theme="info">
      **Important**

      When you POST the form to [https://test.payu.in/\_payment](https://test.payu.in/_payment) or [https://secure.payu.in/\_payment](https://secure.payu.in/_payment), we will redirect the user to PayU checkout page.
    </Callout>
  </Accordion>
</Accordion>

<Accordion title="Step 1.3b: Post request in other language bindings" icon="fa-code">
  Use the sample request according the language binding you integrate:

  ```curl
   curl -X POST "https://test.payu.in/_payment" \
   -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d \
   "key=JP***g&txnid=PQI6MqpYrjEefU&amount=10.00 \
   &firstname=PayU User&email=test@gmail.com&phone=9876543210 \
   &productinfo=iPhone&surl= \
   https://apiplayground-response.herokuapp.com/ \
   &furl=https://apiplayground-response.herokuapp.com/ \
   &hash=05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072"
  ```
  ```python
  import requests

  def make_payu_request():
  try:
      url = "https://test.payu.in/_payment"
      
      headers = {
          'accept': 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded'
      }
      
      data = {
          'key': 'JP***g',
          'txnid': 'PQI6MqpYrjEefU',
          'amount': '10.00',
          'firstname': 'PayU User',
          'email': 'test@gmail.com',
          'phone': '9876543210',
          'productinfo': 'iPhone',
          'surl': 'https://apiplayground-response.herokuapp.com/',
          'furl': 'https://apiplayground-response.herokuapp.com/',
          'hash': '05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072'
      }
      
      response = requests.post(url, headers=headers, data=data)
      
      print(f"Status Code: {response.status_code}")
      print(f"Response: {response.text}")
      
      return {
          'status_code': response.status_code,
          'response': response.text
      }
      
  except requests.exceptions.RequestException as e:
      print(f"Error occurred: {e}")
      return None

  # Execute the request
  result = make_payu_request()
  ```
  ```javascript
  async function makePayURequest() {
      try {
          const url = "https://test.payu.in/_payment";
          
          const formData = new URLSearchParams({
              'key': 'JP***g',
              'txnid': 'PQI6MqpYrjEefU',
              'amount': '10.00',
              'firstname': 'PayU User',
              'email': 'test@gmail.com',
              'phone': '9876543210',
              'productinfo': 'iPhone',
              'surl': 'https://apiplayground-response.herokuapp.com/',
              'furl': 'https://apiplayground-response.herokuapp.com/',
              'hash': '05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072'
          });
          
          const response = await fetch(url, {
              method: 'POST',
              headers: {
                  'accept': 'application/json',
                  'Content-Type': 'application/x-www-form-urlencoded'
              },
              body: formData
          });
          
          const responseText = await response.text();
          
          console.log(`Status Code: ${response.status}`);
          console.log(`Response: ${responseText}`);
          
          return {
              status_code: response.status,
              response: responseText
          };
          
      } catch (error) {
          console.error(`Error occurred: ${error.message}`);
          return null;
      }
  }

  // Execute the request
  makePayURequest()
      .then(result => {
          if (result) {
              console.log('Request completed successfully');
          }
      })
      .catch(error => {
          console.error('Request failed:', error);
      });
  ```
  ```java
  import java.io.*;
  import java.net.*;
  import java.nio.charset.StandardCharsets;

  public class PayURequest {
      public static void main(String[] args) {
          makePayURequest();
      }
      
      public static void makePayURequest() {
          try {
              URL url = new URL("https://test.payu.in/_payment");
              HttpURLConnection connection = (HttpURLConnection) url.openConnection();
              
              connection.setRequestMethod("POST");
              connection.setRequestProperty("accept", "application/json");
              connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
              connection.setDoOutput(true);
              
              String formData = "key=" + URLEncoder.encode("JP***g", StandardCharsets.UTF_8) +
                  "&txnid=" + URLEncoder.encode("PQI6MqpYrjEefU", StandardCharsets.UTF_8) +
                  "&amount=" + URLEncoder.encode("10.00", StandardCharsets.UTF_8) +
                  "&firstname=" + URLEncoder.encode("PayU User", StandardCharsets.UTF_8) +
                  "&email=" + URLEncoder.encode("test@gmail.com", StandardCharsets.UTF_8) +
                  "&phone=" + URLEncoder.encode("9876543210", StandardCharsets.UTF_8) +
                  "&productinfo=" + URLEncoder.encode("iPhone", StandardCharsets.UTF_8) +
                  "&surl=" + URLEncoder.encode("https://apiplayground-response.herokuapp.com/", StandardCharsets.UTF_8) +
                  "&furl=" + URLEncoder.encode("https://apiplayground-response.herokuapp.com/", StandardCharsets.UTF_8) +
                  "&hash=" + URLEncoder.encode("05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072", StandardCharsets.UTF_8);
              
              try (OutputStream os = connection.getOutputStream()) {
                  byte[] input = formData.getBytes(StandardCharsets.UTF_8);
                  os.write(input, 0, input.length);
              }
              
              int statusCode = connection.getResponseCode();
              System.out.println("Status Code: " + statusCode);
              
              InputStream responseStream = (statusCode >= 200 && statusCode < 300) 
                  ? connection.getInputStream() 
                  : connection.getErrorStream();
              
              try (BufferedReader br = new BufferedReader(new InputStreamReader(responseStream, StandardCharsets.UTF_8))) {
                  StringBuilder response = new StringBuilder();
                  String responseLine;
                  while ((responseLine = br.readLine()) != null) {
                      response.append(responseLine.trim());
                  }
                  System.out.println("Response: " + response.toString());
              }
              
              connection.disconnect();
              
          } catch (IOException e) {
              System.err.println("Error occurred: " + e.getMessage());
              e.printStackTrace();
          }
      }
  }
  ```
  ```php
  <?php
  function makePayURequest() {
      try {
          $url = "https://test.payu.in/_payment";
          
          $postData = array(
              'key' => 'JP***g',
              'txnid' => 'PQI6MqpYrjEefU',
              'amount' => '10.00',
              'firstname' => 'PayU User',
              'email' => 'test@gmail.com',
              'phone' => '9876543210',
              'productinfo' => 'iPhone',
              'surl' => 'https://apiplayground-response.herokuapp.com/',
              'furl' => 'https://apiplayground-response.herokuapp.com/',
              'hash' => '05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072'
          );
          
          $ch = curl_init();
          
          curl_setopt_array($ch, array(
              CURLOPT_URL => $url,
              CURLOPT_POST => true,
              CURLOPT_POSTFIELDS => http_build_query($postData),
              CURLOPT_HTTPHEADER => array(
                  'accept: application/json',
                  'Content-Type: application/x-www-form-urlencoded'
              ),
              CURLOPT_RETURNTRANSFER => true,
              CURLOPT_TIMEOUT => 30,
              CURLOPT_SSL_VERIFYPEER => true,
              CURLOPT_SSL_VERIFYHOST => 2
          ));
          
          $response = curl_exec($ch);
          $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
          $error = curl_error($ch);
          
          curl_close($ch);
          
          if ($error) {
              echo "cURL Error: " . $error . "
  ";
              return array('status_code' => 0, 'response' => 'Error: ' . $error);
          }
          
          echo "Status Code: " . $httpCode . "
  ";
          echo "Response: " . $response . "
  ";
          
          return array(
              'status_code' => $httpCode,
              'response' => $response
          );
          
      } catch (Exception $e) {
          echo "Error occurred: " . $e->getMessage() . "
  ";
          return null;
      }
  }

  // Execute the request
  $result = makePayURequest();
  ?>
  ```
  ```perl
  #!/usr/bin/perl
  use strict;
  use warnings;
  use LWP::UserAgent;
  use HTTP::Request::Common qw(POST);
  use URI::Escape;

  sub make_payu_request {
      my $ua = LWP::UserAgent->new;
      $ua->timeout(30);
      
      my $url = "https://test.payu.in/_payment";
      
      my %form_data = (
          'key' => 'JP***g',
          'txnid' => 'PQI6MqpYrjEefU',
          'amount' => '10.00',
          'firstname' => 'PayU User',
          'email' => 'test@gmail.com',
          'phone' => '9876543210',
          'productinfo' => 'iPhone',
          'surl' => 'https://apiplayground-response.herokuapp.com/',
          'furl' => 'https://apiplayground-response.herokuapp.com/',
          'hash' => '05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072'
      );
      
      my $request = POST $url, 
          'accept' => 'application/json',
          'Content-Type' => 'application/x-www-form-urlencoded',
          Content => \%form_data;
      
      my $response = $ua->request($request);
      
      if ($response->is_success) {
          print "Status Code: " . $response->code . "
  ";
          print "Response: " . $response->decoded_content . "
  ";
          
          return {
              'status_code' => $response->code,
              'response' => $response->decoded_content
          };
      } else {
          print "Error occurred: " . $response->status_line . "
  ";
          print "Status Code: " . $response->code . "
  ";
          print "Error Response: " . $response->decoded_content . "
  " if $response->decoded_content;
          return undef;
      }
  }

  # Execute the request
  my $result = make_payu_request();
  if ($result) {
      print "Request completed successfully
  ";
  } else {
      print "Request failed
  ";
  }
  ```
  ```csharp
  using System;
  using System.Collections.Generic;
  using System.Net.Http;
  using System.Threading.Tasks;

  class Program
  {
      static async Task Main(string[] args)
      {
          await MakePayURequest();
      }
      
      static async Task MakePayURequest()
      {
          try
          {
              using (var client = new HttpClient())
              {
                  var url = "https://test.payu.in/_payment";
                  
                  client.DefaultRequestHeaders.Add("accept", "application/json");
                  
                  var formParams = new List<KeyValuePair<string, string>>
                  {
                      new KeyValuePair<string, string>("key", "JP***g"),
                      new KeyValuePair<string, string>("txnid", "PQI6MqpYrjEefU"),
                      new KeyValuePair<string, string>("amount", "10.00"),
                      new KeyValuePair<string, string>("firstname", "PayU User"),
                      new KeyValuePair<string, string>("email", "test@gmail.com"),
                      new KeyValuePair<string, string>("phone", "9876543210"),
                      new KeyValuePair<string, string>("productinfo", "iPhone"),
                      new KeyValuePair<string, string>("surl", "https://apiplayground-response.herokuapp.com/"),
                      new KeyValuePair<string, string>("furl", "https://apiplayground-response.herokuapp.com/"),
                      new KeyValuePair<string, string>("hash", "05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072")
                  };
                  
                  var formContent = new FormUrlEncodedContent(formParams);
                  
                  var response = await client.PostAsync(url, formContent);
                  var responseContent = await response.Content.ReadAsStringAsync();
                  
                  Console.WriteLine($"Status Code: {(int)response.StatusCode}");
                  Console.WriteLine($"Response: {responseContent}");
              }
          }
          catch (HttpRequestException e)
          {
              Console.WriteLine($"Error occurred: {e.Message}");
          }
      }
  }
  ```
</Accordion>

<Accordion title="Step 1.4: Response handling & hash verification" icon="fa-shield-check">
  **Response Handling:**

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

  **Step 1.4.1: Response verification using reverse hashing**

  Verify the response received above by recomputing SHA-512 using the reverse sequence:

  ```json
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  * Compare the computed digest to hash from the POST payload (**case-sensitive**).
  * Trust the result only if the hash matches. Then update your order state.
</Accordion>

<Accordion title="Step 1.6: Verify the payment" icon="fa-magnifying-glass">
  <Verify_Payment_Tabs />
</Accordion>

<br />

## Step 2: Test Integration

Before going live, it's crucial to test your integration thoroughly in the PayU test environment. Follow these steps to ensure your setup is correct and to simulate different transaction scenarios.

<Accordion title="Step 2.1: Pre-Payment Validation" icon="fa-check-circle">
  Before initiating a transaction, ensure your server-side implementation is correct.

  1. **Verify API Credentials:** Double-check that you are using the correct key and salt for the test environment.
  2. **Validate Hash Calculation:** The most common point of failure is an incorrect hash.
     1. Temporarily print the string that you are passing into the hash function on your server.
     2. Ensure the order of the parameters (key|txnid|amount|productinfo|firstname|email...|salt) exactly matches the format specified in the documentation.
     3. Verify that there are no empty or null values for mandatory parameters in the hash string.
     4. If you encounter a "Checksum failed" error upon redirection, this is the first thing to debug.
</Accordion>

<Accordion title="Step 2.2: Simulate a Successful Transaction (The Happy Path)" icon="fa-thumbs-up">
  This test ensures that a successful payment is correctly processed and recorded.

  1. **Initiate Payment:** On your website or app, add items to the cart and proceed to payment. This should trigger your code to send the transaction details to PayU and redirect the user to the PayU payment page.
  2. **Error Check:** If you are not redirected and see an error message on your own site, check your server-side logs. If you are redirected to a PayU error page, refer to the Error Handling section to diagnose the issue.
  3. **Verify Payment Page:** Once on the PayU page, confirm the following:
     1. The transaction amount and product details are displayed correctly.
     2. All the payment methods (Credit/Debit Card, UPI, Net Banking, etc.) that should be active on your account are visible. If a payment method is missing, please contact your Key Account Manager (KAM) or PayU Support.
  4. **Test a Card Transaction**:
     1. Select Credit Card as the payment method.
     2. Use the following test card details:
        1. Card Number: 5123456789012346
        2. Expiry Date: Any valid future date (e.g., 12/2030)
        3. CVV: 123
        4. Name on Card: Test Name
     3. Click Pay Now. You will be redirected to a dummy bank page to simulate 3D Secure authentication.
     4. Enter the test OTP 123456 and click Submit.
  5. **Test a UPI Transaction:**
     1. Select UPI as the payment method.
     2. Enter a test UPI ID: anything\@payu or 9999999999\@payu
     3. Click Verify and then Pay Now. This will simulate a successful UPI transaction.

  For more test credentials, refer to the [Test Cards, UPI ID and Wallets guide](https://docs.payu.in/docs/test-cards-upi-id-and-wallets).
</Accordion>

<Accordion title="Step 2.3: Simulate a Failed Transaction" icon="fa-times-circle">
  It's equally important to test how your system handles failed payments.

  1. Initiate a New Payment as you did in Step 2.
  2. Test a Failing Card Transaction:
     1. Select Credit Card as the payment method.
     2. Use a test card designed to fail, for example:
        1. Card Number: 5123456789012340 (Payment failed by user)
     3. Complete the payment flow. The transaction should fail.
</Accordion>

<Accordion title="Step 2.4: Post-Transaction Verification" icon="fa-magnifying-glass">
  After both the successful and failed transactions, you must verify the final status at multiple points.

  1. **Check the Return URL (surl / furl):**
     1. After a successful payment, PayU will redirect the user to the Success URL (surl) you provided. Verify that your application handles this redirect correctly and displays an appropriate success message to the user.
     2. After a failed payment, PayU will redirect the user to the Failure URL (furl). Verify that your application displays a clear failure message and provides the user with options to retry.
  2. **Verify the Server-to-Server (S2S) Webhook:**
     1. This is the most reliable way to confirm transaction status.
     2. Check your server logs to ensure that you have received the S2S POST request from PayU for the transaction.
     3. Validate the hash in the webhook response to ensure the data is authentic.
     4. Update the transaction status in your database based on the status received in the S2S webhook, not based on the browser redirect (surl/furl).
  3. **Cross-Verify in the PayU Dashboard:**
     1. Log in to your PayU test dashboard.
     2. Navigate to the "Transactions" section.
     3. Verify that both the successful and failed transactions are logged correctly with the corresponding status (success, failure). Check that details like txnid and amount match your records.
</Accordion>

## Step 3: Going Live: Your Final Checklist

You've successfully tested your integration. Now, follow these critical steps to switch to the live environment and start accepting real payments from your customers.

<Accordion title="Step 3.1. Update to Production Credentials" icon="fa-key">
  First, you must switch your integration from using test credentials to production credentials.

  ***

  ### Generate Live Keys\*\*

  * Log in to your **[PayU Dashboard](https://onboarding.payu.in/app/account/signin)**.
  * Use the toggle at the top to switch from **Test Mode** to **Live Mode**.
  * Navigate to **Developer Tools** → **API Keys** from the sidebar.
  * Copy the **Live Merchant Key** and **Live Salt**.

  ***

  ### Update Your Code\*\*

  * In your integration code, replace the test `key` and `salt` with your new live credentials.

  ***

  ### Update the Endpoint URLs\*\*

  * Ensure all API requests are now being sent to the correct production endpoints:
    * **For`_payment` API:** `https://secure.payu.in/_payment`
    * **For Verify Payments API:** `https://info.payu.in/merchant/postservice.php?form=2`
</Accordion>

<Accordion title="Step 3.2. Final Integration Verification" icon="fa-clipboard-check">
  Before you announce that you're live, run through this checklist to ensure everything is configured correctly.

  * **✅ Conduct a Live Transaction:** Make a small, real transaction with a genuine credit card or UPI ID. This is the best way to confirm that your production credentials are correct and that the end-to-end flow is working.

  * **✅ Verify the Server-to-Server (S2S) Webhook:** This is the most crucial step for confirming transaction status reliably.
    * After your live test transaction, check your server logs to confirm that you received the webhook from PayU.
    * Ensure your system correctly processes this webhook and updates the order status in your database.
    * **Important:** Your system should rely on this S2S webhook as the primary source of truth for a transaction's final status, not the browser redirect. For more details, refer to **Webhooks**.

  * **✅ Validate the Response Hash:**
    * Confirm that your code correctly validates the hash for the response sent to your return URL (`surl`/`furl`) and for the S2S webhook. This security measure prevents tampering and confirms the response is genuinely from PayU. For more information, refer to **Hashing Request and Response**.

  * **✅ Check Success and Failure Pages (`surl` / `furl`):**
    * Ensure that after a successful payment, your customer is redirected to your success page and sees a clear confirmation message.
    * Simulate a failed live payment (if possible, with a card that has insufficient funds) to ensure the customer is redirected to your failure page and given instructions to retry.

  * **✅ Implement a Reconciliation Plan:**
    * In case of any discrepancy (e.g., a webhook is missed), use the **Verify Payment API** to programmatically fetch the status of a transaction from PayU and reconcile your records.
</Accordion>

<br />
