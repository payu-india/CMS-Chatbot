---
title: PayU Hosted Checkout Integration
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: customer-journey-for-fksc
      title: Customer Journey for FKSC
    - type: basic
      slug: understanding-refunds-fksc
      title: Understanding Refunds
---
This section describes the parameters required to collect payments by redeeming the FKSC rewards with PayU Hosted Checkout integration (using the  **\_payment** API) to enforce only the Supercoins pay in the **LR** category or hide it.

## Step 1: Post the Transaction Request to PayU

The parameters for redeeming the Supercoins remain the same as mentioned in the [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout).

\*\*Environment\*\*

<table style="border:0.1rem solid rgb(242, 242, 242);"><tbody><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Test</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">https://test.payu.in/_payment</td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Production</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">https://secure.payu.in/_payment</td></tr></tbody></table>

### Enforcing FKSC Redemption as Payment Mode

If you wish to enforce the FKSC redemption as the payment and hide other payment modes, you can use the following parameters and other PayU Hosted Checkout parameters according to your requirements.

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "enforce\\_paymethod  \n**optional**",
    "0-1": "This parameter allows you to customize the payment options for each individual transaction. To enforce Flipkart Supercoins as the payment method, specify **FKSC**.",
    "0-2": "FKSC"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


### Dropping the FKSC Card Payment

If you wish to hide the Supercoin redemption as a payment mode in the **LR** category, you can use the following parameters and other PayU Hosted Checkout parameters according to your requirements.

| **Parameter**                | **Description**                                                                                                                                                                                    | **Example** |    |      |
| :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------- | :- | :--- |
| drop\_category  **optional** | This parameter is used to customize the payment options for each individual transaction. To drop the Flipkart Supercoins as the payment mode with PayU Hosted Checkout integration, specify \*\*LR | FKSC\*\*.   | LR | FKSC |

Currently, PayU only supports the FKSC redemption option under the **L**R category.

### Sample Request

For a sample request, refer to [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout).

***

## Step 2: Customer Submits Payment Details on PayU Page

The customer selects **SuperCoins Pay** as the payment option on PayU’s page.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/03/customer_journey_fksc-1024x769.png)

After the customer selects **Supercoin Pay** as the payment mode, PayU collects the Flipkart account details from the customer.

The customer performs the authorization or authentication process on the bank’s login page, and the bank communicates the success or failure response back to PayU.

***

## Step 3: Check the Response from PayU

PayU marks the transaction status based on the response received from the bank. PayU communicates the success URL to you if the payment is successful. Verify the authenticity of the hash value before accepting or rejecting the invoice order. For the list of parameters in the response body for the PayU Hosted integration, refer to [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout).

