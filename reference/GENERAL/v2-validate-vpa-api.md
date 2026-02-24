---
title: Validate VPA API
deprecated: false
hidden: false
metadata:
  robots: index
---
This API allows merchants to validate a UPI (Unified Payment Interface) Virtual Payment Address.

HTTP Request Method: GET

**Environment**

|            |                                                                                            |
| :--------- | :----------------------------------------------------------------------------------------- |
| Production | [https://info.payu.inpayment-mode/v1/upi/vpa](https://info.payu.inpayment-mode/v1/upi/vpa) |
| Test       | [https://info.payu.inpayment-mode/v1/upi/vpa](https://info.payu.inpayment-mode/v1/upi/vpa) |

## Request headers

<V2_payment_header_params />

## Request body

<Table>
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
        isAutoVPAValid
        `mandatory`
      </td>

      <td>
        `Boolean` Determines whether to check for auto-pay VPA validation.
      </td>
    </tr>

    <tr>
      <td>
        vpa
        `mandatory`
      </td>

      <td>
        `String` The UPI Virtual Payment Address to be validated.
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```bash
curl --location 'https://info.payu.in/payment-mode/v1/upi/vpa?isAutoVPAValid=true&vpa=test@payu' \
--header 'Content-Type: application/json' \
--header 'date: Tue, 17 Jun 2025 06:48:55 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="b4db4b20d1d9146edfd846fc11c2145ab1ac99c001df5923e3a412672f577b73f3b2cee4dc492f18ea55a0be8a4ec9f0df4475ad6eb03bedc0c6ef46235f0ed7"'
```

## Sample response

```json
{
    "message": "Success",
    "status": 1,
    "result": {
        "isValidVpa": true,
        "payerAccountName": "Test",
        "vpa": "test@payu",
        "isAutoPayVPAValid": true
    }
}
```

## Response parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        message
      </td>

      <td>
        Response message indicating the operation result.
      </td>

      <td>
        Success
      </td>
    </tr>

    <tr>
      <td>
        status
      </td>

      <td>
        Status code for the operation. It can be any of the following:

        * `1` for success
        * `0` for failure.
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        result
      </td>

      <td>
        The result of the response in a JSON format. For more information, refer [result JSON fields description](#result-json-fields-description)
      </td>

      <td>
        true
      </td>
    </tr>
  </tbody>
</Table>

### result JSON fields description

| Parameter         | Description                                      | Example             |
| ----------------- | ------------------------------------------------ | ------------------- |
| isValidVpa        | Indicates whether the provided VPA is valid.     | true                |
| payerAccountName  | Name associated with the VPA.                    | RIDHI GARG          |
| vpa               | The validated VPA.                               | ridhigarg95@okicici |
| isAutoPayVPAValid | Indicates whether the VPA is valid for auto-pay. | true                |
