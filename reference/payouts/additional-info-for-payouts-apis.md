---
title: Additional Info for Payouts APIs
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
## Request parameters for Initiate Transfer API

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
        batchId```

        mandatory
        ```
      </td>

      <td>
        `String`It can be any string value. Merchants can use this value if they want to process the request in batch and also what status of transfer in batch. This can be unique for a batch or across multiple requests.  

        * \*Max char length\*\*: 40.
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        amount```

        mandatory
        ```
      </td>

      <td>
        `Double`Indicates Amount to transfer to the beneficiary account
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        merchantRefId```

        optional
        ```
      </td>

      <td>
        `String`Indicates a unique reference ID at the merchant side to distinguish between multiple transfers.  

        * \*Max char length\*\*: 40.  
        * \*Notes\*\* :  
          * Same value will be used by the merchant in the status check of transfer.  
          * In case if the merchant reference ID is not passed, an auto generated ID will be used.
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        beneficiaryAccountNumber```

        mandatory in case of IMPS, NEFT and RTGS transactions otherwise Conditional
        ```
      </td>

      <td>
        `String` Indicates beneficiary account number to transfer money.\
        **Min Character**: 9\*\*  

        * \*Max Character\*\*: 35
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        beneficiaryIfscCode ```

        mandatory in case of IMPS, NEFT and RTGS transactions otherwise Conditional
        ```
      </td>

      <td>
        `String` Indicates IFSC Code of the Beneficiary Bank Account.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        beneficiaryName\
        `mandatory`
      </td>

      <td>
        `String` Indicates name of the Beneficiary of the Beneficiary associated with Bank Account
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        beneficiaryMobile\
        `optional`
      </td>

      <td>
        `String` Indicates Beneficiary mobile number
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        beneficiaryEmail\
        `optional`
      </td>

      <td>
        `String` Indicates Beneficiary Email Address
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        purpose\
        `mandatory`
      </td>

      <td>
        `String` This parameter must include the purpose of doing this transfer.  

        * \*Note\*\*: Only alphanumeric characters are allowed.
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        paymentType\
        `mandatory`
      </td>

      <td>
        `String` Specify the any of the following mode of payment in this field:  

        * IMPS  
        * UPI  
        * NEFT  
        * RTGS  
        * MASTERCARD  
        * VISA  
        * CC\_PAYMENT
      </td>

      <td>
        MASTERCARD
      </td>
    </tr>

    <tr>
      <td>
        vpa ```

        mandatory in case of UPI transactions otherwise Conditional
        ```
      </td>

      <td>
        `String` Indicates VPA (UPI) address of Beneficiary.
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        retry\
        `mandatory`
      </td>

      <td>
        `String`Specify the flag as either True or False to indicate whether to retry transfer or not in this field:\
            \- **true**: Specifies that retry the payment.  

        * **false**: Specifies that do not retry the payment.  

        * \*Note\*\*: Default value for this will be false.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        scheduledTime\
         `optional`
      </td>

      <td>
        `Date` Specify the date and time on which Payout scheduled in this field.  

        * \*Example\*\*: 2020-10-20 15:02:11
      </td>

      <td>
        2020-10-20 15:02:11
      </td>
    </tr>

    <tr>
      <td>
        recipientCardNo\
         `optional`
      </td>

      <td>
        `String`The Credit Card Number with which the payment is made by your customer is specified in this field.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        beneficiaryId\
        `conditional`
      </td>

      <td>
        `Long` Id of beneficiary to which the payout needs to be done. This value can be passed instead of other beneficiary details.
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        vpaToken\
         `mandatory for UPI`
      </td>

      <td>
        `String` VPA token corresponding to VPA(UPI) address of beneficiary.
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        custom1\
        `optional`
      </td>

      <td>
        `String` This is custom parameter. No processing is done from payU side and can be used by you to pass any information they want in the reports for the transactions. Only 50 characters are allowed in this field.
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        custom2\
        `optional`
      </td>

      <td>
        `String` This is custom parameter. No processing is done from payU side and can be used by you to pass any information they want in the reports for the transactions. Only 50 characters are allowed in this field.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        custom3\
        `optional`
      </td>

      <td>
        `String` This is custom parameter. No processing is done from payU side and can be used by you to pass any information they want in the reports for the transactions. Only 50 characters are allowed in this field.
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

### Sample Request

#### IMPS, NEFT or RTGS Payment Request

