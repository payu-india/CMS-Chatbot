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

> 📘 Note:
> 
> The character “X” in the card numbers are placeholders that can be substituted with any number (1-9).

## Web Checkout

> 📘 Note:
> 
> Any value can be used for the **name** parameter in Test environment.

### Credit Card

| **Payment Flow**              | **Card Number**  | **Network** | **Expiry** | **CVV** | **OTP** |
| ----------------------------- | ---------------- | ----------- | ---------- | ------- | ------- |
| PayU/Merchant Hosted Checkout | 5123456789012346 | Mastercard  | 05/25      | 123     | 123456  |
| PayU/Merchant Hosted Checkout | 4012001037141112 | VISA        | 05/25      | 123     | 123456  |
| Server-to-Server              | 5497774415170603 | Mastercard  | 05/25      | 412     | 123456  |
| PayU/Merchant Hosted Checkout | 6082015309577308 | RUPAY       | 05/25      | 123     | 123456  |

### Debit Card

| Card Number         | Network    | Expiry | CVV | OTP    |
| :------------------ | :--------- | :----- | :-- | :----- |
| 5118-7000-0000-0003 | Mastercard | 05/25  | 123 | 123456 |
| 4594-5380-5063-9999 | VISA       | 05/25  | 123 | 123456 |

## EMI test cards

> 📘 Note:
> 
> Any value can be used for the **name** parameter in Test environment.

[block:parameters]
{
  "data": {
    "h-0": "**Payment Flow**",
    "h-1": "**Card Number**",
    "h-2": "**Expiry**",
    "h-3": "**CVV**",
    "h-4": "**OTP**",
    "h-5": "**Mobile (mandatory for EMIs)**",
    "0-0": "Kotak Bank DC EMI",
    "0-1": "4706137805099594  \n**Note**: Amount range is : 5000.00 to 10000.00",
    "0-2": "05/25",
    "0-3": "any random three-digit number",
    "0-4": "111111",
    "0-5": "9123412345",
    "1-0": "AXIS Bank DC EMI",
    "1-1": "4011510000000007",
    "1-2": "05/25",
    "1-3": "any random three-digit number",
    "1-4": "123456",
    "1-5": "8884758579",
    "2-0": "HDFC Bank CC EMI",
    "2-1": "4453341065876437",
    "2-2": "05/25",
    "2-3": "any random three-digit number",
    "2-4": "123456",
    "2-5": "9123412345",
    "3-0": "ICICI Bank CC EMI",
    "3-1": "4808557848741463",
    "3-2": "05/25",
    "3-3": "any random three-digit number",
    "3-4": "123456",
    "3-5": "9123412345",
    "4-0": "Onecard CC EMI",
    "4-1": "4010636236612108",
    "4-2": "05/25",
    "4-3": "any random three-digit number",
    "4-4": "123456",
    "4-5": "9123412345",
    "5-0": "Axis Bank CC EMI",
    "5-1": "5241784703665106",
    "5-2": "05/25",
    "5-3": "123",
    "5-4": "123456",
    "5-5": "9123412345",
    "6-0": "Standard Chartered CC EMI",
    "6-1": "5404608014083225",
    "6-2": "05/25",
    "6-3": "any random three-digit number",
    "6-4": "123456",
    "6-5": "9123412345",
    "7-0": "HSBC Bank CC EMI",
    "7-1": "4862696278807023",
    "7-2": "05/25",
    "7-3": "any random three-digit number",
    "7-4": "123456",
    "7-5": "9123412345",
    "8-0": "Kotak Bank CC EMI",
    "8-1": "4363888155006621",
    "8-2": "05/25",
    "8-3": "any random three-digit number",
    "8-4": "123456",
    "8-5": "9123412345",
    "9-0": "IndusInd Bank CC EMI",
    "9-1": "4029706572777150",
    "9-2": "05/25",
    "9-3": "any random three-digit number",
    "9-4": "123456",
    "9-5": "9123412345",
    "10-0": "Citibank CC EMI",
    "10-1": "4550387246273400",
    "10-2": "05/25",
    "10-3": "any random three-digit number",
    "10-4": "123456",
    "10-5": "9123412345",
    "11-0": "SBI CC EMI",
    "11-1": "5264686823451576",
    "11-2": "05/25",
    "11-3": "any random three-digit number",
    "11-4": "123456",
    "11-5": "9123412345",
    "12-0": "HSBC Bank CC EMI",
    "12-1": "4862696278807023",
    "12-2": "05/25",
    "12-3": "any random three-digit number",
    "12-4": "123456",
    "12-5": "9123412345"
  },
  "cols": 6,
  "rows": 13,
  "align": [
    null,
    null,
    null,
    null,
    null,
    null
  ]
}
[/block]


### Other EMIs

#### Axio

- Mob:   9999999999
- OTP =   123456
- PAN = XYZPA1234A (for eKYC)
- DOB = 21-07-1980
- Aadhaar = 9999 9999 1234
- Aadhaar OTP = 123456
- UPI ID - test@upi

## International Payments or DCC

> 📘 Note:
> 
> Any name can be used for the **name** parameter in Test environment.

| Currency | **Card Number**  | **Expiry** | **CVV** | **OTP** |
| -------- | ---------------- | ---------- | ------- | ------- |
| USD $    | 4755964453587236 | 12/2024    | 596     | 111111  |
| Euro €   | 4020419926566936 | 12/2024    | 041     | 111111  |

## Save cards

> 📘 Note:
> 
> Any value can be used for the **name** parameter in Test environment.

| **Card Number**  | Network     | **Expiry** | **CVV** |
| ---------------- | :---------- | ---------- | ------- |
| 5506900480000008 | Master Card | 05/2025    | 123     |
| 4895370077346937 | VISA        | 05/2025    | 123     |

## Test UPI ID

You can use **anything@payu** or **[9999999999@payu](mailto:9999999999@payu)** as VPA to test your UPI-related integration in the [sandbox](https://en.wikipedia.org/wiki/Sandbox_(software_development)#:) (Test environment) only for the payment flows involving ** \_payment** AP.

> 📘 Notes:
> 
> - The **anything@payu** VPA can be used in the sandbox or [API Playground](https://api-playground.payu.in/) and any other VPA will not work for the** \_payment** only.
> - For the [Validate VPA Handle API](ref:validate_vpa_api), you can use any valid VPA.

## Test Net Banking credentials

Use the following credentials for Net Banking in the sandbox:

- **user name**: payu
- **password**: payu
- **OTP**: 123456

The above Net Banking credentials must be used in [API Playground](https://api-playground.payu.in/).

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