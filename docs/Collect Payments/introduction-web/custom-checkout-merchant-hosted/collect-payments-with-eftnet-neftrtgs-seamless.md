---
title: EFTNET (NEFT/RTGS) Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Collect Payments with EFTNET (NEFT/RTGS) - Merchant Hosted Checkout
  description: >-
    Learn how to efficiently collect payments through EFTNET (NEFT/RTGS)
    transactions using PayU's Merchant Hosted Checkout integration. This guide
    outlines the process of initiating payments and verifying payment status for
    secure and seamless transactions.
  robots: index
next:
  description: ''
---
Collect payments using EFTNET (NEFT/RTGS) with Merchant Hosted Checkout integration as described in this section. After collecting the details from the customer, make the transaction request with the payment details to PayU.

To integrate with EFTNET:

### Steps to Integrate

<RegisterMerchantPrerequiste />

<Accordion title="Step 1: Initiate the payment with PayU" icon="fa-code">


### Post request syntax & composition

```html
<body>
<form action='https://test.payu.in/_payment' method='post'>
<input type="hidden" name="key" value="JP***g" />
<input type="hidden" name="txnid" value="t6svtqtjRdl34W" />
<input type="hidden" name="productinfo" value="iPhone" />
<input type="hidden" name="amount" value="10" />
<input type="hidden" name="email" value="test@gmail.com" />
<input type="hidden" name="firstname" value="Ashish" />
<input type="hidden" name="lastname" value="Kumar" />
<input type="hidden" name="pg" value="NEFTRTGS" />
<input type="hidden" name="bankcode" value="EFTAXIS" />
<input type="hidden" name="surl" value="your own success url" />
<input type="hidden" name="furl" value="your own failure url" />
<input type="hidden" name="phone" value="9988776655" />
<input type="hidden" name="hash" value="eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972" />
<input type="submit" value="submit"> </form>
</body>

</html>
```

<Callout icon="📘" theme="info">
  **Note**: The sample HTML code mentioned above is for Merchant Checkout integration with the NEFT/RTGS payment method call for the test environment.
</Callout>

### Optional configuration

PayU provides an optional **Back to Merchant** button on the payment challan of a NEFT/RTGS payment. This button enables your customer to go back to the merchant portal once the transaction is done.

In this scenario, if a customer clicks on **Back to Merchant** button the merchant will receive the response on the furl shared in the [Collect Payment API - Merchant Hosted Checkout](ref:_payment_merchant_hosted).

_Sample challan of a NEFT/RTGS transaction_

<img
  src="https://files.readme.io/4f959a8-neftrtgs_challan.jpeg"
  alt=""
  style={{
    display: "block",
    margin: "0 auto",
    width: "400px"
  }}
/>

### Post parameters

The following parameters vary for the EFTNEFT payment mode in the **Collect Payment**API (**_payment** API).

**Environment**

|                            |                                                                         |
| :------------------------- | :---------------------------------------------------------------------- |
| **Test Environment**       | https://test.payu.in/_payment                                           |
| **Production Environment** | https://secure.payu.in/_payment                                         |

