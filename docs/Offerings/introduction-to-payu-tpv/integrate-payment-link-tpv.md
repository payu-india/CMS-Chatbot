---
title: Integrate Payment Link TPV
deprecated: false
hidden: false
metadata:
  robots: index
---
This section describes the steps to integrate Payment Link TPV (Third Party Verification) - from payment link creation to payment processing.

> **Note**: Ensure your merchant account has Payment Link enabled for TPV. Contact your PayU Key Account Manager (KAM) or PayU Support if this configuration is not active.

<Cards columns={4}>
  <Card title="1. Create Payment Link" href="#step-1-create-payment-link">
    Create a payment link with beneficiary account details for TPV verification.
    <br />
  </Card>
  <Card title="2. Intermediate Page" href="#step-2-intermediate-page">
    Backend sends beneficiary details to prepayment page for customer visibility.
    <br />
  </Card>
  <Card title="3. Initiate Payment" href="#step-3-initiate-payment">
    Customer initiates payment; backend fetches beneficiary details from database.
    <br />
  </Card>
  <Card title="4. Process Payment" href="#step-4-process-payment">
    Backend converts data and sends to _payment API with api_version 20.
    <br />
  </Card>
</Cards>

---

## Step 1: Create Payment Link

Create a payment link with beneficiary account details using the Create Payment Link API.

<Accordion title="Environment" icon="fa-globe">

| Environment | URL |
|-------------|-----|
| Test | `https://test.payu.in/paymentlink/create` |
| Production | `https://info.payu.in/paymentlink/create` |

</Accordion>

<Accordion title="Request Parameters" icon="fa-table">

| Parameter | Description | Example |
|-----------|-------------|---------|
| amount<br/>`mandatory` | `Decimal`<br/>The payment amount. | `5000.00` |
| maxPaymentsAllowed<br/>`mandatory` | `Integer`<br/>Must be 1 for TPV flow (single payment only). | `1` |
| invoiceNumber<br/>`mandatory` | `String`<br/>Unique invoice number for the payment link. | `INV123456789012` |
| description<br/>`optional` | `String`<br/>Description of the payment. | `Payment for services` |
| customerName<br/>`optional` | `String`<br/>Customer's name. | `John Doe` |
| customerEmail<br/>`optional` | `String`<br/>Customer's email address. | `john.doe@example.com` |
| customerPhone<br/>`optional` | `String`<br/>Customer's phone number. | `9876543210` |
| beneficiarydetail<br/>`optional` | `Object`<br/>Object containing beneficiary account details for TPV. | See below |
| source<br/>`optional` | `String`<br/>Source of the payment link creation. | `API` |

<Accordion title="beneficiarydetail Object Parameters" icon="fa-code">

| Parameter | Description | Example |
|-----------|-------------|---------|
| beneficiaryAccountNumber<br/>`mandatory` | `List<String>`<br/>Array of beneficiary account numbers. Maximum 4 accounts. | `["917732227242", "72522762"]` |
| ifscCode<br/>`mandatory` | `List<String>`<br/>Array of IFSC codes corresponding to each account number. | `["SBIN0007001", "HDFC0001234"]` |

</Accordion>

</Accordion>

<Accordion title="Sample Request" icon="fa-code">

```bash
curl --location 'https://test.payu.in/paymentlink/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <access_token>' \
--data '{
    "amount": 5000.00,
    "maxPaymentsAllowed": 1,
    "invoiceNumber": "INV123456789012",
    "description": "Payment for services",
    "customerName": "John Doe",
    "customerEmail": "john.doe@example.com",
    "customerPhone": "9876543210",
    "beneficiarydetail": {
        "beneficiaryAccountNumber": ["917732227242", "72522762"],
        "ifscCode": ["SBIN0007001", "HDFC0001234"]
    },
    "source": "API"
}'
```

