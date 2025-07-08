---
title: 1. API Integration to Onboard Merchants
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU Split Settlements allows marketplace platforms to split payment transactions among multiple child merchants (sub-sellers) involved in an order. This integration guide walks you through the complete process of onboarding child merchants and implementing split settlements.

## Prerequisites

Before integrating Split Settlements, ensure you have:

1. **Parent Merchant Account**: A verified PayU merchant account that will act as the platform/aggregator
2. **API Credentials**: Your `key` and `salt` from the PayU dashboard
3. **Marketplace Setup**: Business model allowing multiple sellers on your platform
4. **KYC Documentation**: Required documents for child merchant verification

### Getting Your API Credentials

1. Log into your [PayU Dashboard](https://test.payu.in/merchant/dashboard)
2. Navigate to **Account & Settings** → **API Configuration**
3. Copy your `Key` and `Salt` values
4. Note your Merchant ID for reference

## Step 1: Onboard Child Merchants

Child merchant onboarding is a multi-step process that ensures compliance and security.

### Register Child Merchant

Use the Child Merchant Registration API to create new sub-merchant accounts:

**Endpoint**: `POST /api/v1/createChildMerchant`

**Request Parameters**:

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        merchantName
        `mandatory`
      </td>

      <td>
        `String` Legal name of the child merchant
      </td>
    </tr>

    <tr>
      <td>
        email
        `mandatory`
      </td>

      <td>
        `String`Valid email address for login
      </td>
    </tr>

    <tr>
      <td>
        mobile
        `mandatory`
      </td>

      <td>
        `String`10-digit mobile number
      </td>
    </tr>

    <tr>
      <td>
        businessType
        `mandatory`
      </td>

      <td>
        `String`Type of business (Individual/Partnership/LLP/Pvt Ltd)
      </td>
    </tr>

    <tr>
      <td>
        tradeName
        `mandatory`
      </td>

      <td>
        `String`Business trade name (must match bank account)
      </td>
    </tr>

    <tr>
      <td>
        category
        `mandatory`
      </td>

      <td>
        `String`Business category code
      </td>
    </tr>

    <tr>
      <td>
        subcategory
        `mandatory`
      </td>

      <td>
        `String`Business subcategory code
      </td>
    </tr>
  </tbody>
</Table>

**Sample Request (cURL)**:

```bash
curl -X POST "https://test.payu.in/api/v1/createChildMerchant" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_CLIENT_TOKEN" \
-d '{
  "merchantName": "ABC Electronics Store",
  "email": "merchant@abcelectronics.com",
  "mobile": "9876543210",
  "businessType": "Pvt Ltd",
  "tradeName": "ABC Electronics",
  "category": "1001",
  "subcategory": "1001001"
}'
```

**Sample Response**:

```json
{
  "status": "success",
  "message": "Child merchant created successfully",
  "data": {
    "childMerchantId": "CM_ABC_123456",
    "merchantName": "ABC Electronics Store",
    "email": "merchant@abcelectronics.com",
    "status": "pending_activation",
    "createdAt": "2024-01-15T10:30:00Z"
  }
}
```

### Activate Child Merchant Account

After registration, the child merchant must activate their account:

1. **Email Notification**: Child merchant receives activation email
2. **Dashboard Login**: Visit `https://onboarding.payu.in/app/account/signin`
3. **Account Activation**: Click "Activate Account" in the dashboard
4. **Password Setup**: Create a secure password for the account

#### 1.3 Complete KYC Verification

Child merchants must complete Know Your Customer (KYC) verification:

**Required Documents**:

* Business registration certificate
* PAN card of business/individual
* Bank account verification (cancelled cheque/bank statement)
* Address proof
* ID proof of authorized signatory

**KYC Process**:

1. Login to PayU dashboard
2. Navigate to **Account Settings** → **KYC Documents**
3. Upload required documents
4. Submit for verification
5. Wait for PayU approval (typically 1-3 business days)

**Important**: Trade name must exactly match the bank account holder name.

## Step 2: Implement Split Settlements

Once child merchants are onboarded and verified, implement split settlements in your payment flow.

### Add Payment Splits

Use the Payment Splits API to define how transaction amounts should be distributed:

**Endpoint**: `POST /api/v1/addPaymentSplits`

**Request Parameters**:

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        txnid
        `mandatory`
      </td>

      <td>
        `String` Unique transaction ID
      </td>
    </tr>

    <tr>
      <td>
        amount
        `mandatory`
      </td>

      <td>
        `String`Total transaction amount
      </td>
    </tr>

    <tr>
      <td>
        splits
        `mandatory`
      </td>

      <td>
        `Array` JSON object array of split details
      </td>
    </tr>
  </tbody>
</Table>

#### splits JSON object fields

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        childMerchantId
        `mandatory`
      </td>

      <td>
        `String`Child merchant identifier
      </td>
    </tr>

    <tr>
      <td>
        amountToBeSettled
        `mandatory`
      </td>

      <td>
        `String`Amount for this child merchant
      </td>
    </tr>

    <tr>
      <td>
        aggregatorCommission
        `optional`
      </td>

      <td>
        `String`Platform commission amount
      </td>
    </tr>

    <tr>
      <td>
        suborderId
        `mandatory`
      </td>

      <td>
        `String`Unique sub-order identifier
      </td>
    </tr>
  </tbody>
</Table>

**Sample Request (Python)**:

```curl
curl -X POST "https://test.payu.in/api/v1/addPaymentSplits" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_AUTH_TOKEN" \
-d '{
  "txnid": "TXN_20240115_001",
  "amount": 2000.00,
  "splits": [
    {
      "childMerchantId": "CM_ABC_123456",
      "amountToBeSettled": 800.00,
      "aggregatorCommission": 50.00,
      "suborderId": "SUB_001"
    },
    {
      "childMerchantId": "CM_XYZ_789012",
      "amountToBeSettled": 1200.00,
      "aggregatorCommission": 75.00,
      "suborderId": "SUB_002"
    }
  ]
}'

# Alternative with variables
TXNID="TXN_20240115_001"
AMOUNT=2000.00
AUTH_TOKEN="YOUR_AUTH_TOKEN"

curl -X POST "https://test.payu.in/api/v1/addPaymentSplits" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $AUTH_TOKEN" \
-d "{
  \"txnid\": \"$TXNID\",
  \"amount\": $AMOUNT,
  \"splits\": [
    {
      \"childMerchantId\": \"CM_ABC_123456\",
      \"amountToBeSettled\": 800.00,
      \"aggregatorCommission\": 50.00,
      \"suborderId\": \"SUB_001\"
    },
    {
      \"childMerchantId\": \"CM_XYZ_789012\",
      \"amountToBeSettled\": 1200.00,
      \"aggregatorCommission\": 75.00,
      \"suborderId\": \"SUB_002\"
    }
  ]
}"
```
```python
import requests
import hashlib
import json

def add_payment_splits(txnid, total_amount, splits_data):
    url = "https://test.payu.in/api/v1/addPaymentSplits"
    
    payload = {
        "txnid": txnid,
        "amount": total_amount,
        "splits": splits_data
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_auth_token()}"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Example usage
splits = [
    {
        "childMerchantId": "CM_ABC_123456",
        "amountToBeSettled": 800.00,
        "aggregatorCommission": 50.00,
        "suborderId": "SUB_001"
    },
    {
        "childMerchantId": "CM_XYZ_789012",
        "amountToBeSettled": 1200.00,
        "aggregatorCommission": 75.00,
        "suborderId": "SUB_002"
    }
]

result = add_payment_splits("TXN_20240115_001", 2000.00, splits)
print(json.dumps(result, indent=2))
```
```java
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URI;
import java.time.Duration;
import java.util.List;
import java.util.Map;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.core.type.TypeReference;

public class PayUSplitSettlements {
    
    private static final String API_URL = "https://test.payu.in/api/v1/addPaymentSplits";
    private final HttpClient httpClient;
    private final ObjectMapper objectMapper;
    
    public PayUSplitSettlements() {
        this.httpClient = HttpClient.newBuilder()
            .connectTimeout(Duration.ofSeconds(30))
            .build();
        this.objectMapper = new ObjectMapper();
    }
    
    public static class Split {
        public String childMerchantId;
        public double amountToBeSettled;
        public double aggregatorCommission;
        public String suborderId;
        
        public Split(String childMerchantId, double amountToBeSettled, 
                    double aggregatorCommission, String suborderId) {
            this.childMerchantId = childMerchantId;
            this.amountToBeSettled = amountToBeSettled;
            this.aggregatorCommission = aggregatorCommission;
            this.suborderId = suborderId;
        }
    }
    
    public static class PaymentSplitRequest {
        public String txnid;
        public double amount;
        public List<Split> splits;
        
        public PaymentSplitRequest(String txnid, double amount, List<Split> splits) {
            this.txnid = txnid;
            this.amount = amount;
            this.splits = splits;
        }
    }
    
    public Map<String, Object> addPaymentSplits(String txnid, double totalAmount, 
                                               List<Split> splitsData, String authToken) {
        try {
            // Create request payload
            PaymentSplitRequest payload = new PaymentSplitRequest(txnid, totalAmount, splitsData);
            String jsonPayload = objectMapper.writeValueAsString(payload);
            
            // Build HTTP request
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(API_URL))
                .header("Content-Type", "application/json")
                .header("Authorization", "Bearer " + authToken)
                .POST(HttpRequest.BodyPublishers.ofString(jsonPayload))
                .build();
            
            // Send request and get response
            HttpResponse<String> response = httpClient.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            // Parse response
            Map<String, Object> result = objectMapper.readValue(
                response.body(), new TypeReference<Map<String, Object>>() {});
            
            return result;
            
        } catch (Exception e) {
            e.printStackTrace();
            return Map.of("error", "Request failed: " + e.getMessage());
        }
    }
    
    // Example usage
    public static void main(String[] args) {
        PayUSplitSettlements api = new PayUSplitSettlements();
        
        // Create splits data
        List<Split> splits = List.of(
            new Split("CM_ABC_123456", 800.00, 50.00, "SUB_001"),
            new Split("CM_XYZ_789012", 1200.00, 75.00, "SUB_002")
        );
        
        // Make API call
        Map<String, Object> result = api.addPaymentSplits(
            "TXN_20240115_001", 
            2000.00, 
            splits, 
            getAuthToken()
        );
        
        // Print result
        System.out.println("API Response: " + result);
    }
    
    private static String getAuthToken() {
        // Implement your token retrieval logic here
        return "YOUR_AUTH_TOKEN";
    }
}
```
```php
class PayUSplitSettlements {
    /** @var string */
    private string $baseUrl;
    
    /** @var int */
    private int $timeout;
    
    /** @var bool */
    private bool $verifySSL;
    
    /**
     * Constructor
     * 
     * @param string $baseUrl API base URL
     * @param int $timeout Request timeout in seconds
     * @param bool $verifySSL Whether to verify SSL certificates
     */
    public function __construct(
        string $baseUrl = 'https://test.payu.in/api/v1',
        int $timeout = 30,
        bool $verifySSL = true
    ) {
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->verifySSL = $verifySSL;
    }
    
    /**
     * Add Payment Splits API Request
     * 
     * @param string $txnid Transaction ID
     * @param float $totalAmount Total transaction amount
     * @param array $splitsData Array of split details
     * @param string $authToken Authentication token
     * @return array Response from API
     * @throws Exception If request fails
     */
    public function addPaymentSplits(
        string $txnid,
        float $totalAmount,
        array $splitsData,
        string $authToken
    ): array {
        // Validate input data
        $this->validateInput($txnid, $totalAmount, $splitsData);
        
        // Create request payload
        $payload = [
            'txnid' => $txnid,
            'amount' => $totalAmount,
            'splits' => $splitsData
        ];
        
        // Convert payload to JSON
        $jsonPayload = json_encode($payload);
        if (json_last_error() !== JSON_ERROR_NONE) {
            throw new Exception('JSON encoding error: ' . json_last_error_msg());
        }
        
        // Set up cURL request
        $ch = curl_init($this->baseUrl . '/addPaymentSplits');
        
        // Set cURL options
        curl_setopt_array($ch, [
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $jsonPayload,
            CURLOPT_TIMEOUT => $this->timeout,
            CURLOPT_HTTPHEADER => [
                'Content-Type: application/json',
                'Authorization: Bearer ' . $authToken,
                'Content-Length: ' . strlen($jsonPayload)
            ],
            CURLOPT_SSL_VERIFYPEER => $this->verifySSL
        ]);
        
        // Execute request
        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        
        // Check for cURL errors
        if ($response === false) {
            $error = curl_error($ch);
            curl_close($ch);
            throw new Exception('cURL error: ' . $error);
        }
        
        curl_close($ch);
        
        // Parse JSON response
        $result = json_decode($response, true);
        
        // Check for JSON parsing errors
        if (json_last_error() !== JSON_ERROR_NONE) {
            throw new Exception('JSON decoding error: ' . json_last_error_msg());
        }
        
        // Check for HTTP errors
        if ($httpCode >= 400) {
            $errorMessage = $result['message'] ?? 'Unknown error';
            throw new Exception("HTTP error {$httpCode}: {$errorMessage}");
        }
        
        return $result;
    }
    
    /**
     * Validate input data
     * 
     * @param string $txnid Transaction ID
     * @param float $totalAmount Total amount
     * @param array $splitsData Splits data
     * @throws Exception If validation fails
     */
    private function validateInput(string $txnid, float $totalAmount, array $splitsData): void {
        // Validate transaction ID
        if (empty($txnid)) {
            throw new Exception('Transaction ID cannot be empty');
        }
        
        // Validate amount
        if ($totalAmount <= 0) {
            throw new Exception('Amount must be greater than zero');
        }
        
        // Validate splits data
        if (empty($splitsData)) {
            throw new Exception('Splits data cannot be empty');
        }
        
        // Check if splits data is an array
        if (!is_array($splitsData)) {
            throw new Exception('Splits data must be an array');
        }
        
        // Validate each split
        foreach ($splitsData as $index => $split) {
            if (empty($split['childMerchantId'])) {
                throw new Exception("Split #{$index}: childMerchantId is required");
            }
            
            if (!isset($split['amountToBeSettled']) || !is_numeric($split['amountToBeSettled'])) {
                throw new Exception("Split #{$index}: amountToBeSettled must be a number");
            }
            
            if (empty($split['suborderId'])) {
                throw new Exception("Split #{$index}: suborderId is required");
            }
        }
    }
    
    /**
     * Get total amount from splits
     * 
     * @param array $splitsData Splits data
     * @return float Total amount
     */
    public function getTotalFromSplits(array $splitsData): float {
        $total = 0.0;
        
        foreach ($splitsData as $split) {
            $total += (float)$split['amountToBeSettled'];
            
            if (isset($split['aggregatorCommission']) && is_numeric($split['aggregatorCommission'])) {
                $total += (float)$split['aggregatorCommission'];
            }
        }
        
        return $total;
    }
}

// --------------------------------------------------------------------------
// Procedural implementation (alternative)
// --------------------------------------------------------------------------

/**
 * Add Payment Splits API Request (procedural version)
 * 
 * @param string $txnid Transaction ID
 * @param float $totalAmount Total transaction amount
 * @param array $splitsData Array of split details
 * @param string $authToken Authentication token
 * @param string $apiUrl API URL
 * @param int $timeout Request timeout in seconds
 * @param bool $verifySSL Whether to verify SSL certificates
 * @return array Response from API
 */
function payu_add_payment_splits(
    string $txnid,
    float $totalAmount,
    array $splitsData,
    string $authToken,
    string $apiUrl = 'https://test.payu.in/api/v1/addPaymentSplits',
    int $timeout = 30,
    bool $verifySSL = true
): array {
    // Create request payload
    $payload = [
        'txnid' => $txnid,
        'amount' => $totalAmount,
        'splits' => $splitsData
    ];
    
    // Convert payload to JSON
    $jsonPayload = json_encode($payload);
    if ($jsonPayload === false) {
        return [
            'status' => 'error',
            'message' => 'JSON encoding error: ' . json_last_error_msg()
        ];
    }
    
    // Set up cURL request
    $ch = curl_init($apiUrl);
    
    // Set cURL options
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $jsonPayload,
        CURLOPT_TIMEOUT => $timeout,
        CURLOPT_HTTPHEADER => [
            'Content-Type: application/json',
            'Authorization: Bearer ' . $authToken,
            'Content-Length: ' . strlen($jsonPayload)
        ],
        CURLOPT_SSL_VERIFYPEER => $verifySSL
    ]);
    
    // Execute request
    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    
    // Check for cURL errors
    if ($response === false) {
        $error = curl_error($ch);
        curl_close($ch);
        return [
            'status' => 'error',
            'message' => 'cURL error: ' . $error,
            'code' => 'CURL_ERROR'
        ];
    }
    
    curl_close($ch);
    
    // Parse JSON response
    $result = json_decode($response, true);
    
    // Check for JSON parsing errors
    if ($result === null && json_last_error() !== JSON_ERROR_NONE) {
        return [
            'status' => 'error',
            'message' => 'JSON decoding error: ' . json_last_error_msg(),
            'response' => $response
        ];
    }
    
    // Check for HTTP errors
    if ($httpCode >= 400) {
        return [
            'status' => 'error',
            'message' => $result['message'] ?? 'HTTP error ' . $httpCode,
            'code' => 'HTTP_ERROR',
            'http_code' => $httpCode,
            'response' => $result
        ];
    }
    
    return $result;
}

// --------------------------------------------------------------------------
// Guzzle implementation (for modern PHP applications)
// --------------------------------------------------------------------------

/*
// Requires Guzzle HTTP client
// Install via Composer: composer require guzzlehttp/guzzle

use GuzzleHttp\Client;
use GuzzleHttp\Exception\GuzzleException;
use GuzzleHttp\RequestOptions;

class PayUSplitSettlementsGuzzle {
    private Client $client;
    
    public function __construct(string $baseUrl = 'https://test.payu.in/api/v1', int $timeout = 30) {
        $this->client = new Client([
            'base_uri' => $baseUrl,
            'timeout' => $timeout,
            'http_errors' => false
        ]);
    }
    
    public function addPaymentSplits(
        string $txnid,
        float $totalAmount,
        array $splitsData,
        string $authToken
    ): array {
        try {
            $payload = [
                'txnid' => $txnid,
                'amount' => $totalAmount,
                'splits' => $splitsData
            ];
            
            $response = $this->client->post('addPaymentSplits', [
                RequestOptions::JSON => $payload,
                RequestOptions::HEADERS => [
                    'Authorization' => 'Bearer ' . $authToken
                ]
            ]);
            
            $statusCode = $response->getStatusCode();
            $body = (string) $response->getBody();
            $result = json_decode($body, true);
            
            if (json_last_error() !== JSON_ERROR_NONE) {
                throw new Exception('JSON decoding error: ' . json_last_error_msg());
            }
            
            if ($statusCode >= 400) {
                $errorMessage = $result['message'] ?? 'Unknown error';
                throw new Exception("HTTP error {$statusCode}: {$errorMessage}");
            }
            
            return $result;
            
        } catch (GuzzleException $e) {
            throw new Exception('HTTP request failed: ' . $e->getMessage(), 0, $e);
        }
    }
}
*/

// --------------------------------------------------------------------------
// Example usage
// --------------------------------------------------------------------------

/**
 * Get authentication token
 * 
 * @return string Authentication token
 */
function get_auth_token(): string {
    // Implement your token retrieval logic here
    // For example, from environment variables, database, or another API call
    return 'YOUR_AUTH_TOKEN';
}

// Example splits data
$splits = [
    [
        'childMerchantId' => 'CM_ABC_123456',
        'amountToBeSettled' => 800.00,
        'aggregatorCommission' => 50.00,
        'suborderId' => 'SUB_001'
    ],
    [
        'childMerchantId' => 'CM_XYZ_789012',
        'amountToBeSettled' => 1200.00,
        'aggregatorCommission' => 75.00,
        'suborderId' => 'SUB_002'
    ]
];

/**
 * Example using object-oriented approach
 */
function example_oop_usage(): void {
    try {
        // Create API client
        $api = new PayUSplitSettlements();
        
        // Call API
        $result = $api->addPaymentSplits(
            'TXN_20240115_001',
            2000.00,
            $GLOBALS['splits'],
            get_auth_token()
        );
        
        // Print result
        echo "API Response (OOP):\n";
        print_r($result);
        
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage() . "\n";
    }
}

/**
 * Example using procedural approach
 */
function example_procedural_usage(): void {
    // Call API
    $result = payu_add_payment_splits(
        'TXN_20240115_001',
        2000.00,
        $GLOBALS['splits'],
        get_auth_token()
    );
    
    // Print result
    echo "API Response (Procedural):\n";
    print_r($result);
    
    // Check for errors
    if (isset($result['status']) && $result['status'] === 'error') {
        echo "Error: " . $result['message'] . "\n";
    }
}

// Only execute examples if running this file directly
if (basename(__FILE__) === basename($_SERVER['PHP_SELF'])) {
    // Example of OOP usage
    echo "Running OOP example...\n";
    example_oop_usage();
    
    echo "\n--------------------------------------------------\n\n";
    
    // Example of procedural usage
    echo "Running procedural example...\n";
    example_procedural_usage();
}

/**
 * Integration example with PayU Hosted Checkout
 */
function integration_with_payu_checkout(): void {
    // Create splits data for a multi-seller order
    $splits = [
        [
            'childMerchantId' => 'CM_ABC_123456',
            'amountToBeSettled' => 800.00,
            'aggregatorCommission' => 50.00,
            'suborderId' => 'SUB_001'
        ],
        [
            'childMerchantId' => 'CM_XYZ_789012',
            'amountToBeSettled' => 1200.00,
            'aggregatorCommission' => 75.00,
            'suborderId' => 'SUB_002'
        ]
    ];
    
    // Transaction details
    $txnid = 'TXN_' . time();
    $amount = 2000.00;
    $productInfo = 'Multi-seller Order';
    $firstname = 'John';
    $email = 'john@example.com';
    $phone = '9876543210';
    $key = 'YOUR_MERCHANT_KEY';
    $salt = 'YOUR_MERCHANT_SALT';
    
    // Set success and failure URLs
    $surl = 'https://yoursite.com/payment/success';
    $furl = 'https://yoursite.com/payment/failure';
    
    // Register splits before payment
    try {
        $api = new PayUSplitSettlements();
        $result = $api->addPaymentSplits($txnid, $amount, $splits, get_auth_token());
        
        if ($result['status'] === 'success') {
            // Generate hash for PayU checkout
            $hashString = $key . '|' . $txnid . '|' . $amount . '|' . $productInfo . '|' . 
                          $firstname . '|' . $email . '|' . '|||||||||||' . $salt;
            $hash = hash('sha512', $hashString);
            
            // Generate HTML form for checkout
            $formHtml = '
            <form action="https://test.payu.in/_payment" method="post" name="payuForm" id="payuForm">
                <input type="hidden" name="key" value="' . htmlspecialchars($key) . '" />
                <input type="hidden" name="txnid" value="' . htmlspecialchars($txnid) . '" />
                <input type="hidden" name="amount" value="' . htmlspecialchars($amount) . '" />
                <input type="hidden" name="productinfo" value="' . htmlspecialchars($productInfo) . '" />
                <input type="hidden" name="firstname" value="' . htmlspecialchars($firstname) . '" />
                <input type="hidden" name="email" value="' . htmlspecialchars($email) . '" />
                <input type="hidden" name="phone" value="' . htmlspecialchars($phone) . '" />
                <input type="hidden" name="surl" value="' . htmlspecialchars($surl) . '" />
                <input type="hidden" name="furl" value="' . htmlspecialchars($furl) . '" />
                <input type="hidden" name="hash" value="' . htmlspecialchars($hash) . '" />
                
                <!-- Split Settlement specific parameters -->
                <input type="hidden" name="split_payments" value="1" />
                <input type="hidden" name="sub_merchant_id" value="CM_ABC_123456,CM_XYZ_789012" />
                
                <input type="submit" value="Pay Now" />
            </form>
            <script>
                // Auto-submit form
                document.getElementById("payuForm").submit();
            </script>
            ';
            
            echo $formHtml;
        } else {
            echo "Failed to register splits: " . ($result['message'] ?? 'Unknown error');
        }
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage();
    }
}

/**
 * Webhook handler for split settlement notifications
 */
function handle_settlement_webhook(): void {
    // Get raw POST data
    $payload = file_get_contents('php://input');
    
    // Verify webhook signature
    $signature = $_SERVER['HTTP_X_PAYU_SIGNATURE'] ?? '';
    
    if (!verify_webhook_signature($payload, $signature)) {
        http_response_code(401);
        echo json_encode(['status' => 'error', 'message' => 'Invalid signature']);
        exit;
    }
    
    // Parse webhook data
    $data = json_decode($payload, true);
    
    if (json_last_error() !== JSON_ERROR_NONE) {
        http_response_code(400);
        echo json_encode(['status' => 'error', 'message' => 'Invalid JSON payload']);
        exit;
    }
    
    // Handle different event types
    $event = $data['event'] ?? '';
    
    switch ($event) {
        case 'settlement.completed':
            handle_settlement_completed($data);
            break;
            
        case 'settlement.failed':
            handle_settlement_failed($data);
            break;
            
        default:
            // Unknown event type
            http_response_code(400);
            echo json_encode(['status' => 'error', 'message' => 'Unknown event type']);
            exit;
    }
    
    // Respond with success
    http_response_code(200);
    echo json_encode(['status' => 'success']);
}

/**
 * Verify webhook signature
 * 
 * @param string $payload Raw payload
 * @param string $signature Provided signature
 * @return bool Whether signature is valid
 */
function verify_webhook_signature(string $payload, string $signature): bool {
    // Implement signature verification logic
    // This is a placeholder - implement according to PayU's signature algorithm
    $secretKey = 'YOUR_WEBHOOK_SECRET';
    $expectedSignature = hash_hmac('sha256', $payload, $secretKey);
    
    return hash_equals($expectedSignature, $signature);
}

/**
 * Handle settlement completed event
 * 
 * @param array $data Event data
 */
function handle_settlement_completed(array $data): void {
    // Extract relevant data
    $txnid = $data['txnid'] ?? '';
    $childMerchantId = $data['childMerchantId'] ?? '';
    $settledAmount = $data['settledAmount'] ?? 0;
    
    // Log settlement
    error_log("Settlement completed for transaction {$txnid}, child merchant {$childMerchantId}, amount {$settledAmount}");
    
    // Update database (example)
    // update_settlement_status($txnid, $childMerchantId, 'completed', $settledAmount);
    
    // Notify child merchant (example)
    // notify_child_merchant($childMerchantId, $settledAmount);
}

/**
 * Handle settlement failed event
 * 
 * @param array $data Event data
 */
function handle_settlement_failed(array $data): void {
    // Extract relevant data
    $txnid = $data['txnid'] ?? '';
    $childMerchantId = $data['childMerchantId'] ?? '';
    $reason = $data['reason'] ?? 'Unknown reason';
    
    // Log failure
    error_log("Settlement failed for transaction {$txnid}, child merchant {$childMerchantId}, reason: {$reason}");
    
    // Update database (example)
    // update_settlement_status($txnid, $childMerchantId, 'failed', 0, $reason);
    
    // Notify admin (example)
    // notify_admin_settlement_failed($txnid, $childMerchantId, $reason);
}

```
```javascript
class PayUSplitSettlements {
    constructor(baseUrl = 'https://test.payu.in/api/v1') {
        this.baseUrl = baseUrl;
        this.apiUrl = `${baseUrl}/addPaymentSplits`;
        
        // For Node.js environment, you might need to import fetch
        // const fetch = require('node-fetch'); // Uncomment for Node.js < 18
    }

    /**
     * Add payment splits for a transaction
     * @param {string} txnid - Transaction ID
     * @param {number} totalAmount - Total transaction amount
     * @param {Array} splitsData - Array of split objects
     * @param {string} authToken - Bearer authentication token
     * @returns {Promise<Object>} API response
     */
    async addPaymentSplits(txnid, totalAmount, splitsData, authToken) {
        try {
            // Create request payload
            const payload = {
                txnid: txnid,
                amount: totalAmount,
                splits: splitsData
            };

            // Configure request options
            const requestOptions = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${authToken}`
                },
                body: JSON.stringify(payload)
            };

            // Make API request
            const response = await fetch(this.apiUrl, requestOptions);
            
            // Check if request was successful
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }

            // Parse and return JSON response
            const result = await response.json();
            return result;

        } catch (error) {
            console.error('Error in addPaymentSplits:', error);
            return {
                status: 'error',
                message: `Request failed: ${error.message}`,
                error: error
            };
        }
    }

    /**
     * Validate splits data before sending
     * @param {Array} splitsData - Array of split objects
     * @param {number} totalAmount - Total transaction amount
     * @returns {Object} Validation result
     */
    validateSplits(splitsData, totalAmount) {
        if (!Array.isArray(splitsData) || splitsData.length === 0) {
            return { valid: false, message: 'Splits data must be a non-empty array' };
        }

        let totalSplitAmount = 0;
        for (const split of splitsData) {
            if (!split.childMerchantId || !split.amountToBeSettled || !split.suborderId) {
                return { 
                    valid: false, 
                    message: 'Each split must have childMerchantId, amountToBeSettled, and suborderId' 
                };
            }
            totalSplitAmount += parseFloat(split.amountToBeSettled) + 
                               parseFloat(split.aggregatorCommission || 0);
        }

        if (Math.abs(totalSplitAmount - totalAmount) > 0.01) {
            return { 
                valid: false, 
                message: `Total split amount (${totalSplitAmount}) does not match transaction amount (${totalAmount})` 
            };
        }

        return { valid: true, message: 'Validation passed' };
    }
}

