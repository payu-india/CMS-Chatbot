---
api:
  file: payment-link-33.json
  operationId: CreatePaymentLinkAPI
hidden: false
metadata:
  title: Create a Payment Link API
  description: >-
    The Create a Payment Link API allows users to generate payment links for
    customers, requiring an access token with the "create_payment_links" scope,
    and supports both test and production environments.
  keywords:
    - Create a Payment Link API
    - Payment Link Creation API
    - Share Payment Link API
    - ' Send Payment Link API'
    - ' SI Payment Link'
    - ' Recurring Payment Link'
  robots: index
next:
  description: ''
---
# Create Payment Link API

The **Create a Payment Link** API is used to create a regular payment link, recurring or SI payment link for your customer.

## Environment

| | |
|:--|:--|
| Test Environment | https://uatoneapi.payu.in/payment-links/ |
| Production Environment | https://oneapi.payu.in/payment-links/ |

> **Notes:**
> - The access token with the scope as **create_payment_links** is required on the header.
> - To create a seamless eNACH payment link, the **enforcePayMethod** parameter must be passed with "enach" as the only method.

---

## Sample Requests

### Create a payment link

```curl
curl --location -g --request POST 'https://uatoneapi.payu.in/payment-links/' \
--header 'merchantId: {{merchantId}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data-raw '{
  "subAmount": 2,
  "isPartialPaymentAllowed": false,
  "description": "paymentLink for testing",
  "source": "API"
}'
```
```python
import http.client
import json

conn = http.client.HTTPSConnection("uatoneapi.payu.in")
payload = json.dumps({
    "subAmount": 2,
    "isPartialPaymentAllowed": False,
    "description": "paymentLink for testing",
    "source": "API"
})
headers = {
    "merchantId": "{{merchantId}}",
    "Content-Type": "application/json",
    "Authorization": "Bearer {{access_token}}"
}
conn.request("POST", "/payment-links/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        try
        {
            string url = "https://uatoneapi.payu.in/payment-links/";
            string jsonBody = "{\"subAmount\": 2, \"isPartialPaymentAllowed\": false, \"description\": \"paymentLink for testing\", \"source\": \"API\"}";

            var request = new HttpRequestMessage(HttpMethod.Post, url);
            request.Headers.Add("merchantId", "{{merchantId}}");
            request.Headers.Add("Authorization", "Bearer {{access_token}}");
            request.Content = new StringContent(jsonBody, Encoding.UTF8, "application/json");

            HttpResponseMessage response = await client.SendAsync(request);
            string responseContent = await response.Content.ReadAsStringAsync();
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {responseContent}");
        }
        catch (HttpRequestException e)
        {
            Console.WriteLine($"Error: {e.Message}");
        }
    }
}
```
```javascript
async function createPaymentLink() {
    const url = "https://uatoneapi.payu.in/payment-links/";
    const body = JSON.stringify({
        subAmount: 2,
        isPartialPaymentAllowed: false,
        description: "paymentLink for testing",
        source: "API"
    });

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "merchantId": "{{merchantId}}",
                "Content-Type": "application/json",
                "Authorization": "Bearer {{access_token}}"
            },
            body: body
        });
        const responseText = await response.text();
        console.log(`Status: ${response.status}`);
        console.log(`Response: ${responseText}`);
    } catch (error) {
        console.error("Error:", error);
    }
}

createPaymentLink();
```
```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class CreatePaymentLink {
    public static void main(String[] args) {
        try {
            String url = "https://uatoneapi.payu.in/payment-links/";
            String jsonBody = "{\"subAmount\": 2, \"isPartialPaymentAllowed\": false, \"description\": \"paymentLink for testing\", \"source\": \"API\"}";

            URL urlObj = new URL(url);
            HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("merchantId", "{{merchantId}}");
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Authorization", "Bearer {{access_token}}");
            connection.setDoOutput(true);

            try (OutputStream os = connection.getOutputStream()) {
                byte[] input = jsonBody.getBytes(StandardCharsets.UTF_8);
                os.write(input, 0, input.length);
            }

            int responseCode = connection.getResponseCode();
            System.out.println("Status Code: " + responseCode);

            try (BufferedReader br = new BufferedReader(new InputStreamReader(
                    responseCode >= 200 && responseCode < 300
                        ? connection.getInputStream()
                        : connection.getErrorStream(), StandardCharsets.UTF_8))) {
                StringBuilder response = new StringBuilder();
                String responseLine;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }
                System.out.println("Response: " + response.toString());
            }
            connection.disconnect();
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
```php
<?php
function createPaymentLink() {
    $url = "https://uatoneapi.payu.in/payment-links/";
    $body = json_encode([
        "subAmount" => 2,
        "isPartialPaymentAllowed" => false,
        "description" => "paymentLink for testing",
        "source" => "API"
    ]);

    $curl = curl_init();
    curl_setopt_array($curl, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $body,
        CURLOPT_HTTPHEADER => [
            "merchantId: {{merchantId}}",
            "Content-Type: application/json",
            "Authorization: Bearer {{access_token}}"
        ],
        CURLOPT_TIMEOUT => 30,
        CURLOPT_SSL_VERIFYPEER => true
    ]);

    $response = curl_exec($curl);
    $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
    $error = curl_error($curl);
    curl_close($curl);

    if ($error) {
        echo "cURL Error: " . $error . PHP_EOL;
        return false;
    }

    echo "Status Code: " . $httpCode . PHP_EOL;
    echo "Response: " . $response . PHP_EOL;
}

createPaymentLink();
?>
```

---

### Create an open-invoice payment link

Set `isAmountFilledByCustomer` to `true`. In this flow, `subAmount` must be `null` because the customer enters the amount.

```curl
curl --location -g --request POST 'https://uatoneapi.payu.in/payment-links/' \
--header 'merchantId: {{merchantId}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data-raw '{
  "isAmountFilledByCustomer": true,
  "subAmount": null,
  "description": "Customer-entered payment for {{customerReference}}",
  "source": "API"
}'
```
```python
import http.client
import json

conn = http.client.HTTPSConnection("uatoneapi.payu.in")
payload = json.dumps({
    "isAmountFilledByCustomer": True,
    "subAmount": None,
    "description": "Customer-entered payment for {{customerReference}}",
    "source": "API"
})
headers = {
    "merchantId": "{{merchantId}}",
    "Content-Type": "application/json",
    "Authorization": "Bearer {{access_token}}"
}
conn.request("POST", "/payment-links/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        try
        {
            string url = "https://uatoneapi.payu.in/payment-links/";
            string jsonBody = "{\"isAmountFilledByCustomer\": true, \"subAmount\": null, \"description\": \"Customer-entered payment for {{customerReference}}\", \"source\": \"API\"}";

            var request = new HttpRequestMessage(HttpMethod.Post, url);
            request.Headers.Add("merchantId", "{{merchantId}}");
            request.Headers.Add("Authorization", "Bearer {{access_token}}");
            request.Content = new StringContent(jsonBody, Encoding.UTF8, "application/json");

            HttpResponseMessage response = await client.SendAsync(request);
            string responseContent = await response.Content.ReadAsStringAsync();
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {responseContent}");
        }
        catch (HttpRequestException e)
        {
            Console.WriteLine($"Error: {e.Message}");
        }
    }
}
```
```javascript
async function createOpenInvoiceLink() {
    const url = "https://uatoneapi.payu.in/payment-links/";
    const body = JSON.stringify({
        isAmountFilledByCustomer: true,
        subAmount: null,
        description: "Customer-entered payment for {{customerReference}}",
        source: "API"
    });

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "merchantId": "{{merchantId}}",
                "Content-Type": "application/json",
                "Authorization": "Bearer {{access_token}}"
            },
            body: body
        });
        const responseText = await response.text();
        console.log(`Status: ${response.status}`);
        console.log(`Response: ${responseText}`);
    } catch (error) {
        console.error("Error:", error);
    }
}

