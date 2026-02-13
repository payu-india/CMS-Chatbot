---
title: UPI Collection with S2S Integration
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
In UPI Collect, the sequence of APIs is called to follow for redirection less experience.

<RegisterMerchantPrerequiste />

<Callout icon="❗️" theme="error">
  **Important UPI Integration Changes as per NPCI Mandate on UPI Collect Disablement**:

  For Android and Desktop web, UPI Collect flow has limitations. Consider migrating to UPI Intent S2S for better user experience:

  * **For Android Apps**: Implement Smart Intent using [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow) or use [PayU Android SDKs](doc:explore-android-sdks).

  * **For Web**: Use [UPI Intent S2S Integration](doc:upi-intent-server-to-server) to generate a QR code of the deeplink for better conversion.

  * **For iOS Apps**: You can continue using the UPI Collect flow as is, or implement deeplink handling.
</Callout>

**Steps to integrate**

<Cards columns={3}>
  <Card title="1. Validate VPA" href="https://docs.payu.in/docs/upi-collection-s2s#step-1-validate-vpa">
    Validate the Virtual Payment Address (VPA) before initiating the UPI transaction

    <br />
  </Card>

  <Card title="2. Initiate the payment to PayU" href="https://docs.payu.in/docs/upi-collection-s2s#step-2-initiate-the-payment-to-payu">
    Initiate the UPI payment request to PayU with required parameters

    <br />
  </Card>

  <Card title="3. Check UPI Transaction Status" href="https://docs.payu.in/docs/upi-collection-s2s#step-3-check-upi-transaction-status">
    Monitor and check the status of the UPI transaction in real-time

    <br />
  </Card>

  <Card title="4. S2S Call Back Response" href="https://docs.payu.in/docs/upi-collection-s2s#step-4-check-the-s2s-callback-response">
    Handle and process the server-to-server callback response from PayU

    <br />
  </Card>

  <Card title="5. Verify the payment" href="https://docs.payu.in/docs/upi-collection-s2s#step-5-verify-the-payment">
    Verify the payment status and ensure transaction completion
  </Card>

  <br />
</Cards>

<Accordion title="UPI Content Flow" icon="fa-table">
  The following diagram illustrates the UPI content process flow from the initiation of the transaction by the customer to the success of payment.

  ![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/07/UPI-Content-Flow-1024x457.png)

  **UPI Collect Process Steps**

  1. Customer selects UPI from the website or mobile app to make payment through. 

  2. PayU ​pre-fills the VPA address issuer to reduce customer input. ​ 

  3. PayU verifies the customer’s VPA and shares the customer’s name.  

  4. Customer proceeds with the transaction after confirmation 

     The customer sees a payment screen pre-filled with the amount and your name.  

  5. Customer accepts the payment to complete the transaction. ​ 
</Accordion>

## Workflow

<Image align="center" src="https://files.readme.io/af55c40e9c1fd7a87fc2c70872e63563ec83e940bba99c55d5d66f8e037eeecc-upi-s2s-collection-workflow.png" />

## Step 1: Validate VPA

This web service will let you validate VPA if it is a valid VPA or not.

After the customer enters VPA on your website, you need to call this API to check for VPA validation. If VPA is valid, you need to proceed with the next step. For a sample request or response, refer to  <a href="https://docs.payu.in/reference/validate_vpa_api" target="_blank"> Validate VPA</a>.

Collect the response in the  <a href="https://docs.payu.in/reference/_payment_s2s_upi_collection" target="_blank"> UPI Collection</a> under API Reference. The response for the S2S payment request is not similar to Merchant Hosted or PayU Hosted Checkout. For description of response parameters, refer to <a href="https://docs.payu.in/reference/addl_info-payment-apis#response-for-initial-server-to-server-request" target="_blank"> Additional Info for Payment APIs</a>.

## Step 2: Initiate the payment to PayU

To start with, the request is raised from the Merchant to PayU with the required transaction mandatory/optional parameters. This needs to be a server-to-server curl call request. This API is used for both Cards and UPI for generating a new transaction. Parameters and their descriptions are mentioned below.

