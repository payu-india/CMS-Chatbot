---
name: PACB_Cards_Step2
---
## Step 2: Handle the Initiate Response from PayU

After posting the payment request, PayU returns a response containing transaction status and next steps for 3DS authentication.

<Accordion title="Response Parameters" icon="fa-table">
  | Parameter                | Description                                                                | Example                                                            |
  | ------------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------------------ |
  | metaData                 | `Object`<br />JSON object containing transaction metadata.                 | -                                                                  |
  | metaData.referenceId     | `String`<br />PayU reference ID to be sent back in subsequent calls.       | `5a3e7cb9884e003dce1f28f965478a9a12fb9244fc15be91b0b3de48763a12e7` |
  | metaData.txnId           | `String`<br />Merchant's transaction ID.                                   | `payuTestTransaction12345`                                         |
  | metaData.txnStatus       | `String`<br />Transaction status (e.g., "Enrolled").                       | `Enrolled`                                                         |
  | metaData.unmappedStatus  | `String`<br />Status for flow control: `pending`, `captured`, or `failed`. | `pending`                                                          |
  | result.otpPostUrl        | `String`<br />URL to post OTP for verification.                            | `https://test.payu.in/ResponseHandler.php`                         |
  | result.acsTemplate       | `String`<br />Base64 encoded HTML form for bank ACS redirect.              | `PGh0bWw+PGJvZHk+...`                                              |
  | binData.pureS2SSupported | `Boolean`<br />Whether native S2S OTP flow is supported.                   | `true`                                                             |
  | binData.issuingBank      | `String`<br />Card issuing bank.                                           | `AXIS`                                                             |
  | binData.category         | `String`<br />Card category (`creditcard` or `debitcard`).                 | `creditcard`                                                       |
  | binData.cardType         | `String`<br />Card network (`VISA`, `MAST`, `RUPAY`).                      | `MAST`                                                             |
  | binData.isDomestic       | `Boolean`<br />Whether the card is domestic.                               | `true`                                                             |
</Accordion>

<Accordion title="Sample Response" icon="fa-code">
  ```json
  {
    "metaData": {
      "message": null,
      "referenceId": "5a3e7cb9884e003dce1f28f965478a9a12fb9244fc15be91b0b3de48763a12e7",
      "statusCode": null,
      "txnId": "payuTestTransaction12345",
      "txnStatus": "Enrolled",
      "unmappedStatus": "pending",
      "resendOtp": {
        "isSupported": true,
        "attemptsLeft": 2
      },
      "submitOtp": {
        "attemptsLeft": 3
      }
    },
    "result": {
      "otpPostUrl": "https://test.payu.in/ResponseHandler.php",
      "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0i..."
    },
    "binData": {
      "pureS2SSupported": true,
      "issuingBank": "AXIS",
      "category": "creditcard",
      "cardType": "MAST",
      "isDomestic": true
    }
  }
  ```
</Accordion>

<Callout icon="📘" theme="info">
  **Redirect** the customer using the result.acsTemplate(base64encoded) to their bank's page for authentication. The final response will be posted to surl/furl and the configured Webhook.
</Callout>

