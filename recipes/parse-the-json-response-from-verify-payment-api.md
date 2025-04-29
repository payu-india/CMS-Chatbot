---
title: Parse the JSON Response from Verify Payment API
description: Recipe Description
hidden: false
recipe:
  color: '#018FF4'
  icon: 🦉
---
```javascript JavaScript
const response = {
  status: 1,
  msg: "Card Stored Successfully.",
  cardToken: "917757449926e57ff2662",
  card_number: "XXXXXXXXXXXX1165",
  card_label: "My_card",
  network_token: "44173XXX1000XXX1",
  issuer_token: "QQ3LkzgZOnEjY428",
};

const regex = /cardToken: "(\w+)",\n\s*card_number: "(\w+)",\n\s*card_label: "(\w+)",\n\s*network_token: "(\w+)",\n\s*issuer_token: "(\w+)"/;

const matches = response.toString().match(regex);

const cardToken = matches[1];
const cardNumber = matches[2];
const cardLabel = matches[3];
const networkToken = matches[4];
const issuerToken = matches[5];

console.log(`Card Token: ${cardToken}\nCard Number: ${cardNumber}\nCard Label: ${cardLabel}\nNetwork Token: ${networkToken}\nIssuer Token: ${issuerToken}`);

```

```python Python
response = {
  "status": 1,
  "msg": "Card Stored Successfully.",
  "cardToken": "917757449926e57ff2662",
  "card_number": "XXXXXXXXXXXX1165",
  "card_label": "My_card",
  "network_token": "44173XXX1000XXX1",
  "issuer_token": "QQ3LkzgZOnEjY428",
}

regex = r'cardToken: "(\w+)",\n\s*card_number: "(\w+)",\n\s*card_label: "(\w+)",\n\s*network_token: "(\w+)",\n\s*issuer_token: "(\w+)"'

matches = re.search(regex, str(response))

cardToken = matches.group(1)
cardNumber = matches.group(2)
cardLabel = matches.group(3)
networkToken = matches.group(4)
issuerToken = matches.group(5)

print(f"Card Token: {cardToken}\nCard Number: {cardNumber}\nCard Label: {cardLabel}\nNetwork Token: {networkToken}\nIssuer Token: {issuerToken}")

```

```php PHP
$response = array(
  "status" => 1,
  "msg" => "Card Stored Successfully.",
  "cardToken" => "917757449926e57ff2662",
  "card_number" => "XXXXXXXXXXXX1165",
  "card_label" => "My_card",
  "network_token" => "44173XXX1000XXX1",
  "issuer_token" => "QQ3LkzgZOnEjY428",
);

$regex = '/cardToken: "(\w+)",\n\s*card_number: "(\w+)",\n\s*card_label: "(\w+)",\n\s*network_token: "(\w+)",\n\s*issuer_token: "(\w+)"/';

preg_match($regex, print_r($response, true), $matches);

$cardToken = $matches[1];
$cardNumber = $matches[2];
$cardLabel = $matches[3];
$networkToken = $matches[4];
$issuerToken = $matches[5];

echo "Card Token: " . $cardToken . "\nCard Number: " . $cardNumber . "\nCard Label: " . $cardLabel . "\nNetwork Token: " . $networkToken . "\nIssuer Token: " . $issuerToken;

```

```java Java
String response = "{\n" +
                  "  status: 1,\n" +
                  "  msg: \"Card Stored Successfully.\",\n" +
                  "  cardToken: \"917757449926e57ff2662\",\n" +
                  "  card_number: \"XXXXXXXXXXXX1165\",\n" +
                  "  card_label: \"My_card\",\n" +
                  "  network_token: \"44173XXX1000XXX1\",\n" +
                  "  issuer_token: \"QQ3LkzgZOnEjY428\",\n" +
                  "}";

String regex = "cardToken: \"(\\w+)\",\\s*card_number: \"(\\w+)\",\\s*card_label: \"(\\w+)\",\\s*network_token: \"(\\w+)\",\\s*issuer_token: \"(\\w+)\"";

Pattern pattern = Pattern.compile(regex);
Matcher matcher = pattern.matcher(response);

String cardToken = "";
String cardNumber = "";
String cardLabel = "";
String networkToken = "";
String issuerToken = "";

if (matcher.find()) {
    cardToken = matcher.group(1);
    cardNumber = matcher.group(2);
    cardLabel = matcher.group(3);
    networkToken = matcher.group(4);
    issuerToken = matcher.group(5);
}

System.out.println("Card Token: " + cardToken + "\nCard Number: " + cardNumber + "\nCard Label: " + cardLabel + "\nNetwork Token: " + networkToken + "\nIssuer Token: " + issuerToken);

```

# Define the response

<!-- javascript@1-9 -->
<!-- python@1-9 -->
<!-- php@1-9 -->
<!-- java@1-9 -->

Define the response object (JS), dictionary (Python) or array (PHP) that contains the data we want to extract.

# Extract the required fields

<!-- javascript@11 -->
<!-- python@11 -->
<!-- php@11 -->
<!-- java@11 -->

Define a regular expression "regex" that matches the pattern of the fields we want to extract.

# Extract the value fields

<!-- javascript@13 -->
<!-- python@13 -->
<!-- php@13 -->
<!-- java@13-14 -->

JS: Use the match() method to extract the values of the fields from the response object using the regex pattern.
Python: Use the search() method to extract the values of the fields.
PHP: preg_match() function to extract the values of the fields from the $response array using the $regex pattern.
Java;  Use the Pattern and Matcher classes to extract the values of the fields

# Store the extracted values

<!-- javascript@15-19 -->
<!-- python@15-19 -->
<!-- php@15-19 -->
<!-- java@16-28 -->

Store the extracted values in separate variables for further use.

# Print the extracted values

<!-- javascript@21 -->
<!-- python@21 -->
<!-- php@21 -->
<!-- java@30 -->

JS: Print the extracted values using console.log().
PHP: Print the extracted values using echo.
Java; Print the extracted values using System.out.println().