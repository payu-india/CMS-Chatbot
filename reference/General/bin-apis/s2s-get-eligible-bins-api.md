---
title: S2S Get Eligible BINs API
excerpt: 'API Command: s2sEligibleBins'
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The S2S Eligible BINs API (**s2sEligibleBins**) API is similar to the **Get BIN Info** API, but used in S2S environment. For more information on Get BIN Info API, refer to [Get Bin Info API](ref:get_bin_info_api).

**Environment**

|                        |                                                    |
| :--------------------- | :------------------------------------------------- |
| Production Environment | <https://info.payu.in/merchant/postservice?form=2> |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Reference",
    "0-0": "key  \n`mandatory`",
    "0-1": "For more information on how to generate the Key and Salt, refer to any of the following:  \n  \n- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  \n- **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)",
    "1-0": "var1  \n`mandatory`",
    "1-1": "Specify the value as \"**2**\" for S2S flow.",
    "2-0": "var2  \n`mandatory`",
    "2-1": "Specify any of the following values in this field based on the output you required:  \n  \n- 1: Specify this value if a single bin-level information is required. Output contains the information on a single bin only.  \n- 2: Specify this value if a specific feature-level information is required. Output would give the bin list.  \n- 3: Specify this value if all the bins and their information are required",
    "3-0": "var3  \n`optional`",
    "3-1": "Specify the bank Name to be passed to get Bins of specific Bank.",
    "4-0": "var4  \n`optional`",
    "4-1": "Specify the categories of thecCard need to be passed. For example, **creditcard**.",
    "5-0": "var5  \n`optional`",
    "5-1": "Specify the card schemes should be passed in this field. For example; **VISA**,** MAST**.",
    "6-0": "hash  \n`mandatory`",
    "6-1": "The hash logic that must be used by merchants to calculate the hash:  \nHash logic for this API is:  \n`sha512(key\\|command\\|var1\\|salt) sha512\n`"
  },
  "cols": 2,
  "rows": 7,
  "align": [
    "left",
    "left"
  ]
}
[/block]

## Sample request

```
curl --location 'https://info.payu.in/merchant/postservice.php?form=2' \
--form 'key="smsplus"' \
--form 'command="s2sEligibleBins"' \
--form 'var1="2"' \
--form 'var2="1"' \
--form 'var3="KOTAK"' \
--form 'var4="debitcard"' \
--form 'var5="RUPAY"' \
--form 'hash="aksduhfksdjhjkdskkfdsjkdfkjshfkjhadsjkfsdfsdf"'
```

## Sample response

```
{
   "data":[
      {
         "issuingBank":"HDFC",
         "schemes":[
            {
               "scheme":"MAST",
               "categories":[
                  {
                     "bins":[
                        "515470517",
                        "51166608",
                        "515470541"
                     ],
                     "category":"creditcard"
                  },
                  {
                     "bins":[
                        "535375995",
                        "535376757",
                        "54191904"
                     ],
                     "category":"debitcard"
                  }
               ]
            },
            {
               "scheme":"VISA",
               "categories":[
                  {
                     "bins":[
                        "478971945",
                        "432001408",
                        "434415570"
                     ],
                     "category":"debitcard"
                  }
               ]
            },
            {
               "scheme":"RUPAY",
               "categories":[
                  {
                     "bins":[
                        "652166040",
                        "607311",
                        "65254243"
                     ],
                     "category":"debitcard"
                  }
               ]
            }
         ]
      }
   ],
   "statusCode":200
}
```