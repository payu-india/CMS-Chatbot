---
excerpt: ''
api:
  file: payment-api-9.json
  operationId: PayUHostedCheckoutwithPre-AuthorizePayment
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **pre\_authorize** parameter is used to pre-authorize payments using the PayU Hosted Checkout integration.

<PayU_Labs />

<br />

## Postman Collection

<Postman_collection />

<Accordion title="Sample request" icon="fa-info-circle">

  ```curl
  curl -X POST "https://test.payu.in/_payment
  -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
  "key=JP***g&txnid=PQI6MqpYrjEefU&amount=10.00
  &firstname=PayU User&email=test@gmail.com&phone=9876543210
  &productinfo=iPhone&pre_authorize=1&pg=cc&bankcode=CC&surl=
  https://apiplayground-response.herokuapp.com/
  &furl=https://apiplayground-response.herokuapp.com/
  &pre_authorize=1&hash=05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072"
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-info-circle">
  By default, the response in HTML format. The formatted sample response body is similar to the following, and you need to look for the following parameters:

  * PG\_TYPE: CC PG
  * bankcode: CC
  * **unamappedstatus: auth**

  ```
  mihpayid: 403993715523615328
  mode: CC
  status: success
  unmappedstatus: auth
  key: JPM7Fg
  txnid: 50QJq6lBJBmx14
  amount: 10.00
  cardCategory: domestic
  discount: 0.00
  net_amount_debit: 10
  addedon: 2021-07-28 15:11:37
  productinfo: iPhone
  firstname: PayU User
  lastname: 
  address1: 
  address2: 
  city: 
  state: 
  country: 
  zipcode: 
  email: test@gmail.com
  phone: 9876543210
  udf1: 
  udf2: 
  udf3: 
  udf4: 
  udf5: 
  udf6: 
  udf7: 
  udf8: 
  udf9: 
  udf10: 
  hash: afeab9dcf4e43d47f8fbf5a6838d393c70694a58e30ada08e6cb86ac943236c05717c5f5e4872d671fe81d0d9b2d9facd44e9a061ba621aff6f20c4343ea5dfa
  field1: 
  field2: 
  field3: 
  field4: 
  field5: 
  field6: 
  field7: 
  field8: 
  field9: Transaction Completed Successfully
  payment_source: payu
  PG_TYPE: CC-PG
  bank_ref_num: 7f0d5ada-59bb-41d7-9e41-20a6af2406c9
  bankcode: CC
  error: E000
  error_Message: No Error
  name_on_card: test
  cardnum: 411111XXXXXX1111
  cardhash: This field is no longer supported in postback params.
  ```
</Accordion>

## Request parameters

<Accordion title="Reference information for request parameters" icon="fa-info-circle">

  <Table align={["left","left"]}>
    <thead>
      <tr>
        <th style={{ textAlign: "left" }}>
          Parameter
        </th>

        <th style={{ textAlign: "left" }}>
          Reference
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td style={{ textAlign: "left" }}>
          <Glossary>key</Glossary>
        </td>

        <td style={{ textAlign: "left" }}>
          For more information on how to generate the Key and Salt, refer to any of the following:

          * **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)

          * **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          <Glossary>hash</Glossary>
        </td>

        <td style={{ textAlign: "left" }}>
          Hash logic for this API is:\
          sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
        </td>
      </tr>
    </tbody>
  </Table>

  > 📘 Reference:
  >
  > * Use the card details as follows: ccnum=5123456789012346, ccexpmon=11, ccexpyr=2025, ccvv=123 and OTP =123456 (displayed in Simulator page).
  > * For the list of error codes, refer to [Error Codes - Pre-Authorize Payment](ref:error-codes-pre-authorize-payment).
  > * If you want to cancel or refund a pre-authorized transaction, refer to [Cancel a Pre-Authorized Payment](doc:cancel-a-pre-authorized-payment).
</Accordion>

<br />
