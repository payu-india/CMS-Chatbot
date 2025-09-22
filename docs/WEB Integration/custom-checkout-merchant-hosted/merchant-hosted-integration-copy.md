---
title: Merchant Hosted Integration - COPY
deprecated: false
hidden: true
metadata:
  robots: index
---
# What you're building

A custom payment experience where you collect payment details on your own website and securely process them through PayU's APIs. Unlike the hosted solution, you have complete control over the UI/UX while PayU handles the secure payment processing. You pass order details, customer information, payment method-specific parameters (pg, bankcode), and a server-generated SHA-512 hash for integrity.

The PayU Merchant Hosted (Custom Checkout) integration involves the following steps:

<br />

<Cards columns={3}>
  <Card title="1. Start Integration" href="#step-1-start-integration" target="_blank" className="bg-gradient-to-r from-blue-400 to-blue-600 hover:from-blue-500 hover:to-blue-700 text-white shadow-lg rounded-xl border-0">
    Build custom payment forms and integrate with PayU APIs
  </Card>

  <Card title="2. Test Integration" href="#step-2-test-integration" className="bg-gradient-to-r from-teal-400 to-teal-600 hover:from-teal-500 hover:to-teal-700 text-white shadow-lg rounded-xl border-0">
    Test different payment modes with sandbox credentials
  </Card>

  <Card title="3. Go live Checklist" href="#step-3-going-live-your-final-checklist" className="bg-gradient-to-r from-indigo-400 to-indigo-600 hover:from-indigo-500 hover:to-indigo-700 text-white shadow-lg rounded-xl border-0">
    Complete security requirements and go live
  </Card>
</Cards>

<Callout icon="📘" theme="info">
  **Pre-requisites**

  * Merchant Key and Salt (test or production)
  * HTTPS success & failure URLs (surl, furl) reachable from the public internet
  * Ability to generate SHA-512 on the server (never in the browser)
  * Order ID generator for unique txnid
  * **PCI DSS compliance** if handling card data directly
  * SSL certificate for secure data transmission
</Callout>

<Callout icon="⚠️" theme="warning">
  **Security Requirements**

  * **PCI DSS Compliance**: Required when collecting card details on your website
  * **Never store sensitive payment data** like CVV, card numbers, or PINs
  * **Use HTTPS** for all payment-related communications
  * **Validate all inputs** on both client and server side
</Callout>

<Accordion title="Environment & Key Differences" icon="fa-globe">
  **Environment URLs**
  
  |                        |                                                                     |
  | :--------------------- | :------------------------------------------------------------------ |
  | Test Environment       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
  | Production Environment | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |

  **Key Differences from Hosted Checkout**
  
  | Feature | Merchant Hosted | PayU Hosted |
  |---------|----------------|-------------|
  | UI Control | Full customization | Limited customization |
  | Payment Data Collection | On your website | On PayU's website |
  | PCI DSS Compliance | Required | PayU handles it |
  | pg & bankcode parameters | **Required** | **Not required** |
  | Integration Complexity | Higher | Lower |
  | Security Responsibility | Shared | PayU handles most |
</Accordion>

## Step 1: Start Integration

Follow the below steps to complete the integration:

<Accordion title="Step 1.1: Understand Payment Mode Parameters" icon="fa-list-check">
  In Merchant Hosted checkout, you must specify the payment method using `pg` (payment gateway) and `bankcode` parameters. These vary by payment mode:

  **Payment Mode Matrix**

  | Payment Method | pg | bankcode | Additional Required Fields |
  |---|---|---|---|
  | **Credit/Debit Cards** | CC | VISA, MAST, AMEX, DINERS, RUPAY | ccnum, ccname, ccvv, ccexpmon, ccexpyr |
  | **Net Banking** | NB | Bank-specific (HDFC, ICICI, SBI, etc.) | Customer selects bank |
  | **UPI** | UPI | UPI | vpa (Virtual Payment Address) |
  | **Wallets** | CASH | PAYTM, PHONEPE, FREECHARGE, etc. | Wallet-specific parameters |
  | **EMI** | CC | Bank-specific EMI codes | emi_tenure, emi_amount |
  | **BNPL** | Varies | LAZYPAY, SIMPL, ZESTMONEY | Provider-specific fields |
  | **Pluxee Card** | MC | SODEXO | Pluxee card details |
  | **NEFT/RTGS** | NB | EFTAXTPV | Account number, IFSC code |

  <Callout icon="💡" theme="info">
    **Important**: Each payment mode requires specific parameters. Refer to individual payment method sections for detailed parameter lists.
  </Callout>
