---
name: Validate_VPA
---
```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&command=validateVPA&var1=9999999999@upi&hash=75bb573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472fff9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e"
```
```python
import requests

url = "https://test.payu.in/merchant/postservice"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "key": "JP***g",
    "command": "validateVPA",
    "var1": "9999999999@upi",
    "hash": "75bb573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472fff9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e"
}

response = requests.post(url, headers=headers, data=data, params={"form": "2"})

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
        String url = "https://test.payu.in/merchant/postservice?form=2";
        
        Map<String, String> params = new HashMap<>();
        params.put("key", "JP***g");
        params.put("command", "validateVPA");
        params.put("var1", "9999999999@upi");
        params.put("hash", "75bb573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472fff9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e");
        
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

const url = 'https://test.payu.in/merchant/postservice?form=2';

const data = {
    key: 'JP***g',
    command: 'validateVPA',
    var1: '9999999999@upi',
    hash: '75bb573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472fff9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e'
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

$url = "https://test.payu.in/merchant/postservice?form=2";

$data = array(
    'key' => 'JP***g',
    'command' => 'validateVPA',
    'var1' => '9999999999@upi',
    'hash' => '75bb573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472fff9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e'
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

my $url = "https://test.payu.in/merchant/postservice?form=2";

my %data = (
    key     => 'JP***g',
    command => 'validateVPA',
    var1    => '9999999999@upi',
    hash    => '75bb573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472fff9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e'
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
