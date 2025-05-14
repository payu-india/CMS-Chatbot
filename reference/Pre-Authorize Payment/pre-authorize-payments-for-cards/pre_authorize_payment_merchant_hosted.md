---
title: Merchant Hosted with Pre-Authorize Payment
excerpt: ''
api:
  file: payment-api-10.json
  operationId: MerchantHostedPre-AuthorizePayment
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **pre\_authorize** parameter is used to pre-authorize payments using the Merchant Hosted Checkout integration along with the parameters to collect card details.

<PaymentAPIEnvironment />

<details>
  <summary>Sample request</summary>

  ```curl
  curl --request POST \
       --url 'https://test.payu.in/_payment?form=2' \
       --header 'Content-Type: application/x-www-form-urlencoded' \
       --header 'accept: text/plain' \
       --data key=JPM7Fg \
       --data pg=CC \
       --data bankcode=CC \
       --data pre_authorize=1 \
       --data surl=https://test-payment-middleware.payu.in/simulatorResponse \
       --data furl=https://test-payment-middleware.payu.in/simulatorResponse \
       --data txnid=ypskjfdaaksdjfh \
       --data amount=10000 \
       --data productinfo=iPhone \
       --data firstname=Ashish \
       --data email=ashish@gmail.com \
       --data phone=9889XXXXXX \
       --data ccnum=512*******012346 \
       --data ccname=Ashish \
       --data ccexpmon=11 \
       --data ccexpyr=2025 \
       --data ccvv=123 \
       --data hash=d99f230c19d781016fa64c57f976d0ec8ff3761fe5d9d6448933cf46d7177db6fb7b370e551e39dd37f2045a2a761f9065f8462838bbaad22963c083c84f9ced
  ```
</details>

<details>
  <summary>Sample request</summary>

  The formatted sample response body is similar to the following, and you need to look for the following parameters:

  * PG\_TYPE: CC PG
  * bankcode: CC
  * **unamappedstatus: auth**

  ```
    {
    "mihpayid": "403993715531065775",
    "mode": "CC",
    "status": "success",
    "unmappedstatus": "captured",
    "key": "JPM7Fg",
    "txnid": "ypskjfdaaksdjfh",
    "amount": "10000.00",
    "cardCategory": "domestic",
    "discount": "0.00",
    "net_amount_debit": "10000",
    "addedon": "2024-02-26 07:20:56",
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
    "phone": "9889843845",
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
    "hash": "00f188fdda2d60d418b147e7dce3a6ead172cf760a95a4df09b763f7627c01d867127e022de97841f1fe41cecb420b12b482fd8b68aaf66476b840bdfe82ca3c",
    "field1": "261005309469848160",
    "field2": "724760",
    "field3": "10000.00",
    "field4": "",
    "field5": "00",
    "field6": "02",
    "field7": "AUTHPOSITIVE",
    "field8": "AUTHORIZED",
    "field9": "Transaction is Successful",
    "payment_source": "payu",
    "PG_TYPE": "CC-PG",
    "bank_ref_num": "261005309469848160",
    "bankcode": "CC",
    "error": "E000",
    "error_Message": "No Error",
    "cardnum": "XXXXXXXXXXXX2346",
    "cardhash": "This field is no longer supported in postback params.",
    "splitInfo": "{\"splitStatus\":\"splitNotReceived\",\"splitSegments\":[]}"
  }
  ```
</details>

## Request parameters

