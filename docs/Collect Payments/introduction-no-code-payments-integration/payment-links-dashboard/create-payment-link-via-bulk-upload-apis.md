---
title: Create Payment Links via Bulk Upload - APIs
excerpt: Know how to create payment links via bulk upload option using APIs.
deprecated: false
hidden: true
metadata:
  robots: index
---
The bulk upload option using APIs lets you create many payment links by uploading a `.csv` file.

## Integration Steps

Below are the integration steps:

<style>
  {`
        .zoom-card-link {
          display: block;
          color: inherit !important;
          text-decoration: none !important;
          transition: transform 0.2s ease;
        }
        .zoom-card-link h4,
        .zoom-card-link p,
        .zoom-card-link span {
          color: inherit !important;
          text-decoration: none !important;
        }
        .zoom-card-link:hover {
          transform: scale(1.05);
        }
      `}
</style>

<Cards columns={3}>
  <Card>
    <a href="#step-1-get-the-access-token" className="zoom-card-link">
      <div style={{ color: "#000", padding: "8px" }}>
        <i className="fa fa-key" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }} />

        <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Step 1. Get the Access Token</h4>

        <p style={{ margin: 0 }}>
          Fetch the Bearer Token.
        </p>
      </div>
    </a>
  </Card>

  <Card>
    <a href="#step-2-upload-the-bulk-file" className="zoom-card-link">
      <div style={{ color: "#000", padding: "8px" }}>
        <i className="fa fa-file-upload" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }} />

        <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Step 2. Upload the Bulk File</h4>

        <p style={{ margin: 0 }}>
          Upload the .csv File to Create Payment Links.
        </p>
      </div>
    </a>
  </Card>

  <Card>
    <a href="#step-3-fetch-payment-links" className="zoom-card-link">
      <div style={{ color: "#000", padding: "8px" }}>
        <i className="fa fa-link" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }} />

        <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Step 3. Fetch Payment Links</h4>

        <p style={{ margin: 0 }}>
          Get the Created Payment Links Using the Batch ID.
        </p>
      </div>
    </a>
  </Card>
</Cards>

### Step 1. Get the Access Token

The first step is to obtain an access token using the following API. Refer to the <Anchor label="Get Access Token API" target="_blank" href="https://docs.payu.in/reference/get-token-api-for-payment-links">Get Access Token API</Anchor> for more information.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /oauth/token
  </Card>
</Cards>

