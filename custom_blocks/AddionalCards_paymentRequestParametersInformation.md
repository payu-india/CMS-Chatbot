---
name: Addional Cards _payment Request Parameters Information
---
[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Reference",
    "0-0": "<<glossary:key>>",
    "0-1": "For more information on how to generate the Key and Salt, refer to any of the following:  \n  \n\\- **Production**: [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  \n  \n- **Test**: [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)",
    "1-0": "<<glossary:hash>>",
    "1-1": "Hash logic for **\\_payment** API is:  \nsha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)  \nFor more information about the hash generation process, refer to [Generate Hash](doc:generate-hash-merchant-hosted).  \n**Note**: Hash logic for \\_payment API version 19:  \n  \nThe following hash logic must be used for \\_payment API with** api_version=19**:  \n`key\\|txnid\\|amount\\|productinfo\\|firstname\\|email\\|udf1\\|udf2\\|udf3\\|udf4\\|udf5\\|udf6\\|udf7\\|udf8\\|udf9\\|udf10\\|user_token\\|offer_key\\|offer_auto_apply\\|cart_details\\|extra_charges\\|phone`",
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


> 📘 Note:
> 
> The following parameters are mandatory for Cross-Border Payments in addition to user-defined parameters specified above:  firstname, lastname, address1, city, state, country and zipcode.