```
Introduction
Getting Started
Customer Journey
Collect Payments with PayU Hosted Checkout
Collect Payments using Merchant Hosted Checkout
Flipkart Supercoins Rewards APIs
Understanding Refunds
Search
API Reference
Plugins
Web Checkout
API Playground
Supercoins Pay Integration/Collect Payments With PayU Hosted Checkout
Collect Payments with Flipkart Supercoins-PayU Hosted Checkout
This section describes the parameters required to collect payments by redeeming the FKSC rewards with PayU Hosted Checkout integration (using the  _payment API) to enforce only the Supercoins pay in the LR category or hide it.

Steps to Integrate:
Post the transaction request to PayU
Customer submits payment details on PayU Page
Check the response from PayU
Step 1: Post the Transaction Request to PayU
The parameters for redeeming the Supercoins remain the same as mentioned in the Collect Payments with PayU Hosted Checkout.

Environment

Test	https://test.payu.in/_payment
Production	https://secure.payu.in/_payment
Enforcing FKSC Redemption as Payment Mode
If you wish to enforce the FKSC redemption as the payment and hide other payment modes, you can use the following parameters and other PayU Hosted Checkout parameters according to your requirements.

Parameter	Description	Example
enforce_paymethod
optional
This parameter allows you to customize the payment options for each individual transaction. To enforce Flipkart Supercoins as the payment method, specify FKSC.	FKSC
Dropping the FKSC Card Payment
If you wish to hide the Supercoin redemption as a payment mode in the LR category, you can use the following parameters and other PayU Hosted Checkout parameters according to your requirements.

Parameter	Description	Example
drop_category
optional
This parameter is used to customize the payment options for each individual transaction. To drop the Flipkart Supercoins as the payment mode with PayU Hosted Checkout integration, specify LR|FKSC.	LR|FKSC
Currently, PayU only supports the FKSC redemption option under the LR category.

Sample Request
For a sample request, refer to Sample Request of the Collect Payments with PayU Hosted Checkout.

Step 2: Customer Submits Payment Details on PayU Page
The customer selects SuperCoins Pay as the payment option on PayU’s page.


After the customer selects Supercoin Pay as the payment mode, PayU collects the Flipkart account details from the customer.

The customer performs the authorization or authentication process on the bank’s login page, and the bank communicates the success or failure response back to PayU.

Step 3: Check the Response from PayU
PayU marks the transaction status based on the response received from the bank. PayU communicates the success URL to you if the payment is successful. Verify the authenticity of the hash value before accepting or rejecting the invoice order. For the list of parameters in the response body for the PayU Hosted integration, refer to Collect Payments with PayU Hosted Checkout.

Array
(
    [mihpayid] => 403993715523409521
    [mode] => LR
    [status] => success
    [unmappedstatus] => captured
    [key] => JP***g
    [txnid] => 5jJ9xYceXX1ydT
    [amount] => 1000.00
    [discount] => 0.00
    [net_amount_debit] => 1000
    [addedon] => 2021-07-02 15:03:50
    [productinfo] => iPhone
    [firstname] => PayU User
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
    [hash] => 716f92a6452adadba68d133ba7f5ca3f3403f03f554e3ef850911f3e6727ee73402b249054170ad276c8b55ca12368a5e27cc69ffb0642ef6403dae9a5708794
    [field1] => 9876543210
    [field2] => 5jJ9xRceXX1ydT
    [field3] => 
    [field4] => PayU User
    [field5] => AXIhh4ExnaJ9dKiJvPxsewHwxMMmT3ba7UY
    [field6] => 
    [field7] => Transaction completed successfully
    [field8] => 
    [field9] => Transaction completed successfully
    [payment_source] => payu
    [PG_TYPE] => LR-PG
    [bank_ref_num] => 5jJ9xRceXX1ydT
    [bankcode] => FKSC
    [error] => E000
    [error_Message] => No Error
)
Array
(
    [mihpayid] => 403993715523409521
    [mode] => LR
    [status] => success
    [unmappedstatus] => captured
    [key] => JP***g
    [txnid] => 5jJ9xYceXX1ydT
    [amount] => 1000.00
    [discount] => 0.00
    [net_amount_debit] => 1000
    [addedon] => 2021-07-02 15:03:50
    [productinfo] => iPhone
    [firstname] => PayU User
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
    [hash] => 716f92a6452adadba68d133ba7f5ca3f3403f03f554e3ef850911f3e6727ee73402b249054170ad276c8b55ca12368a5e27cc69ffb0642ef6403dae9a5708794
    [field1] => 9876543210
    [field2] => 5jJ9xRceXX1ydT
    [field3] => 
    [field4] => PayU User
    [field5] => AXIhh4ExnaJ9dKiJvPxsewHwxMMmT3ba7UY
    [field6] => 
    [field7] => Transaction completed successfully
    [field8] => 
    [field9] => Transaction completed successfully
    [payment_source] => payu
    [PG_TYPE] => LR-PG
    [bank_ref_num] => 5jJ9xRceXX1ydT
    [bankcode] => FKSC
    [error] => E000
    [error_Message] => No Error
)
Next Steps
PayU Hosted Checkout Integration Workflow – Sodexo
The following describe the characteristics and workflow involved using PayU Hosted Checkout Integration with Sodexo: The existing _payment API used to initiate payments for online transactions will be used to initiate payments for Sodexo payment option. In case the merchant wants to enforce Sodexo payment option on our check out page, enforce_paymethod value should be…
Continue reading
PayU Hosted Checkout Integration Workflow – Sodexo

Fetch Balance API – Sodexo
API Command: check_balance The check_balance API command is used to check the balance of a Sodexo card. When using Seamless Integration, integrate this API and display the balance on the Checkout page to your customers. Endpoints Test Environment https://test.payu.in/merchant/postservice.php Production Environment https://info.payu.in/merchant/postservice.php Request Parameters Notes: var1 is in a JSON format. All the sub fields…
Continue reading
Fetch Balance API – Sodexo

Was this document helpful?
ON THIS PAGE
Step 1: Post the Transaction Request to PayU
Enforcing FKSC Redemption as Payment Mode
Dropping the FKSC Card Payment
Sample Request
Step 2: Customer Submits Payment Details on PayU Page
Step 3: Check the Response from PayU
Updated about 2 months ago
Twitter
Follow @PayUindia on Twitter
Github
Follow @PayUindia on Github
API Playground
API Playground
Test the actual APIs you want to use in API Playground
© 2023 PayU Docs

To the top↑
```