```python
import requests
import json

url = "https://test.payu.in/paymentlink/create"

payload = {
    "amount": 5000.00,
    "maxPaymentsAllowed": 1,
    "invoiceNumber": "INV123456789012",
    "description": "Payment for services",
    "customerName": "John Doe",
    "customerEmail": "john.doe@example.com",
    "customerPhone": "9876543210",
    "beneficiarydetail": {
        "beneficiaryAccountNumber": ["917732227242", "72522762"],
        "ifscCode": ["SBIN0007001", "HDFC0001234"]
    },
    "source": "API"
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <access_token>"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        using var client = new HttpClient();
        
        var payload = @"{
            ""amount"": 5000.00,
            ""maxPaymentsAllowed"": 1,
            ""invoiceNumber"": ""INV123456789012"",
            ""description"": ""Payment for services"",
            ""customerName"": ""John Doe"",
            ""customerEmail"": ""john.doe@example.com"",
            ""customerPhone"": ""9876543210"",
            ""beneficiarydetail"": {
                ""beneficiaryAccountNumber"": [""917732227242"", ""72522762""],
                ""ifscCode"": [""SBIN0007001"", ""HDFC0001234""]
            },
            ""source"": ""API""
        }";
        
        var content = new StringContent(payload, Encoding.UTF8, "application/json");
        client.DefaultRequestHeaders.Add("Authorization", "Bearer <access_token>");
        
        var response = await client.PostAsync("https://test.payu.in/paymentlink/create", content);
        var result = await response.Content.ReadAsStringAsync();
        Console.WriteLine(result);
    }
}
```

```javascript
const createPaymentLinkTPV = async () => {
    const url = "https://test.payu.in/paymentlink/create";
    
    const payload = {
        amount: 5000.00,
        maxPaymentsAllowed: 1,
        invoiceNumber: "INV123456789012",
        description: "Payment for services",
        customerName: "John Doe",
        customerEmail: "john.doe@example.com",
        customerPhone: "9876543210",
        beneficiarydetail: {
            beneficiaryAccountNumber: ["917732227242", "72522762"],
            ifscCode: ["SBIN0007001", "HDFC0001234"]
        },
        source: "API"
    };
    
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer <access_token>"
        },
        body: JSON.stringify(payload)
    });
    
    const data = await response.json();
    console.log(data);
};

createPaymentLinkTPV();
```

```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class CreatePaymentLinkTPV {
    public static void main(String[] args) throws Exception {
        String url = "https://test.payu.in/paymentlink/create";
        
        String payload = "{"
            + "\"amount\": 5000.00,"
            + "\"maxPaymentsAllowed\": 1,"
            + "\"invoiceNumber\": \"INV123456789012\","
            + "\"description\": \"Payment for services\","
            + "\"customerName\": \"John Doe\","
            + "\"customerEmail\": \"john.doe@example.com\","
            + "\"customerPhone\": \"9876543210\","
            + "\"beneficiarydetail\": {"
            + "\"beneficiaryAccountNumber\": [\"917732227242\", \"72522762\"],"
            + "\"ifscCode\": [\"SBIN0007001\", \"HDFC0001234\"]"
            + "},"
            + "\"source\": \"API\""
            + "}";
        
        HttpURLConnection conn = (HttpURLConnection) new URL(url).openConnection();
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setRequestProperty("Authorization", "Bearer <access_token>");
        conn.setDoOutput(true);
        
        try (OutputStream os = conn.getOutputStream()) {
            os.write(payload.getBytes(StandardCharsets.UTF_8));
        }
        
        try (BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()))) {
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        }
    }
}
```

```php
<?php
$url = "https://test.payu.in/paymentlink/create";

$payload = array(
    "amount" => 5000.00,
    "maxPaymentsAllowed" => 1,
    "invoiceNumber" => "INV123456789012",
    "description" => "Payment for services",
    "customerName" => "John Doe",
    "customerEmail" => "john.doe@example.com",
    "customerPhone" => "9876543210",
    "beneficiarydetail" => array(
        "beneficiaryAccountNumber" => array("917732227242", "72522762"),
        "ifscCode" => array("SBIN0007001", "HDFC0001234")
    ),
    "source" => "API"
);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    "Content-Type: application/json",
    "Authorization: Bearer <access_token>"
));

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```

</Accordion>

<Accordion title="Sample Response" icon="fa-check">

```json
{
    "status": "SUCCESS",
    "data": {
        "invoiceNumber": "INV123456789012",
        "amount": 5000.00,
        "beneficiarydetail": {
            "beneficiaryAccountNumber": ["917732227242", "72522762"],
            "ifscCode": ["SBIN0007001", "HDFC0001234"]
        }
    }
}
```

</Accordion>

---

## Step 2: Intermediate Page

When the customer accesses the payment link, the backend sends beneficiary details to the prepayment page.

<Accordion title="Endpoint" icon="fa-globe">

**Endpoint**: `GET /pay/{id}/intermediate`

The backend retrieves the payment link details including beneficiary information and sends it to the prepayment/checkout page.

</Accordion>

<Accordion title="Data Format" icon="fa-code">

The beneficiary details are sent in **list format** (same as the create payment link format):

