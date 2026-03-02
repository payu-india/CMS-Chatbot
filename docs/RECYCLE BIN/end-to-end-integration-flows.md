---
title: End-to-End Integration Flows
deprecated: false
hidden: true
metadata:
  robots: index
---
## PayU Hosted 

### 🔁 Flow Overview

```
Frontend → Your Backend → PayU → User Pays → PayU redirects to success/failure URL → You verify hash → Update DB
```

***

### 🧠 Step 1: Environment Variables

```bash
PAYU_KEY=your_test_key
PAYU_SALT=your_test_salt
PAYU_BASE_URL=https://test.payu.in/_payment
```

***

### 🖥 Step 2: Backend (Node.js / Express)

Install dependencies:

```bash
npm install express body-parser crypto
```

#### server.js

```javascript
const express = require("express");
const bodyParser = require("body-parser");
const crypto = require("crypto");

const app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

const key = process.env.PAYU_KEY;
const salt = process.env.PAYU_SALT;
const PAYU_BASE_URL = process.env.PAYU_BASE_URL;

function generateHash(data) {
  const hashString = `${key}|${data.txnid}|${data.amount}|${data.productinfo}|${data.firstname}|${data.email}|||||||||||${salt}`;
  return crypto.createHash("sha512").update(hashString).digest("hex");
}

app.post("/create-payment", (req, res) => {
  const txnid = "txn_" + Date.now();

  const paymentData = {
    key: key,
    txnid: txnid,
    amount: "10.00",
    productinfo: "Test Product",
    firstname: "Rahul",
    email: "rahul@test.com",
    phone: "9999999999",
    surl: "http://localhost:3000/success",
    furl: "http://localhost:3000/failure",
    service_provider: "payu_paisa"
  };

  paymentData.hash = generateHash(paymentData);

  res.json({
    action: PAYU_BASE_URL,
    params: paymentData
  });
});

app.post("/success", (req, res) => {
  const posted = req.body;

  const reverseHashString = `${salt}|${posted.status}|||||||||||${posted.email}|${posted.firstname}|${posted.productinfo}|${posted.amount}|${posted.txnid}|${key}`;
  const calculatedHash = crypto.createHash("sha512")
    .update(reverseHashString)
    .digest("hex");

  if (calculatedHash === posted.hash) {
    res.send("Payment Successful and Verified!");
  } else {
    res.send("Hash mismatch. Possible tampering.");
  }
});

app.post("/failure", (req, res) => {
  res.send("Payment Failed.");
});

app.listen(3000, () => console.log("Server running on port 3000"));
```

***

### 🖼 Step 3: Frontend HTML

```html
<button onclick="pay()">Pay Now</button>

<script>
async function pay() {
  const response = await fetch("/create-payment", { method: "POST" });
  const data = await response.json();

  const form = document.createElement("form");
  form.method = "POST";
  form.action = data.action;

  for (const key in data.params) {
    const input = document.createElement("input");
    input.type = "hidden";
    input.name = key;
    input.value = data.params[key];
    form.appendChild(input);
  }

  document.body.appendChild(form);
  form.submit();
}
</script>
```

<br />

***

### 🧠 Production Architecture Advice

From real-world experience integrating PayU India:

#### 1. Always Store:

* txnid
* user_id
* amount
* status
* payu_response

#### 2. Never Trust Frontend Success

Only trust:

* Hash verification
* Webhook confirmation

#### 3. Always Handle:

* Duplicate callbacks
* Payment success but redirect failure
* User closes browser

***

### &#x20;What Developers Usually Get Wrong

| Mistake                        | Result                  |
| ------------------------------ | ----------------------- |
| Wrong hash sequence            | Payment always fails    |
| Not verifying reverse hash     | Fraud risk              |
| Logging card details           | PCI violation           |
| Not handling duplicate webhook | Double order processing |

***

## Merchant Hosted - Cards

### 1️⃣ Overview of Flow

```
Browser (Card Form)
      ↓ submit
Your Server → Generate Hash & PayU Params
      ↓ post to PayU Seamless API
PayU → Returns Authorize/Decline
Your Server → Process Response
```

