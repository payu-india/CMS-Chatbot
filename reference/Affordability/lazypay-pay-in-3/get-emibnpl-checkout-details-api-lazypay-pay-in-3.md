---
title: Get EMI/BNPL Checkout Details API - LazyPay Pay-in-3
deprecated: false
hidden: true
metadata:
  robots: index
---
This reference describes `command=get_checkout_details` on `POST /merchant/postservice?form=2` when you use `var1` filters for **cardless EMI** and **PayInParts** lenders (including **LazyPay Pay-in-3**). It is **standalone** for PayInParts / Pay-in-3 workstreams only.

**Source for sample response:** Transcribed from `Seamless-Response for GCD and GECD for PayInParts Lenders-120626-053241.pdf` — same JSON as in [`PRDs/Lazypay/seamless-response-gcd-gecd-payinparts-lenders.md`](../../../../PRDs/Lazypay/seamless-response-gcd-gecd-payinparts-lenders.md) (section **GCD response — customer is ETB**).

## Environment

| Environment | URL                                                |
| :---------- | :------------------------------------------------- |
| Production  | `https://info.payu.in/merchant/postservice?form=2` |
| Test        | `https://test.payu.in/merchant/postservice?form=2` |

Some gateways still accept `postservice.php?form=2`. Confirm with your **PayU Key Account Manager (KAM)**.

## Request Parameters

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> JSON string containing:<br>
• <code>requestId</code><br>
• <code>transactionDetails</code> (e.g. <code>amount</code>, <code>source</code>, <code>pre_authorize</code>, <code>additional_charges</code>)<br>
• <code>useCase</code> (e.g. <code>checkCustomerEligibility</code>, <code>checkNTBCustomerEligibility</code>, <code>returnUserLimit</code>)<br>
• <code>customerDetails</code> (e.g. <code>mobile</code>)<br>
• <code>filters.paymentOptions.emi</code> (e.g. <code>dc</code>, <code>cardless</code>, and <code>payInParts</code> when you need Pay-in-parts lenders in the response)</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{"requestId":"abc123","transactionDetails":{"amount":500}}</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>hash<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> <code>sha512(key|command|var1|SALT)</code> — see <a href="doc:hashing-request-and-response">Hashing request and response</a>. Replace <code>{{info_hash}}</code> with the computed digest.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{info_hash}}</p></td>
</tr>
</tbody>
</table>


<br />

## Sample request

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


To surface **PayInParts** lenders in the response (as in the PRD), add `"payInParts":"all"` next to `dc` / `cardless` inside `filters.paymentOptions.emi` when your pack requires it.

## Sample response (ETB — from PayInParts lenders PDF)

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

## GCD response — customer is NTB

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

## GCD response — customer is not eligible

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