createOpenInvoiceLink();
```
```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class CreateOpenInvoiceLink {
    public static void main(String[] args) {
        try {
            String url = "https://uatoneapi.payu.in/payment-links/";
            String jsonBody = "{\"isAmountFilledByCustomer\": true, \"subAmount\": null, \"description\": \"Customer-entered payment for {{customerReference}}\", \"source\": \"API\"}";

            URL urlObj = new URL(url);
            HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("merchantId", "{{merchantId}}");
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Authorization", "Bearer {{access_token}}");
            connection.setDoOutput(true);

            try (OutputStream os = connection.getOutputStream()) {
                byte[] input = jsonBody.getBytes(StandardCharsets.UTF_8);
                os.write(input, 0, input.length);
            }

            int responseCode = connection.getResponseCode();
            System.out.println("Status Code: " + responseCode);

            try (BufferedReader br = new BufferedReader(new InputStreamReader(
                    responseCode >= 200 && responseCode < 300
                        ? connection.getInputStream()
                        : connection.getErrorStream(), StandardCharsets.UTF_8))) {
                StringBuilder response = new StringBuilder();
                String responseLine;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }
                System.out.println("Response: " + response.toString());
            }
            connection.disconnect();
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
```php
<?php
function createOpenInvoiceLink() {
    $url = "https://uatoneapi.payu.in/payment-links/";
    $body = json_encode([
        "isAmountFilledByCustomer" => true,
        "subAmount" => null,
        "description" => "Customer-entered payment for {{customerReference}}",
        "source" => "API"
    ]);

    $curl = curl_init();
    curl_setopt_array($curl, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $body,
        CURLOPT_HTTPHEADER => [
            "merchantId: {{merchantId}}",
            "Content-Type: application/json",
            "Authorization: Bearer {{access_token}}"
        ],
        CURLOPT_TIMEOUT => 30,
        CURLOPT_SSL_VERIFYPEER => true
    ]);

    $response = curl_exec($curl);
    $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
    $error = curl_error($curl);
    curl_close($curl);

    if ($error) {
        echo "cURL Error: " . $error . PHP_EOL;
        return false;
    }

    echo "Status Code: " . $httpCode . PHP_EOL;
    echo "Response: " . $response . PHP_EOL;
}

createOpenInvoiceLink();
?>
```

---

### Allow partial payments

Set `isPartialPaymentAllowed` to `true`. Use `minAmountForCustomer` when the customer must pay at least a specified amount.

```curl
curl --location -g --request POST 'https://uatoneapi.payu.in/payment-links/' \
--header 'merchantId: {{merchantId}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data-raw '{
  "subAmount": 5000,
  "isPartialPaymentAllowed": true,
  "minAmountForCustomer": 500,
  "paymentDeadline": "2026-10-15 23:59:59",
  "description": "Part-payment for order {{orderId}}",
  "source": "API"
}'
```
```python
import http.client
import json

conn = http.client.HTTPSConnection("uatoneapi.payu.in")
payload = json.dumps({
    "subAmount": 5000,
    "isPartialPaymentAllowed": True,
    "minAmountForCustomer": 500,
    "paymentDeadline": "2026-10-15 23:59:59",
    "description": "Part-payment for order {{orderId}}",
    "source": "API"
})
headers = {
    "merchantId": "{{merchantId}}",
    "Content-Type": "application/json",
    "Authorization": "Bearer {{access_token}}"
}
conn.request("POST", "/payment-links/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        try
        {
            string url = "https://uatoneapi.payu.in/payment-links/";
            string jsonBody = "{\"subAmount\": 5000, \"isPartialPaymentAllowed\": true, \"minAmountForCustomer\": 500, \"paymentDeadline\": \"2026-10-15 23:59:59\", \"description\": \"Part-payment for order {{orderId}}\", \"source\": \"API\"}";

            var request = new HttpRequestMessage(HttpMethod.Post, url);
            request.Headers.Add("merchantId", "{{merchantId}}");
            request.Headers.Add("Authorization", "Bearer {{access_token}}");
            request.Content = new StringContent(jsonBody, Encoding.UTF8, "application/json");

            HttpResponseMessage response = await client.SendAsync(request);
            string responseContent = await response.Content.ReadAsStringAsync();
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {responseContent}");
        }
        catch (HttpRequestException e)
        {
            Console.WriteLine($"Error: {e.Message}");
        }
    }
}
```
```javascript
async function allowPartialPayments() {
    const url = "https://uatoneapi.payu.in/payment-links/";
    const body = JSON.stringify({
        subAmount: 5000,
        isPartialPaymentAllowed: true,
        minAmountForCustomer: 500,
        paymentDeadline: "2026-10-15 23:59:59",
        description: "Part-payment for order {{orderId}}",
        source: "API"
    });

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "merchantId": "{{merchantId}}",
                "Content-Type": "application/json",
                "Authorization": "Bearer {{access_token}}"
            },
            body: body
        });
        const responseText = await response.text();
        console.log(`Status: ${response.status}`);
        console.log(`Response: ${responseText}`);
    } catch (error) {
        console.error("Error:", error);
    }
}

allowPartialPayments();
```
```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class AllowPartialPayments {
    public static void main(String[] args) {
        try {
            String url = "https://uatoneapi.payu.in/payment-links/";
            String jsonBody = "{\"subAmount\": 5000, \"isPartialPaymentAllowed\": true, \"minAmountForCustomer\": 500, \"paymentDeadline\": \"2026-10-15 23:59:59\", \"description\": \"Part-payment for order {{orderId}}\", \"source\": \"API\"}";

            URL urlObj = new URL(url);
            HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("merchantId", "{{merchantId}}");
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Authorization", "Bearer {{access_token}}");
            connection.setDoOutput(true);

            try (OutputStream os = connection.getOutputStream()) {
                byte[] input = jsonBody.getBytes(StandardCharsets.UTF_8);
                os.write(input, 0, input.length);
            }

            int responseCode = connection.getResponseCode();
            System.out.println("Status Code: " + responseCode);

            try (BufferedReader br = new BufferedReader(new InputStreamReader(
                    responseCode >= 200 && responseCode < 300
                        ? connection.getInputStream()
                        : connection.getErrorStream(), StandardCharsets.UTF_8))) {
                StringBuilder response = new StringBuilder();
                String responseLine;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }
                System.out.println("Response: " + response.toString());
            }
            connection.disconnect();
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
```php
<?php
function allowPartialPayments() {
    $url = "https://uatoneapi.payu.in/payment-links/";
    $body = json_encode([
        "subAmount" => 5000,
        "isPartialPaymentAllowed" => true,
        "minAmountForCustomer" => 500,
        "paymentDeadline" => "2026-10-15 23:59:59",
        "description" => "Part-payment for order {{orderId}}",
        "source" => "API"
    ]);

    $curl = curl_init();
    curl_setopt_array($curl, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $body,
        CURLOPT_HTTPHEADER => [
            "merchantId: {{merchantId}}",
            "Content-Type: application/json",
            "Authorization: Bearer {{access_token}}"
        ],
        CURLOPT_TIMEOUT => 30,
        CURLOPT_SSL_VERIFYPEER => true
    ]);

    $response = curl_exec($curl);
    $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
    $error = curl_error($curl);
    curl_close($curl);

    if ($error) {
        echo "cURL Error: " . $error . PHP_EOL;
        return false;
    }

    echo "Status Code: " . $httpCode . PHP_EOL;
    echo "Response: " . $response . PHP_EOL;
}

allowPartialPayments();
?>
```

---

### Create a recurring or SI payment link

Use `si_payment_link` as the `source` and provide the recurring schedule in `siDetails`.

```curl
curl --location -g --request POST 'https://uatoneapi.payu.in/payment-links/' \
--header 'merchantId: {{merchantId}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data-raw '{
  "subAmount": 500,
  "description": "Monthly subscription for {{customerId}}",
  "source": "si_payment_link",
  "siDetails": {
    "billingAmount": 500,
    "billingCurrency": "INR",
    "billingCycle": "MONTHLY",
    "billingInterval": 1,
    "paymentStartDate": "2026-10-01",
    "paymentEndDate": "2027-09-30"
  }
}'
```
```python
import http.client
import json

conn = http.client.HTTPSConnection("uatoneapi.payu.in")
payload = json.dumps({
    "subAmount": 500,
    "description": "Monthly subscription for {{customerId}}",
    "source": "si_payment_link",
    "siDetails": {
        "billingAmount": 500,
        "billingCurrency": "INR",
        "billingCycle": "MONTHLY",
        "billingInterval": 1,
        "paymentStartDate": "2026-10-01",
        "paymentEndDate": "2027-09-30"
    }
})
headers = {
    "merchantId": "{{merchantId}}",
    "Content-Type": "application/json",
    "Authorization": "Bearer {{access_token}}"
}
conn.request("POST", "/payment-links/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        try
        {
            string url = "https://uatoneapi.payu.in/payment-links/";
            string jsonBody = @"{
                \"subAmount\": 500,
                \"description\": \"Monthly subscription for {{customerId}}\",
                \"source\": \"si_payment_link\",
                \"siDetails\": {
                    \"billingAmount\": 500,
                    \"billingCurrency\": \"INR\",
                    \"billingCycle\": \"MONTHLY\",
                    \"billingInterval\": 1,
                    \"paymentStartDate\": \"2026-10-01\",
                    \"paymentEndDate\": \"2027-09-30\"
                }
            }";

            var request = new HttpRequestMessage(HttpMethod.Post, url);
            request.Headers.Add("merchantId", "{{merchantId}}");
            request.Headers.Add("Authorization", "Bearer {{access_token}}");
            request.Content = new StringContent(jsonBody, Encoding.UTF8, "application/json");

            HttpResponseMessage response = await client.SendAsync(request);
            string responseContent = await response.Content.ReadAsStringAsync();
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {responseContent}");
        }
        catch (HttpRequestException e)
        {
            Console.WriteLine($"Error: {e.Message}");
        }
    }
}
```
```javascript
async function createSIPaymentLink() {
    const url = "https://uatoneapi.payu.in/payment-links/";
    const body = JSON.stringify({
        subAmount: 500,
        description: "Monthly subscription for {{customerId}}",
        source: "si_payment_link",
        siDetails: {
            billingAmount: 500,
            billingCurrency: "INR",
            billingCycle: "MONTHLY",
            billingInterval: 1,
            paymentStartDate: "2026-10-01",
            paymentEndDate: "2027-09-30"
        }
    });

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "merchantId": "{{merchantId}}",
                "Content-Type": "application/json",
                "Authorization": "Bearer {{access_token}}"
            },
            body: body
        });
        const responseText = await response.text();
        console.log(`Status: ${response.status}`);
        console.log(`Response: ${responseText}`);
    } catch (error) {
        console.error("Error:", error);
    }
}

