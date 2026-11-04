---
title: PACB Imports -  Webhooks & Security
deprecated: false
hidden: true
metadata:
  robots: index
---
<Banner color="#FFC107">Integration Guide: Server-to-Server (S2S) Webhooks & Security</Banner>

In Cross-Border Payments – Import (PACB), client-side browser redirects (`surl`/`furl`) are subject to consumer network drops, browser crashes, or tab closures. **Server-to-Server (S2S) Webhooks serve as the authoritative single source of truth** for triggering automated downstream actions:

1. Updating order status to **Paid / Captured**.
2. Initiating automated commercial invoice PDF generation and upload within the mandatory 10-day window.
3. Managing virtual account inward remittance holds.

<Callout icon="🛡️" theme="warning">
  ### **Critical Security Rule:**

  Never fulfill an order or mark goods as shipped based solely on browser redirects (`surl`). Always verify the cryptographic `hash` included in the PayU S2S webhook on your secure server backend before processing fulfillment.
</Callout>

***

## Canonical Webhook Payloads by Flow

<Tabs>
  <Tab title="One-Time Checkout (Cards / NB / UPI Intent)">
    Triggered immediately upon completion of customer payment authorization:

    ```json
    {
      "mihpayid": "403993715530123456",
      "mode": "CC",
      "status": "success",
      "unmappedstatus": "captured",
      "key": "YOUR_MERCHANT_KEY",
      "txnid": "PACB_TXN_1730708400",
      "amount": "1500.00",
      "cardCategory": "domestic",
      "discount": "0.00",
      "net_amount_debit": "1500.00",
      "addedon": "2026-11-04 13:45:02",
      "productinfo": "Digital Goods Cross-Border",
      "firstname": "Aarav",
      "lastname": "Sharma",
      "address1": "123 MG Road",
      "city": "Bengaluru",
      "state": "Karnataka",
      "country": "IN",
      "zipcode": "560001",
      "email": "aarav.sharma@example.com",
      "phone": "9876543210",
      "udf1": "ABCDE1234F",
      "udf2": "Order_Ref_8872",
      "udf3": "15-08-1988",
      "udf4": "Global Tech Services Ltd",
      "udf5": "INV-2026-1104",
      "field9": "Success",
      "bank_ref_num": "630912345678",
      "bankcode": "VISA",
      "error": "E000",
      "error_Message": "No Error",
      "hash": "d13f9c3132e4876b5b54687258be0a59750d4eb066d7adbc0d984534f3b1456209e7de7db939efbd1bbab66cb4b5b2e987c2f0bf571bb21e35d1d6a7f805a911"
    }
    ```
  </Tab>

  <Tab title="UPI Autopay Mandate (Consent)">
    Triggered when the Indian customer authorizes the recurring payment mandate in their UPI app:

    ```json
    {
      "mihpayid": "403993715530987654",
      "mode": "UPI",
      "status": "success",
      "unmappedstatus": "captured",
      "key": "YOUR_MERCHANT_KEY",
      "txnid": "PACB_SI_1730708500",
      "amount": "2.00",
      "productinfo": "SaaS Subscription Cross-Border",
      "firstname": "Aarav",
      "email": "aarav.sharma@example.com",
      "phone": "9876543210",
      "udf1": "ABCDE1234F||15-08-1988",
      "udf2": "",
      "udf3": "INV-2026-1104||GlobalTechLtd",
      "udf4": "",
      "udf5": "INV-2026-1104",
      "field9": "MD202: Mandate successfully created",
      "bank_ref_num": "630987654321",
      "bankcode": "UPI",
      "error": "E000",
      "error_Message": "Mandate registered successfully",
      "hash": "4a7b7468153b6cbbe152914bbd2df80a97bfa923053ad63a6dc91456cbbcf82b545f448bdf129753e19876efcad1b899d21396ebf45612803b01a1c97a2948bb"
    }
    ```

    <Callout icon="💡" theme="info">
      ### **Key Value to Store:**

      For UPI Autopay, persist the returned `mihpayid` (e.g., `403993715530987654`). This value serves as the `authpayuid` (`var1`) required to execute all subsequent recurring debits via `command=siTransaction`.
    </Callout>
  </Tab>

  <Tab title="UPI Autopay Recurring Debit Execution">
    Triggered when a scheduled recurring subscription debit executes against the active mandate:

    ```json
    {
      "mihpayid": "403993715531555666",
      "mode": "UPI",
      "status": "success",
      "unmappedstatus": "captured",
      "key": "YOUR_MERCHANT_KEY",
      "txnid": "PACB_REC_1733300400",
      "amount": "499.00",
      "discount": "0.00",
      "net_amount_debit": "499.00",
      "addedon": "2026-12-04 10:15:00",
      "productinfo": "Monthly SaaS Plan",
      "firstname": "Aarav",
      "email": "aarav.sharma@example.com",
      "phone": "9876543210",
      "udf1": "ABCDE1234F||15-08-1988",
      "udf3": "INV-2026-1204||GlobalTechLtd",
      "udf5": "INV-2026-1204",
      "bank_ref_num": "633455112233",
      "bankcode": "UPI",
      "error": "E000",
      "error_Message": "Recurring transaction successful",
      "hash": "e6a2bc45012399887766554433221100aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"
    }
    ```
  </Tab>

  <Tab title="Virtual Account Wire Remittance">
    Triggered when funds clear into the merchant's dedicated Nodal Virtual Account via NEFT or RTGS:

    ```json
    {
      "event": "PAYMENT_CAPTURED",
      "subMerchantId": "SM_GLOBAL_102",
      "virtualAccountId": "PAYUVAGLOBAL102",
      "remittanceTxnId": "AXISN26309187654",
      "amount": "450000.00",
      "currency": "INR",
      "payerName": "Indian Enterprise Pvt Ltd",
      "payerAccountNumber": "918010045678901",
      "payerIfsc": "UTIB0000045",
      "paymentMode": "RTGS",
      "utrNumber": "AXISN26309187654",
      "settlementHold": true,
      "holdReason": "PENDING_INVOICE_SUBMISSION",
      "timestamp": "2026-11-04T13:46:10+05:30"
    }
    ```
  </Tab>