</Accordion>

<Accordion title="Step 1.2: Prepare the request parameters" icon="fa-cogs">
  **Common Parameters (Required for all payment modes)**

  <HTMLBlock>{`
  <div>
    <table>
      <thead>
        <tr>
          <th style="width: 10%;">Parameter</th>
          <th style="width: 75%; white-space: normal; word-break: break-word;">Type & Description</th>
          <th style="width: 15%;">Example</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            key<br>
            <code>mandatory</code>
          </td>
          <td style="white-space: normal; word-break: break-word;">
            <code>String</code> Merchant key provided by PayU during onboarding.
          </td>
          <td>JPG****.k</td>
        </tr>
        <tr>
          <td>
            txnid<br>
            <code>mandatory</code>
          </td>
          <td style="white-space: normal; word-break: break-word;">
            <code>String</code> The transaction ID is a reference number for a specific order generated by the merchant.
          </td>
          <td>ypl938459435</td>
        </tr>
        <tr>
          <td>
            amount<br>
            <code>mandatory</code>
          </td>
          <td style="white-space: normal; word-break: break-word;">
            <code>String</code> The payment amount for the transaction.
          </td>
          <td>10.00</td>
        </tr>
        <tr>
          <td>
            productinfo<br>
            <code>mandatory</code>
          </td>
          <td style="white-space: normal; word-break: break-word;">
            <code>String</code> A brief description of the product.
          </td>
          <td>iPhone</td>
        </tr>
        <tr>
          <td>
            firstname<br>
            <code>mandatory</code>
          </td>
          <td style="white-space: normal; word-break: break-word;">
            <code>String</code> The first name of the customer.
          </td>
          <td>Ashish</td>
        </tr>
        <tr>
          <td>
            email<br>
            <code>mandatory</code>
          </td>
          <td style="white-space: normal; word-break: break-word;">
            <code>String</code> The email address of the customer.
          </td>
          <td>test@payu.in</td>
        </tr>
        <tr>
          <td>
            phone<br>
            <code>mandatory</code>
          </td>
          <td style="white-space: normal; word-break: break-word;">
            <code>String</code> The phone number of the customer.
          </td>
          <td>9876543210</td>
        </tr>
        <tr>
          <td>
            pg<br>
            <code>mandatory</code>
          </td>
          <td style="white-space: normal; word-break: break-word;">
            <code>String</code> Payment gateway/method identifier. <strong>This is the key difference from hosted checkout.</strong>
          </td>
          <td>CC, NB, UPI, CASH</td>
        </tr>
        <tr>
          <td>
            bankcode<br>
            <code>conditional</code>
          </td>
          <td style="white-space: normal; word-break: break-word;">
            <code>String</code> Bank or payment provider specific code. Required for specific payment methods.
          </td>
          <td>HDFC, PAYTM, UPI</td>
        </tr>
        <tr>
          <td>
            surl<br>
            <code>mandatory</code>
          </td>
          <td style="white-space: normal; word-break: break-word;">
            <code>String</code> The success URL, which is the page PayU will redirect to if the transaction is successful.
          </td>
          <td>https://yoursite.com/success</td>
        </tr>
        <tr>
          <td>
            furl<br>
            <code>mandatory</code>
          </td>
          <td style="white-space: normal; word-break: break-word;">
            <code>String</code> The failure URL, which is the page PayU will redirect to if the transaction fails.
          </td>
          <td>https://yoursite.com/failure</td>
        </tr>
        <tr>
          <td>
            hash<br>
            <code>mandatory</code>
          </td>
          <td style="white-space: normal; word-break: break-word;">
            <code>String</code> It is the hash calculated by the merchant using SHA-512.
          </td>
          <td>[computed hash]</td>
        </tr>
      </tbody>
    </table>
  </div>
  `}</HTMLBlock>

  **Payment Method Specific Parameters**

  <Accordion title="Credit/Debit Card Parameters" icon="fa-credit-card">
    ```json
    {
      "pg": "CC",
      "bankcode": "VISA", // or MAST, AMEX, DINERS, RUPAY
      "ccnum": "4111111111111111",
      "ccname": "John Doe",
      "ccvv": "123",
      "ccexpmon": "12",
      "ccexpyr": "2025"
    }
    ```
    
    **Additional Requirements:**
    - PCI DSS compliance mandatory
    - Use LUHN algorithm for card validation
    - 3D Secure authentication required
  </Accordion>

  <Accordion title="Net Banking Parameters" icon="fa-university">
    ```json
    {
      "pg": "NB",
      "bankcode": "HDFC" // Bank-specific codes
    }
    ```
    
    **Popular Bank Codes:**
    - HDFC Bank: `HDFC`
    - ICICI Bank: `ICICI`
    - State Bank of India: `SBI`
    - Axis Bank: `AXIS`
    - Test Environment: `TESTPGNB`
  </Accordion>

  <Accordion title="UPI Parameters" icon="fa-mobile">
    ```json
    {
      "pg": "UPI",
      "bankcode": "UPI",
      "vpa": "customer@paytm" // Virtual Payment Address
    }
    ```
    
    **UPI Flows Supported:**
    - Collect Flow (VPA-based)
    - Intent Flow (App-based)
    - Smart Intent Flow
  </Accordion>

  <Accordion title="Wallet Parameters" icon="fa-wallet">
    ```json
    {
      "pg": "CASH",
      "bankcode": "PAYTM" // or PHONEPE, FREECHARGE, etc.
    }
    ```
    
    **Supported Wallets:**
    - PayTM: `PAYTM`
    - PhonePe: `PHONEPE`
    - FreeCharge: `FREECHARGE`
    - Amazon Pay: `AMAZONPAY`
  </Accordion>
