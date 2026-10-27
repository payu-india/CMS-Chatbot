---
title: Merchant Hosted - Quick Start Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
<Banner color="#FFC107">Some technical setup required: you build the checkout page and generate the hash on your server.</Banner>

## When to Use Merchant Hosted Checkout

Use Merchant Hosted Checkout if you want to:

- Keep customers on **your** branded checkout page from start to finish
- Control how payment methods, fields and the order summary appear
- Post the payment method details (`pg`, `bankcode` and method-specific fields) directly to PayU

If you'd rather not build a checkout page, use [PayU Hosted Checkout](doc:payu-hosted-checkout) instead. It needs less technical work. For more about this option, see [Merchant Hosted Checkout](doc:merchant-hosted-checkout).

This quick start covers the four most common payment methods: **cards**, **net banking**, **UPI** and **wallets**. One request, one hash formula and one response check work for all of them. Only the method-specific parameters change.

***

<Accordion title="What it looks like after integration" icon="far fa-check-to-slot">
  The sample screens below use a fictitious merchant, **Nimbus Mart**, to show a typical Merchant Hosted Checkout experience.

  ### 1. Checkout on your website

  Customers stay on **Nimbus Mart**, choose a payment method and enter their details next to the order summary. You control this page. PayU receives the payment request you post.

  ![](https://files.readme.io/885ee54d0bb0b25b9ea1584b6b13cadf03e710a52e326175a8d9246181cd4102-nimbus-mart-card-checkout.png)

  ### 2. Authentication

  Depending on the payment method, the customer:

  - enters an OTP or completes 3-D Secure (cards)
  - logs in to their bank (net banking)
  - approves the request in their UPI app (UPI)
  - approves in the wallet (wallets)

  ![](https://files.readme.io/73e4b2dff67dae8877f975da455056e465e964c7e7b90f0f79a6e762968fc15c-nimbus-mart-otp-challenge.png)

  ### 3. Payment success on your website

  PayU sends the customer back to your success page. Mark the order as paid only after the reverse hash check and a Verify Payment or webhook confirmation.

  ![](https://files.readme.io/414295fecb5baa482d60a4bf9c2906122d08ec89c7c06a0790f4b84e10ab5378-nimbus-mart-payment-success.png)

  {/* REVIEW: these screenshots show a card payment. Consider adding net banking, UPI and wallet screens. */}
</Accordion>

***

## Prerequisites

Before you begin:

- Create a [PayU account](https://onboarding.payu.in/app/account/signup).
- Get your merchant **key** and **salt** for the test and production environments.
- Ask PayU to enable the payment methods you want to accept (cards, net banking, UPI, wallets) on your account.
- Make sure your success (`surl`) and failure (`furl`) URLs use HTTPS and can be reached from the public internet.
- Be able to generate a SHA-512 hash on your server (never in the browser).
- Generate a unique transaction ID (`txnid`) for every payment attempt.

<Callout icon="🚧" theme="warn">
  ### **Watch Out! Cards need PCI DSS compliance**

  When customers enter card details on your page, you're responsible for PCI DSS compliance. PayU rejects card payments sent from your checkout page unless your business is registered with PayU as PCI DSS compliant. Net banking, UPI and wallets aren't affected.

  For cards, never store the CVV, never log the full card number, and use HTTPS on every page.
</Callout>

***

## Make Your Test Payment

| **Environment**            | **URL**                           |
| :------------------------- | :-------------------------------- |
| **Test Environment**       | `https://test.payu.in/_payment`   |
| **Production Environment** | `https://secure.payu.in/_payment` |

<Accordion title="Step 1: Prepare Request Parameters" icon="far fa-table-list">
  Every payment request has two parts: the **common parameters**, which are the same for every payment method, and the **payment method parameters**.

  ### Common parameters

  | **Parameter**   | **Description**                                                                             | **Example**                              |
  | :-------------- | :------------------------------------------------------------------------------------------ | :--------------------------------------- |
  | **key**         | `string` Merchant key provided by PayU.                                                     | `JPM7Fg`                                 |
  | **txnid**       | `string` Your unique reference for this payment attempt. Use a new value for every attempt. | `txn_123456`                             |
  | **amount**      | `string` Amount in INR, up to 2 decimal places, no commas.                                  | `10.00`                                  |
  | **productinfo** | `string` Short description of the product.                                                  | `Wireless Earbuds`                       |
  | **firstname**   | `string` Customer's first name.                                                             | `Aarav`                                  |
  | **email**       | `string` Customer's email address.                                                          | `aarav@testmail.com`                     |
  | **phone**       | `string` Customer's 10-digit mobile number.                                                 | `9999999999`                             |
  | **surl**        | `string` HTTPS URL that PayU sends the customer to after a successful payment.              | `https://nimbusmart.example.com/success` |
  | **furl**        | `string` HTTPS URL that PayU sends the customer to after a failed payment.                  | `https://nimbusmart.example.com/failure` |
  | **pg**          | `string` Payment method category. See the tabs below.                                       | `CC`                                     |
  | **bankcode**    | `string` Specific payment option within the category. See the tabs below.                   | `CC`                                     |
  | **hash**        | `string` SHA-512 hash generated on your server in Step 2.                                   | `YOUR_GENERATED_HASH`                    |

  ### Payment method parameters

  <Tabs>
    <Tab title="Cards">
      | **Parameter** | **Description**                                                                                     | **Example**        |
      | :------------ | :-------------------------------------------------------------------------------------------------- | :----------------- |
      | **pg**        | `string` Set to `CC` for credit and debit cards.                                                    | `CC`               |
      | **bankcode**  | `string` Card type code, for example `CC`, `MAST` or `VISA`.                                        | `CC`               |
      | **ccnum**     | `string` Card number. Use a [test card](doc:test-cards-upi-id-and-wallets) in the test environment. | `5123456789012346` |
      | **ccname**    | `string` Name on the card.                                                                          | `Aarav Sharma`     |
      | **ccvv**      | `string` CVV. Never store it after sending the request.                                             | `123`              |
      | **ccexpmon**  | `string` Expiry month in `MM` format.                                                               | `05`               |
      | **ccexpyr**   | `string` Expiry year in `YYYY` format.                                                              | `2030`             |
    </Tab>

    <Tab title="Net banking">
      | **Parameter** | **Description**                                                                                                                                         | **Example** |
      | :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------- |
      | **pg**        | `string` Set to `NB`.                                                                                                                                   | `NB`        |
      | **bankcode**  | `string` Code of the customer's bank. Use `TESTPGNB` in the test environment. For live bank codes, refer to [Net Banking Codes](doc:net-banking-codes). | `TESTPGNB`  |
    </Tab>

    <Tab title="UPI">
      | **Parameter** | **Description**                                                                                                   | **Example**      |
      | :------------ | :---------------------------------------------------------------------------------------------------------------- | :--------------- |
      | **pg**        | `string` Set to `UPI`.                                                                                            | `UPI`            |
      | **bankcode**  | `string` Set to `UPI` for a collect request sent to the customer's UPI ID.                                        | `UPI`            |
      | **vpa**       | `string` Customer's UPI ID. Validate it before sending the request. Use `9999999999@upi` in the test environment. | `9999999999@upi` |

      <Callout icon="📘" theme="info">
        ### **Note**

        To open the customer's UPI app directly instead (UPI Intent), use `bankcode=INTENT` with a server-to-server request. Refer to [UPI Intent Integration](doc:upi-intent-merchant-hosted). {/* REVIEW: confirm the UPI Intent guide slug. */}
      </Callout>
    </Tab>

    <Tab title="Wallets">
      | **Parameter** | **Description**                                                                                                               | **Example** |
      | :------------ | :---------------------------------------------------------------------------------------------------------------------------- | :---------- |
      | **pg**        | `string` Set to `CASH` for wallets.                                                                                           | `CASH`      |
      | **bankcode**  | `string` Code of the wallet, for example `AMZPAY` for Amazon Pay. For other codes, refer to [Wallet Codes](doc:wallet-codes). | `AMZPAY`    |

      {/* REVIEW: confirm the wallet codes page slug and a wallet code that works in the test environment. */}
    </Tab>
  </Tabs>

  <Callout icon="📘" theme="info">
    ### **Tips**

    - `txnid` must be unique for every attempt, including retries.
    - Remove extra spaces from every value.
    - Your **salt** isn't a request parameter. Use it only on your server to generate the hash, and never send it to PayU or to the browser.
  </Callout>

  **Expected output:** a set of common parameters plus the parameters for one payment method, ready to hash.
</Accordion>

<Accordion title="Step 2: Generate the SHA-512 Hash (Critical Step)" icon="far fa-lock-a">
  The hash protects your payment request from being changed on the way to PayU. If the hash is wrong, PayU rejects the payment with an `Invalid Hash` error.

  The formula is the same for every payment method. The method-specific parameters (`pg`, `bankcode`, card fields, `vpa`) aren't part of the hash.

  ```Hash Logic
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
  ```

  If you don't send `udf1`–`udf5`, leave their positions empty:

  ```Example Hash String
  JPM7Fg|txn_123456|10.00|Wireless Earbuds|Aarav|aarav@testmail.com|||||||||||YOUR_SALT
  ```

  <Callout icon="🚧" theme="warn">
    ### **Critical Rules**

    - Don't change the parameter order.
    - Don't skip pipes (`|`). Keep the separators for empty fields, including `udf1`–`udf5`.
    - Use exactly the same values in the hash and in the request.
    - Remove extra spaces and hidden characters, and encode the string as UTF-8.
    - Generate the hash only on your server.
  </Callout>

  <Tabs>
    <Tab title="Node.js">
      ```javascript
      const crypto = require("crypto");

      function generateHash(p, salt) {
        const hashString = [
          p.key, p.txnid, p.amount, p.productinfo, p.firstname, p.email,
          p.udf1 || "", p.udf2 || "", p.udf3 || "", p.udf4 || "", p.udf5 || "",
          "", "", "", "", "", salt
        ].join("|");

        return crypto.createHash("sha512").update(hashString, "utf8").digest("hex");
      }

      const hash = generateHash({
        key: "JPM7Fg",
        txnid: "txn_123456",
        amount: "10.00",
        productinfo: "Wireless Earbuds",
        firstname: "Aarav",
        email: "aarav@testmail.com"
      }, process.env.PAYU_SALT);

      console.log(hash);
      ```
    </Tab>

    <Tab title="PHP">
      ```php
      <?php
      function generateHash($p, $salt) {
          $hashString = implode('|', [
              $p['key'], $p['txnid'], $p['amount'], $p['productinfo'], $p['firstname'], $p['email'],
              $p['udf1'] ?? '', $p['udf2'] ?? '', $p['udf3'] ?? '', $p['udf4'] ?? '', $p['udf5'] ?? '',
              '', '', '', '', '', $salt
          ]);
          return strtolower(hash('sha512', $hashString));
      }

      $hash = generateHash([
          'key' => 'JPM7Fg',
          'txnid' => 'txn_123456',
          'amount' => '10.00',
          'productinfo' => 'Wireless Earbuds',
          'firstname' => 'Aarav',
          'email' => 'aarav@testmail.com'
      ], getenv('PAYU_SALT'));

      echo $hash;
      ```
    </Tab>

    <Tab title="Python">
      ```python
      import hashlib
      import os

      def generate_hash(p, salt):
          fields = [
              p["key"], p["txnid"], p["amount"], p["productinfo"], p["firstname"], p["email"],
              p.get("udf1", ""), p.get("udf2", ""), p.get("udf3", ""), p.get("udf4", ""), p.get("udf5", ""),
              "", "", "", "", "", salt,
          ]
          return hashlib.sha512("|".join(fields).encode("utf-8")).hexdigest()

      print(generate_hash({
          "key": "JPM7Fg",
          "txnid": "txn_123456",
          "amount": "10.00",
          "productinfo": "Wireless Earbuds",
          "firstname": "Aarav",
          "email": "aarav@testmail.com",
      }, os.environ["PAYU_SALT"]))
      ```
    </Tab>
  </Tabs>

  <Accordion title="Debug your hash (highly recommended)" icon="far fa-computer-mouse-button-left">
    Before you use the hash, print the exact string so you can spot extra spaces, line breaks or missing pipes:

    ```javascript
    console.log(JSON.stringify(hashString));
    ```
  </Accordion>

  **Expected output:** a 128-character lowercase hexadecimal string.
</Accordion>

<Accordion title="Step 3: Post the Payment Request" icon="far fa-paper-plane">
  Post the parameters to the test URL as `application/x-www-form-urlencoded`. In production, build the form on your server after you generate the hash.

  <Tabs>
    <Tab title="Cards">
      ```curl
      curl -X POST "https://test.payu.in/_payment" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -d "key=JPM7Fg" \
        -d "txnid=txn_123456" \
        -d "amount=10.00" \
        -d "productinfo=Wireless Earbuds" \
        -d "firstname=Aarav" \
        -d "email=aarav@testmail.com" \
        -d "phone=9999999999" \
        -d "surl=https://nimbusmart.example.com/success" \
        -d "furl=https://nimbusmart.example.com/failure" \
        -d "pg=CC" \
        -d "bankcode=CC" \
        -d "ccnum=5123456789012346" \
        -d "ccname=Aarav Sharma" \
        -d "ccvv=123" \
        -d "ccexpmon=05" \
        -d "ccexpyr=2030" \
        -d "hash=YOUR_GENERATED_HASH"
      ```
    </Tab>

    <Tab title="Net banking">
      ```curl
      curl -X POST "https://test.payu.in/_payment" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -d "key=JPM7Fg" \
        -d "txnid=txn_123457" \
        -d "amount=10.00" \
        -d "productinfo=Wireless Earbuds" \
        -d "firstname=Aarav" \
        -d "email=aarav@testmail.com" \
        -d "phone=9999999999" \
        -d "surl=https://nimbusmart.example.com/success" \
        -d "furl=https://nimbusmart.example.com/failure" \
        -d "pg=NB" \
        -d "bankcode=TESTPGNB" \
        -d "hash=YOUR_GENERATED_HASH"
      ```
    </Tab>

    <Tab title="UPI">
      ```curl
      curl -X POST "https://test.payu.in/_payment" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -d "key=JPM7Fg" \
        -d "txnid=txn_123458" \
        -d "amount=10.00" \
        -d "productinfo=Wireless Earbuds" \
        -d "firstname=Aarav" \
        -d "email=aarav@testmail.com" \
        -d "phone=9999999999" \
        -d "surl=https://nimbusmart.example.com/success" \
        -d "furl=https://nimbusmart.example.com/failure" \
        -d "pg=UPI" \
        -d "bankcode=UPI" \
        -d "vpa=9999999999@upi" \
        -d "hash=YOUR_GENERATED_HASH"
      ```
    </Tab>

    <Tab title="Wallets">
      ```curl
      curl -X POST "https://test.payu.in/_payment" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -d "key=JPM7Fg" \
        -d "txnid=txn_123459" \
        -d "amount=10.00" \
        -d "productinfo=Wireless Earbuds" \
        -d "firstname=Aarav" \
        -d "email=aarav@testmail.com" \
        -d "phone=9999999999" \
        -d "surl=https://nimbusmart.example.com/success" \
        -d "furl=https://nimbusmart.example.com/failure" \
        -d "pg=CASH" \
        -d "bankcode=AMZPAY" \
        -d "hash=YOUR_GENERATED_HASH"
      ```
    </Tab>

    <Tab title="HTML form">
      ```html
      <!-- Render this form from your server after generating the hash. Never put your salt in the page. -->
      <form action="https://test.payu.in/_payment" method="post">
        <input type="hidden" name="key" value="JPM7Fg" />
        <input type="hidden" name="txnid" value="txn_123457" />
        <input type="hidden" name="amount" value="10.00" />
        <input type="hidden" name="productinfo" value="Wireless Earbuds" />
        <input type="hidden" name="firstname" value="Aarav" />
        <input type="hidden" name="email" value="aarav@testmail.com" />
        <input type="hidden" name="phone" value="9999999999" />
        <input type="hidden" name="surl" value="https://nimbusmart.example.com/success" />
        <input type="hidden" name="furl" value="https://nimbusmart.example.com/failure" />
        <input type="hidden" name="pg" value="NB" />
        <input type="hidden" name="bankcode" value="TESTPGNB" />
        <input type="hidden" name="hash" value="YOUR_GENERATED_HASH" />
        <button type="submit">Pay ₹10.00</button>
      </form>
      ```
    </Tab>
  </Tabs>

  **Replace:**

  - `JPM7Fg` with your test key
  - `YOUR_GENERATED_HASH` with the hash from Step 2
  - `surl` and `furl` with your own HTTPS URLs

  **Expected output:** the customer is taken to the authentication step for the chosen payment method.
</Accordion>

<Accordion title="Step 4: Complete the Test Payment" icon="far fa-circle-check">
  1. Serve your checkout page from a local or test server (HTTPS recommended).
  2. Submit the payment request to the PayU test URL.
  3. Complete authentication with the [test credentials](doc:test-cards-upi-id-and-wallets):

  | **Payment method** | **What to do in the test environment**                          |
  | :----------------- | :-------------------------------------------------------------- |
  | Cards              | Use a test card and enter the test OTP when prompted.           |
  | Net banking        | Use `TESTPGNB` and complete the test bank page.                 |
  | UPI                | Use `9999999999@upi` and approve the simulated collect request. |
  | Wallets            | Use the wallet test details from the test credentials page.     |

  4. Check that you land on your `surl` (success) or `furl` (failure).

  **Expected output:** PayU posts the payment result to your `surl` or `furl`.
</Accordion>

<Accordion title="Step 5: Check the Response" icon="far fa-shield-check">
  PayU posts the result to your `surl` or `furl` as form data. Before you mark the order as paid:

  1. **Check the reverse hash.** Calculate it on your server and compare it with the `hash` you received:

     ```Reverse Hash Logic
     sha512(salt|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
     ```

  2. **Check the status.** Treat the payment as successful only when `status` is `success` and the reverse hash matches.

  3. **Confirm with PayU.** Call the [Verify Payment API](doc:verify-payment-api) or use a [webhook](doc:webhooks) before you fulfil the order.

  {/* REVIEW: the reverse hash formula changes if the response includes additional_charges. Confirm the wording and the Verify Payment API and webhook slugs. */}

  <Tabs>
    <Tab title="Success">
      ```json
      {
        "mihpayid": "403993715525331373",
        "mode": "CC",
        "status": "success",
        "unmappedstatus": "captured",
        "key": "JPM7Fg",
        "txnid": "txn_123456",
        "amount": "10.00",
        "productinfo": "Wireless Earbuds",
        "firstname": "Aarav",
        "email": "aarav@testmail.com",
        "phone": "9999999999",
        "field9": "Transaction Completed Successfully",
        "bankcode": "CC",
        "error": "E000",
        "error_Message": "No Error",
        "hash": "<response hash>"
      }
      ```
    </Tab>

    <Tab title="Failure">
      ```json
      {
        "mihpayid": "403993715525331374",
        "mode": "CC",
        "status": "failure",
        "unmappedstatus": "failed",
        "key": "JPM7Fg",
        "txnid": "txn_123460",
        "amount": "10.00",
        "productinfo": "Wireless Earbuds",
        "firstname": "Aarav",
        "email": "aarav@testmail.com",
        "field9": "Transaction declined due to either incorrect cvv/expiry or card validation failure",
        "bankcode": "CC",
        "error": "E1632",
        "error_Message": "Transaction declined due to either incorrect cvv/expiry or card validation failure",
        "hash": "<response hash>"
      }
      ```
    </Tab>
  </Tabs>

  {/* REVIEW: illustrative card responses. The mode, bankcode and field values differ for net banking (NB), UPI and wallets (CASH). */}

  <Callout icon="🚧" theme="warn">
    ### **Critical Rules**

    Browser redirects can be spoofed. Never mark an order as paid based on the redirect to `surl` alone. Always check the reverse hash and confirm the status with the Verify Payment API or a webhook.
  </Callout>

  **Expected output:** a verified payment status that you can safely record against the order.
</Accordion>

<Accordion title="Errors and Troubleshooting" icon="far fa-triangle-exclamation">
  **Invalid Hash**

  - Check the parameter order and the number of pipes.
  - Remove extra spaces and encode the string as UTF-8.
  - Make sure the salt is the one for the environment you're using (test or production).
  - Make sure the values in the hash match the values in the request exactly.

  **Payment doesn't start or the page shows an error**

  - Check the URL (`https://test.payu.in/_payment`) and that the request uses POST.
  - Check that `pg` and `bankcode` are present and that the payment method is enabled on your account.
  - Cards: check that all card fields are present and the expiry date isn't in the past.
  - UPI: check that `vpa` is a valid UPI ID.

  **Card payments are rejected straight away**

  - Your account may not be registered as PCI DSS compliant. Contact PayU, or use [PayU Hosted Checkout](doc:payu-hosted-checkout) for cards.

  **Success page shown, but the order isn't paid**

  - Don't rely on the browser redirect alone. Check the reverse hash and confirm with the Verify Payment API or a webhook.
</Accordion>

***

## Next Steps

<Cards columns="3">
  <Card title="Collect Payments with Cards" href="doc:collect-payments-with-cards-seamless" icon="fa-credit-card">
    Full card integration guide: build, test and go live.
  </Card>

  <Card title="Test the Integration" href="doc:test-integration" icon="fa-flask">
    Test scenarios and test credentials for every payment method.
  </Card>

  <Card title="Production Checklist" href="doc:integration-checklist-merchant-hosted-checkout" icon="fa-list-check">
    Everything to check before you go live.
  </Card>
</Cards>

{/* REVIEW: add links to the full net banking, UPI and wallet merchant-hosted guides once their slugs are confirmed. */}