For the "Try It" experience, refer to <a href="https://docs.payu.in/reference/_payment_s2s_upi_collection" target="_blank"> UPI Collection</a>.

**PayU URL Endpoint:**

<PaymentAPIEnvironment />

<Callout icon="📮" theme="default">
  **Postman Collection**: Download the **S2S > UPI Integration Postman Collection** from the following location:

  https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/5t0c6pe/upi-s2s-integration
</Callout>

Some of the parameters are mandatory for S2S integration, and a few are optional. You need to include the following parameters.

<Accordion title="Request parameters" icon="fa-table">
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
          `String` (alphanumeric) Merchant transaction identifier - This parameter must be unique (after a successful transaction) & alphanumeric special (\<= 50 characters & excluding >,\<, =,:,&, ‘).
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
          `String` (alphanumeric) This field must contain the product name. By default, the value is 'storefront' (max. 100 characters).
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
          <p>surl<br /><code>mandatory</code></p>
        </td>

        <td style={{ textAlign: "left" }}>
          <p><strong>String</strong> Success URL (surl) – It must contain the URL to which PayU will redirect the final response if the transaction is successful.</p>
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
          <p><strong>String</strong> Failure URL (furl) – It must contain the URL to which PayU will redirect the final response in case of failure.</p>
        </td>

        <td style={{ textAlign: "left" }}>
          <p><a href="https://apiplayground-response.herokuapp.com/">[https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)</a></p>
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
          <p><strong>String</strong> Each payment option is identified with a unique bank code at PayU. For UPI Collect, specify the value as <strong>UPI</strong>.</p>
        </td>

        <td style={{ textAlign: "left" }}>
          <p>UPI</p>
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          lastname
          `optional`
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
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter can include any custom information in request (up to 255 characters).
        </td>

        <td style={{ textAlign: "left" }}>
          Website order
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
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter can include any custom information in request.
          (up to 255 characters.)
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          udf4
          optional
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter can include any custom information in request.
          (up to 255 characters.)
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          udf5
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter can include any custom information in request.
          (up to 255 characters.)
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          s2s\_client\_ip
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `Sting` This parameter must have the source IP of the user's device.

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
          `String` This parameter must have the user agent of device.

          * *Note*\*: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          txn\_s2s\_flow
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String`This parameter must be posted with the values a **4** for transaction flow.
        </td>

        <td style={{ textAlign: "left" }}>
          4
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          upiAppName
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` For Specific Intent, merchant should share the app name which is selected by customer on the merchant check-out page. The following are the enum’s expected for major apps:

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
          vpa
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` Virtual Private Address. VPA can first be validated using VPA validate web service. Also, add regex where ‘@’ exists. Example: 8800411088\@upi This needs to be passed in case of collect flow of UPI only.
        </td>

        <td style={{ textAlign: "left" }}>
          8800411088\@upi
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          hash
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` Hash is a crucial parameter – used specifically to avoid any tampering during the transaction. For more information, refer to  <a href="hashing-request-and-response" target="_blank"> Generate Hash</a>.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>
    </tbody>
  </Table>
</Accordion>

<Accordion title="Understanding Hashing and sample code" icon="fa-code">
  <HashingRequestParameters />

  #### Hashing Sample Code

  <HashingSample />
</Accordion>