</Accordion>

<Accordion title="Step 1.3: Generate Hash" icon="fa-key">
  The hash generation for merchant hosted is identical to hosted checkout:

  ```json
  key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|SALT
  ```

  **Sample Hash Generation (PHP)**
  ```php
  $key = "JP***g";
  $txnid = "TXN" . time();
  $amount = "100.00";
  $productinfo = "Test Product";
  $firstname = "John";
  $email = "john@example.com";
  $salt = "your_salt_here";
  
  $hash_string = $key . "|" . $txnid . "|" . $amount . "|" . $productinfo . "|" . $firstname . "|" . $email . "|||||||||||" . $salt;
  $hash = strtolower(hash('sha512', $hash_string));
  ```

  **Sample Hash Generation (Node.js)**
  ```javascript
  const crypto = require('crypto');
  
  const hashString = `${key}|${txnid}|${amount}|${productinfo}|${firstname}|${email}|||||||||||${salt}`;
  const hash = crypto.createHash('sha512').update(hashString).digest('hex');
  ```

  * Use empty strings for missing udf fields
  * Always compute hash on server-side
  * Include the lowercase hex digest as hash parameter
</Accordion>

<Accordion title="Step 1.4: Build Payment Forms" icon="fa-code">
  Create payment forms for different payment methods on your website:

  **Card Payment Form**
  ```html
  <form id="cardPaymentForm" action="https://test.payu.in/_payment" method="post">
    <!-- Hidden fields -->
    <input type="hidden" name="key" value="JP***g">
    <input type="hidden" name="txnid" value="TXN123456">
    <input type="hidden" name="amount" value="100.00">
    <input type="hidden" name="productinfo" value="Test Product">
    <input type="hidden" name="firstname" value="John">
    <input type="hidden" name="email" value="john@example.com">
    <input type="hidden" name="phone" value="9876543210">
    <input type="hidden" name="pg" value="CC">
    <input type="hidden" name="surl" value="https://yoursite.com/success">
    <input type="hidden" name="furl" value="https://yoursite.com/failure">
    <input type="hidden" name="hash" value="[computed_hash]">
    
    <!-- Card details -->
    <input type="text" name="ccnum" placeholder="Card Number" required>
    <input type="text" name="ccname" placeholder="Name on Card" required>
    <input type="text" name="ccvv" placeholder="CVV" required>
    <input type="text" name="ccexpmon" placeholder="MM" required>
    <input type="text" name="ccexpyr" placeholder="YYYY" required>
    <input type="hidden" name="bankcode" value="VISA">
    
    <button type="submit">Pay Now</button>
  </form>
  ```

  **UPI Payment Form**
  ```html
  <form id="upiPaymentForm" action="https://test.payu.in/_payment" method="post">
    <!-- Hidden fields -->
    <input type="hidden" name="key" value="JP***g">
    <input type="hidden" name="txnid" value="TXN123456">
    <input type="hidden" name="amount" value="100.00">
    <input type="hidden" name="productinfo" value="Test Product">
    <input type="hidden" name="firstname" value="John">
    <input type="hidden" name="email" value="john@example.com">
    <input type="hidden" name="phone" value="9876543210">
    <input type="hidden" name="pg" value="UPI">
    <input type="hidden" name="bankcode" value="UPI">
    <input type="hidden" name="surl" value="https://yoursite.com/success">
    <input type="hidden" name="furl" value="https://yoursite.com/failure">
    <input type="hidden" name="hash" value="[computed_hash]">
    
    <!-- UPI VPA -->
    <input type="text" name="vpa" placeholder="Enter UPI ID (e.g., user@paytm)" required>
    
    <button type="submit">Pay with UPI</button>
  </form>
  ```

  **Net Banking Form**
  ```html
  <form id="netBankingForm" action="https://test.payu.in/_payment" method="post">
    <!-- Hidden fields -->
    <input type="hidden" name="key" value="JP***g">
    <input type="hidden" name="txnid" value="TXN123456">
    <input type="hidden" name="amount" value="100.00">
    <input type="hidden" name="productinfo" value="Test Product">
    <input type="hidden" name="firstname" value="John">
    <input type="hidden" name="email" value="john@example.com">
    <input type="hidden" name="phone" value="9876543210">
    <input type="hidden" name="pg" value="NB">
    <input type="hidden" name="surl" value="https://yoursite.com/success">
    <input type="hidden" name="furl" value="https://yoursite.com/failure">
    <input type="hidden" name="hash" value="[computed_hash]">
    
    <!-- Bank selection -->
    <select name="bankcode" required>
      <option value="">Select Bank</option>
      <option value="HDFC">HDFC Bank</option>
      <option value="ICICI">ICICI Bank</option>
      <option value="SBI">State Bank of India</option>
      <option value="AXIS">Axis Bank</option>
    </select>
    
    <button type="submit">Pay with Net Banking</button>
  </form>
  ```

  <Callout icon="🔒" theme="warning">
    **Security Best Practices**
    
    - Never store card details in browser localStorage/sessionStorage
    - Validate all inputs on both client and server side
    - Use HTTPS for all form submissions
    - Implement proper error handling
    - Mask sensitive data in logs
  </Callout>