```curl
{"callType":"Request","requestTitle":"Request Body For IMPS/NEFT/RTGS","requestType":"Get","requests":{"bash":"[\n {\n \"beneficiaryAccountNumber\": \"51234567890\",\n \"beneficiaryIfscCode\": \"HDFC0001234\",\n \"beneficiaryName\": \"Payu\",\n \"beneficiaryEmail\": \"payu@payu.in\",\n \"beneficiaryMobile\": \"9876473627\",\n \"purpose\": \"Payment from Company\",\n \"amount\": 1234.12,\n \"batchId\": \"1\",\n \"merchantRefId\": \"123asdfad3\",\n \"paymentType\": \"IMPS\",\n \"retry\" : false\n }\n]"},"isInline":true}
```

#### UPI Payment Request

```curl
{"callType":"Request","requestTitle":"Request Body For UPI Payment","requestType":"Get","requests":{"bash":"[\n {\n \"beneficiaryName\": \"Payu\",\n \"beneficiaryEmail\": \"payu@payu.in\",\n \"beneficiaryMobile\": \"9876473627\",\n \"purpose\": \"Payment from Company\",\n \"amount\": 1234.12,\n \"batchId\": \"1\",\n \"merchantRefId\": \"123\",\n \"paymentType\": \"UPI\",\n \"vpa\" : \"ankush.pokarana@ybl\"\n \"retry\" : false\n }\n]"},"isInline":true}
```

#### MasterCard Payment Request

```curl
{"callType":"Request","requestTitle":"Request Body For MasterCard payment","requestType":"Get","requests":{"bash":"[\n {\n \"beneficiaryName\": \"Payu\",\n \"beneficiaryEmail\": \"payu@payu.in\",\n \"beneficiaryMobile\": \"9876473627\",\n \"purpose\": \"Payment from Company\",\n \"amount\": 1234.12,\n \"batchId\": \"1\",\n \"merchantRefId\": \"1234\",\n \"paymentType\": \"MASTERCARD\",\n \"recipientCardNo\":\"5291170702832\"\n }\n]"},"isInline":true}
```

#### VISA Card Payment Request

```curl
{"callType":"Request","requestTitle":"Request Body For VISA card payment","requestType":"Get","requests":{"bash":"[\n {\n \"beneficiaryName\": \"Payu\",\n \"beneficiaryEmail\": \"payu@payu.in\",\n \"beneficiaryMobile\": \"9876473627\",\n \"purpose\": \"Payment from Company\",\n \"amount\": 1234.12,\n \"batchId\": \"1\",\n \"merchantRefId\": \"1234\",\n \"paymentType\": \"VISA\",\n \"recipientCardNo\":\"4012888888881882\"\n }\n]"},"isInline":true}
```

### Sample Response

* Success response

```plaintext
{"callType":"Response","responseTitle":"Sample Success Response","response":"{\n \"status\": 0,\n \"msg\": \"Requests are in process. Will send response of individual request on webhooks set by you\",\n \"code\": null,\n \"data\": []\n }","isInline":true}
```

* Failure response

````plaintext
{"callType":"Response","responseTitle":"Sample Failure Response","response":"{\n \"status\": 1,\n \"msg\": null,\n \"code\": null,\n \"data\": [\n {\n \"batchId\": \"1\",\n \"merchantRefId\": \"111\",\n \"error\": \"beneficiary account number can not be empty. \",\n \"code\": [1004]\n }\n ]\n }","isInline":true}
```plaintext

 
````

## Request Parameters in Check Transfer Status API

### Transfer Status

<table><tbody><tr><td>QUEUED/SHEDULED</td><td>It will be first state once we get transaction request from merchant.</td></tr><tr><td>IN_PROGRESS</td><td>This is an intermediary stage and can also come if merchant is not having enough balance in his virtual account.</td></tr><tr><td>PENDING</td><td>PayU has received pending status from bank.</td></tr><tr><td>FAILED</td><td>Final status will be updated once PayU get success or failure from bank.</td></tr></tbody></table>

The Status of a particular Transaction has to be determined Only from the field **txnStatus** in `transactionDetails` JSON against the `merchantRefId`.

On receiving the following JSON Response in the **Check Transfer Status** API, the transaction status is not determined and has to considered as unidentified or Pending by merchant.

```
{
    "status": 0,
    "msg": null,
    "code": null,
    "data": {
        "payoutMerchantId": null,
        "noOfPages": 0,
        "totalElements": 0,
        "currentPage": 0,
        "totalAmount": 0.0,
        "succesTxn": 0,
        "pendingTxn": 0,
        "transactionDetails": []
    }
}
```

## Headers and request parameters

> 📘 Note