// Example usage function
async function exampleUsage() {
    const api = new PayUSplitSettlements();

    // Create splits data
    const splits = [
        {
            childMerchantId: "CM_ABC_123456",
            amountToBeSettled: 800.00,
            aggregatorCommission: 50.00,
            suborderId: "SUB_001"
        },
        {
            childMerchantId: "CM_XYZ_789012",
            amountToBeSettled: 1200.00,
            aggregatorCommission: 75.00,
            suborderId: "SUB_002"
        }
    ];

    const txnid = "TXN_20240115_001";
    const totalAmount = 2000.00;

    // Validate splits before sending
    const validation = api.validateSplits(splits, totalAmount);
    if (!validation.valid) {
        console.error('Validation failed:', validation.message);
        return;
    }

    try {
        // Make API call
        const result = await api.addPaymentSplits(
            txnid,
            totalAmount,
            splits,
            getAuthToken()
        );

        // Display result
        console.log('API Response:', JSON.stringify(result, null, 2));
        
        // Handle different response types
        if (result.status === 'success') {
            console.log('✅ Payment splits added successfully!');
            console.log(`Transaction ID: ${result.data?.txnid}`);
            console.log(`Total Splits: ${result.data?.splitsCount}`);
        } else {
            console.log('❌ Failed to add payment splits');
            console.log(`Error: ${result.message}`);
        }

    } catch (error) {
        console.error('Exception occurred:', error);
    }
}

