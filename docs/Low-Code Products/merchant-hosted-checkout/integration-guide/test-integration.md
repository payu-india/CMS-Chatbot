---
title: Test Your Integration
excerpt: Test key, salt, and the payment-method test values published for Merchant Hosted Checkout
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Test Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Test PayU Merchant Hosted Checkout with the test key and salt, net banking login, UPI VPAs, EMI test cards, and wallet test numbers.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">
  Use test credentials only. The legacy test page says you must only use the test merchant key and test salt for a test transaction.
</Callout>

# Test Your Integration

Test before you take live payments. You can test with a payment method that is configured on your checkout.

<!-- OMITTED: The legacy test page says to set setIsProduction() to false and that this enables live payments. That sentence contradicts itself, and Merchant Hosted Checkout in this folder is a form post, not an SDK call. The control is not copied. -->

## Test Credentials

<KeySaltReference />

## Test Credentials by Payment Method

### Net Banking

| Field | Value |
| --- | --- |
| Username | payu |
| Password | payu |
| OTP | 123456 |

### UPI Collect

| VPA |
| --- |
| anything@payu |
| 9999999999@payu.in |

<Callout icon="⚠️" theme="warn">
  The legacy test page says the UPI in-app flow and the UPI Intent flow are not available in test mode.
</Callout>

### EMI

The legacy test page lists these cards. Expiry is any future date. CVV is `123`. OTP is `111111`. Name is any name. Mobile `9123412345` is mandatory for EMI.

| Card | Number |
| --- | --- |
| Kotak DC EMI | 4706-1378-0509-9594 |
| AXIS DC EMI | 4011-5100-0000-0007 |
| HDFC CC EMI | 4453-3410-65876437 |
| ICICI CC EMI | 4453-3410-65876437 |

<!-- VALIDATION NEEDED: The legacy test page lists the same card number for HDFC CC EMI and ICICI CC EMI. -->

### Wallets

| Wallet | Test details |
| --- | --- |
| Paytm | Mobile `7777777777`, OTP `888888` |
| PhonePe | PhonePe pre-prod app: https://developer.phonepe.com/v1/docs/setting-up-test-account |
| Amazon Pay | Use your original Amazon account |
| Airtel | The wallets integration page says to use your mobile number. The product test page does not list Airtel |

<!-- VALIDATION NEEDED: PhonePe is only on the product test page. Airtel is only on the wallets integration page. -->

### Cards

<!-- DOCUMENTATION GAP: The Merchant Hosted test page does not list plain credit or debit test cards. EMI cards are in the table above. Card numbers inside integration samples are not republished here as test cards. -->

### PayPal

<!-- DOCUMENTATION GAP: No PayPal sandbox buyer, test amount, or test currency is in the Merchant Hosted PayPal page or the test page. -->

### Pluxee

<!-- DOCUMENTATION GAP: No Pluxee test card, OTP, or balance fixture is in this folder. The integration sample uses a masked PAN. -->

### Advantage Club

The wallets page says Advantage Club has no test credentials and no test environment. Test that wallet on production.

## Test Scenarios

<Accordion title="Successful payment" icon="fa-circle-check">
  Post a test payment with the test key and salt. Net banking success sample: `status=success`, `unmappedstatus=captured`, `error=E000`, `error_Message=No Error`, `mode=NB`. UPI Collect, wallets, PayPal, Pluxee, and cards success samples in the legacy pages also show `error=E000` and `error_Message=No Error`.
</Accordion>

<Accordion title="Failed / declined payment" icon="fa-xmark">
  The cards failure sample shows `status=failure`, `unmappedstatus=failed`, `error=E1903`, `error_Message=Authorization failed at Bank`, `field7=AUTHNEGATIVE`, and `field9=Authorization failed at Bank`.
</Accordion>

<Accordion title="Pending / timeout" icon="fa-clock">
  <!-- DOCUMENTATION GAP: The legacy overview says to simulate pending transactions. It does not say which status value to expect, which method returns pending, or how long to wait. -->
</Accordion>

<Accordion title="Hash mismatch" icon="fa-shield-halved">
  The legacy overview troubleshooting list says an incorrect hash means the hash parameters are in the wrong order. It does not name an error code for that case.
</Accordion>

<Accordion title="Duplicate txnid" icon="fa-copy">
  <!-- DOCUMENTATION GAP: The saved-card parameter text says PayU will not accept a duplicate transaction id. It does not name the error code or the response body. -->
</Accordion>
