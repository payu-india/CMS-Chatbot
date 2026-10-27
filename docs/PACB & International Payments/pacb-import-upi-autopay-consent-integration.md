---
title: PACB Import - UPI Autopay Consent Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
<Banner color="#FFC107">Developer integration required</Banner>

Use this page to register a UPI Autopay mandate (the **consent transaction**) for a cross-border import subscription. The customer approves the mandate in their UPI app. After that, you can charge them on schedule with the [recurring transaction API](/docs/post-a-upi-recurring-transaction-cb) without asking them again.

<Cards columns="3">
  <Card title="1. Build the request" href="#step-1-build-the-consent-request">
    Parameters, UDFs and si_details
  </Card>

  <Card title="2. Generate the hash" href="#step-2-generate-the-hash">
    Server-side SHA-512
  </Card>

  <Card title="3. Post the request" href="#step-3-post-the-consent-request-to-payu">
    Call \_payment
  </Card>

  <Card title="4. Check the response" href="#step-4-check-the-response-from-payu">
    Initial and final responses
  </Card>

  <Card title="5. Verify the payment" href="#step-5-verify-the-payment">
    Confirm the mandate
  </Card>

  <Card title="6. Update UDFs and invoice" href="#step-6-update-udfs-and-upload-the-invoice">
    Post-payment compliance
  </Card>
</Cards>

<Callout icon="📘" theme="info">
  ### **Before you begin**

  - Your PayU account must be enabled for **Cross-Border Payments – Import** and for **UPI Autopay**. Contact your PayU Key Account Manager if it isn't.
  - Have your **key** and **salt** for the test environment. Keep the salt on your server only.
  - Collect the buyer's **PAN**, **date of birth** and **UPI ID (VPA)**, and generate an **invoice ID** for the order.
</Callout>

***

## Step 1: Build the consent request

<PaymentAPIEnvironment />