<Accordion title="Environment Details" icon="fa-cogs">
  |                |                                                              |
  | :------------- | :----------------------------------------------------------- |
  | **Test**       | https://uat-accounts.payu.in/oauth/token |
  | **Production** | https://accounts.payu.in/oauth/token    |
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
  ```curl
  curl --location -g --request POST '{{hub_base_url}}/oauth/token' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'client_id={{client_id}}' \
  --data-urlencode 'client_secret={{client_secret}}' \
  --data-urlencode 'grant_type=client_credentials' \
  --data-urlencode 'scope=read_payment_links'
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-code">
  ```json Success Response
  {
  "access_token": "ea4ed864b4d2a04b90c1e987a5d25a5da1d43fa5f7d123be6814a1e973f196c4",
  "token_type": "Bearer",
  "expires_in": 7011,
  "scope": "create_payment_links",
  "created_at": 1763036368
  }
  ```
  ```json Error Response
  {
    "error": "invalid_client",
    "error_description": "Client authentication failed",
    "status": 401
  }
  ```
</Accordion>

<Accordion title="Request Parameters" icon="fa-table">
  <Table align={["left","left"]}>
    <thead>
      <tr>
        <th style={{ textAlign: "left" }}>
          **Parameter**
        </th>

        <th style={{ textAlign: "left" }}>
          **Description**
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td style={{ textAlign: "left" }}>
          `client_id` *mandatory*
        </td>

        <td style={{ textAlign: "left" }}>
          `string` Your OAuth 2.0 client ID issued by PayU. Refer to the <Anchor label="Get Client ID and Secret from Dashboard" target="_blank" href="/docs/get-client-id-and-secret-from-dashboard">Get Client ID and Secret from Dashboard</Anchor> page for more information.
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          `client_secret` *mandatory*
        </td>

        <td style={{ textAlign: "left" }}>
          `string` Your OAuth 2.0 client secret (keep this secure). Refer to the <Anchor label="Get Client ID and Secret from Dashboard" target="_blank" href="/docs/get-client-id-and-secret-from-dashboard">Get Client ID and Secret from Dashboard</Anchor> page for more information.
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          `grant_type` *mandatory*
        </td>

        <td style={{ textAlign: "left" }}>
          `string/enum` The OAuth 2.0 grant type for server-to-server authentication. Allowed value is `client_credentials`.
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          `scope` *optional*
        </td>

        <td style={{ textAlign: "left" }}>
          `string` The scope that must be used for payment links are: <ul><li>Create Link: create\_payment\_links</li> <li>Change status and expiry: update\_payment\_links</li> <li>Get a single payment link: read\_payment\_links</li> <li>Get all payment links: read\_payment\_links</li> <li>Share payment links: read\_payment\_links</li></ul>

          <strong>Note:</strong> Merchant can pass up to three scopes simultaneously for an access token value. This is done by passing scopes separated by a space between them. For example: `create_payment_links update_payment_links read_payment_links`.
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>

<Accordion title="Response Parameters" icon="fa-table">
  | **Parameter**  | **Description**                                                |
  | :------------- | :------------------------------------------------------------- |
  | `access_token` | `string` The generated access token.                           |
  | `token_type`   | `string` The type of the generated token. Here it is `Bearer`. |
  | `expires_in`   | `string` The token expiry timestamp.                           |
  | `scope`        | `string` The scope of the token.                               |
  | `created_at`   | `string` The timestamp at which the token was created.         |
</Accordion>

### Step 2: Upload the Bulk File

Use the generated access token in the step 1 and upload the bulk file using the following API:

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /payment-links/bulk-uploads/v2/upload
  </Card>
</Cards>

<Accordion title="Environment Details" icon="fa-cogs">
  |                |                                                        |
  | :------------- | :----------------------------------------------------- |
  | **Test**       | [https://oneapi.payu.in](https://oneapi.payu.in)       |
  | **Production** | [https://uatoneapi.payu.in](https://uatoneapi.payu.in) |
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
  ```curl
  curl -X POST 'https://oneapi.payu.in/payment-links/bulk-uploads/v2/upload' \
    -H 'accept: application/json' \
    -H 'authorization: Bearer_ACCESS_TOKEN' \
    -H 'mid: 8235901' \
    -H 'product: PAYUBIZ' \
    -H 'origin: https://payu.in' \
    -H 'referer: https://payu.in/' \
    -F 'file=@/absolute/path/to/bulktest.csv;type=text/csv' \
    -F 'payload={
      "batchDesc": "Apr-26 marketing batch",
      "batchId": "",
      "source": "BULKUPLOAD",
      "fileType": 0,
      "shareVia": {
        "email": true,
        "mobile": true
      },
      "customAttributes": [
        {
          "customAttributeName": "Customer Name",
          "attributeType": "input",
          "checked": true,
          "required": true
        },
        {
          "customAttributeName": "Customer Email",
          "attributeType": "input",
          "checked": true,
          "required": true
        },
        {
          "customAttributeName": "Customer Phone",
          "attributeType": "input",
          "checked": true,
          "required": true
        }
      ]
    };type=application/json'
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-code">
  ```json Success Response
  {
    "status":0,
    "message":"Bulk link creation started",
    "result":{
      "batchId":"BULK832297752700",
      "errorFileDownloadUrl":null,
      "rowCount":3
    },
    "errorCode":null,
    "guid":"25666641-b2a7-4ecc-93b3-79e16761fd6a"
  }
  ```
  ```json Error Response
  {
    "status":-1,
    "message":"Invalid Data.Please check the errorFile",
    "result":{
      "batchId":null,
      "errorFileDownloadUrl":"https://<s3-presigned-url>",
      "rowCount":3
    }
  }
  ```
</Accordion>

<Accordion title="Request Headers" icon="fa-table">
  | **Header Parameter**        | **Description**                                                                                                                    |
  | :-------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
  | `authorization` *mandatory* | `string` The access token generated in the step 1. For example, `ea4ed864b4d2a04b90c1e987a5d25a5da1d43fa5f7d123be6814a1e973f196c4` |
  | `mid` *mandatory*           | `string` The unique merchant ID.                                                                                                   |
  | `product` *mandatory*       | `string` The PayU product family. For example `PAYUBIZ`.                                                                           |
