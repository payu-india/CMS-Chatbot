---
title: Get Checkout Details API
excerpt: ''
api:
  file: others-12.json
  operationId: get-checkout_details
deprecated: false
hidden: false
metadata:
  title: Get Checkout Details API
  description: >-
    The Get Checkout Details API provides information on payment options,
    additional charges, eligibility details, and downtime status for custom
    checkout pages. It allows merchants to retrieve extended payment details,
    additional charges, tax specifications, check down status, and customer
    eligibility.
  keywords:
    - get_checkout_details API Command
    - Get additional charges API
    - Get tax specification API
    - ' Check down status API'
    - Check customer eligibility API
    - API Command get_checkout_details
  robots: index
next:
  description: ''
---
The Get Checkout Details (**get_checkout_details**) API is a generic API using which they can get information when you create the custom checkout pages, that will contain the payment options, offers, recommendations, and downtime details. The API provides the following details: 

* **Payment option details**: The extended details for each payment option are available for the merchant.
* **Additional charges**: The additional charges are configured for all payment options.
* eligibility details
* **Downtime details**: The downtime status of the payment options.

<Callout icon="📮" theme="default">
  **Postman Collection**: Access the Get Checkout Details API Postman Collection from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/f1fv12l/getcheckoutdetails-paymodes](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/f1fv12l/getcheckoutdetails-paymodes)
</Callout>

**Environment**

