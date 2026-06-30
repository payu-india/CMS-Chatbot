---
title: Tokenize a Card API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Save a Card API
  description: >-
    The Save a Card API allows merchants to securely save customer card details
    to the PayU vault. This API returns a card token upon successful storage,
    ensuring compliance with RBI guidelines by requiring customer consent and
    additional authentication. Learn how to implement this API with detailed
    request parameters, sample requests, and environment configurations.
  keywords:
    - AEVV
    - save card
    - saved card API
    - authorization reference number
    - AMEX AEVV
    - American Express Verification Value
  robots: index
next:
  description: ''
---
The Tokenize a Card API is used for saving a card to the vault. After successfully storing a card, it returns the `cardToken`.

<Callout icon="📘" theme="info">
  ###

  **Note** As per RBI guidelines, taking consent from the customer and doing an additional factor of authentication is mandatory to tokenize the card. You must ensure this is done before using this API.
</Callout>

HTTP Method: **POST**

**Environment**

|                        |                                                                                                                        |
| :--------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| Test Environment       | \<[https://apitest.payu.in/merchant/postservice.php?form=2>](https://apitest.payu.in/merchant/postservice.php?form=2>) |
| Production Environment | \<[https://info.payu.in/merchant/postservice?form=2>](https://info.payu.in/merchant/postservice?form=2>)               |

## Request parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Reference</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>key<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The merchant key provided by PayU while onboarding.<br>For more information on how to generate the Key and Salt, refer to any of the following:  </p>
<ul>
<li><strong>Production</strong>: <a href="http://docs.payu.in/docs/generate-merchant-key-and-salt-on-payu-dashboard">Generate Merchant Key and Salt</a></li>
<li><strong>Test</strong>: <a href="http://docs.payu.in/docs/generate-test-merchant-key-and-salt">Generate Test Merchant Key and Salt</a></li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>JP*****g</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>command<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The command name for this REST API call must be included in this parameter. For getting user cards details, use <strong>save_payment_instrument</strong> here.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>save_payment_instrument</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>hash<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The hash must be included in this parameter. Hash logic for this API is:<br><code>sha512(key\|command\|var1\|salt) sha512  </code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var1<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The user credentials are posted in this parameter in the following format: MerchantKey:UserId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>JP***G:abc</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var2<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The nickname of the card is specified in this parameter.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>My_card</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var3<br>mandatory</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The card mode is specified in this parameter. For more information on card mode codes, refer to <a href="http://docs.payu.in/docs/card-type-codes-and-supported-banks-for-cards">Card Type Codes and Supported Banks for Cards</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>CC</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var4<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The card type of the card is specified in this parameter. For more information on card type codes, refer to <a href="http://docs.payu.in/docs/card-type-codes-and-supported-banks-for-cards">Card Type Codes and Supported Banks for Cards</a></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>AMEX</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var5<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The name on the card is specified in this parameter.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Ashish</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var6<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The card number is is specified in this parameter. For the <strong>test cards</strong> to do mock API calls, refer to <a href="http://docs.payu.in/docs/test-cards-upi-id-and-wallets">Test Cards, UPI ID and Wallets</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var7<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The card expiry month is specified in this parameter.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>9</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var8<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The card expiry year is specified in this parameter.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2021</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var9<br><code>mandatory for Rupay and AMEX cards</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Integer</code>This parameter can be any of the following based on the Rupay or AMEX card used:  </p>
<strong>Rupay Cards</strong>
<ul>
<li>Authentication Reference Number (AuthRefID) is required for Rupay BePG Flow.</li>
<li>DS Transaction ID is required for Rupay SecureNxt Card Tokenization.</li>
</ul>
<strong>AMEX Cards</strong>
<ul>
<li>The authorization reference number received during authorization call of AMEX card transactions.</li>
<li>The AEVV received during authorization call of AMEX card transactions.<br><strong>Notes</strong>:</li>
<li>This parameter is mandatory for AMEX cards. American Express Verification Value will be sent by the PG in the authorization response.</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;">
<ul>
<li>Rupay BePG Transaction ID :
authenticationCode : 100112026062200000001164999087</li>
 <li>DSTransID :
authenticationCode : a39d7f09-3891-44c9-bf22-ab3fcba46d8f</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var10<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter must be set to <strong>true</strong> if the transaction authentication has been done for the tokenization.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>true</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var11<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter must be set to <strong>true</strong> if the user has given consent to tokenise the card.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>true</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

```curl
curl --request POST \
     --url 'https://test.payu.in/merchant/postservice?form=2' \
     --header 'Content-Type: application/x-www-form-urlencoded' \
     --header 'accept: text/html; charset=UTF-8' \
     --data key=JPM7Fg \
     --data command=save_payment_instrument \
     --data var1=JPM7Fg:abc \
     --data var2=visaraghu \
     --data var3=CC \
     --data var4=CC \
     --data var5=ashish \
     --data var6=4895370077346937 \
     --data var7=11 \
     --data var8=25 \
     --data var10=true \
     --data var11=true \
     --data hash=7487417efc1e8f1aadd72ac35b410d74c94dbc21b21e01d5ac7b91db0f0d01705986d2d2094ab12fab6e794a4b54bd9c7aaaca2648ce2916bb5c9365ff95f3a3
```

## Sample response

### Success scenarios

- VISA

```plaintext
{
status: 1,
msg: "Card Stored Successfully.",
cardToken: "917757449926e57ff2662",
card_number: "XXXXXXXXXXXX1165",
card_label: "My_card",
network_token: "44173XXX1000XXX1",
issuer_token: QQ3LkzgZOnEjY428,
}
```

- Mastercard

```plaintext
{
status: 1,
msg: "Card Stored Successfully.",
cardToken: "917e296b5b6da5d20fbfb",
card_number: "XXXXXXXXXXXX2346",
card_label: "Test_Card",
network_token: "3117328711111210",
issuer_token: AQ3LkzgBNyEjY213,
}
```

- American Express

```plaintext
{
status: 1,
msg: "Card Stored Successfully.",
cardToken: "917e29XXX6da5XXCbfb",
card_number: "XXXXXXXXXXX1002",
card_label: "AMEX_Card",
network_token: "51273287XXX61215",
issuer_token: Va3RaqBNyPnY673,
}
```

- Rupay

```plaintext
{
status: 1,
msg: "Card Stored Successfully.",
cardToken: "91XXX96b5b6da5dXXXbfb",
card_number: "XXXXXXXXXXXX0001",
card_label: "Rupay_Card",
network_token: "712XXX870976XX2",
issuer_token: Ya4HawKgbLmr312,
}
```

- Diners

```plaintext
{
status: 1,
msg: "Card Stored Successfully.",
cardToken: "91XXX296b5b6da5XXXbfb",
card_number: "XXXXXXXXXXXX0009",
card_label: "Diner_Card",
"network_token": "8koNXXXC1bT0Hv5a",
"issuer_token": "LQ3QkzXXXnEjY428"
}
```

### Failure scenario

- If card Number is invalid

```plaintext
{
"status": 0
"msg": CardNumber is invalid
}
```

## Response parameters for Save a Card API

The following table describes the parameters in the response:

<Callout icon="📘" theme="info">
  ###

  **Note**:  For every successful payment transactions, PayU returns the **mihpayuid** and **cardToken** parameters to the merchants, but networkToken and issuer\_token are returned only if you are PCI-DSS compliant.
</Callout>

<HTMLBlock>{`
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>status</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The status of the response can be any of the following:<br>_ 1: Success <br>_  0: Failure</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>msg</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The description of the response whether the card details were stored successfully or not stored.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Card Stored Successfully.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cardToken</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The cardToken is sent by PayU for the successful response.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>74\*\*\*2e2fd9b7e\*\*\*24fef4e7ed7dac1fe624b7</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>network_token</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The network token is returned in this parameter.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>1234 5*** 9*** 3456</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>issuer_token</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The parameter contains the issuer token that is returned by issuer.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>3456 7*** A*** EFGH</code></p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

<br />