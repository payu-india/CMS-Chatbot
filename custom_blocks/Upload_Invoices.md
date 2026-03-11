---
name: Upload_Invoices
---
The invoices / Airway Bill can be uploaded using the **Invoice Upload API API**. AWB details are mandatory for Goods transactions. Invoice copies can be uploaded optionally.

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
