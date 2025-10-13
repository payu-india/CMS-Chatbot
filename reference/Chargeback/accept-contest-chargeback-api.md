---
title: Accept/Contest Chargeback API
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
The **Accept/Reject Chargeback** API allows the merchant user to accept the chargeback by providing the appropriate reasons in the request body against the chargeback and merchant ID. The API supports file uploads through base64 encoding directly in the JSON payload.

HTTP Method: **PATCH**

<ChargebackEnvironment />

## Request parameters

### Request header

| Parameter           | Description                     |
| ------------------- | ------------------------------- |
| `X-Optimus-API-Key` | Merchant authentication key     |
| `Content-Type`      | Must be set to application/json |

This must contain the header with token you get using the Get Token API in the following format:

```
\--header 'X-Optimus-API-Key: <Bearer token>'
```

### Request body

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
        chargeback_id
        `mandatory`
      </td>

      <td>
        `String` The ID of the chargeback to respond to
      </td>
    </tr>

    <tr>
      <td>
        merchant_key
        `mandatory`
      </td>

      <td>
        `String`Key of merchant
      </td>
    </tr>

    <tr>
      <td>
        dispute_type
        `mandatory`
      </td>

      <td>
        `String`Types of response: `accept`, `contest`. For the dispute_type as  `partially_accept` or `contest`, refer to the notes in the

        [File upload fields](#file-upload-fields)

        table
      </td>
    </tr>

    <tr>
      <td>
        reason_code
        `mandatory`
      </td>

      <td>
        `Array` An array of reason codes with form data. For more information, refer to

        [ Reason code structure](#reason-code-structure)

        .
      </td>
    </tr>
  </tbody>
</Table>

#### Reason code structure

The parameter must be an array of objects with the following structure:

```json
[
  {
    "uuid": "reason-uuid",
    "form_data": [
      {
        "identifier": "form-field-uuid",
        "value": "field-value"
      }
      // Additional form fields...
    ]
  }
  // Additional reasons if applicable...
]
```

#### File upload fields

For file upload fields (identified by `tag_type: "file_tag"` in the system):

```json
{
  "identifier": "file-field-uuid",
  "value": "BASE64_ENCODED_FILE_CONTENT",
  "filename": "evidence.pdf",
  "content_type": "application/pdf"
}
```

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        identifier
        `mandatory`
      </td>

      <td>
        UUID of the file field
      </td>
    </tr>

    <tr>
      <td>
        value
        `mandatory`
      </td>

      <td>
        Dependent on response received from the Read Reasons API, the Value(evidence) to be submitted for accepting/contesting the chargeback, for a particular reason code(UUID), should be text(plain text), image(png ,jpeg/jpg) or file(doc,docx,pdf). This is Base-64 encoded.
      </td>
    </tr>

    <tr>
      <td>
        filename
        `mandatory`
      </td>

      <td>
        Original filename with extension.
        **Notes**:

        * The file size limit is 5MB per file.
        * File uploads are processed as base64 encoded strings directly in the JSON payload. Do not use multipart/form-data.
        * When using `partially_accept` as the dispute type, you must include a form field with  the value (amount) that is less than the total chargeback amount and greater than 0.
        * Each form field has a specific UUID that must be used correctly for the system to process your response.
        * Do not upload file for when using `accept` as the dispute type.
      </td>
    </tr>

    <tr>
      <td>
        content_type
        `mandatory`
      </td>

      <td>
        MIME type of the file
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

### Accept a Chargeback

```bash
curl --location --request PATCH 'https://bankportal.payu.in/api/v1/chargebacks/dispute' \
--header 'X-Optimus-API-Key: MERCHANT KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "reason_code": [
    {
      "uuid": "bb10e1bb-f128-4ace-ab0f-59881f11fa4d",
      "form_data": [
        {
          "identifier": "bb10e1bb-f128-4ace-ab0f-59881f11fa4d",
          "value": "We accept this chargeback due to service issue."
        }
      ]
    }
  ],
  "chargeback_id": "1128897",
  "merchant_key": "2WEDS",
  "dispute_type": "accept"
}'
```

### Contest a Chargeback with file evidence

```bash
curl --location --request PATCH 'https://bankportal.payu.in/api/v1/chargebacks/dispute' \
--header 'X-Optimus-API-Key: MERCHANT KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "reason_code": [
    {
      "uuid": "cc20e2cc-f238-5bdf-ab0f-59881f11fa4e",
      "form_data": [
        {
          "identifier": "cc20e2cc-f238-5bdf-ab0f-59881f11fa4e",
          "value": "We are contesting this chargeback. Please see attached proof of delivery."
        },
        {
          "identifier": "200edfd3-84b6-4311-8486-23887f167772",
          "value": "BASE64_ENCODED_FILE_CONTENT_HERE",
          "filename": "delivery_proof.pdf",
          "content_type": "application/pdf"
        }
      ]
    }
  ],
  "chargeback_id": "1128897",
  "merchant_key": "2WEDS",
  "dispute_type": "contest"
}'
```

### Partially accept a Chargeback

```bash
curl --location --request PATCH 'https://bankportal.payu.in/api/v1/chargebacks/dispute' \
--header 'X-Optimus-API-Key: MERCHANT KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "reason_code": [
    {
      "uuid": "dd30e3dd-f348-6ceg-ab0f-59881f11fa4f",
      "form_data": [
        {
          "identifier": "6f92dad0-4446-4465-bfea-17f587e973d4",
          "value": "500.00"
        },
        {
          "identifier": "dd30e3dd-f348-6ceg-ab0f-59881f11fa4f-comments",
          "value": "We can partially refund as customer was charged for premium service but received standard service."
        }
      ]
    }
  ],
  "chargeback_id": "1128897",
  "merchant_key": "2WEDS",
  "dispute_type": "partially_accept"
}'
```

## Response parameters

| Parameter  | Description                                                                                                                                                                |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id         | This parameter contains the  chargeback ID.                                                                                                                                |
| type       | The parameter contains the **chargeback-details** as type. For the list of chargeback type, refer to [Chargeback Types](doc:chargeback-types).                             |
| attributes | This parameter contains the chargeback details in a JSON format. For more information, refer to  [attributes JSON field descriptions](attributes-json-field-descriptions). |

### attributes JSON field descriptions

| Field   | Description                                                                                                                                                           | Example            |
| :------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------- |
| id      | This field contains the  chargeback ID.                                                                                                                               | 1035881            |
| payu-id | The field contains the PayU ID of the merchant.                                                                                                                       | 15420278029        |
| status  | This field contains the status of the chargeback. For the list of chargeback states, refer to [Chargeback Status List](https://docs.payu.in/docs/chargeback-status) . | Pending Doc Review |

## Sample response

### Success scenario

```json
{
    "data": {
        "id": "1035881",
        "type": "chargeback-details",
        "attributes": {
            "id": 1035881,
            "payu-id": "15420278029",
            "status": "Pending Doc Review"
        }
    }
}
```
