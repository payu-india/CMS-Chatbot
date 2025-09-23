---
title: Integration Steps (COPY)
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  title: PayU Hosted Checkout Integration
  keywords:
    - PayU Hosted Checkout Integration
    - Integrate PayU Hosted Checkout
    - Steps for PayU Hosted Checkout Integration
    - PayU Hosted Checkout Integration Steps
  robots: index
---
# What you're building

A simple server-generated redirect that sends customers from your site/app to the PayU-hosted payment page, then returns them to your success/failure URLs. You pass order & customer fields + a server-generated SHA-512 hash for integrity; PayU handles the payment UI and authentication.

The PayU Hosted Checkout integration involves the following steps:

<Cards columns={3}>
  <Card title="1. Start Integration" href="https://docs.payu.in/docs/integration-steps-copy#step-1--start-integration" target="_blank" className="bg-gradient-to-r from-emerald-400 to-emerald-600 hover:from-emerald-500 hover:to-emerald-700 text-white shadow-lg rounded-xl border-5">
    Integrate pre-built checkout solution
  </Card>

  <Card title="2. Test Integration" href="https://docs.payu.in/docs/integration-steps-copy#step-2-test-integration" className="bg-gradient-to-r from-amber-400 to-amber-600 hover:from-amber-500 hover:to-amber-700 text-white shadow-lg rounded-xl border-5">
    Test the integration by making a test transaction
  </Card>

  <Card title="3. Go live Checklist" href="https://docs.payu.in/docs/integration-steps-copy#step-3-going-live-your-final-checklist" className="bg-gradient-to-r from-purple-400 to-purple-600 hover:from-purple-500 hover:to-purple-700 text-white shadow-lg rounded-xl border-5">
    Follow the production checklist to go live
  </Card>
</Cards>

<Callout icon="📘" theme="info">
  **Pre-requisite**

  * Create an <Anchor label="account with PayU" target="_blank" href="https://onboarding.payu.in/app/account/signup">account with PayU</Anchor>
  * Get your key and salt for test and production environment. <Anchor label="Click here to access detail guide on accessing your key and salt " target="_blank" href="https://docs.payu.in/docs/generate-test-merchant-key-and-salt">Click here to access detail guide on accessing your key and salt </Anchor>
  * Keep https success & failure URLs (surl, furl) ready,  reachable from the public internet.
  * Ability to generate SHA-512 on the server (not recommended to do it in browser).
</Callout>

<Accordion title="Environment" icon="fa-globe">
  |                        |                                                                     |
  | :--------------------- | :------------------------------------------------------------------ |
  | Test Environment       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
  | Production Environment | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |
</Accordion>

## Step 1:  Start Integration

Follow the below steps to complete the integration:

\<Accordion title="Step 1.1: Prepare the request parameters" icon="fa-list-check">
&#x20; First, you need to collect all the necessary information for the transaction. Below is the list of parameters where some are mandatory and others are optional.

&#x20; \<HTMLBlock>\{\`
&#x20;                                           \<div >
&#x20;                                             \<table>
&#x20;                                               \<thead>
&#x20;                                                 \<tr>
&#x20;                                                   \<th style="width: 10%;">Parameter\</th>
&#x20;                                                   \<th style="width: 75%; white-space: normal; word-break: break-word;">Type & Description\</th>
&#x20;                                                   \<th style="width: 15%;">Example\</th>
&#x20;                                                 \</tr>
&#x20;                                               \</thead>
&#x20;                                               \<tbody>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     key\<br>
&#x20;                                                     \<code>mandatory\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> Merchant key provided by PayU during onboarding.
&#x20;                                                   \</td>
&#x20;                                                   \<td>JPG\*\*\*\*.k\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     txnid\<br>
&#x20;                                                    \<code class="inline-block rounded-full bg-red-100 px-2 py-0.5 text-xs font-semibold text-red-800 ring-1 ring-inset ring-red-200">mandatory\</code>