</Accordion>

<Accordion title="Step 1.5: Response handling & hash verification" icon="fa-shield-check">
  Response handling is identical to hosted checkout. After payment completion:

  **Sample Success Response**
  ```json
  mihpayid=403993715531077182
  mode=CC
  status=success
  unmappedstatus=captured
  key=JPM7Fg
  txnid=TXN12345
  amount=1000.00
  productinfo=Test Product
  firstname=John
  email=john@example.com
  phone=9876543210
  pg_type=CC-PG
  bankcode=VISA
  bank_ref_num=896193988312194700
  hash=<response_hash>
  ```

  **Response verification using reverse hashing**
  ```json
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  **PHP Response Verification**
  ```php
  $salt = "your_salt_here";
  $status = $_POST['status'];
  $firstname = $_POST['firstname'];
  $amount = $_POST['amount'];
  $txnid = $_POST['txnid'];
  $hash = $_POST['hash'];
  
  $retHashSeq = $salt.'|'.$status.'|||||||||||'.$_POST['udf5'].'|'.$_POST['udf4'].'|'.$_POST['udf3'].'|'.$_POST['udf2'].'|'.$_POST['udf1'].'|'.$_POST['email'].'|'.$firstname.'|'.$_POST['productinfo'].'|'.$amount.'|'.$txnid.'|'.$_POST['key'];
  
  $retHash = hash("sha512", $retHashSeq);
  
  if(hash_equals($retHash, $hash)) {
      // Hash verified - process the response
      if($status == 'success') {
          // Payment successful
      } else {
          // Payment failed
      }
  } else {
      // Hash verification failed
  }
  ```
</Accordion>

<Accordion title="Step 1.6: Verify the payment" icon="fa-magnifying-glass">
  Use the same verification API as hosted checkout:

  **Verification API Endpoints**

  |                        |                                                                                                              |
  | :--------------------- | :----------------------------------------------------------------------------------------------------------- |
  | Test Environment       | [https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2) |
  | Production Environment | [https://info.payu.in/merchant/postservice.php?form=2](https://info.payu.in/merchant/postservice.php?form=2) |

  **Sample Verification Request**
  ```curl
  curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=JP***g' \
  --data-urlencode 'command=verify_payment' \
  --data-urlencode 'var1=TXN123456' \
  --data-urlencode 'hash=[verification_hash]'
  ```

  The verification API response format is identical to hosted checkout.
</Accordion>

<br />

## Step 2: Test Integration

Test your merchant hosted integration thoroughly across all payment modes:

<Accordion title="Step 2.1: Pre-Integration Security Checklist" icon="fa-check-circle">
  Before testing payments, ensure your security setup is complete:

  **Security Requirements**
  1. **SSL Certificate**: Ensure your website has a valid SSL certificate
  2. **HTTPS Enforcement**: All payment pages must use HTTPS
  3. **PCI DSS Assessment**: Complete Self-Assessment Questionnaire if handling card data
  4. **Input Validation**: Implement client and server-side validation
  5. **Hash Validation**: Verify request and response hashes
  6. **Error Handling**: Implement proper error handling for failed payments

  **Test Environment Setup**
  - Use test merchant credentials
  - Point to `https://test.payu.in/_payment`
  - Implement proper logging for debugging