</Accordion>

<Accordion title="Request Parameters" icon="fa-table">
  | **Parameter**      | **Description**                                                                                     |                                                                        |
  | :----------------- | :-------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
  | `file` *mandatory* | `file (CSV)` The `.csv` file name you wan to upload. It should match \`^\[-\_A-Za-z.()\s\d]+.(csv\\ | CSV)$`. For example, `@/absolute/path/to/bulktest.csv;type=text/csv\`. |
  | `payload`          | `application/json` The payload details. Parameters are described in the payload Object section.     |                                                                        |
</Accordion>

<br />

<Accordion title="Payload Object Parameters and Description" icon="fa-table">
  | **Parameter**                 | **Description**                                                                                                                                                                                                  |
  | :---------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `batchId` *optional*          | `string` The batch ID. If passed, should be alphanumeric (^\[a-zA-Z0-9]\*$) and unique for the merchant.                                                                                                         |
  | `batchDesc` *mandatory*       | `string` The batch description.                                                                                                                                                                                  |
  | `source` *optional*           | `string` The payload source. Defaults to `BULKUPLOAD`. Allowed values: <ul><li><code>BULKUPLOAD</code></li> <li><code>SI\_BULKUPLOAD</code></li></ul>                                                            |
  | `fileType` *optional*         | `integer` The uploaded file type. Possible values: <ul><li><code>0</code>: Payment Link</li> <li><code>1</code>: Aggregator Payment Link</li> <li><code>2</code>: Subscription</li></ul>                         |
  | `shareVia` *optional*         | `object` Use this object to share the link via email or mobile. `{email: bool, mobile: bool}`                                                                                                                    |
  | `customAttributes` *optional* | `array` The array of custom attributes with extra fields collected from the customer. `{"customAttributeName":"Customer Name","attributeType":"input","options":["opt1","opt2"],"checked":true,"required":true}` |
  | `reminder` *optional*         | `object` Use this object send a reminder. `{isScheduled, type (0=BEFORE,1=AFTER), channels:[\"email\",\"phone\"]}`                                                                                               |
</Accordion>

<Accordion title="Response Parameters" icon="fa-table">
  | **Parameter**          | **Description**                                                                                               |
  | :--------------------- | :------------------------------------------------------------------------------------------------------------ |
  | `status`               | `string` The upload status.                                                                                   |
  | `message`              | `string` The status message. For example `Bulk link creation started`.                                        |
  | `batchId`              | `string` The created unique batch ID. For example `BULK832297752700`.                                         |
  | `errorFileDownloadUrl` | `string/null` This is returned as null if the upload is successful.                                           |
  | `rowCount`             | `integer` Total data rows in the uploaded file (excluding header). This value is returned only when non-null. |
</Accordion>

<Accordion title="Error Response Scenarios" icon="fa-exclamation-triangle">
  | **Error Message**                                                  | **Description**                                          |       |              |
  | :----------------------------------------------------------------- | :------------------------------------------------------- | ----- | ------------ |
  | `merchantId can not be null`                                       | Missing `mid`                                            |       |              |
  | `Invalid bulk upload source`                                       | Invalid `source`                                         |       |              |
  | `Batch with given batch Id already exists`                         | Duplicate `batchId`                                      |       |              |
  | `Invalid file format`                                              | Bad file extension / name                                |       |              |
  | \`col = Not a valid column \\                                      | Mandatory columns(Amount/Description) are not present \\ | ...\` | Header issue |
  | `Number of cell in row is not equal to number of headers :- <row>` | Row width mismatch                                       |       |              |
  | `Exception while uploading`                                        | Kafka / IO error                                         |       |              |
</Accordion>

### Step 3. Fetch Payment Links

Now that you have uploaded the file, use this API to fetch the payment links that have already been persisted for a given batch. Because creation is async, this endpoint will return links progressively while the batch is still in `processing`.

<Cards>
  <Card title="Method">
    GET
  </Card>

  <Card title="Endpoint">
    /payment-links/bulk-uploads/batchId
  </Card>
</Cards>

<Accordion title="Environment Details" icon="fa-cogs">
  |                |                                                        |
  | :------------- | :----------------------------------------------------- |
  | **Test**       | [https://oneapi.payu.in](https://oneapi.payu.in)       |
  | **Production** | [https://uatoneapi.payu.in](https://uatoneapi.payu.in) |
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
  ```curl
  curl -X GET 'https://oneapi.payu.in/payment-links/bulk-uploads/BULK832297752700?orderBy=addedOn&order=desc&pageOffset=0&pageSize=20' \
    -H 'accept: application/json' \
    -H 'authorization: Bearer_ACCESS_TOKEN' \
    -H 'mid: 8235901' \
    -H 'product: PAYUBIZ' \
    -H 'origin: https://payu.in' \
    -H 'referer: https://payu.in/'
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-code">
  ```json Success Response
  {
    "status": 0,
    "message": null,
    "result": {
      "pageSize": 20,
      "pages": 1,
      "rows": 3,
      "pageOffset": 0,
      "paymentLinksList": [
        {
          "invoiceNumber": "INV-1001",
          "description": "Apr subscription",
          "createDate": "2026-04-24T11:32:18.000+00:00",
          "paymentLinkURL": "https://u.payu.in/abcd1234",
          "customerName": "Asha Rao",
          "amount": 1499.00,
          "active": true,
          "expiry": "2026-05-24T11:32:18.000+00:00",
          "isAmountFilledByCustomer": false,
          "isPartialPaymentAllowed": false,
          "status": "active",
          "isScheduled": null,
          "reminderCount": null,
          "isSplit": false,
          "currency": "INR",
          "merchantId": 8235901,
          "creatorEmail": "ops@example.com"
        }
      ]
    },
    "errorCode": null,
    "guid": "..."
  }
  ```
</Accordion>

<Accordion title="Path and Query Parameters" icon="fa-table">
  | **Parameter**           | **Passed In** | **Description**                                                              |
  | :---------------------- | :------------ | :--------------------------------------------------------------------------- |
  | `batchId` *mandatory*   | path          | `string` The unique batch ID.                                                |
  | `orderBy` *mandatory*   | query         | `string` The order by description.                                           |
  | `order` *optional*      | query         | `string` The order description.                                              |
  | `pageOffset` *optional* | query         | `integer` The page offset number.                                            |
  | `pageSize` *optional*   | query         | `integer` The page size.                                                     |
  | `searchText` *optional* | query         | `string` The search text. Case‑insensitive substring match on `customerName` |
  | `status` *optional*     | query         | `object` The link status.                                                    |
</Accordion>

<Accordion title="Response Parameters" icon="fa-table">
  | **Parameter**              | **Description**                                                                            |
  | :------------------------- | :----------------------------------------------------------------------------------------- |
  | `invoiceNumber`            | `string` The invoice number. Same value as InvoiceId from CSV (or auto‑generated if blank) |
  | `description`              | `string` The product description from the CSV file.                                        |
  | `createDate`               | `datetime` The created date.                                                               |
  | `paymentLinkURL`           | `string` The payment link to share with the customer.                                      |
  | `customerName`             | `string` The customer name.                                                                |
  | `amount`                   | `number` The total amount of the link.                                                     |
  | `active`                   | `boolean` Determines whether the link is active.                                           |
  | `expiry`                   | `datetime` The expiry timestamp of the link.                                               |
  | `isAmountFilledByCustomer` | `boolean` Determines whether the amount is filled by the customer.                         |
  | `isPartialPaymentAllowed`  | `boolean` Determines whether the partial payment is allowed.                               |
  | `status`                   | `string` The status of the payment link.                                                   |
  | `isSplit`                  | `boolean` Determines whether the split payment is enabled.                                 |
  | `currency`                 | `string` The currency of the amount.                                                       |
  | `merchantId`               | `integer` The unique merchant ID.                                                          |
  | `creatorEmail`             | `string` The creator email address.                                                        |
</Accordion>

<Accordion title="Error Response Scenarios" icon="fa-exclamation-triangle">
  | **Error Message**                       | **Description**                                                 |
  | :-------------------------------------- | :-------------------------------------------------------------- |
  | `invalid orderBy`                       | `orderBy` not in the allowed list.                              |
  | `pass valid status param`               | `status` query value not in `active`, `inactive`, or `expired`. |
  | `error occured while bulk paymentLinks` | Server‑side exception                                           |
</Accordion>