createSIPaymentLink();
```
```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class CreateSIPaymentLink {
    public static void main(String[] args) {
        try {
            String url = "https://uatoneapi.payu.in/payment-links/";
            String jsonBody = "{\"subAmount\": 500, \"description\": \"Monthly subscription for {{customerId}}\", \"source\": \"si_payment_link\", \"siDetails\": {\"billingAmount\": 500, \"billingCurrency\": \"INR\", \"billingCycle\": \"MONTHLY\", \"billingInterval\": 1, \"paymentStartDate\": \"2026-10-01\", \"paymentEndDate\": \"2027-09-30\"}}";

            URL urlObj = new URL(url);
            HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("merchantId", "{{merchantId}}");
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Authorization", "Bearer {{access_token}}");
            connection.setDoOutput(true);

            try (OutputStream os = connection.getOutputStream()) {
                byte[] input = jsonBody.getBytes(StandardCharsets.UTF_8);
                os.write(input, 0, input.length);
            }

            int responseCode = connection.getResponseCode();
            System.out.println("Status Code: " + responseCode);

            try (BufferedReader br = new BufferedReader(new InputStreamReader(
                    responseCode >= 200 && responseCode < 300
                        ? connection.getInputStream()
                        : connection.getErrorStream(), StandardCharsets.UTF_8))) {
                StringBuilder response = new StringBuilder();
                String responseLine;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }
                System.out.println("Response: " + response.toString());
            }
            connection.disconnect();
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
```php
<?php
function createSIPaymentLink() {
    $url = "https://uatoneapi.payu.in/payment-links/";
    $body = json_encode([
        "subAmount" => 500,
        "description" => "Monthly subscription for {{customerId}}",
        "source" => "si_payment_link",
        "siDetails" => [
            "billingAmount" => 500,
            "billingCurrency" => "INR",
            "billingCycle" => "MONTHLY",
            "billingInterval" => 1,
            "paymentStartDate" => "2026-10-01",
            "paymentEndDate" => "2027-09-30"
        ]
    ]);

    $curl = curl_init();
    curl_setopt_array($curl, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $body,
        CURLOPT_HTTPHEADER => [
            "merchantId: {{merchantId}}",
            "Content-Type: application/json",
            "Authorization: Bearer {{access_token}}"
        ],
        CURLOPT_TIMEOUT => 30,
        CURLOPT_SSL_VERIFYPEER => true
    ]);

    $response = curl_exec($curl);
    $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
    $error = curl_error($curl);
    curl_close($curl);

    if ($error) {
        echo "cURL Error: " . $error . PHP_EOL;
        return false;
    }

    echo "Status Code: " . $httpCode . PHP_EOL;
    echo "Response: " . $response . PHP_EOL;
}

createSIPaymentLink();
?>
```

---

### Create a seamless eNACH payment link

For a seamless eNACH link, pass `enforcePayMethod` with `enach` as the only method. The eNACH `bankDetails` object is nested inside `siDetails`.

```curl
curl --location -g --request POST 'https://uatoneapi.payu.in/payment-links/' \
--header 'merchantId: {{merchantId}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data-raw '{
  "subAmount": 500,
  "description": "eNACH subscription for {{customerId}}",
  "source": "si_payment_link",
  "enforcePayMethod": "enach",
  "siDetails": {
    "billingAmount": 500,
    "billingCycle": "MONTHLY",
    "paymentStartDate": "2026-10-01",
    "bankDetails": {
      "bankCode": "{{bankCode}}",
      "bankAccountNumber": "{{customerBankAccountNumber}}",
      "ifsc": "{{customerIfsc}}",
      "accountType": "SAVINGS"
    }
  }
}'
```
```python
import http.client
import json

conn = http.client.HTTPSConnection("uatoneapi.payu.in")
payload = json.dumps({
    "subAmount": 500,
    "description": "eNACH subscription for {{customerId}}",
    "source": "si_payment_link",
    "enforcePayMethod": "enach",
    "siDetails": {
        "billingAmount": 500,
        "billingCycle": "MONTHLY",
        "paymentStartDate": "2026-10-01",
        "bankDetails": {
            "bankCode": "{{bankCode}}",
            "bankAccountNumber": "{{customerBankAccountNumber}}",
            "ifsc": "{{customerIfsc}}",
            "accountType": "SAVINGS"
        }
    }
})
headers = {
    "merchantId": "{{merchantId}}",
    "Content-Type": "application/json",
    "Authorization": "Bearer {{access_token}}"
}
conn.request("POST", "/payment-links/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        try
        {
            string url = "https://uatoneapi.payu.in/payment-links/";
            string jsonBody = @"{
                \"subAmount\": 500,
                \"description\": \"eNACH subscription for {{customerId}}\",
                \"source\": \"si_payment_link\",
                \"enforcePayMethod\": \"enach\",
                \"siDetails\": {
                    \"billingAmount\": 500,
                    \"billingCycle\": \"MONTHLY\",
                    \"paymentStartDate\": \"2026-10-01\",
                    \"bankDetails\": {
                        \"bankCode\": \"{{bankCode}}\",
                        \"bankAccountNumber\": \"{{customerBankAccountNumber}}\",
                        \"ifsc\": \"{{customerIfsc}}\",
                        \"accountType\": \"SAVINGS\"
                    }
                }
            }";

            var request = new HttpRequestMessage(HttpMethod.Post, url);
            request.Headers.Add("merchantId", "{{merchantId}}");
            request.Headers.Add("Authorization", "Bearer {{access_token}}");
            request.Content = new StringContent(jsonBody, Encoding.UTF8, "application/json");

            HttpResponseMessage response = await client.SendAsync(request);
            string responseContent = await response.Content.ReadAsStringAsync();
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {responseContent}");
        }
        catch (HttpRequestException e)
        {
            Console.WriteLine($"Error: {e.Message}");
        }
    }
}
```
```javascript
async function createENachLink() {
    const url = "https://uatoneapi.payu.in/payment-links/";
    const body = JSON.stringify({
        subAmount: 500,
        description: "eNACH subscription for {{customerId}}",
        source: "si_payment_link",
        enforcePayMethod: "enach",
        siDetails: {
            billingAmount: 500,
            billingCycle: "MONTHLY",
            paymentStartDate: "2026-10-01",
            bankDetails: {
                bankCode: "{{bankCode}}",
                bankAccountNumber: "{{customerBankAccountNumber}}",
                ifsc: "{{customerIfsc}}",
                accountType: "SAVINGS"
            }
        }
    });

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "merchantId": "{{merchantId}}",
                "Content-Type": "application/json",
                "Authorization": "Bearer {{access_token}}"
            },
            body: body
        });
        const responseText = await response.text();
        console.log(`Status: ${response.status}`);
        console.log(`Response: ${responseText}`);
    } catch (error) {
        console.error("Error:", error);
    }
}

createENachLink();
```
```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class CreateENachLink {
    public static void main(String[] args) {
        try {
            String url = "https://uatoneapi.payu.in/payment-links/";
            String jsonBody = "{\"subAmount\": 500, \"description\": \"eNACH subscription for {{customerId}}\", \"source\": \"si_payment_link\", \"enforcePayMethod\": \"enach\", \"siDetails\": {\"billingAmount\": 500, \"billingCycle\": \"MONTHLY\", \"paymentStartDate\": \"2026-10-01\", \"bankDetails\": {\"bankCode\": \"{{bankCode}}\", \"bankAccountNumber\": \"{{customerBankAccountNumber}}\", \"ifsc\": \"{{customerIfsc}}\", \"accountType\": \"SAVINGS\"}}}";

            URL urlObj = new URL(url);
            HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("merchantId", "{{merchantId}}");
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Authorization", "Bearer {{access_token}}");
            connection.setDoOutput(true);

            try (OutputStream os = connection.getOutputStream()) {
                byte[] input = jsonBody.getBytes(StandardCharsets.UTF_8);
                os.write(input, 0, input.length);
            }

            int responseCode = connection.getResponseCode();
            System.out.println("Status Code: " + responseCode);

            try (BufferedReader br = new BufferedReader(new InputStreamReader(
                    responseCode >= 200 && responseCode < 300
                        ? connection.getInputStream()
                        : connection.getErrorStream(), StandardCharsets.UTF_8))) {
                StringBuilder response = new StringBuilder();
                String responseLine;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }
                System.out.println("Response: " + response.toString());
            }
            connection.disconnect();
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
```php
<?php
function createENachLink() {
    $url = "https://uatoneapi.payu.in/payment-links/";
    $body = json_encode([
        "subAmount" => 500,
        "description" => "eNACH subscription for {{customerId}}",
        "source" => "si_payment_link",
        "enforcePayMethod" => "enach",
        "siDetails" => [
            "billingAmount" => 500,
            "billingCycle" => "MONTHLY",
            "paymentStartDate" => "2026-10-01",
            "bankDetails" => [
                "bankCode" => "{{bankCode}}",
                "bankAccountNumber" => "{{customerBankAccountNumber}}",
                "ifsc" => "{{customerIfsc}}",
                "accountType" => "SAVINGS"
            ]
        ]
    ]);

    $curl = curl_init();
    curl_setopt_array($curl, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $body,
        CURLOPT_HTTPHEADER => [
            "merchantId: {{merchantId}}",
            "Content-Type: application/json",
            "Authorization: Bearer {{access_token}}"
        ],
        CURLOPT_TIMEOUT => 30,
        CURLOPT_SSL_VERIFYPEER => true
    ]);

    $response = curl_exec($curl);
    $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
    $error = curl_error($curl);
    curl_close($curl);

    if ($error) {
        echo "cURL Error: " . $error . PHP_EOL;
        return false;
    }

    echo "Status Code: " . $httpCode . PHP_EOL;
    echo "Response: " . $response . PHP_EOL;
}

createENachLink();
?>
```

---

### Schedule a payment reminder

Set `reminder.isScheduled` to `true`, choose the reminder timing with `reminder.type`, and provide one or both supported channels.

```curl
curl --location -g --request POST 'https://uatoneapi.payu.in/payment-links/' \
--header 'merchantId: {{merchantId}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data-raw '{
  "subAmount": 2500,
  "paymentDeadline": "2026-10-15 23:59:59",
  "reminder": {
    "isScheduled": true,
    "type": 0,
    "channels": ["email", "phone"]
  },
  "description": "Payment with reminder for {{orderId}}",
  "source": "API"
}'
```
```python
import http.client
import json

conn = http.client.HTTPSConnection("uatoneapi.payu.in")
payload = json.dumps({
    "subAmount": 2500,
    "paymentDeadline": "2026-10-15 23:59:59",
    "reminder": {
        "isScheduled": True,
        "type": 0,
        "channels": ["email", "phone"]
    },
    "description": "Payment with reminder for {{orderId}}",
    "source": "API"
})
headers = {
    "merchantId": "{{merchantId}}",
    "Content-Type": "application/json",
    "Authorization": "Bearer {{access_token}}"
}
conn.request("POST", "/payment-links/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        try
        {
            string url = "https://uatoneapi.payu.in/payment-links/";
            string jsonBody = @"{
                \"subAmount\": 2500,
                \"paymentDeadline\": \"2026-10-15 23:59:59\",
                \"reminder\": {
                    \"isScheduled\": true,
                    \"type\": 0,
                    \"channels\": [\"email\", \"phone\"]
                },
                \"description\": \"Payment with reminder for {{orderId}}\",
                \"source\": \"API\"
            }";

            var request = new HttpRequestMessage(HttpMethod.Post, url);
            request.Headers.Add("merchantId", "{{merchantId}}");
            request.Headers.Add("Authorization", "Bearer {{access_token}}");
            request.Content = new StringContent(jsonBody, Encoding.UTF8, "application/json");

            HttpResponseMessage response = await client.SendAsync(request);
            string responseContent = await response.Content.ReadAsStringAsync();
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {responseContent}");
        }
        catch (HttpRequestException e)
        {
            Console.WriteLine($"Error: {e.Message}");
        }
    }
}
```
```javascript
async function schedulePaymentReminder() {
    const url = "https://uatoneapi.payu.in/payment-links/";
    const body = JSON.stringify({
        subAmount: 2500,
        paymentDeadline: "2026-10-15 23:59:59",
        reminder: {
            isScheduled: true,
            type: 0,
            channels: ["email", "phone"]
        },
        description: "Payment with reminder for {{orderId}}",
        source: "API"
    });

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "merchantId": "{{merchantId}}",
                "Content-Type": "application/json",
                "Authorization": "Bearer {{access_token}}"
            },
            body: body
        });
        const responseText = await response.text();
        console.log(`Status: ${response.status}`);
        console.log(`Response: ${responseText}`);
    } catch (error) {
        console.error("Error:", error);
    }
}

