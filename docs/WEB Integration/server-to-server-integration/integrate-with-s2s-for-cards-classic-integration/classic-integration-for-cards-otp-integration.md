---
title: Classic Integration for Cards - OTP Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
The Server-to-Server (S2S) integration for cards allows merchants to securely process card transactions using PayU’s classic integration method. This document describes the step-by-step process to integrate and handle card submissions, OTP verification, and transaction responses.

1. Initiate Payment Request with PayU
   * The merchant sends a payment request to PayU with necessary parameters such as transaction details, customer information, and surl/furl URLs for redirection after processing.
   * The transaction parameters must comply with the PayU Classic Integration. For more information, refer to [Cards Classic Integration](ref:_payment_s2s_classic_integration).

> 📘 Reference:
>
> This integration is supported for Cards, Network Tokens, Payu token based integrations. For more details how to pass the network token and payu token, refer to [Collect Payments using a Saved Card](doc:collect-payments-using-a-saved-card).

1. Handle the OTP Flow or Redirect the Customer
   * After receiving PayU’s response to the initiate payment request (Step 1), merchants can choose one of the below paths based on the response conditions:
   * Collect and submit the OTP using the **Native Submit OTP API**.
   * Redirect the customer to the Bank Page for OTP entry if required.
2. Check Response from PayU

* After the transaction process (either through OTP submission or bank redirection), PayU will send the final response to the URLs (surl/furl) provided in Step 1.
* The merchant should validate the response to confirm whether the transaction was successful.

### Step 1: Initiate Payment request with PayU

The merchant initiates PayU with the required transaction mandatory or optional parameters. This needs to be a server-to-server cURL call request. URL, parameters, and descriptions. For more information, refer to . Collect the response in the  under API Reference. The response for the S2S payment request is not similar to Merchant Hosted or PayU Hosted Checkout. For description of response parameters, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

**Environment**

**Hashing**

You must hash the request parameters using the following hash logic:

sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)

For more information, refer to .

### Sample request

<br />

### Sample Responses

<br />

<br />

#### Response When Native Submit OTP is Supported

<br />

\{\
"metaData": \{\
"txnId": "payuTestTransaction3818940",
"txnStatus": "Enrolled",
"unmappedStatus": "pending",
...
},

<br />

"result": \{\
"acsTemplate": "Base64\_encoded\_HTML\_form\_string"\
},
"binData": \{
"pureS2SSupported": true,
"issuingBank": "UBI",
"category": "debitcard",
"cardType": "VISA",
"isDomestic": true
}
}

<br />

#### Response When Native Submit OTP is NOT Supported

<br />

\{\
"metaData": \{\
"txnId": "payuTestTransaction3818940",
"txnStatus": "Enrolled",
"unmappedStatus": "pending",
...
},
"result": \{
"acsTemplate": "Base64\_encoded\_HTML\_form\_string"
},
"binData": \{
"pureS2SSupported": false,
"issuingBank": "UBI",
"category": "debitcard",
"cardType": "VISA",
"isDomestic": true
}
}

<br />

**Note**

<br />

### Step 2: Handle OTP or Redirect

<br />

<br />

#### When Native Submit OTP is Supported

<br />

If the response from Step 1 contains the parameters: - metaData.unmappedStatus = pending - binData.pureS2SSupported = true

<br />

Then, the following actions should be taken: 1. Collect the OTP from the customer. 2. Submit the OTP to PayU using the .

<br />

#### When Native Submit OTP is NOT Supported

<br />

If the response contains: - metaData.unmappedStatus = pending - binData.pureS2SSupported = false

<br />

The following actions should be performed: 1. Decode result.acsTemplate from the response using Base64 decoding. 2. Generate the HTML form from the decoded template. 3. Redirect the customer to the Bank Page to enter the OTP.

<br />

### Associated Actions on the OTP Page

<br />

When collecting the OTP on your page, you must provide the following functionality to the customer: - **Resend OTP**: Enable customers to request another OTP using the .

* **Redirect to Bank Page**: If merchants decide to redirect the customer, decode the acsTemplate and redirect them to the bank for transaction completion.
  <br />
  : Ensure you decode the acsTemplate to redirect the customer to the proper bank interface.
  <br />

### Step 3: Check response from Payu and Do Verify Payment.

This will be a call back on the URL provided by you.

**Hash validation logic for payment response (Reverse Hashing)**

While sending the response, PayU takes the exact same parameters that were sent in the request (in reverse order) to calculate the hash and returns it to you. You must verify the hash and then mark a transaction as a success or failure. This is to make sure the transaction has not tampered within the response.

The order of the parameters is similar to the following code block:

sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)

**Response parameters**

The parameters in the response for similar for all the S2S flows. For more information, refer to for response and  for response parameter description.

**Sample response**

**For native Submit OTP response will be provided on the API call itself.**

**For redirection to bank response will be returned on the SURL/FURL basis on the payment response.**

