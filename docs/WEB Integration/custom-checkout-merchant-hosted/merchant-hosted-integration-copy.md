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
  <Card title="1. Start Integration" href="#step-1-start-integration" target="_blank" className="bg-blue text-white shadow-lg rounded-xl border-0">
    Build custom payment forms and integrate with PayU APIs
  </Card>

  <Card title="2. Test Integration" href="#step-2-test-integration" className="bg-teal text-white shadow-lg rounded-xl border-0">
    Test different payment modes with sandbox credentials
  </Card>

  <Card title="3. Go live Checklist" href="#step-3-going-live-your-final-checklist" className="bg-indigo text-white shadow-lg rounded-xl border-0">
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

<Accordion title="Environment" icon="fa-globe">
  **Environment URLs**

  |                        |                                                                     |
  | :--------------------- | :------------------------------------------------------------------ |
  | Test Environment       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
  | Production Environment | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |
</Accordion>

## Step 1: Start Integration

Follow the below steps to complete the integration:

<Accordion title="Step 1.1: Understand Payment Mode Parameters" icon="fa-list-check">
  In Merchant Hosted checkout, you must specify the payment method using `pg` (payment gateway) and `bankcode` parameters. These vary by payment mode:

  **Payment Mode Matrix**

  | Payment Method         | pg       | bankcode                               | Additional Required Fields             |
  | ---------------------- | -------- | -------------------------------------- | -------------------------------------- |
  | **Credit/Debit Cards** | CC       | VISA, MAST, AMEX, DINERS, RUPAY        | ccnum, ccname, ccvv, ccexpmon, ccexpyr |
  | **Net Banking**        | NB       | Bank-specific (HDFC, ICICI, SBI, etc.) | Customer selects bank                  |
  | **UPI**                | UPI      | UPI                                    | vpa (Virtual Payment Address)          |
  | **Wallets**            | CASH     | PAYTM, PHONEPE, FREECHARGE, etc.       | Wallet-specific parameters             |
  | **EMI**                | EMI      | Bank-specific EMI codes                | emi\_planid, emi\_tenure               |
  | **BNPL**               | BNPL     | LAZYPAY, SIMPL, ZESTMONEY              | Provider-specific fields               |
  | **Pluxee Card**        | MC       | SODEXO                                 | Pluxee card details                    |
  | **NEFT/RTGS**          | NEFTRTGS | EFTAXIS, etc.                          | Bank account details                   |

  <Callout icon="💡" theme="info">
    **Important**: Each payment mode requires specific parameters. Refer to individual payment method tabs below for detailed parameter lists.
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

  ## Payment Method Specific Parameters

  <Tabs>
    <Tab title="💳 Cards">
      **Additional Parameters for Card Payments**

      | Parameter | Type   | Description                    | Example                                   |
      | --------- | ------ | ------------------------------ | ----------------------------------------- |
      | pg        | String | Payment gateway (mandatory)    | `CC`                                      |
      | bankcode  | String | Card type identifier           | `VISA`, `MAST`, `AMEX`, `DINERS`, `RUPAY` |
      | ccnum     | String | 13-19 digit card number        | `4111111111111111`                        |
      | ccname    | String | Name on card                   | `John Doe`                                |
      | ccvv      | String | 3-digit CVV (4-digit for AMEX) | `123`                                     |
      | ccexpmon  | String | Card expiry month (MM)         | `12`                                      |
      | ccexpyr   | String | Card expiry year (YYYY)        | `2025`                                    |

      **Sample Card Payment Request**

      ```html
      <form action="https://test.payu.in/_payment" method="post">
        <input type="hidden" name="key" value="JP***g" />
        <input type="hidden" name="txnid" value="TXN123456" />
        <input type="hidden" name="amount" value="500.00" />
        <input type="hidden" name="productinfo" value="Test Product" />
        <input type="hidden" name="firstname" value="John" />
        <input type="hidden" name="email" value="john@example.com" />
        <input type="hidden" name="phone" value="9876543210" />
        <input type="hidden" name="pg" value="CC" />
        <input type="hidden" name="bankcode" value="VISA" />
        <input type="hidden" name="ccnum" value="4111111111111111" />
        <input type="hidden" name="ccname" value="John Doe" />
        <input type="hidden" name="ccvv" value="123" />
        <input type="hidden" name="ccexpmon" value="12" />
        <input type="hidden" name="ccexpyr" value="2025" />
        <input type="hidden" name="surl" value="https://yoursite.com/success" />
        <input type="hidden" name="furl" value="https://yoursite.com/failure" />
        <input type="hidden" name="hash" value="[computed_hash]" />
        <input type="submit" value="Pay Now" />
      </form>
      ```

      **Important Security Notes:**

      * PCI DSS compliance mandatory
      * Use LUHN algorithm for card validation
      * 3D Secure authentication required
      * Never store card details on your server
    </Tab>

    <Tab title="🏦 Net Banking">
      **Additional Parameters for Net Banking**

      | Parameter | Type   | Description                 | Example                        |
      | --------- | ------ | --------------------------- | ------------------------------ |
      | pg        | String | Payment gateway (mandatory) | `NB`                           |
      | bankcode  | String | Bank identifier code        | `HDFC`, `ICICI`, `SBI`, `AXIS` |

      **Popular Bank Codes**

      | Bank Name            | Bank Code  |
      | -------------------- | ---------- |
      | HDFC Bank            | `HDFC`     |
      | ICICI Bank           | `ICICI`    |
      | State Bank of India  | `SBI`      |
      | Axis Bank            | `AXIS`     |
      | Punjab National Bank | `PNB`      |
      | Kotak Mahindra Bank  | `KOTAK`    |
      | Yes Bank             | `YES`      |
      | Test Environment     | `TESTPGNB` |

      **Sample Net Banking Request**

      ```html
      <form action="https://test.payu.in/_payment" method="post">
        <input type="hidden" name="key" value="JP***g" />
        <input type="hidden" name="txnid" value="NB_TXN123" />
        <input type="hidden" name="amount" value="200.00" />
        <input type="hidden" name="productinfo" value="Net Banking Test" />
        <input type="hidden" name="firstname" value="Test User" />
        <input type="hidden" name="email" value="test@example.com" />
        <input type="hidden" name="phone" value="9876543210" />
        <input type="hidden" name="pg" value="NB" />
        <input type="hidden" name="bankcode" value="HDFC" />
        <input type="hidden" name="surl" value="https://yoursite.com/success" />
        <input type="hidden" name="furl" value="https://yoursite.com/failure" />
        <input type="hidden" name="hash" value="[computed_hash]" />
        <input type="submit" value="Pay with Net Banking" />
      </form>
      ```
    </Tab>

    <Tab title="📱 UPI">
      **Additional Parameters for UPI Payments**

      | Parameter | Type   | Description                 | Example          |
      | --------- | ------ | --------------------------- | ---------------- |
      | pg        | String | Payment gateway (mandatory) | `UPI`            |
      | bankcode  | String | UPI identifier              | `UPI`            |
      | vpa       | String | Virtual Payment Address     | `customer@paytm` |

      **UPI Flows Supported:**

      * Collect Flow (VPA-based)
      * Intent Flow (App-based)
      * Smart Intent Flow

      **Sample UPI Request**

      ```html
      <form action="https://test.payu.in/_payment" method="post">
        <input type="hidden" name="key" value="JP***g" />
        <input type="hidden" name="txnid" value="UPI_TXN123" />
        <input type="hidden" name="amount" value="50.00" />
        <input type="hidden" name="productinfo" value="UPI Test" />
        <input type="hidden" name="firstname" value="Test User" />
        <input type="hidden" name="email" value="test@example.com" />
        <input type="hidden" name="phone" value="9876543210" />
        <input type="hidden" name="pg" value="UPI" />
        <input type="hidden" name="bankcode" value="UPI" />
        <input type="hidden" name="vpa" value="testsuccess@payu" />
        <input type="hidden" name="surl" value="https://yoursite.com/success" />
        <input type="hidden" name="furl" value="https://yoursite.com/failure" />
        <input type="hidden" name="hash" value="[computed_hash]" />
        <input type="submit" value="Pay with UPI" />
      </form>
      ```
    </Tab>

    <Tab title="👛 Wallets">
      **Additional Parameters for Wallet Payments**

      | Parameter | Type   | Description                 | Example                          |
      | --------- | ------ | --------------------------- | -------------------------------- |
      | pg        | String | Payment gateway (mandatory) | `CASH`                           |
      | bankcode  | String | Wallet provider code        | `PAYTM`, `PHONEPE`, `FREECHARGE` |

      **Supported Wallet Codes**

      | Wallet Name | Bank Code    |
      | ----------- | ------------ |
      | PayTM       | `PAYTM`      |
      | PhonePe     | `PHONEPE`    |
      | Mobikwik    | `MOBIKWIK`   |
      | FreeCharge  | `FREECHARGE` |
      | Ola Money   | `OLA`        |
      | Amazon Pay  | `AMAZONPAY`  |
      | JioMoney    | `JIO`        |

      **Sample Wallet Request**

      ```html
      <form action="https://test.payu.in/_payment" method="post">
        <input type="hidden" name="key" value="JP***g" />
        <input type="hidden" name="txnid" value="WALLET_TXN123" />
        <input type="hidden" name="amount" value="100.00" />
        <input type="hidden" name="productinfo" value="Wallet Test" />
        <input type="hidden" name="firstname" value="Test User" />
        <input type="hidden" name="email" value="test@example.com" />
        <input type="hidden" name="phone" value="9876543210" />
        <input type="hidden" name="pg" value="CASH" />
        <input type="hidden" name="bankcode" value="PAYTM" />
        <input type="hidden" name="surl" value="https://yoursite.com/success" />
        <input type="hidden" name="furl" value="https://yoursite.com/failure" />
        <input type="hidden" name="hash" value="[computed_hash]" />
        <input type="submit" value="Pay with Wallet" />
      </form>
      ```
    </Tab>

    <Tab title="💰 EMI">
      **Additional Parameters for EMI Payments**

      | Parameter   | Type   | Description                 | Example                 |
      | ----------- | ------ | --------------------------- | ----------------------- |
      | pg          | String | Payment gateway (mandatory) | `EMI`                   |
      | bankcode    | String | Bank EMI code               | Bank-specific EMI codes |
      | ccnum       | String | Card number for EMI         | `4111111111111111`      |
      | ccname      | String | Name on card                | `John Doe`              |
      | ccvv        | String | CVV                         | `123`                   |
      | ccexpmon    | String | Expiry month                | `12`                    |
      | ccexpyr     | String | Expiry year                 | `2025`                  |
      | emi\_planid | String | EMI plan identifier         | `1`                     |
      | emi\_tenure | String | EMI tenure in months        | `6`                     |

      **Sample EMI Request**

      ```html
      <form action="https://test.payu.in/_payment" method="post">
        <input type="hidden" name="key" value="JP***g" />
        <input type="hidden" name="txnid" value="EMI_TXN123" />
        <input type="hidden" name="amount" value="10000.00" />
        <input type="hidden" name="productinfo" value="Mobile" />
        <input type="hidden" name="firstname" value="John" />
        <input type="hidden" name="email" value="john@example.com" />
        <input type="hidden" name="phone" value="9876543210" />
        <input type="hidden" name="pg" value="EMI" />
        <input type="hidden" name="bankcode" value="HDFC" />
        <input type="hidden" name="ccnum" value="4111111111111111" />
        <input type="hidden" name="ccname" value="John Doe" />
        <input type="hidden" name="ccvv" value="123" />
        <input type="hidden" name="ccexpmon" value="12" />
        <input type="hidden" name="ccexpyr" value="2025" />
        <input type="hidden" name="emi_planid" value="1" />
        <input type="hidden" name="emi_tenure" value="6" />
        <input type="hidden" name="surl" value="https://yoursite.com/success" />
        <input type="hidden" name="furl" value="https://yoursite.com/failure" />
        <input type="hidden" name="hash" value="[computed_hash]" />
        <input type="submit" value="Pay with EMI" />
      </form>
      ```
    </Tab>

    <Tab title="📅 BNPL">
      **Additional Parameters for BNPL Payments**

      | Parameter | Type   | Description                 | Example                         |
      | --------- | ------ | --------------------------- | ------------------------------- |
      | pg        | String | Payment gateway (mandatory) | `BNPL`                          |
      | bankcode  | String | BNPL provider code          | `LAZYPAY`, `SIMPL`, `ZESTMONEY` |

      **BNPL Provider Codes**

      | Provider  | Bank Code   |
      | --------- | ----------- |
      | LazyPay   | `LAZYPAY`   |
      | Simpl     | `SIMPL`     |
      | ZestMoney | `ZESTMONEY` |
      | TwidPay   | `TWID`      |
      | FlexMoney | `FLEXMONEY` |

      **Sample BNPL Request**

      ```html
      <form action="https://test.payu.in/_payment" method="post">
        <input type="hidden" name="key" value="JP***g" />
        <input type="hidden" name="txnid" value="BNPL_TXN123" />
        <input type="hidden" name="amount" value="5000.00" />
        <input type="hidden" name="productinfo" value="Product Description" />
        <input type="hidden" name="firstname" value="John" />
        <input type="hidden" name="email" value="john@example.com" />
        <input type="hidden" name="phone" value="9876543210" />
        <input type="hidden" name="pg" value="BNPL" />
        <input type="hidden" name="bankcode" value="LAZYPAY" />
        <input type="hidden" name="surl" value="https://yoursite.com/success" />
        <input type="hidden" name="furl" value="https://yoursite.com/failure" />
        <input type="hidden" name="hash" value="[computed_hash]" />
        <input type="submit" value="Pay with BNPL" />
      </form>
      ```
    </Tab>

    <Tab title="🎫 Pluxee Card">
      **Additional Parameters for Pluxee Card Payments**

      | Parameter          | Type   | Description                  | Example                        |
      | ------------------ | ------ | ---------------------------- | ------------------------------ |
      | pg                 | String | Payment gateway (mandatory)  | `MC`                           |
      | bankcode           | String | Pluxee identifier            | `SODEXO`                       |
      | ccnum              | String | 16-digit card number         | `637513XXXXXX9318`             |
      | ccname             | String | Name on card                 | `John Doe`                     |
      | ccvv               | String | 3-digit CVV                  | `123`                          |
      | ccexpmon           | String | Expiry month                 | `05`                           |
      | ccexpyr            | String | Expiry year                  | `2025`                         |
      | save\_sodexo\_card | String | Save card for future use     | `1` (save), `0` (don't save)   |
      | is\_check\_balance | String | Check balance before payment | `1` (check), `0` (don't check) |

      **Sample Pluxee Card Request**

      ```html
      <form action="https://test.payu.in/_payment" method="post">
        <input type="hidden" name="key" value="JP***g" />
        <input type="hidden" name="txnid" value="PLUXEE_TXN123" />
        <input type="hidden" name="amount" value="100.00" />
        <input type="hidden" name="productinfo" value="Meal Voucher" />
        <input type="hidden" name="firstname" value="John" />
        <input type="hidden" name="email" value="john@example.com" />
        <input type="hidden" name="phone" value="9876543210" />
        <input type="hidden" name="pg" value="MC" />
        <input type="hidden" name="bankcode" value="SODEXO" />
        <input type="hidden" name="ccnum" value="637513XXXXXX9318" />
        <input type="hidden" name="ccname" value="John Doe" />
        <input type="hidden" name="ccvv" value="123" />
        <input type="hidden" name="ccexpmon" value="05" />
        <input type="hidden" name="ccexpyr" value="2025" />
        <input type="hidden" name="save_sodexo_card" value="0" />
        <input type="hidden" name="is_check_balance" value="1" />
        <input type="hidden" name="surl" value="https://yoursite.com/success" />
        <input type="hidden" name="furl" value="https://yoursite.com/failure" />
        <input type="hidden" name="hash" value="[computed_hash]" />
        <input type="submit" value="Pay with Pluxee Card" />
      </form>
      ```
    </Tab>

    <Tab title="🏛️ NEFT/RTGS">
      **Additional Parameters for NEFT/RTGS Payments**

      | Parameter | Type   | Description                 | Example    |
      | --------- | ------ | --------------------------- | ---------- |
      | pg        | String | Payment gateway (mandatory) | `NEFTRTGS` |
      | bankcode  | String | Bank NEFT/RTGS code         | `EFTAXIS`  |

      **NEFT/RTGS Bank Codes**

      | Bank Name  | Bank Code  |
      | ---------- | ---------- |
      | Axis Bank  | `EFTAXIS`  |
      | HDFC Bank  | `EFTHDFC`  |
      | ICICI Bank | `EFTICICI` |

      **Sample NEFT/RTGS Request**

      ```html
      <form action="https://test.payu.in/_payment" method="post">
        <input type="hidden" name="key" value="JP***g" />
        <input type="hidden" name="txnid" value="NEFT_TXN123" />
        <input type="hidden" name="amount" value="1000.00" />
        <input type="hidden" name="productinfo" value="Bank Transfer" />
        <input type="hidden" name="firstname" value="John" />
        <input type="hidden" name="email" value="john@example.com" />
        <input type="hidden" name="phone" value="9876543210" />
        <input type="hidden" name="pg" value="NEFTRTGS" />
        <input type="hidden" name="bankcode" value="EFTAXIS" />
        <input type="hidden" name="surl" value="https://yoursite.com/success" />
        <input type="hidden" name="furl" value="https://yoursite.com/failure" />
        <input type="hidden" name="hash" value="[computed_hash]" />
        <input type="submit" value="Pay with NEFT/RTGS" />
      </form>
      ```

      **Note**: Customer will be redirected to bank interface for completing NEFT/RTGS transfer.
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Step 1.3: Generate Hash" icon="fa-key">
  ```json
  key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|SALT
  ```

  tab: PHP \`\`\`php $key = "JP\*\*\*g"; $txnid = "TXN" . time(); $amount = "100.00"; $productinfo = "Test Product"; $firstname = "John"; $email = "[john@example.com](mailto:john@example.com)"; $salt = "your\_salt\_here";  $hash\_string = $key . "|" . $txnid . "|" . $amount . "|" . $productinfo . "|" . $firstname . "|" . $email . "|||||||||||" . $salt; $hash = strtolower(hash('sha512', $hash\_string));
  tab: Node.js
  const crypto = require('crypto');  const hashString = `${key}|${txnid}|${amount}|${productinfo}|${firstname}|${email}|||||||||||${salt}`; const hash = crypto.createHash('sha512').update(hashString).digest('hex');

  ````
    * Use empty strings for missing udf fields
    * Always compute hash on server-side
    * Include the lowercase hex digest as hash parameter
  </Accordion>

  <Accordion title="Step 1.4: Response handling & hash verification" icon="fa-shield-check">
    **Response Handling:**

    After the customer completes or abandons the payment, PayU POSTs back to your return URL with URL-encoded fields (form post). This payload includes the transaction status, txnid, mihpayid, and a hash you must verify (reverse hashing) before trusting the result.

    Sample surl/furl payload:

    ```json Success
    mihpayid=403993715531077182
    mode=CC
    status=success
    unmappedstatus=captured
    key=JPM7Fg
    txnid=TXN12345
    amount=1000.00
    productinfo=Pro Plan
    firstname=Aditi
    email=aditi@example.com
    phone=9999999999
    udf1=
    ...
    udf5=
    PG_TYPE=CC-PG
    bankcode=CC
    bank_ref_num=896193988312194700
    field1=...
    field9=Transaction is Successful
    hash=<response_hash>
  ````
  ```json Failure
  mihpayid=403993715531077182
  mode=CC
  status=failure
  unmappedstatus=failed
  key=JPM7Fg
  txnid=TXN12345
  amount=1000.00
  productinfo=Pro Plan
  firstname=Aditi
  email=aditi@example.com
  phone=9999999999
  udf1=
  ...
  udf5=
  PG_TYPE=CC-PG
  bankcode=CC
  bank_ref_num=
  field1=
  field2=
  ...
  field9=Transaction Failed
  error=E000
  error_Message=Bank was unable to authenticate
  hash=<response_hash>
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

<Accordion title="Step 1.5: Verify the payment" icon="fa-magnifying-glass">
  <Tabs>
    <Tab title="1. Verify using Webhooks">
      Configure the webhooks to monitor the status of payments.\
      Webhooks enable a server to communicate with another server by sending an HTTP callback or message.\
      These callbacks are triggered by specific events or instances and operate at the server-to-server (S2S) level.

      👉 For more details, refer to [Webhooks for Payments](https://docs.payu.in/reference/webhooks). <br />
    </Tab>

    <Tab title="2. Verify using Verify Payments API">
      **Environment**

      |                        |                                                                                                              |
      | :--------------------- | :----------------------------------------------------------------------------------------------------------- |
      | Test Environment       | [https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2) |
      | Production Environment | [https://info.payu.in/merchant/postservice.php?form=2](https://info.payu.in/merchant/postservice.php?form=2) |

      <Accordion title="Sample request" icon="fa-code">
        ```curl
        curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
        --header 'Content-Type: application/x-www-form-urlencoded' \
        --data-urlencode 'key=JP***g' \
        --data-urlencode 'command=verify_payment' \
        --data-urlencode 'var1=IhfgcZnXR4o4nB' \
        --data-urlencode 'hash=<<calculated_hash_here>>'
        ```
      </Accordion>

      <Accordion title="Sample response" icon="fa-reply">
        <br />

        ```json Success Response
        If credit card payment is made, the response is similar to the following:
        {
        "status": 1,
        "msg": "1 out of 1 Transactions Fetched Successfully",
        "transaction_details": {
           "1733900931584": {
               "mihpayid": "21820644083",
               "request_id": null,
               "bank_ref_num": null,
               "amt": "1.00",
               "transaction_amount": "1.00",
               "txnid": "1733900931584",
               "additional_charges": "0.00",
               "productinfo": "Macbook Pro",
               "firstname": "Abc",
               "bankcode": "MAST",
               "udf1": "udf1",
               "udf2": "udf2",
               "udf3": "udf3",
               "udf4": "udf4",
               "udf5": "udf5",
               "field2": null,
               "field9": "OTP/ATM page expired due to no user action",
               "error_code": "E1602",
               "addedon": "2024-12-11 12:43:03",
               "payment_source": "payu",
               "card_type": "MAST",
               "error_Message": "Bank was unable to authenticate.",
               "net_amount_debit": "0.00",
               "disc": "0.00",
               "mode": "DC",
               "PG_TYPE": "DC-PG",
               "card_no": "XXXXXXXXXXXX7596",
               "status": "failure",
               "unmappedstatus": "dropped",
               "Merchant_UTR": null,
               "Settled_At": null,
               "cardhash": "095d184331be367bb92aa3eeecb57d0728de96cc598dd563d407982d75021149",
               "name_on_card": null,
               "card_token": "4e97156bc2d6320cdfe15",
               "field4": null,
               "threeDSVersion": "2.2.0",
               "offerAvailed": null
           }
        }
        }
        ```
        ```json Failure Response

        If txnID is not found, the response is similar to the following
        {
            "status":0,
            "msg":"0 out of 1 Transactions Fetched Successfully",
              "transaction_details":
              {	
        						"IhfgcZnXR4o4nB":
                {
        								"mihpayid":"Not Found",
                    "status":"Not Found"
                  }
        						}
        }
        ```
      </Accordion>

      <Accordion title="Response parameters" icon="fa-list">
        <Table align={["left","left","left"]}>
          <thead>
            <tr>
              <th style={{ textAlign: "left" }}>
                **Parameter**
              </th>

              <th style={{ textAlign: "left" }}>
                **Description**
              </th>

              <th style={{ textAlign: "left" }}>
                **Example**
              </th>
            </tr>
          </thead>

          <tbody>
            <tr>
              <td style={{ textAlign: "left" }}>
                status
              </td>

              <td style={{ textAlign: "left" }}>
                This parameter returns the status of web service call. The status can be any of the following:

                * 0 - If web service call failed.
                * 1 - If web service call succeeded
              </td>

              <td style={{ textAlign: "left" }}>
                0
              </td>
            </tr>

            <tr>
              <td style={{ textAlign: "left" }}>
                msg
              </td>

              <td style={{ textAlign: "left" }}>
                This parameter returns the reason string.
              </td>

              <td style={{ textAlign: "left" }}>
                For example, any of the following messages are displayed:

                * Parameter missing
                * Token is empty
                * Amount is empty
                * Transaction not exists
              </td>
            </tr>

            <tr>
              <td style={{ textAlign: "left" }}>
                transaction\_details
              </td>

              <td style={{ textAlign: "left" }}>
                This parameter contains the response in a JSON format. For more information refer to [JSON fields description for transaction\_details parameter ](#json-field-description-for-transaction_details-parameter).
              </td>

              <td style={{ textAlign: "left" }} />
            </tr>

            <tr>
              <td style={{ textAlign: "left" }}>
                request\_id
              </td>

              <td style={{ textAlign: "left" }}>
                PayU Request ID for a request in a Transaction. For example, a transaction can have a refund request.
              </td>

              <td style={{ textAlign: "left" }}>
                7800456
              </td>
            </tr>

            <tr>
              <td style={{ textAlign: "left" }}>
                bank\_ref\_num
              </td>

              <td style={{ textAlign: "left" }}>
                This parameter returns the bank reference number. If the bank provides after a successful action.
              </td>

              <td style={{ textAlign: "left" }}>
                204519474956
              </td>
            </tr>
          </tbody>
        </Table>

        To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).
      </Accordion>
    </Tab>
  </Tabs>
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

  * Use test merchant credentials
  * Point to `https://test.payu.in/_payment`
  * Implement proper logging for debugging
</Accordion>

<Accordion title="Step 2.2: Pre-Payment Validation" icon="fa-check-circle">
  Before initiating a transaction, ensure your server-side implementation is correct.

  1. **Verify API Credentials:** Double-check that you are using the correct key and salt for the test environment.
  2. **Validate Hash Calculation:** The most common point of failure is an incorrect hash.
     1. Temporarily print the string that you are passing into the hash function on your server.
     2. Ensure the order of the parameters (key|txnid|amount|productinfo|firstname|email...|salt) exactly matches the format specified in the documentation.
     3. Verify that there are no empty or null values for mandatory parameters in the hash string.
     4. If you encounter a "Checksum failed" error upon redirection, this is the first thing to debug.
</Accordion>

<Accordion title="Step 2.3: Simulate a Successful Transaction (The Happy Path)" icon="fa-thumbs-up">
  This test ensures that a successful payment is correctly processed and recorded.

  1. **Initiate Payment:** On your website or app, add items to the cart and proceed to payment. This should trigger your code to send the transaction details to PayU and redirect the user to the PayU payment page.
  2. **Error Check:** If you are not redirected and see an error message on your own site, check your server-side logs. If you are redirected to a PayU error page, refer to the Error Handling section to diagnose the issue.
  3. **Verify Payment Page:** Once on the PayU page, confirm the following:
     1. The transaction amount and product details are displayed correctly.
     2. All the payment methods (Credit/Debit Card, UPI, Net Banking, etc.) that should be active on your account are visible. If a payment method is missing, please contact your Key Account Manager (KAM) or PayU Support.
  4. **Test a Card Transaction**:
     1. Select Credit Card as the payment method.
     2. Use the following test card details:
        1. Card Number: 5123456789012346
        2. Expiry Date: Any valid future date (e.g., 12/2030)
        3. CVV: 123
        4. Name on Card: Test Name
     3. Click Pay Now. You will be redirected to a dummy bank page to simulate 3D Secure authentication.
     4. Enter the test OTP 123456 and click Submit.
  5. **Test a UPI Transaction:**
     1. Select UPI as the payment method.
     2. Enter a test UPI ID: testsuccess\@gpay
     3. Click Verify and then Pay Now. This will simulate a successful UPI transaction.

  For more test credentials, refer to the [Test Cards, UPI ID and Wallets guide](https://docs.payu.in/docs/test-cards-upi-id-and-wallets).
</Accordion>

<Accordion title="Step 2.4: Simulate a Failed Transaction" icon="fa-times-circle">
  It's equally important to test how your system handles failed payments.

  1. Initiate a New Payment as you did in Step 2.
  2. Test a Failing Card Transaction:
     1. Select Credit Card as the payment method.
     2. Use a test card designed to fail, for example:
        1. Card Number: 5123456789012340 (Payment failed by user)
     3. Complete the payment flow. The transaction should fail.
</Accordion>

<Accordion title="Step 2.5: Post-Transaction Verification" icon="fa-magnifying-glass">
  After both the successful and failed transactions, you must verify the final status at multiple points.

  1. **Check the Return URL (surl / furl):**
     1. After a successful payment, PayU will redirect the user to the Success URL (surl) you provided. Verify that your application handles this redirect correctly and displays an appropriate success message to the user.
     2. After a failed payment, PayU will redirect the user to the Failure URL (furl). Verify that your application displays a clear failure message and provides the user with options to retry.
  2. **Verify the Server-to-Server (S2S) Webhook:**
     1. This is the most reliable way to confirm transaction status.
     2. Check your server logs to ensure that you have received the S2S POST request from PayU for the transaction.
     3. Validate the hash in the webhook response to ensure the data is authentic.
     4. Update the transaction status in your database based on the status received in the S2S webhook, not based on the browser redirect (surl/furl).
  3. **Cross-Verify in the PayU Dashboard:**
     1. Log in to your PayU test dashboard.
     2. Navigate to the "Transactions" section.
     3. Verify that both the successful and failed transactions are logged correctly with the corresponding status (success, failure). Check that details like txnid and amount match your records.
</Accordion>

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

  * Valid SSL certificate from trusted CA
  * TLS 1.2 or higher
  * Strong cipher suites
  * Proper certificate chain

  **Code Security Requirements**

  * Input validation on all payment fields
  * SQL injection prevention
  * XSS protection
  * CSRF protection
  * Secure session management

  <Callout icon="⚠️" theme="warning">
    **Important**: Failure to comply with PCI DSS requirements may result in account suspension and liability for fraud.
  </Callout>
</Accordion>

<Accordion title="Step 3.2: Update to Production Credentials" icon="fa-key">
  **Switch to Live Environment**

  1. **Update API Credentials**
     * Replace test merchant key with live key
     * Replace test salt with live salt
     * Update endpoint URL to `https://secure.payu.in/_payment`

  2. **Update Verification API URL**
     * Change from test to production verification endpoint
     * Update URL to `https://info.payu.in/merchant/postservice.php?form=2`

  3. **Update Webhook URLs**
     * Configure production webhook endpoints
     * Ensure HTTPS URLs are accessible from internet
     * Test webhook reception

  **Production Configuration Sample**

  ```php
  // Production configuration
  define('PAYU_BASE_URL', 'https://secure.payu.in');
  define('PAYU_PAYMENT_URL', PAYU_BASE_URL . '/_payment');
  define('PAYU_VERIFY_URL', 'https://info.payu.in/merchant/postservice.php?form=2');
  define('MERCHANT_KEY', 'your_live_merchant_key');
  define('MERCHANT_SALT', 'your_live_salt');
  ```
</Accordion>

<Accordion title="Step 3.3: Final Integration Verification" icon="fa-clipboard-check">
  **Pre-Launch Checklist**

  **✅ Security Verification**

  * [ ] PCI DSS compliance completed (if applicable)
  * [ ] SSL certificate installed and verified
  * [ ] All payment forms use HTTPS
  * [ ] Hash validation implemented for requests and responses
  * [ ] Input validation on all fields
  * [ ] No sensitive data logged or stored
  * [ ] Error handling implemented
  * [ ] Security headers configured

  **✅ Technical Integration**

  * [ ] Production credentials configured
  * [ ] Payment endpoints updated to production URLs
  * [ ] All payment modes tested in production
  * [ ] Webhook endpoints configured and tested
  * [ ] Response handling and hash verification working
  * [ ] Transaction verification API integration tested
  * [ ] Database integration for transaction storage
  * [ ] Email/SMS notifications configured

  **✅ Live Transaction Testing**

  * [ ] Conduct small live transactions for each payment mode
  * [ ] Verify successful transactions in PayU dashboard
  * [ ] Test failed transaction handling
  * [ ] Verify webhook reception for live transactions
  * [ ] Test refund process (if applicable)
  * [ ] Verify settlement process

  <Callout icon="🚀" theme="success">
    **Go Live!** Once all checklist items are completed and verified, your Merchant Hosted PayU integration is ready for production use.
  </Callout>
</Accordion>

<br />

## Additional Resources

* [Merchant Hosted Checkout Integration Introduction](https://docs.payu.in/docs/custom-checkout-merchant-hosted)
* [Hash Generation](https://docs.payu.in/docs/generate-hash-payu-hosted)
* [Webhooks](https://docs.payu.in/docs/webhooks-for-payments)
* [Error Codes Reference](https://docs.payu.in/reference/error-codes)
* [Test Credentials](https://docs.payu.in/docs/test-cards-upi-id-and-wallets)

<br />
