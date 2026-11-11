---
title: Merchant Hosted - Quick Start Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
This section helps you set up a test transaction within minutes using PayU's sandbox environment.

---

## Environment Endpoints

| Environment | Purpose | Payment Initiation URL (`_payment`) | Post-Service & Verification URL |
| :--- | :--- | :--- | :--- |
| **Test (Sandbox)** | Integration testing & mock payments | `<redacted URL>` | `<redacted URL>` |
| **Production (Live)** | Real customer payments | `https://secure.payu.in/_payment` | `https://info.payu.in/merchant/postservice.php?form=2` |

---

## Test Credentials

Use these standard sandbox test credentials for local and staging development:

* **Merchant Key:** `gtKFFx`
* **Merchant Salt:** `eCwWELxi`
* **Test Payment Endpoint:** `<redacted URL>`
* **Test Post-Service Endpoint:** `<redacted URL>`

---

## Simulated Test Payment Instruments

### 1. Test Cards
| Card Type | Card Number | Expiry | CVV | OTP | Behavior |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Visa (Domestic)** | `4012001033333333` | Any future date | `123` | `123456` | Direct Success |
| **Mastercard** | `5123450000000008` | Any future date | `123` | `123456` | Direct Success |
| **RuPay Card** | `6070000000000001` | Any future date | `123` | `123456` | Direct Success |
| **Declined Card** | `4012001033333334` | Any future date | `123` | Any | Simulated Decline |

### 2. Test Net Banking
* **Bank Code:** `TESTPGNB` (or select any major bank in the PayU simulator)
* **Username:** `payu`
* **Password:** `payu`
* **OTP:** `123456`

### 3. Test UPI VPAs
* **Successful Transaction:** `success@payu` or `9999999999@payu`
* **Declined Transaction:** `failure@payu`

### 4. Test Wallets
* **PayTM Mobile:** `7777777777` (OTP: `888888`)
* **PhonePe:** Use PhonePe sandbox app simulator or test phone numbers

---

## Ready-to-Run HTML Sandbox Form

Save this as an HTML file and open it in your browser to submit a test payment directly to `<redacted URL>`:

```html
<!DOCTYPE html>
<html>
<head>
  <title>PayU Merchant Hosted Quick Start</title>
</head>
<body>
  <h2>PayU Merchant Hosted - Test Card Payment</h2>
  <form action="<redacted URL>" method="POST">
    <!-- Mandatory Core Parameters -->
    <input type="hidden" name="key" value="gtKFFx" />
    <input type="hidden" name="txnid" value="TXN_TEST_101" />
    <input type="hidden" name="amount" value="10.00" />
    <input type="hidden" name="productinfo" value="TestProduct" />
    <input type="hidden" name="firstname" value="TestUser" />
    <input type="hidden" name="email" value="test@payu.in" />
    <input type="hidden" name="phone" value="9876543210" />
    <input type="hidden" name="surl" value="<redacted URL>" />
    <input type="hidden" name="furl" value="<redacted URL>" />
    
    <!-- Precomputed Request Hash for: gtKFFx|TXN_TEST_101|10.00|TestProduct|TestUser|test@payu.in|||||||||||eCwWELxi -->
    <input type="hidden" name="hash" value="f977c77d4681648a97c48529b5c808f2537c356b7c5286596b5bfa07f4bb587421ce809a4d048eb52cefc052bb89a19c7921ee62319ef586cfcae4a6820577bf" />
    
    <!-- Card Instrument Parameters -->
    <input type="hidden" name="pg" value="CC" />
    <input type="hidden" name="bankcode" value="CC" />
    <label>Card Number:</label><br />
    <input type="text" name="ccnum" value="4012001033333333" /><br /><br />
    <label>Card Holder Name:</label><br />
    <input type="text" name="ccname" value="Test User" /><br /><br />
    <label>Expiry Month (MM):</label><br />
    <input type="text" name="ccexpmon" value="12" /><br /><br />
    <label>Expiry Year (YYYY):</label><br />
    <input type="text" name="ccexpyr" value="2028" /><br /><br />
    <label>CVV:</label><br />
    <input type="password" name="ccvv" value="123" /><br /><br />

    <input type="submit" value="Pay Rs. 10.00 via Sandbox" />
  </form>
</body>
</html>
```