```
"mihpayid" :  "403993715524046125" 

"mode" :  "DC" 

"status" :  "success" 

"unmappedstatus" :  "captured" 

"key" :  "smsplus" 

"txnid" :  "payuTestTransaction5700849" 

"amount" :  "1.00" 

"cardCategory" :  "domestic" 

"discount" :  "0.00" 

"net_amount_debit" :  "1.00" 

"addedon" :  "2022-12-03 15:03:08" 

"productinfo" :  "Product Info" 

"firstname" :  "Ashish" 

"lastname" :  "" 

"address1" :  "" 

"address2" :  "" 

"city" :  "" 

"state" :  "" 

"country" : ""  

"zipcode" :  "" 

"email" :  "test@payu.in" 

"phone" :  "9876543210" 

"udf1" :  "" 

"udf2" :  "" 

"udf3" :  "" 

"udf4" :  "" 

"udf5" :  "" 

"udf6" :  "" 

"udf7" :  "" 

"udf8" :  "" 

"udf9" :  "" 

"udf10" :  "" 

"hash" :  "6586bb33ed936d07f866cfeb42b9af99e9408270bd31c722ab3a11e61f6b6581cee3cd4f1b8b4aec3a6695c764e5cd76597832735e1e924f2ac0defbd6b3b68f" 

"field1" :  "" 

"field2" :  "" 

"field3" :  "" 

"field4" :  "" 

"field5" :  "" 

"field6" :  "" 

"field7" :  "AUTHPOSITIVE" 

"field8" :  "" 

"field9" :  "Success Transaction" 

"payment_source" :  "payuS2S" 

"PG_TYPE" :  "DC-PG" 

"bank_ref_num" :   

"bankcode" :  "VISA" 

"error" :  "E000" 

"error_Message" : "success"  

"cardnum" :  XXXXXXXXXXXX8811 

"cardhash" :  "This field is no longer supported in postback params." 

"issuing_bank" :  "UBI" 

"card_type" :  "VISA" 
```

Verify the payment and do webhook verification:

Call Verify\_payment API to check the transaction status.

Integrate with webhooks here.

[https://docs.payu.in/docs/webhooks](https://docs.payu.in/docs/webhooks)

|                        |                                                                     |
| ---------------------- | ------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
| Production Environment | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |

| Parameter | Description | Example |
| --------- | ----------- | ------- |

\| key\
mandatory | String Merchant key provided by PayU during onboarding. |  |
\| txnid
mandatory | String The transaction ID is a reference number for a specific order that is generated by the merchant. |  |
\| amount mandatory | String The payment amount for the transaction. |  |
\| productinfo mandatory | String A brief description of the product. |  |
\| firstname mandatory | String The first name of the customer. | Ashish |
\| email
mandatory | String The email address of the customer. |  |
\| phone
mandatory | String The phone number of the customer. |  |
\| pg
mandatory | String The pg parameter determines which payment tabs will be displayed on the PayU page. For cards, 'CC' will be the value. | CC |
\| bankcode mandatory | String Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option’s bank code value in it. For more information, refer to
Card Type Codes and Supported Banks for Cards. | AMEX |
\| ccnum
mandatory | String Use 13-19 digit card number for credit/debit cards (15 digits for AMEX, 13-19 for Maestro) and validate with LUHN algorithm. Refer to Card Number Formats and display error message on invalid input. | 5123456789012346 |
\| ccname mandatory | String This parameter must contain the name on card – as entered by the customer for the transaction. | Ashish Kumar |
\| ccvv
mandatory | String Use 3-digit CVV number for credit/debit cards and 4-digit security code (4DBC/CID) for AMEX cards. Validate with BIN API. | 123 |
\| ccexpmon mandatory | String This parameter must contain the card’s expiry month – as entered by the user for the transaction. It must always be in 2 digits or in MM format. For months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – It should be 10,11 and 12 respectively. | 10 |
\| ccexpyr
mandatory | String This parameter must contain the card’s expiry year – as entered by the customer for the transaction. It must be of four digits. | 2021 |
\| furl
mandatory | String The success URL, which is the page PayU will redirect to if the transaction is successful. |  |
\| surl
mandatory | String The Failure URL, which is the page PayU will redirect to if the transaction is failed. |  |
\| hash
mandatory | String It is the hash calculated by the merchant. The hash calculation logic is:
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT) |  |
\| txn\_s2s\_flow
mandatory | String This parameter must be passed with the value as:
- 4 for Legacy Decoupled flow.
- 3 for Direct Authorization. |  |
\| s2s\_client\_ip
mandatory | String This parameter must have the source IP of the customer. |  |
\| s2s\_device\_info
mandatory | String This parameter must have the customer agent's device. |  |
\| address1
optional | String The first line of the billing address.
For Fraud Detection: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information. | Line 1 address |
\| address2
optional | String The second line of the billing address. | Line 2 address |
\| city
optional | String The city where your customer resides as part of the billing address. | Gurugram |
\| state
optional | String The state where your customer resides as part of the billing address, | HR |
\| country
optional | String The country where your customer resides. | INDIA |
\| zipcode
optional | String Billing address zip code is mandatory for the cardless EMI option.
Character Limit-20 | 122011 |
\| udf1
optional | String User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5. | Some value |
\| udf2
optional | String User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5. | Some value |
\| udf3
optional | String User-defined fields (udf) are used to store any information corresponding to a particular transaction. | Some value |
\| udf4
optional | String User-defined fields (udf) are used to store any information corresponding to a particular transaction. | Some value |
\| udf5
optional | String User-defined fields (udf) are used to store any information corresponding to a particular transaction. | Some value |
\| authorization\_flow
optional | String If merchant only wants to redirection experience for the OTP submission, then they have to  pass the value of this parameter as “REDIRECT”, if this param not passed, Payu will provide the response basis on the bin (first 9 digits of the card/token number) | REDIRECT |