```json
{
    "beneficiarydetail": {
        "beneficiaryAccountNumber": ["917732227242", "72522762", "283228235"],
        "ifscCode": ["SBIN0007001", "HDFC0001234", "ICIC0002522"]
    }
}
```

> **Note**: The frontend displays these beneficiary accounts on the checkout page for customer visibility.

</Accordion>

<Accordion title="Sample Response" icon="fa-check">

```json
{
    "status": "SUCCESS",
    "data": {
        "invoiceNumber": "INV123456789012",
        "amount": 5000.00,
        "beneficiarydetail": {
            "beneficiaryAccountNumber": ["917732227242", "72522762"],
            "ifscCode": ["SBIN0007001", "HDFC0001234"]
        }
    }
}
```

</Accordion>

---

## Step 3: Initiate Payment

When the customer initiates the payment, the backend fetches beneficiary details from the database.

<Accordion title="Endpoint" icon="fa-globe">

**Endpoint**: `POST /payment` (form-urlencoded)

The customer submits their payment details through the checkout page.

</Accordion>

<Accordion title="Request Parameters" icon="fa-table">

| Parameter | Description | Example |
|-----------|-------------|---------|
| email<br/>`mandatory` | `String`<br/>Customer's email address. | `john.doe@example.com` |
| phone<br/>`mandatory` | `String`<br/>Customer's phone number. | `9876543210` |
| invoiceNumber<br/>`mandatory` | `String`<br/>Invoice number from the payment link. | `INV123456789012` |
| amount<br/>`mandatory` | `Decimal`<br/>Payment amount. | `5000.00` |
| firstName<br/>`optional` | `String`<br/>Customer's first name. | `John` |
| lastName<br/>`optional` | `String`<br/>Customer's last name. | `Doe` |

</Accordion>

<Accordion title="Process Flow" icon="fa-code">

1. Customer submits payment details on checkout page
2. Backend receives the payment initiation request
3. Backend fetches beneficiary details from the database using the invoice number
4. Beneficiary details are prepared for the `_payment` API call

</Accordion>

---

## Step 4: Process Payment

The backend converts beneficiary details to pipe-separated format and sends to the `_payment` API.

<Accordion title="Data Conversion" icon="fa-exchange">

**Conversion Logic:**

| Stage | Format |
|-------|--------|
| Input | Lists from database (same format as create payment link) |
| Processing | Join each list with pipe separator (`\|`) |
| Output | Pipe-separated strings in JSON object |

**Before Conversion (List Format):**

```json
{
    "beneficiarydetail": {
        "beneficiaryAccountNumber": ["917732227242", "72522762", "283228235"],
        "ifscCode": ["SBIN0007001", "HDFC0001234", "ICIC0002522"]
    }
}
```

**After Conversion (Pipe-Separated Format):**

```json
{
    "beneficiarydetail": {
        "beneficiaryAccountNumber": "917732227242|72522762|283228235",
        "ifscCode": "SBIN0007001|HDFC0001234|ICIC0002522"
    },
    "api_version": 20
}
```

</Accordion>

<Accordion title="Hash Generation" icon="fa-lock">

The hash is generated using the following format:

```
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|beneficiarydetail|si_details|user_token|offer_key|offer_auto_apply|cart_details|SALT
```

Where `beneficiarydetail` is the JSON string representation:

```json
{"beneficiaryAccountNumber":"acc1|acc2","ifscCode":"IFSC1|IFSC2"}
```

</Accordion>

<Accordion title="Sample Request to _payment API" icon="fa-code">

```json
{
    "key": "merchant_key",
    "txnid": "TXN123456",
    "amount": "5000.00",
    "productinfo": "Payment for services",
    "firstname": "John",
    "email": "john.doe@example.com",
    "beneficiarydetail": {
        "beneficiaryAccountNumber": "917732227242|72522762",
        "ifscCode": "SBIN0007001|HDFC0001234"
    },
    "api_version": 20,
    "hash": "<generated_hash>"
}
```

> **Important**: `api_version: 20` is required when beneficiary details are present.

</Accordion>

---

## Validation Rules

| Validation | Rule | Error Code |
|------------|------|------------|
| Merchant TPV Enabled | enableTpvFlow = "1" | 427 |
| Max Payments | maxPaymentsAllowed = 1 | 400 |
| Max Beneficiaries | ≤ 4 beneficiaries | 400 |
| Equal Count | Account numbers = IFSC codes count | 400 |
| Account Format | Alphanumeric, max 50 chars | 400 |
| IFSC Format | Exactly 11 chars: `[A-Z]{4}0[A-Z0-9]{6}` | 400 |