<details>
  <summary>Reference for request parameters</summary>

  ## Reference info for request parameters

  <Table align={["left","left"]}>
    <thead>
      <tr>
        <th>
          Parameter
        </th>

        <th>
          Reference
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          <Glossary>key</Glossary>
        </td>

        <td>
          For more information on how to generate the Key and Salt, refer to any of the following:

          * **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)

          * **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
        </td>
      </tr>

      <tr>
        <td>
          <Glossary>hash</Glossary>
        </td>

        <td>
          Hash logic for this API is:\
          sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
        </td>
      </tr>
    </tbody>
  </Table>

  > 📘 Reference:
  >
  > * Use the card details as follows: cccnum=5123456789012346, ccexpmon=11, ccexpyr=2025, ccvv=123 and OTP =123456 (displayed in Simulator page).
  > * For the list of error codes, refer to [Error Codes - Pre-Authorize Payment](ref:error-codes-pre-authorize-payment).
  > * If you want to cancel or refund a pre-authorized transaction, refer to [Cancel a Pre-Authorized Payment](doc:cancel-a-pre-authorized-payment).
  >   ### Sample request
  >   ```curl
  >   curl --request POST \
  >        --url 'https://test.payu.in/_payment?form=2' \
  >        --header 'Content-Type: application/x-www-form-urlencoded' \
  >        --header 'accept: text/plain' \
  >        --data key=JPM7Fg \
  >        --data pg=CC \
  >        --data bankcode=CC \
  >        --data pre_authorize=1 \
  >        --data surl=https://test-payment-middleware.payu.in/simulatorResponse \
  >        --data furl=https://test-payment-middleware.payu.in/simulatorResponse \
  >        --data txnid=ypskjfdaaksdjfh \
  >        --data amount=10000 \
  >        --data productinfo=iPhone \
  >        --data firstname=Ashish \
  >        --data email=ashish@gmail.com \
  >        --data phone=9889XXXXXX \
  >        --data ccnum=512*******012346 \
  >        --data ccname=Ashish \
  >        --data ccexpmon=11 \
  >        --data ccexpyr=2025 \
  >        --data ccvv=123 \
  >        --data hash=d99f230c19d781016fa64c57f976d0ec8ff3761fe5d9d6448933cf46d7177db6fb7b370e551e39dd37f2045a2a761f9065f8462838bbaad22963c083c84f9ced
  >   ```
  >   ### Check the PayU response
  >   The formatted sample response body is similar to the following, and you need to look for the following parameters:
  >   * PG\_TYPE: CC PG
  >   * bankcode: CC
  >   * **unamappedstatus: auth**
  >   ```
  >     {
  >     "mihpayid": "403993715531065775",
  >     "mode": "CC",
  >     "status": "success",
  >     "unmappedstatus": "captured",
  >     "key": "JPM7Fg",
  >     "txnid": "ypskjfdaaksdjfh",
  >     "amount": "10000.00",
  >     "cardCategory": "domestic",
  >     "discount": "0.00",
  >     "net_amount_debit": "10000",
  >     "addedon": "2024-02-26 07:20:56",
  >     "productinfo": "iPhone",
  >     "firstname": "Ashish",
  >     "lastname": "",
  >     "address1": "",
  >     "address2": "",
  >     "city": "",
  >     "state": "",
  >     "country": "",
  >     "zipcode": "",
  >     "email": "ashish@gmail.com",
  >     "phone": "9889843845",
  >     "udf1": "",
  >     "udf2": "",
  >     "udf3": "",
  >     "udf4": "",
  >     "udf5": "",
  >     "udf6": "",
  >     "udf7": "",
  >     "udf8": "",
  >     "udf9": "",
  >     "udf10": "",
  >     "hash": "00f188fdda2d60d418b147e7dce3a6ead172cf760a95a4df09b763f7627c01d867127e022de97841f1fe41cecb420b12b482fd8b68aaf66476b840bdfe82ca3c",
  >     "field1": "261005309469848160",
  >     "field2": "724760",
  >     "field3": "10000.00",
  >     "field4": "",
  >     "field5": "00",
  >     "field6": "02",
  >     "field7": "AUTHPOSITIVE",
  >     "field8": "AUTHORIZED",
  >     "field9": "Transaction is Successful",
  >     "payment_source": "payu",
  >     "PG_TYPE": "CC-PG",
  >     "bank_ref_num": "261005309469848160",
  >     "bankcode": "CC",
  >     "error": "E000",
  >     "error_Message": "No Error",
  >     "cardnum": "XXXXXXXXXXXX2346",
  >     "cardhash": "This field is no longer supported in postback params.",
  >     "splitInfo": "{\"splitStatus\":\"splitNotReceived\",\"splitSegments\":[]}"
  >   }
  >   ```
  >   <br />
</details>