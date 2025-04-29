---
title: PayU Hosted Integration - Supercoins Pay
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This section describes the parameters required to collect payments by redeeming the FKSC rewards with PayU Hosted Checkout integration (using the  **\_payment** API) to enforce only the Supercoins pay in the **LR** category or hide it.

## Step 1: Post the Transaction Request to PayU

The parameters for redeeming the Supercoins remain the same as mentioned in the [PayU Hosted Checkout Integration](doc:integrate-with-payu-hosted-checkout).

**Environment**

<table style={{ border: "0.1rem solid rgb(242, 242, 242)" }}>
  <tbody>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Test</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>https://test.payu.in/_payment</td>
    </tr>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Production</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>https://secure.payu.in/_payment</td>
    </tr>
  </tbody>
</table>

### Enforcing FKSC Redemption as Payment Mode

If you wish to enforce the FKSC redemption as the payment and hide other payment modes, you can use the following parameters and other PayU Hosted Checkout parameters according to your requirements.

| **Parameter**      | **Description**                                                                                                                                                    | **Example** |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| enforce\_paymethod | This parameter allows you to customize the payment options for each individual transaction. To enforce Flipkart Supercoins as the payment method, specify **FKSC** | FKSC        |

### **Dropping the FKSC Card Payment**

If you wish to hide the Supercoin redemption as a payment mode in the **LR** category, you can use the following parameters and other PayU Hosted Checkout parameters according to your requirements.

| **Parameter**  | **Description**                                                                                                                                                                                           | **Example** |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| drop\_category | This parameter is used to customize the payment options for each individual transaction. To drop the Flipkart Supercoins as the payment mode with PayU Hosted Checkout integration, specify **LR\|FKSC**. | LR\|FKSC    |

Currently, PayU only supports the FKSC redemption option under the **L**R category.

### Sample Request

***

## Step 2: Customer Submits Payment Details on PayU Page

The customer selects **SuperCoins Pay** as the payment option on PayU’s page.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/03/customer_journey_fksc-1024x769.png)

After the customer selects **Supercoin Pay** as the payment mode, PayU collects the Flipkart account details from the customer.

The customer performs the authorization or authentication process on the bank’s login page, and the bank communicates the success or failure response back to PayU.

***

## Step 3: Check the Response from PayU

PayU marks the transaction status based on the response received from the bank. PayU communicates the success URL to you if the payment is successful. Verify the authenticity of the hash value before accepting or rejecting the invoice order. For the list of parameters in the response body for the PayU Hosted integration, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

```plaintext
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
    [payment_so
```