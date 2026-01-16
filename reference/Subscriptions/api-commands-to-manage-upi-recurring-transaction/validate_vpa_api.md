---
title: Validate VPA API
excerpt: ''
api:
  file: paritalgeneral-apis-15.json
  operationId: validateVPA
deprecated: false
hidden: false
metadata:
  title: Validate VPA or UPI Handle API
  description: >-
    Learn how to validate Virtual Payment Addresses (VPA) using PayU's Validate
    VPA API. This documentation provides detailed instructions for integrating
    VPA validation, ensuring secure and accurate UPI transactions for your
    customers.
  keywords:
    - PayU Validate VPA API
    - ' Validate Virtual Payment Address'
    - ' PayU UPI handle validation'
    - ' UPI VPA validation'
    - ' Check UPI Handle'
    - ' Check UPI VPA'
  robots: index
next:
  description: ''
---
This API (**validateVPA**) will let you validate VPA if it is a valid VPA or not.

After the customer enters VPA on the merchant page, you need to call this API to check for VPA validation. If VPA is valid only then, the second call should be made.

<Accordion title="Sample request" icon="fa-code">
  **Validate VPA**
<Validate_VPA />

  **Validate VPA for Recurring Payment**

  ```curl
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&command=validateVPA&var1=9999999999@upi&var2={"validateAutoPayVPA":"1"}&hash=75uy573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472poy9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e"
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  **Success scenario**

  if successfully validated:

  ```plaintext
  {
     "status":"SUCCESS",
     "vpa":"9999999999@upi",
     "isVPAValid":1,
     "isAutoPayVPAValid":1,
     "isAutoPayBankValid":"NA",
     "payerAccountName":"ABC"
  }
  ```

  > 📘 Notes:
  >
  > * The **payerAccountName** parameter can be empty or NA or will have a payer name based on the value given by the bank.
  > * If both **isVPAValid** and **isAutoPayVPAValid** is 1, you must initiate payment for Recurring Payments.
  > * Ignore the **isAutoPayBankValid** parameter in the response.

  **Failure scenarios**

  * If invalid VPA, the response is similar to the following:

  ```plaintext
  {
   "status":"SUCCESS","vpa":"abc@upi","isVPAValid":0,"payerAccountName":"NA"
  }  
  ```

  * Invalid VPA but handle supporting SI (Autopay):

  ```plaintext
  {
   "status":"SUCCESS","vpa":"abc@upi","isVPAValid":0,"isAutoPayVPAValid":1,"isAutoPayBankValid":"NA","payerAccountName":"NA"
  }
  ```

  * Customer valid but handle not supporting SI (Autopay):

  ```plaintext
  {
    "status":"SUCCESS","vpa":"xyz@freecharge","isVPAValid":1,"isAutoPayVPAValid":0,"isAutoPayBankValid":"NA","payerAccountName":"XYZ"
  }
  ```

  * Neither customer valid nor handle supporting Autopay:

  ```plaintext
  {
    "status":"SUCCESS","vpa":"xyz@freecharge","isVPAValid":0,"isAutoPayVPAValid":0,"isAutoPayBankValid":"NA","payerAccountName":"NA"
  }
  ```
</Accordion>

<Accordion title="Response parameters" icon="fa-list">
  {/* Properly formatted JSX Table */}

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
          status
        </td>

        <td>
          This parameter returns any of the following based on whether the API was successful or failure:

          * Successful
          * Failure
        </td>
      </tr>

      <tr>
        <td>
          vpa
        </td>

        <td>
          This parameter returns the VPA ID.
        </td>
      </tr>

      <tr>
        <td>
          isVPAValid
        </td>

        <td>
          This parameter returns any of the following to indicate whether the VPA is valid or not:

          * **1**: Indicates that VPA is valid
          * **0**: Indicates the VPA is invalid
        </td>
      </tr>

      <tr>
        <td>
          isAutoPayVPAValid
        </td>

        <td>
          This parameter returns any of the following to indicate whether the VPA has registered for Recurring Payments or Autopay:

          * **1**: Indicates that VPA has registered for Recurring Payments
          * **0**: Indicates that VPA has not registered for Recurring Payments
        </td>
      </tr>

      <tr>
        <td>
          isAutoPayBankValid
        </td>

        <td>
          This parameter returns any of the following to indicate whether the corresponding bank account has registered for Recurring Payments or Autopay:

          * **1**: Indicates that bank account has registered for Recurring Payments
          * **0**: Indicates that bank account has not registered for Recurring Payments
        </td>
      </tr>

      <tr>
        <td>
          payerAccountName
        </td>

        <td>
          This parameter returns the name of the account holder (corresponding VPA).
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>

## Request parameters

You can use any valid VPA while trying out the API:

<Accordion title="Additional information for request parameters" icon="fa-flask">
  {/* Properly formatted JSX Table with align attribute */}

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
          {/* Properly formatted JSX component */}

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
          {/* Properly formatted JSX component */}

          <Glossary>hash</Glossary>
        </td>

        <td style={{ textAlign: "left" }}>
          Hash logic for this API is:

          ```
          sha512(key|command|var1|salt) sha512
          ```
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          var1
        </td>

        <td style={{ textAlign: "left" }}>
          For JSON fields description, refer to [Additional Info for General APIs](ref:addl-info-general-apis)
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>