// Helper function to get authentication token
function getAuthToken() {
    // Implement your token retrieval logic here
    // This could be from localStorage, environment variables, or API call
    return process?.env?.PAYU_AUTH_TOKEN || 'YOUR_AUTH_TOKEN';
}

// Alternative implementation using async/await with better error handling
class PayUSplitSettlementsAdvanced {
    constructor(config = {}) {
        this.baseUrl = config.baseUrl || 'https://test.payu.in/api/v1';
        this.timeout = config.timeout || 30000;
        this.retries = config.retries || 3;
    }

    async addPaymentSplits(txnid, totalAmount, splitsData, authToken) {
        const payload = {
            txnid,
            amount: totalAmount,
            splits: splitsData
        };

        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${authToken}`
            },
            body: JSON.stringify(payload)
        };

        // Add timeout support
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), this.timeout);
        options.signal = controller.signal;

        try {
            const response = await this.makeRequestWithRetry(
                `${this.baseUrl}/addPaymentSplits`, 
                options
            );
            
            clearTimeout(timeoutId);
            return await response.json();

        } catch (error) {
            clearTimeout(timeoutId);
            throw error;
        }
    }

    async makeRequestWithRetry(url, options, currentRetry = 0) {
        try {
            const response = await fetch(url, options);
            
            if (!response.ok) {
                // Retry on server errors (5xx) but not client errors (4xx)
                if (response.status >= 500 && currentRetry < this.retries) {
                    console.warn(`Retry ${currentRetry + 1}/${this.retries} after ${response.status} error`);
                    await this.delay(1000 * Math.pow(2, currentRetry)); // Exponential backoff
                    return this.makeRequestWithRetry(url, options, currentRetry + 1);
                }
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }
            
            return response;
        } catch (error) {
            if (currentRetry < this.retries && error.name !== 'AbortError') {
                console.warn(`Retry ${currentRetry + 1}/${this.retries} after network error`);
                await this.delay(1000 * Math.pow(2, currentRetry));
                return this.makeRequestWithRetry(url, options, currentRetry + 1);
            }
            throw error;
        }
    }

    delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

// Browser-specific implementation (for frontend applications)
class PayUSplitSettlementsBrowser {
    constructor() {
        this.apiUrl = 'https://test.payu.in/api/v1/addPaymentSplits';
    }

    async addPaymentSplits(txnid, totalAmount, splitsData, authToken) {
        // Check if running in browser
        if (typeof window === 'undefined') {
            throw new Error('This method is designed for browser environment');
        }

        const payload = {
            txnid,
            amount: totalAmount,
            splits: splitsData
        };

        try {
            // Using modern fetch API with proper CORS handling
            const response = await fetch(this.apiUrl, {
                method: 'POST',
                mode: 'cors',
                cache: 'no-cache',
                credentials: 'same-origin',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${authToken}`
                },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }

            return await response.json();

        } catch (error) {
            console.error('Browser API request failed:', error);
            
            // Handle common browser errors
            if (error.name === 'TypeError' && error.message.includes('fetch')) {
                throw new Error('Network error: Please check your internet connection');
            } else if (error.message.includes('CORS')) {
                throw new Error('CORS error: API endpoint may not allow browser requests');
            }
            
            throw error;
        }
    }
}

