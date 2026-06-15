---
title: Get EMI/BNPL Checkout Details API - LazyPay Pay-in-3
deprecated: false
hidden: true
metadata:
  robots: index
---
This reference describes Get Checkout Details `get_checkout_details` API to check Pay-in-Parts lenders eligibility. You will get response for various scenarios whether customer is Existing to Bank (ETB) or New to Bank (NTB) customer.

## Environment

| Environment | URL                                                |
| :---------- | :------------------------------------------------- |
| Production  | `https://info.payu.in/merchant/postservice?form=2` |
| Test        | `https://test.payu.in/merchant/postservice?form=2` |

<br />

## Request Parameters

<Accordion title="Request Parameters" icon="fa-info-table">

<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>key<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Merchant key from the PayU Dashboard (masked test style: <code>JP***g</code> in samples).</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>JP***g</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>command<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Must be <code>get_checkout_details</code>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>get_checkout_details</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var1<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> JSON Object containing the fields to check eligibility. For more information, refer to  <a href="#var1-json-fields-description">var1 JSON Fields Description</a></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{"requestId":"abc123","transactionDetails":{"amount":500}}</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>hash<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> <code>sha512(key|command|var1|SALT)</code> — see <a href="doc:hashing-request-and-response">Hashing request and response</a>. Replace <code>{{info_hash}}</code> with the computed digest.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{info_hash}}</p></td>
</tr>
</tbody>
</table>

#### var1 JSON Fields Description
<Accordion title=" var1 JSON Fields Description" icon="fa-info-circle">
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>requestId<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Unique identifier for this Get Checkout Details call.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>transactionDetails<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Transaction context (amount and optional metadata) used for eligibility.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>transactionDetails.source<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Optional payment-source hint; sample uses <code>null</code>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>null</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>transactionDetails.amount<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Number</code> Amount for which eligibility is evaluated.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>transactionDetails.pre_authorize<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Any</code> Pre-authorization context when applicable; sample uses <code>null</code>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>null</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>transactionDetails.additional_charges<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Any</code> Additional charges when applicable; sample uses <code>null</code>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>null</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>useCase<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Flags that control which eligibility checks GCD performs.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>useCase.checkNTBCustomerEligibility<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> When <code>true</code>, requests new-to-bank (NTB) style checks where supported.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>true</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>useCase.checkCustomerEligibility<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> When <code>true</code>, requests standard customer eligibility.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>true</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>useCase.returnUserLimit<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> When <code>true</code>, may return repeat-user / limit information where supported.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>true</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>customerDetails<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Customer attributes required for EMI / Pay-in-parts lookups.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>customerDetails.mobile<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Mobile number used for lender and Pay-in-parts eligibility.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>filters<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Limits which payment options are returned in the GCD payload.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>filters.paymentOptions<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Wrapper for payment-option filters.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>filters.paymentOptions.emi<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> EMI filters (debit card EMI, cardless EMI, Pay-in-parts).</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>filters.paymentOptions.emi.dc<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Debit-card EMI scope; sample uses <code>"all"</code>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>"all"</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>filters.paymentOptions.emi.cardless<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Cardless EMI scope; sample uses <code>"all"</code>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>"all"</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>filters.paymentOptions.emi.payInParts<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Set to <code>"all"</code> when your pack must return PayInParts lenders (for example LazyPay Pay-in-3 / <code>LAZYPI3</code>) in addition to cardless EMI.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>"all"</p></td>
</tr>
</tbody>
</table>

</Accordion>
</Accordion>

<Accordion title="Sample request" icon="fa-code">

The following matches the integration sample you provided (`Cookie` omitted; `key` shown as `JP***g` like other PayU API reference pages—substitute your real merchant key if different), with `hash` templated.

