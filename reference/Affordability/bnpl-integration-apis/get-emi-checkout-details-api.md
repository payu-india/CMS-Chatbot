---
title: Get EMI Checkout Details API
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
### Environment

|                        |                                                                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Test Environment       | \<[https://test.payu.in/info/linkAndPay/get\_emi\_checkout\_details>](https://test.payu.in/info/linkAndPay/get_emi_checkout_details>) |
| Production Environment | \<[https://info.payu.in/linkAndPay/get\_emi\_checkout\_details>](https://info.payu.in/linkAndPay/get_emi_checkout_details>)           |

## Request Parameters

### Header

The request header contains the following fields:

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Date<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The date and time should be in the GMT time conversion(not the IST). For example, current time in India is 18:00:00 IST, the time in the date header should be 12:30:00 GMT.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Thu, 17 Feb 2022 08:17:59 GMT</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Digest<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Base 64 encode of (sha256 hash of the JSON data (post to server).</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Authorization<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field is in the following format:<br><code>hmac username=&quot;smsplus&quot;, algorithm=&quot;hmac-sha512&quot;, headers=&quot;date digest&quot;, signature=&quot;CkGfgbho69uTMMOGU0mHWf+1CUAlIp3AjvsON9n9/E4=&quot;</code><br>Where the above format includes the following:  </p>
<ul>
<li><strong>username</strong>: The merchant key of the merchant.</li>
<li><strong>algorithm</strong>: This must have the value as <strong>hmac-sha512</strong> that is used for this API</li>
<li><strong>headers</strong>: This must have the value as <strong>date digest</strong></li>

<li><strong>signature</strong>: This must contain the hmacsha512 of (signing_string, merchant_secret), where:<ul>
<li><strong>signing_string</strong>: This is in the &quot;<strong>Date</strong>&quot;+&quot;\n&quot;+&quot;<strong>Digest</strong>&quot; format. Here, the Date and Digest is the same values in the fields listed in this table For example, &quot;Thu, 17 Feb 2022 08:17:59 GMT&quot;&quot;\n&quot;+“vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=“</li>
<li><strong>merchant_secret</strong>: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to <a href="https://docs.payu.in/docs/generate-merchant-key-and-salt-on-payu-dashboard">Generate Merchant Key and Salt on PayU Dashboard</a></li>
</ul>
</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> hmac username=&quot;smsplus&quot;, algorithm=&quot;hmac-sha256&quot;, headers=&quot;date digest&quot;, signature=&quot;zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI=&quot;</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>platformId<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the platform ID and you must include the value as <strong>1</strong>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

#### Required parameters for calculating authorization

- Date
- Authorization

The following sample Java code contains the logic used to encrypt as described in the above table:

```javascript
// date
var date = new Date();
// var date = "Wed, 28 Jun 2023 11:25:19 GMT";
date = date.toUTCString();
 
// authorization
var authorization = getAuthHeader(date);
console.log(authorization);
 
function getAuthHeader(date) {
    var AUTH_TYPE = 'sha512';
    var data = isEmpty(request['data'])?"":request['data'];
    var hash_string = data + '|' + date + '|' + pm.variables.get("merchantSalt");
    console.log("Hash String is ", hash_string);
    var hash = CryptoJS.SHA512(hash_string).toString(CryptoJS.enc.Hex);
    var authHeader = 'hmac username="' + pm.variables.get("merchantKey") + '", ' + 'algorithm="' + AUTH_TYPE + '", headers="date", signature="' + hash + '"'
    return authHeader;
}
 
pm.environment.set('date', date);
pm.environment.set('authorization', authorization);
 
function isEmpty(obj) {
    for(var key in obj) {
        if(obj.hasOwnProperty(key))
        return false;
    }
    return true;
}
```

### Body parameters

| Parameter                                                       | Description                                                                                                                                                                              | Example           |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| bankCode<br /><code>mandatory</code>                            | <code>String</code> Bank/lender code (e.g. LPEMI for cardless EMI).                                                                                                                      | `LPEMI`           |
| key<br /><code>mandatory</code>                                 | `string` The API key generated from the dashboard.                                                                                                                                       | `yFbXg3`          |
| phone<br /><code>mandatory</code>                               | <code>String</code> Customer mobile number for eligibility check.                                                                                                                        | `8178959206`      |
| amount<br /><code>mandatory</code>                              | <code>String</code> Transaction amount for which eligibility is checked.                                                                                                                 | `10000.00`        |
| pg<br /><code>mandatory</code>                                  | <code>String</code> Payment category; use `EMI` for EMI/Link and Pay NTB flow.                                                                                                           | `EMI`             |
| checkCustomerEligibilityWithDetails<br /><code>mandatory</code> | <code>Boolean</code> When true, eligibility is checked using the provided customer details.                                                                                              | `true`            |
| payuToken<br /><code>optional</code>                            | <code>String</code>This parameter must contain is the PayU instrument token for saved card.                                                                                              |                   |
| requestId<br /><code>optional</code>                            | `string` The payment request ID.                                                                                                                                                         | `Testing_111`     |
| userCredentials<br /><code>optional</code>                      | <code>String</code>This parameter must contain an unique user credential mapped against each user, to be passed by the merchant for saved card.                                          | `abc:xyz`         |
| customerDetails<br /><code>mandatory for NTB eligibility</code> | <code>Object</code> Customer onboarding details for NTB eligibility. For more information, refer to [customerDetails JSON Fields Description](#customerDetails-json-fields-description). | See example below |

### customerDetails JSON Fields Description

| Field                                        | Description                                                           | Example      |
| -------------------------------------------- | --------------------------------------------------------------------- | ------------ |
| panNumber<br /><code>mandatory</code>        | <code>String</code> Customer PAN number.                              | EIJPS1234R   |
| dob<br /><code>mandatory</code>              | <code>String</code> Date of birth (DD-MM-YYYY).                       | `14-12-1996` |
| zipcode<br /><code>mandatory</code>          | <code>String</code> Postal zip code.                                  | `411014`     |
| firstName<br /><code>mandatory</code>        | <code>String</code> Customer first name.                              | `Shray`      |
| lastName<br /><code>mandatory</code>         | <code>String</code> Customer last name.                               | `Suri`       |
| bureauPullConsent<br /><code>optional</code> | <code>String</code> Consent for bureau pull (e.g. "true" or "false"). | `false`      |
| gender<br /><code>optional</code>            | <code>String</code> Customer gender.                                  | `Male`       |
| income<br /><code>optional</code>            | <code>String</code> Customer income.                                  | `65000`      |
| employeeType<br /><code>optional</code>      | <code>String</code> Employment type (e.g. Salaried).                  | `Salaried`   |
| abs<br /><code>optional</code>               | <code>String</code> Additional business-specific field if required.   | `Asnw`       |

## Sample request

### Link and Pay Eligibilty

```curl
curl --location 'https://test.payu.in/info/linkAndPay/get_emi_checkout_details' \
--header 'x-credential-username: smsplus' \
--header 'Content-Type: application/json' \
--header 'authorization: hmac username="x0i6r2", algorithm="sha512", headers="date", signature="0e0ebc518c085d8ff49058b7c232bfe2e8779e9e9cafd34a4cdf1c11114035eea75b0e404a9b9e152757dbcc4926f78b6f18ba7f6643e2bf687a65942d3bde38"' \
--header 'date: Mon, 28 Oct 2024 10:34:49 GMT' \
--data '{
  "Key": "yFbXg3",
  "amount": 21,
  "userCredentials": "yFbXg3:test_sud",
  "phone": "9999999999",
  "bankCode": "LAZYPAY",
  "payuToken": null,
  "requestId": "Testing_111"
}'
```

### NTB Eligibility

```curl
curl --location 'https://test.payu.in/info/linkAndPay/get_emi_checkout_details' \
--header 'x-credential-username: smsplus' \
--header 'Content-Type: application/json' \
--header 'authorization: hmac username="x0i6r2", algorithm="sha512", headers="date", signature="0e0ebc518c085d8ff49058b7c232bfe2e8779e9e9cafd34a4cdf1c11114035eea75b0e404a9b9e152757dbcc4926f78b6f18ba7f6643e2bf687a65942d3bde38"' \
--header 'date: Mon, 28 Oct 2024 10:34:49 GMT' \
--data '{
  "bankCode": "LPEMI",
  "phone": "8178959206",
  "amount": "10000.00",
  "pg": "EMI",
  "checkCustomerEligibilityWithDetails": true,
  "customerDetails": {
    "panNumber": "EIJPS1234R",
    "dob": "14-12-1996",
    "zipcode": "411014",
    "firstName": "Shray",
    "lastName": "Suri",
    "bureauPullConsent": "false",
    "gender": "Male",
    "income": "65000",
    "employeeType": "Salaried",
    "abs": "Asnw"
  }
}'
```

<Callout icon="📘" theme="info">
  ### Authorization calculation logic:

  For authorization calculation logic, refer to[ Required parameters for calculating authorization](#required-parameters-for-calculating-authorization).
</Callout>

## Sample response

### Success scenario

```json
{
   "bnpl":{
      "all":[
         {
            "Lazypay":{
               "status":1,
               "kfsLink":"https://",
               "eligible":true,
               "customerLinked":true,
               "PayuToken":"Token12345"
            },
            "Simpl":{
               "status":1,
               "availableBalance":500,
               "kfsLink":"https://",
               "eligible":true,
               "customerLinked":true,
               "PayuToken":"Token78901"
            }
         }
      ]
   }
}
```

### Failure scenario

- Customer eligible but not linked

```json
{
  "httpCode": "200",
  "message": "",
  "status": 1,
  "data": {
    "emi": {
      "ntb": {
        "cardless": {
          "all": {
            "LPEMI": {
              "tenureOptions": {
                "LPEMI12": {
                  "tenure": 12,
                  "maximumAmount": 100000.0,
                  "eligibility": {
                    "status": false,
                    "reason": "Tenure not available"
                  }
                },
                "LPEMI03": {
                  "tenure": 3,
                  "maximumAmount": 60000.0,
                  "eligibility": {
                    "status": true
                  }
                },
                "LPEMI09": {
                  "tenure": 9,
                  "maximumAmount": 100000.0,
                  "eligibility": {
                    "status": false,
                    "reason": "Tenure not available"
                  }
                },
                "LPEMI06": {
                  "tenure": 6,
                  "maximumAmount": 100000.0,
                  "eligibility": {
                    "status": true
                  }
                },
                "LPEMI": {
                  "tenure": 0,
                  "maximumAmount": 100000.0,
                  "eligibility": {
                    "status": false,
                    "reason": "Tenure not available"
                  }
                }
              },
              "eligibility": {
                "status": true
              }
            }
          },
          "hasEligible": true
        }
      }
    }
  }
}
```

- Customer not eligible

```json
{
  "httpCode": "200",
  "message": "",
  "status": 1,
  "data": {
    "emi": {
      "ntb": {
        "cardless": {
          "all": {
            "LPEMI": {
              "tenureOptions": {
                "LPEMI12": {
                  "tenure": 12,
                  "maximumAmount": 100000.0,
                  "eligibility": {
                    "status": false,
                    "reason": "Tenure not available"
                  }
                },
                "LPEMI03": {
                  "tenure": 3,
                  "maximumAmount": 60000.0,
                  "eligibility": {
                    "status": false,
                    "reason": "Tenure not available"
                  }
                },
                "LPEMI09": {
                  "tenure": 9,
                  "maximumAmount": 100000.0,
                  "eligibility": {
                    "status": false,
                    "reason": "Tenure not available"
                  }
                },
                "LPEMI06": {
                  "tenure": 6,
                  "maximumAmount": 100000.0,
                  "eligibility": {
                    "status": false,
                    "reason": "Tenure not available"
                  }
                },
                "LPEMI": {
                  "tenure": 0,
                  "maximumAmount": 100000.0,
                  "eligibility": {
                    "status": false,
                    "reason": "Tenure not available"
                  }
                }
              },
              "eligibility": {
                "status": false,
                "reason": "Use is not eligible for cof product"
              }
            }
          },
          "hasEligible": false
        }
      }
    }
  }
}
```

<br />
