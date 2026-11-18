---
title: Test Your Integration
excerpt: Test key, salt, and the payment-method values the source actually lists
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Test Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Test Merchant Hosted Checkout with the test key and salt. Net banking, UPI VPA, EMI card, and wallet values from the current test page. Do not use a live key.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">
  Use the test key and salt only. The source says you must not use live credentials for a test transaction.
</Callout>

# Test Your Integration

Test before you go live. The source says you can test with a payment method that is configured at checkout.

<!-- VALIDATION NEEDED: The current test page says to set setIsProduction() to false, and that this enables the integration to accept live payments. Merchant Hosted Checkout in this folder is a form POST. None of the samples call setIsProduction(). That instruction is not repeated here. -->

## Test Credentials

<KeySaltReference />

<TestKeyAndSaltProcedure />

## Test Credentials by Payment Method

### Net Banking

| Field | Value |
| --- | --- |
| Username | `payu` |
| Password | `payu` |
| OTP | `123456` |

The test request in the net-banking guide uses `pg=TESTPG` and `bankcode=TESTPGNB`.

### UPI

| VPA |
| --- |
| `anything@payu` |
| `9999999999@payu.in` |

<Callout icon="⚠️" theme="warn">
  The test page says the UPI in-app flow and the UPI intent flow are not available in test mode.
</Callout>

### EMI

Expiry is any future date. CVV is `123`. OTP is `111111`. Name is any name. Mobile `9123412345` is mandatory for EMI.

| Card | Number |
| --- | --- |
| Kotak DC EMI | `4706-1378-0509-9594` |
| AXIS DC EMI | `4011-5100-0000-0007` |
| HDFC CC EMI | `4453-3410-65876437` |
| ICICI CC EMI | `4453-3410-65876437` |

<!-- VALIDATION NEEDED: HDFC CC EMI and ICICI CC EMI are given the same card number on the test page. -->

### Wallets

| Wallet | Test details in the source |
| --- | --- |
| Paytm | Mobile `7777777777`, OTP `888888` |
| PhonePe | PhonePe pre-prod app. The test page links `https://developer.phonepe.com/v1/docs/setting-up-test-account`. OTP is `NA` |
| Amazon Pay | Use your real Amazon account |
| Airtel | The wallets page says to use your mobile number. The test page does not list Airtel |

### Advantage Club

<Callout icon="🚧" theme="warn">
  The wallets page says there is no test environment and no test credentials for Advantage Club. It says to test on production.
</Callout>

### Cards

<!-- DOCUMENTATION GAP: The test page does not list a sandbox card for a normal card payment. Card numbers on the cards page are request examples, not labeled test cards. The EMI numbers above are labeled for EMI. -->

### Pluxee, PayPal, BNPL, EFTNET, and TPV

<!-- DOCUMENTATION GAP: The test page has no credentials for Pluxee, PayPal, BNPL, EFTNET, or net-banking TPV. -->

## Test Scenarios

<Accordion title="Successful payment" icon="fa-circle-check">
  The overview says to simulate a successful payment. The cards success sample has `status=success`, `unmappedstatus=captured`, and `error=E000` ("No Error"). The net-banking, UPI, wallet, PayPal, and Pluxee success samples also use `error=E000`.

  <!-- DOCUMENTATION GAP: The source does not say which test credential forces success beyond "use the test key and the test method credentials." -->
</Accordion>

<Accordion title="Failed payment" icon="fa-xmark">
  The cards failure sample has `status=failure`, `unmappedstatus=failed`, `error=E1903`, `error_Message=Authorization failed at Bank`, and `field7=AUTHNEGATIVE`.

  <!-- DOCUMENTATION GAP: No decline test card, decline OTP, or decline VPA is given. -->
</Accordion>

<Accordion title="Pending" icon="fa-clock">
  The overview says to simulate a pending transaction.

  <!-- DOCUMENTATION GAP: No pending trigger and no pending response sample are in this folder. Do not describe NEFT timing or a fulfilment rule that is not written here. -->
</Accordion>

<Accordion title="Hash mismatch" icon="fa-shield-halved">
  The overview says an incorrect hash means you should recheck the parameter order.

  <!-- DOCUMENTATION GAP: No hash-mismatch error code is in this folder. E501 is not used because it does not appear in the Merchant Hosted source. -->
</Accordion>

<Accordion title="Duplicate txnid" icon="fa-copy">
  The saved-card parameters say the txnid must be unique and that PayU will not accept a duplicate transaction id.

  <!-- DOCUMENTATION GAP: No error code or response body for a duplicate txnid is in this folder. -->
</Accordion>