schedulePaymentReminder();
```
```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class SchedulePaymentReminder {
    public static void main(String[] args) {
        try {
            String url = "https://uatoneapi.payu.in/payment-links/";
            String jsonBody = "{\"subAmount\": 2500, \"paymentDeadline\": \"2026-10-15 23:59:59\", \"reminder\": {\"isScheduled\": true, \"type\": 0, \"channels\": [\"email\", \"phone\"]}, \"description\": \"Payment with reminder for {{orderId}}\", \"source\": \"API\"}";

            URL urlObj = new URL(url);
            HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("merchantId", "{{merchantId}}");
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Authorization", "Bearer {{access_token}}");
            connection.setDoOutput(true);

            try (OutputStream os = connection.getOutputStream()) {
                byte[] input = jsonBody.getBytes(StandardCharsets.UTF_8);
                os.write(input, 0, input.length);
            }

            int responseCode = connection.getResponseCode();
            System.out.println("Status Code: " + responseCode);

            try (BufferedReader br = new BufferedReader(new InputStreamReader(
                    responseCode >= 200 && responseCode < 300
                        ? connection.getInputStream()
                        : connection.getErrorStream(), StandardCharsets.UTF_8))) {
                StringBuilder response = new StringBuilder();
                String responseLine;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }
                System.out.println("Response: " + response.toString());
            }
            connection.disconnect();
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
```php
<?php
function schedulePaymentReminder() {
    $url = "https://uatoneapi.payu.in/payment-links/";
    $body = json_encode([
        "subAmount" => 2500,
        "paymentDeadline" => "2026-10-15 23:59:59",
        "reminder" => [
            "isScheduled" => true,
            "type" => 0,
            "channels" => ["email", "phone"]
        ],
        "description" => "Payment with reminder for {{orderId}}",
        "source" => "API"
    ]);

    $curl = curl_init();
    curl_setopt_array($curl, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $body,
        CURLOPT_HTTPHEADER => [
            "merchantId: {{merchantId}}",
            "Content-Type: application/json",
            "Authorization: Bearer {{access_token}}"
        ],
        CURLOPT_TIMEOUT => 30,
        CURLOPT_SSL_VERIFYPEER => true
    ]);

    $response = curl_exec($curl);
    $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
    $error = curl_error($curl);
    curl_close($curl);

    if ($error) {
        echo "cURL Error: " . $error . PHP_EOL;
        return false;
    }

    echo "Status Code: " . $httpCode . PHP_EOL;
    echo "Response: " . $response . PHP_EOL;
}

schedulePaymentReminder();
?>
```

---

### Send a payment link to multiple WhatsApp recipients

Set `viaWhatsapp` to `true` and provide up to four recipient objects in `whatsappRecipients`. Use `whatsappTemplateName` to select the WhatsApp notification template.

```curl
curl --location -g --request POST 'https://uatoneapi.payu.in/payment-links/' \
--header 'merchantId: {{merchantId}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data-raw '{
  "subAmount": 1500,
  "viaWhatsapp": true,
  "whatsappRecipients": [
    {"phone": "9876543210"},
    {"phone": "9123456789"}
  ],
  "whatsappTemplateName": "{{whatsappTemplateName}}",
  "description": "WhatsApp payment link for {{orderId}}",
  "source": "API"
}'
```
```python
import http.client
import json

conn = http.client.HTTPSConnection("uatoneapi.payu.in")
payload = json.dumps({
    "subAmount": 1500,
    "viaWhatsapp": True,
    "whatsappRecipients": [
        {"phone": "9876543210"},
        {"phone": "9123456789"}
    ],
    "whatsappTemplateName": "{{whatsappTemplateName}}",
    "description": "WhatsApp payment link for {{orderId}}",
    "source": "API"
})
headers = {
    "merchantId": "{{merchantId}}",
    "Content-Type": "application/json",
    "Authorization": "Bearer {{access_token}}"
}
conn.request("POST", "/payment-links/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        try
        {
            string url = "https://uatoneapi.payu.in/payment-links/";
            string jsonBody = @"{
                \"subAmount\": 1500,
                \"viaWhatsapp\": true,
                \"whatsappRecipients\": [
                    {\"phone\": \"9876543210\"},
                    {\"phone\": \"9123456789\"}
                ],
                \"whatsappTemplateName\": \"{{whatsappTemplateName}}\",
                \"description\": \"WhatsApp payment link for {{orderId}}\",
                \"source\": \"API\"
            }";

            var request = new HttpRequestMessage(HttpMethod.Post, url);
            request.Headers.Add("merchantId", "{{merchantId}}");
            request.Headers.Add("Authorization", "Bearer {{access_token}}");
            request.Content = new StringContent(jsonBody, Encoding.UTF8, "application/json");

            HttpResponseMessage response = await client.SendAsync(request);
            string responseContent = await response.Content.ReadAsStringAsync();
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {responseContent}");
        }
        catch (HttpRequestException e)
        {
            Console.WriteLine($"Error: {e.Message}");
        }
    }
}
```
```javascript
async function sendWhatsAppPaymentLink() {
    const url = "https://uatoneapi.payu.in/payment-links/";
    const body = JSON.stringify({
        subAmount: 1500,
        viaWhatsapp: true,
        whatsappRecipients: [
            { phone: "9876543210" },
            { phone: "9123456789" }
        ],
        whatsappTemplateName: "{{whatsappTemplateName}}",
        description: "WhatsApp payment link for {{orderId}}",
        source: "API"
    });

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "merchantId": "{{merchantId}}",
                "Content-Type": "application/json",
                "Authorization": "Bearer {{access_token}}"
            },
            body: body
        });
        const responseText = await response.text();
        console.log(`Status: ${response.status}`);
        console.log(`Response: ${responseText}`);
    } catch (error) {
        console.error("Error:", error);
    }
}

sendWhatsAppPaymentLink();
```
```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class SendWhatsAppPaymentLink {
    public static void main(String[] args) {
        try {
            String url = "https://uatoneapi.payu.in/payment-links/";
            String jsonBody = "{\"subAmount\": 1500, \"viaWhatsapp\": true, \"whatsappRecipients\": [{\"phone\": \"9876543210\"}, {\"phone\": \"9123456789\"}], \"whatsappTemplateName\": \"{{whatsappTemplateName}}\", \"description\": \"WhatsApp payment link for {{orderId}}\", \"source\": \"API\"}";

            URL urlObj = new URL(url);
            HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("merchantId", "{{merchantId}}");
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Authorization", "Bearer {{access_token}}");
            connection.setDoOutput(true);

            try (OutputStream os = connection.getOutputStream()) {
                byte[] input = jsonBody.getBytes(StandardCharsets.UTF_8);
                os.write(input, 0, input.length);
            }

            int responseCode = connection.getResponseCode();
            System.out.println("Status Code: " + responseCode);

            try (BufferedReader br = new BufferedReader(new InputStreamReader(
                    responseCode >= 200 && responseCode < 300
                        ? connection.getInputStream()
                        : connection.getErrorStream(), StandardCharsets.UTF_8))) {
                StringBuilder response = new StringBuilder();
                String responseLine;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }
                System.out.println("Response: " + response.toString());
            }
            connection.disconnect();
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
```php
<?php
function sendWhatsAppPaymentLink() {
    $url = "https://uatoneapi.payu.in/payment-links/";
    $body = json_encode([
        "subAmount" => 1500,
        "viaWhatsapp" => true,
        "whatsappRecipients" => [
            ["phone" => "9876543210"],
            ["phone" => "9123456789"]
        ],
        "whatsappTemplateName" => "{{whatsappTemplateName}}",
        "description" => "WhatsApp payment link for {{orderId}}",
        "source" => "API"
    ]);

    $curl = curl_init();
    curl_setopt_array($curl, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $body,
        CURLOPT_HTTPHEADER => [
            "merchantId: {{merchantId}}",
            "Content-Type: application/json",
            "Authorization: Bearer {{access_token}}"
        ],
        CURLOPT_TIMEOUT => 30,
        CURLOPT_SSL_VERIFYPEER => true
    ]);

    $response = curl_exec($curl);
    $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
    $error = curl_error($curl);
    curl_close($curl);

    if ($error) {
        echo "cURL Error: " . $error . PHP_EOL;
        return false;
    }

    echo "Status Code: " . $httpCode . PHP_EOL;
    echo "Response: " . $response . PHP_EOL;
}

sendWhatsAppPaymentLink();
?>
```

---

### Attach an offer or coupon

Pass the offer or coupon identifier in `offerKey`.

```curl
curl --location -g --request POST 'https://uatoneapi.payu.in/payment-links/' \
--header 'merchantId: {{merchantId}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data-raw '{
  "subAmount": 2000,
  "offerKey": "{{offerKey}}",
  "description": "Payment link with offer for {{orderId}}",
  "source": "API"
}'
```
```python
import http.client
import json

conn = http.client.HTTPSConnection("uatoneapi.payu.in")
payload = json.dumps({
    "subAmount": 2000,
    "offerKey": "{{offerKey}}",
    "description": "Payment link with offer for {{orderId}}",
    "source": "API"
})
headers = {
    "merchantId": "{{merchantId}}",
    "Content-Type": "application/json",
    "Authorization": "Bearer {{access_token}}"
}
conn.request("POST", "/payment-links/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        try
        {
            string url = "https://uatoneapi.payu.in/payment-links/";
            string jsonBody = "{\"subAmount\": 2000, \"offerKey\": \"{{offerKey}}\", \"description\": \"Payment link with offer for {{orderId}}\", \"source\": \"API\"}";

            var request = new HttpRequestMessage(HttpMethod.Post, url);
            request.Headers.Add("merchantId", "{{merchantId}}");
            request.Headers.Add("Authorization", "Bearer {{access_token}}");
            request.Content = new StringContent(jsonBody, Encoding.UTF8, "application/json");

            HttpResponseMessage response = await client.SendAsync(request);
            string responseContent = await response.Content.ReadAsStringAsync();
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {responseContent}");
        }
        catch (HttpRequestException e)
        {
            Console.WriteLine($"Error: {e.Message}");
        }
    }
}
```
```javascript
async function attachOfferToLink() {
    const url = "https://uatoneapi.payu.in/payment-links/";
    const body = JSON.stringify({
        subAmount: 2000,
        offerKey: "{{offerKey}}",
        description: "Payment link with offer for {{orderId}}",
        source: "API"
    });

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "merchantId": "{{merchantId}}",
                "Content-Type": "application/json",
                "Authorization": "Bearer {{access_token}}"
            },
            body: body
        });
        const responseText = await response.text();
        console.log(`Status: ${response.status}`);
        console.log(`Response: ${responseText}`);
    } catch (error) {
        console.error("Error:", error);
    }
}