&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> The transaction ID is a reference number for a specific order generated by the merchant.
&#x20;                                                   \</td>
&#x20;                                                   \<td>ypl938459435\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     amount\<br>
&#x20;                                                     \<code>mandatory\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> The payment amount for the transaction.
&#x20;                                                   \</td>
&#x20;                                                   \<td>10.00\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     productinfo\<br>
&#x20;                                                     \<code>mandatory\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> A brief description of the product.
&#x20;                                                   \</td>
&#x20;                                                   \<td>iPhone\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     firstname\<br>
&#x20;                                                     \<code>mandatory\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> The first name of the customer.
&#x20;                                                   \</td>
&#x20;                                                   \<td>Ashish\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     email\<br>
&#x20;                                                     \<code>mandatory\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> The email address of the customer.
&#x20;                                                   \</td>
&#x20;                                                   \<td>
&#x20;                                                       \<a href="mailto:abc\@payu.in">abc\@payu.in\</a>
&#x20;                                                   \</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     phone\<br>
&#x20;                                                     \<code>mandatory\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> The phone number of the customer.
&#x20;                                                   \</td>
&#x20;                                                   \<td>\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     lastname\<br>
&#x20;                                                     \<code>optional\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> The last name of the customer.
&#x20;                                                   \</td>
&#x20;                                                   \<td>Kumar\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     surl\<br>
&#x20;                                                     \<code>mandatory\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> The success URL, which is the page PayU will redirect to if the transaction is successful.
&#x20;                                                   \</td>
&#x20;                                                   \<td>
&#x20;                                                       \<a href="https\://test-payment-middleware.payu.in/simulatorResponse" target="\_blank">https\://test-payment-middleware.payu.in/simulatorResponse\</a>
&#x20;                                                   \</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     furl\<br>
&#x20;                                                     \<code>mandatory\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> The failure URL, which is the page PayU will redirect to if the transaction fails.
&#x20;                                                   \</td>
&#x20;                                                   \<td>
&#x20;                                                       \<a href="https\://test-payment-middleware.payu.in/simulatorResponse" target="\_blank">https\://test-payment-middleware.payu.in/simulatorResponse\</a>
&#x20;                                                   \</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     hash\<br>
&#x20;                                                     \<code>mandatory\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> It is the hash calculated by the merchant. The hash calculation logic is:\<br>
&#x20;                                                     \<code>sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)\</code>\<br>
&#x20;                                                     Reference: For detailed information on hashing, refer to
&#x20;                                                     \<a href="generate-hash-payu-hosted" target="\_blank">Generate Hash\</a>.
&#x20;                                                   \</td>
&#x20;                                                   \<td>\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     address1\<br>
&#x20;                                                     \<code>optional\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> The first line of the billing address.\<br>
&#x20;                                                     Fraud Detection: This information is helpful for fraud detection and chargebacks. Please provide the correct information.
&#x20;                                                   \</td>
&#x20;                                                   \<td>H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     address2\<br>
&#x20;                                                     \<code>optional\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> The second line of the billing address.
&#x20;                                                   \</td>
&#x20;                                                   \<td>34 Saikripa-Estate, Tilak Nagar\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     city\<br>
&#x20;                                                     \<code>optional\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> The city where your customer resides as part of the billing address.
&#x20;                                                   \</td>
&#x20;                                                   \<td>Mumbai\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     state\<br>
&#x20;                                                     \<code>optional\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> The state where your customer resides as part of the billing address.
&#x20;                                                   \</td>
&#x20;                                                   \<td>Maharashtra\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     country\<br>
&#x20;                                                     \<code>optional\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> The country where your customer resides.
&#x20;                                                   \</td>
&#x20;                                                   \<td>India\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     zipcode\<br>
&#x20;                                                     \<code>optional\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> Billing address zip code is mandatory for the cardless EMI option.\<br>
&#x20;                                                     Character Limit: 20
&#x20;                                                   \</td>
&#x20;                                                   \<td>400004\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     enforced\_payment\<br>
&#x20;                                                     \<code>optional\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> This parameter is to customize the payment options for each transaction. You can enforce specific payment modes, card schemes, and specific banks under Net Banking using this method.
&#x20;                                                   \</td>
&#x20;                                                   \<td>creditcard|debitcard\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     drop\_category\<br>
&#x20;                                                     \<code>optional\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> This parameter is used if you want to hide one or multiple payment options. For example, if you consider the payment options such as credit card, debit card, and net banking, you can hide the credit card mode of payment.
&#x20;                                                   \</td>
&#x20;                                                   \<td>CC\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     udf1\<br>
&#x20;                                                     \<code>optional\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.
&#x20;                                                   \</td>
&#x20;                                                   \<td>AELPR\*\*\*\*E\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     udf2\<br>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.
&#x20;                                                   \</td>
&#x20;                                                   \<td>\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     udf3\<br>
&#x20;                                                     \<code>optional\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.
&#x20;                                                   \</td>
&#x20;                                                   \<td>02-02-1980\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     udf4\<br>
&#x20;                                                     \<code>optional\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.
&#x20;                                                   \</td>
&#x20;                                                   \<td>XYZ Pvt. Ltd.\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     udf5\<br>
&#x20;                                                     \<code>optional\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.
&#x20;                                                   \</td>
&#x20;                                                   \<td>098450845\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     custom\_note\<br>
&#x20;                                                     \<code>optional\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> This parameter allows you to display a message on the PayU Payment page. This can be useful if you want to provide additional information to your customers, such as an extra charge for a particular product. The message specified in the custom\_note parameter will be displayed below the payment options.
&#x20;                                                   \</td>
&#x20;                                                   \<td>You will be charged an extra amount of Rs 100 on this transaction\</td>
&#x20;                                                 \</tr>
&#x20;                                                 \<tr>
&#x20;                                                   \<td>
&#x20;                                                     note\_category\<br>
&#x20;                                                     \<code>optional\</code>
&#x20;                                                   \</td>
&#x20;                                                   \<td style="white-space: normal; word-break: break-word;">
&#x20;                                                     \<code>String\</code> This parameter allows you to specify which payment options the custom\_note message will be displayed for. This parameter should contain a comma-separated list of the payment options that you want the custom\_note displayed for. Example: "CC, NB" will show the custom\_note for Credit Card & Net banking only.
&#x20;                                                   \</td>
&#x20;                                                   \<td>CC, NB\</td>
&#x20;                                                 \</tr>
&#x20;                                               \</tbody>
&#x20;                                             \</table>
&#x20;                                           \</div>
&#x20; \`}\</HTMLBlock>