</Accordion>

<Accordion title="Step 2.2: Test Card Payments" icon="fa-credit-card">
  **Test Card Details**
  
  | Card Type | Card Number | CVV | Expiry | Expected Result |
  |-----------|-------------|-----|--------|----------------|
  | Visa | 4111111111111111 | 123 | Any future date | Success |
  | MasterCard | 5123456789012346 | 123 | Any future date | Success |
  | Amex | 378282246310005 | 1234 | Any future date | Success |
  | Failed Card | 4111111111111112 | 123 | Any future date | Failure |

  **Test Flow**
  1. Fill card payment form with test card details
  2. Set `pg=CC` and appropriate `bankcode` (VISA, MAST, AMEX)
  3. Submit form to PayU test endpoint
  4. Complete 3D Secure authentication (use OTP: 123456)
  5. Verify success/failure response
  6. Validate response hash
  7. Check transaction in PayU test dashboard

  **Sample Test Form Submission**
  ```javascript
  // Dynamic form generation for testing
  function testCardPayment() {
    const form = document.createElement('form');
    form.method = 'POST';
    form.action = 'https://test.payu.in/_payment';
    
    const fields = {
      key: 'JP***g',
      txnid: 'TEST_' + Date.now(),
      amount: '100.00',
      productinfo: 'Test Product',
      firstname: 'Test',
      email: 'test@example.com',
      phone: '9876543210',
      pg: 'CC',
      bankcode: 'VISA',
      ccnum: '4111111111111111',
      ccname: 'Test User',
      ccvv: '123',
      ccexpmon: '12',
      ccexpyr: '2025',
      surl: window.location.origin + '/success',
      furl: window.location.origin + '/failure',
      hash: generateHash() // Implement hash generation
    };
    
    for (let key in fields) {
      const input = document.createElement('input');
      input.type = 'hidden';
      input.name = key;
      input.value = fields[key];
      form.appendChild(input);
    }
    
    document.body.appendChild(form);
    form.submit();
  }
  ```
