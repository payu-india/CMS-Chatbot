---
title: Merchant Hosted BNPL Workflow
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - Merchant Hosted Checkout BNPL Integration
    - BNPL Seamless Integration with PayU
    - PayU Seamless BNPL integration
    - Buy Now Pay Later Integration with Merchant Hosted Checkout
    - BNPL API Integration Pay Later Services with PayU
    - Merchant Hosted BNPL Merchant Integration
    - Flexible Payment Options Merchant Hosted Checkout Integration
  robots: index
next:
  description: ''
---
This section describes the general steps to integrate <Glossary>BNPL</Glossary>.

**Steps to Integrate**

<Cards columns={2}>
  <Card title="1. Check the BNPL Eligibility" href="https://docs.payu.in/docs/general-flow-bnpl-integration-with-merchant-hosted#step-1-check-the-bnpl-eligibility">
    Verify customer eligibility for Buy Now Pay Later options before proceeding with the payment

    <br />
  </Card>

  <Card title="2. Initiate the Payment" href="https://docs.payu.in/docs/general-flow-bnpl-integration-with-merchant-hosted#step-2-initiate-the-payment">
    Start the BNPL payment process using merchant hosted integration

    <br />
  </Card>

  <Card title="3. Check the Response from PayU" href="https://docs.payu.in/docs/general-flow-bnpl-integration-with-merchant-hosted#step-3-check-the-response-from-payu">
    Handle and process the response received from PayU after payment initiation
  </Card>

  <Card title="4. Verify the Payment" href="https://docs.payu.in/docs/general-flow-bnpl-integration-with-merchant-hosted#step-4-verify-the-payment">
    Confirm the payment status and ensure successful BNPL transaction completion

    <br />
  </Card>
</Cards>

<Callout icon="📮" theme="default">
  **Postman Collection**: Download the **Merchant Hosted Checkout > BNPL Postman Collection** from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/lt115hb/bnpl-integration](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/lt115hb/bnpl-integration)
</Callout>

## Step 1: Check the BNPL eligibility

When your customer makes a payment through BNPL, you can check the `customer’s` eligibility using the <Anchor label="Get Checkout Details API" target="_blank" href="ref:get_checkout_details#check-customer-eligibility">Get Checkout Details API</Anchor>  and then initiate payment.

> 🚧 Minimum amount for BNPL transaction
>
> The minimum amount for BNPL transactions shall vary for each bank, so you need to check with the banks for the minimum amount.

For request parameters and response to perform BNPL Eligibility Check, refer to <Anchor label="Get Checkout Details API" target="_blank" href="ref:get_checkout_details">Get Checkout Details API</Anchor>.

## Step 2: Initiate the payment

You need to ensure that **BNPL** for the **pg** parameter and BNPL provider code based on the desired BNPL for the **bankcode** parameter is posted. For API reference, refer to <a href="_payment_merchant_hosted_bnpl" target="_blank">Collect Payments API</a> under API Reference.

`<PaymentAPIEnvironment />`

<Accordion title="Post Request Syntax & Composition" icon="fa-database">
  ```html
  <body>
  <form action='https://test.payu.in/_payment' method='post'>
  <input type="hidden" name="key" value="J*****g" />
  <input type="hidden" name="txnid" value="t6svtqtjRdl34W" />
  <input type="hidden" name="productinfo" value="iPhone" />
  <input type="hidden" name="amount" value="1000" />
  <input type="hidden" name="email" value="test@gmail.com" />
  <input type="hidden" name="firstname" value="Ashish" />
  <input type="hidden" name="lastname" value="Kumar" />
  <input type="hidden" name="pg" value="BNPL" />
  <input type="hidden" name="bankcode" value="LAZYPAY" />
  <input type="hidden" name="surl" value="your own success url" />
  <input type="hidden" name="furl" value="your own failure url" />
  <input type="hidden" name="phone" value="9988776655" />
  <input type="hidden" name="hash" value="eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972" />
  <input type="submit" value="submit"> </form>
  </body>
  </html>
  ```
</Accordion>

