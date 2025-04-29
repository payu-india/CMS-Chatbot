---
title: Account Discovery API
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
This API is to validate if user's account/customer profile exists or not with the merchant basis mobile number or email id identifiers.

## Request parameters

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
        phone
        `mandatory`
      </td>

      <td>
        The customer phone number.
      </td>
    </tr>

    <tr>
      <td>
        email\
        `mandatory`
      </td>

      <td>
        The customer email ID.
      </td>
    </tr>

    <tr>
      <td>
        key\
        `mandatory`
      </td>

      <td>
        The merchant key used for encryption that was provided by PayU.
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```
curl --location -g --request POST 'https://{host}/payu/accountDiscovery' \
--header 'Content-Type: application/json' \
--data-raw '{
    "phone": "12345678",//AES encrypted
    "email": "jagadesh@reddy.com", //AES encrypted
    "key": "encryption key"
}'
```

## Sample response

```
{
    "success": true|false,
    "data":{
      "customerId": "jagadesh33445"
      },
    "message": "SUCCESS"
}
```
