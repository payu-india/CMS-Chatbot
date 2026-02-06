---
title: REST API Format
excerpt: >-
  PayU has created many REST APIs and each REST API has a specific function. You
  can use them to automate different features. The basic format and execution of
  all web services remain the same. Each REST API is a server-to-server call
  from your server to PayU’s server.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
REST API can be accessed by making a server-to-server call on the following PayU URLs:

<Callout icon="📘" theme="info">
  **Reference**: Refer to the following recipe for a walkthrough of a cURL request for a REST API:

  <a
    href="https://payu-hosted-checkout.readme.io/v1/recipes/curl-walkthrough"
    id="65084edbb1c590100cf1243e"
    style={{
          display: "block",
          backgroundColor: "#018FF4",
          color: "white",
          padding: "1rem",
          borderRadius: "0.5rem",
          textDecoration: "none",
          maxWidth: "400px",
          marginBottom: "1rem",
        }}
  >
    <div style={{ fontSize: "2rem" }}>🦉</div>
    <h3 style={{ margin: "0.5rem 0 0" }}>CURL Walkthrough</h3>
    <p style={{ margin: 0 }}>Learn how to make API calls using CURL</p>
  </a>
</Callout>

## URLs for Test and Production environment

### Base URLs

<table style={{ border: "0.1rem solid rgb(242, 242, 242)" }}>
  <tbody>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Test</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>[https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2)</td>
    </tr>

    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Production</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>[https://info.payu.in/merchant/postservice.php?form=2](https://info.payu.in/merchant/postservice.php?form=2)</td>
    </tr>
  </tbody>
</table>

> 📘 Note:
>
> The above base URLs are for the General APIs. Refer to the specific API reference page to get the exact endpoints. For the _payment APIs, refer to any of the following:
>
> * [Collect Payment API for PayU Hosted Checkout integration](ref:_payment_payu_hosted_checkout)
> * [Collect Payment API for Merchant Hosted Checkout integration](ref:_payment_merchant_hosted)
> * [Collect Payment API for S2S integration](ref:_payment_server_to_server)

## Request format

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Sample Value**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key
      </td>

      <td>
        Merchant key provided by PayU. For more information on checking your key and Salt, refer to [Access Merchant Key and Salt](doc:generate-merchant-key-and-salt-copy).
      </td>

      <td>
        Ibibo
      </td>
    </tr>

    <tr>
      <td>
        command
      </td>

      <td>
        This parameter must have name of the web-service.
      </td>

      <td>
        save_card
      </td>
    </tr>

    <tr>
      <td>
        hash
      </td>

      <td>
        This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash is mentioned below:
        sha512(key|command|var1|salt) sha512 is the encryption method used.

        * _Note_*:  For _payment APIs, refer to [Generate Hash](doc:hashing-request-and-response)
      </td>

      <td>
        ajh84ba8abvav
      </td>
    </tr>

    <tr>
      <td>
        var1, var2, var3 ... up to var15
      </td>

      <td>
        These are the variable parameters, whose values depend on the particular web-service. The definition of these parameters will be covered in the (Read command explanations mentioned later - separate for all the actions/commands.)
      </td>

      <td>
        Read specific commands.
      </td>
    </tr>
  </tbody>
</Table>

## Response format

> 📘 Note:
>
> To get the response in JSON, you need to append **form=2** along with the endpoint similar to the following:

[https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2)

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **Parameter**
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
        status
      </td>

      <td>
        This parameter returns the any of the following status of web service call:

        * 1 - If web service call succeeded
        * 0 - if web service call failed
      </td>

      <td>
        0
      </td>
    </tr>

    <tr>
      <td>
        msg
      </td>

      <td>
        Reason String
      </td>

      <td>
        Parameter missing or token is empty or amount is empty or transaction not exists
      </td>
    </tr>

    <tr>
      <td>
        transaction_details
      </td>

      <td>
        This parameter may or may not be return response depending on the web service being called.
      </td>

      <td>
        mihpayid,request_id, bank_ref_num etc
      </td>
    </tr>

    <tr>
      <td>
        request_id
      </td>

      <td>
        PayU Request ID for a request in a Transaction. eg. A transaction can have a refund request.
      </td>

      <td>
        7800456
      </td>
    </tr>

    <tr>
      <td>
        bank_ref_num
      </td>

      <td>
        Bank Reference Number. If bank provides after a successful action.
      </td>

      <td>
        204519474956
      </td>
    </tr>
  </tbody>
</Table>
