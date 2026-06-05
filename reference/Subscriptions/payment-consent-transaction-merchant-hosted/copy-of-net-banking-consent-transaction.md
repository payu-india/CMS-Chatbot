---
title: '[Internal Review] Net Banking Consent Transaction - Plans'
deprecated: false
hidden: true
metadata:
  title: Net Banking Recurring Payment Consent Transaction
  description: >-
    Explore how to set up a Netbanking Recurring Payment Consent Transaction
    using Merchant Hosted Checkout. This API documentation for integrating
    PayU's Netbanking or Net Banking consent feature, enabling secure and
    efficient recurring payments for your customers.
  keywords:
    - PayU Netbanking Recurring Payment for Custom Checkout
    - Netbanking Consent Transaction for Custom Checkout
    - PayU Netbanking Recurring Payment for Merchant Hosted Checkout
    - Netbanking Consent Transaction for Merchant Hosted Checkout
    - PayU recurring payments
    - PayU subscription payments registration for Net Banking
    - Net Banking Registration transaction
    - Netbbanking Registration transaction
    - Netbanking Autopay
    - Autopay for NetBanking non-PACB flow
    - Netbanking Autopay Consent Transaction
    - Net Banking Autopay
    - Autopay for Net Banking non-PACB flow
    - Net Banking Autopay Consent Transaction
  robots: index
next:
  pages:
    - slug: using-api-integration-recurring-payments
      title: Using API Integration
      type: basic
    - slug: customer-experience-and-workflow-recurring-payments
      title: Customer Experience and Workflow
      type: basic
---
> 📘
>
>

This section provides the request parameters, sample request and response for a Net Banking Recurring Payment consent transaction or Consent transaction.

> 📘 Note:
>
> During integration with PayU, first integrate with the Test Server environment. PayU will provide you the necessary Merchant Key for the test serve. After testing is done, you are ready to move to the Production server.

<br />

> 👍
>
> Experience the end-to-end **Merchant Hosted Checkout** > **Net Banking** flow and instantly generate the complete code for seamless, zero-coding integration into your website.
>
>   
>
> <HTMLBlock>{`
>                                     <style>
>                                     .tooltip-btn {
>                                         position: relative;
>                                         background-color: #4CAF50;
>                                         color: white;
>                                         padding: 10px 20px;
>                                         border: none;
>                                         border-radius: 5px;
>                                         cursor: pointer;
>                                         font-weight: bold; /* Added this line */
>                                     }
>                                     .tooltip-btn:hover::after {
>                                         content: attr(data-tooltip);
>                                         position: absolute;
>                                         bottom: 125%;
>                                         left: 50%;
>                                         transform: translateX(-50%);
>                                         background-color: #333;
>                                         color: white;
>                                         padding: 5px 10px;
>                                         border-radius: 4px;
>                                         white-space: nowrap;
>                                         font-size: 12px;
>                                         z-index: 1;
>                                     }
>                                     </style>
>
>                                     <button onclick="window.open('https://payu.in/integrationlab/seamless/sm-nb-subscription', '_blank')" 
>                                             class="tooltip-btn" 
>                                             data-tooltip="Click here to see the Merchant Hosted Checkout > Net Banking > Consent Registration end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">
>                                         Experience the flow and get the code
>                                     </button>
> `}</HTMLBlock>

<br />

HTTP Method: **POST**

**Environment**

|                        |                                                                      |
| :--------------------- | :------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/\_payment](https://test.payu.in/_payment>)     |
| Production Environment | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment>) |

## Request parameters

