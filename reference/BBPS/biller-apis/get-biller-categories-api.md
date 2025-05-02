---
title: Get Biller Categories API
excerpt: ''
api:
  file: bbps-apis-agent-share-3.json
  operationId: GetBillerCategories
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# Get Biller Categories

The **Get Biller Categories** API will fetch all the categories from PayU.


> 📘 Note:
>
> Send the scope of the GET Token API as **read_biller_categories** to obtain the access_token for this request. For more information, refer to [Get Token API - BBPS](ref:get-token-api-bbps).

<details>
  <summary>Sample request</summary>

```
curl --location -g --request GET 'https://{{host_name}}/payu-nbc//v1/getbillercategory' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}'
```

</details>

<details>
  <summary>Response parameters</summary>

<Table>
  <thead>
    <tr>
      <th>
        Field Name
      </th>
      <th>
        Description
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        code
      </td>
      <td>
        The global response code and can be any of the following:  

        * **0**: If web service call failed
        * **1**: if web service call succeeded
      </td>
    </tr>
    <tr>
      <td>
        status
      </td>
      <td>
        The status of the API command and can be any of the following:  

        * SUCCESS
        * FAILURE
      </td>
    </tr>
    <tr>
      <td>
        payload
      </td>
      <td>
        It will contain a list of biller categories. For more information, refer to the payload table below.
      </td>
    </tr>
  </tbody>
</Table>

### payload

<Table>
  <thead>
    <tr>
      <th>
        Field Name
      </th>
      <th>
        Description
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colSpan="2">
        **Success Scenarios**
      </td>
    </tr>
    <tr>
      <td>
        billerCategories
      </td>
      <td>
        This field contains the biller categories in an array format.
      </td>
    </tr>
    <tr>
      <td colSpan="2">
        **Failure Scenarios**
      </td>
    </tr>
    <tr>
      <td>
        refId
      </td>
      <td>
        For failure scenarios, This parameter contains the reference ID.  

        **Note**: In case of category fetch refId will be null.
      </td>
    </tr>
    <tr>
      <td>
        type
      </td>
      <td>
        For failure scenarios, this field contains the type of error.
      </td>
    </tr>
    <tr>
      <td>
        code
      </td>
      <td>
        The global response code
      </td>
    </tr>
    <tr>
      <td>
        payload
      </td>
      <td>
        It will contain payload with error messages.
      </td>
    </tr>
    <tr>
      <td>
        status
      </td>
      <td>
        The status of the response. Example, SUCCESS/FAILURE
      </td>
    </tr>
    <tr>
      <td>
        message
      </td>
      <td>
        For failure scenarios, this field contains the description of error type for failure or success.
      </td>
    </tr>
    <tr>
      <td>
        errors
      </td>
      <td>
        For failure scenarios, this field contains the following in the response:  

        * **reason**: The error description if the request has failed.
        * **errorCode**: The error code of the error if the request has failed
      </td>
    </tr>
    <tr>
      <td>
        additionalParams
      </td>
      <td>
        For failure scenarios, this field contains the additional fields (if any) related to billers in an array format.
      </td>
    </tr>
  </tbody>
</Table>

</details>

<details>
  <summary>Sample response</summary>

### Success scenario

```json
{ 
  "code": 200, 
  "status": "SUCCESS", 
  "payload": { 
    "billerCategories": [ 
      "INSURANCE", 
      "LOAN", 
      "EDUCATION", 
      "SOCIETY BILLER" 
    ] 
  } 
}
```

### Failure scenario

```json
{ 
  "code": 600, 
  "status": "FAILURE", 
  "payload": { 
    "errors": [ 
      { 
        "reason": "<error message>", 
        "errorCode": "<error code>" 
      } 
    ], 
    "refId": null, 
    "type": "category_response", 
    "message": "category_response_failed",
    "additionalParams": { 
      "Key1": "value1", 
      "Key2": "value2", 
      "Key3": "value3"
    } 
  } 
} 
```

</details>

## Request Parameters

No request parameters input required for this API.