&#x20; \<Callout icon="📘" theme="info">
&#x20;   Swap the form action to the production endpoint: \[https\://secure.payu.in/\\\_payment]\(https\://secure.payu.in/\_payment) when you go live.
&#x20; \</Callout>
\</Accordion>

\<Accordion title="Step 1.2: Generate Hash" icon="fa-key">
&#x20; Concatenate fields in this exact sequence, then SHA-512:

&#x20; \`\`\`json
&#x20; key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|SALT
&#x20; \`\`\`

&#x20; \* Use empty strings for missing udf\\\*.
&#x20; \* Compute on your server and include the lowercase hex digest as hash.

&#x20; For more information, refer to  \<a href="generate-hash-payu-hosted" target="\_blank"> Generate Hash\</a>.
\</Accordion>

\<Accordion title="Step 1.3: POST the html form (server renders)" icon="fa-code">
&#x20; \`\`\`html
&#x20; \<!doctype html>
&#x20; \<html>
&#x20;   \<body onload="document.forms.payu.submit()">
&#x20;     \<form name="payu" method="post" action="https\://test.payu.in/\_payment">
&#x20;       \<input type="hidden" name="key" value="JP\*\*\*g">
&#x20;       \<input type="hidden" name="txnid" value="t6svtqtjRdl4ws">
&#x20;       \<input type="hidden" name="amount" value="499.00">
&#x20;       \<input type="hidden" name="productinfo" value="Pro Plan">
&#x20;       \<input type="hidden" name="firstname" value="Aditi">
&#x20;       \<input type="hidden" name="email" value="test\@example.com">
&#x20;       \<input type="hidden" name="phone" value="9999999999">
&#x20;       \<input type="hidden" name="surl" value="https\://yourapp.com/payu/success">
&#x20;       \<input type="hidden" name="furl" value="https\://yourapp.com/payu/failure">
&#x20;       \<input type="hidden" name="hash" value="sha512(...hash sequence...)">
&#x20;       \<input type="submit" value="Submit" />
&#x20;     \</form>
&#x20;   \</body>
&#x20; \</html>
&#x20; \`\`\`

