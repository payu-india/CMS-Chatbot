---
name: Key/Hash for General Parameters Description
---
[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Reference",
    "0-0": "<<glossary:key>>",
    "0-1": "For more information on how to generate the Key and Salt, refer to any of the following:  \n  \n- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)\n\n- **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)",
    "1-0": "<<glossary:hash>>",
    "1-1": "Hash logic for this API is:  \n`sha512(key\\|command\\|var1\\|salt) sha512`"
  },
  "cols": 2,
  "rows": 2,
  "align": [
    "left",
    "left"
  ]
}
[/block]