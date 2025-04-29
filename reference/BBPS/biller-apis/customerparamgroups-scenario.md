---
title: CustomerParamGroups Scenario
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **customerParamGroups** tag in the Biller MDM Response returns the possible groups in which customer can share the input . This should be handled by agents for billers, when all parameters in **customerParams** tag has optional field as true.

For example, if the biller Indian Oil Corporation Limited, has **customerParams** tag similar to following:

```
[
   {
      "paramName":"Mobile Number",
      "dataType":"NUMERIC",
      "optional":true,
      "minLength":10,
      "maxLength":10,
      "minValue":null,
      "maxValue":null,
      "regex":"^[0-9]{10}$",
      "values":null
   },
   {
      "paramName":"Consumer Number",
      "dataType":"ALPHANUMERIC",
      "optional":true,
      "minLength":1,
      "maxLength":10,
      "minValue":null,
      "maxValue":null,
      "regex":"^[0-9A-Za-z]{1,10}$",
      "values":null
   },
   {
      "paramName":"Distributor Code",
      "dataType":"NUMERIC",
      "optional":true,
      "minLength":6,
      "maxLength":6,
      "minValue":null,
      "maxValue":null,
      "regex":"^[0-9]{6}$",
      "values":null
   },
   {
      "paramName":"Consumer ID",
      "dataType":"NUMERIC",
      "optional":true,
      "minLength":16,
      "maxLength":16,
      "minValue":null,
      "maxValue":null,
      "regex":"^[0-9]{16}$",
      "values":null
   }
]
```

Here, all parameters have optional as true, so the groups should be made as per the **customerParamGroups** tag value similar to the following:

```
{
   "customerParamGroups":[
      {
         "params":[
            "Mobile Number"
         ],
         "name":"Group1",
         "input":"1",
         "groups":[
            {
               "params":[
                  "Consumer Number",
                  "Distributor Code"
               ],
               "name":"Group1.1",
               "input":"2",
               "groups":[
                  
               ]
            },
            {
               "params":[
                  "Consumer ID"
               ],
               "name":"Group1.2",
               "input":"1",
               "groups":[
                  
               ]
            }
         ]
      }
   ]
}
```

In the scenario, the customer can pass inputs in any of the following groups:

* “Mobile Number”
* “Consumer Number” and “Distributor Code”
* “Consumer ID”