&#x20; \*\*Replace the value attributes with your actual data and the generated hash. You can add more parameters to this form as needed.\*\*

&#x20; \<Callout icon="📘" theme="info">
&#x20;   \*\*Important\*\*

&#x20;   When you POST the form to \[https\://test.payu.in/\\\_payment]\(https\://test.payu.in/\_payment) or \[https\://secure.payu.in/\\\_payment]\(https\://secure.payu.in/\_payment), PayU returns HTML for the hosted checkout page (i.e., the payment UI). Render this response to user, it will render the PayU checkout.
&#x20; \</Callout>
\</Accordion>

\<Accordion title="Step 1.4: Response handling & hash verification" icon="fa-shield-check">
&#x20; \*\*Response Handling:\*\*

&#x20; After the customer completes or abandons the payment, PayU POSTs back to your return URL with URL-encoded fields (form post). This payload includes the transaction status, txnid, mihpayid, and a hash you must verify (reverse hashing) before trusting the result.

&#x20; Sample surl/furl payload:
&#x20;&#x20;
&#x20; \<Tabs groupId="callback" defaultValue="success" values=\{\[
&#x20;   \{ label: 'Success (surl)', value: 'success' },
&#x20;   \{ label: 'Failure (furl)', value: 'failure' }
&#x20; ]}>
&#x20;   \<TabItem value="success">

&#x20; \`\`\`json Success Response
&#x20; mihpayid=403993715531077182
&#x20; mode=CC
&#x20; status=success
&#x20; unmappedstatus=captured
&#x20; key=JPM7Fg
&#x20; txnid=TXN12345
&#x20; amount=1000.00
&#x20; productinfo=Pro Plan
&#x20; firstname=Aditi
&#x20; email=aditi\@example.com
&#x20; phone=9999999999
&#x20; udf1=
&#x20; ...
&#x20; udf10=
&#x20; PG\_TYPE=CC-PG
&#x20; bankcode=CC
&#x20; bank\_ref\_num=896193988312194700
&#x20; field1=...
&#x20; field9=Transaction is Successful
&#x20; hash=\<response\_hash>
&#x20; \`\`\`

&#x20; \`\`\`json Failure Response
&#x20; mihpayid=403993715531077182
&#x20; mode=CC
&#x20; status=failure
&#x20; unmappedstatus=failed
&#x20; key=JPM7Fg
&#x20; txnid=TXN12345
&#x20; amount=1000.00
&#x20; productinfo=Pro Plan
&#x20; firstname=Aditi
&#x20; email=aditi\@example.com
&#x20; phone=9999999999
&#x20; udf1=
&#x20; ...
&#x20; udf10=
&#x20; PG\_TYPE=CC-PG
&#x20; bankcode=CC
&#x20; bank\_ref\_num=
&#x20; field1=
&#x20; field2=
&#x20; ...
&#x20; field9=Transaction Failed
&#x20; error=E000
&#x20; error\_Message=Bank was unable to authenticate
&#x20; hash=\<response\_hash>
&#x20; \`\`\`

&#x20; \*\*Step 1.4.1: Response verification using reverse hashing\*\*

&#x20; Verify the response received above by recomputing SHA-512 using the reverse sequence:

&#x20; \`\`\`json
&#x20; sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
&#x20; \`\`\`

&#x20; \* Compare the computed digest to hash from the POST payload (\*\*case-insensitive\*\*).
&#x20; \* Trust the result only if the hash matches. Then update your order state.
\</Accordion>

\<Accordion title="Step 1.5: Verify the payment" icon="fa-magnifying-glass">
&#x20; Upon receiving the response, We recommend performing a reconciliation step by querying the verification APIs to validate all transaction details.

&#x20; \*\*Environment\*\*

&#x20; \|                        |                                                                                                              |
&#x20; \| :--------------------- | :----------------------------------------------------------------------------------------------------------- |
&#x20; \| Test Environment       | \[https\://test.payu.in/merchant/postservice.php?form=2]\(https\://test.payu.in/merchant/postservice.php?form=2) |
&#x20; \| Production Environment | \[https\://info.payu.in/merchant/postservice.php?form=2]\(https\://info.payu.in/merchant/postservice.php?form=2) |