***

### 2️⃣ Environment Setup

Create a `.env` file:

```
PAYU_KEY=your_test_key
PAYU_SALT=your_test_salt
PAYU_BASE_URL=https://test.payu.in
PORT=3000
```

***

### 3️⃣ Project Setup (Node + Express)

```bash
mkdir payu-cards-demo
cd payu-cards-demo
npm init -y
npm install express body-parser axios crypto dotenv
```

***

### 4️⃣ Server: server.js

```javascript
require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const crypto = require('crypto');

const app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

const { PAYU_KEY, PAYU_SALT, PAYU_BASE_URL, PORT } = process.env;

// Utility: Generate PayU Hash
function generateHash(data) {
  // As documented for Merchant Hosted Cards
  const {
    key, txnid, amount, productinfo, firstname, email,
    cardnum, cardexp_month, cardexp_year, cvv2
  } = data;

  const hashStr = `${key}|${txnid}|${amount}|${productinfo}|${firstname}|${email}|||||||||||${PAYU_SALT}`;
  return crypto.createHash('sha512').update(hashStr).digest('hex');
}

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/cardform.html");
});

// 1) Create Payment Endpoint
app.post("/pay", async (req, res) => {
  try {
    const txnid = "txn_" + Date.now();
    const {
      firstname, email, phone,
      cardnum, cardexp_month, cardexp_year, cvv2
    } = req.body;

    const paymentData = {
      key: PAYU_KEY,
      txnid,
      amount: "500.00",             // Example amount
      productinfo: "Demo Product",
      firstname,
      email,
      phone,
      surl: "http://localhost:3000/success",
      furl: "http://localhost:3000/failure",
      // Merchant Hosted Tag
      pg: "CC",                     // Credit Card
      bankcode: "",                 // Not needed for cards
      cardnum,
      cardexp_month,
      cardexp_year,
      cvv2
    };

    // Hash
    paymentData.hash = generateHash(paymentData);

    // Post to PayU Seamless API
    const apiUrl = `${PAYU_BASE_URL}/_payment`;
    const formParams = new URLSearchParams(paymentData);

    const result = await axios.post(apiUrl, formParams.toString(), {
      headers: { "Content-Type": "application/x-www-form-urlencoded" }
    });

    // PayU responds with HTML if 3D Secure etc
    res.send(result.data);

  } catch (err) {
    console.error(err.message);
    res.status(500).send("Payment Error");
  }
});

// Success callback
app.post("/success", (req, res) => {
  // 1) Verify Response Hash
  const response = req.body;

  const reverseHashStr = `${PAYU_SALT}|${response.status}|||||||||||${response.email}|${response.firstname}|${response.productinfo}|${response.amount}|${response.txnid}|${PAYU_KEY}`;
  const calculated = crypto.createHash('sha512').update(reverseHashStr).digest('hex');

  if (calculated === response.hash) {
    res.send("Payment Successful & Verified!");
  } else {
    res.send("Hash mismatch!");
  }
});

// Failure
app.post("/failure", (req, res) => {
  res.send("Payment failed");
});

app.listen(PORT, () => console.log(`Running on ${PORT}`));
```
```python
import os
import hashlib
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

PAYU_KEY = os.getenv("PAYU_KEY")
PAYU_SALT = os.getenv("PAYU_SALT")
PAYU_BASE_URL = os.getenv("PAYU_BASE_URL")


def generate_hash(data):
    """
    Generate hash as per PayU seamless integration format
    """
    hash_string = f"{PAYU_KEY}|{data['txnid']}|{data['amount']}|{data['productinfo']}|{data['firstname']}|{data['email']}|||||||||||{PAYU_SALT}"
    return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()


@app.route("/")
def home():
    return render_template("card_form.html")


@app.route("/pay", methods=["POST"])
def pay():
    txnid = f"txn_{int(os.urandom(4).hex(), 16)}"

    payment_data = {
        "key": PAYU_KEY,
        "txnid": txnid,
        "amount": "500.00",
        "productinfo": "Demo Product",
        "firstname": request.form["firstname"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "surl": "http://localhost:5000/success",
        "furl": "http://localhost:5000/failure",

        # Seamless Card parameters
        "pg": "CC",
        "cardnum": request.form["cardnum"],
        "cardexp_month": request.form["cardexp_month"],
        "cardexp_year": request.form["cardexp_year"],
        "cvv2": request.form["cvv2"]
    }

    payment_data["hash"] = generate_hash(payment_data)

    # Send to PayU
    response = requests.post(PAYU_BASE_URL, data=payment_data)

    # PayU may return HTML (3DS page)
    return response.text


@app.route("/success", methods=["POST"])
def success():
    response = request.form.to_dict()

    # Reverse hash verification
    reverse_hash_string = f"{PAYU_SALT}|{response['status']}|||||||||||{response['email']}|{response['firstname']}|{response['productinfo']}|{response['amount']}|{response['txnid']}|{PAYU_KEY}"
    calculated_hash = hashlib.sha512(reverse_hash_string.encode('utf-8')).hexdigest()

    if calculated_hash == response["hash"]:
        # Update DB here
        return "Payment Successful & Verified!"
    else:
        return "Hash mismatch. Possible tampering."


@app.route("/failure", methods=["POST"])
def failure():
    return "Payment Failed"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
```