|                        |                                                                                                      |
| :--------------------- | :--------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in-merchant/postservice?form=2](https://test.payu.in-merchant/postservice?form=2) |
| Production Environment | [https://info.payu.in-merchant/postservice?form=2](https://info.payu.in-merchant/postservice?form=2) |

<Accordion title="Sample request and response" icon="fa-reply">
  ### Get extended payment details

```curl
curl --location 'https://info.payu.in/merchant/postservice.php?form=2' \
--form 'key=0d5aDh' \
--form 'command=get_checkout_details' \
--form 'var1={"requestId":"9920371372_38","transactionDetails":{"amount":8000},"useCase":{"getExtendedPaymentDetails":true}}' \
--form 'hash=5c4784472c10fab50be3730a923474925c477e0fdd9a4957d5b0e0469cca3144cb74670ddc5cbe0e3edcbcd04dae64792a93989e99fd17b1cb4ce561659ce24a'
```
```python
import requests

url = "https://info.payu.in/merchant/postservice.php?form=2"

files = {
    'key': (None, '0d5aDh'),
    'command': (None, 'get_checkout_details'),
    'var1': (None, '{"requestId":"9920371372_38","transactionDetails":{"amount":8000},"useCase":{"getExtendedPaymentDetails":true}}'),
    'hash': (None, '5c4784472c10fab50be3730a923474925c477e0fdd9a4957d5b0e0469cca3144cb74670ddc5cbe0e3edcbcd04dae64792a93989e99fd17b1cb4ce561659ce24a')
}

try:
    response = requests.post(url, files=files)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```
```javascript
async function makeRequest() {
    const url = "https://info.payu.in/merchant/postservice.php?form=2";
    
    const formData = new FormData();
    formData.append('key', '0d5aDh');
    formData.append('command', 'get_checkout_details');
    formData.append('var1', '{"requestId":"9920371372_38","transactionDetails":{"amount":8000},"useCase":{"getExtendedPaymentDetails":true}}');
    formData.append('hash', '5c4784472c10fab50be3730a923474925c477e0fdd9a4957d5b0e0469cca3144cb74670ddc5cbe0e3edcbcd04dae64792a93989e99fd17b1cb4ce561659ce24a');

    try {
        const response = await fetch(url, {
            method: "POST",
            body: formData
        });
        
        const responseText = await response.text();
        console.log(`Status Code: ${response.status}`);
        console.log(`Response: ${responseText}`);
    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
}

makeRequest();
```
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;
import java.util.HashMap;
import java.util.Map;

public class ApiRequest {
    public static void main(String[] args) {
        try {
            String url = "https://info.payu.in/merchant/postservice.php?form=2";
            String boundary = "----boundary" + System.currentTimeMillis();
            
            Map<String, String> formData = new HashMap<>();
            formData.put("key", "0d5aDh");
            formData.put("command", "get_checkout_details");
            formData.put("var1", "{\"requestId\":\"9920371372_38\",\"transactionDetails\":{\"amount\":8000},\"useCase\":{\"getExtendedPaymentDetails\":true}}");
            formData.put("hash", "5c4784472c10fab50be3730a923474925c477e0fdd9a4957d5b0e0469cca3144cb74670ddc5cbe0e3edcbcd04dae64792a93989e99fd17b1cb4ce561659ce24a");
            
            StringBuilder body = new StringBuilder();
            for (Map.Entry<String, String> entry : formData.entrySet()) {
                body.append("--").append(boundary).append("\r\n");
                body.append("Content-Disposition: form-data; name=\"").append(entry.getKey()).append("\"\r\n\r\n");
                body.append(entry.getValue()).append("\r\n");
            }
            body.append("--").append(boundary).append("--\r\n");
            
            HttpClient client = HttpClient.newBuilder()
                .connectTimeout(Duration.ofSeconds(10))
                .build();

            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("Content-Type", "multipart/form-data; boundary=" + boundary)
                .POST(HttpRequest.BodyPublishers.ofString(body.toString()))
                .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            
            System.out.println("Status Code: " + response.statusCode());
            System.out.println("Response: " + response.body());
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
```csharp
using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        try
        {
            string url = "https://info.payu.in/merchant/postservice.php?form=2";
            
            var formContent = new MultipartFormDataContent();
            formContent.Add(new StringContent("0d5aDh"), "key");
            formContent.Add(new StringContent("get_checkout_details"), "command");
            formContent.Add(new StringContent("{\"requestId\":\"9920371372_38\",\"transactionDetails\":{\"amount\":8000},\"useCase\":{\"getExtendedPaymentDetails\":true}}"), "var1");
            formContent.Add(new StringContent("5c4784472c10fab50be3730a923474925c477e0fdd9a4957d5b0e0469cca3144cb74670ddc5cbe0e3edcbcd04dae64792a93989e99fd17b1cb4ce561659ce24a"), "hash");

            HttpResponseMessage response = await client.PostAsync(url, formContent);
            string responseBody = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {responseBody}");
        }
        catch (HttpRequestException ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
```
```php
<?php
$url = "https://info.payu.in/merchant/postservice.php?form=2";

$postData = [
    "key" => "0d5aDh",
    "command" => "get_checkout_details",
    "var1" => '{"requestId":"9920371372_38","transactionDetails":{"amount":8000},"useCase":{"getExtendedPaymentDetails":true}}',
    "hash" => "5c4784472c10fab50be3730a923474925c477e0fdd9a4957d5b0e0469cca3144cb74670ddc5cbe0e3edcbcd04dae64792a93989e99fd17b1cb4ce561659ce24a"
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $postData);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

if (curl_errno($ch)) {
    echo "Error: " . curl_error($ch) . "\n";
} else {
    echo "Status Code: " . $httpCode . "\n";
    echo "Response: " . $response . "\n";
}

curl_close($ch);
?>
```

  **Response**

  ```json
  {
    "status": 1,
    "details": {
      "paymentOptions": {
        "emi": {
          "all": {
            "dc": {
              "hasEligible": true,
              "all": {
                // Key is the 4 letter IFSC initials of the banks.
                "UTIB": {
                  "title": "Axis Bank",
                  "shortName": "Axis",
                  // Minimum amount for this bank.
                  "minimumAmount": 1000,
                  // Maximum amount for this bank, null means no-limit.
                  "maximumAmount": null,
                  "eligibility": {"status": true},
                  "tenureOptions": {
                    // Key name is the value of bankcode accepted by PayU.
                    "AXISD03": {
                      "tenure": 3,
                      "interestRate": 10.5,
                      "interestCharged": 200.45,
                      "monthlyEmi": 400.5,
                      "minimumAmount": 1000,
                      "maximumAmount": null,
                      "eligibility": {"status": true},
                    },
                    "AXISD...": { "...": "..." }
                  }
                },
                "HDFC": { "...": "..." }
              },
              // Least amount limit of any dc emi.
              "minimumAmount": 1000,
              // Highest amount limit of any dc emi, null means no limit.
              "maximumAmount": null
            },
            "cc": { "...": "..." },
            "others": { "...": "..." },
            "cardless": {
              "hasEligible": true,
              "all": {
                "ZESTMON": {
                  "title": "Zest Money",
                  "shortName": "ZestMoney",
                  "minimumAmount": 1000,
                  "maximumAmount": null,
                  "tenureOptions": {
                    "ZESTMON": {
                      // Tenure field will be all in case tenures of an option
                      // not managed on PayU end.
                      "tenure": null,
                      "minimumAmount": 1000,
                      "maximumAmount": null,
                      "eligibility": {"status": true},
                      // interestRate, interestCharged, monthlyEmi, etc may/may
                      // not be present depending whether these are maintained
                      // at payu's end or not. Eg ZESTMON's tenures are maintained
                      // on the bank end only and are returned once the customer
                      // proceeds with this option and submits the OTP.
                    }
                  }
                },
                "...": { "...": "..." }
              }
            }
          }
        },
        "nb": {
          "all": {
            // Key name is the value of bankcode accepted by PayU.
            "SBIB": {
              "title": "State Bank of India"
            },
            "ADBB": {
              "title": "Andhra Bank"
            },
            "AXIB": {
              "title": "AXIS Bank NetBanking"
            },
            "AXNBTPV": {
              "title": "Axis NB TPV"
            },
            "...": { "...": "..." }
          }
        },
        "si": {
          "all": {
            "ANDBENCR": {
              "title": "Andhra Bank Recurring"
            },
            "AUBLENCR": {
              "title": "AU Small Finance Bank Ltd Recurring"
            },
            "UTIBENCR": {
              "title": "AXIS BANK Recurring"
            },
            "BARBENCR": {
              "title": "BARB ENACH Recurring"
            },
            "...": { "...": "..." }
          }
        },
        "dc": {
          "all": {
            "MAST": {
              "title": "MasterCard Debit Cards"
            },
            "MASTTPV": {
              "title": "MasterCard TPV Debit Cards"
            },
            "SMAE": {
              "title": "State Bank Maestro Cards"
            },
            "MAES": {
              "title": "Other Maestro Cards"
            },
            "RUPAY": {
              "title": "Rupay Debit Card"
            },
            "...": { "...": "..." }
          }
        },
        "cc": {
          "all": {
            "CC": {
              "title": "Credit Card"
            },
            "DINR": {
              "title": "Diners"
            },
            "RUPAYCC": {
              "title": "Rupay Credit Card"
            },
            "...": { "...": "..." }
          }
        },
        "lazypay": {
          "all": {
            "LAZYPAY": {
              "title": "LazyPay"
            }
          }
        },
        "lp-emi": {
          "all": {
            "LP-EMI": {
              "title": "LAZYPAYEMI"
            }
          }
        },
        "cash": {
          "all": {
            "PAYTM": {
              "title": "Paytm"
            },
            "...": { "...": "..." }
          }
        },
        // Similarly all the modes & payment options that are available for
        // the merchant.
        "...": { "...": "..." }
      }
    }
  }
  ```

  ### Get additional charges

  ```bash
  {
      "requestId": "12345678",
      "transactionDetails": {
        "amount": 12345.12
      },
      "useCase": {
        "getAdditionalCharges": true
      }
    }
  ```

  **Response**

  ```json
  {
    "status": 1,
    "details": {
      "paymentOptions": {
        "emi": {
          "all": {
            "dc": {
              "all": {
                "UTIB": {
                  "tenureOptions": {
                    "AXISD03": {
                      "additionalCharge": 13.37
                    },
                    "AXISD...": { "...": "..." }
                  }
                },
                "...": { "...": "..." }
              }
            },
            "...": { "...": "..." }
          }
        },
        "nb": {
          "all": {
            "SBIB": {
              "additionalCharge": 0
            },
            "ADBB": {
              "additionalCharge": 0
            },
            "AXIB": {
              "additionalCharge": 0
            },
            "AXNBTPV": {
              "additionalCharge": 0
            },
            "...": { "...": "..." }
          }
        },
        "dc": {
          "all": {
            "MAST": {
              "additionalCharge": 5.0
            },
            "MASTTPV": {
              "additionalCharge": 5.0
            },
            "SMAE": {
              "additionalCharge": 5.0
            },
            "MAES": {
              "additionalCharge": 5.0
            },
            "RUPAY": {
              "additionalCharge": 5.0
            },
            "...": { "...": "..." }
          }
        },
        "cc": {
          "all": {
            "CC": {
              "additionalCharge": 5.0
            },
            "DINR": {
              "additionalCharge": 5.0
            },
            "RUPAYCC": {
              "additionalCharge": 5.0
            },
            "...": { "...": "..." }
          }
        },
        "cash": {
          "all": {
            "PAYTM": {
              "additionalCharge": 10.5
            },
            "...": { "...": "..." }
          }
        },
        // Similarly all the modes & payment options that are available for
        // the merchant.
        "...": { "...": "..." }
      }
    }
  }
  ```

  ### Get tax specification

  ```bash
  {
    // Mandatory field, random id for debugging purposes only
    "requestId": "12345678",
    "transactionDetails": {
      // Mandatory field
      "amount": 12345.12
    },
    "useCase": {
      // Down Banks info will be returned only if this flag is true.
      "getTaxSpecification": true
    }
  }
  ```

  **Response**

  ```json
  {
    "status": 1,
    "details": {
      // No change in the payment options returned or any other internal field
      // due to the checkDownStatus flag.
      // These will remain as it is as the remaining responses.
      "paymentOptions": {
        "cc": { "...": "..." },
        "dc": { "...": "..." },
        "...": { "...": "..." }
      },
      "config": {
        // This object will be returned if getTaxSpecification flag is true.
        // Default is the one to be applied on all modes.
        // In special cases, this can also have mode level tax percent
        "taxSpecification": {
          "default": 18
        }
      }
    }
  }
  ```

  ### Check down status

  ```bash
  {
    // Mandatory field, random id for debugging purposes only
    "requestId": "12345678",
    "transactionDetails": {
      // Mandatory field
      "amount": 12345.12
    },
    "useCase": {
      // Down Banks info will be returned only if this flag is true.
      "checkDownStatus": true
    }
  }
  ```

  \*\* Response\*\*

  ```json
  {
    "status": 1,
    "details": {
      // No change in the payment options returned or any other internal field
      // due to the checkDownStatus flag.
      // These will remain as it is as the remaining responses.
      "paymentOptions": {
        "cc": { "...": "..." },
        "dc": { "...": "..." },
        "nb": { "...": "..." },
        "emi": { "...": "..." },
        "upi": { "...": "..." },
        "cash": { "...": "..." }
      },
      // This object will be returned if checkDownStatus flag is true.
      "downInfo": {
        // issuingBank contains the list of down issuing banks for the cards
        "issuingBanks": ["HDFC", "AXIS", "ICICI"],
        // nb/cashcard/etc all the other keys in this object contains the list of
        // down ibibo codes corresponding to the modes. The remaing keys will the
        // same as the ones present in the "paymentOptions" object
        "nb": ["SBIB", "ANDB"],
        "cash": ["PAYTM", "YESW"],
        "...": ["..."]
      }
    }
  }
  ```

  ### Check customer eligibility

  This field is used to check the customer eligibility.

```curl
curl --location 'https://info.payu.in/merchant/postservice.php?form=2' \
--form 'key=merchant key' \
--form 'command=get_checkout_details' \
--form 'var1={"requestId":"Test212345","transactionDetails":{"amount":10000},"customerDetails":{"mobile":"9368252248"},"useCase":{"checkCustomerEligibility":true},"filters":{"paymentOptions":{"emi":{"dc":"all","cc":"all","cardless":"all"},"bnpl":"all"}}}' \
--form 'hash=hash value'
```
```python
import requests

url = "https://info.payu.in/merchant/postservice.php?form=2"

files = {
    'key': (None, 'merchant key'),
    'command': (None, 'get_checkout_details'),
    'var1': (None, '{"requestId":"Test212345","transactionDetails":{"amount":10000},"customerDetails":{"mobile":"9368252248"},"useCase":{"checkCustomerEligibility":true},"filters":{"paymentOptions":{"emi":{"dc":"all","cc":"all","cardless":"all"},"bnpl":"all"}}}'),
    'hash': (None, 'hash value')
}

try:
    response = requests.post(url, files=files)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```
```javascript
async function makeRequest() {
    const url = "https://info.payu.in/merchant/postservice.php?form=2";
    
    const formData = new FormData();
    formData.append('key', 'merchant key');
    formData.append('command', 'get_checkout_details');
    formData.append('var1', '{"requestId":"Test212345","transactionDetails":{"amount":10000},"customerDetails":{"mobile":"9368252248"},"useCase":{"checkCustomerEligibility":true},"filters":{"paymentOptions":{"emi":{"dc":"all","cc":"all","cardless":"all"},"bnpl":"all"}}}');
    formData.append('hash', 'hash value');

    try {
        const response = await fetch(url, {
            method: "POST",
            body: formData
        });
        
        const responseText = await response.text();
        console.log(`Status Code: ${response.status}`);
        console.log(`Response: ${responseText}`);
    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
}

makeRequest();
```
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;
import java.util.HashMap;
import java.util.Map;

public class ApiRequest {
    public static void main(String[] args) {
        try {
            String url = "https://info.payu.in/merchant/postservice.php?form=2";
            String boundary = "----boundary" + System.currentTimeMillis();
            
            Map<String, String> formData = new HashMap<>();
            formData.put("key", "merchant key");
            formData.put("command", "get_checkout_details");
            formData.put("var1", "{\"requestId\":\"Test212345\",\"transactionDetails\":{\"amount\":10000},\"customerDetails\":{\"mobile\":\"9368252248\"},\"useCase\":{\"checkCustomerEligibility\":true},\"filters\":{\"paymentOptions\":{\"emi\":{\"dc\":\"all\",\"cc\":\"all\",\"cardless\":\"all\"},\"bnpl\":\"all\"}}}");
            formData.put("hash", "hash value");
            
            StringBuilder body = new StringBuilder();
            for (Map.Entry<String, String> entry : formData.entrySet()) {
                body.append("--").append(boundary).append("\r\n");
                body.append("Content-Disposition: form-data; name=\"").append(entry.getKey()).append("\"\r\n\r\n");
                body.append(entry.getValue()).append("\r\n");
            }
            body.append("--").append(boundary).append("--\r\n");
            
            HttpClient client = HttpClient.newBuilder()
                .connectTimeout(Duration.ofSeconds(10))
                .build();

            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("Content-Type", "multipart/form-data; boundary=" + boundary)
                .POST(HttpRequest.BodyPublishers.ofString(body.toString()))
                .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            
            System.out.println("Status Code: " + response.statusCode());
            System.out.println("Response: " + response.body());
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
```csharp
using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        try
        {
            string url = "https://info.payu.in/merchant/postservice.php?form=2";
            
            var formContent = new MultipartFormDataContent();
            formContent.Add(new StringContent("merchant key"), "key");
            formContent.Add(new StringContent("get_checkout_details"), "command");
            formContent.Add(new StringContent("{\"requestId\":\"Test212345\",\"transactionDetails\":{\"amount\":10000},\"customerDetails\":{\"mobile\":\"9368252248\"},\"useCase\":{\"checkCustomerEligibility\":true},\"filters\":{\"paymentOptions\":{\"emi\":{\"dc\":\"all\",\"cc\":\"all\",\"cardless\":\"all\"},\"bnpl\":\"all\"}}}"), "var1");
            formContent.Add(new StringContent("hash value"), "hash");

            HttpResponseMessage response = await client.PostAsync(url, formContent);
            string responseBody = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {responseBody}");
        }
        catch (HttpRequestException ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
```
```php
<?php
$url = "https://info.payu.in/merchant/postservice.php?form=2";

$postData = [
    "key" => "merchant key",
    "command" => "get_checkout_details",
    "var1" => '{"requestId":"Test212345","transactionDetails":{"amount":10000},"customerDetails":{"mobile":"9368252248"},"useCase":{"checkCustomerEligibility":true},"filters":{"paymentOptions":{"emi":{"dc":"all","cc":"all","cardless":"all"},"bnpl":"all"}}}',
    "hash" => "hash value"
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $postData);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

if (curl_errno($ch)) {
    echo "Error: " . curl_error($ch) . "\n";
} else {
    echo "Status Code: " . $httpCode . "\n";
    echo "Response: " . $response . "\n";
}

curl_close($ch);
?>
```

  **Sample response**

  ```
  {
      "status": 1,
      "details": {
          "paymentOptions": {
              "emi": {
                  "all": {
                      "dc": {
                          "all": {
                              "KKBK": {
                                  "tenureOptions": {
                                      "KOTAKD01": {
                                          "tenure": 1,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "KOTAKD12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "KOTAKD02": {
                                          "tenure": 2,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "KOTAKD03": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "KOTAKD06": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "KOTAKD09": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "ICIC": {
                                  "tenureOptions": {
                                      "ICICID12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "This mobile number is not eligible. Please change the mobile number."
                                          }
                                      },
                                      "ICICID03": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "This mobile number is not eligible. Please change the mobile number."
                                          }
                                      },
                                      "ICICID06": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "This mobile number is not eligible. Please change the mobile number."
                                          }
                                      },
                                      "ICICID09": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "This mobile number is not eligible. Please change the mobile number."
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": false,
                                      "reason": "Customer not eligible for EMI"
                                  }
                              },
                              "BARB": {
                                  "tenureOptions": {
                                      "BOBD18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "This mobile number is not eligible. Please change the mobile number."
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": false,
                                      "reason": "Customer not eligible for EMI"
                                  }
                              }
                          },
                          "hasEligible": true
                      },
                      "cc": {
                          "all": {
                              "YESB": {
                                  "tenureOptions": {
                                      "EMIY12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIY18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIY24": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIY03": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIY06": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIY09": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "FDRL": {
                                  "tenureOptions": {
                                      "FDRL12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "FDRL18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "FDRL24": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "FDRL03": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "FDRL06": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "FDRL09": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "INDB": {
                                  "tenureOptions": {
                                      "EMIIND12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIIND18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIIND24": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIIND3": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIIND36": {
                                          "tenure": 36,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIIND6": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIIND9": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "SBIN": {
                                  "tenureOptions": {
                                      "SBI12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "SBI18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "SBI24": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "SBI03": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "SBI06": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "SBI09": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "AUSF": {
                                  "tenureOptions": {
                                      "AUSF12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "AUSF18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "AUSF24": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "AUSF03": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "AUSF06": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "AUSF09": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "HDFC": {
                                  "tenureOptions": {
                                      "EMI12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMI18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMI24": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMI": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMI36": {
                                          "tenure": 36,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "Minimum required amount is 30000"
                                          }
                                      },
                                      "EMI48": {
                                          "tenure": 48,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "Minimum required amount is 40000"
                                          }
                                      },
                                      "EMI6": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMI9": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "ICIC": {
                                  "tenureOptions": {
                                      "EMIIC12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIIC18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIIC24": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIIC3": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIIC6": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIIC9": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "BARB": {
                                  "tenureOptions": {
                                      "BOBCC12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "BOBCC18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "BOBCC02": {
                                          "tenure": 2,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "BOBCC24": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "BOBCC03": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "BOBCC36": {
                                          "tenure": 36,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "BOBCC04": {
                                          "tenure": 4,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "BOBCC05": {
                                          "tenure": 5,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "BOBCC06": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "BOBCC07": {
                                          "tenure": 7,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "BOBCC08": {
                                          "tenure": 8,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "BOBCC09": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "ONEC": {
                                  "tenureOptions": {
                                      "ONEC12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "ONEC18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "ONEC24": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "ONEC03": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "ONEC06": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "ONEC09": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "AMEX": {
                                  "tenureOptions": {
                                      "EMAMEX12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIAMEX3": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIAMEX6": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIAMEX9": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "CITI": {
                                  "tenureOptions": {
                                      "EMI012": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMI018": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMI024": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMI03": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMI06": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMI09": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "SCBL": {
                                  "tenureOptions": {
                                      "EMISCB12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMISCB18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMISCB24": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMISCB3": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMISCB6": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMISCB9": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "IDFC": {
                                  "tenureOptions": {
                                      "IDFC12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "IDFC15": {
                                          "tenure": 15,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "IDFC18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "IDFC24": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "IDFC03": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "IDFC36": {
                                          "tenure": 36,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "IDFC06": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "IDFC09": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "KKBK": {
                                  "tenureOptions": {
                                      "EMIK12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIK18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIK24": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIK3": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIK36": {
                                          "tenure": 36,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIK6": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIK9": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "DBSCC": {
                                  "tenureOptions": {
                                      "DBS12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "DBS18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "DBS24": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "DBS03": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "DBS06": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "DBS09": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "RATN": {
                                  "tenureOptions": {
                                      "EMIRBL12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIRBL18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIRBL24": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIRBL3": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIRBL6": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIRBL9": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "CANARA": {
                                  "tenureOptions": {
                                      "CANARA12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "CANARA18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "CANARA24": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "CANARA03": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "CANARA06": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "CANARA09": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "HSBC": {
                                  "tenureOptions": {
                                      "EMIHS12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIHS18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIHS24": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIHS03": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIHS06": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIHS09": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "IDBI": {
                                  "tenureOptions": {
                                      "IDBI12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "IDBI18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "IDBI24": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "IDBI03": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "IDBI30": {
                                          "tenure": 30,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "IDBI36": {
                                          "tenure": 36,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "IDBI06": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "IDBI09": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "UTIB": {
                                  "tenureOptions": {
                                      "EMIA12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIA18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIA24": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIA3": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIA6": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "EMIA9": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              }
                          },
                          "hasEligible": true
                      },
                      "cardless": {
                          "all": {
                              "AXIO": {
                                  "tenureOptions": {
                                      "AXIO12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "AXIO18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "AXIO24": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "AXIO03": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "AXIO06": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "AXIO09": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "AXIO": {
                                          "tenure": null,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "HMECDT": {
                                  "tenureOptions": {
                                      "HMECDT03": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "This mobile number is not eligible. Please change the mobile number."
                                          }
                                      },
                                      "HMECDT06": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "This mobile number is not eligible. Please change the mobile number."
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": false,
                                      "reason": "Customer not eligible for EMI"
                                  }
                              },
                              "LIQUIL": {
                                  "tenureOptions": {
                                      "LIQUIL06": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "ZESTMON": {
                                  "tenureOptions": {
                                      "ZESTMON": {
                                          "tenure": null,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "This mobile number is not eligible. Please change the mobile number."
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": false,
                                      "reason": "Customer not eligible for EMI"
                                  }
                              }
                          },
                          "hasEligible": true
                      }
                  }
              },
              "bnpl": {
                  "all": {
                      "LAZYPAY": {
                          "eligibility": {
                              "status": false,
                              "reason": "Maximum allowed amount is 5000"
                          }
                      },
                      "MOBIZIP": {
                          "eligibility": {
                              "status": false,
                              "reason": "This mobile number is not eligible. Please change the mobile number."
                          }
                      },
                      "POSTPE": {
                          "eligibility": {
                              "status": false,
                              "reason": "This mobile number is not eligible. Please change the mobile number."
                          }
                      }
                  }
              }
          }
      }
  }
  ```

  #### emi field in the \*\*paymentOptions \*\*field with filters parameter

  In this example, SBI, Kotak Mahindra and ICICI Bank EMI options are filtered. For list of EMI options, refer to [EMI Options for Get Checkout Details API](#emi-options-for-get-checkout-details-api).

  ```
  {
    "requestId": "4NQD7jcrGCt2LAxB",
    "filters": {
      "paymentOptions": {
        "emi": {
          "dc": "SBIN,KKBK,ICIC"
        }
      }
    },
    "useCase": {
      "checkCustomerEligibility": true
    },
    "customerDetails": {
      "mobile": "9871732405"
    },
    "transactionDetails": {
      "amount": "12386.00"
    }
  }
  ```

  **Response**

  ```
  {
      "status": 1,
      "details": {
          "paymentOptions": {
              "emi": {
                  "all": {
                      "dc": {
                          "all": {
                              "SBIN": {
                                  "tenureOptions": {
                                      "SBID12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "SBID18": {
                                          "tenure": 18,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "Minimum required amount is 25000"
                                          }
                                      },
                                      "SBID24": {
                                          "tenure": 24,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "Minimum required amount is 25000"
                                          }
                                      },
                                      "SBID03": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "SBID30": {
                                          "tenure": 30,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "Minimum required amount is 50000"
                                          }
                                      },
                                      "SBID36": {
                                          "tenure": 36,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "Minimum required amount is 50000"
                                          }
                                      },
                                      "SBID06": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": true
                                          }
                                      },
                                      "SBID09": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": true
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": true
                                  }
                              },
                              "KKBK": {
                                  "tenureOptions": {
                                      "KOTAKD12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "This mobile number is not eligible. Please change the mobile number."
                                          }
                                      },
                                      "KOTAKD03": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "This mobile number is not eligible. Please change the mobile number."
                                          }
                                      },
                                      "KOTAKD06": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "This mobile number is not eligible. Please change the mobile number."
                                          }
                                      },
                                      "KOTAKD09": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "This mobile number is not eligible. Please change the mobile number."
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": false,
                                      "reason": "Customer not eligible for EMI"
                                  }
                              },
                              "ICIC": {
                                  "tenureOptions": {
                                      "ICICID12": {
                                          "tenure": 12,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "This mobile number is not eligible. Please change the mobile number."
                                          }
                                      },
                                      "ICICID03": {
                                          "tenure": 3,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "This mobile number is not eligible. Please change the mobile number."
                                          }
                                      },
                                      "ICICID06": {
                                          "tenure": 6,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "This mobile number is not eligible. Please change the mobile number."
                                          }
                                      },
                                      "ICICID09": {
                                          "tenure": 9,
                                          "eligibility": {
                                              "status": false,
                                              "reason": "This mobile number is not eligible. Please change the mobile number."
                                          }
                                      }
                                  },
                                  "eligibility": {
                                      "status": false,
                                      "reason": "Customer not eligible for EMI"
                                  }
                              }
                          },
                          "hasEligible": true
                      }
                  }
              }
          }
      }
  }
  has context menu
  ```
</Accordion>

<Accordion title="Response parameters" icon="fa-book">
  ### JSON Format

  ```bash
  {
      "requestId": "12345678", // random id - mandatory
      "transactionDetails": {
        "amount": 12345.12, // mandatory
        "...": "..."
      },
      "customerDetails": {
        // optional
        "mobile": "9098765432", // optional
        "...": "..."
      },
      "filters": {
        // optional - for limiting the data to be fetched
        "paymentOptions": {
          // optional - if not set, will return all payment options
          "emi": {
            // optional - only the requested fields will be returned
            "dc": "SBIN,KKBK,ICIC", // optional - all means, all options under that category, case insensitive
            "...": "..."
          },
          "...": "..."
        },
        "...": "..."
      },
      "useCase": {
        // optional
        "checkCustomerEligibility": true, // optional - default: false.
        "...": "..."
      }
    }
  ```

  ### JSON Fields Description

  | **JSON Field**                     | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **Example**                                                                                                    |
  | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
  | requestId   **mandatory**          | `String` This parameter must contain the request ID.                                                                                                                                                                                                                                                                                                                                                                                                             | 12345678                                                                                                       |
  | transactionDetails   **mandatory** | `JSON` This parameter must contain the following fields in a JSON format as in the example:      - **amount**: This field contains the transaction amount - ` **txnid**: This fields contains the transaction ID.`                                                                                                                                                                                                                                               |  `{       "amount": 12345.12     }`                                                                            |
  | useCase   **mandatory**            | `JSON` This field contains list of fields for which you want get information. For the list of fields and its description, refer to the [Additional Info for General APIs > useCase JSON Field Description](#usecase-json-field-descriptions). table.                                                                                                                                                                                                             | ` {     "getExtendedPaymentDetails": true     }`                                                               |
  | filters   **optional**             | `JSON`This parameter is used to filter the response of this API based on one or more following in the **paymentOptions** field:      - **cc**: Filter the credit cards. - **dc**: Filter the debit cards. - **nb**: Filter the Net Banking - **emi**:  Filter the EMI options. For list of EMI options, refer to [EMI Options for Get Checkout Details API](#emi-options-for-get-checkout-details-api). - **upi**: Filter the UPI - **cash**: Filter the wallets | `{ "paymentOptions":     {       "emi": {                     "dc": "SBIN,KKBK,ICIC"               }      } }` |

  ### useCase JSON Field Description

  | **useCase Field**                        | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                    |
  | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | getExtendedPaymentDetails   **optional** | `Boolean` This flag is posted as **true** to check EMI eligibility based on mobile number and-or card number depending on the payment method used. Also, checks the eligibility for “Buy Now Pay Later” payment modes.   **Example**: Title, EMI amount breakup, etc details are displayed in the response. For a sample request or response using this field, refer to the [Get Extended Payment Details](#get-extended-payment-details) section. |
  | getAdditionalCharges   **optional**      | `Boolean` This flag is posted as **true** to return the additional charges configured for all payment options. For a sample request or response using this field, refer to the [Get Additional Charges](#get-additional-charges) section.   **Note**: You need to use the **getTaxSpecification** field if you want to calculate the tax split of additional charges on their end.                                                                 |
  | getTaxSpecification` `**optional**       | `Boolean` This flag is posted as **true** to returns the tax specification configured on the backend. Clients can use the result to show the split of additional charges for each payment option. For a sample request or response using this field, refer to the [Get Tax Specification](#get-tax-specification) section.                                                                                                                         |
  | checkDownStatus` `**optional**           | `Boolean` This flag is posted as **true** to return the downtime of the payment options. For a sample request or response using this field, refer to [Check Down Status](#check-down-status) field.                                                                                                                                                                                                                                                |
  | checkCustomerEligibility   **optional**  | `Boolean` This flag is posted as **true** to return the customer eligibility. For a sample request or response using this field, refer to [Check Customer Eligibility](#check-customer-eligibility)  field.                                                                                                                                                                                                                                        |
</Accordion>

<Accordion title="Additional information for request parameters" icon="fa-book">
  | Parameter | Reference                                                                                                                                                                                                                                                                                        |           |        |                 |
  | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------- | ------ | --------------- |
  | **key**   | For more information on how to generate the Key and Salt, refer to any of the following:      - **Production**: [Generate Merchant Key and Salt](#generate-merchant-key-and-salt-on-payu-dashboard)      - **Test**: [Generate Test Merchant Key and Salt](#generate-test-merchant-key-and-salt) |           |        |                 |
  | **hash**  | Hash logic for this API is:   \`sha512(key\\                                                                                                                                                                                                                                                     | command\\ | var1\\ | salt) sha512 \` |
  | var1      | For JSON fields description, refer to [var1 JSON fields description](#var1-JSON-fields-description).                                                                                                                                                                                             |           |        |                 |

  ### var1 JSON fields description

  | **JSON Field**                     | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **Example**                                                                                                    |
  | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
  | requestId   **mandatory**          | `String` This parameter must contain the request ID.                                                                                                                                                                                                                                                                                                                                                                                                             | 12345678                                                                                                       |
  | transactionDetails   **mandatory** | `JSON` This parameter must contain the following fields in a JSON format as in the example:      - **amount**: This field contains the transaction amount - ` **txnid**: This fields contains the transaction ID.`                                                                                                                                                                                                                                               |  `{       "amount": 12345.12     }`                                                                            |
  | useCase   **mandatory**            | `JSON` This field contains list of fields for which you want get information. For the list of fields and its description, refer to the [useCase JSON field descriptions](#usecase-json-field-descriptions). table.                                                                                                                                                                                                                                               | ` {     "getExtendedPaymentDetails": true     }`                                                               |
  | filters   **optional**             | `JSON`This parameter is used to filter the response of this API based on one or more following in the **paymentOptions** field:      - **cc**: Filter the credit cards. - **dc**: Filter the debit cards. - **nb**: Filter the Net Banking - **emi**:  Filter the EMI options. For list of EMI options, refer to [EMI Options for Get Checkout Details API](#emi-options-for-get-checkout-details-api). - **upi**: Filter the UPI - **cash**: Filter the wallets | `{ "paymentOptions":     {       "emi": {                     "dc": "SBIN,KKBK,ICIC"               }      } }` |

  ### useCase JSON field descriptions

  | **useCase Field**                   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                |
  | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | getExtendedPaymentDetails`optional` | `Boolean` This flag is posted as **true** to check EMI eligibility based on mobile number and-or card number depending on the payment method used. Also, checks the eligibility for “Buy Now Pay Later” payment modes. **Example**: Title, EMI amount breakup, etc details are displayed in the response. For a sample request or response using this field, refer to the [Get Extended Payment Details](#getExtendedPaymentDetails)  section. |
  | getAdditionalCharges`optional`      | `Boolean` This flag is posted as **true** to return the additional charges configured for all payment options. For a sample request or response using this field, refer to the [Get Additional Charges](#getAdditionalCharges) section. **Note**: You need to use the **getTaxSpecification** field if you want to calculate the tax split of additional charges on their end.                                                                 |
  | getTaxSpecification`optional`       | `Boolean` This flag is posted as **true** to returns the tax specification configured on the backend. Clients can use the result to show the split of additional charges for each payment option. For a sample request or response using this field, refer to the [Get Tax Specification](#getTaxSpecification) section.                                                                                                                       |
  | checkDownStatus`optional`           | `Boolean` This flag is posted as **true** to return the downtime of the payment options. For a sample request or response using this field, refer to [Check Down Status](#checkDownStatus) field.                                                                                                                                                                                                                                              |
</Accordion>
