---
title: UPI Intent with S2S Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
The following steps allow you to integrate the server-to-server UPI (United Payments Interface) intent:

<Cards columns={3}>
  <Card title="1. Initiate payment" href="https://docs.payu.in/docs/upi-intent-server-to-server#step-1-initiate-payment">
    Initiate the UPI Intent payment request with required parameters
  </Card>

  <Card title="2. Invoke UPI Intent on customer's device" href="https://docs.payu.in/docs/upi-intent-server-to-server#step-2-invoke-upi-intent-on-customers-device">
    Trigger the UPI Intent on the customer's mobile device to complete payment
  </Card>

  <Card title="3. Check UPI transaction status" href="https://docs.payu.in/docs/upi-intent-server-to-server#step-3-check-upi-transaction-status">
    Monitor and verify the UPI transaction status after intent invocation
  </Card>

  <Card title="4. PayU sends Server-to-Server callback response" href="https://docs.payu.in/docs/upi-intent-server-to-server#step-4-payu-sends-server-to-server-callback-response">
    Receive and process the server-to-server callback response from PayU
  </Card>

  <Card title="5. Verify the payment" href="https://docs.payu.in/docs/upi-intent-server-to-server#step-5-verify-the-payment">
    Verify the payment status and ensure successful transaction completion
  </Card>

  <Card title="6. Update Invoice ID (Conditional)" href="#step-6-update-invoice-id-conditional">
    Update the invoice ID associated with the transaction

    <br />
  </Card>

  <Card title="7. Upload the Invoices / Shipping Document (Conditional)" href="#step-7-upload-the-invoices-optional">
    Upload invoice documents related to the completed transaction
  </Card>

  <br />
</Cards>

<RegisterMerchantPrerequiste />

<Callout icon="❗️" theme="error">
  **Important UPI Integration Changes as per NPCI Mandate on UPI Collect Disablement**:

  * **For Android Apps**: Merchants must implement the Smart Intent implementation. Refer to [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow) for non-SDK implementation, or use [PayU Android SDKs](doc:explore-android-sdks) which have Smart Intent built-in.

  * **For iOS Apps**: Merchants can implement the specific deeplink handling and continue using the UPI flow as is. Refer to [iOS UPI SDK](doc:ios-upi-sdk) for SDK-based implementation.

  * **For Web**: Use the deeplink returned in the API response to generate a QR code that customers can scan with their UPI app.

  For easier integration with built-in Smart Intent support, use PayU SDKs:

  * [Android Mobile SDKs](doc:explore-android-sdks)
  * [iOS Mobile SDKs](doc:explore-ios-sdks)
</Callout>

<Accordion title="Intent Flow Diagram" icon="fa-code">
  The following diagram depicts the UPI intent flow from server to server:

  ![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/07/UPI-Intent-Process-Flow-1024x511.png)
</Accordion>

***

## Step 1: Initiate payment

### Environment

<PaymentAPIEnvironment />

The **_payment** API needs to be called with all the required parameters. For the complete list of parameters, refer to  <Anchor label="UPI Intent - Non SDK Flow" target="_blank" href="doc:upi-smart-intent-non-sdk-flow">UPI Intent - Non SDK Flow</Anchor>.

This needs to be a server-to-server cURL request. This API is used for both Cards and UPI for generating a new transaction.

If specific intent has to be opened instead of Generic Intent, then the **bankcode** values will change accordingly:

* For Generic Intent, **bankcode** = INTENT

> 📘 Notes:
>
> * If you are using this for their application, then the Generic Intent, and Specific Intent, can be invoked.
> * If you are using this for your Mobile Web, then only Generic Intent can be invoked. To invoke App specific intents on the mobile web, the libraries have to be added separately. PayU offers the same for GPay Intent through the Mobile web. Refer to the GPay Seamless Integration Document for the same.
> * User VPA is not required for this flow.

