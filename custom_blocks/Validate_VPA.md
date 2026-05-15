---
name: Validate_VPA
---
```curl
curl --location '`https://test.payu.in/merchant/postservice.php?form=2`' \
  --header 'accept: application/json' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'form=2' \
  --data-urlencode 'key=BmTY3G' \
  --data-urlencode 'command=validateVPA' \
  --data-urlencode 'var1=9999999999@upi' \
  --data-urlencode 'hash=d415188799f49f554a24064752bd6ce4d8a18c075b7b88b534e3150f253c09ae28a48554d2d1ba4be66b8441b2cbc364491d26bcead605c5fcecf4eaf622e224'
```
```python
import requests

url = "https://secure.payu.in/merchant/postservice"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "form": "2",
    "key": "BmTY3G",
    "command": "validateVPA",
    "var1": "9999999999@upi",
    "hash": "d415188799f49f554a24064752bd6ce4d8a18c075b7b88b534e3150f253c09ae28a48554d2d1ba4be66b8441b2cbc364491d26bcead605c5fcecf4eaf622e224"
}

response = requests.post(url, headers=headers, data=data)

print("Status Code:", response.status_code)
print("Response:", response.json())
```
```java
import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class ValidateVPA {
    public static void main(String[] args) throws IOException, InterruptedException {
        String url = "https://secure.payu.in/merchant/postservice";
        
        Map<String, String> params = new HashMap<>();
        params.put("form", "2");
        params.put("key", "BmTY3G");
        params.put("command", "validateVPA");
        params.put("var1", "9999999999@upi");
        params.put("hash", "d415188799f49f554a24064752bd6ce4d8a18c075b7b88b534e3150f253c09ae28a48554d2d1ba4be66b8441b2cbc364491d26bcead605c5fcecf4eaf622e224");
        
        String formData = params.entrySet().stream()
            .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "=" 
                    + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
            .collect(Collectors.joining("&"));
        
        HttpClient client = HttpClient.newHttpClient();
        
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("accept", "application/json")
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formData))
            .build();
        
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response: " + response.body());
    }
}
```
```javascript
const axios = require('axios');
const qs = require('qs');

const url = 'https://secure.payu.in/merchant/postservice';

const data = {
    form: '2',
    key: 'BmTY3G',
    command: 'validateVPA',
    var1: '9999999999@upi',
    hash: 'd415188799f49f554a24064752bd6ce4d8a18c075b7b88b534e3150f253c09ae28a48554d2d1ba4be66b8441b2cbc364491d26bcead605c5fcecf4eaf622e224'
};

const config = {
    headers: {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
};

axios.post(url, qs.stringify(data), config)
    .then(response => {
        console.log('Status Code:', response.status);
        console.log('Response:', response.data);
    })
    .catch(error => {
        console.error('Error:', error.response ? error.response.data : error.message);
    });
```
```php
<?php

$url = "https://secure.payu.in/merchant/postservice";

$data = array(
    'form' => '2',
    'key' => 'BmTY3G',
    'command' => 'validateVPA',
    'var1' => '9999999999@upi',
    'hash' => 'd415188799f49f554a24064752bd6ce4d8a18c075b7b88b534e3150f253c09ae28a48554d2d1ba4be66b8441b2cbc364491d26bcead605c5fcecf4eaf622e224'
);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'accept: application/json',
    'Content-Type: application/x-www-form-urlencoded'
));

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";

$jsonResponse = json_decode($response, true);
print_r($jsonResponse);
?>
```
```perl
#!/usr/bin/perl
use strict;
use warnings;
use LWP::UserAgent;
use HTTP::Request::Common;

my $url = "https://secure.payu.in/merchant/postservice";

my %data = (
    form    => '2',
    key     => 'BmTY3G',
    command => 'validateVPA',
    var1    => '9999999999@upi',
    hash    => 'd415188799f49f554a24064752bd6ce4d8a18c075b7b88b534e3150f253c09ae28a48554d2d1ba4be66b8441b2cbc364491d26bcead605c5fcecf4eaf622e224'
);

my $ua = LWP::UserAgent->new;
$ua->timeout(30);

my $response = $ua->post($url, 
    Content_Type => 'application/x-www-form-urlencoded',
    Content => \%data
);

if ($response->is_success) {
    print "Status Code: " . $response->code . "\n";
    print "Response: " . $response->decoded_content . "\n";
} else {
    print "Error: " . $response->status_line . "\n";
}
```
