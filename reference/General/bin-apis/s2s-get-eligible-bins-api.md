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

## Environment

| Environment            | URL                                                                                                  |
| :--------------------- | :--------------------------------------------------------------------------------------------------- |
| Production Environment | [https://info.payu.in/merchant/postservice?form=2](https://info.payu.in/merchant/postservice?form=2) |

## Request parameters

<Table>
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
        `mandatory`
      </td>

      <td>
        For more information on how to generate the Key and Salt, refer to any of the following:  - **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard) - **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
      </td>
    </tr>

    <tr>
      <td>
        var1
        `mandatory`
      </td>

      <td>
        Specify the value as "**2**" for S2S flow.
      </td>
    </tr>

    <tr>
      <td>
        var2
        `mandatory`
      </td>

      <td>
        Specify any of the following values in this field based on the output you required: - 1: Specify this value if a single bin-level information is required. Output contains the information on a single bin only. - 2: Specify this value if a specific feature-level information is required. Output would give the bin list. - 3: Specify this value if all the bins and their information are required
      </td>
    </tr>

    <tr>
      <td>
        var3
        `mandatory`
      </td>

      <td>
        Specify the bank Name to be passed to get Bins of specific Bank.
      </td>
    </tr>

    <tr>
      <td>
        var4
        `mandatory`
      </td>

      <td>
        Specify the categories of the card need to be passed. For example, **creditcard**.
      </td>
    </tr>

    <tr>
      <td>
        var5
        `mandatory`
      </td>

      <td>
        Specify the card schemes should be passed in this field. For example; **VISA**, **MAST**.
      </td>
    </tr>

    <tr>
      <td>
        hash
        `mandatory`
      </td>

      <td>
        The hash logic that must be used by merchants to calculate the hash:
        Hash logic for this API is:
        <code>sha512(key|command|var1|salt) sha512</code>
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```bash
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

```json
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