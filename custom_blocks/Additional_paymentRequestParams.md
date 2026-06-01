---
name: Additional_paymentRequestParams
---
<Accordion title="Additional info for Request parameters" icon="fa-info-circle">
  | Parameter | Reference |
|-----------|-----------|
| `key` | For more information on how to generate the Key and Salt, refer to any of the following:<br/>• **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)<br/>• **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt) |
| `hash` | Hash logic for **\_payment** API is:<br/>`sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)`<br/>For more information about the hash generation process, refer to [Generate Hash](doc:generate-hash-merchant-hosted). |
</Accordion>

> 📘
>
> **Reference**: For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

<br />
