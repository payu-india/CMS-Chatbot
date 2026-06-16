---
title: Test Cards, UPI ID and Wallets
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Test Cards, UPI ID and Wallets
  description: >-
    The page provides a table with details of some of the test cards that can be
    used to test your integration in the sandbox (Test environment). The table
    includes details such as card number, brand, expiry date, CVV, OTP, and
    name. The page also provides details of some of the test UPI IDs that can be
    used to test your UPI-related integration in the sandbox (Test environment).
  keywords:
    - PayU India sandbox
    - PayU India Test Credentials
    - PayU India Test Cards
    - Test cards for PayU integration
    - Test wallets for PayU
    - Test UPI ID for PayU
    - Test credit card for PayU
    - Test NetBanking for PayU
  robots: index
next:
  description: ''
---
<TestCardsCallout />

## Test Cards

The following table provides details of some of the test cards that you can use to test your integration in the sandbox (Test environment). As Sandbox is a replica of the production environment, you can push the code in production by just replacing account credentials and URLs.

> 📘
>
> **Note**: The character “X” in the card numbers are placeholders that can be substituted with any number (1-9).

## Web Checkout

> 📘
>
> **Note**: Any value can be used for the **name** parameter in Test environment.

### Credit Card

| **Payment Flow**              | **Card Number**  | **Network** | **Expiry** | **CVV** | **OTP** |
| ----------------------------- | ---------------- | ----------- | ---------- | ------- | ------- |
| PayU/Merchant Hosted Checkout | 5123456789012346 | Mastercard  | 05/30      | 123     | 123456  |
| PayU/Merchant Hosted Checkout | 4012001037141112 | VISA        | 05/30      | 123     | 123456  |
| Server-to-Server              | 5497774415170603 | Mastercard  | 05/30      | 412     | 123456  |
| PayU/Merchant Hosted Checkout | 6082015309577308 | RUPAY       | 05/30      | 123     | 123456  |
| PayU/Merchant Hosted Checkout | 370295061673669  | AMEX        | 03/30      | 1234    | 725356  |

### Debit Card

| Card Number         | Network    | Expiry | CVV | OTP    |
| :------------------ | :--------- | :----- | :-- | :----- |
| 5118-7000-0000-0003 | Mastercard | 05/30  | 123 | 123456 |
| 4594-5380-5063-9999 | VISA       | 05/30  | 123 | 123456 |

## Rupay Card

| **Card Number**     | **Network** | **Expiry** | **CVV** | **OTP** |
| ------------------- | ----------- | ---------- | ------- | ------- |
| 6071-4898-7654-3212 | RUPAY       | 12/27      | 123     | 123456  |
| 6074-8299-0000-4938 | RUPAY       | 12/27      | 123     | 123456  |

## EMI test cards

> 📘 **Note**:&#x20;
>
> Any value can be used for the **name** parameter in Test environment.

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Payment Flow</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Card Number</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Expiry</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>CVV</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>OTP</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Mobile (mandatory for EMIs)</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Kotak Bank DC EMI</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>4706137805099594<br><strong>Note</strong>: Amount range is : 5000.00 to 10000.00</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>05/30</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>any random three-digit number</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>111111</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>9123412345</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>AXIS Bank DC EMI</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>4011510000000007</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>05/30</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>any random three-digit number</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>123456</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>8884758579</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>HDFC Bank CC EMI</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>4453341065876437</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>05/30</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>any random three-digit number</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>123456</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>9123412345</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>ICICI Bank CC EMI</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>4808557848741463</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>05/30</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>any random three-digit number</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>123456</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>9123412345</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Onecard CC EMI</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>4010636236612108</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>05/30</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>any random three-digit number</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>123456</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>9123412345</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Axis Bank CC EMI</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>5241784703665106</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>05/30</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>123</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>123456</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>9123412345</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Standard Chartered CC EMI</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>5404608014083225</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>05/30</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>any random three-digit number</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>123456</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>9123412345</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>HSBC Bank CC EMI</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>4862696278807023</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>05/30</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>any random three-digit number</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>123456</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>9123412345</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Kotak Bank CC EMI</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>4363888155006621</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>05/30</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>any random three-digit number</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>123456</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>9123412345</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>IndusInd Bank CC EMI</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>4029706572777150</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>05/30</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>any random three-digit number</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>123456</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>9123412345</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Citibank CC EMI</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>4550387246273400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>05/30</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>any random three-digit number</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>123456</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>9123412345</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>SBI CC EMI</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>5264686823451576</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>05/30</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>any random three-digit number</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>123456</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>9123412345</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>HSBC Bank CC EMI</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>4862696278807023</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>05/30</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>any random three-digit number</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>123456</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>9123412345</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### Other EMIs