</Tabs>

***

## Cryptographic Reverse Hash Verification

To verify that the webhook was genuinely issued by PayU and has not been intercepted or tampered with, your server must calculate the SHA-512 reverse hash and compare it with the `hash` field provided in the payload.

### The Reverse Hash Formula

The response hash sequence reverses the request sequence, placing `SALT` and `status` at the beginning, followed by the UDFs in reverse order (`udf5` down to `udf1`):

#### 1. Standard Reverse Hash Sequence

```text
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

#### 2. Sequence When `additional_charges` Are Present

If convenience fees or dynamic surcharges were applied by PayU, the `additional_charges` parameter is prepended:

```text
sha512(additional_charges|SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

<Callout icon="⚠️" theme="warning">
  ### **Notice on Empty Pipes:**

  Notice the six consecutive empty pipes `||||||` between `status` and `udf5`. These represent empty fields in the reverse string and must be maintained exactly.
</Callout>

***

## Multi-Language Signature Verification Code

<Tabs>
  <Tab title="Node.js">
    ```javascript
    const crypto = require('crypto');

    /**
     * Validates the cryptographic SHA-512 signature of a PayU webhook payload.
     * @param {Object} payload - Parsed JSON or form body received from PayU.
     * @param {string} merchantSalt - Your merchant API Salt.
     * @returns {boolean} True if signature is authentic, false otherwise.
     */
    function verifyPayUSignature(payload, merchantSalt) {
      const {
        additional_charges,
        status = '',
        udf5 = '',
        udf4 = '',
        udf3 = '',
        udf2 = '',
        udf1 = '',
        email = '',
        firstname = '',
        productinfo = '',
        amount = '',
        txnid = '',
        key = '',
        hash: receivedHash = ''
      } = payload;

      let hashSequence = '';
      if (additional_charges) {
        hashSequence = `${additional_charges}|${merchantSalt}|${status}||||||${udf5}|${udf4}|${udf3}|${udf2}|${udf1}|${email}|${firstname}|${productinfo}|${amount}|${txnid}|${key}`;
      } else {
        hashSequence = `${merchantSalt}|${status}||||||${udf5}|${udf4}|${udf3}|${udf2}|${udf1}|${email}|${firstname}|${productinfo}|${amount}|${txnid}|${key}`;
      }

      const calculatedHash = crypto
        .createHash('sha512')
        .update(hashSequence, 'utf-8')
        .digest('hex');

      return calculatedHash.toLowerCase() === receivedHash.toLowerCase();
    }

    // Express.js Route Example
    app.post('/api/payu/webhook', (req, res) => {
      const merchantSalt = process.env.PAYU_MERCHANT_SALT;
      const isValid = verifyPayUSignature(req.body, merchantSalt);

      if (!isValid) {
        console.error('Invalid PayU Webhook Signature. Rejecting request.');
        return res.status(400).send('Signature verification failed');
      }

      // Idempotently process fulfillment and invoice upload
      if (req.body.status === 'success') {
        handleSuccessfulPayment(req.body);
      }

      // Return HTTP 200 OK immediately to acknowledge receipt
      return res.status(200).json({ status: 'ACK' });
    });
    ```
  </Tab>

  <Tab title="Python">
    ```python
    import hashlib
    import os

    def verify_payu_signature(payload: dict, merchant_salt: str) -> bool:
        """
        Validates the SHA-512 reverse hash signature of an incoming PayU webhook.
        """
        additional_charges = payload.get("additional_charges")
        status = payload.get("status", "")
        udf5 = payload.get("udf5", "")
        udf4 = payload.get("udf4", "")
        udf3 = payload.get("udf3", "")
        udf2 = payload.get("udf2", "")
        udf1 = payload.get("udf1", "")
        email = payload.get("email", "")
        firstname = payload.get("firstname", "")
        productinfo = payload.get("productinfo", "")
        amount = payload.get("amount", "")
        txnid = payload.get("txnid", "")
        key = payload.get("key", "")
        received_hash = payload.get("hash", "").lower()

        if additional_charges:
            hash_seq = f"{additional_charges}|{merchant_salt}|{status}||||||{udf5}|{udf4}|{udf3}|{udf2}|{udf1}|{email}|{firstname}|{productinfo}|{amount}|{txnid}|{key}"
        else:
            hash_seq = f"{merchant_salt}|{status}||||||{udf5}|{udf4}|{udf3}|{udf2}|{udf1}|{email}|{firstname}|{productinfo}|{amount}|{txnid}|{key}"

        calculated_hash = hashlib.sha512(hash_seq.encode('utf-8')).hexdigest().lower()
        return calculated_hash == received_hash

    # FastAPI / Flask endpoint example
    @app.post("/api/payu/webhook")
    async def payu_webhook(request: Request):
        payload = await request.form()
        salt = os.getenv("PAYU_MERCHANT_SALT")
        
        if not verify_payu_signature(dict(payload), salt):
            raise HTTPException(status_code=400, detail="Invalid signature")
            
        if payload.get("status") == "success":
            process_order_fulfillment(payload)
            
        return {"status": "SUCCESS"}
    ```
  </Tab>

  <Tab title="PHP">
    ```php
    <?php
    /**
     * Verifies PayU S2S Webhook signature.
     */
    function verifyPayUSignature($payload, $merchantSalt) {
        $additionalCharges = $payload['additional_charges'] ?? '';
        $status            = $payload['status'] ?? '';
        $udf5              = $payload['udf5'] ?? '';
        $udf4              = $payload['udf4'] ?? '';
        $udf3              = $payload['udf3'] ?? '';
        $udf2              = $payload['udf2'] ?? '';
        $udf1              = $payload['udf1'] ?? '';
        $email             = $payload['email'] ?? '';
        $firstname         = $payload['firstname'] ?? '';
        $productinfo       = $payload['productinfo'] ?? '';
        $amount            = $payload['amount'] ?? '';
        $txnid             = $payload['txnid'] ?? '';
        $key               = $payload['key'] ?? '';
        $receivedHash      = strtolower($payload['hash'] ?? '');

        if (!empty($additionalCharges)) {
            $hashSeq = "{$additionalCharges}|{$merchantSalt}|{$status}||||||{$udf5}|{$udf4}|{$udf3}|{$udf2}|{$udf1}|{$email}|{$firstname}|{$productinfo}|{$amount}|{$txnid}|{$key}";
        } else {
            $hashSeq = "{$merchantSalt}|{$status}||||||{$udf5}|{$udf4}|{$udf3}|{$udf2}|{$udf1}|{$email}|{$firstname}|{$productinfo}|{$amount}|{$txnid}|{$key}";
        }

        $calculatedHash = strtolower(hash('sha512', $hashSeq));
        return ($calculatedHash === $receivedHash);
    }

    // Processing Webhook POST
    $merchantSalt = getenv('PAYU_MERCHANT_SALT');
    $postData = $_POST;

    if (!verifyPayUSignature($postData, $merchantSalt)) {
        http_response_code(400);
        echo json_encode(["error" => "Invalid signature"]);
        exit();
    }

    if (($postData['status'] ?? '') === 'success') {
        // Process order fulfillment & invoice compliance
        fulfillOrder($postData);
    }

    http_response_code(200);
    echo json_encode(["status" => "ACK"]);
    ?>
    ```
  </Tab>

  <Tab title="Java">
    ```java
    import java.nio.charset.StandardCharsets;
    import java.security.MessageDigest;
    import java.util.Map;

    public class PayUWebhookValidator {

        public static boolean verifySignature(Map<String, String> payload, String salt) {
            String additionalCharges = payload.getOrDefault("additional_charges", "");
            String status = payload.getOrDefault("status", "");
            String udf5 = payload.getOrDefault("udf5", "");
            String udf4 = payload.getOrDefault("udf4", "");
            String udf3 = payload.getOrDefault("udf3", "");
            String udf2 = payload.getOrDefault("udf2", "");
            String udf1 = payload.getOrDefault("udf1", "");
            String email = payload.getOrDefault("email", "");
            String firstname = payload.getOrDefault("firstname", "");
            String productinfo = payload.getOrDefault("productinfo", "");
            String amount = payload.getOrDefault("amount", "");
            String txnid = payload.getOrDefault("txnid", "");
            String key = payload.getOrDefault("key", "");
            String receivedHash = payload.getOrDefault("hash", "").toLowerCase();

            String hashSeq;
            if (additionalCharges != null && !additionalCharges.isEmpty()) {
                hashSeq = String.format("%s|%s|%s||||||%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s",
                    additionalCharges, salt, status, udf5, udf4, udf3, udf2, udf1, email, firstname, productinfo, amount, txnid, key);
            } else {
                hashSeq = String.format("%s|%s||||||%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s",
                    salt, status, udf5, udf4, udf3, udf2, udf1, email, firstname, productinfo, amount, txnid, key);
            }

            try {
                MessageDigest md = MessageDigest.getInstance("SHA-512");
                byte[] digest = md.digest(hashSeq.getBytes(StandardCharsets.UTF_8));
                StringBuilder sb = new StringBuilder();
                for (byte b : digest) {
                    sb.append(String.format("%02x", b));
                }
                return sb.toString().equalsIgnoreCase(receivedHash);
            } catch (Exception e) {
                return false;
            }
        }
    }
    ```
  </Tab>

  <Tab title="C#">
    ```csharp
    using System;
    using System.Collections.Generic;
    using System.Security.Cryptography;
    using System.Text;

    public class PayUWebhookValidator
    {
        public static bool VerifySignature(Dictionary<string, string> payload, string salt)
        {
            payload.TryGetValue("additional_charges", out string additionalCharges);
            payload.TryGetValue("status", out string status);
            payload.TryGetValue("udf5", out string udf5);
            payload.TryGetValue("udf4", out string udf4);
            payload.TryGetValue("udf3", out string udf3);
            payload.TryGetValue("udf2", out string udf2);
            payload.TryGetValue("udf1", out string udf1);
            payload.TryGetValue("email", out string email);
            payload.TryGetValue("firstname", out string firstname);
            payload.TryGetValue("productinfo", out string productinfo);
            payload.TryGetValue("amount", out string amount);
            payload.TryGetValue("txnid", out string txnid);
            payload.TryGetValue("key", out string key);
            payload.TryGetValue("hash", out string receivedHash);

            string hashSeq;
            if (!string.IsNullOrEmpty(additionalCharges))
            {
                hashSeq = $"{additionalCharges}|{salt}|{status}||||||{udf5}|{udf4}|{udf3}|{udf2}|{udf1}|{email}|{firstname}|{productinfo}|{amount}|{txnid}|{key}";
            }
            else
            {
                hashSeq = $"{salt}|{status}||||||{udf5}|{udf4}|{udf3}|{udf2}|{udf1}|{email}|{firstname}|{productinfo}|{amount}|{txnid}|{key}";
            }

            using (SHA512 sha512 = SHA512.Create())
            {
                byte[] bytes = sha512.ComputeHash(Encoding.UTF8.GetBytes(hashSeq));
                StringBuilder sb = new StringBuilder();
                foreach (byte b in bytes)
                {
                    sb.Append(b.ToString("x2"));
                }
                return string.Equals(sb.ToString(), receivedHash, StringComparison.OrdinalIgnoreCase);
            }
        }
    }
    ```
  </Tab>
</Tabs>

***

## Webhook Operational Best Practices

### 1. Respond with Immediate HTTP 200 OK

* PayU expects an HTTP `200 OK` status response from your webhook endpoint within **5 seconds**.
* If your endpoint times out, returns HTTP 5xx, or experiences network interruptions, PayU's webhook retry scheduler will re-attempt delivery at increasing exponential backoff intervals.
* **Architecture Pattern**: Decouple signature verification from heavy processing. Verify the signature, queue the event into an internal job queue (e.g., Redis / SQS), and return HTTP `200 OK` immediately.

### 2. Implement Strict Idempotency

* Network retries mean your server may receive duplicate webhook deliveries for the same `txnid` or `mihpayid`.
* Store incoming transaction IDs in an atomic cache or transactional database table with a unique constraint. If a webhook arrives for an already processed `txnid`, verify the hash and return `200 OK` without duplicating inventory deduction, customer messaging, or invoice generation.

### 3. Automated Reconciliation via Verify Payment API

* Webhooks should be complemented with an automated reconciliation cron job.
* If no webhook has been received within **5 to 10 minutes** of a user initiating checkout, invoke the server-to-server **Verify Payment API** (`verify_payment`) using `txnid` to fetch authoritative terminal state.

***

## Next Steps

<Cards columns="3">
  <Card title="Mandatory Parameters" href="/docs/pacb-mandatory-cross-border-parameters">
    Review regulatory KYC, trade UDFs, and formatting rules.
  </Card>

  <Card title="Errors & Troubleshooting" href="/docs/pacb-error-map-and-resolutions">
    Resolve reverse hash mismatches and signature verification errors.
  </Card>

  <Card title="PACB Best Practices" href="/docs/cross-border-payments-import-best-practices">
    Explore the automated 10-day invoice compliance pipeline.
  </Card>
</Cards>
