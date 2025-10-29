---
title: Post a UPI Recurring transaction - CB
deprecated: false
hidden: false
metadata:
  robots: index
---
Posting a UPI recurring transaction for cross-border payments involves the following steps:

## Step 1: Pre-Debit Notification

Post the pre-debit notification before 48 hours of the actual debit to notify the customer. For more information, refer to [Pre-Debit Notification API](ref:pre_debit_notification_api) .

## Step 2: Recurring Payment Transaction

Initiate recurring using the **Recurring Payment Transaction** API including the below UDF params under var1 object required for PACB flow. For more information, refer to <Anchor label="Recurring Payment Transaction API" target="_blank" href="ref:recurring_payment_api">Recurring Payment Transaction API</Anchor>.

<Table align={["left","left"]}>
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
        udf1
      </td>

      <td>
        This parameter must include the PAN and DOB of the buyer in the following format:
        PAN||DOB

        * _Note_*: The PAN and DOB are separated with two pipe (||) characters.
      </td>
    </tr>

    <tr>
      <td>
        udf3
      </td>

      <td>
        This parameter must include the invoice_id and the seller name(for PACB reseller use case) in the following format:
        invoice_id||sellerName

        * _Note_*: The invoice_id and seller name are separated with two pipe (||) characters.
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Notes:
>
> For the UDFs above:
>
> * If first value is absent, then UDF param will be sent as  NULL || \<VALUE>
> * If second value is absent, then UDF param will be sent as \ \<VALUE>

## Step 3: Update Invoice ID [Optional]

If the Invoice ID value was unavailable when posting the transaction at [Step 1](#step-1-make-payment-using-web-checkout-integration), it can be updated using the **UDF Update** API by posting it in the UDF5 parameter.

<GENERALAPIsEnvironment />

<Accordion title="Sample request other then UPI AutoPay" icon="fa-code">
  ```
    curl --location --globoff 'https://test.payu.in/merchant/postservice.php?form=2' \
    --form 'key="PRiQvJ"' \
    --form 'command="udf_update"' \
    --form 'var1="my_order_642"' \
    --form 'var2="AAAPZ1234C"' \
    --form 'var4="22/08/1972"' \
    --form 'var5="SellerName"' \
    --form 'var6="INV000000005"' \
    --form 'hash="{{hash}}"'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  ### Success Scenario

  * If successfully updated for cards

  ```JSON
  {
      "status": "UDF values updated",
      "transaction_id": "my_order_64240",
      "udf1": "AAAPZ1234C",
      "udf2": "",
      "udf3": "22/08/1972",
      "udf4": "SellerName",
      "udf5": "INV000000005"
  }
  ```

  * If successfully updated for UPI autopay:

  ```JSON
  {
      "status": "UDF values updated",
      "transaction_id": "my_order_64240",
      "udf1": "AAAPZ1234C",
      "udf2": "",
      "udf3": "22/08/1972",
      "udf4": "SellerName",
      "udf5": "INV000000005"
  }
  ```

  ### Failure Scenarios

  * If the transaction ID is empty

  ```JSON
  ( 
  [status] => 0 
  [msg] => Parameter missing 
  ) 
  ```

  * If the transaction ID is invalid

  ```JSON
  ( 
  [status] => 0 
  [msg] => Invalid TXN ID 
  ) 
  ```

  * If Hash is invalid:

  ```JSON
  {
      "status": 0,
      "msg": "Invalid Hash."
  }
  ```

  * If the merchant is not enabled for UDF updates:

  ```JSON
  {
    "status": "0",
    "msg": "Update not allowed on provided Field"
  }
  ```

  * If no data found in the transaction ID:

  ```JSON
  {
    "status": "0",
    "msg": "No Data Found for txnid: 3424"
  }
  ```

  * If the merchant is inactive:

  ```JSON
  {
    "msg": "Merchant is not authorized to use PayU API",
    "status": 0
  }
  ```
</Accordion>

<br />

## Step 4: Upload the Invoices

According to the RBI guidelines, the invoice file must be shared with PayU within 10 days of the transaction. The invoices can be uploaded using the **Invoice Upload** API.

<GENERALAPIsEnvironment />

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location -g --request POST '{{baseUrl}}/merchant/postservice?form=2' \ 
  --form 'key="{{merchantKey}}"' \ 
  --form 'command="opgsp_upload_invoice_awb"' \ 
  --form 'var1="403993715525825059"' \  - PayuId 
  --form 'var2="TestInv0001234568"' \ - invoice Id 
  --form 'var3="Invoice"' \ - type of upload - Invoice/AWB 
  --form 'file=@"/path/to/file"' \ - file 
  --form 'hash="{{hash}}"' 
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  <Accordion title="Success Scenario" icon="fa-check-circle">
    * When a file is uploaded successfully:

    ```plaintext
    {
    "responseCode":"00",
    "responseMsg":"File Uploaded Successfully"
    }
    ```
  </Accordion>

  <Accordion title="Failure Scenarios" icon="fa-exclamation-triangle">
    * When there is an error in uploading the file:

    ```plaintext
    { 
    "responseCode": "103", 
    "responseMsg": "Failed to Upload" 
    } 
    ```

    * When the file format is not supported:

    ```plaintext
    { 
    "responseCode": "105", 
    "responseMsg": "Not an PACB merchant, contact KAM" 
    } 
    ```

    * When the payuid is invalid:

    ```plaintext
    {
    "responseCode":"107",
    "responseMsg":"The PayuID in request is invalid"
    }
    ```

    * When a mandatory field is missing:

    ```plaintext
    {
    "responseCode":"109",
    "responseMsg":"All fields are mandatory, please check!"
    } 
    ```
  </Accordion>
</Accordion>

<Accordion title="Response Code and Description" icon="fa-list">
  Refer to [Response Code and Description - Invoice Upload API](ref:response-code-and-description-invoice-upload-api).
</Accordion>