&#x20; \<Accordion title="Sample request" icon="fa-code">
&#x20;   \`\`\`curl
&#x20;   curl --location 'https\://test.payu.in/merchant/postservice.php?form=2' \\
&#x20;   \--header 'Content-Type: application/x-www-form-urlencoded' \\
&#x20;   \--data-urlencode 'key=JP\*\*\*g' \\
&#x20;   \--data-urlencode 'command=verify\_payment' \\
&#x20;   \--data-urlencode 'var1=IhfgcZnXR4o4nB' \\
&#x20;   \--data-urlencode 'hash=a0ae79fdd66c875af6e9b21c4a67f1822deb00f2df5e9f0b1948f3222f536a9bf741b24efbb1874ca0f84f76b036e6c0d641581d0100f7abe4aeed2f3264f5c9'
&#x20;   \`\`\`
&#x20; \</Accordion>

&#x20; \<Accordion title="Sample response" icon="fa-reply">
&#x20;   \* If credit card payment is made, the response is similar to the following:

&#x20;   \`\`\`plaintext
&#x20;   \{
&#x20;       "status": 1,
&#x20;       "msg": "1 out of 1 Transactions Fetched Successfully",
&#x20;       "transaction\_details": \{
&#x20;           "1733900931584": \{
&#x20;               "mihpayid": "21820644083",
&#x20;               "request\_id": null,
&#x20;               "bank\_ref\_num": null,
&#x20;               "amt": "1.00",
&#x20;               "transaction\_amount": "1.00",
&#x20;               "txnid": "1733900931584",
&#x20;               "additional\_charges": "0.00",
&#x20;               "productinfo": "Macbook Pro",
&#x20;               "firstname": "Abc",
&#x20;               "bankcode": "MAST",
&#x20;               "udf1": "udf1",
&#x20;               "udf2": "udf2",
&#x20;               "udf3": "udf3",
&#x20;               "udf4": "udf4",
&#x20;               "udf5": "udf5",
&#x20;               "field2": null,
&#x20;               "field9": "OTP/ATM page expired due to no user action",
&#x20;               "error\_code": "E1602",
&#x20;               "addedon": "2024-12-11 12:43:03",
&#x20;               "payment\_source": "payu",
&#x20;               "card\_type": "MAST",
&#x20;               "error\_Message": "Bank was unable to authenticate.",
&#x20;               "net\_amount\_debit": "0.00",
&#x20;               "disc": "0.00",
&#x20;               "mode": "DC",
&#x20;               "PG\_TYPE": "DC-PG",
&#x20;               "card\_no": "XXXXXXXXXXXX7596",
&#x20;               "status": "failure",
&#x20;               "unmappedstatus": "dropped",
&#x20;               "Merchant\_UTR": null,
&#x20;               "Settled\_At": null,
&#x20;               "cardhash": "095d184331be367bb92aa3eeecb57d0728de96cc598dd563d407982d75021149",
&#x20;               "name\_on\_card": null,
&#x20;               "card\_token": "4e97156bc2d6320cdfe15",
&#x20;               "field4": null,
&#x20;               "threeDSVersion": "2.2.0",
&#x20;               "offerAvailed": null
&#x20;           }
&#x20;       }
&#x20;   }
&#x20;   \`\`\`

&#x20;   \* Offer availed on cart level

