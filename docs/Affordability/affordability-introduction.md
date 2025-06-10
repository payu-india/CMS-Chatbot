---
title: Affordability - Introduction
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: PayU Affordability Suite Documentation
---

{/* 
  This MDX file replicates the layout of the original HTML right-pane.
  It uses CSS for styling and React-compatible className props.
*/}

<style jsx>{`
  /* Main layout containers */
  .main-container {
    display: flex;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .content {
    flex-grow: 1;
    padding: 20px 40px;
    max-width: 800px;
  }
  
  /* Grid layouts */
  .feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 15px;
    margin: 20px 0;
  }
  
  .feature-item {
    background: #f8f9fa;
    padding: 15px;
    border-radius: 5px;
    border: 1px solid #eaeaea;
  }
  
  .integration-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin: 20px 0;
  }
  
  .integration-card {
    background: #f8f9fa;
    padding: 20px;
    border-radius: 5px;
    border: 1px solid #eaeaea;
  }
  
  /* Component styles */
  .placeholder {
    background: #f0f2f5;
    border: 1px dashed #c0c0c0;
    border-radius: 5px;
    padding: 30px;
    margin: 15px 0;
    text-align: center;
    color: #666;
  }
  
  .key-value {
    background: #f8f9fa;
    padding: 15px;
    border-radius: 5px;
    margin: 10px 0;
  }
  
  /* Basic element styling */
  hr {
    margin: 30px 0;
    border: none;
    border-top: 1px solid #eaeaea;
  }
  
  pre {
    background: #f8f9fa;
    padding: 15px;
    border-radius: 5px;
    overflow-x: auto;
    border: 1px solid #eaeaea;
    font-family: monospace;
  }
  
  code {
    font-family: monospace;
  }
  
  .page-nav {
    margin-top: 30px;
    padding-top: 15px;
    border-top: 1px solid #eaeaea;
    text-align: right;
  }
`}</style>

<div className="main-container">
<div className="content">

<section id="getting-started">

# Getting Started with PayU Affordability Suite

## What is PayU Affordability Suite?

PayU Affordability Suite helps customers pay in flexible installments, increasing your conversion rates and average order value.

<div className="feature-grid">
<div className="feature-item">No Cost EMI & Standard EMI</div>
<div className="feature-item">Cardless EMI (ZestMoney, EarlySalary)</div>
<div className="feature-item">Pay Later (LazyPay, Simpl)</div>
<div className="feature-item">Checkout Finance</div>
</div>

<hr />

## Integration Flow Overview

```
Customer Selects Product → PayU Shows Affordability Options → Customer Chooses Payment → Instant Approval/Rejection → Payment Completion
```

<div className="placeholder">Visual Flow Diagram</div>

<hr />

## Prerequisites

### 1. PayU Account Setup

- Active PayU merchant account
- Affordability Suite enabled
- Test environment access

### 2. Credentials Required

**Merchant ID (MID):** YOUR_MERCHANT_ID  
**Salt Key:** YOUR_SALT_KEY  
**Environment:** Test/Production URLs

### 3. Technical Requirements

- HTTPS enabled website
- Webhook URL for payment notifications
- Basic HTML/JavaScript knowledge

<hr />

## Quick Integration Options

<div className="integration-grid">
<div className="integration-card">
<h3>Option A: PayU Hosted</h3>
<p>Quickest integration where customers are redirected to PayU's payment page.</p>
<ul>
<li>Minimal development</li>
<li>All options pre-configured</li>
<li>Redirect to PayU's checkout</li>
</ul>
</div>
<div className="integration-card">
<h3>Option B: Merchant Hosted</h3>
<p>Customizable integration where all options are on your site.</p>
<ul>
<li>Maximum customization</li>
<li>Customer stays on your site</li>
<li>More development effort</li>
</ul>
</div>
</div>

## First Integration Steps

### Step 1: Get Your Test Credentials

1. Login to PayU Dashboard: https://onboarding.payu.in/app/account/signin
2. Switch to Test Mode from the toggle option
3. Go to Developer → API Details to get your credentials

<div className="placeholder">Dashboard Screenshot</div>

### Step 2: Create Payment Form

```html
<form action="https://test.payu.in/_payment" method="post">
    <input type="hidden" name="key" value="YOUR_TEST_KEY" />
    <input type="hidden" name="txnid" value="unique_txn_123" />
    <input type="hidden" name="productinfo" value="iPhone" />
    <input type="hidden" name="amount" value="10.00" />
    <input type="hidden" name="email" value="test@gmail.com" />
    <input type="hidden" name="firstname" value="Ashish" />
    <input type="hidden" name="lastname" value="Kumar" />
    <input type="hidden" name="phone" value="9988776655" />
    <input type="hidden" name="surl" value="https://yoursite.com/success" />
    <input type="hidden" name="furl" value="https://yoursite.com/failure" />
    <input type="hidden" name="hash" value="CALCULATED_HASH" />
    <input type="submit" value="Pay Now" />
</form>
```

### Step 3: Generate Hash (Important!)

Hash Logic: sha512(key|txnid|amount|productinfo|firstname|email|||||||||SALT)

### Step 4: Test Payment

Test Card Details:

- Card Number: 5123-4567-8901-2346
- Expiry: Any future date
- CVV: 123
- OTP: 123456 (for test environment)

<div className="placeholder">Payment Screenshot</div>

<div className="page-nav">
<strong>Next:</strong> <a href="#payu-hosted">PayU Hosted Solution →</a>
</div>

</section>

<section id="payu-hosted">