<HTMLBlock>{`
<style>
/* Target only the second column in the table */
.markdown-body table td:nth-child(2) {
  word-break: break-word !important;
}

/* Keep the first column from breaking unnecessarily */
.markdown-body table td:nth-child(1) {
  word-break: normal;
  white-space: nowrap;
}
</style> <table> <thead> <tr> <th style="border: 1px solid #ddd; "><strong>Parameter</strong></th> <th style="border: 1px solid #ddd; "><strong>Description</strong></th> <th style="border: 1px solid #ddd; "><strong>Value</strong></th> </tr> </thead> <tbody> <tr> <td style="border: 1px solid #ddd; "><p>key<br/><code>mandatory</code></p> </td> <td style="border: 1px solid #ddd; "><p><code>String</code> The merchant key is a unique identifier for a merchant account in PayU's database.</p> </td> <td style="border: 1px solid #ddd; "><p>Your Test Key</p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>api_version<br/><code>optional</code></p> </td> <td style="border: 1px solid #ddd; "><p><code>String</code> The API version for this API.</p> </td> <td style="border: 1px solid #ddd; "><p>7</p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>txnid<br/><code>mandatory</code></p> </td> <td style="border: 1px solid #ddd; "><p><code>String</code> The transaction ID is a reference number for a specific order that is generated by the merchant. It is used to track the order and must be unique. PayU's system will not accept duplicate transaction IDs.<br/><strong>Note</strong>: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID.'</p> </td> <td style="border: 1px solid #ddd; "><p>s7hhDQVWvbhBdN</p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>amount<br/><code>mandatory</code></p> </td> <td style="border: 1px solid #ddd; "><p><code>String</code> This field should contain the payment amount for the transaction.<br/>The transaction limit is as follows:  </p> <ul> <li><strong>Net Banking authentication</strong>: Rs.10,00,000</li> <li><strong>eNACH Aadhaar authentication</strong>: Rs.1,00,000</li> </ul> </td> <td style="border: 1px solid #ddd; "><p>10.00.</p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>productinfo<br/><code>mandatory</code></p> </td> <td style="border: 1px solid #ddd; "><p><code>String</code> It should be a string containing a brief description of the product.<code>Character Limit-100</code></p> </td> <td style="border: 1px solid #ddd; "><p>iPhone</p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>firstname<br/><code>mandatory</code></p> </td> <td style="border: 1px solid #ddd; "><p><code>String</code> The first name of the customer.<code>Character Limit-60</code></p> </td> <td style="border: 1px solid #ddd; "><p>Ashish</p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>email<br/><code>mandatory</code></p> </td> <td style="border: 1px solid #ddd; "><p><code>String</code> The email of the customer.<code>Character Limit-50</code></p> </td> <td style="border: 1px solid #ddd; "><p><a href="mailto:test@gmail.com">test@gmail.com</a></p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>phone<br/><code>mandatory</code></p> </td> <td style="border: 1px solid #ddd; "><p><code>String</code> The phone number of the customer.</p> </td> <td style="border: 1px solid #ddd; "><p>9876543210</p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>lastname<br/><code>mandatory</code></p> </td> <td style="border: 1px solid #ddd; "><p><code>String</code> The last name of the customer.<code>Character Limit-60</code></p> </td> <td style="border: 1px solid #ddd; "><p>Verma</p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>address1<br/><code>optional</code></p> </td> <td style="border: 1px solid #ddd; "><p><code>String</code> The first line of the billing address.<code>Character Limit-100</code></p> </td> <td style="border: 1px solid #ddd; "><p>H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai</p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>address2<br/><code>optional</code></p> </td> <td style="border: 1px solid #ddd; "><p><code>String</code> The second line of the billing address.<code>Character Limit-100</code></p> </td> <td style="border: 1px solid #ddd; "><p>34 Saikripa-Estate, Tilak Nagar</p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>city<br/><code>optional</code></p> </td> <td style="border: 1px solid #ddd; "><p><code>String</code> The city where your customer resides as part of the billing address.</p> </td> <td style="border: 1px solid #ddd; "><p>Mumbai</p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>state<br/><code>optional</code></p> </td> <td style="border: 1px solid #ddd; "><p><code>String</code> The state where your customer resides as part of the billing address,</p> </td> <td style="border: 1px solid #ddd; "><p>Maharashtra</p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>country<br/><code>optional</code></p> </td> <td style="border: 1px solid #ddd; "><p><code>String</code> The country where your customer resides.<code>Character Limit-50</code></p> </td> <td style="border: 1px solid #ddd; "><p>India</p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>zipcode<br/><code>optional</code></p> </td> <td style="border: 1px solid #ddd; "><p><code>String</code> Billing address zip code is mandatory for the cardless EMI option.<code>Character Limit-20</code></p> </td> <td style="border: 1px solid #ddd; "><p>400004</p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>si<br/><code>mandatory</code></p> </td> <td style="border: 1px solid #ddd; "><p>This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.<br/><strong>Notes</strong>: You can modify or cancel existing recurring payment registration as described in the following sections:<br/>_.   <a href="http://docs.payu.in/reference/manage-recurring-payment-for-cards">Manage Recurring Payment for Cards</a><br/>_.   <a href="http://docs.payu.in/reference/api-commands-to-manage-upi-recurring-transaction">Manage UPI Recurring Transaction</a></p> </td> <td style="border: 1px solid #ddd; "><p>1</p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>si_details<br/><code>mandatory</code></p> </td> <td style="border: 1px solid #ddd; "><p>This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.  </p> <p><strong>Note</strong>: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers ( for more details refer – <a href="https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668&amp;Mode=0">https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668&amp;Mode=0</a> )  </p> <p>This is a JSON object and it includes a set of fields. For more information,  refer to <a href="http://docs.payu.in/reference/si-parameter-json-details">SI Parameter JSON Details</a></p> </td> <td style="border: 1px solid #ddd; "></td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>beneficiarydetail<br/><code>mandatory for Net Banking</code></p> </td> <td style="border: 1px solid #ddd; "><p><code>varchar</code> This object represents bank account details of the customer which involves account number, name on the account and account type and needs to be passed if the recurring transaction needs to be set up against Net Banking. It includes the fields as mentioned in the <a href="#beneficiarydetail-fields-description">beneficiarydetail fields description</a> table.</p> </td> <td style="border: 1px solid #ddd; "><p>Refer to next sectoin</p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>hash<br/><code>mandatory</code></p> </td> <td style="border: 1px solid #ddd; "><p><code>String</code> It is used to avoid the possibility of transaction tampering. For more information on hash generation process, refer to <a href="http://docs.payu.in/docs/generate-hash-merchant-hosted">Generate Hash</a>.<br/>In the case of registration transaction, the formula is used to calculate this hash is similar to the following:<br/><code>HASH = SHA512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\||\||\||si_details\|SALT)</code></p> </td> <td style="border: 1px solid #ddd; "><p><code>eabec285da28fd 0e3054d41a4d24fe 9f7599c9d0b6664 6f7a9984303fd612 4044b6206daf831 e9a8bda28a6200d 318293a13d6c193 109b60bd4b4f8b09 c90972</code></p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>pg<br/><code>mandatory</code></p> </td> <td style="border: 1px solid #ddd; "><p><code>String</code> The pg parameter must include ENACH for Net Banking.</p> </td> <td style="border: 1px solid #ddd; "><p>ENACH</p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>bankcode<br/><code>mandatory</code></p> </td> <td style="border: 1px solid #ddd; "><p>\`String. The merchant must post this parameter with the corresponding payment option's bank code value in it.  For more information, refer to <a href="http://docs.payu.in/docs/bank-codes-recurring-payments">Bank Codes - Recurring Payments</a>.</p> </td> <td style="border: 1px solid #ddd; "><p>ICICENCC</p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>udf1 - udf5<br/><code>optional</code></p> </td> <td style="border: 1px solid #ddd; "><p><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.<br/><code>Character Limit</code>-255</p> </td> <td style="border: 1px solid #ddd; "><p>Payment Preference, Shipping Method, Shipping Address1, Shipping City, Shipping Zip Code, etc.</p> </td> </tr> <tr> <td style="border: 1px solid #ddd; "><p>free_trial<br/><code>optional</code></p> </td> <td style="border: 1px solid #ddd; "><p>This is mandatory only if the merchant wants to support free trial use cases.
In this case, PayU adjusts the transaction amount as INR 2.00 for cards and UPI and INR 0.00 for Net Banking irrespective of what amount is passed against the amount field in the request.<br/>This parameter has no significance in the case of seamless flow.</p> </td> <td style="border: 1px solid #ddd; "></td> </tr>  </tbody> </table>
`}</HTMLBlock>