&#x20;   \`\`\`
&#x20;   \{
&#x20;       "status": 1,
&#x20;       "msg": "1 out of 1 Transactions Fetched Successfully",
&#x20;       "transaction\_details": \{
&#x20;           "1036-f0cf85f2": \{
&#x20;               "mihpayid": "21564143078",
&#x20;               "request\_id": "",
&#x20;               "bank\_ref\_num": "431998369241",
&#x20;               "amt": "2.00",
&#x20;               "transaction\_amount": "2.00",
&#x20;               "txnid": "1036-f0cf85f2",
&#x20;               "additional\_charges": "0.00",
&#x20;               "productinfo": "EXPRESS",
&#x20;               "firstname": "guest",
&#x20;               "bankcode": "TEZOMNI",
&#x20;               "udf1": "Magento2",
&#x20;               "udf2": "",
&#x20;               "udf3": "",
&#x20;               "udf4": "",
&#x20;               "udf5": "qs8rbc1ng2hmqtakk381en6j2p",
&#x20;               "field2": "114390824407",
&#x20;               "field9": "SUCCESS|Completed Using Callback",
&#x20;               "error\_code": "E000",
&#x20;               "addedon": "2024-11-14 16:06:40",
&#x20;               "payment\_source": "express",
&#x20;               "card\_type": null,
&#x20;               "error\_Message": "NO ERROR",
&#x20;               "net\_amount\_debit": 2.00,
&#x20;               "disc": "0.00",
&#x20;               "mode": "UPI",
&#x20;               "PG\_TYPE": "UPI-PG",
&#x20;               "card\_no": "",
&#x20;               "status": "success",
&#x20;               "unmappedstatus": "captured",
&#x20;               "Merchant\_UTR": null,
&#x20;               "Settled\_At": "0000-00-00 00:00:00",
&#x20;               "App\_Name": "GooglePay",
&#x20;               "card\_token": null,
&#x20;               "field4": null,
&#x20;               "offerAvailed": null,
&#x20;               "cart\_details": \{
&#x20;                   "id": "2446425",
&#x20;                   "payu\_id": "21564143078",
&#x20;                   "total\_items": "1",
&#x20;                   "total\_cart\_amount": "2.00",
&#x20;                   "offer\_applied": null,
&#x20;                   "offer\_availed": null,
&#x20;                   "offer\_auto\_apply": "0",
&#x20;                   "instant\_discount": "0.00",
&#x20;                   "cashback\_discount": "0.00",
&#x20;                   "total\_discount": "0.00",
&#x20;                   "net\_cart\_amount": "2.00",
&#x20;                   "created\_at": "2024-11-14 16:06:40",
&#x20;                   "updated\_at": "2024-11-14 16:06:40",
&#x20;                   "sku\_details": \[
&#x20;                       \{
&#x20;                           "id": "3468748",
&#x20;                           "cart\_id": "2446425",
&#x20;                           "payu\_id": "21564143078",
&#x20;                           "mid": "2",
&#x20;                           "sku\_id": "Sample Sofa Design-Red",
&#x20;                           "sku\_name": "Sample Sofa Designtest?=!name",
&#x20;                           "amount\_per\_sku": "2.00",
&#x20;                           "quantity": "1",
&#x20;                           "amount\_before\_discount": "2.00",
&#x20;                           "discount": "0.00",
&#x20;                           "amount\_after\_discount": "2.00",
&#x20;                           "offer\_applied": null,
&#x20;                           "offer\_availed": null,
&#x20;                           "offer\_status": null,
&#x20;                           "offer\_type": null,
&#x20;                           "offer\_auto\_apply": "0",
&#x20;                           "is\_nce": "0",
&#x20;                           "failure\_reason": null,
&#x20;                           "created\_at": "2024-11-14 16:06:40",
&#x20;                           "updated\_at": "2024-11-14 16:06:40",
&#x20;                           "offer\_title": null,
&#x20;                           "offer\_description": null,
&#x20;                           "instant\_discount": null,
&#x20;                           "cashback\_discount": null,
&#x20;                           "offers\_raw\_response": null,
&#x20;                           "raw\_response": null
&#x20;                       }
&#x20;                   ]
&#x20;               }
&#x20;           }
&#x20;       }
&#x20;   }
&#x20;   \`\`\`

&#x20;   \* Offer availed at Transaction level