***

### 5️⃣ HTML Form (cardform.html)

Create this file in the same folder:

```html
<!DOCTYPE html>
<html>
<head>
<title>Card Payment</title>
</head>
<body>

<h3>Pay with Card</h3>
<form method="POST" action="/pay">
  <label>First Name</label><br>
  <input type="text" name="firstname" required /><br>

  <label>Email</label><br>
  <input type="email" name="email" required /><br>

  <label>Phone</label><br>
  <input type="text" name="phone" required /><br>

  <hr>

  <label>Card Number</label><br>
  <input type="text" name="cardnum" maxlength="16" required /><br>

  <label>Expiry (MM)</label><br>
  <input type="text" name="cardexp_month" maxlength="2" required /><br>

  <label>Expiry (YY)</label><br>
  <input type="text" name="cardexp_year" maxlength="2" required /><br>

  <label>CVV</label><br>
  <input type="text" name="cvv2" maxlength="3" required /><br><br>

  <button type="submit">Pay ₹500</button>
</form>

</body>
</html>
```

***

### 6️⃣ What Happens Behind the Scenes

| Step                          | What Happens                |
| ----------------------------- | --------------------------- |
| User submits card info        | Browser → Your Server       |
| Your Server calculates hash   | Prevents tampering          |
| Server posts to PayU Seamless | PayU processes card         |
| PayU returns HTML             | Could be 3DS or status page |
| Success/failure               | PayU hits your callback     |

***

### 7️⃣ Webhook Handling (Recommended)

Create `/webhook` route:

```javascript
app.post('/webhook', (req, res) => {
  const payload = req.body;

  // Always verify signature if provided
  console.log("Webhook Received:", payload);
  res.status(200).send("OK");
});
```
```python
@app.route("/webhook", methods=["POST"])
def webhook():
    payload = request.form.to_dict()

    # Verify hash again
    print("Webhook received:", payload)

    return "OK", 200
```

Configure webhook URL in your PayU dashboard to receive asynchronous confirmations.

***

### 8️⃣ Common Errors & Fixes

| Problem                       | Fix                         |
| ----------------------------- | --------------------------- |
| Invalid hash                  | Check hash sequence exactly |
| Silent failures               | Check callback URLs         |
| CVV fails                     | Test card details mismatch  |
| Redirects not hitting success | Confirm HTTP POST           |
| Production card decline       | Enable BINs in dashboard    |

***

### 9️⃣ Test Card Credentials (Sandbox)

You can use sample test card numbers like:

```
Card: 5123450000000008
Expiry: 12/24
CVV: 123
```

(Different banks will let you generate different responses.)

<br />