### beneficiarydetail fields description

#### Sample object

```
{"beneficiaryName": "Sachin Tendulkar","beneficiaryAccountNumber": "1211450021","beneficiaryAccountType": "SAVINGS", "beneficiaryIfscCode":"ICIC0000046", "verificationMode":"DEBIT_CARD"}
```

#### description

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Field</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>BeneficiaryName</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Registered name against customer’s account</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>BeneficiaryAccountNumber</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Account number against which recurring transactions need to be executed.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>BeneficiaryAccountType</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>SAVINGS or CURRENT</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>beneficiaryIfscCode</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>11-digit IFSC code of the customer bank</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>verificationMode</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The verification mode can be any of the following:  </p>
<ul>
<li><strong>DEBIT_CARD</strong> – authentication will be done through a debit card. If no value is provided, then it will trigger Net Banking login password flow.</li>
<li><strong>AADHAAR</strong> – authentication will be done through a Aadhaar card. If no value , then it will trigger net banking login password flow.  If no value is provided, then it will trigger Net Banking login password flow.</li>
</ul>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

If the merchant sends any other special characters, then they will be automatically removed. The address parameter will consider only the first 100 characters.

When the transaction POST REQUEST hits the PayU server, a new transaction entry is created in the PayU Database. A unique identifier is created in the PayU database to identify each new transaction. This identifier is known as the PayU ID (or mihpayid).

