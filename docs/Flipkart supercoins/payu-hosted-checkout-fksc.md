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
This section describes the parameters required to collect payments by redeeming the FKSC rewards with PayU Hosted Checkout integration (using the  **_payment** API) to enforce only the Supercoins pay in the **LR** category or hide it.

## Step 1: Post the Transaction Request to PayU

The parameters for redeeming the Supercoins remain the same as mentioned in the [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout).

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

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>enforce_paymethod<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter allows you to customize the payment options for each individual transaction. To enforce Flipkart Supercoins as the payment method, specify <strong>FKSC</strong>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>FKSC</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

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

PayU marks the transaction status based on the response received from the bank. PayU communicates the success URL to you if the payment is successful. Verify the authenticity of the hash value before accepting or rejecting the invoice order. For the list of parameters in the response body for the PayU Hosted integration, refer to [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout).