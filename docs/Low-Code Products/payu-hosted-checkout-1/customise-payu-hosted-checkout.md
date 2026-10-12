---
title: Customise PayU Hosted Checkout
excerpt: >-
  Control which payment methods appear on the checkout page, hide specific
  methods, and set the checkout display language using request parameters.
deprecated: false
hidden: true
metadata:
  title: Customise PayU Hosted Checkout
  description: >-
    Restrict or hide payment methods on PayU Hosted Checkout using
    enforce_paymethod and drop_category. Set checkout display language with
    display_lang. Enable BNPL, EMI from Dashboard.
  keywords:
    - customise payu hosted checkout
    - payu enforce_paymethod restrict payment methods
    - payu drop_category hide payment methods
    - payu display_lang hindi tamil kannada checkout
    - payu checkout language customization india
    - payu show only upi creditcard checkout
    - payu bnpl emi enable dashboard
  robots: index
next:
  description: Explore related information and resources.
---
<Banner
  isInline={true}
  message="Integration effort: Minimal technical setup required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
 />

Customise your checkout experience for each transaction by passing optional parameters in the payment request. You can control which payment methods are available, which are hidden, and which language the checkout page displays in.

| Parameter                                | Goal                                     |
| ---------------------------------------- | ---------------------------------------- |
| `enforce_paymethod`                      | Show only specific payment methods       |
| `drop_category`                          | Hide specific payment methods            |
| `display_lang`                           | Change checkout display language         |
| **PayU Dashboard** → **Manage Checkout** | Enable BNPL, EMI, International Payments |

<Callout icon="📘" theme="info">
  ### **Payment Method Eligibility**

  Payment methods such as BNPL, EMI, and International Payments require PayU merchant eligibility or approval before they appear in checkout. Contact your PayU Key Account Manager to check eligibility and enable these methods.
</Callout>

***

## Enable or Activate Payment Methods

These payment methods are enabled by default for all PayU Hosted Checkout integrations:

- NetBanking
- Debit Card
- Credit Card
- UPI
- Wallet

