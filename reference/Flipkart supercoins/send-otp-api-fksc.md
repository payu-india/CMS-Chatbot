---
title: Send OTP API - FKSC
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
The **Send OTP** API is used to send the OTP to the customer and then verify the OTP using the **Verify OTP** API. For more information, refer to [Verify OTP API](https://devguide.payu.in/supercoins-pay-integration/rewards-apis/get-token-api-rewards/).

## Request Header

<Table>
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
        Content-Type
        **mandatory**
      </td>

      <td>
        Indicates the format in which the request is sent.
      </td>

      <td>
        application/json
      </td>
    </tr>

    <tr>
      <td>
        clientType
      </td>

      <td>
        Pass the type of client making the request and in this case, it is **loyalty**.
      </td>

      <td>
        loyalty
      </td>
    </tr>

    <tr>
      <td>
        Origin
      </td>

      <td>
        Pass the origin URL (the domain) from which the request is being made.
      </td>

      <td>
        [https://staging-rewards-api.payu.in'](https://staging-rewards-api.payu.in')
      </td>
    </tr>

    <tr>
      <td>
        Referer
      </td>

      <td>
        Pass the URL that the client was on when the request was done.
      </td>

      <td>
        [https://staging-rewards-api.payu.in/](https://staging-rewards-api.payu.in/)
      </td>
    </tr>
  </tbody>
</Table>

## Request Parameters

The request contains the **data** parameter in a JSON format similar to the following:

```plaintext
{"mobileNumber":"8076499393"}
```

## Sample Request

```curl
curl 'https://sandbox.payu.in/otp/send' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Content-Type: application/json' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36' \
  -H 'clientType: loyalty' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'Origin: https://staging-rewards-api.payu.in' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://staging-rewards-api.payu.in/' \
  -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
  --data-raw '{"mobileNumber":"8076499393"}' \
  --compressed
```

## Response Parameters

| **Parameter**   | **Description**                                                                                                                                                                                                                              |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| httpStatusCode  | The status code indicates whether the API was successful.                                                                                                                                                                                    |
| responseCode    | The response code indicates whether the OTP was successfully sent or not failed to send the OTP.                                                                                                                                             |
| responseMessage | The response message indicates whether the OTP was successfully sent or failed to send the OTP.                                                                                                                                              |
| uuid            | The UUID (Universally unique identifier) of the customer. This must be used in the Verify OTP API. For more information, refer to [Verify OTP API](https://devguide.payu.in/supercoins-pay-integration/rewards-apis/get-token-api-rewards/). |

## Sample Response

```plaintext
{"httpStatusCode":200,"responseCode":10,"responseMessage":"Send Otp Success","uuid":"1061094686780890066"}
```