&#x20;   \`\`\`
&#x20;   \{
&#x20;       "status": 1,
&#x20;       "msg": "1 out of 1 Transactions Fetched Successfully",
&#x20;       "transaction\_details": \{
&#x20;           "1725950872187": \{
&#x20;               "mihpayid": "20911942990",
&#x20;               "request\_id": null,
&#x20;               "bank\_ref\_num": null,
&#x20;               "amt": "9900.00",
&#x20;               "transaction\_amount": "10000.00",
&#x20;               "txnid": "1725950872187",
&#x20;               "additional\_charges": "0.00",
&#x20;               "productinfo": "Macbook Pro",
&#x20;               "firstname": "Abc",
&#x20;               "bankcode": "MAST",
&#x20;               "udf1": "udf1",
&#x20;               "udf2": "udf2",
&#x20;               "udf3": "udf3",
&#x20;               "udf4": "udf4",
&#x20;               "udf5": "udf5",
&#x20;               "field2": null,
&#x20;               "field9": "You have reached credit card load limit. Please use other payment options to continue.",
&#x20;               "error\_code": "E4936",
&#x20;               "addedon": "2024-09-10 12:18:20",
&#x20;               "payment\_source": "payu",
&#x20;               "card\_type": "MAST",
&#x20;               "error\_Message": "Bank was unable to authenticate.",
&#x20;               "net\_amount\_debit": "0.00",
&#x20;               "disc": "100.00",
&#x20;               "mode": "DC",
&#x20;               "PG\_TYPE": "DC-PG",
&#x20;               "card\_no": "XXXXXXXXXXXX9528",
&#x20;               "status": "failure",
&#x20;               "unmappedstatus": "failed",
&#x20;               "Merchant\_UTR": null,
&#x20;               "Settled\_At": null,
&#x20;               "cardhash": "31056eb2112b68cdc90896f1953ca26605bb525249096172c178881bcd45ac93",
&#x20;               "name\_on\_card": null,
&#x20;               "card\_token": null,
&#x20;               "field4": null,
&#x20;               "offerApplied": "LoadTest1\@m3phN7YptAA6",
&#x20;               "offerAvailed": "LoadTest1\@m3phN7YptAA6",
&#x20;               "transactionOffer": "\{\\"offer\_data\\":\[\{\\"offer\_key\\":\\"LoadTest1\@m3phN7YptAA6\\",\\"discount\\":100,\\"offer\_type\\":\\"INSTANT\\",\\"isNoCost\\":false,\\"flag\_to\_fail\\":false,\\"status\\":\\"SUCCESS\\",\\"failure\_code\\":null,\\"failure\_reason\\":\\"Offer Applied Successfully\\",\\"offer\_description\\":\\"Load Test 1\\",\\"offer\_title\\":\\"Load Test 1\\",\\"record\_type\\":\\"OFFER\\",\\"parent\_offer\_key\\":null,\\"offer\_category\\":null,\\"isDpEmi\\":false}],\\"discount\_data\\":\{\\"total\_discount\\":100,\\"cashback\_discount\\":0,\\"instant\_discount\\":100,\\"total\_nce\_discount\\":0,\\"instant\_nce\_discount\\":0,\\"cashback\_nce\_discount\\":0,\\"gstSubventedViaOffer\\":false,\\"downPaymentAmount\\":0}}",
&#x20;               "offerType": "instant",
&#x20;               "offerLevel": "TRANSACTION\_LEVEL"
&#x20;           }
&#x20;       }
&#x20;   }
&#x20;   \`\`\`

&#x20;   \*\*Failure Responses\*\*

&#x20;   \* If txnID is not found, the response is similar to the following:

&#x20;   \`\`\`plaintext
&#x20;   \{
&#x20;   "status":0,"msg":"0 out of 1 Transactions Fetched

&#x20;   Successfully","transaction\_details":\{"IhfgcZnXR4o4nB":\{"mihpayid":"Not Found","status":"Not Found"}}
&#x20;   }
&#x20;   \`\`\`
&#x20; \</Accordion>

&#x20; \<Accordion title="Response parameters" icon="fa-list">
&#x20;   \<Table align=\{\["left","left","left"]}>
&#x20;     \<thead>
&#x20;       \<tr>
&#x20;         \<th style=\{\{ textAlign: "left" }}>
&#x20;           \*\*Parameter\*\*
&#x20;         \</th>

&#x20;         \<th style=\{\{ textAlign: "left" }}>
&#x20;           \*\*Description\*\*
&#x20;         \</th>

&#x20;         \<th style=\{\{ textAlign: "left" }}>
&#x20;           \*\*Example\*\*
&#x20;         \</th>
&#x20;       \</tr>
&#x20;     \</thead>

&#x20;     \<tbody>
&#x20;       \<tr>
&#x20;         \<td style=\{\{ textAlign: "left" }}>
&#x20;           status
&#x20;         \</td>

