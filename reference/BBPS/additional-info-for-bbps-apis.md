---
title: Additional Info for BBPS APIs
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Response Parameters for Get Token API

| **Field Name** | **Description**                                               |
| -------------- | ------------------------------------------------------------- |
| access\_token  | The access token for the validation  for all subsequent apis. |
| token\_type    | The token type and It will always be **Bearer**.              |
| expires\_in    | The expiry time for the token will be in seconds.             |
| scope          | The scope for which the token is applicable for.              |
| created\_at    | The time stamp when the token was created in UNIX format.     |

### Sample Response

* Success scenario

```plaintext
{
  "access_token": "82c38b64e072f3d64da6e4e6efee9789ffe1250f0cd04c20753d6e6f25df9cc7",
  "token_type": "Bearer",
  "expires_in": 7200,
  "scope": "read_transactions",
  "created_at": 1595411399
}
```

* Failure scenario

```plaintext
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
    "message": "category_response_failed" 
    "additionalParams":{ 
           "Key1": "value1" 
           "Key2": "value2" 
           "Key3": "value3" 
     } 
  } 
} 
```

## Response Parameters for Get Biller Categories API

<Table>
  <thead>
    <tr>
      <th>
        **Field Name**
      </th>

      <th>
        **Description**
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
        It will contain a list of biller categories. For more information, refer to [payload](https://devguide.payu.in/recharge-api-integration/biller-apis-recharge-api-integration/get-biller-categories/#payLoad).
      </td>
    </tr>
  </tbody>
</Table>

### payload

<Table>
  <thead>
    <tr>
      <th>
        **Field Name**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Success Scenarios**
      </td>

      <td>

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
      <td>
        **Failure Scenarios**
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        refId
      </td>

      <td>
        For failure scenarios, This parameter contains the reference ID.  

        * \*Note\*\*: In case of category fetch refId will be null.
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

### Sample response

* Success scenario

```plaintext
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

* Failure scenario

```plaintext
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
    "message": "category_response_failed" 
    "additionalParams":{ 
           "Key1": "value1" 
           "Key2": "value2" 
           "Key3": "value3" 

     } 
  } 
 
} 
```
