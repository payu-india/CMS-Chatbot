---
title: Integrate Merchant Hosted Checkout
deprecated: false
hidden: false
metadata:
  title: Integrate Merchant Hosted Checkout - Cross Border Transaction under LRS
  keywords:
    - Integrate Merchant Hosted Checkout for Cross Border Transaction under LRS
    - Integrate Merchant Hosted Checkout for CB LRS
  robots: index
---
PayU’s **_payment** API supports LRS implementation using the following parameters mandatorily in an S2S transaction:

* lrs_service_type
* lrs_mandatory_limit_declaration
* lrs_tnc
* tcs_amount
* lrs_tcs_declaration_under_limit
* buyer_type_business (optional)

<br />

The steps to integrate involves:

1. [Validate the PAN card](#step-1-validate-the-pan-card)
2. [Request Payment with PayU](#step-2-request-payment-with-payu)
3. [Check response from PayU](#step-3-check-response-from-payu)
4. [Verify the Payment](#step-4-verify-the-payment)

## Step 1: Validate the PAN card

The PAN Card Status Check API allows merchants to verify PAN (Permanent Account Number) card details. It validates whether a given PAN number is active, confirms if the provided name and date of birth match the official PAN records, and checks the seeding status of the PAN. This API is essential for KYC (Know Your Customer) processes, identity verification, and regulatory compliance.

**Endpoint**

```
https://test10-onboarding.payu.in/dvs/kyc/check_pan_card_status
```
<Accordion title="Request parameters" icon="fa-table">

| Parameter                     | Description                                                   | Example      |
| ----------------------------- | ------------------------------------------------------------- | ------------ |
| `pan_number`<br />`mandatory` | The PAN (Permanent Account Number) to be verified             | "CYCPD2784G" |
| `name`<br />`mandatory`       | The name of the PAN card holder as it appears on the PAN card | "AKASH DEEP" |
| `dob`<br />`mandatory`        | Date of Birth of the PAN holder in DD/MM/YYYY format          | "15/09/1993" |
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
```bash
curl --location 'https://test10-onboarding.payu.in/dvs/kyc/check_pan_card_status' \
--header 'Content-Type: application/json' \
--header 'Date: Thu, 17 Jun 2025 08:17:59 GMT' \
--header 'Digest: DFXmqI0rFnXlmHLlsRwdDMw9vUSVzyYQzGP+MKLo8f8=' \
--header 'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="7qjgpH9B4QALxDR0nVlHdEKEYMZ0XeJ0QpnvveSyqMo="' \
--header 'platformId: 1' \
--data '{
    "pan_number": "CYCPD2784G",
    "name": "AKASH DEEP",
    "dob": "15/09/1993"
}'
```
</Accordion>
<Accordion title="Sample Response" icon="fa-reply">
```json
{
    "id": 86235,
    "api_name": "pan_status_check",
    "identifier": "79c0d918a4f4661cb9cb17d96d24ac1cf04b6013d504cc766ac5235380bfc0d5",
    "response": {
        "result": {
            "status": "Active",
            "nameMatch": "Y",
            "dobMatch": "Y",
            "seedingStatus": "Y"
        }
    },
    "status": "success",
    "http_status": 200,
    "client_id": "195ab95fa4700eeaaf38b7f5b538d2979f0f281e0a4eaedca1aa675b79b331a2",
    "created_at": "2025-04-30T05:51:40.000Z",
    "updated_at": "2025-04-30T05:51:40.000Z",
    "client_name": "SignzyClient"
}
```
</Accordion>
<Accordion title="Response Parameters" icon="fa-table">

| Parameter   | Description                                             | Example                                                              |
| ----------- | ------------------------------------------------------- | -------------------------------------------------------------------- |
| id          | Unique identifier for the verification request          | `86235`                                                              |
| api_name    | Identifier of the API that was called                   | `"pan_status_check"`                                                 |
| identifier  | A unique hash identifier for the verification request   | `"79c0d918a4f4661cb9cb17d96d24ac1cf04b6013d504cc766ac5235380bfc0d5"` |
| response    | Contains the verification results                       | See result table below                                               |
| status      | Overall status of the API call                          | `"success"`                                                          |
| http_status | HTTP status code of the response                        | `200`                                                                |
| client_id   | Unique identifier of the client making the request      | `"195ab95fa4700eeaaf38b7f5b538d2979f0f281e0a4eaedca1aa675b79b331a2"` |
| created_at  | Timestamp when the verification record was created      | `"2025-04-30T05:51:40.000Z"`                                         |
| updated_at  | Timestamp when the verification record was last updated | `"2025-04-30T05:51:40.000Z"`                                         |
| client_name | Name of the client account                              | `"SignzyClient"`                                                     |

#### Response Result Object

| Parameter     | Description                                                        | Example    |
| ------------- | ------------------------------------------------------------------ | ---------- |
| status        | Status of the PAN card                                             | `"Active"` |
| nameMatch     | Indicates if the provided name matches with PAN records (Y/N)      | `"Y"`      |
| dobMatch      | Indicates if the provided DOB matches with PAN records (Y/N)       | `"Y"`      |
| seedingStatus | Indicates if the PAN is seeded with additional verifications (Y/N) | `"Y"`      |
</Accordion>
## Step 2: Request Payment with PayU

The following parameters (mandatory) must be posted using any of the following seamless integration and refer to the corresponding section of [Web Checkout Integration](doc:introduction-web) documentation for the complete list of parameters to be posted:

* [Merchant Hosted Checkout > Cards](doc:collect-payments-with-cards-seamless)
* [Server-to-Server > General Integration](doc:integration-with-s2s)


**Environment**

|                            |                                                                        |
| :------------------------- | :--------------------------------------------------------------------- |
| **Test Environment**       | \<[https://test.payu.in/_payment>](https://test.payu.in/_payment>)     |
| **Production Environment** | \<[https://secure.payu.in/_payment>](https://secure.payu.in/_payment>) |
<Accordion title="Request Parameters" icon="fa-table">
| Parameter                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Example                           |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| `key`<br />`mandatory`                                                      | `String` Merchant key provided by PayU during onboarding.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | JPg****f                          |
| `txnid`<br />`mandatory`                                                    | `String` The transaction ID is a reference number for a specific order that is generated by the merchant.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | ypl938459435                      |
| `amount`<br />`optional`                                                    | `String` The transaction amount.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 100.00                            |
| `productinfo`<br />`mandatory`                                              | `String` A brief description of the product.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | iPhone                            |
| `firstname`<br />`mandatory`                                                | `String` The first name of the customer as on their Permanent Account Number (PAN)<br /><br />_Note: This should be validated by PAN Status Check API_                                                                                                                                                                                                                                                                                                                                                                                                                              | Ashish                            |
| `lastname`<br />`mandatory`                                                 | `String` The last name of the customer as on their Permanent Account Number (PAN)<br /><br />_Note: This should be validated by PAN Status Check API_                                                                                                                                                                                                                                                                                                                                                                                                                               | Kumar                             |
| `email`<br />`mandatory`                                                    | `String` The email address of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [abc@payu.in](mailto:abc@payu.in) |
| `phone`<br />`mandatory`                                                    | `String` The phone number of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                   |
| `address1`<br />`mandatory`                                                 | `String` The first line of the billing address.<br />H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai<br /><br />_Note_: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.                                                                                                                                                                                                                                                                                               | 34 Saikripa-Estate, Tilak Nagar   |
| `address2`<br />`optional`                                                  | `String` The second line of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                   |
| `city`<br />`mandatory`                                                     | `String` The city where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Mumbai                            |
| `state`<br />`mandatory`                                                    | `String` The state where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Maharashtra                       |
| `country`<br />`mandatory`                                                  | `String` The country where your customer resides.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | India                             |
| `zipcode`<br />`mandatory`                                                  | `String` Billing address zip code is mandatory for the cardless EMI option.<br />`Character Limit-20`                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 400004                            |
| `pg`<br />`mandatory for seamless/s2s flow`                                 | `String` It defines the payment category that the merchant wants the customer to see by default on the PayU's payment page. If this field is empty, the system assumes the credit card payment option by default.                                                                                                                                                                                                                                                                                                                                                                   | CC, NB or UPI                     |
| `bankcode`<br />`mandatory for seamless/s2s flow`                           | `String` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it.                                                                                                                                                                                                                                                                                                                                                                                                    | AMEX                              |
| `ccnum`<br />`mandatory for cards`                                          | `String` Use 13-19 digit card number for credit/debit cards (15 digits for AMEX, 13-19 for Maestro) and validate with LUHN algorithm. Refer to Card Number Formats and display error message on invalid input.                                                                                                                                                                                                                                                                                                                                                                      |                                   |
| `ccname`<br />`mandatory for cards`                                         | `String` This parameter must contain the name on card – as entered by the customer for the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                   |
| `ccvv`<br />`mandatory for cards`                                           | `String` Use 3-digit CVV number for credit/debit cards and 4-digit security code (4DBC/CID) for AMEX cards.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                   |
| `ccexpmon`<br />`mandatory for cards`                                       | `String` This parameter must contain the card's expiry month – as entered by the user for the transaction. It must always be in 2 digits or in MM format. For months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – It should be 10,11 and 12 respectively.                                                                                                                                                                                                                                                  |                                   |
| `ccexpyr`<br />`mandatory for cards`                                        | `String` This parameter must contain the card's expiry year – as entered by the customer for the transaction. It must be of four digits.                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                   |
| `surl`<br />`mandatory`                                                     | `String` The success URL, which is the page PayU will redirect to if the transaction is successful.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                   |
| `furl`<br />`mandatory`                                                     | `String` The Failure URL, which is the page PayU will redirect to if the transaction is failed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                   |
| `udf1`<br />`mandatory for LRS S2S transaction`                             | `String` The Permanent Account Number (PAN) of the buyer must be collected in this field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | AELPR****E                        |
| `udf3`<br />`mandatory for LRS S2S transaction`                             | `String` The date of birth of the buyer must be collected using this field in the DD-MM-YYYY format as on their Permanent Account Number (PAN).<br /><br />_Note: This should be validated by PAN Status Check API_                                                                                                                                                                                                                                                                                                                                                                 | 02-02-1980                        |
| `udf4`<br />`mandatory for payment aggregators`                             | `String` This parameter must include end merchant legal entity name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | XYZ Pvt. Ltd.                     |
| `udf5`<br />`mandatory`                                                     | `String` The invoice ID or invoice number must be collected using this field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | INV123456                         |
| `buyer_type_business`<br />`conditional for cross-border transactions`      | This parameter is used to identify whether it is a business-to-business transaction. If 1 is posted, it is a B2B transaction.<br /><br />In case of B2B, no other LRS specific parameters (listed below) need to be sent, as B2B transactions are outside the scope of the regulation.                                                                                                                                                                                                                                                                                              | 0                                 |
| `lrs_mandatory_limit_declaration`<br />`mandatory for LRS S2S transactions` | `String` Mandatory declaration from buyer that they have remitted less than $250,000 USD under Liberalised Remittance Scheme.<br /><br />**Note**: The limit is as per RBI regulation and needs to be mandatorily collected on the checkout page.                                                                                                                                                                                                                                                                                                                                   | 1                                 |
| `lrs_tnc`<br />`mandatory for LRS S2S transactions`                         | `String` Mandatory declaration from buyer that they agree to PayU's terms & conditions.<br /><br />**Note**: The declaration needs to be taken mandatorily from the buyer on the checkout page.                                                                                                                                                                                                                                                                                                                                                                                     | 1                                 |
| `lrs_service_type`<br />`mandatory for LRS S2S transactions`                | `String` The LRS service type describes the nature of service & decides the tax amount based on it. For more information, refer to the [lrs_service_type parameter values](#lrs_service_type-parameter-values) table.                                                                                                                                                                                                                                                                                                                                                               | travel                            |
| `tcs_amount`<br />`mandatory for LRS S2S transactions`                      | `String` Amount of TCS (Tax Collected at Source) to be charged.<br /><br />**Note**: The amount needs to be captured as per guidance in the [lrs_service_type parameter values](#lrs_service_type-parameter-values) table.                                                                                                                                                                                                                                                                                                                                                          | 2.00                              |
| `lrs_tcs_declaration_under_limit`<br />`mandatory for LRS S2S transactions` | `String` Declaration from buyer that they are either under or over INR 1,00,000 based on which TCS will be collected.<br /><br />Values expected:<br /><br />**0** (in case of under the limit)<br />**1** (in case of over the limit)<br /><br />**Note**: The declaration needs to be taken mandatorily from the buyer on the checkout page. Also, when user declares they are over the limit (i.e. when this param is sent as "1", the "tcs_amount" field to contain amount calculated as per the [lrs_service_type parameter values](#lrs_service_type-parameter-values) table. | 0 / 1                             |

#### lrs_service_type parameter values

| **lrs_service_type** | **Txn Amount \<= INR 10 lacs** | **Txn Amount > INR 10 lacs** |
| -------------------- | ------------------------------ | ---------------------------- |
| education_loan       | 0                              | 0                            |
| education_non_loan   | 0                              | 5%                           |
| medical              | 0                              | 5%                           |
| travel               | 0                              | 20%                          |
| others               | 0                              | 20%                          |

````
</Accordion>

<Accordion title="Sample Request" icon="fa-code">

```curl
curl --location 'https://test.payu.in/_payment' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=PRiQvJ' \
--data-urlencode 'txnid=my_order_64240' \
--data-urlencode 'amount=5' \
--data-urlencode 'productinfo=asfas' \
--data-urlencode 'email=test@test.com' \
--data-urlencode 'phone=8688359250' \
--data-urlencode 'txn_s2s_flow=4' \
--data-urlencode 'hash={{hash}}' \
--data-urlencode 'pg=CC' \
--data-urlencode 'bankcode=CC' \
--data-urlencode 'surl=https://test.payu.in/admin/test_response' \
--data-urlencode 'furl=https://test.payu.in/admin/test_response' \
--data-urlencode 'udf1=CYCPD2784G' \
--data-urlencode 'udf2=' \
--data-urlencode 'udf3=02-02-1980' \
--data-urlencode 'udf4=XYZ Pvt. Ltd' \
--data-urlencode 'udf5=INV123456' \
--data-urlencode 'ccnum=5506900480000008' \
--data-urlencode 'ccexpyr=2025' \
--data-urlencode 'ccexpmon=09' \
--data-urlencode 'ccvv=123' \
--data-urlencode 'ccname=test' \
--data-urlencode 'si_details={"billingAmount":"10.00","billingCurrency":"INR","billingCycle":"ADHOC","billingInterval": 1,"paymentStartDate":"2024-11-19","paymentEndDate":"2025-12-01"}' \
--data-urlencode 'api_version=7' \
--data-urlencode 'si=1' \
--data-urlencode 'firstname=sudhanshu' \
--data-urlencode 'user_credentials=T58CQx:sudhanshu' \
--data-urlencode 'address1=308,third floor' \
--data-urlencode 'address2=testing' \
--data-urlencode 'city=ggn' \
--data-urlencode 'state=UP' \
--data-urlencode 'country=IND' \
--data-urlencode 'zipcode=122018' \
--data-urlencode 'buyer_type_business=0' \
--data-urlencode 'lrs_mandatory_limit_declaration=1' \
--data-urlencode 'lrs_tnc=1' \
--data-urlencode 'lrs_service_type=travel' \
--data-urlencode 'lrs_tcs_declaration_under_limit=0'  

````
</Accordion> 

## Step 3: Check response from PayU

<ReverseHashing />

<Accordion title="Sample response [Parsed]" icon="fa-reply">


* Success scenario

```
Array
(
    [mihpayid] => 403993715524069222
    [mode] => CC
    [status] => success
    [unmappedstatus] => captured
    [key] => JF***g
    [txnid] => EaE4ZO3vU4iPsp
    [amount] => 10.00
    [cardCategory] => domestic
    [discount] => 0.00
    [net_amount_debit] => 12
    [addedon] => 2021-09-08 19:37:19
    [productinfo] => iPhone
    [firstname] => Ashish
    [lastname] => 
    [address1] => 
    [address2] => 
    [city] => 
    [state] => 
    [country] => 
    [zipcode] => 
    [email] => test@gmail.com
    [phone] => 9876543210
    [udf1] => 
    [udf2] => 
    [udf3] => 
    [udf4] => 
    [udf5] => 
    [udf6] => 
    [udf7] => 
    [udf8] => 
    [udf9] => 
    [udf10] => 
    [hash] => ed99957adb08fea56c907b88e8d158a79c3562c67f96c298461509826f77a7ae9e88b2a176b3234c25f50bcd451271728719656f3bb59c13a52bebabc468615a
    [field1] => 0608273386032718000015
    [field2] => 986987
    [field3] => 10.00
    [field4] => 403993715524069222
    [field5] => 100
    [field6] => 02
    [field7] => AUTHPOSITIVE
    [field8] => 
    [field9] => Transaction is Successful
    [payment_source] => payu
    [PG_TYPE] => CC-PG
    [bank_ref_num] => 0608273386032718000015
    [bankcode] => CC
    [error] => E000
    [error_Message] => No Error
    [name_on_card] => payu
    [cardnum] => 512345XXXXXX2346
		[tcs_amount] => 2
)
```

* Failure scenario

```
Array
(
    [mihpayid] => 20869277619
    [mode] => CC
    [status] => failure
    [unmappedstatus] => failed
    [key] => L43t1c
    [txnid] => 26ba7cd6a67b0a010542
    [amount] => 10.00
    [cardCategory] => domestic
    [discount] => 0.00
    [net_amount_debit] => 0.00
    [addedon] => 2024-09-05 17:46:10
    [productinfo] => Product Info
    [firstname] => Payu-Admin
    [lastname] => 
    [address1] => 
    [address2] => 
    [city] => 
    [state] => 
    [country] => 
    [zipcode] => 
    [email] => test@example.com
    [phone] => 1234567890
    [udf1] => 
    [udf2] => 
    [udf3] => 
    [udf4] => 
    [udf5] => 
    [udf6] => 
    [udf7] => 
    [udf8] => 
    [udf9] => 
    [udf10] => 
    [hash] => ac7720e4bc33e5494bec6d37302e522171175a987f9d47286bfd29e8a7fc794f56433fcacf0bc120db781c4dc1d05a4857d71e83f00f6ed6aa9c97a1938b9467
    [field1] => 
    [field2] => 
    [field3] => 
    [field4] => 
    [field5] => 05
    [field6] => 
    [field7] => AUTHNEGATIVE
    [field8] => 
    [field9] => Authorization failed at Bank
    [payment_source] => payu
    [pa_name] => PayU
    [PG_TYPE] => CC-PG
    [bank_ref_num] => 2409052690
    [bankcode] => AMEX
    [error] => E1903
    [error_Message] => Authorization failed at Bank
    [cardnum] => XXXXXXXXXXXX2003
    [cardhash] => This field is no longer supported in postback params.
		[tcs_amount] => 2
)
```
</Accordion> 

## Step 4: Verify the Payment

Verify the transaction details using the Verification APIs. For API reference, refer to [Verify Payment API](doc:verify_payment_api) under API Reference.