# PayU Hosted Solution

## Overview

PayU Hosted Solution is the fastest way to integrate affordability options. Customer gets redirected to PayU's payment page where all EMI, Pay Later, and Cardless options are automatically displayed.

<div className="feature-grid">
<div className="feature-item">Quick setup (30 minutes)</div>
<div className="feature-item">Minimal development effort</div>
<div className="feature-item">Testing affordability features</div>
<div className="feature-item">Proof of concept deployments</div>
</div>

## Customer Journey Flow

```
Your Website → Add to Cart → Click Pay → Redirect to PayU → Select Affordability Option → Complete Payment → Return to Your Site
```

<div className="placeholder">Visual Flow Diagram</div>

## Integration Steps

### Step 1: Basic Payment Form

```html
<form action="https://test.payu.in/_payment" method="post">
    <input type="hidden" name="key" value="YOUR_MERCHANT_KEY" />
    <input type="hidden" name="txnid" value="unique_transaction_id" />
    <input type="hidden" name="amount" value="15000" />
    <input type="hidden" name="productinfo" value="Samsung Galaxy S24" />
    <input type="hidden" name="firstname" value="John" />
    <input type="hidden" name="email" value="john@example.com" />
    <input type="hidden" name="phone" value="9876543210" />
    <input type="hidden" name="surl" value="https://yoursite.com/payment/success" />
    <input type="hidden" name="furl" value="https://yoursite.com/payment/failure" />
    <input type="hidden" name="hash" value="CALCULATED_HASH" />
    
    <!-- Enable Affordability Options -->
    <input type="hidden" name="show_payment_mode" value="CC,DC,EMI,CARDLESSEMI,LAZYPAY" />
    
    <button type="submit">Pay ₹15,000</button>
</form>
```

### Step 2: Enable Affordability Display

```html
<!-- Show affordability message -->
<input type="hidden" name="custom_note" value="EMI starting ₹1,250/month available" />
<input type="hidden" name="note_category" value="CC,DC,EMI" />

<!-- Enforce specific payment methods -->
<input type="hidden" name="enforced_payment" value="creditcard|debitcard|emi" />
```

## PayU Payment Page Features

### Automatic Affordability Display

<div className="placeholder">PayU Payment Page Screenshot</div>

What customers see:

- Credit/Debit Card payment options
- EMI plans (3, 6, 9, 12 months)
- No Cost EMI options (if available)
- Cardless EMI providers (ZestMoney, EarlySalary)
- Pay Later options (LazyPay, Simpl)

### EMI Calculator Widget

<div className="placeholder">EMI Calculator Widget</div>

Features:

- Real-time EMI calculation
- Interest rate and processing fee display
- Monthly installment breakdown
- Total cost comparison

<div className="page-nav">
<strong>Next:</strong> <a href="#emi-options">EMI Options →</a>
</div>

</section>

<section id="emi-options">

# EMI Options (Credit & Debit Cards)

## Overview

EMI on Credit and Debit Cards allows customers to convert their purchases into easy monthly installments, making high-value products more affordable.

<div className="feature-grid">
<div className="feature-item">3, 6, 9, 12, 18, 24 month tenures</div>
<div className="feature-item">Available on purchases ≥ ₹2,500</div>
<div className="feature-item">Works with major bank cards</div>
<div className="feature-item">No Cost EMI options available</div>
</div>

## Integration Options

<div className="integration-grid">
<div className="integration-card">
<h3>Basic Integration</h3>
<p>Use PayU hosted checkout to automatically display EMI options.</p>
<ul>
<li>Minimal code changes</li>
<li>No custom UI development</li>
<li>Quick implementation</li>
</ul>
</div>
<div className="integration-card">
<h3>Advanced Integration</h3>
<p>Embed EMI calculator and options directly on your website.</p>
<ul>
<li>Custom styling</li>
<li>Enhanced user experience</li>
<li>Detailed EMI breakup</li>
</ul>
</div>
</div>

## Displaying EMI Options

### Method 1: Using Eligibility Check API

```html
<!-- Include PayU affordability.js -->
<script src="https://checkout-static.citruspay.com/affordability/affordability.js"></script>

<script>
// Initialize affordability widget
var affordability = new Affordability({
  merchantId: "YOUR_MERCHANT_ID",
  amount: 15000,
  selector: "#emi-container",
  currency: "INR"
});

// Check card eligibility
document.getElementById('check-emi').addEventListener('click', function() {
  var cardNumber = document.getElementById('ccnum').value;
  affordability.checkEligibility(cardNumber);
});
</script>
```

### Method 2: Enable EMI in PayU Hosted Checkout

```html
<input type="hidden" name="pg" value="cc" />
<input type="hidden" name="enforce_paymethod" value="creditcard|debitcard|emi" />
<input type="hidden" name="show_payment_mode" value="CC,DC,EMI" />
```

## Supported Banks & Card Types

| Bank Name | Credit Card | Debit Card | No Cost EMI |
|-----------|-------------|------------|-------------|
| HDFC Bank | ✓ | ✓ | ✓ |
| ICICI Bank | ✓ | ✓ | ✓ |
| Axis Bank | ✓ | ✓ | ✓ |
| SBI Card | ✓ | ✗ | ✓ |
| Kotak Bank | ✓ | ✗ | ✓ |
| RBL Bank | ✓ | ✗ | ✗ |

<div className="page-nav">
<strong>Next:</strong> <a href="#cardless-emi">Cardless EMI →</a>
</div>

</section>

</div>
</div>

{/* End of PayU Affordability Suite Documentation */}