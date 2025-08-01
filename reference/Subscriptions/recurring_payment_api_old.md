---
title: '[Backup]Recurring Payment API'
excerpt: ''
api:
  file: test_si_collection.json
  operationId: RecurringPaymentAPI
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
All successful registration transactions are charged over the recurring interface with server-to-server API without any additional 2FA or the customers’ involvement. This section describes how to achieve the Recurring Transaction for Net Banking, Cards, and UPI through the common platform.

> 📘 Note:
>
> Banks do not support refunds for Net Banking Recurring Payment transactions (or e-NACH transaction) so you will get an error message, “Refund not accepted for txn” or Error 232. For the list of banks supporting e-NACH, refer to Recurring Payments Bank Codes.

> 🚧 Assumptions:
>
> If the merchant has already performed a successful registration transaction with Net Banking/UPI/Card and mihpayid is received in response to the registration transaction captured successfully and mapped to the customer at the merchant’s end.

### Environment

| Test Environment       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)  |
| :--------------------- | :--------------------------------------------------------------- |
| Production Environment | [https://info.payu.in/merchant/](https://info.payu.in/merchant/) |

## Reference Information for Request Parameters

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Reference
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key
      </td>

      <td>
        For more information on how to generate the Key and Salt, refer to any of the following:  

        * **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  
        * **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
      </td>
    </tr>

    <tr>
      <td>
        hash
      </td>

      <td>
        Hash logic for **\_payment** API is:\
        ```
        sha512(key\|command\|var1\|salt) sha512

        ```
      </td>
    </tr>

    <tr>
      <td>
        var1
      </td>

      <td>
        For JSON fields description, refer to [Additional Info. for Recurring Payment APIs](ref:additional-info-for-recurring-payment-apis)
      </td>
    </tr>
  </tbody>
</Table>

## Request Parameters