#### Axio

- Mob:   9999999999
- OTP =   123456
- PAN = XYZPA1234A (for eKYC)
- DOB = 21-07-1980
- Aadhaar = 9999 9999 1234
- Aadhaar OTP = 123456
- UPI ID - test\@upi

## International Payments or DCC

> 📘
>
> **Note**: Any name can be used for the **name** parameter in Test environment.

| Currency | **Card Number**  | **Expiry** | **CVV** | **OTP** |
| -------- | ---------------- | ---------- | ------- | ------- |
| USD $    | 4755964453587236 | 12/2030    | 596     | 725356  |
| Euro €   | 4020419926566936 | 12/2030    | 041     | 725356  |

## Save cards

> 📘
>
> **Note**: Any value can be used for the **name** parameter in Test environment.

| **Card Number**  | Network     | **Expiry** | **CVV** |
| ---------------- | :---------- | ---------- | ------- |
| 5506900480000008 | Master Card | 05/2030    | 123     |
| 4895370077346937 | VISA        | 05/2030    | 123     |

## Test UPI ID

You can use **anything\@payu** or **999999999\@payu** as VPA to test your UPI-related integration in the [sandbox](https://en.wikipedia.org/wiki/Sandbox_\(software_development\)#:) (Test environment) only for the payment flows involving **\_payment** API.

> 📘 Notes:
>
> - The **anything\@payu** VPA can be used in the sandbox or [Merchant Hosted > Collect Payment - UPI](ref:_payment_merchant_hosted_upi) API reference page and any other VPA will not work for th&#x65;**\_payment** only.
> - For the [Validate VPA Handle API](ref:validate_vpa_api), you can use any valid VPA.

## Test UPI Intent Flow

To test the UPI intent flow on UAT, please follow the steps below:

1. **Download the UPI Intent Simulator APK**

- Access the UPI Intent Simulator repository:
  [https://github.com/payu-india/PayU-UPI-Intent-Simulator-App](https://github.com/payu-india/PayU-UPI-Intent-Simulator-App)
- Download the latest UAT APK from the Releases section or the appropriate branch tagged for UAT.

2. **Install the APK on Your Mobile Device**

- Transfer the APK to your device or download it directly on your phone.
- Enable installation from unknown sources if prompted.
- Install the APK.

**For More Details**

Please refer to the official GitHub README and follow the detailed steps here:
[https://github.com/payu-india/PayU-UPI-Intent-Simulator-App](https://github.com/payu-india/PayU-UPI-Intent-Simulator-App)

## Test Net Banking credentials

Use the following credentials for Net Banking in the sandbox:

- **user name**: payu
- **password**: payu
- **OTP**: 123456

The above Net Banking credentials must be used in[ Collect Payment > Net Banking ](ref:_payment_merchant_hosted_netbanking)API Reference.

## Test Wallets

| Vendor | Mobile Number                                                     | OTP    |
| ------ | ----------------------------------------------------------------- | ------ |
| PayTM  | 7777777777 or use card mentioned under [Test Cards](#test-cards). | 888888 |
| Amazon | You can test using your original Amazon account details.          |        |
| Airtel | You can use your mobile number.                                   |        |

## Test BNPL credentials

| BNPL Provider | bankcode | Tenure  | Mobile Number | Credit Card No.  |
| ------------- | -------- | ------- | :------------ | :--------------- |
| Lazypay       | LAZYPAY  | NA      | 9123412345    | NA               |
| HDFC Bank     | HDFCF15  | 15 days | 9123412345    | 4234567890056334 |
| HDFC Bank     | HDFCF30  | 30 days | 9123412345    | 4234567890056334 |
| HDFC Bank     | HDFCF60  | 60 days | 9123412345    | 4234567890056334 |
| HDFC Bank     | HDFCF90  | 90 days | 9123412345    | 4234567890056334 |

<br />
