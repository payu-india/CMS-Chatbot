---
title: Merchant Hosted Checkout Integration - Supercoins Pay
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
You can collect payments from customers by redeeming their Flipkart Supercoins (FKSC) using the Merchant Hosted Checkout integration.

When your customer makes a payment by redeeming their SuperCoins, you can check the SuperCoins balance using the **Supercoins Balance** API and then initiate payment. You need to ensure that **LR** for the **pg** parameter and **FKSC** for the **bankcode** parameter is posted as mentioned in [Additional Info for Payment APIs](ref:addl_info-payment-apis)

## Step 1: Check the SuperCoins Balance

Use the following APIs to check the SuperCoins balance:

* [Send OTP API](ref:send-otp-api-fksc) (one-time)
* [Verify Token API](ref:verify-token-api-fksc) (one-time)
* [Get SuperCoins Balance API](ref:get-supercoins-balance-api)

> 📘 Notes:
>
> * The **Send OTP** and **Verify OTP** APIs for Flipkart Supercoins will be used only for the first time when the customer logs in using the mobile number associated with  Flipkart. After the OTP validation is successful, PayU responds to the merchant with a token. The merchant must save this token and must be used in repeat flows when the same customer uses Flipkart Supercoins for payments.
> * Merchant has to create screens to accept their customer’s mobile number to send the OTP using the **Send OTP** API and authenticate the OTP using the **Verify OTP** API.

## Step 2: Initiate the Payment

### Post Request Syntax & Composition

```html
<body>
<form action='https://test.payu.in/_payment' method='post'>
<input type="hidden" name="key" value="JP***g" />
<input type="hidden" name="txnid" value="t6svtqtjRdl34W" />
<input type="hidden" name="productinfo" value="iPhone" />
<input type="hidden" name="amount" value="1000" />
<input type="hidden" name="email" value="test@gmail.com" />
<input type="hidden" name="firstname" value="Ashish" />
<input type="hidden" name="lastname" value="Kumar" />
<input type="hidden" name="pg" value="LR" />
<input type="hidden" name="bankcode" value="FKSC" />
<input type="hidden" name="surl" value="your own success url" />
<input type="hidden" name="furl" value="your own failure url" />
<input type="hidden" name="phone" value="9988776655” />
<input type="hidden" name="hash" value="eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972" />
<input type="submit" value="submit"> </form>
</body>
</html>
```

> 📘 Note:
>
> The above HTML code block is for Merchant Checkout integration on the SuperCoins call for the test environment.

### Request Parameters for Transaction Request

Along with the mandatory parameters mentioned in [Collect Payments with Merchant Hosted Checkout](https://devguide.payu.in/merchant-integration/merchant-hosted-checkout/merchant-hosted-integration#Step2), you must post the following parameters for the Flipkart Supercoins:

<Table align={["left","left","left"]}>
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
        key
        **mandatory**
      </td>

      <td>
        `varchar` This parameter is the unique Merchant Key provided by PayU for your merchant account.
      </td>

      <td>
        Your Test Key
      </td>
    </tr>

    <tr>
      <td>
        txnid\
        **mandatory**
      </td>

      <td>
        `varchar` This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant’s) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction.\
        `Character limit`: 25  

        * \*Note\*\*: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of ‘duplicate Order ID.’
      </td>

      <td>
        fd3e847h2
      </td>
    </tr>

    <tr>
      <td>
        amount\
        **mandatory**
      </td>

      <td>
        `float` This parameter should contain the payment amount of the particular transaction.  

        * \*Note\*\*: Type-cast the amount to float type\
          Depending upon the merchant use case, this value will vary.\
            
        * It can be either 0 INR (for Net Banking) or min 1 INR (for Cards & UPI) in penny transaction use case.  
        * In the case of first instalment use cases, this amount can be equal to initiate setup amount, but this use case will be supported only against selected Net Banking (ICICI and HDFC), all Credit / Debit Cards, and UPI
      </td>

      <td>
        1000
      </td>
    </tr>

    <tr>
      <td>
        productinfo\
        **mandatory**
      </td>

      <td>
        `varchar` This parameter should contain a brief product description. It should be a string describing the product.\
        `Character limit`: 100
      </td>

      <td>
        Time Magazine Subscription
      </td>
    </tr>

    <tr>
      <td>
        firstname\
        **mandatory**
      </td>

      <td>
        `varchar` Must contain the first name of the customer.\
        `Character limit`: 60
      </td>

      <td>
        Ashish
      </td>
    </tr>

    <tr>
      <td>
        email\
        **mandatory**
      </td>

      <td>
        `varchar` Must contain the email of the customer.\
        This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information.\
        Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.\
        Character limit: 50
      </td>

      <td>
        [Ashish@test.com](mailto:Ashish@test.com)
      </td>
    </tr>

    <tr>
      <td>
        phone\
        **mandatory**
      </td>

      <td>
        `varchar` Must contain the phone number of the customer.  

        This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.\
        Character limit: 50
      </td>

      <td>
        9843176540
      </td>
    </tr>

    <tr>
      <td>
        surl\
        **mandatory**
      </td>

      <td>
        surL is the acronym for Success URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is successful.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        furl\
        **mandatory**
      </td>

      <td>
        furl is the acronym for for Failure URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is failed.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        api\_version\
        **mandatory**
      </td>

      <td>
        This parameter must always needs to be passed as 7.
      </td>

      <td>
        7
      </td>
    </tr>

    <tr>
      <td>
        hash\
        **mandatory**
      </td>

      <td>
        Hash is a crucial parameter used to ensure that any date is not tampered while redirecting customer from the merchant website to PayU’s payment interface while registration transactions.  

        It is SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si\_details by merchant salt.  

        In the case of registration transaction, the formula is used to calculate this hash is similar to the following:\
        `HASH = SHA512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\||\||\||si_details\|SALT)`
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        pg\
        **mandatory**
      </td>

      <td>
        `String` The pg parameter must contain the payment category using the Merchant Hosted Checkout integration. For a FKSC redemption, "LR" must be specified in the pg parameter.  

        * EFTNET (NEFT/RTGS): **NEFTRTGS**
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        bankcode\
        **mandatory**
      </td>

      <td>
        `String` Pass the bankcode as **FKSC** for Flipkart Supercoins redemption.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        ud1\
        **optional for seamless flow**
      </td>

      <td>
        User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.\
        `Character Limit-255`
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        ud2\
        **optional for seamless flow**
      </td>

      <td>
        User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.\
        `Character Limit-255`
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        ud3\
        **optional for seamless flow**
      </td>

      <td>
        User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.\
        `Character Limit-255`
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        ud4\
        **optional for seamless flow**
      </td>

      <td>
        User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.\
        `Character Limit-255`
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        ud15\
        **optional for seamless flow**
      </td>

      <td>
        User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.\
        `Character Limit-255`
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

### Sample Request

```curl
curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=xdB9G7qYpfqszo&amount=10&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=LR&bankcode=FKSC&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb"
```

***

## Step 3: Check Response from PayU

The following is the sample response from PayU for Merchant Hosted Checkout. For the description of the response parameters, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

```plaintext
Array
(
    [mihpayid] => 40XXXXXXXX9XX1
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
    [phone] => 98XXXX210
    [udf1] => 
    [udf2] => 
    [udf3] => 
    [udf4] => 
    [udf5] => 
```