The Net Banking recurring payment registration is also known as e-Mandate. The request for Net Banking involves the following extra parameters posted compared to Cards or UPI:

- billingCycle
- billingInterval
- paymentStartDate
- paymentEndDate
- billingAmount
- beneficiaryName
- beneficiaryAccountNumber
- beneficiaryAccountType
- ifscCode
- verificationMode (optional)

### Sample request with Debit Card as Verification mode

The sample code block for Net Banking Seamless integration (Merchant-Hosted Checkout) with the **verificationMode** field of the **beneficiaryDetail** JSON parameter with the values as **DEBIT\_CARD** is similar to the following:

```curl
curl -X \
 POST "https://test.payu.in/_payment
-H \
 "accept: application/json" -H \
 "Content-Type: application/x-www-form-urlencoded" -d
"key=JP***g&txnid=oRWSUMU4XSQBZn&amount=0.0&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&si=1&pg=ENACH&bankcode=ICICENCC&surl=https://apiplayground-response.herokuapp.com/&furl=&api_version=7&beneficiarydetail={“beneficiaryName”: “Ashish Kumar”,”beneficiaryAccountNumber”: “1211450021”,”beneficiaryAccountType”: “SAVINGS”, “beneficiaryIfscCode“:”ICIC0000046”, “verificationMode”:”DEBIT_CARD”} Kumar&hash=dbe874c46dcd68ae8c6dd14d04e213f4dff1f2f89106653f61df3e8cee900df33d976e737a82291dfbea3d54d3c67c403d7371c387a1e9652e27ec682d3dce21"
```

### Sample request with Aadhaar as Verification mode

The sample code block for Net Banking Seamless integration (Merchant-Hosted Checkout) with the **verificationMode** field of the **beneficiaryDetail** JSON parameter with the values as **Aadhaar** is similar to the following:

