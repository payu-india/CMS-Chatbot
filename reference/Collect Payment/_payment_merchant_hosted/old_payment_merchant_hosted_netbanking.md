---
title: '[BCKUP]Net Banking'
excerpt: ''
api:
  file: merchant-hosted-14.json
  operationId: MerchantHostedCheckout-NetBanking
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Collect payments using Net Banking with Merchant Hosted Checkout integration as described in this section. After collecting the details from the customer, make the transaction request with the payment details to PayU.

## Check Net Banking health

You can check whether the Net Banking server is up and running using the **getNetBankingStatus** API. If the Net Banking server is down for a bank, you can inform your customers that the Net Banking server is down. For more information on the **getNetBankingStatus** API, refer to getNetBankingStatus.

<PaymentAPIEnvironment />

## Additional info for request parameters

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>key</td>
      <td>
        For more information on how to generate the Key and Salt, refer to any of the following:

        * **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
        * **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
      </td>
    </tr>
    <tr>
      <td>hash</td>
      <td>
        Hash logic for **\_payment** API is:\
        sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)\
        For more information about the hash generation process, refer to [Generate Hash](doc:generate-hash-merchant-hosted).
      </td>
    </tr>
  </tbody>
</Table>

## Request parameters

> 📘 Reference:
>
> For the response parameters description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis#response-parameters).

> ❗️ Error Handling
>
> If any error message is displayed with an error code, refer to the <a href="error-codes" target="_blank">Error Codes</a> section to understand the reason for these error codes.

> 🚧 Values to be used in Test environment
>
> You can test NetBanking only with pg=**TESTPG** and bankcode=**TESTPGNB** only.