<Accordion title="Submit OTP and Resend OTP" icon="fa-reply">
  For S2S4 flow, you'll receive an OTP enrollment response if the card requires OTP authentication. Use the Submit OTP API and Resend OTP API (if the OTP entered by the customer fails). For more information refer to (Submit OTP API)\[ref:submit-otp-to-payu] and (Resend OTP API)\[ref:resend-otp-api].

  <Accordion title="Sample response from Submit OTP" icon="fa-code">
    **First failure**

    ```json
    { 
    "metaData": { 
        "message": "OTP invalid. 2 retry attempts left out of 3", 
        "referenceId": "3d954a723bbb920cee8b0975556f115957ca9992514e4810c859365f0666b044", 
        "statusCode": null, 
        "txnId": "my_order_13975", 
        "unmappedStatus": "pending", 
        "submitOtp": { 
            "status": "failed", 
            "attemptsLeft": 2 
        } 
    }, 
    "result": {} 
    } 
    ```

    **Second failure**

    ```json
    { 
    "metaData": { 
        "message": "OTP invalid. 1 retry attempts left out of 3", 
        "referenceId": "3d954a723bbb920cee8b0975556f115957ca9992514e4810c859365f0666b044", 
        "statusCode": null, 
        "txnId": "my_order_13975", 
        "unmappedStatus": "pending", 
        "submitOtp": { 
            "status": "failed", 
            "attemptsLeft": 1 
        } 
    }, 
    "result": {} 
    } 
    ```

    **Third attempt (success)**, any further attempt for SUBMIT/RESEND OTP, when the unmapped status reached to success/failure will provide the final result as below JSON only.

    ```json
    { 
    "metaData": { 
        "message": "No Error", 
        "referenceId": "3d954a723bbb920cee8b0975556f115957ca9992514e4810c859365f0666b044", 
        "statusCode": "E000", 
        "txnId": "my_order_13975", 
        "unmappedStatus": "success", 
        "submitOtp": { 
            "status": "success" 
        } 
    }, 
    "result": { 
        "mihpayid": "403993715534252033", 
        "mode": "CC", 
        "status": "success", 
        "key": "PRiQvJ", 
        "txnid": "my_order_13975", 
        "amount": "2.00", 
        "addedon": "2025-07-03 19:12:46", 
        "productinfo": "asfas", 
        "firstname": "sudhanshu", 
        "lastname": "", 
        "address1": "", 
        "address2": "", 
        "city": "", 
        "state": "", 
        "country": "", 
        "zipcode": "", 
        "email": "test@test.com", 
        "phone": "9999999999", 
        "udf1": "<optional>", 
        "udf2": "<optional>", 
        "udf3": "<optional>", 
        "udf4": "<optional>", 
        "udf5": "", 
        "udf6": "", 
        "udf7": "", 
        "udf8": "", 
        "udf9": "", 
        "udf10": "", 
        "card_token": "", 
        "card_no": "XXXXXXXXXXXX0008", 
        "field0": "", 
        "field1": "766301020057097000", 
        "field2": "466683", 
        "field3": "2.00", 
        "field4": "", 
        "field5": "00", 
        "field6": "02", 
        "field7": "AUTHPOSITIVE", 
        "field8": "AUTHORIZED", 
        "field9": "Transaction is Successful", 
        "payment_source": "payuPureS2S", 
        "PG_TYPE": "CC-PG", 
        "error": "E000", 
        "error_Message": "No Error", 
        "issuing_bank": "YES", 
        "card_type": "MAST", 
        "cardToken": "", 
        "net_amount_debit": "2", 
        "discount": "0.00", 
        "offer_key": "", 
        "offer_availed": "", 
        "unmappedstatus": "captured", 
        "hash": "67d5aa0304a0699ab0764d157d362074f4cfd54178abd060e1f53850b6b1445a9627dd17c679c0902d74f5c03718e5e8ce32ef836d175786ef42c372a43801fa", 
        "bank_ref_no": "766301020057097000", 
        "bank_ref_num": "766301020057097000", 
        "bankcode": "CC", 
        "surl": "https://test.payu.in/admin/test_response", 
        "curl": "https://test.payu.in/admin/test_response", 
        "furl": "https://test.payu.in/admin/test_response", 
        "card_hash": "46261359f70225c5ed11ef395058f3b2f7d003280bb4feb2f21e41aac113a252", 
        "threeDSVersion": "2.2.0" 
    } 
    } 
    ```
  </Accordion>

  <Accordion title="Resend OTP" icon="fa-code">
    **First resend**

    ```json
    { 
    "metaData": { 
        "message": null, 
        "referenceId": "3d954a723bbb920cee8b0975556f115957ca9992514e4810c859365f0666b044", 
        "statusCode": null, 
        "txnId": "my_order_13975", 
        "unmappedStatus": "pending", 
        "resendOtp": { 
            "status": "success", 
            "attemptsLeft": 1 
        } 
    }, 
    "result": {} 
    } 
    ```

    **Second resend**

    ```json
    { 
        "metaData": { 
            "message": null, 
            "referenceId": "3d954a723bbb920cee8b0975556f115957ca9992514e4810c859365f0666b044", 
            "statusCode": null, 
            "txnId": "my_order_13975", 
            "unmappedStatus": "pending", 
            "resendOtp": { 
                "status": "success", 
                "attemptsLeft": 0 
            } 
        }, 
        "result": {} 
    } 
    ```
  </Accordion>

  <Callout icon="👍" theme="okay">
    **Reference:** PayU recommends you to use PayU Hash Verification Tool to verify the reverse hashing. For more information, refer to [Using PayU Hash Verification Tool](doc:using-payu-hash-verification-tool)
  </Callout>
</Accordion>

***
