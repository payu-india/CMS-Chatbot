---
title: 'NTB EMI - Link and Pay with Merchant '
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Get EMI Checkout Details (Link and Pay) API
excerpt: Accepts customer details from the merchant page and returns eligibility status. Calls EMI MS NTBPreEligibility downstream. Used for NTB Seamless Journey.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---

This API accepts customer details entered on the merchant page and returns the customer's eligibility status for EMI/NTB options. It is also referred to as the **Link and Pay API** in the NTB Seamless Journey.

## Request parameters

| Parameter                                                       | Description                                                                                                                                                                     | Example                                                      |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| key<br />`mandatory`                                            | `String` - This parameter contains the merchant key provided by PayU during onboarding.                                                                                         | JP***g                                                       |
| txnid<br />`mandatory`                                          | `String` - This parameter contains a unique transaction ID. You can generate this ID or use the PayU API to generate it. The maximum length of this parameter is 25 characters. | txn_applepay_001                                             |
| amount<br />`mandatory`                                         | `String` - This parameter contains the payment amount.                                                                                                                          | 100.00                                                       |
| productinfo<br />`mandatory`                                    | `String` - This parameter contains a brief description of the product or service.                                                                                               | iPhone Case                                                  |
| firstname<br />`mandatory`                                      | `String` - This parameter contains the first name of the customer.                                                                                                              | John                                                         |
| email<br />`mandatory`                                          | `String` - This parameter contains the email address of the customer.                                                                                                           | [john@example.com](mailto:john@example.com)                  |
| phone<br /><code>mandatory</code>                               | <code>String</code> Customer mobile number.                                                                                                                                     | `"8178959206"`                                               |
| amount<br /><code>mandatory</code>                              | <code>String</code> Transaction amount.                                                                                                                                         | `"10000.00"`                                                 |
| pg<br /><code>mandatory</code>                                  | <code>String</code> Payment category; use `"EMI"` for EMI.                                                                                                                      | `"EMI"`                                                      |
| bankCode<br /><code>mandatory</code>                            | <code>String</code> Bank/lender code (e.g. LPEMI for cardless EMI).                                                                                                             | `"LPEMI"`                                                    |
| checkCustomerEligibilityWithDetails<br /><code>mandatory</code> | <code>Boolean</code> When true, eligibility is checked using the provided customer details.                                                                                     | `true`                                                       |
| <br />customerDetails<code>mandatory</code>                     | <code>Object</code> Customer onboarding details for NTB eligibility.                                                                                                            | See example below                                            |
| surl<br />`mandatory`                                           | `String` - This parameter contains the Success URL. PayU will redirect the customer to this URL after a successful payment.                                                     | [https://yoursite.com/success](https://yoursite.com/success) |
| furl<br />`mandatory`                                           | `String` - This parameter contains the Failure URL. PayU will redirect the customer to this URL after a failed payment.                                                         | [https://yoursite.com/failure](https://yoursite.com/failure) |
| hash<br />`mandatory`                                           | `String` - This parameter contains the hash value calculated using SHA-512 algorithm. Hash logic ensures the integrity of the transaction data.                                 | See hash generation                                          |
| lastname<br />`optional`                                        | `String` - This parameter contains the last name of the customer.                                                                                                               | Doe                                                          |
| address1<br />`optional`                                        | `String` - This parameter contains the first line of the billing address.                                                                                                       | 123 Main St                                                  |
| address2<br />`optional`                                        | `String` - This parameter contains the second line of the billing address.                                                                                                      | Apt 4B                                                       |
| city<br />`optional`                                            | `String` - This parameter contains the city of the billing address.                                                                                                             | Mumbai                                                       |
| state<br />`optional`                                           | `String` - This parameter contains the state of the billing address.                                                                                                            | Maharashtra                                                  |
| country<br />`optional`                                         | `String` - This parameter contains the country of the billing address.                                                                                                          | India                                                        |
| zipcode<br />`optional`                                         | `String` - This parameter contains the ZIP/postal code of the billing address.                                                                                                  | 400001                                                       |
| udf1<br />`optional`                                            | `String` - This parameter contains any additional information you want to pass. Maximum length is 255 characters.                                                               |                                                              |
| udf2<br />`optional`                                            | `String` - This parameter contains any additional information you want to pass. Maximum length is 255 characters.                                                               |                                                              |
| udf3<br />`optional`                                            | `String` - This parameter contains any additional information you want to pass. Maximum length is 255 characters.                                                               |                                                              |
| udf4<br />`optional`                                            | `String` - This parameter contains any additional information you want to pass. Maximum length is 255 characters.                                                               |                                                              |
| udf5<br />`optional`                                            | `String` - This parameter contains any additional information you want to pass. Maximum length is 255 characters.                                                               |                                                              |

#### customerDetails JSON Fields Description

| Field | Description | Example |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| panNumber<br /><code>mandatory</code> | <code>String</code> Customer PAN number. | `"EIJPS1234R"` |
| dob<br /><code>mandatory</code> | <code>String</code> Date of birth (DD-MM-YYYY). | `"14-12-1996"` |
| zipcode<br /><code>mandatory</code> | <code>String</code> Postal zip code. | `"411014"` |
| firstName<br /><code>mandatory</code> | <code>String</code> Customer first name. | `"Shray"` |
| lastName<br /><code>mandatory</code> | <code>String</code> Customer last name. | `"Suri"` |
| bureauPullConsent<br /><code>optional</code> | <code>String</code> Consent for bureau pull (e.g. "true"/"false"). | `"false"` |
| gender<br /><code>optional</code> | <code>String</code> Customer gender. | `"Male"` |
| income<br /><code>optional</code> | <code>String</code> Customer income. | `"65000"` |
| employeeType<br /><code>optional</code> | <code>String</code> Employment type (e.g. Salaried). | `"Salaried"` |
| abs<br /><code>optional</code> | <code>String</code> Additional business-specific field if required. | `"Asnw"` |

## Response parameters

| Parameter                                                                | Description                                                                                                           | Example                                                                                 |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| httpCode<br /><code>mandatory</code>                                     | <code>String</code> HTTP status code of the response.                                                                 | `"200"`                                                                                 |
| message<br /><code>optional</code>                                       | <code>String</code> Message from the API.                                                                             | `""`                                                                                    |
| status<br /><code>mandatory</code>                                       | <code>Integer</code> Status indicator (1 for success).                                                                | `1`                                                                                     |
| data<br /><code>optional</code>                                          | <code>Object</code> Response payload with EMI tenure options and eligibility.                                         | See sample response                                                                     |
| data.emi.ntb.cardless.all<br /><code>optional</code>                     | <code>Object</code> NTB cardless lender (e.g. LPEMI) with tenureOptions and eligibility.                              | See sample response                                                                     |
| data.emi.ntb.cardless.all.LPEMI.tenureOptions<br /><code>optional</code> | <code>Object</code> Tenure options (e.g. LPEMI03, LPEMI06, LPEMI09, LPEMI12) with tenure, maximumAmount, eligibility. | `{"LPEMI03": {"tenure": 3, "maximumAmount": 60000.0, "eligibility": {"status": true}}}` |
| data.emi.ntb.cardless.all.LPEMI.eligibility<br /><code>optional</code>   | <code>Object</code> Overall eligibility for the lender.                                                               | `{"status": true}` or `{"status": false, "reason": "..."}`                              |
| hasEligible<br /><code>optional</code>                                   | <code>Boolean</code> Whether the customer has any eligible option.                                                    | `true`                                                                                  |

## Sample request
```curl
curl --location --request POST 'https://test.payu.in/_payment' \
  --header 'accept: application/json' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=JP***g' \
  --data-urlencode 'txnid=EaE4ZO3vU4iPsp' \
  --data-urlencode 'amount=10.00' \
  --data-urlencode 'firstname=Ashish' \
  --data-urlencode 'email=test@gmail.com' \
  --data-urlencode 'phone=9876543210' \
  --data-urlencode 'productinfo=iPhone' \
  --data-urlencode 'pg=EMI' \
  --data-urlencode 'bankcode=LPEMI' \
  --data-urlencode 'checkCustomerEligibilityWithDetails=true' \
  --data-urlencode 'customerDetails={"panNumber":"EIJPS1234R","dob":"14-12-1996","zipcode":"411014","firstName":"Shray","lastName":"Suri","bureauPullConsent":"false","gender":"Male","income":"65000","employeeType":"Salaried","abs":"Asnw"}' \
  --data-urlencode 'surl=https://apiplayground-response.herokuapp.com/' \
  --data-urlencode 'furl=https://apiplayground-response.herokuapp.com/' \
  --data-urlencode 'hash=fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304'
```
```python
import requests
import json

url = "https://test.payu.in/_payment"
headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}
customer_details = {
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
payload = {
    "key": "JP***g",
    "txnid": "EaE4ZO3vU4iPsp",
    "amount": "10.00",
    "firstname": "Ashish",
    "email": "test@gmail.com",
    "phone": "9876543210",
    "productinfo": "iPhone",
    "pg": "EMI",
    "bankcode": "LPEMI",
    "checkCustomerEligibilityWithDetails": "true",
    "customerDetails": json.dumps(customer_details),
    "surl": "https://apiplayground-response.herokuapp.com/",
    "furl": "https://apiplayground-response.herokuapp.com/",
    "hash": "fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304"
}
response = requests.post(url, headers=headers, data=payload)
print(response.status_code)
print(response.json())
```
```javascript
const customerDetails = {
  panNumber: "EIJPS1234R",
  dob: "14-12-1996",
  zipcode: "411014",
  firstName: "Shray",
  lastName: "Suri",
  bureauPullConsent: "false",
  gender: "Male",
  income: "65000",
  employeeType: "Salaried",
  abs: "Asnw"
};

const params = new URLSearchParams({
  key: "JP***g",
  txnid: "EaE4ZO3vU4iPsp",
  amount: "10.00",
  firstname: "Ashish",
  email: "test@gmail.com",
  phone: "9876543210",
  productinfo: "iPhone",
  pg: "EMI",
  bankcode: "LPEMI",
  checkCustomerEligibilityWithDetails: "true",
  customerDetails: JSON.stringify(customerDetails),
  surl: "https://apiplayground-response.herokuapp.com/",
  furl: "https://apiplayground-response.herokuapp.com/",
  hash: "fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304"
});

fetch("https://test.payu.in/_payment", {
  method: "POST",
  headers: {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
  },
  body: params.toString()
})
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));
```
```java
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;

String customerDetailsJson = "{\"panNumber\":\"EIJPS1234R\",\"dob\":\"14-12-1996\",\"zipcode\":\"411014\",\"firstName\":\"Shray\",\"lastName\":\"Suri\",\"bureauPullConsent\":\"false\",\"gender\":\"Male\",\"income\":\"65000\",\"employeeType\":\"Salaried\",\"abs\":\"Asnw\"}";

String formBody = String.join("&",
    "key=" + URLEncoder.encode("JP***g", StandardCharsets.UTF_8),
    "txnid=" + URLEncoder.encode("EaE4ZO3vU4iPsp", StandardCharsets.UTF_8),
    "amount=" + URLEncoder.encode("10.00", StandardCharsets.UTF_8),
    "firstname=" + URLEncoder.encode("Ashish", StandardCharsets.UTF_8),
    "email=" + URLEncoder.encode("test@gmail.com", StandardCharsets.UTF_8),
    "phone=" + URLEncoder.encode("9876543210", StandardCharsets.UTF_8),
    "productinfo=" + URLEncoder.encode("iPhone", StandardCharsets.UTF_8),
    "pg=" + URLEncoder.encode("EMI", StandardCharsets.UTF_8),
    "bankcode=" + URLEncoder.encode("LPEMI", StandardCharsets.UTF_8),
    "checkCustomerEligibilityWithDetails=" + URLEncoder.encode("true", StandardCharsets.UTF_8),
    "customerDetails=" + URLEncoder.encode(customerDetailsJson, StandardCharsets.UTF_8),
    "surl=" + URLEncoder.encode("https://apiplayground-response.herokuapp.com/", StandardCharsets.UTF_8),
    "furl=" + URLEncoder.encode("https://apiplayground-response.herokuapp.com/", StandardCharsets.UTF_8),
    "hash=" + URLEncoder.encode("fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304", StandardCharsets.UTF_8)
);

URL url = new URL("https://test.payu.in/_payment");
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
conn.setRequestMethod("POST");
conn.setRequestProperty("accept", "application/json");
conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
conn.setDoOutput(true);
try (OutputStream os = conn.getOutputStream()) {
    os.write(formBody.getBytes(StandardCharsets.UTF_8));
}
int status = conn.getResponseCode();
```
```csharp
using System.Net.Http;
using System.Text.Json;

var customerDetails = new Dictionary<string, string>
{
    ["panNumber"] = "EIJPS1234R",
    ["dob"] = "14-12-1996",
    ["zipcode"] = "411014",
    ["firstName"] = "Shray",
    ["lastName"] = "Suri",
    ["bureauPullConsent"] = "false",
    ["gender"] = "Male",
    ["income"] = "65000",
    ["employeeType"] = "Salaried",
    ["abs"] = "Asnw"
};

var payload = new Dictionary<string, string>
{
    ["key"] = "JP***g",
    ["txnid"] = "EaE4ZO3vU4iPsp",
    ["amount"] = "10.00",
    ["firstname"] = "Ashish",
    ["email"] = "test@gmail.com",
    ["phone"] = "9876543210",
    ["productinfo"] = "iPhone",
    ["pg"] = "EMI",
    ["bankcode"] = "LPEMI",
    ["checkCustomerEligibilityWithDetails"] = "true",
    ["customerDetails"] = JsonSerializer.Serialize(customerDetails),
    ["surl"] = "https://apiplayground-response.herokuapp.com/",
    ["furl"] = "https://apiplayground-response.herokuapp.com/",
    ["hash"] = "fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304"
};

var formContent = new FormUrlEncodedContent(payload);
using var client = new HttpClient();
client.DefaultRequestHeaders.Add("accept", "application/json");
var response = await client.PostAsync("https://test.payu.in/_payment", formContent);
var responseBody = await response.Content.ReadAsStringAsync();
```
## Sample response

### Success scenario (customer eligible)

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
                "LPEMI12": { "tenure": 12, "maximumAmount": 100000.0, "eligibility": { "status": false, "reason": "Tenure not available" } },
                "LPEMI03": { "tenure": 3, "maximumAmount": 60000.0, "eligibility": { "status": true } },
                "LPEMI09": { "tenure": 9, "maximumAmount": 100000.0, "eligibility": { "status": false, "reason": "Tenure not available" } },
                "LPEMI06": { "tenure": 6, "maximumAmount": 100000.0, "eligibility": { "status": true } },
                "LPEMI": { "tenure": 0, "maximumAmount": 100000.0, "eligibility": { "status": false, "reason": "Tenure not available" } }
              },
              "eligibility": { "status": true }
            }
          },
          "hasEligible": true
        }
      }
    }
  }
}
```

### Failure scenario (customer not eligible)

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
                "LPEMI12": { "tenure": 12, "maximumAmount": 100000.0, "eligibility": { "status": false, "reason": "Tenure not available" } },
                "LPEMI03": { "tenure": 3, "maximumAmount": 60000.0, "eligibility": { "status": false, "reason": "Tenure not available" } },
                "LPEMI09": { "tenure": 9, "maximumAmount": 100000.0, "eligibility": { "status": false, "reason": "Tenure not available" } },
                "LPEMI06": { "tenure": 6, "maximumAmount": 100000.0, "eligibility": { "status": false, "reason": "Tenure not available" } },
                "LPEMI": { "tenure": 0, "maximumAmount": 100000.0, "eligibility": { "status": false, "reason": "Tenure not available" } }
              },
              "eligibility": { "status": false, "reason": "Use is not eligible for cof product" }
            }
          },
          "hasEligible": false
        }
      }
    }
  }
}
```