<Accordion title="Request parameters" icon="fa-list">
  <Tabs>
    <Tab title="Mandatory">
      | Parameter         | Description                                                                                                                                                     |
      | :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | `key`             | `String` Merchant key provided by PayU. For example, `JPM7Fg`.                                                                                                  |
      | `txnid`           | `String` Unique transaction ID that you generate for this order. Don't reuse it. For example, `ypl938459435`.                                                   |
      | `amount`          | `String` Amount charged when the customer approves the mandate. For example, `10.00`.                                                                           |
      | `productinfo`     | `String` Short description of the subscription. For example, `Magazine subscription`.                                                                           |
      | `firstname`       | `String` Customer's first name. For example, `Ashish`.                                                                                                          |
      | `lastname`        | `String` Customer's last name. For example, `Kumar`. {/* REVIEW (C23): confirm whether lastname is mandatory for UPI Autopay. */}                               |
      | `email`           | `String` Customer's email address. For example, `ashish.kumar@example.com`.                                                                                     |
      | `phone`           | `String` Customer's 10-digit mobile number. For example, `9876543210`.                                                                                          |
      | `address1`        | `String` First line of the billing address. Send accurate details: they help with fraud checks and chargebacks. For example, `34 Saikripa Estate, Tilak Nagar`. |
      | `address2`        | `String` Second line of the billing address. For example, `Near Metro Station`.                                                                                 |
      | `city`            | `String` Billing city. For example, `Mumbai`.                                                                                                                   |
      | `state`           | `String` Billing state. For example, `Maharashtra`.                                                                                                             |
      | `country`         | `String` Billing country. For example, `IN`. {/* REVIEW (C25): confirm the format. The PACB buyer-details spec uses ISO 3166-1 alpha-2. */}                     |
      | `zipcode`         | `String` 6-digit Indian PIN code of the billing address. For example, `400004`.                                                                                 |
      | `pg`              | `String` Payment category. Send `UPI`.                                                                                                                          |
      | `bankcode`        | `String` Payment option. Send `UPI` for UPI Autopay.                                                                                                            |
      | `vpa`             | `String` Customer's UPI ID. The mandate request is sent to this UPI ID. For example, `ashish@okaxis`.                                                           |
      | `si`              | `Integer` Set to `1` to register a mandate.                                                                                                                     |
      | `si_details`      | `JSON` Mandate details. See the **si_details** tab.                                                                                                             |
      | `api_version`     | `String` Send `7`. This version includes `si_details` in the hash.                                                                                              |
      | `txn_s2s_flow`    | `String` Send `4` for a server-to-server request.                                                                                                               |
      | `s2s_client_ip`   | `String` Customer's IP address. For example, `10.11.101.11`.                                                                                                    |
      | `s2s_device_info` | `String` Customer's browser user agent. For example, `Mozilla/5.0 (Windows NT 10.0; Win64; x64)`.                                                               |
      | `surl`            | `String` URL PayU sends the response to when the payment succeeds. For example, `<redacted URL>`.                                                               |
      | `furl`            | `String` URL PayU sends the response to when the payment fails. For example, `<redacted URL>`.                                                                  |
      | `hash`            | `String` SHA-512 hash generated on your server. See [Step 2](#step-2-generate-the-hash).                                                                        |
    </Tab>

    <Tab title="Cross-border UDFs">
      | Parameter | Description                                                                                                                                                                                                                                                                               |
      | :-------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | `udf1`    | `String` Buyer's PAN and date of birth, separated by two pipe characters: `PAN\|\|DOB`. The date format is `DD-MM-YYYY`. Mandatory if your AD bank asks for it. For example, `AAAPZ1234C\|\|22-08-1972`.                                                                                  |
      | `udf3`    | `String` Your invoice ID and the merchant name, separated by two pipe characters: `InvoiceID\|\|MerchantName`. Send the merchant name only if you're a payment aggregator collecting for another merchant. Mandatory if your AD bank asks for it. For example, `INV12345\|\|XYZ Pvt Ltd`. |
      | `udf4`    | `String` **Don't send this for UPI Autopay.** Leave it empty.                                                                                                                                                                                                                             |
      | `udf5`    | `String` Your invoice ID. You can also add it after the payment with the UDF Update API. For example, `INV12345`. {/* REVIEW: confirm whether udf5 is still needed when the invoice ID is already in udf3. */}                                                                            |

      <Callout icon="🚧" theme="warn">
        ### **Watch Out!**

        UPI Autopay uses a **different UDF format** from one-time cross-border payments. In one-time payments, `udf1` holds only the PAN, `udf3` holds only the date of birth, and `udf4` holds the end merchant name. Using the one-time format here will cause your invoice and buyer details to be recorded incorrectly.
      </Callout>
    </Tab>

    <Tab title="si_details">
      | Field              | Description                                                                                                                                                                             |
      | :----------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | `billingAmount`    | `String` Maximum amount you can debit in each recurring payment. For example, `200.00`.                                                                                                 |
      | `billingCurrency`  | `String` Send `INR`.                                                                                                                                                                    |
      | `billingCycle`     | `String` How often you'll debit the customer, for example `ADHOC`, `DAILY`, `WEEKLY`, `MONTHLY` or `YEARLY`. {/* REVIEW: confirm the billingCycle values supported for UPI Autopay. */} |
      | `billingInterval`  | `Integer` Number of billing cycles between debits. For example, `1`.                                                                                                                    |
      | `paymentStartDate` | `String` Date the mandate starts, in `YYYY-MM-DD` format. For example, `2026-11-01`.                                                                                                    |
      | `paymentEndDate`   | `String` Date the mandate ends, in `YYYY-MM-DD` format. It must be after `paymentStartDate`. For example, `2027-12-01`.                                                                 |

      For example:

      ```json
      {"billingAmount":"200.00","billingCurrency":"INR","billingCycle":"ADHOC","billingInterval":1,"paymentStartDate":"2026-11-01","paymentEndDate":"2027-12-01"}
      ```
    </Tab>
  </Tabs>
</Accordion>

**Expected output:** a complete set of request parameters, with `udf1` and `udf3` in the UPI Autopay format and `si_details` as a JSON string.

***

## Step 2: Generate the hash

Generate the hash on your server using SHA-512. For mandate registration with `api_version=7`, use this formula:

```plaintext
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|SALT)
```

<Callout icon="🚧" theme="warn">
  ### **Critical Rules**

  - Generate the hash on your server only. Never put your salt in a browser or app.
  - Use the **exact same** `si_details` string in the hash and in the request: same field order, no extra spaces or line breaks.
  - Keep six pipe characters between `udf5` and `si_details`. Leave unused UDFs empty, but keep their pipes.
</Callout>

<Accordion title="Hash code samples" icon="fa-code">
  ```javascript Node.js
  const crypto = require('crypto');

  function consentHash(p, salt) {
    const s = [p.key, p.txnid, p.amount, p.productinfo, p.firstname, p.email,
      p.udf1 || '', p.udf2 || '', p.udf3 || '', p.udf4 || '', p.udf5 || '',
      '', '', '', '', '', p.si_details, salt].join('|');
    return crypto.createHash('sha512').update(s).digest('hex');
  }
  ```

  ```php PHP
  <?php
  function consentHash(array $p, string $salt): string {
      $s = implode('|', [$p['key'], $p['txnid'], $p['amount'], $p['productinfo'], $p['firstname'], $p['email'],
          $p['udf1'] ?? '', $p['udf2'] ?? '', $p['udf3'] ?? '', $p['udf4'] ?? '', $p['udf5'] ?? '',
          '', '', '', '', '', $p['si_details'], $salt]);
      return hash('sha512', $s);
  }
  ```

  ```python Python
  import hashlib

  def consent_hash(p, salt):
      s = '|'.join([p['key'], p['txnid'], p['amount'], p['productinfo'], p['firstname'], p['email'],
                    p.get('udf1', ''), p.get('udf2', ''), p.get('udf3', ''), p.get('udf4', ''), p.get('udf5', ''),
                    '', '', '', '', '', p['si_details'], salt])
      return hashlib.sha512(s.encode('utf-8')).hexdigest()
  ```

  ```java Java
  import java.nio.charset.StandardCharsets;
  import java.security.MessageDigest;
  import java.util.Map;

  public class ConsentHash {
      public static String generate(Map<String, String> p, String salt) throws Exception {
          String s = String.join("|", p.get("key"), p.get("txnid"), p.get("amount"), p.get("productinfo"),
              p.get("firstname"), p.get("email"),
              p.getOrDefault("udf1", ""), p.getOrDefault("udf2", ""), p.getOrDefault("udf3", ""),
              p.getOrDefault("udf4", ""), p.getOrDefault("udf5", ""),
              "", "", "", "", "", p.get("si_details"), salt);
          byte[] d = MessageDigest.getInstance("SHA-512").digest(s.getBytes(StandardCharsets.UTF_8));
          StringBuilder hex = new StringBuilder();
          for (byte b : d) hex.append(String.format("%02x", b));
          return hex.toString();
      }
  }
  ```
</Accordion>

**Expected output:** a 128-character lowercase hexadecimal string.

***

## Step 3: Post the consent request to PayU

Post the parameters from your server to `_payment` as `application/x-www-form-urlencoded`.

<Accordion title="Sample request" icon="fa-code">
  ```curl cURL
  curl --location 'https://test.payu.in/_payment' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=JPM7Fg' \
  --data-urlencode 'txnid=ypl938459435' \
  --data-urlencode 'amount=10.00' \
  --data-urlencode 'productinfo=Magazine subscription' \
  --data-urlencode 'firstname=Ashish' \
  --data-urlencode 'lastname=Kumar' \
  --data-urlencode 'email=ashish.kumar@example.com' \
  --data-urlencode 'phone=9876543210' \
  --data-urlencode 'address1=34 Saikripa Estate, Tilak Nagar' \
  --data-urlencode 'address2=Near Metro Station' \
  --data-urlencode 'city=Mumbai' \
  --data-urlencode 'state=Maharashtra' \
  --data-urlencode 'country=IN' \
  --data-urlencode 'zipcode=400004' \
  --data-urlencode 'pg=UPI' \
  --data-urlencode 'bankcode=UPI' \
  --data-urlencode 'vpa=9999999999@upi' \
  --data-urlencode 'si=1' \
  --data-urlencode 'api_version=7' \
  --data-urlencode 'si_details={"billingAmount":"200.00","billingCurrency":"INR","billingCycle":"ADHOC","billingInterval":1,"paymentStartDate":"2026-11-01","paymentEndDate":"2027-12-01"}' \
  --data-urlencode 'udf1=AAAPZ1234C||22-08-1972' \
  --data-urlencode 'udf2=' \
  --data-urlencode 'udf3=INV12345||XYZ Pvt Ltd' \
  --data-urlencode 'udf4=' \
  --data-urlencode 'udf5=INV12345' \
  --data-urlencode 'txn_s2s_flow=4' \
  --data-urlencode 's2s_client_ip=10.11.101.11' \
  --data-urlencode 's2s_device_info=Mozilla/5.0 (Windows NT 10.0; Win64; x64)' \
  --data-urlencode 'surl=<redacted URL>' \
  --data-urlencode 'furl=<redacted URL>' \
  --data-urlencode 'hash=YOUR_GENERATED_HASH'
  ```

  ```javascript Node.js
  const params = {
    key: 'JPM7Fg', txnid: 'ypl938459435', amount: '10.00',
    productinfo: 'Magazine subscription', firstname: 'Ashish', lastname: 'Kumar',
    email: 'ashish.kumar@example.com', phone: '9876543210',
    address1: '34 Saikripa Estate, Tilak Nagar', address2: 'Near Metro Station',
    city: 'Mumbai', state: 'Maharashtra', country: 'IN', zipcode: '400004',
    pg: 'UPI', bankcode: 'UPI', vpa: '9999999999@upi', si: '1', api_version: '7',
    si_details: JSON.stringify({ billingAmount: '200.00', billingCurrency: 'INR', billingCycle: 'ADHOC',
      billingInterval: 1, paymentStartDate: '2026-11-01', paymentEndDate: '2027-12-01' }),
    udf1: 'AAAPZ1234C||22-08-1972', udf2: '', udf3: 'INV12345||XYZ Pvt Ltd', udf4: '', udf5: 'INV12345',
    txn_s2s_flow: '4', s2s_client_ip: '10.11.101.11', s2s_device_info: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    surl: '<redacted URL>', furl: '<redacted URL>'
  };
  params.hash = consentHash(params, process.env.PAYU_SALT); // from Step 2

  const res = await fetch('https://test.payu.in/_payment', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams(params)
  });
  console.log(await res.json());
  ```

  ```python Python
  import json, os, requests

  si_details = json.dumps({"billingAmount": "200.00", "billingCurrency": "INR", "billingCycle": "ADHOC",
                           "billingInterval": 1, "paymentStartDate": "2026-11-01",
                           "paymentEndDate": "2027-12-01"}, separators=(',', ':'))
  params = {
      "key": "JPM7Fg", "txnid": "ypl938459435", "amount": "10.00",
      "productinfo": "Magazine subscription", "firstname": "Ashish", "lastname": "Kumar",
      "email": "ashish.kumar@example.com", "phone": "9876543210",
      "address1": "34 Saikripa Estate, Tilak Nagar", "address2": "Near Metro Station",
      "city": "Mumbai", "state": "Maharashtra", "country": "IN", "zipcode": "400004",
      "pg": "UPI", "bankcode": "UPI", "vpa": "9999999999@upi", "si": "1", "api_version": "7",
      "si_details": si_details,
      "udf1": "AAAPZ1234C||22-08-1972", "udf2": "", "udf3": "INV12345||XYZ Pvt Ltd", "udf4": "", "udf5": "INV12345",
      "txn_s2s_flow": "4", "s2s_client_ip": "10.11.101.11",
      "s2s_device_info": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
      "surl": "<redacted URL>", "furl": "<redacted URL>",
  }
  params["hash"] = consent_hash(params, os.environ["PAYU_SALT"])  # from Step 2
  print(requests.post("https://test.payu.in/_payment", data=params).json())
  ```

  ```php PHP
  <?php
  $siDetails = json_encode(["billingAmount" => "200.00", "billingCurrency" => "INR", "billingCycle" => "ADHOC",
      "billingInterval" => 1, "paymentStartDate" => "2026-11-01", "paymentEndDate" => "2027-12-01"]);
  $params = [
      "key" => "JPM7Fg", "txnid" => "ypl938459435", "amount" => "10.00",
      "productinfo" => "Magazine subscription", "firstname" => "Ashish", "lastname" => "Kumar",
      "email" => "ashish.kumar@example.com", "phone" => "9876543210",
      "address1" => "34 Saikripa Estate, Tilak Nagar", "address2" => "Near Metro Station",
      "city" => "Mumbai", "state" => "Maharashtra", "country" => "IN", "zipcode" => "400004",
      "pg" => "UPI", "bankcode" => "UPI", "vpa" => "9999999999@upi", "si" => "1", "api_version" => "7",
      "si_details" => $siDetails,
      "udf1" => "AAAPZ1234C||22-08-1972", "udf2" => "", "udf3" => "INV12345||XYZ Pvt Ltd", "udf4" => "", "udf5" => "INV12345",
      "txn_s2s_flow" => "4", "s2s_client_ip" => "10.11.101.11",
      "s2s_device_info" => "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
      "surl" => "<redacted URL>", "furl" => "<redacted URL>",
  ];
  $params["hash"] = consentHash($params, getenv("PAYU_SALT")); // from Step 2

  $ch = curl_init("https://test.payu.in/_payment");
  curl_setopt_array($ch, [CURLOPT_POST => true, CURLOPT_RETURNTRANSFER => true,
      CURLOPT_POSTFIELDS => http_build_query($params)]);
  echo curl_exec($ch);
  curl_close($ch);
  ```
</Accordion>

**Expected output:** a JSON response from PayU. The customer receives a mandate request in the UPI app linked to the `vpa` you sent.

***

## Step 4: Check the response from PayU

You receive two responses: an **initial response** to your request, and a **final response** posted to your `surl` or `furl` after the customer approves or declines the mandate.

<Accordion title="Initial response (to your _payment request)" icon="fa-reply">
  {/* REVIEW: these error structures are confirmed for UPI S2S (txn_s2s_flow=4) payments. Confirm the pending response for UPI Autopay collect. */}

  <Tabs>
    <Tab title="Success: mandate request sent">
      ```json
      {
        "metaData": {
          "message": null,
          "referenceId": "<encoded PayU reference>",
          "statusCode": null,
          "txnId": "ypl938459435",
          "txnStatus": "pending",
          "unmappedStatus": "pending"
        },
        "result": {
          "paymentId": "403993715525317379"
        }
      }
      ```
    </Tab>

    <Tab title="Error: request rejected">
      ```json
      {
        "metaData": {
          "message": "Merchant Integration Exception occurred",
          "referenceId": "<encoded PayU reference>",
          "statusCode": "EX158",
          "txnId": "ypl938459435",
          "txnStatus": "failed",
          "unmappedStatus": "failure"
        },
        "result": {}
      }
      ```
    </Tab>

    <Tab title="Failure: payment gateway down">
      ```json
      {
        "metaData": {
          "message": "Payment gateway seems to be down at this moment.",
          "referenceId": "<encoded PayU reference>",
          "statusCode": "E803",
          "txnId": "ypl938459435",
          "txnStatus": "failed",
          "unmappedStatus": "failure"
        }
      }
      ```
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Final response (posted to surl or furl)" icon="fa-flag-checkered">
  PayU posts the final response as form data. Below it's shown parsed as JSON.

  <Tabs>
    <Tab title="Success: mandate approved">
      ```json
      {
        "mihpayid": "403993715525317379",
        "mode": "UPI",
        "status": "success",
        "unmappedstatus": "captured",
        "key": "JPM7Fg",
        "txnid": "ypl938459435",
        "amount": "10.00",
        "discount": "0.00",
        "net_amount_debit": "10",
        "productinfo": "Magazine subscription",
        "firstname": "Ashish",
        "lastname": "Kumar",
        "email": "ashish.kumar@example.com",
        "phone": "9876543210",
        "udf1": "AAAPZ1234C||22-08-1972",
        "udf3": "INV12345||XYZ Pvt Ltd",
        "udf4": "",
        "udf5": "INV12345",
        "field1": "9999999999@upi",
        "field7": "Mandate Request Approved",
        "field9": "MD202|Mandate Request Approved",
        "payment_source": "sist",
        "PG_TYPE": "UPI-PG",
        "bank_ref_num": "<bank reference>",
        "bankcode": "UPI",
        "error": "E000",
        "error_Message": "No Error",
        "hash": "<response hash>"
      }
      ```
    </Tab>

    <Tab title="Failure: mandate not approved">
      {/* REVIEW: illustrative. Confirm the field9 and error values when the customer declines or the request expires. */}

      ```json
      {
        "mihpayid": "403993715525317380",
        "mode": "UPI",
        "status": "failure",
        "unmappedstatus": "failed",
        "key": "JPM7Fg",
        "txnid": "ypl938459436",
        "amount": "10.00",
        "net_amount_debit": "0",
        "productinfo": "Magazine subscription",
        "firstname": "Ashish",
        "email": "ashish.kumar@example.com",
        "field9": "<reason, for example declined or expired in the UPI app>",
        "payment_source": "sist",
        "bankcode": "UPI",
        "error": "<error code>",
        "error_Message": "<error message>",
        "hash": "<response hash>"
      }
      ```
    </Tab>
  </Tabs>

  <Callout icon="🚧" theme="warn">
    ### **Critical Rules**

    - Check the reverse hash before you update the order. Browser and server callbacks can be spoofed. {/* REVIEW: confirm whether si_details is part of the response hash. */}
    - Mark the mandate as active only when `status` is `success` and `unmappedstatus` is `captured`.
    - **Save&#x20;**`mihpayid`**.** You send it as `authpayuid` when you charge the customer with the [recurring transaction API](/docs/post-a-upi-recurring-transaction-cb).
  </Callout>
</Accordion>

**Expected output:** an approved mandate, with `mihpayid` saved against the customer's subscription.

***

## Step 5: Verify the payment

Don't rely only on the redirect. Confirm the result with a webhook or the Verify Payment API before you activate the subscription.

<Verify_Payment_Tabs />

**Expected output:** Verify Payment returns `status` as `success` for your `txnid`.

***

## Step 6: Update UDFs and upload the invoice

If you didn't send the buyer details or invoice ID in the request, add them with the UDF Update API. Keep the UPI Autopay format (`PAN||DOB` in `udf1`, `InvoiceID||MerchantName` in `udf3`).

Then upload the invoice with the Invoice Upload API. Merchants selling goods must also upload the airway bill (AWB).

<Callout icon="🚧" theme="warn">
  ### **Watch Out!**

  Upload invoices **within 10 days** of the payment. If PayU doesn't receive them, your next settlement may be put on hold.
</Callout>

**Expected output:** the transaction has complete buyer and invoice details, and is ready for settlement.

***

## Test your integration

| What to test               | Test value                                                                 |
| :------------------------- | :------------------------------------------------------------------------- |
| UPI ID                     | `9999999999@upi`                                                           |
| Consent amount             | At least `2.00`                                                            |
| `si_details.billingAmount` | At least `200.00`                                                          |
| Successful mandate         | Approve the request and check that the final response has `status=success` |
| Failed mandate             | Decline the request and check that your `furl` handles it                  |

***

## Common first-time errors

| Problem                                   | Likely cause                                                              | Fix                                                                                       |
| :---------------------------------------- | :------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------- |
| Hash mismatch                             | `si_details` in the hash differs from the request, or the pipes are wrong | Use the same `si_details` string in both, and keep six pipes before it                    |
| `EX158`                                   | A mandatory parameter is missing or invalid                               | Check the request against the Mandatory tab                                               |
| Buyer or invoice details recorded wrongly | One-time UDF format used                                                  | Use `PAN\|\|DOB` in `udf1`, `InvoiceID\|\|MerchantName` in `udf3`, and leave `udf4` empty |
| Customer doesn't get the mandate request  | Wrong or unsupported UPI ID                                               | Validate the VPA for UPI Autopay before you send the request                              |
| Settlement on hold                        | Invoice not uploaded within 10 days                                       | Upload the invoice (and AWB for goods)                                                    |

***

## Next Steps

<Cards columns="3">
  <Card title="Charge the customer" href="/docs/post-a-upi-recurring-transaction-cb">
    Send pre-debit notifications and recurring debits.
  </Card>

  <Card title="How it works" href="/docs/workflow-for-cross-border-payments-import">
    Understand the cross-border import flow.
  </Card>

  <Card title="FAQs" href="/docs/faqs-for-cross-border-payments">
    Answers to common questions.
  </Card>
</Cards>