</Accordion>

<Accordion title="Step 2.3: Test UPI Payments" icon="fa-mobile">
  **Test UPI IDs**
  
  | UPI ID | Expected Result |
  |--------|----------------|
  | testsuccess@payu | Success |
  | testfailure@payu | Failure |
  | success@razorpay | Success |
  | failure@razorpay | Failure |

  **UPI Test Flow**
  1. Create UPI payment form with `pg=UPI` and `bankcode=UPI`
  2. Enter test UPI ID
  3. Submit to PayU test endpoint
  4. Verify UPI authentication flow
  5. Check transaction status
  6. Validate response hash

  **Sample UPI Test**
  ```html
  <form action="https://test.payu.in/_payment" method="post">
    <input type="hidden" name="key" value="JP***g">
    <input type="hidden" name="txnid" value="UPI_TEST_123">
    <input type="hidden" name="amount" value="50.00">
    <input type="hidden" name="productinfo" value="UPI Test">
    <input type="hidden" name="firstname" value="Test">
    <input type="hidden" name="email" value="test@example.com">
    <input type="hidden" name="phone" value="9876543210">
    <input type="hidden" name="pg" value="UPI">
    <input type="hidden" name="bankcode" value="UPI">
    <input type="text" name="vpa" value="testsuccess@payu">
    <input type="hidden" name="surl" value="https://yoursite.com/success">
    <input type="hidden" name="furl" value="https://yoursite.com/failure">
    <input type="hidden" name="hash" value="[computed_hash]">
    <input type="submit" value="Test UPI Payment">
  </form>
  ```
</Accordion>

<Accordion title="Step 2.4: Test Net Banking" icon="fa-university">
  **Test Bank Codes**
  
  | Bank | Bank Code | Expected Result |
  |------|-----------|----------------|
  | Test Bank | TESTPGNB | Success |
  | HDFC Bank | HDFC | Success (in test) |
  | ICICI Bank | ICICI | Success (in test) |

  **Net Banking Test Flow**
  1. Select bank from dropdown (`bankcode`)
  2. Set `pg=NB`
  3. Submit to PayU test endpoint
  4. Complete bank authentication simulation
  5. Verify transaction status

  **Sample Net Banking Test**
  ```html
  <form action="https://test.payu.in/_payment" method="post">
    <input type="hidden" name="key" value="JP***g">
    <input type="hidden" name="txnid" value="NB_TEST_123">
    <input type="hidden" name="amount" value="200.00">
    <input type="hidden" name="productinfo" value="Net Banking Test">
    <input type="hidden" name="firstname" value="Test">
    <input type="hidden" name="email" value="test@example.com">
    <input type="hidden" name="phone" value="9876543210">
    <input type="hidden" name="pg" value="NB">
    <input type="hidden" name="bankcode" value="TESTPGNB">
    <input type="hidden" name="surl" value="https://yoursite.com/success">
    <input type="hidden" name="furl" value="https://yoursite.com/failure">
    <input type="hidden" name="hash" value="[computed_hash]">
    <input type="submit" value="Test Net Banking">
  </form>
  ```
</Accordion>

<Accordion title="Step 2.5: Test Wallet Payments" icon="fa-wallet">
  **Test Wallet Codes**
  
  | Wallet | Bank Code | Expected Result |
  |--------|-----------|----------------|
  | PayTM | PAYTM | Success |
  | PhonePe | PHONEPE | Success |
  | FreeCharge | FREECHARGE | Success |

  **Wallet Test Flow**
  1. Select wallet provider (`bankcode`)
  2. Set `pg=CASH`
  3. Submit to PayU test endpoint
  4. Complete wallet authentication
  5. Verify transaction status

  **Test All Payment Modes Checklist**
  - [ ] Credit/Debit Cards (Visa, MasterCard, Amex)
  - [ ] UPI (Collect and Intent flows)
  - [ ] Net Banking (Multiple banks)
  - [ ] Wallets (PayTM, PhonePe, etc.)
  - [ ] EMI payments
  - [ ] BNPL payments
  - [ ] Failed transaction scenarios
  - [ ] Hash verification for all responses
  - [ ] Transaction status in PayU dashboard
