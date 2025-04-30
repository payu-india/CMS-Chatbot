---
title: QR
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Collect payments using QR codes with Merchant Hosted Checkout integration as described in this section. After collecting the details from the customer, make the transaction request with the payment details to PayU.

> 📘 QR does not work in Test environment
>
> QR does not work in PayU Test environment, so the **Try It** experience is not enabled.

### Environment



## Request parameters

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>
      <th>
        Description
      </th>
      <th>
        Example
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <Glossary>key</Glossary> `mandatory`
      </td>
      <td>
        `String` This parameter is the unique merchant key provided by PayU for your merchant account. For more information, refer to [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard).
      </td>
      <td>
        8488225
      </td>
    </tr>
    <tr>
      <td>
        txnid `mandatory`
      </td>
      <td>
        `varchar` This parameter is known as Transaction ID (or OrderID). It is the order reference number generated at your (Merchant's) end. It is an identifier which you(merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of same Transaction ID again would fail. Hence, it is essential that you post us a unique transaction ID for every new transaction (Please make sure that the transaction ID being sent to us hasn't been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID').
      </td>
      <td>
        fd3e847h2
      </td>
    </tr>
    <tr>
      <td>
        amount `mandatory`
      </td>
      <td>
        `float` This parameter should contain the payment amount of the particular transaction. Note: Type-cast the amount to float type
      </td>
      <td>
        10
      </td>
    </tr>
    <tr>
      <td>
        productinfo `mandatory`
      </td>
      <td>
        `varchar` This parameter should contain a brief product description. It should be a string describing the product (The description type is entirely your choice). 
      </td>
      <td>
        T-shirt
      </td>
    </tr>
    <tr>
      <td>
        firstname `mandatory`
      </td>
      <td>
        `varchar` This parameter must contain the first name of the customer.
      </td>
      <td>
        Ankit
      </td>
    </tr>
    <tr>
      <td>
        email `mandatory`
      </td>
      <td>
        `varchar` This parameter must contain the email of the customer)
      </td>
      <td>
        [test@gmail.com](mailto:test@gmail.com)
      </td>
    </tr>
    <tr>
      <td>
        phone `mandatory`
      </td>
      <td>
        `integer` Merchant needs to take the customer's GPay registered phone number and pass in this field. This field will be used for further mapping the customer VPA and initiate a collect request.
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td>
        <Glossary>pg</Glossary> `mandatory`
      </td>
      <td>
        `string` The payment gateway is specified in this parameter. For QR,  specifiy **QR**.
      </td>
      <td>
        QR
      </td>
    </tr>
    <tr>
      <td>
        <Glossary>bankcode</Glossary> `mandatory`
      </td>
      <td>
        `string` Each payment option is identified with a unique bank code at PayU. You must use any of the following bank code for QR:  

        * **UPIQR** for accepting payments with UPI QR.
        * **BQR** for accepting payments with Bharath QR
      </td>
      <td>
        UPIQR
      </td>
    </tr>
    <tr>
      <td>
        surl `mandatory`
      </td>
      <td>
         The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.
      </td>
      <td>
        [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)
      </td>
    </tr>
    <tr>
      <td>
        furl `mandatory`
      </td>
      <td>
        The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.
      </td>
      <td>
        [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)
      </td>
    </tr>
    <tr>
      <td>
        <Glossary>hash</Glossary> `mandatory`
      </td>
      <td>
        `string` The hash calculated by the merchant using the key and salt provided by PayU. The format for calculating the hash: 
        
        `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|||||SALT)`
        
        For more information, refer to [Generate Hash](doc:hashing-request-and-response).
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td>
        lastname `optional`
      </td>
      <td>
        `string` The last name of the customer.
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td>
        address1 `optional`
      </td>
      <td>
        `string` The first line of the billing address.
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td>
        address2 `optional`
      </td>
      <td>
        `string` The second line of the billing address.
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td>
        city `optional`
      </td>
      <td>
        `string` The city where your customer resides as part of the billing address.
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td>
        state `optional`
      </td>
      <td>
        `string` The state where your customer resides as part of the billing address,
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td>
        country `optional`
      </td>
      <td>
        `string` The country where your customer resides.
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td>
        zipcode `optional`
      </td>
      <td>
        `string` Billing address zip code is mandatory for the cardless EMI option.
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td>
        udf1
      </td>
      <td>
        `string` This parameter has been made for you to keep any information corresponding to the transaction.
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td>
        udf2 `optional`
      </td>
      <td>
        `string` This parameter has been made for you to keep any information corresponding to the transaction.
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td>
        udf3
      </td>
      <td>
        `string` This parameter has been made for you to keep any information corresponding to the transaction.
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td>
        udf4 `optional`
      </td>
      <td>
        `string` This parameter has been made for you to keep any information corresponding to the transaction.
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td>
        udf5
      </td>
      <td>
        `string` This parameter has been made for you to keep any information corresponding to the transaction.
      </td>
      <td>
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```curl
curl -X \
 POST "https://test.payu.in/_payment" -H \
 "accept: application/json" -H \
 "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=ewP8oRopzdHEtC&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=QR&bankcode=UPIQR&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
```

## Response parameters

> 📘 Reference
>
> For the response parameters description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis#response-parameters).

## Sample response (parsed)

```php
(
    [mihpayid] => 403993715524045752
    [mode] => QR
    [status] => success
    [unmappedstatus] => captured
    [key] => JPM7Fg
    [txnid] => ewP8oRopzdHEtC
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2021-09-06 13:27:08
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
    [hash] => 1be7e6e97ab1ea9034b9a107e7cf9718308aa9637b4dbbd1a3343c91b0da02b34a40d00ac7267ebe81c20ea1129b931371c555d565bc6e11f470c3d2cf69b5a3
    [field1] =>
    [field2] =>
    [field3] =>
    [field4] =>
    [field5] =>
    [field6] =>
    [field7] =>
    [field8] =>
    [field9] => Transaction Completed Successfully
    [payment_source] => payu
    [PG_TYPE] => QR-PG
    [bank_ref_num] => 87d3b2a1-5a60-4169-8692-649f61923b3d
    [bankcode] => UPIQR
    [error] => E000
    [error_Message] => No Error
)
```