### Request parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>key `mandatory`</td>
      <td>String - This parameter is the unique merchant key provided by PayU for your merchant account. For more information, refer to Generate Merchant Key and Salt.</td>
      <td>8488225</td>
    </tr>
    <tr>
      <td>txnid `mandatory`</td>
      <td>varchar - This parameter is known as Transaction ID (or OrderID). It is the order reference number generated at your (Merchant's) end. It is an identifier which you(merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of same Transaction ID again would fail. Hence, it is essential that you post us a unique transaction ID for every new transaction.</td>
      <td>fd3e847h2</td>
    </tr>
    <tr>
      <td>amount `mandatory`</td>
      <td>float - This parameter should contain the payment amount of the particular transaction. Note: Type-cast the amount to float type</td>
      <td>10</td>
    </tr>
    <tr>
      <td>productinfo `mandatory`</td>
      <td>varchar - This parameter should contain a brief product description. It should be a string describing the product (The description type is entirely your choice).</td>
      <td>T-shirt</td>
    </tr>
    <tr>
      <td>firstname `mandatory`</td>
      <td>varchar - This parameter must contain the first name of the customer.</td>
      <td>Ankit</td>
    </tr>
    <tr>
      <td>email `mandatory`</td>
      <td>varchar - This parameter must contain the email of the customer</td>
      <td>test@gmail.com</td>
    </tr>
    <tr>
      <td>phone `mandatory`</td>
      <td>integer - Merchant needs to take the customer's GPay registered phone number and pass in this field. This field will be used for further mapping the customer VPA and initiate a collect request.</td>
      <td>9876543210</td>
    </tr>
    <tr>
      <td>pg `mandatory`</td>
      <td>string - The payment gateway is specified in this parameter. For EFTNET, specify NEFTRTGS.</td>
      <td>NEFTRTGS</td>
    </tr>
    <tr>
      <td>bankcode `mandatory`</td>
      <td>string - Each payment option is identified with a unique bank code at PayU.</td>
      <td>EFTAXIS</td>
    </tr>
    <tr>
      <td>surl `mandatory`</td>
      <td>The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.</td>
      <td>https://apiplayground-response.herokuapp.com/</td>
    </tr>
    <tr>
      <td>furl `mandatory`</td>
      <td>The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.</td>
      <td>https://apiplayground-response.herokuapp.com/</td>
    </tr>
    <tr>
      <td>hash `mandatory`</td>
      <td>string - The hash calculated by the merchant using the key and salt provided by PayU. The format for calculating the hash: sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|||||SALT) For more information, refer to Generate Hash.</td>
      <td>calculated_hash_value</td>
    </tr>
    <tr>
      <td>lastname `optional`</td>
      <td>string - The last name of the customer.</td>
      <td>Kumar</td>
    </tr>
    <tr>
      <td>address1 `optional`</td>
      <td>string - The first line of the billing address.</td>
      <td>123 Main St</td>
    </tr>
    <tr>
      <td>address2 `optional`</td>
      <td>string - The second line of the billing address.</td>
      <td>Apt 4B</td>
    </tr>
    <tr>
      <td>city `optional`</td>
      <td>string - The city where your customer resides as part of the billing address.</td>
      <td>Mumbai</td>
    </tr>
    <tr>
      <td>state `optional`</td>
      <td>string - The state where your customer resides as part of the billing address.</td>
      <td>Maharashtra</td>
    </tr>
    <tr>
      <td>country `optional`</td>
      <td>string - The country where your customer resides.</td>
      <td>India</td>
    </tr>
    <tr>
      <td>zipcode `optional`</td>
      <td>string - Billing address zip code is mandatory for the cardless EMI option.</td>
      <td>400001</td>
    </tr>
    <tr>
      <td>udf1 `optional`</td>
      <td>string - This parameter has been made for you to keep any information corresponding to the transaction.</td>
      <td>custom_data_1</td>
    </tr>
    <tr>
      <td>udf2 `optional`</td>
      <td>string - This parameter has been made for you to keep any information corresponding to the transaction.</td>
      <td>custom_data_2</td>
    </tr>
    <tr>
      <td>udf3 `optional`</td>
      <td>string - This parameter has been made for you to keep any information corresponding to the transaction.</td>
      <td>custom_data_3</td>
    </tr>
    <tr>
      <td>udf4 `optional`</td>
      <td>string - This parameter has been made for you to keep any information corresponding to the transaction.</td>
      <td>custom_data_4</td>
    </tr>
    <tr>
      <td>udf5 `optional`</td>
      <td>string - This parameter has been made for you to keep any information corresponding to the transaction.</td>
      <td>custom_data_5</td>
    </tr>
  </tbody>
</Table>

<HashingRequestParameters />

### Sample request

```curl
curl -X POST "https://test.payu.in/_payment"  -H "accept: application/json"  -H "Content-Type: application/x-www-form-urlencoded"  -d "key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=NEFTRTGS&bankcode=EFTAXIS&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
```


</Accordion>

<Accordion title="Step 2: Check response from PayU" icon="fa-code">


<ReverseHashing />

<Callout icon="📘" theme="info">
  **Note on Response**: For security reasons, the sample response or URL is not included here.
</Callout>


</Accordion>

<Accordion title="Step 3: Verify the payment" icon="fa-code">


<Verify_Payment_Tabs />

</Accordion>
