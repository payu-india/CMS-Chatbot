---
excerpt: ''
api:
  file: bbps-apis-agent-share-8.json
  operationId: heartBeatAPI
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Check Health Status** API can be used to check the working status of the PayU server.

|            |                                                                                      |
| :--------- | :----------------------------------------------------------------------------------- |
| Production | [https://bbps-sb.payu.in/payu-nbc/v1/nbc/](https://bbps-sb.payu.in/payu-nbc/v1/nbc/) |

<Callout icon="📘" theme="info">
  ### Note:

  Send the scope of the GET Token API as check\_health\_status to obtain the access\_token for this request. For more information, refer to [Get Token API - BBPS](ref:get-token-api-bbps).
</Callout>

<details>
  <summary>Sample request</summary>

```curl
curl --location --request POST 'https://<hostName>/payu-nbc/v1/nbc/heartBeat?agentId=`{agentId}`&refId=`{refId}`' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <token>'
```

</details>

<details>
  <summary>Response parameters</summary>

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

        - **0**: If web service call failed
        - **1**: if web service call succeeded
      </td>
    </tr>

    <tr>
      <td>
        status
      </td>

      <td>
        The status of the API command and can be any of the following:

        - SUCCESS
        - FAILURE
      </td>
    </tr>

    <tr>
      <td>
        payload
      </td>

      <td>
        It will contain a list of biller categories. For more information, refer to the [payload](#payload) table.<br />If the transaction had failed, it will contain:

        - additional data related to transactions
        - List of errors which caused failure transactions
      </td>
    </tr>
  </tbody>
</Table>

### payload

<Table>
  <thead>
    <tr>
      <th>
        **Paramater**
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
        This parameter can contain any of the following:

        - UP
        - DOWN
      </td>
    </tr>

    <tr>
      <td>
        type
      </td>

      <td>
        This field contains the the type of request.
      </td>
    </tr>

    <tr>
      <td>
        refId
      </td>

      <td>
        This field contains the reference ID received in request from the agent.
      </td>
    </tr>

    <tr>
      <td>
        payuId
      </td>

      <td>
        It will be payU system ID and it will be unique every time.
      </td>
    </tr>

    <tr>
      <td>
        message
      </td>

      <td>
        For failure scenario, this field contains the message as **heart\_beat\_failure**.
      </td>
    </tr>

    <tr>
      <td>
        errors
      </td>

      <td>
        For failure scenario, the errors are displayed in an array format.
      </td>
    </tr>
  </tbody>
</Table>

</details>

<details>
  <summary>Sample response</summary>

### Success scenario

```
{
  "code": 200,
  "status": "SUCCESS",
  "payload": {
    "refId": "<refId>",
    "status": "UP",
    "payuId": "<payUSytemId>"
  }
}
```

### Failure scenario

```
{
  "code": 600,
  "status": "FAILURE",
  "payload": {
    "errors": [
      {
        "reason": "<error reason>",
        "errorCode": "<error code>"
      }
    ],
    "refId": "<refId>",
    "type": "heart_beat",
    "message": "heart_beat_failed",
    "additionalParams": null
  }
}
```

</details>

## Request parameters

<br />
