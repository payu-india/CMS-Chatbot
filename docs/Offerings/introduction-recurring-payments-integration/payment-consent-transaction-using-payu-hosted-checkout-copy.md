---
title: Payment Consent Transaction using Zion
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
This section describes the how set up a Payment Consent transaction using PayU Hosted Checkout integration.

> 🚧 Test Environment Limitation
>
> You cannot perform the payment consent transaction with the PayU Test environment.

#### Steps to Integrate:

1. [Make the Transaction Request to PayU](#step-1-make-the-transaction-request-to-payu)
2. [Customer Submits Payment Details on the PayU pageC](#step-2-customer-submits-payment-details-on-the-payu-page)
3. [Check the Response from PayU](#step-3-check-the-response-from-payu)
4. [Capture Successful Registration Response](#step-4-capture-the-registration-response)

## Step 1: Make the transaction request to PayU

In the merchant-initiated POST REQUEST, Hash is a mandatory parameter. It is critical to calculate the hash correctly and post it to PayU in the request.

### Request parameters

In the merchant-initiated POST REQUEST, Hash is a mandatory parameter. It is critical to calculate the hash correctly and post it to PayU in the request.

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
        si\
        **mandatory**
      </td>

      <td>
        This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.  

        * \*Notes\*\*: You can modify or cancel existing recurring payment registration as described in the following sections:  
        * .   [Manage Recurring Payment for Cards](ref:manage-recurring-payment-for-cards)  
        * .   [Manage UPI Recurring Transaction](ref:api-commands-to-manage-upi-recurring-transaction)
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        free\_trial\
        **optional**
      </td>

      <td>
        This is mandatory only if the merchant wants to support free trial use case with card and net banking together that too on PayU Hosted Checkout integration.  

        In this case, PayU adjusts the transaction amount as INR 2.00 for cards. INR 0.00 for Net Banking and UPI registration irrespective of what amount is passed against the amount field in the request.\
        This parameter has no significance in the case of seamless flow.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        si\_details\
        **mandatory**
      </td>

      <td>
        This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.  

        * \*Note\*\*: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers ( for more details refer – [https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0) )  

        This is a JSON object and it includes a set of fields. For more information,  refer to [SI Parameter JSON Details](ref:si-parameter-json-details)
      </td>

      <td>
        Refer the example below the si\_details Parameter Description table.
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
        HASH = SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si\_details|SALT)
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

### Sample request

```curl
curl -X POST "https://test.payu.in/_payment"-H "Content-Type: application/x-www-form-urlencoded" -d"key=JP***g&txnid=fM3O2HnkpJ8XEC&amount=100.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&si=1&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&si_details={“billingAmount”: “100.00”,”billingCurrency”: “INR”,”billingCycle”: “MONTHLY”,”billingInterval”: 1,”paymentStartDate”: “2022-09-01″,”paymentEndDate”: “2022-12-01”}&hash=2ad878f64de47c7c1149ff554cd00ee44555a8512a1d2cff9690d6ea3c9d9de0bc44b0e77c61dd60a3c64ef970612a9b71761559aa202d2a278d29dc87b998c5"
```

Characters allowed for parameters

For parameters address1, address2, city, state, country, product info, email, and phone following characters are allowed:

* Characters: A to Z, a to z, 0 to 9
* – (Minus)
* \_ (Underscore)
* @ ()
* / (Slash)
* (Space)
* . (Dot)

### Parameters required in Seamless flow

In the Seamless flow (Merchant Hosted or S2S integration), the following mandatory parameters are required in the payment request to perform a Consent transaction apart from the above standard parameters, where you accept the card/bank/ UPI details before sending a request to PayU.

<Table>
  <thead>
    <tr>
      <th>
        **Parameters**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        pg
        **mandatory**
      </td>

      <td>
        `varchar` The **pg** parameter for each payment mode are:  

        * **Credit Card**: The value is CC in the case of Credit Cards.  
        * **Debit Cards**: The value is DC in the case of selected Debit cards that support SI.  
        * \*Note\*\*: All Debit Cards does not support SI. Hence, while passing this value, the merchant needs to confirm what issuers are supporting Debit Card SI with PayU’s team and pass only applicable Debit Cards for SI by using BIN APIs. For more information on BIN API, Refer to Get Card BIN Information.  
        * Net Banking: The value needs to be passed as ENACH.  
        * UPI: Pass the values as UPI
      </td>

      <td>
        ENACH
      </td>
    </tr>

    <tr>
      <td>
        bankcode\
        **mandatory**
      </td>

      <td>
        `varchar` This parameter contains any of the following code indicating the payment option used for the transaction:
      </td>

      <td>
        KKBKENCC
      </td>
    </tr>

    <tr>
      <td>
        ccnum\
        **mandatory for cards**
      </td>

      <td>
        `integer` This parameter must contain the card (credit/debit) number entered by the customer for the transaction.
      </td>

      <td>
        51\*3456\*89012\*46
      </td>
    </tr>

    <tr>
      <td>
        ccname\
        **mandatory for cards**
      </td>

      <td>
        `varchar` This parameter must contain the name on the card – as entered by the customer for the transaction.
      </td>

      <td>
        Ashish
      </td>
    </tr>

    <tr>
      <td>
        ccvv\
        **mandatory for cards**
      </td>

      <td>
        `integer` This parameter must contain the CVV number of the card – as entered by the customer for the transaction.
      </td>

      <td>
        123
      </td>
    </tr>

    <tr>
      <td>
        ccexpmon\
        **mandatory for cards**
      </td>

      <td>
        `integer` This parameter must contain the card’s expiry month – as entered by the customer for the transaction.\
        For months 1-9, this parameter must be appended with 0 – like 01, 02…09.\
        For months 10-12, this parameter must not be appended – It should be 10, 11 and 12 respectively.
      </td>

      <td>
        12
      </td>
    </tr>

    <tr>
      <td>
        ccexpyr\
        **mandatory for cards**
      </td>

      <td>
        `integer` This parameter must contain the card’s expiry year – as entered by the customer for the transaction. It must be of 4 digits.
      </td>

      <td>
        2024
      </td>
    </tr>

    <tr>
      <td>
        beneficiarydetail\
        **mandatory for Net Banking**
      </td>

      <td>
        `varchar` This object represents bank account details of the customer which involves account number, name on the account and account type and needs to be passed if the recurring transaction needs to be set up against Net Banking. It includes the following:  

        * **BeneficiaryName**: Registered name against customer’s account  
        * **BeneficiaryAccountNumber**: Account number against which recurring transactions need to be executed  
        * **BeneficiaryAccountType**: SAVINGS or CURRENT  
        * **beneficiaryIfscCode**: 11-digit IFSC code of the customer bank  
        * **verificationMode** DEBIT\_CARD – authentication will be done through a debit card. If no value or value other than DEBIT\_CARD, then it will trigger net banking login password flow.
      </td>

      <td>
        \{“beneficiaryName”: “Sachin Tendulkar”,”beneficiaryAccountNumber”: “1\*114\*00\*1”,”beneficiaryAccountType”: “SAVINGS”, “beneficiaryIfscCode“:”ICIC0000046”, “verificationMode”:”DEBIT\_CARD”}
      </td>
    </tr>

    <tr>
      <td>
        vpa\
        **mandatory for UPI Collect**
      </td>

      <td>
        varchar This parameter contains the customer’s VPA handle. For the list UPI handles supported, refer to UPI Handles.  

        The merchant is advised to check the validity of the VPA through using the VPA Validation API. PayU extends support for the same if required. For more information on using VPA Validation API, refer to Validate UPI Handle API.
      </td>

      <td>
        abc\@upi
      </td>
    </tr>

    <tr>
      <td>
        txn\_s2s\_flow\
        **mandatory for UPI Intent**
      </td>

      <td>
        integer\
        This parameter must be passed with the values as 4 for UPI Intent.
      </td>

      <td>
        4
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Notes
>
> For **bankcode**:
>
> * Debit Card or Credit Card: There are different options like Visa Debit Card, Mastercard, Maestro, etc. For each option, a unique bank code exists and it would be returned in this bankcode parameter. For more information, refer to Card Type Codes. For example, VISA for VISA Debit Card.
> * Net Banking recurring, this value will represent bank codes. For more information, refer to Recurring Payment Bank Codes. For example: KKBKENCC.
>   * UPI: The value can be any of the following:
>   * UPI: Pass this value for UPI transactions.
>   * INTENT: Pass this value for Intent.

For more information on bank codes used for recurring payments registration, refer to [Bank Codes - Recurring Payments](doc:bank-codes-recurring-payments).

### Sample Request for Net Banking

```curl
curl -X POST "https://test.payu.in/_payment
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
"key=JP***g&txnid=oRWSUMU4XSQBZn&amount=0.0&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&si=1&pg=ENACH&bankcode=ICICENCC&surl=https://apiplayground-response.herokuapp.com/&furl=&api_version=7&beneficiarydetail={“beneficiaryName”: “Ashish Kumar”,”beneficiaryAccountNumber”: “1211450021”,”beneficiaryAccountType”: “SAVINGS”, “beneficiaryIfscCode“:”ICIC0000046”, “verificationMode”:”DEBIT_CARD”} Kumar&hash=dbe874c46dcd68ae8c6dd14d04e213f4dff1f2f89106653f61df3e8cee900df33d976e737a82291dfbea3d54d3c67c403d7371c387a1e9652e27ec682d3dce21"
```

### Sample Request for Cards

```curl
curl -X POST "https://test.payu.in/_payment-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d”key=Q*****U&txnid=56bb2e3fcb510f1c1521&amount=10000&firstname=Payu-Admin&email=test@example.com&phone=1234567890&productinfo=iPhone&api_version=7&si=1&pg=CC&bankcode=UTIBENCC&surl=https://test.payu.in/admin/test_response
/&furl=https://test.payu.in/admin/test_response
&ccnum=5123456789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=Test User&si_details={“billingAmount”: “100.00”,”billingCurrency”: “INR”,”billingCycle”: “MONTHLY”,”billingInterval”: 1,”paymentStartDate”: “2022-09-01″,”paymentEndDate”: “2022-12-01”}
&hash=e36568b2dfc460eab0eb3387fb7d90543ed861154f273b9593d6fcc152ed93a91e529c2f4be0965eeb57104e82d58889fa5efb52811ec78cbd1ad646e39c29a0”
```

## Step 2: Customer submits payment details on the PayU page

With the **POST REQUEST**, the customer will be redirected to the PayU’s payment page. The customer now selects the payment option on PayU’s page (credit card, debit card, Net Banking, Sodexo, etc.) and clicks the **Pay Now** button. PayU redirects the customer to the chosen payment method. The customer goes through the necessary authorization/authentication process at the bank’s login page, and the bank gives the success/failure response back to PayU.

PayU marks the transaction status based on the response received from the Bank. PayU provides the final transaction response string to the merchant through a **POST RESPONSE**. The parameters in this response are covered in the subsequent sections.

***

## Step 3: Check the response from PayU

You will receive the final status of the transaction. You will receive the **hash** parameter here also. It is crucial to verify this hash value at your end to accept or reject the invoice order. This is performed to avoid any tampering attempt by the user.

On receiving valid request parameters over **\_payment** API, the customer is redirected to the Card Authentication page, Bank Login page, or UPI waiting page as per the payment method chosen by the customer.

After the registration transaction is completed, the response of that transaction is communicated to you over surl or furl depending upon the transaction’s status as success or failure.

### Response parameters

The description of response parameters for the successful registration:

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        mihpayid
      </td>

      <td>
        It is a unique reference number created for each transaction at PayU’s end which is used to identify a transaction in case of a refund.
      </td>
    </tr>

    <tr>
      <td>
        mode
      </td>

      <td>
        This parameter describes the payment category by which the transaction was completed/attempted by the customer. The values are:  \
        &#x9;•	Credit Card – CC \
        &#x9;•	Debit Card – DC \
        &#x9;•	Net Banking – NB\
        &#x9;•	Cash Card – CASH\
        &#x9;•	EMI – EMI \
        &#x9;•	Cardless EMI – CLEMI\
        &#x9;•	Buy Now Pay Later - BNPL
      </td>
    </tr>

    <tr>
      <td>
        bankcode
      </td>

      <td>
        This parameter contains the code indicating the payment option used for the transaction. For example, Visa Debit Card – VISA, Master Debit Card – MAST.
      </td>
    </tr>

    <tr>
      <td>
        status
      </td>

      <td>
        This parameter returns the status of the transaction and must be used to map the order status. Possible values are success, failure, or pending. The significance of the values for these values are:  \
        &#x9;•	**Success**: If the value of status parameter is ’success’, the transaction is successful. \
        &#x9;•	**Failed**: If the value of status parameter is ‘failure’ or ‘pending’, must only be treated as a failed transaction.
      </td>
    </tr>

    <tr>
      <td>
        unmappedstatus
      </td>

      <td>
        This parameter holds the status of a transaction in PayU's internal database, which can include intermediate states. Possible values include: dropped, bounced, captured, auth, failed, usercancelled, or pending. For information on status description, refer to  [Status Explanations](https://devguide.payu.in/api/miscellaneous/status-explanations/)
      </td>
    </tr>

    <tr>
      <td>
        key
      </td>

      <td>
        This parameter contains the merchant key.
      </td>
    </tr>

    <tr>
      <td>
        error
      </td>

      <td>
        For the failed transactions, this parameter provides the reason for failure.
      </td>
    </tr>

    <tr>
      <td>
        error\_message
      </td>

      <td>
        This parameter contains the error message. For the list of error message, refer to [Error Codes](https://devguide.payu.in/api/miscellaneous/error-codes/).
      </td>
    </tr>

    <tr>
      <td>
        bank\_ref\_num
      </td>

      <td>
        For each successful transaction – this parameter contains the bank reference number generated by the bank.
      </td>
    </tr>

    <tr>
      <td>
        txnid
      </td>

      <td>
        This parameter contains the transaction ID value posted by the merchant during the transaction request.
      </td>
    </tr>

    <tr>
      <td>
        amount
      </td>

      <td>
        This parameter contains the original amount which was sent in the transaction request by the merchant.
      </td>
    </tr>

    <tr>
      <td>
        productinfo
      </td>

      <td>
        This parameter contains the same value of product information which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        firstname
      </td>

      <td>
        This parameter contains the same value of first name which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        lastname
      </td>

      <td>
        This parameter contains the same value of last name which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        email
      </td>

      <td>
        This parameter contains the same value of email which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        phone
      </td>

      <td>
        This parameter contains the same value of phone which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        hash
      </td>

      <td>
        This parameter is crucial and is similar to the hash parameter used in the transaction request. For more information, refer to [Encryption of Request](https://devguide.payu.in/merchant-integration/webhooks//).
      </td>
    </tr>

    <tr>
      <td>
        PG\_TYPE
      </td>

      <td>
        This parameter gives information on the payment gateway used for the transaction.
      </td>
    </tr>

    <tr>
      <td>
        udf1
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf2
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf3
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5 which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf4
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf5
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>
  </tbody>
</Table>

### Sample response

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

## Step 4: Capture the registration response

### Webhook for getting transaction details

You can expose a webhook by requesting the PayU Integration team to configure the same against the ws\_online\_response parameter. If this webhook is configured, you will receive the above response object over HTTP form post method similar to the following:

```plaintext
unmappedstatus=success&phone=9999999999&txnid=FCDA1R100870163781&hash=84e335094bbcb2ddaa0f9a488eb338e143b273765d89c9dfa502402562d0b6f3c7935e28194ca92f380be7c84c3695415b106dcf52cb016a15fcf6adc98d724&status=success&curl=https://www.abc.in/payment/handlepayuresposne&firstname=NA&card_no=519619XXXXXX5049&furl=https://www.abc.in/payment/handlepayuresposne&productinfo=2&mode=DC&amount=800.00&field4=6807112311042810&field3=6807112311042810&field2=838264&field9=SUCCESS&email=NA&mihpayid=175477248&surl=https://www.ABC.in/payment/handlepayuresposne&card_hash=9e88cb0573d4a826b61d808c0a870ed4a990682459b0ec9e95ea421e8e47be8c&field1=42812&payment_source=sist
```

If the mandate is not confirmed by the customer or the mandate is confirmed by the customer, but the mandate registration is rejected from the banks, the status is communicated as a “failure” over webhook. For more information, refer to [Webhooks](doc:webhooks).

## Query the status of transaction

Verify the transaction details using the **Verification Payment** API. For more information, For API reference, refer to <a href="verify_payment_api" target="_blank">Verify Payment API</a>.

> 📘 Note:
>
> The transaction ID that you posted in Step 1 with PayU must be used here.