<Accordion title="Request parameters" icon="fa-code">
  > 📘 Reference:
  >
  > For **Try It** experience, refer to <a href="_payment_merchant_hosted_bnpl" target="_blank">Collect Payments API - BNPL</a> under API Reference.

  | Parameter | Description | **Example** |
  | :-------- | :---------- | :---------- |
  |           |             |             |

  <Glossary>key</Glossary>
  `mandatory`

  |    | `String`Merchant key provided by PayU during onboarding. | `JPg***r` |
  | :- | :------------------------------------------------------- | :-------- |
  |    |                                                          |           |

  <Glossary>txnid</Glossary>
  `mandatory`

  |                                           | `String`The transaction ID is a reference number for a specific order that is generated by the merchant.                                                                                                                      | ypl938459435                      |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | :---------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------- | -------- | ------------- | ----------- | ------- | ------ | ------ | ------ | ------ | ------ | -- | -- | -- | -- | -- | ------- | - |
  | amount  `mandatory`                       | `String`The payment amount for the transaction.                                                                                                                                                                               | 10.00                             |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | productinfo  `mandatory`                  | `String`A brief description of the product.                                                                                                                                                                                   | iPhone                            |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | firstname  `mandatory`                    | `String` The first name of the customer.                                                                                                                                                                                      | Ashish                            |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | `email mandatory`                         | `String`The email address of the customer.                                                                                                                                                                                    | [abc@payu.in](mailto:abc@payu.in) |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | `phone mandatory`                         | `String`The phone number of the customer.                                                                                                                                                                                     |                                   |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | <Glossary>pg</Glossary> `mandatory`       | \* String It defines the payment category using the Merchant Hosted Checkout integration. For a BNPL payment, "BNPL" must be specified in the pg parameter.                                                                   | BNPL                              |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | <Glossary>bankcode</Glossary> `mandatory` | `String` The merchant must post this parameter with the corresponding payment option’s bank code value in it. For the list of bankcodes for BNPL, refer to[BNPL Codes](doc:bnpl-codes).                                       | LAZYPAY                           |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | `furl mandatory`                          | `String`The success URL, which is the page PayU will redirect to if the transaction is successful.                                                                                                                            |                                   |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | `surl mandatory`                          | `String`The Failure URL, which is the page PayU will redirect to if the transaction is failed.                                                                                                                                |                                   |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | `hash mandatory`                          | `String`It is the hash calculated by the merchant. The hash calculation logic is:&#xA;\`sha512(key\\                                                                                                                          | txnid\\                           | amount\\ | productinfo\\ | firstname\\ | email\\ | udf1\\ | udf2\\ | udf3\\ | udf4\\ | udf5\\ | \\ | \\ | \\ | \\ | \\ | SALT)\` |   |
  | `address1 optional`                       | `String` The first line of the billing address.**For Fraud Detection**: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information. |                                   |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | `address2 optional`                       | `String` The second line of the billing address.                                                                                                                                                                              |                                   |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | `city optional`                           | `String` The city where your customer resides as part of the billing address.                                                                                                                                                 |                                   |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | `state optional`                          | `String` The state where your customer resides as part of the billing address,                                                                                                                                                |                                   |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | `country optional`                        | `String` The country where your customer resides.                                                                                                                                                                             |                                   |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | `zipcode optional`                        | `String` Billing address zip code is mandatory for the cardless EMI option.&#xA;`Character Limit`-20                                                                                                                          |                                   |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | `udf1 optional`                           | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.                           |                                   |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | `udf2 optional`                           | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.                           |                                   |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | `udf3 optional`                           | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.                                                                                                               |                                   |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | `udf4 optional`                           | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.                                                                                                               |                                   |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | `udf5 optional`                           | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.                                                                                                               |                                   |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |

  Checked the response mentioned in <Anchor label="Collect Payment API - BNPL Link & Pay" target="_blank" href="ref:collect-payment-api-bnpl-link-pay">Collect Payment API - BNPL Link & Pay</Anchor>  under API Reference.

  <HashingRequestParameters />
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=J****g&txnid=5jJ9xYceXX1ydT&amount=1000.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=BNPL&bankcode=LAZYPAY&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
  ```
</Accordion>

## Step 3: Check the response from PayU

<ReverseHashing />

<Accordion title="Sample response" icon="fa-code">
  ```
  Array
  (
      [mihpayid] => 403993715523409521
      [mode] => BNPL
      [status] => success
      [unmappedstatus] => captured
      [key] => J****g
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
      [PG_TYPE] => BNPL-PG
      [bank_ref_num] => 5jJ9xRceXX1ydT
      [bankcode] => LAZYPAY
      [error] => E000
      [error_Message] => No Error
  )
  ```

  <br />
</Accordion>

## Step 4: Verify the payment

<p>Upon receiving the response, we recommend performing a reconciliation step to validate all transaction details.\
You can verify your payments using either of the following methods:</p>

<p>Upon receiving the response, we recommend performing a reconciliation step to validate all transaction details.\
You can verify your payments using either of the following methods:</p>

<Verify_Payment_Tabs />

<br />