<Accordion title="Request parameters" icon="fa-database">
  For the complete list of parameters, refer to <a href="https://docs.payu.in/reference/_payment_s2s_upi_collection" target="_blank"> UPI Collection - S2S</a>.

  <Table align={["left","left","left"]}>
    <thead>
      <tr>
        <th style={{ textAlign: "left" }}>
          Parameter
        </th>

        <th style={{ textAlign: "left" }}>
          Description
        </th>

        <th style={{ textAlign: "left" }}>
          Example
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td style={{ textAlign: "left" }}>
          key
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` The merchant key provided by PayU must be included.

          * *Reference*\*: For more information on how to generate the Key and Salt, refer to any of the following:
          * **Production**: [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
          * **Test**: [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          txnid
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` (alphanumeric) Merchant transaction identifier - This parameter must be unique (after a successful transaction) & alphanumeric special (\<= 50 characters & excluding >,\<, =,:,&, ').
        </td>

        <td style={{ textAlign: "left" }}>
          1234\_abcdedf
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          amount
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` (rounded to two decimal places) This parameter must contain the amount for which QR needs to be generated. The amount should be greater than or equal to Rs.1.00.
        </td>

        <td style={{ textAlign: "left" }}>
          1000
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          phone
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter must contain the customer phone number (10 characters).
        </td>

        <td style={{ textAlign: "left" }}>
          9876786756
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          productinfo
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` (alphanumeric) Name or brief description of the goods/services being sold. In case of physical goods, please include name / description of all products. (max. 100 characters).
        </td>

        <td style={{ textAlign: "left" }}>
          iPhone 12
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          firstname
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter must contain the customer's first name (max. 60 characters).
        </td>

        <td style={{ textAlign: "left" }}>
          Sundar
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          email
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter must contain the customer email ID.
        </td>

        <td style={{ textAlign: "left" }}>
          [hello@payu.in](mailto:hello@payu.in)
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          lastname
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter must contain the customer last name (maximum 20 characters).
        </td>

        <td style={{ textAlign: "left" }}>
          Teja
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          <p>pg<br /><code>mandatory</code></p>
        </td>

        <td style={{ textAlign: "left" }}>
          <p><strong>String</strong> The payment method is specified in this field. For UPI INTENT, specify the parameter value as <strong>UPI</strong>.</p>
        </td>

        <td style={{ textAlign: "left" }}>
          <p>UPI</p>
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          <p>bankcode<br /><code>mandatory</code></p>
        </td>

        <td style={{ textAlign: "left" }}>
          <p><strong>String</strong> Each payment option is identified with a unique bank code at PayU. For UPI Intent, specify the value as <strong>INTENT</strong>.</p>
        </td>

        <td style={{ textAlign: "left" }}>
          <p>INTENT</p>
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          <p>surl<br /><code>mandatory</code></p>
        </td>

        <td style={{ textAlign: "left" }}>
          <p><strong>String</strong> Success URL(surl) – It must contain the URL on which PayU will redirect the final response if the transaction is successful.</p>
        </td>

        <td style={{ textAlign: "left" }}>
          <p><a href="https://apiplayground-response.herokuapp.com/">[https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)</a></p>
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          <p>furl<br /><code>mandatory</code></p>
        </td>

        <td style={{ textAlign: "left" }}>
          <p><code>String</code> Failure URL (furl) – It must contain the URL on which PayU will redirect the final response in case of failure.</p>
        </td>

        <td style={{ textAlign: "left" }}>
          <p><a href="https://apiplayground-response.herokuapp.com/">[https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)</a></p>
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          address1
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter must contain the first line of customer address (up to 100 characters).
        </td>

        <td style={{ textAlign: "left" }}>
          PayU, Bestech Business Tower, Gurgaon
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          address2
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter must contain the second line of the customer address (up to 100 characters).
        </td>

        <td style={{ textAlign: "left" }}>
          Sohna Road
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          city
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter must contain the customer city (max. 50 characters).
        </td>

        <td style={{ textAlign: "left" }}>
          Gurgaon
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          country
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter must contain the customer's country that is part of the address (max. 50 characters).
        </td>

        <td style={{ textAlign: "left" }}>
          India
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          state
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          String This parameter must contain the customer state that is part of the address (max 50 characters).
        </td>

        <td style={{ textAlign: "left" }}>
          Haryana
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          zipcode
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `Numeric` This parameter must contain the customer's PIN code (6 digits).
        </td>

        <td style={{ textAlign: "left" }}>
          122018
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          udf1
          `conditional` 
        </td>

        <td style={{ textAlign: "left" }}>
          `String` >User-defined field 1. For PACB: Buyer's PAN number.
        </td>

        <td style={{ textAlign: "left" }}>
          `AELPR****E` 
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          udf2
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter can include any custom information in request (up to 255 characters.).
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          udf3
          `optional but recommended for higher approval rate`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` Date of Birth (DOB) of buyer in DD-MM-YYYY.
          (up to 255 characters.)
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          udf4
          `mandatory for payment aggregators`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` End merchant legal entity name. For UPI, this field should not be passed.
          (up to 255 characters.)
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          udf5
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` Contains invoice ID for the transaction. Invoice ID / number should be the ID present on the invoice issued to the customer.
          (up to 255 characters.)
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          txn\_s2s\_flow
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `Numeric` This parameter must be passed with the value as 4
        </td>

        <td style={{ textAlign: "left" }}>
          4
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          s2s\_client\_ip
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `varchar` This parameter must have the source IP of the user's device.

          * *Note*\*: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          s2s\_device\_info
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `varchar` This parameter must have the user agent of device.

          * *Note*\*: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          upiAppName
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          For Specific Intent, merchant should share the app name which is selected by customer on the merchant check-out page. The following are the enum's expected for major apps:

          * phonepe
          * googlepay
          * paytm
          * bhim
          * cred
          * amazonpay
          * whatsapp
          * genericintent – For any other app apart from
            above
        </td>

        <td style={{ textAlign: "left" }}>
          phonepe
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          hash
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` Hash is a crucial parameter – used specifically to avoid any tampering during the transaction. For more information, refer to

          [Generate Hash](doc:hashing-request-and-response)
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>
    </tbody>
  </Table>

  <Accordion title="Hashing Logic" icon="fa-lock">
    <PACB_Hashing />

    ```
    key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|salt|additional_charges|buyer_type_business
    ```

    * **Case4 example**: if the merchant wants to pass the api\_version = 7 and buyer\_type\_business, udf\_params in the payment request.

    ```
    key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|si_details|salt|udf_params|buyer_type_business
    ```

    For more information, refer to  <a href="generate-hash-merchant-hosted" target="_blank"> Generate Hash</a>.
  </Accordion>

  <Accordion title="Sample Request" icon="fa-code">
    ```curl
    curl --location --request POST 'https://test.payu.in/_payment' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'key=JPM7Fg' \
    --data-urlencode 'txnid=payuTestTransaction12345' \
    --data-urlencode 'amount=100.00' \
    --data-urlencode 'firstname=Ashish' \
    --data-urlencode 'email=test@payu.in' \
    --data-urlencode 'phone=9988776655' \
    --data-urlencode 'productinfo=Product Info' \
    --data-urlencode 'surl=https://test.payu.in/admin/test_response' \
    --data-urlencode 'furl=https://test.payu.in/admin/test_response' \
    --data-urlencode 'pg=UPI' \
    --data-urlencode 'bankcode=INTENT' \
    --data-urlencode 'txn_s2s_flow=4' \
    --data-urlencode 's2s_client_ip=10.200.12.12' \
    --data-urlencode 's2s_device_info=Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0' \
    --data-urlencode 'udf1=AELPR1234E' \
    --data-urlencode 'udf3=02-02-1980' \
    --data-urlencode 'udf4=XYZ Pvt. Ltd.' \
    --data-urlencode 'udf5=INV123456' \
    --data-urlencode 'buyer_type_business=1' \
    --data-urlencode 'udf_params={"udf7":"0100000029","udf8":"99953729071"}' \
    --data-urlencode 'hash=YOUR_CALCULATED_HASH'
    ```
  </Accordion>
</Accordion>

<Accordion title="Response for S2S request" icon="fa-code">
  Collect the response in the  [UPI Collection - S2S](ref:_payment_s2s_upi_collection). under API Reference. The response for the S2S payment request is not similar to Merchant Hosted or PayU Hosted Checkout. For description of response parameters, refer to [Additional Info for Payment APIs.](ref:addl_info-payment-apis#response-for-initial-server-to-server-request)

  <Accordion title="Using the IntentURIData value in response" icon="fa-code">
    The **IntentURIData** parameter returns the URI in the response. For example, it contains the first debit amount .

    > 📘 Notes:
    >
    > * Every time there is a change, you need to incorporate the changes to avoid breaking the transactions.
    > * The **tid** value which is passed in the intent URI acts as a validation check at NPCI's end which do not allow duplicate transaction.
    > * The tr value not necessary and it is a payU\_id. It can be any reference id for PayU's internal reconciliation.
  </Accordion>
</Accordion>

## Step 2: Invoke UPI Intent on customer's device

<Accordion title="Request parameters" icon="fa-monitor">
  You need to invoke intent in the customer's mobile device using the merchant VPA URL. Make sure that only this merchant VPA is embedded in the intent call since this helps to track the status of the transaction.

  Open the UPI Intent as per the NPCI Guidelines. Merchants can also open any specific app instead of making the Generic Intent call. For example, Google Pay, PhonePe, etc. This URL can then be fired using an Intent or a hyperlink which would open an Intent tray with a list of available supporting apps on the user's mobile device. The following sample UPI Deep Link URL and the format used for creating the URL:

  **Sample URL** (with values from the above sample JSON):

  ```plaintext
  upi://pay?pa=payu@axisbank&pn=SMSPLUS&tr=8312916361&am=10.17
  ```

  **Format for UPI Deep Linking URL** (as per NPCI guidelines):

  ```plaintext
  "upi://pay?pa=" + merchantVpa + "&pn=" + merchantName + "&tr=" + referenceId + "&am=" + amount 
  ```

  Where the description of the parameters used in the URL is as described in the following table:

  | **Parameter** | **Description**                                                                                   |
  | ------------- | ------------------------------------------------------------------------------------------------- |
  | merchantVpa   | As received in JSON response in key merchantVPA'                                                  |
  | merchantName  | As received in JSON response in key merchantName.                                                 |
  | referenceId   | As received in JSON response in key referenceId.                                                  |
  | amount        | Amount of transaction. This must be the same as the amount passed to the **initiatePayment** API. |

  <Accordion title="Sample request" icon="fa-info-circle">
    ```curl
    curl --location 'https://test.payu.in/_payment' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'key=PRiQvJ' \
    --data-urlencode 'txnid=my_order_991' \
    --data-urlencode 'amount=1' \
    --data-urlencode 'productinfo=my_order_991' \
    --data-urlencode 'email=' \
    --data-urlencode 'phone=9368252248' \
    --data-urlencode 'txn_s2s_flow=4' \
    --data-urlencode 'hash=||||||ABCDE1234F||1990-01-01||INV123456||||||' \
    --data-urlencode 'surl=https://test.payu.in/admin/test_response' \
    --data-urlencode 'furl=https://test.payu.in/admin/test_response' \
    --data-urlencode 'udf1=buyer'\''s DOB' \
    --data-urlencode 'udf2=' \
    --data-urlencode 'udf3=buyer'\''s PAN' \
    --data-urlencode 'udf4=' \
    --data-urlencode 'udf5=invoice number' \
    --data-urlencode 's2s_client_ip=10.200.12.12' \
    --data-urlencode 's2s_device_info=Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0' \
    --data-urlencode 'firstname=' \
    --data-urlencode 'lastname=kr' \
    --data-urlencode 'address1=308,third floor' \
    --data-urlencode 'address2=testing' \
    --data-urlencode 'city=Gurugram' \
    --data-urlencode 'state=UP' \
    --data-urlencode 'country=India' \
    --data-urlencode 'zipcode=122018' \
    --data-urlencode 'pg=UPI' \
    --data-urlencode 'bankcode=INTENT' \
    --data-urlencode 'upiAppName=gpay/phonepe/paytm/qr/amazonpay' \
    --data-urlencode 'udf_params={"udf7":"asdf","udf8":"12"}' \
    --data-urlencode 'buyer_type_business=1'
    ```
  </Accordion>

  <Accordion title="Sample respose" icon="fa-info-circle">
    If metaData.unmappedStatus = pending, then get the result.intentURIData and add the prefix upi://pay?to make it to create a fully qualified deeplink to trigger the UPI App.

    ```json
    {
      "metaData": {
          "message": null,
          "referenceId": "c99a6455b3e0dc5cd7167ab8c8cc10d2fa153cb509e3f64c6cd0ed9c5b64a8c9",
          "statusCode": null,
          "txnId": "my_order_26075",
          "txnStatus": "pending",
          "unmappedStatus": "pending"
      },
      "result": {
          "paymentId": "403993715535965242",
          "merchantName": "Sudhanshu",
          "merchantVpa": "payutest@hdfcbank",
          "amount": "1.00",
          "intentURIData": "pa=payutest@hdfcbank&pn=Kumar&tr=403993715535965242&tid=PPPL403993715535965242080126220900&am=1.00&cu=INR&tn=UPIIntent",
          "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vdGVzdC5wYXl1LmluL2M5OWE2NDU1YjNlMGRjNWNkNzE2N2FiOGM4Y2MxMGQyYzgzYTk5NmFhNDhiYTk4MmZjMGQ4MTI1MGY1ODgxZjMvaW50ZW50U2VhbWxlc3NIYW5kbGVyLnBocCIgbWV0aG9kPSJwb3N0Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJ0b2tlbiIgdmFsdWU9IjhERDNFRUFFLUI5NTktQzY1RS03MDczLTYzQTNGQUUxMjZGRiI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iYW1vdW50IiB2YWx1ZT0iMS4wMCI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0ibWlocGF5aWQiIHZhbHVlPSJjOTlhNjQ1NWIzZTBkYzVjZDcxNjdhYjhjOGNjMTBkMmZhMTUzY2I1MDllM2Y2NGM2Y2QwZWQ5YzViNjRhOGM5Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJkaXNhYmxlSW50ZW50U2VhbWxlc3NGYWlsdXJlIiB2YWx1ZT0iMCI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0icGF5ZWVWcGEiIHZhbHVlPSJwYXl1dGVzdEBoZGZjYmFuayI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0icGF5ZWVOYW1lIiB2YWx1ZT0iU3VkaGFuc2h1Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJhZGRpdGlvbmFsQ2hhcmdlcyIgdmFsdWU9IjAiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InRyYW5zYWN0aW9uRmVlIiB2YWx1ZT0iMS4wMCI+PC9mb3JtPjxzY3JpcHQgdHlwZT0ndGV4dC9qYXZhc2NyaXB0Jz4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdpbmRvdy5vbmxvYWQ9ZnVuY3Rpb24oKXsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkb2N1bWVudC5mb3Jtc1sncGF5bWVudF9wb3N0J10uc3VibWl0KCk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAgICAgICAgIDwvc2NyaXB0PjwvYm9keT48L2h0bWw+",
          "otpPostUrl": "https://test.payu.in/ResponseHandler.php"
      }
    }
    ```
  </Accordion>
</Accordion>

***

## Step 3: Check UPI transaction status

Check the UPI transaction status using the **Verify Payment API** (verify_payment) API. For more information, refer to  <a href="verify_payment_api" target="_blank"> Verify Payment API</a>.

***

## Step 4: PayU sends Server-to-Server callback response

PayU can also send a server-to-server callback response whenever the transaction status gets updated.

<Accordion title="Implementation" icon="fa-code">
  The server-to-server response would be sent by PayU on a pre-set URL, which has to be provided by you. PayU will configure it at your back end. This response would be sent in key/value pair separated by the ampersand (&) character. In case any parameter is not used, we would send it back to you with an empty string. The sample response is similar to the following:

  ```plaintext
  unmappedstatus=success&phone=9999999999&txnid=FCDA1R100870163781&hash=84e3 35094bbcb2ddaa0f9a488eb338e143b273765d89c9dfa502402562d0b6f3c7935e28194ca92f7 380be7c84c3695415b106dcf52cb016a15fcf6adc98d724&status=success&curl=https://www. abc.in/payment/handlepayuresposne&firstname=NA&card_no=519619XXXXXX5049&furl= https://www.abc.in/payment/handlepayuresposne&productinfo=2&mode=DC&amount=800. 00&field4=6807112311042810&field3=6807112311042810&field2=838264&field9=SUCC ESS&email=NA&mihpayid=175477248&surl=https://www.ABC.in/payment/handlepayuresp osne&card_hash=9e88cb0573d4a826b61d808c0a870ed4a990682459b0ec9e95ea421e8e47b e8c&field1=42812
  ```

  The parameter list format is similar to the following:

  ```plaintext
  mihpayid,mode,status,key,txnid,amount,productinfo,firstname,lastname,address1,address2,city,state,country,zipcode,email,phone,udf1,udf2,udf3,udf4,udf5,udf6,udf7,udf8,udf9,udf10,card_token,card_no,field0,field1,field2,field3,field4,field5,field6,field7,field8,field9,offer,discou nt,offer_availed,unmappedstatus,hash,bank_ref_no,surl,curl,furl,card_hash
  ```
</Accordion>

***

## Step 5. Verify the payment

Use the webhooks to verify the payment. The following is the sample webhook payload in response. For more information, refer to [Webhook Events and Sample Payloads](doc:webhook-events-and-sample-payloads).

<Accordion title="Sample Webhook Response" icon="fa-table">
  ```plaintext
  mihpayid=27553369917
  &mode=SBQR
  &status=success
  &key=rZ1fX4
  &txnid=T2603041446091822117753
  &amount=40.00
  &addedon=2026-03-04+14%3A46%3A14
  &productinfo=Static+QR
  &firstname=
  &lastname=
  &address1=
  &address2=
  &city=Gurgaon
  &state=
  &country=
  &zipcode=122001
  &email=
  &phone=##########
  &udf1=
  &udf2=
  &udf3=
  &udf4=SoftQR
  &udf5=BFL0000006601446
  &udf6=
  &udf7=
  &udf8=
  &udf9=
  &udf10=
  &card_token=
  &card_no=
  &field0=STQ9IUFeqlafg78815827
  &field1=PRIYA+SHANKAR+PUSNAKE
  &field2=995486
  &field3=_mobilenum_%40axl
  &field4=bajajpay.6879729.d2m9cckd%40indus
  &field5=AXLd36cfcd317f243b5b3a2d62bc71caf78
  &field6=00000038683323284%7C_mobilenum_%7CSBIN0011418
  &field7=APPROVED+OR+COMPLETED+SUCCESSFULLY%7C00
  &field8=Payment+from+PhonePe
  &field9=Transaction+is+Successful.+Bank+Sent%3ATransaction+success
  &payment_source=payu
  &cardToken=
  &authenticaticationMethod=
  &PG_TYPE=SBQR-PG
  &error=E000
  &error_Message=No+Error
  &net_amount_debit=40
  &discount=0.00
  &offer_key=
  &offer_availed=
  &unmappedstatus=captured
  &hash=aefe0213c4299c7ee2039d5430f7bee63711ee627e1b47d2605d0384abbbf828f3641dae3cb126c8b2f761084cbb0bebad27bb325696cc44ce3061157d7cd9ff
  &bank_ref_no=793887773815
  &bank_ref_num=793887773815
  &bankcode=UPISBQR
  &surl=
  &curl=
  &furl=
  &psp_name=CARDHOLDERXXXXXXXXNAME
  ```
</Accordion>

<Accordion title="Callback Response Parameters" icon="fa-table">
  | Parameter   | Description                                |
  | ----------- | ------------------------------------------ |
  | status      | Transaction status: `success` or `failure` |
  | txnid       | Your transaction ID                        |
  | mihpayid    | PayU transaction ID                        |
  | amount      | Transaction amount                         |
  | productinfo | Product information                        |
  | hash        | Response hash for verification             |
</Accordion>

***

## Step 6: Update Invoice ID [Conditional]

<Update_Invoice_ID />

***

## Step 7: Upload the Invoices [Optional]

<Upload_Invoices />
