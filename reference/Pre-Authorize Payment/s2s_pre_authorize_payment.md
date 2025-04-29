---
title: S2S - Pre-Authorize Payment
excerpt: ''
api:
  file: payment-api-7.json
  operationId: S2SPre-AuthorizePayment
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **pre\_authorize** parameter is used to pre-authorize payments using the S2S integration along with the parameters to collect card details and S2S parameters.

## Reference info for request parameters

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>
      <th>
        **Reference**
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        key
      </td>
      <td>
        The merchant key provided by PayU while onboarding.\
        For more information on how to generate the Key and Salt, refer to any of the following:  
        * **Production**: [Generate Merchant Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard)  
        * **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
      </td>
    </tr>
    <tr>
      <td>
        hash
      </td>
      <td>
        Hash logic for \_payment API is:\
        ```
        sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\||\||\||SALT) 
        ```
        For more information about the hash generation process, refer to \~\~ Generate Hash\~\~.
      </td>
    </tr>
  </tbody>
</Table>

## Request parameters

> 📘 Reference:
>
> Use the card details as follows: cccnum=5123456789012346, ccexpmon=11, ccexpyr=2025, ccvv=123 and OTP =123456 (displayed in Simulator page).