<Accordion title="Steps to Enable or Activate Payment Methods" icon="fad fa-table-rows-add-above">
  To enable additional methods (BNPL, EMI, International Payments):

  1. Log in to [PayU Dashboard](https://payu.in/) and click **Payment Modes** under **Manage Checkout**.

     <Image src="https://files.readme.io/389134b9f74501150922f20236c09d7978f434c566cc4c073ba98f808342dd54-Screenshot_2026-10-12_at_3.25.34_PM.png" align="center" caption="Access Payment Modes" border={true} />

  2. Go to the required payment method tab.
  3. Click **Activate Now** (if the method is enabled and ready) or **Raise Request** (to request enablement).

  <Callout icon="fad fa-list-ol" theme="info">
    ### **Activate PayPal**

    To activate PayPal as a wallet option, see the PayPal linking steps in the Dashboard under **Payment Modes** → **International Payments** → **Link Paypal**.


    <Image src="https://files.readme.io/c87e3fd0acae9c085bf384990c3c4b2891bb7b96665d8ecbe43e9f753bf312b9-Screenshot_2026-10-12_at_3.34.59_PM.png" align="center" caption="Activate PayPal" border={true} />

  </Callout>
</Accordion>

***

## Restrict to Specific Payment Methods (`enforce_paymethod`)

Pass `enforce_paymethod` parameter in your <Anchor target="_blank" href="https://docs.payu.in/docs/payu-hosted-checkout-build-integration#step-1-prepare-payment-request-parameters">payment request</Anchor> to show only the payment methods you specify. Customers will only see those methods on the checkout page. These are the supported values.

| Category    | Value        |
| ----------- | ------------ |
| Credit Card | `creditcard` |
| Debit Card  | `debitcard`  |
| Net Banking | `netbanking` |
| EMI         | `emi`        |
| Wallet      | `cashcard`   |
| UPI         | `upi`        |
| Sodexo      | `SODEXO`     |
| BNPL        | `bnpl`       |
| QR          | `qr`         |

To enforce multiple methods, separate values with `|`. For example `creditcard|upi`.

### Use Cases

Below are the multiple use cases.

<Accordion title="Single Payment Method (Credit Card Only)" icon="fad fa-1">
  Use below code to enforce only credit card.

  ```curl
  curl -X POST "https://test.payu.in/_payment" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=JP***g" \
    -d "txnid=ENFCC001" \
    -d "amount=10.00" \
    -d "firstname=PayU%20User" \
    -d "email=test@gmail.com" \
    -d "phone=9876543210" \
    -d "productinfo=iPhone" \
    -d "surl=https://yourapp.com/success" \
    -d "furl=https://yourapp.com/failure" \
    -d "enforce_paymethod=creditcard" \
    -d "hash=REPLACE_WITH_GENERATED_HASH"
  ```
  ```python
  import requests

  payload = {
      "key": "JP***g",
      "txnid": "ENFCC001",
      "amount": "10.00",
      "firstname": "PayU User",
      "email": "test@gmail.com",
      "phone": "9876543210",
      "productinfo": "iPhone",
      "surl": "https://yourapp.com/success",
      "furl": "https://yourapp.com/failure",
      "enforce_paymethod": "creditcard",
      "hash": "REPLACE_WITH_GENERATED_HASH",
  }
  response = requests.post("https://test.payu.in/_payment", data=payload)
  print(response.text)
  ```
  ```javascript
  const axios = require('axios');
  const qs = require('querystring');

  const payload = {
    key: 'JP***g',
    txnid: 'ENFCC001',
    amount: '10.00',
    firstname: 'PayU User',
    email: 'test@gmail.com',
    phone: '9876543210',
    productinfo: 'iPhone',
    surl: 'https://yourapp.com/success',
    furl: 'https://yourapp.com/failure',
    enforce_paymethod: 'creditcard',
    hash: 'REPLACE_WITH_GENERATED_HASH'
  };
  axios.post('https://test.payu.in/_payment', qs.stringify(payload));
  ```
</Accordion>

<Accordion title="Multiple Methods (Credit Card and UPI Only)" icon="fad fa-list-timeline">
  Pass `enforce_paymethod=creditcard|upi` — use `|` as separator, no spaces.

  ```curl
  curl -X POST "https://test.payu.in/_payment" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=JP***g" \
    -d "txnid=ENFCC001" \
    -d "amount=10.00" \
    -d "firstname=PayU%20User" \
    -d "email=test@gmail.com" \
    -d "phone=9876543210" \
    -d "productinfo=iPhone" \
    -d "surl=https://yourapp.com/success" \
    -d "furl=https://yourapp.com/failure" \
    -d "enforce_paymethod=creditcard|upi" \
    -d "hash=REPLACE_WITH_GENERATED_HASH"
  ```
  ```python
  import requests

  payload = {
      "key": "JP***g",
      "txnid": "ENFCC001",
      "amount": "10.00",
      "firstname": "PayU User",
      "email": "test@gmail.com",
      "phone": "9876543210",
      "productinfo": "iPhone",
      "surl": "https://yourapp.com/success",
      "furl": "https://yourapp.com/failure",
      "enforce_paymethod": "creditcard|upi",
      "hash": "REPLACE_WITH_GENERATED_HASH",
  }
  response = requests.post("https://test.payu.in/_payment", data=payload)
  print(response.text)
  ```
  ```javascript
  const axios = require('axios');
  const qs = require('querystring');

  const payload = {
    key: 'JP***g',
    txnid: 'ENFCC001',
    amount: '10.00',
    firstname: 'PayU User',
    email: 'test@gmail.com',
    phone: '9876543210',
    productinfo: 'iPhone',
    surl: 'https://yourapp.com/success',
    furl: 'https://yourapp.com/failure',
    enforce_paymethod: 'creditcard|upi',
    hash: 'REPLACE_WITH_GENERATED_HASH'
  };
  axios.post('https://test.payu.in/_payment', qs.stringify(payload));
  ```
</Accordion>

***

## Hide Specific Payment Methods (`drop_category`)

Pass the `drop_category` parameter to hide specific payment methods from the checkout. All other enabled methods remain visible. Below are the supported values:

| Category    | Value        |
| ----------- | ------------ |
| Credit Card | `creditcard` |
| Debit Card  | `debitcard`  |
| Net Banking | `netbanking` |
| NEFT/RTGS   | `NEFTRTGS`   |
| EMI         | `emi`        |
| Wallet      | `cashcard`   |
| Sodexo      | `SODEXO`     |
| BNPL        | `bnpl`       |

To drop multiple methods, separate values with `|`. For example `creditcard|netbanking`.

### Use Cases

Below are the multiple use cases.

<Accordion title="Hide a Single Method" icon="fad fa-1">
  Use below code to enforce only credit card.

  ```curl
  curl -X POST "https://test.payu.in/_payment" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=JP***g" \
    -d "txnid=ENFCC001" \
    -d "amount=10.00" \
    -d "firstname=PayU%20User" \
    -d "email=test@gmail.com" \
    -d "phone=9876543210" \
    -d "productinfo=iPhone" \
    -d "surl=https://yourapp.com/success" \
    -d "furl=https://yourapp.com/failure" \
    -d "drop_category=creditcard" \
    -d "hash=REPLACE_WITH_GENERATED_HASH"
  ```
  ```python
  import requests

  payload = {
      "key": "JP***g",
      "txnid": "ENFCC001",
      "amount": "10.00",
      "firstname": "PayU User",
      "email": "test@gmail.com",
      "phone": "9876543210",
      "productinfo": "iPhone",
      "surl": "https://yourapp.com/success",
      "furl": "https://yourapp.com/failure",
      "drop_category=creditcard",
      "hash": "REPLACE_WITH_GENERATED_HASH",
  }
  response = requests.post("https://test.payu.in/_payment", data=payload)
  print(response.text)
  ```
  ```javascript
  const axios = require('axios');
  const qs = require('querystring');

  const payload = {
    key: 'JP***g',
    txnid: 'ENFCC001',
    amount: '10.00',
    firstname: 'PayU User',
    email: 'test@gmail.com',
    phone: '9876543210',
    productinfo: 'iPhone',
    surl: 'https://yourapp.com/success',
    furl: 'https://yourapp.com/failure',
    drop_category: 'creditcard',
    hash: 'REPLACE_WITH_GENERATED_HASH'
  };
  axios.post('https://test.payu.in/_payment', qs.stringify(payload));
  ```
</Accordion>

<Accordion title="Hide Multiple Methods" icon="fad fa-list-timeline">
  Pass `drop_category=creditcard|upi` — use `|` as separator, no spaces.

  ```curl
  curl -X POST "https://test.payu.in/_payment" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=JP***g" \
    -d "txnid=ENFCC001" \
    -d "amount=10.00" \
    -d "firstname=PayU%20User" \
    -d "email=test@gmail.com" \
    -d "phone=9876543210" \
    -d "productinfo=iPhone" \
    -d "surl=https://yourapp.com/success" \
    -d "furl=https://yourapp.com/failure" \
    -d "drop_category=creditcard|upi" \
    -d "hash=REPLACE_WITH_GENERATED_HASH"
  ```
  ```python
  import requests

  payload = {
      "key": "JP***g",
      "txnid": "ENFCC001",
      "amount": "10.00",
      "firstname": "PayU User",
      "email": "test@gmail.com",
      "phone": "9876543210",
      "productinfo": "iPhone",
      "surl": "https://yourapp.com/success",
      "furl": "https://yourapp.com/failure",
      "drop_category=creditcard|netbanking",
      "hash": "REPLACE_WITH_GENERATED_HASH",
  }
  response = requests.post("https://test.payu.in/_payment", data=payload)
  print(response.text)
  ```
  ```javascript
  const axios = require('axios');
  const qs = require('querystring');

  const payload = {
    key: 'JP***g',
    txnid: 'ENFCC001',
    amount: '10.00',
    firstname: 'PayU User',
    email: 'test@gmail.com',
    phone: '9876543210',
    productinfo: 'iPhone',
    surl: 'https://yourapp.com/success',
    furl: 'https://yourapp.com/failure',
    drop_category: 'creditcard|netbanking',
    hash: 'REPLACE_WITH_GENERATED_HASH'
  };
  axios.post('https://test.payu.in/_payment', qs.stringify(payload));
  ```
</Accordion>

###

<Callout icon="📘" theme="info">
  ### `enforce_paymethod`**&#x20;vs&#x20;**`drop_category`

  Use `enforce_paymethod` when you have a short list of methods you want to show. Use `drop_category` when you want to show most methods but exclude a few. Do not use both in the same request — behaviour is undefined.
</Callout>

***

## Set Checkout Display Language (`display_lang`)

Pass the `display_lang` parameter to display the PayU checkout page in one of the following supported Indian languages.

| Language          | Value      |
| ----------------- | ---------- |
| English (default) | `English`  |
| Hindi             | `Hindi`    |
| Kannada           | `Kannada`  |
| Telugu            | `Telugu`   |
| Tamil             | `Tamil`    |
| Gujarati          | `Gujarati` |
| Marathi           | `Marathi`  |

### Sample Request

```curl
curl -X POST "https://test.payu.in/_payment" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g" \
  -d "txnid=ENFCC001" \
  -d "amount=10.00" \
  -d "firstname=PayU%20User" \
  -d "email=test@gmail.com" \
  -d "phone=9876543210" \
  -d "productinfo=iPhone" \
  -d "surl=https://yourapp.com/success" \
  -d "furl=https://yourapp.com/failure" \
  -d "drop_category=creditcard|upi" \
  -d "display_lang=Hindi" \
  -d "hash=REPLACE_WITH_GENERATED_HASH"
```
```python
import requests

payload = {
    "key": "JP***g",
    "txnid": "ENFCC001",
    "amount": "10.00",
    "firstname": "PayU User",
    "email": "test@gmail.com",
    "phone": "9876543210",
    "productinfo": "iPhone",
    "surl": "https://yourapp.com/success",
    "furl": "https://yourapp.com/failure",
    "drop_category=creditcard|netbanking",
    "display_lang=Hindi",
    "hash": "REPLACE_WITH_GENERATED_HASH",
}
response = requests.post("https://test.payu.in/_payment", data=payload)
print(response.text)
```
```javascript
const axios = require('axios');
const qs = require('querystring');

const payload = {
  key: 'JP***g',
  txnid: 'ENFCC001',
  amount: '10.00',
  firstname: 'PayU User',
  email: 'test@gmail.com',
  phone: '9876543210',
  productinfo: 'iPhone',
  surl: 'https://yourapp.com/success',
  furl: 'https://yourapp.com/failure',
  drop_category: 'creditcard|netbanking',
  display_lang: 'Hindi',
  hash: 'REPLACE_WITH_GENERATED_HASH'
};
axios.post('https://test.payu.in/_payment', qs.stringify(payload));
```


<Image src="https://files.readme.io/3aae0ef-hindipage.png" align="center" caption="_PayU Hosted Checkout in hindi_" framed={true} />


<Callout icon="📘" theme="info">
  ### **Vernacular Checkout**

  &#x20;Displaying checkout in the customer's preferred language can improve conversion rates, particularly for regional audiences. See this [video overview](https://www.youtube.com/watch?v=7UCT0jFbB90) for more context.
</Callout>

***

## Customisation Parameters

| Parameter           | Type   | Effect                                    | Example value                  |
| ------------------- | ------ | ----------------------------------------- | ------------------------------ |
| `enforce_paymethod` | string | Show only these methods                   | `upi`, `creditcard\|upi`       |
| `drop_category`     | string | Hide these methods                        | `creditcard`, `creditcard\|NB` |
| `display_lang`      | string | Set checkout UI language                  | `Hindi`, `Tamil`               |
| `custom_note`       | string | Display a message below payment options   | `Extra charge of ₹100 applies` |
| `note_category`     | string | Show `custom_note` only for these methods | `CC, NB`                       |