```curl
curl --location 'https://info.payu.in/merchant/postservice?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=JP***g' \
--data-urlencode 'command=get_checkout_details' \
--data-urlencode 'var1={"requestId":"9078698a15d746feadcffbdaf979a198","transactionDetails":{"source":null,"amount":16721,"pre_authorize":null,"additional_charges":null},"useCase":{"checkNTBCustomerEligibility":true,"checkCustomerEligibility":true,"returnUserLimit":true},"customerDetails":{"mobile":"9910522063"},"filters":{"paymentOptions":{"emi":{"dc":"all","cardless":"all"}}}}' \
--data-urlencode 'hash={{info_hash}}'
```
```python
import requests

url = "https://info.payu.in/merchant/postservice?form=2"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "key": "JP***g",
    "command": "get_checkout_details",
    "var1": '{"requestId":"9078698a15d746feadcffbdaf979a198","transactionDetails":{"source":null,"amount":16721,"pre_authorize":null,"additional_charges":null},"useCase":{"checkNTBCustomerEligibility":true,"checkCustomerEligibility":true,"returnUserLimit":true},"customerDetails":{"mobile":"9910522063"},"filters":{"paymentOptions":{"emi":{"dc":"all","cardless":"all"}}}}',
    "hash": "{{info_hash}}"
}

try:
    response = requests.post(url, headers=headers, data=data)
    print("Status Code:", response.status_code)
    print("Response:", response.text)
except requests.exceptions.RequestException as e:
    print("Error:", e)
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var client = new HttpClient();

        var formData = new List<KeyValuePair<string, string>>
        {
            new KeyValuePair<string, string>("key", "JP***g"),
            new KeyValuePair<string, string>("command", "get_checkout_details"),
            new KeyValuePair<string, string>("var1", "{\"requestId\":\"9078698a15d746feadcffbdaf979a198\",\"transactionDetails\":{\"source\":null,\"amount\":16721,\"pre_authorize\":null,\"additional_charges\":null},\"useCase\":{\"checkNTBCustomerEligibility\":true,\"checkCustomerEligibility\":true,\"returnUserLimit\":true},\"customerDetails\":{\"mobile\":\"9910522063\"},\"filters\":{\"paymentOptions\":{\"emi\":{\"dc\":\"all\",\"cardless\":\"all\"}}}}"),
            new KeyValuePair<string, string>("hash", "{{info_hash}}")
        };

        var content = new FormUrlEncodedContent(formData);

        try
        {
            var response = await client.PostAsync("https://info.payu.in/merchant/postservice?form=2", content);
            string responseBody = await response.Content.ReadAsStringAsync();
            Console.WriteLine("Status Code: " + response.StatusCode);
            Console.WriteLine("Response: " + responseBody);
        }
        catch (HttpRequestException e)
        {
            Console.WriteLine("Error: " + e.Message);
        }
    }
}
```
```javascript
async function getCheckoutDetails() {
    const url = "https://info.payu.in/merchant/postservice?form=2";

    const formData = new URLSearchParams();
    formData.append("key", "JP***g");
    formData.append("command", "get_checkout_details");
    formData.append("var1", JSON.stringify({
        requestId: "9078698a15d746feadcffbdaf979a198",
        transactionDetails: {
            source: null,
            amount: 16721,
            pre_authorize: null,
            additional_charges: null
        },
        useCase: {
            checkNTBCustomerEligibility: true,
            checkCustomerEligibility: true,
            returnUserLimit: true
        },
        customerDetails: {
            mobile: "9910522063"
        },
        filters: {
            paymentOptions: {
                emi: {
                    dc: "all",
                    cardless: "all"
                }
            }
        }
    }));
    formData.append("hash", "{{info_hash}}");

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: formData.toString()
        });

        const data = await response.text();
        console.log("Status Code:", response.status);
        console.log("Response:", data);
    } catch (error) {
        console.error("Error:", error);
    }
}

getCheckoutDetails();
```
```java
import java.io.*;
import java.net.*;

public class GetCheckoutDetails {
    public static void main(String[] args) {
        try {
            URL url = new URL("https://info.payu.in/merchant/postservice?form=2");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
            conn.setDoOutput(true);

            String var1 = URLEncoder.encode(
                "{"requestId":"9078698a15d746feadcffbdaf979a198","transactionDetails":{"source":null,"amount":16721,"pre_authorize":null,"additional_charges":null},"useCase":{"checkNTBCustomerEligibility":true,"checkCustomerEligibility":true,"returnUserLimit":true},"customerDetails":{"mobile":"9910522063"},"filters":{"paymentOptions":{"emi":{"dc":"all","cardless":"all"}}}}",
                "UTF-8"
            );

            String formData = "key=" + URLEncoder.encode("JP***g", "UTF-8")
                + "&command=" + URLEncoder.encode("get_checkout_details", "UTF-8")
                + "&var1=" + var1
                + "&hash=" + URLEncoder.encode("{{info_hash}}", "UTF-8");

            try (OutputStream os = conn.getOutputStream()) {
                os.write(formData.getBytes("UTF-8"));
            }

            int statusCode = conn.getResponseCode();
            System.out.println("Status Code: " + statusCode);

            BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            StringBuilder response = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                response.append(line);
            }
            reader.close();

            System.out.println("Response: " + response.toString());

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```
```php
<?php

$url = "https://info.payu.in/merchant/postservice?form=2";

$postFields = http_build_query([
    "key"     => "JP***g",
    "command" => "get_checkout_details",
    "var1"    => json_encode([
        "requestId"          => "9078698a15d746feadcffbdaf979a198",
        "transactionDetails" => [
            "source"             => null,
            "amount"             => 16721,
            "pre_authorize"      => null,
            "additional_charges" => null
        ],
        "useCase" => [
            "checkNTBCustomerEligibility" => true,
            "checkCustomerEligibility"    => true,
            "returnUserLimit"             => true
        ],
        "customerDetails" => [
            "mobile" => "9910522063"
        ],
        "filters" => [
            "paymentOptions" => [
                "emi" => [
                    "dc"       => "all",
                    "cardless" => "all"
                ]
            ]
        ]
    ]),
    "hash" => "{{info_hash}}"
]);

$ch = curl_init();

curl_setopt_array($ch, [
    CURLOPT_URL            => $url,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST           => true,
    CURLOPT_POSTFIELDS     => $postFields,
    CURLOPT_HTTPHEADER     => [
        "Content-Type: application/x-www-form-urlencoded"
    ]
]);

$response = curl_exec($ch);

if (curl_error($ch)) {
    echo "Error: " . curl_error($ch);
} else {
    echo "Status Code: " . curl_getinfo($ch, CURLINFO_HTTP_CODE) . "\n";
    echo "Response: " . $response . "\n";
}

curl_close($ch);
?>
```
</Accordion>