attachOfferToLink();
```
```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class AttachOfferToLink {
    public static void main(String[] args) {
        try {
            String url = "https://uatoneapi.payu.in/payment-links/";
            String jsonBody = "{\"subAmount\": 2000, \"offerKey\": \"{{offerKey}}\", \"description\": \"Payment link with offer for {{orderId}}\", \"source\": \"API\"}";

            URL urlObj = new URL(url);
            HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("merchantId", "{{merchantId}}");
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Authorization", "Bearer {{access_token}}");
            connection.setDoOutput(true);

            try (OutputStream os = connection.getOutputStream()) {
                byte[] input = jsonBody.getBytes(StandardCharsets.UTF_8);
                os.write(input, 0, input.length);
            }

            int responseCode = connection.getResponseCode();
            System.out.println("Status Code: " + responseCode);

            try (BufferedReader br = new BufferedReader(new InputStreamReader(
                    responseCode >= 200 && responseCode < 300
                        ? connection.getInputStream()
                        : connection.getErrorStream(), StandardCharsets.UTF_8))) {
                StringBuilder response = new StringBuilder();
                String responseLine;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }
                System.out.println("Response: " + response.toString());
            }
            connection.disconnect();
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
```php
<?php
function attachOfferToLink() {
    $url = "https://uatoneapi.payu.in/payment-links/";
    $body = json_encode([
        "subAmount" => 2000,
        "offerKey" => "{{offerKey}}",
        "description" => "Payment link with offer for {{orderId}}",
        "source" => "API"
    ]);

    $curl = curl_init();
    curl_setopt_array($curl, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $body,
        CURLOPT_HTTPHEADER => [
            "merchantId: {{merchantId}}",
            "Content-Type: application/json",
            "Authorization: Bearer {{access_token}}"
        ],
        CURLOPT_TIMEOUT => 30,
        CURLOPT_SSL_VERIFYPEER => true
    ]);

    $response = curl_exec($curl);
    $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
    $error = curl_error($curl);
    curl_close($curl);

    if ($error) {
        echo "cURL Error: " . $error . PHP_EOL;
        return false;
    }

    echo "Status Code: " . $httpCode . PHP_EOL;
    echo "Response: " . $response . PHP_EOL;
}

attachOfferToLink();
?>
```

---

### Specify payout beneficiaries

Use `beneficiarydetail` for NEFT or IMPS payout flows. Keep the four arrays aligned by position and do not send more than four entries.

```curl
curl --location -g --request POST 'https://uatoneapi.payu.in/payment-links/' \
--header 'merchantId: {{merchantId}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data-raw '{
  "subAmount": 4000,
  "beneficiarydetail": {
    "beneficiaryAccountNumber": ["{{beneficiaryAccountNumber1}}"],
    "ifscCode": ["{{beneficiaryIfsc1}}"],
    "beneficiaryName": ["{{beneficiaryName1}}"],
    "beneficiaryAccountType": ["SAVINGS"]
  },
  "description": "Payment link with payout beneficiary",
  "source": "API"
}'
```
```python
import http.client
import json

conn = http.client.HTTPSConnection("uatoneapi.payu.in")
payload = json.dumps({
    "subAmount": 4000,
    "beneficiarydetail": {
        "beneficiaryAccountNumber": ["{{beneficiaryAccountNumber1}}"],
        "ifscCode": ["{{beneficiaryIfsc1}}"],
        "beneficiaryName": ["{{beneficiaryName1}}"],
        "beneficiaryAccountType": ["SAVINGS"]
    },
    "description": "Payment link with payout beneficiary",
    "source": "API"
})
headers = {
    "merchantId": "{{merchantId}}",
    "Content-Type": "application/json",
    "Authorization": "Bearer {{access_token}}"
}
conn.request("POST", "/payment-links/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        try
        {
            string url = "https://uatoneapi.payu.in/payment-links/";
            string jsonBody = @"{
                \"subAmount\": 4000,
                \"beneficiarydetail\": {
                    \"beneficiaryAccountNumber\": [\"{{beneficiaryAccountNumber1}}\"],
                    \"ifscCode\": [\"{{beneficiaryIfsc1}}\"],
                    \"beneficiaryName\": [\"{{beneficiaryName1}}\"],
                    \"beneficiaryAccountType\": [\"SAVINGS\"]
                },
                \"description\": \"Payment link with payout beneficiary\",
                \"source\": \"API\"
            }";

            var request = new HttpRequestMessage(HttpMethod.Post, url);
            request.Headers.Add("merchantId", "{{merchantId}}");
            request.Headers.Add("Authorization", "Bearer {{access_token}}");
            request.Content = new StringContent(jsonBody, Encoding.UTF8, "application/json");

            HttpResponseMessage response = await client.SendAsync(request);
            string responseContent = await response.Content.ReadAsStringAsync();
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {responseContent}");
        }
        catch (HttpRequestException e)
        {
            Console.WriteLine($"Error: {e.Message}");
        }
    }
}
```
```javascript
async function specifyPayoutBeneficiaries() {
    const url = "https://uatoneapi.payu.in/payment-links/";
    const body = JSON.stringify({
        subAmount: 4000,
        beneficiarydetail: {
            beneficiaryAccountNumber: ["{{beneficiaryAccountNumber1}}"],
            ifscCode: ["{{beneficiaryIfsc1}}"],
            beneficiaryName: ["{{beneficiaryName1}}"],
            beneficiaryAccountType: ["SAVINGS"]
        },
        description: "Payment link with payout beneficiary",
        source: "API"
    });

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "merchantId": "{{merchantId}}",
                "Content-Type": "application/json",
                "Authorization": "Bearer {{access_token}}"
            },
            body: body
        });
        const responseText = await response.text();
        console.log(`Status: ${response.status}`);
        console.log(`Response: ${responseText}`);
    } catch (error) {
        console.error("Error:", error);
    }
}

specifyPayoutBeneficiaries();
```
```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class SpecifyPayoutBeneficiaries {
    public static void main(String[] args) {
        try {
            String url = "https://uatoneapi.payu.in/payment-links/";
            String jsonBody = "{\"subAmount\": 4000, \"beneficiarydetail\": {\"beneficiaryAccountNumber\": [\"{{beneficiaryAccountNumber1}}\"], \"ifscCode\": [\"{{beneficiaryIfsc1}}\"], \"beneficiaryName\": [\"{{beneficiaryName1}}\"], \"beneficiaryAccountType\": [\"SAVINGS\"]}, \"description\": \"Payment link with payout beneficiary\", \"source\": \"API\"}";

            URL urlObj = new URL(url);
            HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("merchantId", "{{merchantId}}");
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Authorization", "Bearer {{access_token}}");
            connection.setDoOutput(true);

            try (OutputStream os = connection.getOutputStream()) {
                byte[] input = jsonBody.getBytes(StandardCharsets.UTF_8);
                os.write(input, 0, input.length);
            }

            int responseCode = connection.getResponseCode();
            System.out.println("Status Code: " + responseCode);

            try (BufferedReader br = new BufferedReader(new InputStreamReader(
                    responseCode >= 200 && responseCode < 300
                        ? connection.getInputStream()
                        : connection.getErrorStream(), StandardCharsets.UTF_8))) {
                StringBuilder response = new StringBuilder();
                String responseLine;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }
                System.out.println("Response: " + response.toString());
            }
            connection.disconnect();
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
```php
<?php
function specifyPayoutBeneficiaries() {
    $url = "https://uatoneapi.payu.in/payment-links/";
    $body = json_encode([
        "subAmount" => 4000,
        "beneficiarydetail" => [
            "beneficiaryAccountNumber" => ["{{beneficiaryAccountNumber1}}"],
            "ifscCode" => ["{{beneficiaryIfsc1}}"],
            "beneficiaryName" => ["{{beneficiaryName1}}"],
            "beneficiaryAccountType" => ["SAVINGS"]
        ],
        "description" => "Payment link with payout beneficiary",
        "source" => "API"
    ]);

    $curl = curl_init();
    curl_setopt_array($curl, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $body,
        CURLOPT_HTTPHEADER => [
            "merchantId: {{merchantId}}",
            "Content-Type: application/json",
            "Authorization: Bearer {{access_token}}"
        ],
        CURLOPT_TIMEOUT => 30,
        CURLOPT_SSL_VERIFYPEER => true
    ]);

    $response = curl_exec($curl);
    $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
    $error = curl_error($curl);
    curl_close($curl);

    if ($error) {
        echo "cURL Error: " . $error . PHP_EOL;
        return false;
    }

    echo "Status Code: " . $httpCode . PHP_EOL;
    echo "Response: " . $response . PHP_EOL;
}

specifyPayoutBeneficiaries();
?>
```

---

### Hold a pre-authorisation

Pass the number of days to hold the pre-authorisation in `blockDaysForPreAuthorizeLinks`.

```curl
curl --location -g --request POST 'https://uatoneapi.payu.in/payment-links/' \
--header 'merchantId: {{merchantId}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data-raw '{
  "subAmount": 7500,
  "blockDaysForPreAuthorizeLinks": 7,
  "description": "Pre-authorisation payment link for {{orderId}}",
  "source": "API"
}'
```
```python
import http.client
import json

conn = http.client.HTTPSConnection("uatoneapi.payu.in")
payload = json.dumps({
    "subAmount": 7500,
    "blockDaysForPreAuthorizeLinks": 7,
    "description": "Pre-authorisation payment link for {{orderId}}",
    "source": "API"
})
headers = {
    "merchantId": "{{merchantId}}",
    "Content-Type": "application/json",
    "Authorization": "Bearer {{access_token}}"
}
conn.request("POST", "/payment-links/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        try
        {
            string url = "https://uatoneapi.payu.in/payment-links/";
            string jsonBody = "{\"subAmount\": 7500, \"blockDaysForPreAuthorizeLinks\": 7, \"description\": \"Pre-authorisation payment link for {{orderId}}\", \"source\": \"API\"}";

            var request = new HttpRequestMessage(HttpMethod.Post, url);
            request.Headers.Add("merchantId", "{{merchantId}}");
            request.Headers.Add("Authorization", "Bearer {{access_token}}");
            request.Content = new StringContent(jsonBody, Encoding.UTF8, "application/json");

            HttpResponseMessage response = await client.SendAsync(request);
            string responseContent = await response.Content.ReadAsStringAsync();
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {responseContent}");
        }
        catch (HttpRequestException e)
        {
            Console.WriteLine($"Error: {e.Message}");
        }
    }
}
```
```javascript
async function holdPreAuthorisation() {
    const url = "https://uatoneapi.payu.in/payment-links/";
    const body = JSON.stringify({
        subAmount: 7500,
        blockDaysForPreAuthorizeLinks: 7,
        description: "Pre-authorisation payment link for {{orderId}}",
        source: "API"
    });

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "merchantId": "{{merchantId}}",
                "Content-Type": "application/json",
                "Authorization": "Bearer {{access_token}}"
            },
            body: body
        });
        const responseText = await response.text();
        console.log(`Status: ${response.status}`);
        console.log(`Response: ${responseText}`);
    } catch (error) {
        console.error("Error:", error);
    }
}