&#x20;         \<td style=\{\{ textAlign: "left" }}>
&#x20;           This parameter returns the status of web service call. The status can be any of the following:

&#x20;           \* 0 - If web service call failed.
&#x20;           \* 1 - If web service call succeeded
&#x20;         \</td>

&#x20;         \<td style=\{\{ textAlign: "left" }}>
&#x20;           0
&#x20;         \</td>
&#x20;       \</tr>

&#x20;       \<tr>
&#x20;         \<td style=\{\{ textAlign: "left" }}>
&#x20;           msg
&#x20;         \</td>

&#x20;         \<td style=\{\{ textAlign: "left" }}>
&#x20;           This parameter returns the reason string.
&#x20;         \</td>

&#x20;         \<td style=\{\{ textAlign: "left" }}>
&#x20;           For example, any of the following messages are displayed:

&#x20;           \* Parameter missing
&#x20;           \* Token is empty
&#x20;           \* Amount is empty
&#x20;           \* Transaction not exists
&#x20;         \</td>
&#x20;       \</tr>

&#x20;       \<tr>
&#x20;         \<td style=\{\{ textAlign: "left" }}>
&#x20;           transaction\\\_details
&#x20;         \</td>

&#x20;         \<td style=\{\{ textAlign: "left" }}>
&#x20;           This parameter contains the response in a JSON format. For more information refer to \[JSON fields description for transaction\\\_details parameter ]\(#json-field-description-for-transaction\_details-parameter).
&#x20;         \</td>

&#x20;         \<td style=\{\{ textAlign: "left" }} />
&#x20;       \</tr>

&#x20;       \<tr>
&#x20;         \<td style=\{\{ textAlign: "left" }}>
&#x20;           request\\\_id
&#x20;         \</td>

&#x20;         \<td style=\{\{ textAlign: "left" }}>
&#x20;           PayU Request ID for a request in a Transaction. For example, a transaction can have a refund request.
&#x20;         \</td>

&#x20;         \<td style=\{\{ textAlign: "left" }}>
&#x20;           7800456
&#x20;         \</td>
&#x20;       \</tr>

&#x20;       \<tr>
&#x20;         \<td style=\{\{ textAlign: "left" }}>
&#x20;           bank\\\_ref\\\_num
&#x20;         \</td>

&#x20;         \<td style=\{\{ textAlign: "left" }}>
&#x20;           This parameter returns the bank reference number. If the bank provides after a successful action.
&#x20;         \</td>

&#x20;         \<td style=\{\{ textAlign: "left" }}>
&#x20;           204519474956
&#x20;         \</td>
&#x20;       \</tr>
&#x20;     \</tbody>
&#x20;   \</Table>

&#x20;   To learn more about the possible error codes and their description, refer to \[Error Codes]\(https\://docs.payu.in/reference/error-codes).
&#x20; \</Accordion>
\</Accordion>

<br />

## Step 2: Test Integration

Before going live, it's crucial to test your integration thoroughly in the PayU test environment. Follow these steps to ensure your setup is correct and to simulate different transaction scenarios.

<Accordion title="Step 2.1: Pre-Payment Validation" icon="fa-check-circle">
  **Configure Webhooks**
  Configure the webhooks to monitor the status of payments. Webhooks emable a server to communicate with another server by sending an HTTP callback or message. These callbacks are triggered by specific events or instances and they operate at the server-to-server (S2S) level.  For more information, refer to [Webhooks for Payments](https://docs.payu.in/docs/webhooks).

  **Verify Payment**

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
     2. Enter a test UPI ID: testsuccess\@gpay
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

  1. **Generate Live Keys:**
     * Log in to your **PayU Dashboard**.
     * Use the toggle at the top to switch from **Test Mode** to **Live Mode**.
     * Navigate to **Developer Tools** → **API Keys** from the sidebar.
     * Copy the **Live Merchant Key** and **Live Salt**.
  2. **Update Your Code:**
     * In your integration code, replace the test `key` and `salt` with your new live credentials.
  3. **Update the Endpoint URL:**
     * Ensure all API requests are now being sent to the production endpoint:
       `https://secure.payu.in/_payment`
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
