---
title: Cards with Transaction Biller Name
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
The **txnBillerName** parameter is used to include the transaction biller name for the card transactions. You need to ensure that **CC** or **DC** for the **<Glossary>pg</Glossary>** parameter and  card code based on the desired card provider for the **<Glossary>bankcode</Glossary>** parameter is posted.

<PaymentAPIEnvironment/>

## Request parameters


### additional\_info JSON object field descriptions

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field
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
        txnBillerName
        `optional`
      </td>

      <td>
        This field must be passed with the sub merchant or transaction biller name.
      </td>

      <td>
         Airtel Recharge Payment
      </td>
    </tr>
  </tbody>
</Table>

> ❗️ Error Handling
>
> If any error message is displayed with an error code, refer to the <a href="error-codes" target="_blank">Error Codes</a> section to understand the reason for these error codes.

## Sample request

```curl
curl --location 'https://secure.payu.in/_payment' \ 
--header 'Content-Type: application/x-www-form-urlencoded' \ 
--data-urlencode 'key=JP***g' \ 
--data-urlencode 'firstname=Ashsih' \ 
--data-urlencode 'email=test@example.com' \ 
--data-urlencode 'amount=1' \ 
--data-urlencode 'phone=7988XX5823' \ 
--data-urlencode 'productinfo=Product_info' \ 
--data-urlencode 'surl=https://admin.payu.in/test_response' \ 
--data-urlencode 'furl=https://admin.payu.in/test_response' \ 
--data-urlencode 'pg=CC' \ 
--data-urlencode 'bankcode=CC' \ 
--data-urlencode 'ccnum=XXXXXXXXXXXX9500' \ 
--data-urlencode 'ccname=Test User' \ 
--data-urlencode 'ccvv=XXX' \ 
--data-urlencode 'ccexpmon=XX' \ 
--data-urlencode 'ccexpyr=XXXX' \ 
--data-urlencode 'txnid=' \ 
--data-urlencode 'hash=091dae1bfe27bbad238fcecc88718dd68c92de25098c4ef5f72a17645f37a3a9e55df2e9a31e9c75ecfd145d3157cbd874937b0fe84e4f65233b2fb3cfb9684e' \ 
--data-urlencode 'txn_s2s_flow=1' \ 
--data-urlencode 'additional_info={"txnBillerName":"Airtel Recharge Payment"}'  
```

## Sample response

```
mihpayid=403993715531077182&mode=CC&status=success&unmappedstatus=captured&key=JPM7Fg&txnid=ypl938459435dfdfdf&amount=1000.00&cardCategory=domestic&discount=0.00&net_amount_debit=1000&addedon=2024-02-27+15%3A11%3A37&productinfo=iPhone&firstname=Ashish+User&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=ashish%40gmail.com&phone=9876543210&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=afeab9dcf4e43d47f8fbf5a6838d393c70694a58e30ada08e6cb86ac943236c05717c5f5e4872d671fe81d0d9b2d9facd44e9a061ba621aff6f20c4343ea5dfa&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=CC-PG&bank_ref_num=7f0d5ada-59bb-41d7-9e41-20a6af2406c9&bankcode=CC&error=E000&error_Message=No+Error&name_on_card=test&cardnum=411111XXXXXX1111&cardhash=This+field+is+no+longer+supported+in+postback+params.
```

### Parsed response

```
  {
  "mihpayid": "403993715531077182",
  "mode": "CC",
  "status": "success",
  "unmappedstatus": "captured",
  "key": "JPM7Fg",
  "txnid": "ypl938459435dfdfdf",
  "amount": "1000.00",
  "cardCategory": "domestic",
  "discount": "0.00",
  "net_amount_debit": "1000",
  "addedon": "2024-02-27 15:00:42",
  "productinfo": "iPhone",
  "firstname": "Ashish",
  "lastname": "",
  "address1": "",
  "address2": "",
  "city": "",
  "state": "",
  "country": "",
  "zipcode": "",
  "email": "ashish@gmail.com",
  "phone": "9876543210",
  "udf1": "",
  "udf2": "",
  "udf3": "",
  "udf4": "",
  "udf5": "",
  "udf6": "",
  "udf7": "",
  "udf8": "",
  "udf9": "",
  "udf10": "",
  "hash": "84bbbf0fa3ba2a39942f6c3deab234c4d00bc5b6aceee5cda3c8200d6e1714e19c224d47e24d0c4a9a0cce40eddbae1dc46455c69e5e7d5dd62f6636bfab337c",
  "field1": "896193988312194700",
  "field2": "857712",
  "field3": "1000.00",
  "field4": "",
  "field5": "00",
  "field6": "02",
  "field7": "AUTHPOSITIVE",
  "field8": "AUTHORIZED",
  "field9": "Transaction is Successful",
  "payment_source": "payu",
  "PG_TYPE": "CC-PG",
  "bank_ref_num": "896193988312194700",
  "bankcode": "CC",
  "error": "E000",
  "error_Message": "No Error",
  "cardnum": "XXXXXXXXXXXX2346",
  "cardhash": "This field is no longer supported in postback params.",
  "splitInfo": "{\"splitStatus\":\"splitNotReceived\",\"splitSegments\":[]}"
}
```

## Response parameters

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
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
        This parameter holds the status of a transaction in PayU's internal database, which can include intermediate states. Possible values include: dropped, bounced, captured, auth, failed, usercancelled, or pending. For information on status description, refer to  [Payment State Explanations](ref:payment-state-explanations).
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
        This parameter contains the error message. For the list of error message, refer to [Error Codes](ref:error-codes).
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
        cardCategory
      </td>

      <td>
        This parameter contains the card category to indicate whether it is domestic or international.
      </td>
    </tr>

    <tr>
      <td>
        discount
      </td>

      <td>
        This parameter contains the discount amount by the merchant.
      </td>
    </tr>

    <tr>
      <td>
        net\_amount\_debit
      </td>

      <td>
        This parameter contains the net amount debited.
      </td>
    </tr>

    <tr>
      <td>
        addedon
      </td>

      <td>
        The transaction date and time of the transaction.
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
        This parameter is crucial and is similar to the hash parameter used in the transaction request. For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted).
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

    <tr>
      <td>
        udf6
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf7
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.\*\*\*\*
      </td>
    </tr>

    <tr>
      <td>
        udf8
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf9
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        success\_at
      </td>

      <td>
        This parameter contains the date and timestamp when the transaction was successful.
      </td>
    </tr>

    <tr>
      <td>
        cardnum
      </td>

      <td>
        The parameter contains the card number masked and only last 4 digits are returned.
      </td>
    </tr>

    <tr>
      <td>
        issuing\_bank
      </td>

      <td>
        The parameters contains the card issuing bank.
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Notes:
>
> To identify a particular transaction is routed to which aggregator you have to check the udf parameters of the response. The following aggregators are showing udf parameters if the transaction are routed them: 
>
> * PayU
> * RazorPay  
> * BillDesk
> * Pinelabs  
> * Paytm