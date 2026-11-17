---
title: Test Your Integration
excerpt: Use the test key and salt and the test values published for each payment method
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Test Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Test PayU Merchant Hosted Checkout with the test key and salt. Net banking, UPI VPA, EMI card, and wallet test values from the current test guide pages.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">
  Use only the test merchant key and test salt for test transactions.
</Callout>

# Test Your Integration

Test the integration before you accept live payments. You can make test payments with a payment method configured at checkout.

## Test Credentials

<KeySaltReference />

## Test Credentials by Payment Method

### Net Banking

| Field | Value |
| --- | --- |
| User name | payu |
| Password | payu |
| OTP | 123456 |

### UPI Collect

| VPA |
| --- |
| anything@payu |
| 9999999999@payu.in |

<Callout icon="⚠️" theme="warn">
  The UPI in-app flow and the UPI Intent flow are not available in test mode.
</Callout>

### EMI

The test page lists these debit and credit cards for EMI. Mobile number `9123412345` is mandatory for EMI. Expiry is any future date. CVV is `123`. OTP is `111111`. Name is any name.

| Card | Number |
| --- | --- |
| Kotak DC EMI | 4706-1378-0509-9594 |
| AXIS DC EMI | 4011-5100-0000-0007 |
| HDFC CC EMI | 4453-3410-65876437 |
| ICICI CC EMI | 4453-3410-65876437 |

<!-- VALIDATION NEEDED: The test page assigns the same card number, 4453-3410-65876437, to both HDFC CC EMI and ICICI CC EMI. -->

### Wallets

<!-- VALIDATION NEEDED: test-integration.md lists PayTM, PhonePe, and AmazonPay. The wallets guide also lists Airtel and a sandbox note for Amazon. Both sources are shown. -->

| Wallet | Mobile number or instructions | OTP |
| --- | --- | --- |
| PayTM | 7777777777 | 888888 |
| PhonePe | Use the PhonePe pre-prod app. The test page links to https://developer.phonepe.com/v1/docs/setting-up-test-account | Not stated |
| AmazonPay | The test page says to use your original Amazon account details. The wallets page says to use your real Amazon account in sandbox. | Not stated |
| Airtel | The wallets page says to use your mobile number. | Not stated |

### Cards

<!-- DOCUMENTATION GAP: No plain credit or debit test card is listed on the test page. The EMI rows above are the only card numbers marked as test data. -->

### PayPal

<!-- DOCUMENTATION GAP: No PayPal test account is listed in this folder. -->

### Pluxee

<!-- DOCUMENTATION GAP: No Pluxee test card, OTP, or balance is listed in this folder. -->

### Advantage Club

The wallets guide says there is no test environment and no test credentials. The sample posts to `https://secure.payu.in/_payment`.

## Test Scenarios

<Accordion title="Successful payment" icon="fa-circle-check">
  The overview says to simulate a successful payment. Callback samples for cards, UPI Collect, net banking, wallets, PayPal, and Pluxee use `status=success` and `error=E000` (`error_Message` is `No Error`). Card success samples also include `unmappedstatus=captured` and `field7=AUTHPOSITIVE`.
</Accordion>

<Accordion title="Failed / declined payment" icon="fa-xmark">
  The cards failure sample uses `status=failure`, `unmappedstatus=failed`, `field7=AUTHNEGATIVE`, `field9=Authorization failed at Bank`, `error=E1903`, and `error_Message=Authorization failed at Bank`.
</Accordion>

<Accordion title="Pending / timeout" icon="fa-clock">
  <!-- DOCUMENTATION GAP: The overview says to test pending transactions. It does not give a status value, a test trigger, or handling steps. -->
</Accordion>

<Accordion title="Incorrect hash" icon="fa-shield-halved">
  The overview troubleshooting note says an incorrect hash comes from the hash string parameter order. Compare the string with `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||Salt)`.

  <!-- DOCUMENTATION GAP: This folder does not name an error code for a hash mismatch. -->
</Accordion>

<Accordion title="Duplicate txnid" icon="fa-copy">
  The saved-card parameters say PayU will not accept a duplicate transaction ID.

  <!-- DOCUMENTATION GAP: No error code or response sample for a duplicate txnid is in this folder. -->
</Accordion>