<Accordion title="Sample request" icon="fa-code">
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
  --data-urlencode 'bankcode=UPI' \
  --data-urlencode 'vpa=9999999999@upi' \
  --data-urlencode 'udf_params={"udf7":"asdf","udf8":"12"}' \
  --data-urlencode 'buyer_type_business=1'
  ```
</Accordion>

## Step 3: Redirect the customer to Timer Page

Redirect the customer to PayU Hosted Timer page, or create your own timer page and check the transactions status from PayU using the verify_payment API.

To redirect customer on Payu hosted timer page, use the result.acsTemplate, and base64decode to use that HTML to open the timer page.

<Accordion title="Sample PayU response for successfully initiated UPI Collect request" icon="fa-code">
  ```json
  {
      "metaData": {
          "message": null,
          "referenceId": "04029ff0af37fc9290f6d9b5a3997f9a9ea4a7b22e2b3fc768cae87c1e78c16c",
          "statusCode": null,
          "txnId": "my_order_68480",
          "txnStatus": "pending",
          "unmappedStatus": "pending"
      },
      "result": {
          "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vYXBpdGVzdC5wYXl1LmluL3B1YmxpYy8jLzA0MDI5ZmYwYWYzN2ZjOTI5MGY2ZDliNWEzOTk3ZjlhOWVhNGE3YjIyZTJiM2ZjNzY4Y2FlODdjMWU3OGMxNmMvdXBpTG9hZGVyIiBtZXRob2Q9ImdldCI+PC9mb3JtPjxzY3JpcHQgdHlwZT0ndGV4dC9qYXZhc2NyaXB0Jz4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdpbmRvdy5vbmxvYWQ9ZnVuY3Rpb24oKXsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkb2N1bWVudC5mb3Jtc1sncGF5bWVudF9wb3N0J10uc3VibWl0KCk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAgICAgICAgIDwvc2NyaXB0PjwvYm9keT48L2h0bWw+",
          "otpPostUrl": "https://test.payu.in/ResponseHandler.php"
      }
  }
  ```
</Accordion>

<Callout icon="📘" theme="info">
  Using a webbook wait for Payu to mark the transaction completed. For more information, refer to [Webhooks](doc:webhooks-consolidated).
</Callout>

## Step 4: Check UPI transaction status

Check the UPI transaction status using the **Verify Payment API** (verify_payment) API. For more information, refer to [Verify Payment API](ref:verify_payment_api)

***

## Step 5: Check the S2S callback response

The response to this call would be a base64 encoded JSON containing transaction ID and other transaction details.

<Accordion title="Reverse hashing" icon="fa-info-circle">
  <ReverseHashing />
</Accordion>

<Accordion title="Sample response" icon="fa-table">
  ```plaintext
  eyJzdGF0dXMiOiJzdWNjZXNzIiwicmVzdWx0Ijp7Im1paHBheWlkIjoiNzYwMTI2NTU4NSIsIm1vZGUiOiJVUEkiLCJzdGF0dXMiOiJwZW5kaW5nIiwia2V5IjoiTWVyY2hhbnRLZXkiLCJ0eG5pZCI6IjZiMmYzZDY4NWVjMWJiYTdkZDRiIiwiYW1vdW50IjoiMTAuMDAiLCJhZGRlZG9uIjoiMjAxOC0xMS0wMSAxOTo1NjozMiIsInByb2R1Y3RpbmZvIjoiUHJvZHVjdCBJbmZvIiwiZmlyc3RuYW1lIjoiUGF5dS1Vc2VyIiwibGFzdG5hbWUiOiIiLCJhZGRyZXNzMSI6IiIsImFkZHJlc3MyIjoiIiwiY2l0eSI6IiIsInN0YXRlIjoiIiwiY291bnRyeSI6IiIsInppcGNvZGUiOiIiLCJlbWFpbCI6InRlc3RAZXhhbXBsZS5jb20iLCJwaG9uZSI6IjEyMzQ1Njc4OTAiLCJ1ZGYxIjoiIiwidWRmMiI6IiIsInVkZjMiOiIiLCJ1ZGY0IjoiIiwidWRmNSI6IiIsInVkZjYiOiIiLCJ1ZGY3IjoiIiwidWRmOCI6IiIsInVkZjkiOiIiLCJ1ZGYxMCI6IiIsImNhcmRfdG9rZW4iOiIiLCJjYXJkX25vIjoiIiwiZmllbGQwIjoiIiwiZmllbGQxIjoiYWJjZEB1cGkiLCJmaWVsZDIiOiIiLCJmaWVsZDMiOiIiLCJmaWVsZDQiOiIiLCJmaWVsZDUiOiIiLCJmaWVsZDYiOiIiLCJmaWVsZDciOiIiLCJmaWVsZDgiOiIiLCJmaWVsZDkiOiIiLCJwYXltZW50X3NvdXJjZSI6InBheXVQdXJlUzJTIiwiUEdfVFlQRSI6IkFYSVNVIiwiZXJyb3IiOiJFMDAwIiwiZXJyb3JfTWVzc2FnZSI6Ik5vIEVycm9yIiwibmV0X2Ftb3VudF9kZWJpdCI6IjAiLCJhZGRpdGlvbmFsQ2hhcmdlcyI6IjI5LjUiLCJ1bm1hcHBlZHN0YXR1cyI6ImluIHByb2dyZXNzIiwiaGFzaCI6IjU2NzQ3OGE5ZDUyMzhlZTIyZGFhMDM2ZWMwMjAxMzk0OGY2YjgwNGUzMWNhYzNkYmQyMDc1NmU5ZjFkNDFlMjI4ZTQxYzJkYjcwZmU4ZWRlZmMyNDBiOTQwODZlN2QzN2Y4ZDQ2OTA4MzU4Y2NjNzA4Y2JjNWVlNTJjMjlkYWEwIiwiYmFua19yZWZfbm8iOiJBWEk5MTEwMDAwMDAwMDQ5MTg0NzY2MTU0MTc5OTcwNTY5OCIsImJhbmtfcmVmX251bSI6IkFYSTkxMTAwMDAwMDAwNDkxODQ3NjYxNTQxNzk5NzA1Njk4IiwiYmFua2NvZGUiOiJVUEkiLCJzdXJsIjoiaHR0cHM6XC9cL2FkbWluLnBheXUuaW5cL3Rlc3RfcmVzcG9uc2UiLCJjdXJsIjoiaHR0cHM6XC9cL2FkbWluLnBheXUuaW5cL3Rlc3RfcmVzcG9uc2UiLCJmdXJsIjoiaHR0cHM6XC9cL2FkbWluLnBheXUuaW5cL3Rlc3RfcmVzcG9uc2UifX0
  ```

  **Base64 decoded response:**

  ```plaintext
  {"status":"success","result":{"mihpayid":"7601265585","mode":"UPI","status":"pending","key":"MerchantKey","txnid":"6b2f3d685ec1bba7dd4b","amount":"10.00","addedon":"2018-11-01
  19:56:32","productinfo":"ProductInfo","firstname":"PayuUser","lastname":"","address1":"","address2":"","city":"","state":"","country":"","zipcode":"","email":"test@example.com","phone":"1234567890","udf1":"","udf2":"","udf3":"","udf4":"","udf5":"","udf6":"","udf7":"","udf8":"","udf9":"","udf10":"","card_token":"","card_no":"","field0":"","field1":"abcd@upi","field2":"","field3":"","field4":"","field5":"","field6":"","field7":"","field8":"","field9":"","payment_source":"payuPureS2S","PG_TYPE":"AXISU","error":"E000","error_Message":"NoError","net_amount_debit":"0","additionalCharges":"29.5","unmappedstatus":"inprogress","hash":"567478a9d5238ee22daa036ec02013948f6b804e31cac3dbd20756e9f1d41e228e41c2db70fe8edefc240b94086e7d37f8d46908358ccc708cbc5ee52c29daa0","bank_ref_no":"AXI91100000000491847661541799705698","bank_ref_num":"AXI91100000000491847661541799705698","bankcode":"UPI","surl":"https:\/\/admin.payu.in\/test_response","curl":"https:\/\/admin.payu.in\/test_response","furl":"https:\/\/admin.payu.in\/test_response"}}
  ```

  > 📘 Note:
  >
  > In case of an invalid VPA, the final result will be a JSON in plain text as follows.

  ```plaintext
  {"result":null,"status":"failed","error":"E1617","message":"Invalid vpa"}
  ```

  ## Step 6: Verify the payment

  <Verify_Payment_Tabs />

  <br />
</Accordion>
