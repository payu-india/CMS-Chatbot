---
title: v2 Validate VPA API
deprecated: false
hidden: false
metadata:
  robots: index
---
This API allows merchants to validate a UPI (Unified Payment Interface) Virtual Payment Address.

HTTP Request Method: GET

## Endpoint

* **Production Environment**: `https://info.payu.in/payment-mode/v1/upi/vpa`

## Request Headers

The request header contains the following fields:

| Field                     | Description                           | Example                                                                                                                                                                                                   |
| ------------------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Content-Type `mandatory`  | The content type for the API request. | application/json                                                                                                                                                                                          |
| Date `mandatory`          | The date and time in GMT format.      | Tue, 17 Jun 2025 06:48:55 GMT                                                                                                                                                                             |
| Authorization `mandatory` | Authentication signature for the API. | hmac username="smsplus", algorithm="sha512", headers="date", signature="b4db4b20d1d9146edfd846fc11c2145ab1ac99c001df5923e3a412672f577b73f3b2cee4dc492f18ea55a0be8a4ec9f0df4475ad6eb03bedc0c6ef46235f0ed7" |

## Request Parameters

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

## Sample Request (cURL)

```bash
curl --location 'https://info.payu.in/payment-mode/v1/upi/vpa?isAutoVPAValid=true&vpa=ridhigarg95@okicici' \
--header 'Content-Type: application/json' \
--header 'date: Tue, 17 Jun 2025 06:48:55 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="b4db4b20d1d9146edfd846fc11c2145ab1ac99c001df5923e3a412672f577b73f3b2cee4dc492f18ea55a0be8a4ec9f0df4475ad6eb03bedc0c6ef46235f0ed7"'
```

## Sample Response

```json
{
    "message": "Success",
    "status": 1,
    "result": {
        "isValidVpa": true,
        "payerAccountName": "RIDHI GARG",
        "vpa": "ridhigarg95@okicici",
        "isAutoPayVPAValid": true
    }
}
```

## Response Parameters

| Parameter                  | Description                                                      | Example               |
| -------------------------- | ---------------------------------------------------------------- | --------------------- |
| `message`                  | Response message indicating the operation result.                | `Success`             |
| `status`                   | Status code for the operation. `1` for success, `0` for failure. | `1`                   |
| `result.isValidVpa`        | Indicates whether the provided VPA is valid.                     | `true`                |
| `result.payerAccountName`  | Name associated with the VPA.                                    | `RIDHI GARG`          |
| `result.vpa`               | The validated VPA.                                               | `ridhigarg95@okicici` |
| `result.isAutoPayVPAValid` | Indicates whether the VPA is valid for auto-pay.                 | `true`                |