</Accordion>

<br />

## Step 3: Going Live: Your Final Checklist

Complete security requirements and deploy to production:

<Accordion title="Step 3.1: Security Compliance Requirements" icon="fa-lock">
  **PCI DSS Compliance (For Card Payments)**
  
  If you're collecting card details on your website, you must complete:
  
  1. **Self-Assessment Questionnaire A-EP**: Download and complete the [PCI DSS SAQ A-EP form](https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2-SAQ-A_EP-rev1_1.pdf)
  2. **Attestation of Compliance**: Submit completed form to PayU
  3. **Network Security**: Implement proper firewall and network security
  4. **Data Protection**: Never store sensitive card data (PAN, CVV, etc.)
  5. **Access Control**: Implement proper user access controls
  6. **Monitoring**: Set up security monitoring and logging

  **SSL/TLS Requirements**
  - Valid SSL certificate from trusted CA
  - TLS 1.2 or higher
  - Strong cipher suites
  - Proper certificate chain

  **Code Security Requirements**
  - Input validation on all payment fields
  - SQL injection prevention
  - XSS protection
  - CSRF protection
  - Secure session management

  <Callout icon="⚠️" theme="warning">
    **Important**: Failure to comply with PCI DSS requirements may result in account suspension and liability for fraud.
  </Callout>
</Accordion>

<Accordion title="Step 3.2: Update to Production Credentials" icon="fa-key">
  **Switch to Live Environment**
  
  1. **Update API Credentials**
     - Replace test merchant key with live key
     - Replace test salt with live salt
     - Update endpoint URL to `https://secure.payu.in/_payment`

  2. **Update Verification API URL**
     - Change from test to production verification endpoint
     - Update URL to `https://info.payu.in/merchant/postservice.php?form=2`

  3. **Update Webhook URLs**
     - Configure production webhook endpoints
     - Ensure HTTPS URLs are accessible from internet
     - Test webhook reception

  **Production Configuration Sample**
  ```php
  // Production configuration
  define('PAYU_BASE_URL', 'https://secure.payu.in');
  define('PAYU_PAYMENT_URL', PAYU_BASE_URL . '/_payment');
  define('PAYU_VERIFY_URL', 'https://info.payu.in/merchant/postservice.php?form=2');
  define('MERCHANT_KEY', 'your_live_merchant_key');
  define('MERCHANT_SALT', 'your_live_salt');
  ```

  ```javascript
  // Production configuration for Node.js
  const config = {
    payuBaseUrl: 'https://secure.payu.in',
    paymentUrl: 'https://secure.payu.in/_payment',
    verifyUrl: 'https://info.payu.in/merchant/postservice.php?form=2',
    merchantKey: 'your_live_merchant_key',
    merchantSalt: 'your_live_salt'
  };
  ```
</Accordion>