## Sample response

To surface **PayInParts** lenders in the response (as in the PRD), add `"payInParts":"all"` next to `dc` / `cardless` inside `filters.paymentOptions.emi` when your pack requires it.

### Customer is ETB

**Scenario:** GCD response when the customer is **ETB** (`httpCode` **200**, `status` **1**). The payload is large; structure below is **verbatim** from the PRD transcription (cardless EMI catalogue + `payInParts` block including `LAZYPI3`).

```json
{
  "httpCode": "200",
  "message": "",
  "status": 1,
  "data": {
    "details": {
      "paymentOption": {
        "emi": {
          "all": {
            "cardless": {
              "all": {
                "IDFCCL": {
                  "tenureOptions": {
                    "IDFCCL12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "IDFCCL03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "IDFCCL06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "IDFCCL09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "SMPI3": {
                  "tenureOptions": {
                    "SMPI03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": true
                  }
                },
                "ZESTMON": {
                  "tenureOptions": {
                    "ZEST09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZEST06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZEST03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZESTMON": {
                      "tenure": 0,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZEST12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "ICICCL": {
                  "tenureOptions": {
                    "ICICCL12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "ICICCL03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "ICICCL06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "ICICCL09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "HMECDT": {
                  "tenureOptions": {
                    "HMECDT03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT18": {
                      "tenure": 18,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": true
                  }
                },
                "LPEMI": {
                  "tenureOptions": {
                    "LPEMI12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "Journey Type is not allowed on merchant"
                      }
                    },
                    "LPEMI": {
                      "tenure": 0,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "Journey Type is not allowed on merchant"
                      }
                    },
                    "LPEMI09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "Journey Type is not allowed on merchant"
                      }
                    },
                    "LPEMI03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "Journey Type is not allowed on merchant"
                      }
                    },
                    "LPEMI06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "Journey Type is not allowed on merchant"
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Journey Type is not allowed on merchant"
                  }
                },
                "HDFC_CL": {
                  "tenureOptions": {
                    "HDFCCL09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL18": {
                      "tenure": 18,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": true
                  }
                }
              },
              "hasEligible": true
            }
          },
          "payInParts": {
            "LAZYPI3": {
              "tenure": "3",
              "processingFee": 94.4,
              "processingFeeGst": 14.4,
              "maximumEligibleLimit": 120000.0,
              "eligibility": {
                "status": true
              },
              "repaymentSchedule": [
                {
                  "amount": 4000.0,
                  "serialNo": 0,
                  "dueDate": "2026-06-10"
                },
                {
                  "amount": 4000.0,
                  "serialNo": 1,
                  "dueDate": "2026-08-01"
                },
                {
                  "amount": 4000.0,
                  "serialNo": 2,
                  "dueDate": "2026-09-01"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

### GCD response — customer is NTB

```json
{
  "httpCode": "200",
  "message": "",
  "status": 1,
  "data": {
    "details": {
      "paymentOption": {
        "emi": {
          "all": {
            "cardless": {
              "all": {
                "IDFCCL": {
                  "tenureOptions": {
                    "IDFCCL12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "IDFCCL03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "IDFCCL06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "IDFCCL09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "SMPI3": {
                  "tenureOptions": {
                    "SMPI03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": true
                  }
                },
                "ZESTMON": {
                  "tenureOptions": {
                    "ZEST09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZEST06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZEST03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZESTMON": {
                      "tenure": 0,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZEST12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "ICICCL": {
                  "tenureOptions": {
                    "ICICCL12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "ICICCL03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "ICICCL06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "ICICCL09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "HMECDT": {
                  "tenureOptions": {
                    "HMECDT03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT18": {
                      "tenure": 18,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": true
                  }
                },
                "LPEMI": {
                  "tenureOptions": {
                    "LPEMI12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "LPEMI": {
                      "tenure": 0,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "LPEMI09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "Minimum required amount is 15000"
                      }
                    },
                    "LPEMI03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "LPEMI06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "HDFC_CL": {
                  "tenureOptions": {
                    "HDFCCL09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL18": {
                      "tenure": 18,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": true
                  }
                }
              },
              "hasEligible": true
            }
          },
          "ntb": {
            "payInParts": {
              "all": {
                "LAZYPI3": {
                  "maximumAmount": null,
                  "eligibility": {
                    "status": true
                  }
                }
              },
              "hasEligible": true
            },
            "cardless": {
              "all": {},
              "hasEligible": false
            }
          }
        }
      }
    }
  }
}
```

### GCD response — customer is not eligible

```json
{
  "httpCode": "200",
  "message": "",
  "status": 1,
  "data": {
    "details": {
      "paymentOption": {
        "emi": {
          "all": {
            "cardless": {
              "all": {
                "IDFCCL": {
                  "tenureOptions": {
                    "IDFCCL12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "IDFCCL03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "IDFCCL06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "IDFCCL09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "SMPI3": {
                  "tenureOptions": {
                    "SMPI03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": true
                  }
                },
                "ZESTMON": {
                  "tenureOptions": {
                    "ZEST09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZEST06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZEST03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZESTMON": {
                      "tenure": 0,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "ZEST12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "ICICCL": {
                  "tenureOptions": {
                    "ICICCL12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "ICICCL03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "ICICCL06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    },
                    "ICICCL09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "API Time Out"
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "HMECDT": {
                  "tenureOptions": {
                    "HMECDT03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT18": {
                      "tenure": 18,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    },
                    "HMECDT09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 12000.0
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": true
                  }
                },
                "LPEMI": {
                  "tenureOptions": {
                    "LPEMI12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "LPEMI": {
                      "tenure": 0,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "LPEMI09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "Minimum required amount is 15000"
                      }
                    },
                    "LPEMI03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    },
                    "LPEMI06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                },
                "HDFC_CL": {
                  "tenureOptions": {
                    "HDFCCL09": {
                      "tenure": 9,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL18": {
                      "tenure": 18,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL06": {
                      "tenure": 6,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL03": {
                      "tenure": 3,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "HDFCCL12": {
                      "tenure": 12,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    }
                  },
                  "maximumAmount": null,
                  "eligibility": {
                    "status": true
                  }
                }
              },
              "hasEligible": true
            }
          },
          "payInParts": {
            "LAZYPI3": {
              "tenure": "3",
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
}
```

<br />
