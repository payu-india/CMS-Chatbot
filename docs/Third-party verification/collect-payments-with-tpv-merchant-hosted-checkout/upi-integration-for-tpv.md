---
title: UPI Integration
deprecated: false
hidden: false
metadata:
  title: UPI TPV Integration - Merchant Hosted Checkout
  description: >-
    Discover how to integrate UPI with Third Party Validation (TPV) using PayU's
    detailed guide. This documentation offers step-by-step instructions, API
    specifications, and best practices for efficient and secure payment
    processing. Streamline your online payment solutions with seamless UPI
    integration.
  keywords:
    - UPI Integration for TPV
    - ' Third Party Validation UPI Integration'
    - API Integration for UPI TPV
    - ' PayU UPI TPV Integration'
    - TPV UPI Setup Guide
  robots: index
next:
  description: ''
---
Integrate TPV through UPI using the procedure described in this section.

## Prerequisites

Merchant Hosted or S2S (Seamless) integration has to be done as per the standard kit. For more information, refer to  [UPI Integration](doc:collect-payments-with-upi-seamless).

## Step 1: Validate VPA

When your customer makes payment through UPI, you can validate the customer’s Virtual Payment Address (VPA) and then initiate payment. The **validateVpa** API is used to validate the UPI handle. Validate the VPA (UPI handle) using the **validateVpa** API. For more information, refer to [Validate VPA Handle API](ref:validate_vpa_api).

***

## Step 2: Post the parameters to PayU

With the following parameters, make the transaction request with the customer’s bank account number to the PayU using the Collect Payment (**\_payment**) API.

**Environment**

|                            |                                                                         |
| -------------------------- | ----------------------------------------------------------------------- |
| **Test Environment**       | [https://test.payu.in/\_payment>](https://test.payu.in/_payment%3E)     |
| **Production Environment** | [https://secure.payu.in/\_payment>](https://secure.payu.in/_payment%3E) |

### Request parameters

#### beneficiarydetail JSON Object Fields

It must contain the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key). You can post up to five account details in this parameter. For example:

```
{"beneficiaryAccountNumber":"002001600674|00000031957292212|00000035955239352|00000035955239352",  
"ifscCode":"KTKB0000046|KTKB0000023|KTKB0000035|KTKB0000035"}
```

#### Checksum Logic for Hash

The following hash logic must be used for the parameters posted:

> 📘 beneficiarydetail parameter in Hashing:
>
> The **beneficiarydetail** parameter value will be at last or the last value to be appended.
>
> ```plaintext
> key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3
> |udf4|udf5||||||beneficiarydetail|SALT
> ```

## Step 3: Check the response from PayU

### Hash Validation Logic for Payment Response (Reverse Hashing)

While sending the response, PayU takes the exact same parameters that were sent in the request (in reverse order) to calculate the hash and returns it to you. You must verify the hash and then mark a transaction as a success or failure. This is to make sure the transaction has not tampered within the response.

The order of the parameters is similar to the following code block:

```
sha512(SALT|beneficiarydetail|status||||||udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

### Response parameters

The following table describes the parameters in the response from PayU:

| **Param Name**   | **Description**                                                                                                                                                                                                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mihpayid         | It is a unique reference number created for each transaction at PayU’s end. You must note this transaction ID as this will be used as a reference for all the future actions on this transaction like Inquiry or Refund.                                                                                                 |
| merchantid       | It is the unique ID of the merchant.                                                                                                                                                                                                                                                                                     |
| txnid            | This parameter would contain the transaction ID value posted by the merchant during the transaction request.                                                                                                                                                                                                             |
| transaction\_fee | The transaction fee for the TPV transaction. For Net Banking, INR 10 is charged by default.                                                                                                                                                                                                                              |
| discount         | The discount amount given by bank on the transaction fee (if any).                                                                                                                                                                                                                                                       |
| amount           | The net amount after discount (if any) is displayed in this parameter. For Net Banking, INR 10 is charged by default.                                                                                                                                                                                                    |
| paymentgatewayid | The payment gateway identifier for the bank sending the response.                                                                                                                                                                                                                                                        |
| pg               | The payment gateway used for the transaction. In case of UPI, it is “UPI.”                                                                                                                                                                                                                                               |
| status           | This parameter gives the status of the transaction as either success, failed or pending. Possible values: success, failure, pending If the value of the ‘status’ parameter is ’success’, the transaction is successful. If the value of ‘status’ is ‘failure’ or ‘pending’, must be treated as a failed transaction only |
| PG\_Type         | The bankcode (as in Merchant Hosted Checkout integration) of the bank is returned in the parameter.                                                                                                                                                                                                                      |
| key              | This parameter contains the merchant key for the merchant’s account at PayU. It would be the same as the key used while the transaction request is being posted from the merchant’s end to PayU.                                                                                                                         |
| riskactionStr    | This parameter contains risk action (if any) taken on the account holder.                                                                                                                                                                                                                                                |
| addedon          | The transaction timestamp is returned in this parameter.                                                                                                                                                                                                                                                                 |

> 📘 Store the mihpayid and txnid parameter values in response:
>
> PayU recommends you to make provisions to store the **mihpayid** and **txnid** parameter values (in the response) in your server as proof that TPV has been completed for a customer.

### Sample response

The formatted response from PayU:

```
Array
(
    [mihpayid] => 403993715524308315
    [mode] => UPI
    [status] => success
    [unmappedstatus] => captured
    [key] => JP***g
    [txnid] => Job7NydtwPVAmy
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2021-10-05 12:51:20
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
    [hash] => de4f82af65458c84080d6515c1a80d42af703be390346ef020974e520efeb4ab9ebe4752e63e70d6f00dedd671c663dfdb22d0f0c818c52790e911e8babd3f6e
    [field1] => anything@payu
    [field2] => Job7NydtwPVAmy
    [field3] => 
    [field4] => Ashish
    [field5] => AXImAH1BxekGdTLY7qgjMXffAAjJj5Q75mY
    [field6] => 
    [field7] => Transaction completed successfully
    [field8] => 
    [field9] => Transaction completed successfully
    [payment_source] => payu
    [PG_TYPE] => UPI-PG
    [bank_ref_num] => Job7NydtwPVAmy
    [bankcode] => UPI
    [error] => E000
    [error_Message] => No Error
)

```

> 📘 Verify payment:
>
> PayU recommends you. to verify the transaction details using the **Verification Payment** API. For more information, For API reference, refer to <a href="https://docs.payu.in/reference/verify_payment_api" target="_blank">Verify Payment API</a>.