holdPreAuthorisation();
```
```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class HoldPreAuthorisation {
    public static void main(String[] args) {
        try {
            String url = "https://uatoneapi.payu.in/payment-links/";
            String jsonBody = "{\"subAmount\": 7500, \"blockDaysForPreAuthorizeLinks\": 7, \"description\": \"Pre-authorisation payment link for {{orderId}}\", \"source\": \"API\"}";

            URL urlObj = new URL(url);
            HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("merchantId", "{{merchantId}}");
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Authorization", "Bearer {{access_token}}");
            connection.setDoOutput(true);

            try (OutputStream os = connection.getOutputStream()) {
                byte[] input = jsonBody.getBytes(StandardCharsets.UTF_8);
                os.write(input, 0, input.length);
            }

            int responseCode = connection.getResponseCode();
            System.out.println("Status Code: " + responseCode);

            try (BufferedReader br = new BufferedReader(new InputStreamReader(
                    responseCode >= 200 && responseCode < 300
                        ? connection.getInputStream()
                        : connection.getErrorStream(), StandardCharsets.UTF_8))) {
                StringBuilder response = new StringBuilder();
                String responseLine;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }
                System.out.println("Response: " + response.toString());
            }
            connection.disconnect();
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
```php
<?php
function holdPreAuthorisation() {
    $url = "https://uatoneapi.payu.in/payment-links/";
    $body = json_encode([
        "subAmount" => 7500,
        "blockDaysForPreAuthorizeLinks" => 7,
        "description" => "Pre-authorisation payment link for {{orderId}}",
        "source" => "API"
    ]);

    $curl = curl_init();
    curl_setopt_array($curl, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $body,
        CURLOPT_HTTPHEADER => [
            "merchantId: {{merchantId}}",
            "Content-Type: application/json",
            "Authorization: Bearer {{access_token}}"
        ],
        CURLOPT_TIMEOUT => 30,
        CURLOPT_SSL_VERIFYPEER => true
    ]);

    $response = curl_exec($curl);
    $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
    $error = curl_error($curl);
    curl_close($curl);

    if ($error) {
        echo "cURL Error: " . $error . PHP_EOL;
        return false;
    }

    echo "Status Code: " . $httpCode . PHP_EOL;
    echo "Response: " . $response . PHP_EOL;
}

holdPreAuthorisation();
?>
```