// Node.js specific implementation (for backend applications)
class PayUSplitSettlementsNode {
    constructor() {
        this.apiUrl = 'https://test.payu.in/api/v1/addPaymentSplits';
        
        // For Node.js versions < 18, you might need:
        // this.fetch = require('node-fetch');
    }

    async addPaymentSplits(txnid, totalAmount, splitsData, authToken) {
        // Check if running in Node.js
        if (typeof process === 'undefined') {
            throw new Error('This method is designed for Node.js environment');
        }

        const payload = {
            txnid,
            amount: totalAmount,
            splits: splitsData
        };

        try {
            // Use global fetch (Node.js 18+) or imported fetch
            const response = await fetch(this.apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${authToken}`,
                    'User-Agent': 'PayU-Node-Client/1.0'
                },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                const errorBody = await response.text();
                throw new Error(`HTTP ${response.status}: ${response.statusText}\nResponse: ${errorBody}`);
            }

            return await response.json();

        } catch (error) {
            console.error('Node.js API request failed:', error);
            throw error;
        }
    }
}

// Export for different environments
if (typeof module !== 'undefined' && module.exports) {
    // Node.js environment
    module.exports = {
        PayUSplitSettlements,
        PayUSplitSettlementsAdvanced,
        PayUSplitSettlementsNode,
        exampleUsage
    };
} else if (typeof window !== 'undefined') {
    // Browser environment
    window.PayUSplitSettlements = PayUSplitSettlements;
    window.PayUSplitSettlementsBrowser = PayUSplitSettlementsBrowser;
}

// If running this file directly in Node.js, execute example
if (typeof require !== 'undefined' && require.main === module) {
    exampleUsage().catch(console.error);
}

/* 
// Alternative implementation using Axios (popular HTTP client)
// npm install axios

const axios = require('axios'); // For Node.js
// or import axios from 'axios'; // For ES6 modules

class PayUSplitSettlementsAxios {
    constructor() {
        this.client = axios.create({
            baseURL: 'https://test.payu.in/api/v1',
            timeout: 30000,
            headers: {
                'Content-Type': 'application/json'
            }
        });

        // Add request interceptor for authentication
        this.client.interceptors.request.use(
            config => {
                // Add auth token to all requests
                if (config.authToken) {
                    config.headers.Authorization = `Bearer ${config.authToken}`;
                }
                return config;
            },
            error => Promise.reject(error)
        );

        // Add response interceptor for error handling
        this.client.interceptors.response.use(
            response => response,
            error => {
                console.error('Axios request failed:', error.response?.data || error.message);
                return Promise.reject(error);
            }
        );
    }

    async addPaymentSplits(txnid, totalAmount, splitsData, authToken) {
        try {
            const payload = {
                txnid,
                amount: totalAmount,
                splits: splitsData
            };

            const response = await this.client.post('/addPaymentSplits', payload, {
                authToken: authToken
            });

            return response.data;

        } catch (error) {
            throw new Error(`API request failed: ${error.response?.data?.message || error.message}`);
        }
    }
}
*/
```

**Sample Response**:

```json
{
  "status": "success",
  "message": "Payment splits added successfully",
  "data": {
    "txnid": "TXN_20240115_001",
    "totalAmount": 2000.00,
    "splitsCount": 2,
    "splits": [
      {
        "childMerchantId": "CM_ABC_123456",
        "amountToBeSettled": 800.00,
        "aggregatorCommission": 50.00,
        "suborderId": "SUB_001",
        "status": "pending_settlement"
      },
      {
        "childMerchantId": "CM_XYZ_789012",
        "amountToBeSettled": 1200.00,
        "aggregatorCommission": 75.00,
        "suborderId": "SUB_002",
        "status": "pending_settlement"
      }
    ]
  }
}
```

### Integration with Payment Flow

Integrate split settlements with your existing payment process:

**HTML Form Example**:

```html
<form action="https://test.payu.in/_payment" method="post" name="payuForm">
    <input type="hidden" name="key" value="YOUR_MERCHANT_KEY" />
    <input type="hidden" name="txnid" value="TXN_20240115_001" />
    <input type="hidden" name="amount" value="2000.00" />
    <input type="hidden" name="productinfo" value="Multi-seller Order" />
    <input type="hidden" name="firstname" value="John" />
    <input type="hidden" name="email" value="john@example.com" />
    <input type="hidden" name="phone" value="9876543210" />
    <input type="hidden" name="surl" value="https://yoursite.com/payment/success" />
    <input type="hidden" name="furl" value="https://yoursite.com/payment/failure" />
    <input type="hidden" name="hash" value="CALCULATED_HASH" />
    
    <!-- Split Settlement specific parameters -->
    <input type="hidden" name="split_payments" value="1" />
    <input type="hidden" name="sub_merchant_id" value="CM_ABC_123456,CM_XYZ_789012" />
    
    <input type="submit" value="Pay Now" />
</form>
```

## Step 3: Handle Settlement and Reconciliation

### Settlement Reconciliation API

Use the Settlement Reconciliation API to track and verify settlements:

**Endpoint**: `GET /api/v1/getSettlementDetails`

**Request Parameters**:

| Parameter         | Type   | Required | Description              |
| ----------------- | ------ | -------- | ------------------------ |
| `txnid`           | String | Yes      | Transaction ID to query  |
| `settlementDate`  | Date   | No       | Specific settlement date |
| `childMerchantId` | String | No       | Filter by child merchant |

**Sample Request (Java)**:

```java
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URI;

public class SettlementReconciliation {
    
    public String getSettlementDetails(String txnid) {
        try {
            HttpClient client = HttpClient.newHttpClient();
            
            String url = "https://test.payu.in/api/v1/getSettlementDetails?txnid=" + txnid;
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("Authorization", "Bearer " + getAuthToken())
                .GET()
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            return response.body();
            
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
```

### Webhook Notifications

Set up webhooks to receive real-time settlement notifications:

**Webhook Endpoint Configuration**:

1. Navigate to **Dashboard** → **Settings** → **Webhooks**
2. Add your webhook URL: `https://yoursite.com/webhooks/settlement`
3. Select events: `settlement.completed`, `settlement.failed`

**Sample Webhook Handler (PHP)**:

```php
<?php
function handleSettlementWebhook() {
    $payload = file_get_contents('php://input');
    $data = json_decode($payload, true);
    
    // Verify webhook signature
    $signature = $_SERVER['HTTP_X_PAYU_SIGNATURE'];
    if (!verifyWebhookSignature($payload, $signature)) {
        http_response_code(401);
        exit('Unauthorized');
    }
    
    switch ($data['event']) {
        case 'settlement.completed':
            handleSettlementCompleted($data);
            break;
        case 'settlement.failed':
            handleSettlementFailed($data);
            break;
    }
    
    http_response_code(200);
    echo 'OK';
}

function handleSettlementCompleted($data) {
    $txnid = $data['txnid'];
    $childMerchantId = $data['childMerchantId'];
    $settledAmount = $data['settledAmount'];
    
    // Update your database
    updateSettlementStatus($txnid, $childMerchantId, 'completed', $settledAmount);
    
    // Notify child merchant
    notifyChildMerchant($childMerchantId, $settledAmount);
}
?>
```

## Additional Resources

* [Split Settlements API Reference](https://docs.payu.in/docs/split-settlments)
* [Settlement Reconciliation Guide](https://docs.payu.in/reference/settlement-reconciliation-api)
* [KYC Requirements](https://docs.payu.in/docs/kyc-requirements)
* [Error Codes Reference](https://docs.payu.in/docs/error-codes)