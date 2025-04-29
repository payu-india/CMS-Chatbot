---
name: Additional _payment Request Params
---
[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Reference",
    "0-0": "<<glossary:key>>",
    "0-1": "For more information on how to generate the Key and Salt, refer to any of the following:  \n  \n\\- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  \n  \n- **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)",
    "1-0": "<<glossary:hash>>",
    "1-1": "Hash logic for **\\_payment** API is:  \nsha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)  \nFor more information about the hash generation process, refer to [Generate Hash](doc:generate-hash-merchant-hosted).",
    "2-0": "",
    "2-1": ""
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]