```
curl -X \ 
POST "https://test.payu.in/_payment 
 -H \
"accept: application/json" -H \
"Content-Type: application/x-www-form-urlencoded" -d
"key=JP***g&txnid=oRWSUMU4XSQBZn&amount=0.0&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&si=1&pg=ENACH&bankcode=ICICENCC&surl=
https://apiplayground-response.herokuapp.com/&furl=&api_version=7&beneficiarydetail={“beneficiaryName”:
“Ashish Kumar”,”beneficiaryAccountNumber”: “1211450021”,”beneficiaryAccountType”: “SAVINGS”, “beneficiaryIfscCode“:”ICIC0000046”, “verificationMode”:”AADHAAR”} Kumar&hash=dbe874c46dcd68ae8c6dd14d04e213f4dff1f2f89106653f61df3e8cee900df33d976e737a82291dfbea3d54d3c67c403d7371c387a1e9652e27ec682d3dce21"
```

## Sample response

For Net Banking, you must ensure that the payment response from PayU has the expected values as described in the following table so that Net Banking registration is successful or initiated successfully with the customer’s bank.

| **Response Parameter** | **Expected Value**               | **Description**                                                                 |
| ---------------------- | -------------------------------- | ------------------------------------------------------------------------------- |
| status                 | success                          | This indicates that the transaction is successful                               |
| payment\_source        | sist                             | Indicates that bank details have been marked correctly for Standing Instruction |
| mihpayid               | \<mihpayid number> sent. by PayU | Indicates PayU’s transaction acknowledgment for a Consent transaction           |

The response URL returned from PayU is in the form URL format (application/x-www-form-urlencoded).

### Parsed response

```
Array
(
    [mihpayid] => 403993715525331373
    [mode] => ENACH
    [status] => success
    [unmappedstatus] => captured
    [key] => JPM7Fg
    [txnid] => oRWSUMU4XSQBZn
    [amount] => 0.00
    [discount] => 0.00
    [net_amount_debit] => 0
    [addedon] => 2022-02-03 19:06:55
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
    [hash] => f3f8e4088231b190930fc4b87d3f39397d1a1d02622ef4683a983244e1cd5158f39adbb67c3d87dcb4da25ae4a941ebbf55918e4575fa1c39677a774d02c0d2d
    [field1] => ENACH285259747472911093
    [field2] => 337026657857179355
    [field3] => 
    [field4] => 
    [field5] => 
    [field6] => 
    [field7] => 
    [field8] => 
    [field9] => Mandate successfully scheduled at bank end: Your payment is scheduled successfully
    [payment_source] => sist
    [PG_TYPE] => ENACH-PG
    [bank_ref_num] => 450699821592111537
    [bankcode] => ICICENCC
    [error] => E000
    [error_Message] => No Error
)
```

## Webhook for Getting Transaction Details

You can expose a webhook by requesting the PayU Integration team to configure the same against the **ws\_online\_response** parameter. If this webhook is configured, you will receive the above response object over HTTP form post method similar to the following:

```plaintext
unmappedstatus=success&phone=9999999999&txnid=FCDA1R100870163781&hash=84e335094bbcb2ddaa0f9a488eb338e143b273765d89c9dfa502402562d0b6f3c7935e28194ca92f380be7c84c3695415b106dcf52cb016a15fcf6adc98d724&status=success&curl=https://www.abc.in/payment/handlepayuresposne&firstname=NA&card_no=519619XXXXXX5049&furl=https://www.abc.in/payment/handlepayuresposne&productinfo=2&mode=DC&amount=800.00&field4=6807112311042810&field3=6807112311042810&field2=838264&field9=SUCCESS&email=NA&mihpayid=175477248&surl=https://www.ABC.in/payment/handlepayuresposne&card_hash=9e88cb0573d4a826b61d808c0a870ed4a990682459b0ec9e95ea421e8e47be8c&field1=42812&payment_source=sist
```

If the mandate is not confirmed by the customer or the mandate is confirmed by the customer, but the mandate registration is rejected from the banks, the status is communicated as a “failure” over webhook. For more information, refer to [Webhooks](doc:webhooks).