<Accordion title="Step 3.3: Final Integration Verification" icon="fa-clipboard-check">
  **Pre-Launch Checklist**
  
  **✅ Security Verification**
  - [ ] PCI DSS compliance completed (if applicable)
  - [ ] SSL certificate installed and verified
  - [ ] All payment forms use HTTPS
  - [ ] Hash validation implemented for requests and responses
  - [ ] Input validation on all fields
  - [ ] No sensitive data logged or stored
  - [ ] Error handling implemented
  - [ ] Security headers configured

  **✅ Technical Integration**
  - [ ] Production credentials configured
  - [ ] Payment endpoints updated to production URLs
  - [ ] All payment modes tested in production
  - [ ] Webhook endpoints configured and tested
  - [ ] Response handling and hash verification working
  - [ ] Transaction verification API integration tested
  - [ ] Database integration for transaction storage
  - [ ] Email/SMS notifications configured

  **✅ Live Transaction Testing**
  - [ ] Conduct small live transactions for each payment mode
  - [ ] Verify successful transactions in PayU dashboard
  - [ ] Test failed transaction handling
  - [ ] Verify webhook reception for live transactions
  - [ ] Test refund process (if applicable)
  - [ ] Verify settlement process

  **✅ User Experience**
  - [ ] Payment forms user-friendly and responsive
  - [ ] Clear error messages for failed payments
  - [ ] Success/failure pages properly designed
  - [ ] Mobile-responsive payment interface
  - [ ] Loading states during payment processing
  - [ ] Proper redirection flow

  **✅ Business Process**
  - [ ] Order management system integration
  - [ ] Inventory management integration
  - [ ] Customer notification system
  - [ ] Reconciliation process defined
  - [ ] Support process for payment issues
  - [ ] Refund/chargeback handling process

  **✅ Monitoring & Analytics**
  - [ ] Transaction monitoring dashboard
  - [ ] Payment success rate tracking
  - [ ] Error rate monitoring
  - [ ] Performance monitoring
  - [ ] Alert system for payment failures
  - [ ] Regular reconciliation reports

  <Callout icon="🚀" theme="success">
    **Go Live!** Once all checklist items are completed and verified, your Merchant Hosted PayU integration is ready for production use.
  </Callout>
</Accordion>

<br />

## Payment Mode Specific Integration Guides

<Cards columns={2}>
  <Card title="Cards Integration" href="https://docs.payu.in/docs/collect-payments-with-cards-seamless" className="bg-gradient-to-r from-red-400 to-red-600 hover:from-red-500 hover:to-red-700 text-white shadow-lg rounded-xl border-0">
    Credit/Debit cards with 3D Secure authentication
  </Card>

  <Card title="Net Banking Integration" href="https://docs.payu.in/docs/collect-payments-with-net-banking-seamless" className="bg-gradient-to-r from-green-400 to-green-600 hover:from-green-500 hover:to-green-700 text-white shadow-lg rounded-xl border-0">
    Bank account based payments
  </Card>

  <Card title="UPI Integration" href="https://docs.payu.in/docs/collect-payments-with-upi-seamless" className="bg-gradient-to-r from-orange-400 to-orange-600 hover:from-orange-500 hover:to-orange-700 text-white shadow-lg rounded-xl border-0">
    Unified Payments Interface
  </Card>

  <Card title="Wallets Integration" href="https://docs.payu.in/docs/collect-payments-with-wallets-seamless" className="bg-gradient-to-r from-pink-400 to-pink-600 hover:from-pink-500 hover:to-pink-700 text-white shadow-lg rounded-xl border-0">
    PayTM, PhonePe, and other wallets
  </Card>

  <Card title="EMI Integration" href="https://docs.payu.in/docs/collect-payments-with-emi-seamless" className="bg-gradient-to-r from-cyan-400 to-cyan-600 hover:from-cyan-500 hover:to-cyan-700 text-white shadow-lg rounded-xl border-0">
    Easy Monthly Installments
  </Card>

  <Card title="BNPL Integration" href="https://docs.payu.in/docs/collect-payments-with-bnpl" className="bg-gradient-to-r from-violet-400 to-violet-600 hover:from-violet-500 hover:to-violet-700 text-white shadow-lg rounded-xl border-0">
    Buy Now Pay Later solutions
  </Card>
</Cards>

<br />

## Additional Resources

<Callout icon="📚" theme="info">
  **Reference Documentation**
  
  * [Merchant Hosted Checkout Overview](https://docs.payu.in/docs/custom-checkout-merchant-hosted)
  * [Hash Generation Guide](https://docs.payu.in/docs/generate-hash-payu-hosted)
  * [Webhooks Documentation](https://docs.payu.in/docs/webhooks-for-payments)
  * [Error Codes Reference](https://docs.payu.in/reference/error-codes)
  * [PCI DSS Compliance Guide](https://docs.payu.in/docs/pci-dss-compliance)
  * [Test Credentials](https://docs.payu.in/docs/test-cards-upi-id-and-wallets)
</Callout>