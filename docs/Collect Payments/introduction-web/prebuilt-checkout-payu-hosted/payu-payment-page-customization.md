---
title: Customize PayU Payment Page
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Customize PayU Payment Page or Checkout Page
  description: ''
  robots: index
next:
  description: ''
---
---
title: Customize PayU Payment Page
excerpt: >-
  Customize the PayU Hosted Checkout page: enforce payment modes with enforce_paymethod,
  hide options with drop_category, set display language with display_lang, and
  configure checkout payment methods.
deprecated: false
hidden: false
metadata:
  title: Customize PayU Payment Page or Checkout Page
  description: >-
    Customize PayU Hosted Checkout for the Collect Payment (/_payment) flow: use
    enforce_paymethod to limit payment modes (cards, UPI, netbanking, EMI, wallet,
    BNPL, QR, and more), drop_category to hide categories or bank/scheme codes,
    and display_lang for Hindi, Tamil, Marathi, and other languages. Covers
    checkout branding, payment method activation, and sample requests with hash,
    surl, furl, key, and txnid.
  keywords:
    - enforce_paymethod
    - drop_category
    - display_lang
    - language
    - PayU Hosted Checkout
    - payment page customization
    - Collect Payment API
    - _payment
    - hash
    - surl
    - furl
    - creditcard
    - debitcard
    - netbanking
    - upi
    - checkout settings
    - payment methods
  robots: index
next:
  description: ''
---

After you complete PayU Hosted Checkout integration, you will be able to see the PayU Payment page similar to the following screenshot when calling the **Collect Payment** API:

<Image align="center" border={true} width="400px" src="https://files.readme.io/1ee3893480e6e3d3c1e28d6ecffc4c52d1b3e8f2aba0247c9eb486dfef0fafc5-Screenshot_2024-09-06_at_11.54.02_AM.png" className="border" />

You can customize the following in the Checkout page:

* [Enforce Pay Method or Remove Category](#enforce-pay-method-or-remove-category)
* [Change the Language](#changing-the-language)
* [Configure Payment Method and Checkout Settings](#configure-checkout-payment-methods-and-settings)

## Enforce Pay Method or Remove Category

<Callout icon="📘" theme="info">
  **Note**: Before implementing on your Production environment, PayU strongly recommends you to enforce the payment parameters described in this section on the Test environment.
</Callout>

You can append the parameter names in your transaction request to opt for all or some of the payment modes.

<Accordion title="Enforce payment customization" icon="fa-code">
  Parameter name: **enforce\_paymethod**

  This parameter allows you to customize the payment options for each transaction. You can enforce specific payment modes, cards scheme, and specific banks under Net Banking using this method.

  You need to include the necessary payment options in this parameter and POST them to PayU at the transaction time. All the categories and sub-categories have specific values that need to be included in this string.

  The categories and sub-categories are as follows:

  | Category    | Sub-category                              |
  | :---------- | :---------------------------------------- |
  | Credit Card | MasterCard, Amex, Diners, etc.            |
  | Debit Card  | Visa, MasterCard, Maestro, etc.           |
  | Net Banking | SBI Net Banking, HDFC Net Banking, etc    |
  | EMI         | CITI 3 Months EMI, HFC 6 Months EMI, etc. |
  | Wallet      | Airtel Money, YPay, ITZ, Cash Card, etc.  |
  | UPI         | GooglePay, PhonePe, UPI, etc.             |

  <br />

  To enforce complete categories, use the values as described in the following table:

  | Category    | Value of enforce\_paymethod |
  | :---------- | :-------------------------- |
  | Credit Card | creditcard                  |
  | Debit Card  | debitcard                   |
  | Net Banking | netbanking                  |
  | NEFT/RTGS   | neftrtgs                    |
  | EMI         | emi                         |
  | UPI         | upi                         |
  | Wallet      | cashcard                    |
  | Sodexo      | SODEXO                      |
  | BNPL        | bnpl                        |
  | QR          | qr                          |

  To enforce sub-categories, use the respective bank codes for them. Contact PayU Support or at help.payu.in to get the respective bank codes.

  <Callout icon="📘" theme="info">
    **Note**: Ensure that you are using the delimiter as pipe (|) character between the values in these examples.
  </Callout>
</Accordion>

<Accordion title="Usage examples" icon="fa-code">
  #### creditcard|debitcard

  All the credit card and debit card options are displayed (as the whole category is enforced). The rest of the categories will not be displayed, that is, EMI, cash card, credit card, debit card, etc. – as they are not being mentioned in the string.

  <Accordion title="Sample request with single category" icon="fa-code">
    **Credit Card only (`creditcard`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=ENFCC001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=creditcard&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'ENFCC001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'enforce_paymethod': 'creditcard', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "ENFCC001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "enforce_paymethod", "creditcard" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'ENFCC001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod': 'creditcard',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=ENFCC001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=creditcard&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'ENFCC001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod' => 'creditcard',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'ENFCC001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        enforce_paymethod => 'creditcard',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```

    **Debit Card only (`debitcard`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=ENFDC001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=debitcard&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'ENFDC001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'enforce_paymethod': 'debitcard', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "ENFDC001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "enforce_paymethod", "debitcard" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'ENFDC001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod': 'debitcard',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=ENFDC001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=debitcard&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'ENFDC001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod' => 'debitcard',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'ENFDC001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        enforce_paymethod => 'debitcard',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```

    **Net Banking only (`netbanking`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=ENFNB001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=netbanking&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'ENFNB001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'enforce_paymethod': 'netbanking', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "ENFNB001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "enforce_paymethod", "netbanking" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'ENFNB001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod': 'netbanking',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=ENFNB001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=netbanking&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'ENFNB001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod' => 'netbanking',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'ENFNB001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        enforce_paymethod => 'netbanking',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```

    **NEFT/RTGS only (`neftrtgs`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=ENFNEFT001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=neftrtgs&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'ENFNEFT001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'enforce_paymethod': 'neftrtgs', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "ENFNEFT001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "enforce_paymethod", "neftrtgs" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'ENFNEFT001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod': 'neftrtgs',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=ENFNEFT001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=neftrtgs&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'ENFNEFT001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod' => 'neftrtgs',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'ENFNEFT001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        enforce_paymethod => 'neftrtgs',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```

    **EMI only (`emi`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=ENFEMI001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=emi&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'ENFEMI001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'enforce_paymethod': 'emi', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "ENFEMI001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "enforce_paymethod", "emi" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'ENFEMI001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod': 'emi',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=ENFEMI001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=emi&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'ENFEMI001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod' => 'emi',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'ENFEMI001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        enforce_paymethod => 'emi',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```

    **UPI only (`upi`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=ENFUPI001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=upi&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'ENFUPI001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'enforce_paymethod': 'upi', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "ENFUPI001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "enforce_paymethod", "upi" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'ENFUPI001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod': 'upi',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=ENFUPI001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=upi&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'ENFUPI001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod' => 'upi',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'ENFUPI001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        enforce_paymethod => 'upi',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```

    **Wallet / Cash Card only (`cashcard`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=ENFCASH001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=cashcard&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'ENFCASH001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'enforce_paymethod': 'cashcard', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "ENFCASH001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "enforce_paymethod", "cashcard" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'ENFCASH001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod': 'cashcard',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=ENFCASH001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=cashcard&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'ENFCASH001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod' => 'cashcard',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'ENFCASH001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        enforce_paymethod => 'cashcard',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```

    **Sodexo only (`SODEXO`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=ENFSODEXO001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=SODEXO&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'ENFSODEXO001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'enforce_paymethod': 'SODEXO', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "ENFSODEXO001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "enforce_paymethod", "SODEXO" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'ENFSODEXO001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod': 'SODEXO',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=ENFSODEXO001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=SODEXO&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'ENFSODEXO001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod' => 'SODEXO',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'ENFSODEXO001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        enforce_paymethod => 'SODEXO',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```

    **BNPL only (`bnpl`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=ENFBNPL001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=bnpl&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'ENFBNPL001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'enforce_paymethod': 'bnpl', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "ENFBNPL001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "enforce_paymethod", "bnpl" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'ENFBNPL001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod': 'bnpl',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=ENFBNPL001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=bnpl&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'ENFBNPL001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod' => 'bnpl',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'ENFBNPL001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        enforce_paymethod => 'bnpl',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```

    **QR only (`qr`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=ENFQR001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=qr&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'ENFQR001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'enforce_paymethod': 'qr', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "ENFQR001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "enforce_paymethod", "qr" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'ENFQR001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod': 'qr',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=ENFQR001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=qr&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'ENFQR001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod' => 'qr',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'ENFQR001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        enforce_paymethod => 'qr',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```
  </Accordion>

  #### creditcard|netbanking|cashcard

  All the credit card, Net Banking, and cash card options are displayed (as the whole category is enforced for these).

  <Callout icon="📘" theme="info">
    **Note**: Ensure you use this parameter only after testing properly as an incorrect string will lead to undesirable payment options being displayed.
  </Callout>

  For an example procedure on how to enforce payment with a credit card, refer to Enforce Payment with Credit Card.

  <Accordion title="Sample request with multiple categories" icon="fa-code">
    **Credit Card and Debit Card (`creditcard|debitcard`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=ENFCCDC001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=creditcard|debitcard&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'ENFCCDC001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'enforce_paymethod': 'creditcard|debitcard', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "ENFCCDC001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "enforce_paymethod", "creditcard|debitcard" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'ENFCCDC001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod': 'creditcard|debitcard',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=ENFCCDC001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=creditcard|debitcard&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'ENFCCDC001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod' => 'creditcard|debitcard',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'ENFCCDC001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        enforce_paymethod => 'creditcard|debitcard',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```

    **Credit Card, Net Banking, and Wallet (`creditcard|netbanking|cashcard`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=ENFMIX001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=creditcard|netbanking|cashcard&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'ENFMIX001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'enforce_paymethod': 'creditcard|netbanking|cashcard', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "ENFMIX001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "enforce_paymethod", "creditcard|netbanking|cashcard" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'ENFMIX001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod': 'creditcard|netbanking|cashcard',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=ENFMIX001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&enforce_paymethod=creditcard|netbanking|cashcard&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'ENFMIX001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'enforce_paymethod' => 'creditcard|netbanking|cashcard',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'ENFMIX001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        enforce_paymethod => 'creditcard|netbanking|cashcard',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```
  </Accordion>
</Accordion>

<Accordion title="Hide Specific Payment Modes" icon="fa-code">
  **Parameter name : drop\_category**

  The **drop\_category** parameter can be used if you want to hide one or multiple payment options. For example, if you consider the payment options such as credit card, debit card, and net banking, you can hide the credit card mode of payment.

  If 30 Net Banking options are available and you want to drop two of those net banking options (that is, do not display those two options on the PayU page), the **drop\_category** parameter can be used effectively.

  To drop the whole category, use the following values:

  | Category    | Category Value |
  | :---------- | :------------- |
  | Credit Card | CC             |
  | Debit Card  | DC             |
  | Net Banking | NB             |
  | NEFT/RTGS   | NEFTRTGS       |
  | EMI         | EMI            |
  | Wallet      | CASH           |
  | BNPL        | BNPL           |
  | Sodexo      | SODEXO         |

  To drop sub-categories mentioned in the above table, use the respective bank codes for them. For the list bankcodes, refer to [Bank and Card Codes for Integration](doc:bank-and-card-codes-for-integration).

  <Accordion title="Checkout customization examples" icon="fa-code">
    **drop\_category – DC|VISA|MAST**

    In this example:

    * For the debit card category, only Visa and Master Card options will be dropped, so they are not displayed on the PayU page.
    * All other active payment options are displayed.

    In this example:

    * For the credit card category, only the AMEX option is dropped and not displayed on the PayU page.
    * In the debit card category, only the VISA option would be dropped.
    * In the EMI category, only HDFC 6 months EMI option (bank code – EMI6) will be dropped.
    * All the other active payment options will be displayed on the PayU page.

    <Callout icon="📘" theme="info">
      **Note**: Use this parameter only after proper testing as an incorrect string will display undesirable payment modes.
    </Callout>
  </Accordion>

  <Accordion title="Sample request with a single payment method removed or dropped" icon="fa-code">
    **Hide Credit Card (`CC`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=DROPCC001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=CC&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'DROPCC001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'drop_category': 'CC', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "DROPCC001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "drop_category", "CC" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'DROPCC001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'drop_category': 'CC',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=DROPCC001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=CC&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'DROPCC001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'drop_category' => 'CC',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'DROPCC001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        drop_category => 'CC',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```

    **Hide Debit Card (`DC`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=DROPD001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=DC&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'DROPD001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'drop_category': 'DC', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "DROPD001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "drop_category", "DC" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'DROPD001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'drop_category': 'DC',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=DROPD001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=DC&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'DROPD001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'drop_category' => 'DC',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'DROPD001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        drop_category => 'DC',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```

    **Hide Net Banking (`NB`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=DROPB001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=NB&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'DROPB001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'drop_category': 'NB', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "DROPB001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "drop_category", "NB" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'DROPB001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'drop_category': 'NB',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=DROPB001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=NB&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'DROPB001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'drop_category' => 'NB',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'DROPB001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        drop_category => 'NB',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```

    **Hide NEFT/RTGS (`NEFTRTGS`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=DROPNE001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=NEFTRTGS&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'DROPNE001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'drop_category': 'NEFTRTGS', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "DROPNE001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "drop_category", "NEFTRTGS" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'DROPNE001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'drop_category': 'NEFTRTGS',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=DROPNE001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=NEFTRTGS&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'DROPNE001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'drop_category' => 'NEFTRTGS',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'DROPNE001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        drop_category => 'NEFTRTGS',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```

    **Hide EMI (`EMI`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=DROPEMI001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=EMI&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'DROPEMI001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'drop_category': 'EMI', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "DROPEMI001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "drop_category", "EMI" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'DROPEMI001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'drop_category': 'EMI',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=DROPEMI001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=EMI&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'DROPEMI001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'drop_category' => 'EMI',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'DROPEMI001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        drop_category => 'EMI',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```

    **Hide Wallet (`CASH`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=DROPCASH001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=CASH&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'DROPCASH001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'drop_category': 'CASH', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "DROPCASH001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "drop_category", "CASH" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'DROPCASH001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'drop_category': 'CASH',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=DROPCASH001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=CASH&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'DROPCASH001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'drop_category' => 'CASH',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'DROPCASH001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        drop_category => 'CASH',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```

    **Hide BNPL (`BNPL`)**

    ````curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=DROPBNPL001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=BNPL&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'DROPBNPL001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'drop_category': 'BNPL', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ````
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "DROPBNPL001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "drop_category", "BNPL" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'DROPBNPL001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'drop_category': 'BNPL',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=DROPBNPL001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=BNPL&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'DROPBNPL001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'drop_category' => 'BNPL',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'DROPBNPL001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        drop_category => 'BNPL',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```

    **Hide Sodexo (`SODEXO`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=DROPSODEXO001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=SODEXO&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'DROPSODEXO001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'drop_category': 'SODEXO', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "DROPSODEXO001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "drop_category", "SODEXO" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'DROPSODEXO001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'drop_category': 'SODEXO',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=DROPSODEXO001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=SODEXO&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'DROPSODEXO001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'drop_category' => 'SODEXO',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'DROPSODEXO001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        drop_category => 'SODEXO',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```
  </Accordion>

  <Accordion title="Sample request with multiple payment method removed or dropped" icon="fa-code">
    **Hide Credit Card and Net Banking (`CC|NB`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=DROP2CAT001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=CC|NB&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'DROP2CAT001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'drop_category': 'CC|NB', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "DROP2CAT001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "drop_category", "CC|NB" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'DROP2CAT001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'drop_category': 'CC|NB',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=DROP2CAT001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=CC|NB&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'DROP2CAT001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'drop_category' => 'CC|NB',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'DROP2CAT001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        drop_category => 'CC|NB',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```

    #### `drop_category` — hide sub-options (bank / scheme codes)

    Use the bank and scheme codes from [Bank and Card Codes for Integration](doc:bank-and-card-codes-for-integration) (illustrative codes below match the earlier examples in this page).

    **Debit Card: drop Visa and Mastercard only (`DC|VISA|MAST`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=DROPSUB001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=DC|VISA|MAST&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'DROPSUB001', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'drop_category': 'DC|VISA|MAST', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "DROPSUB001" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "drop_category", "DC|VISA|MAST" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'DROPSUB001',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'drop_category': 'DC|VISA|MAST',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=DROPSUB001&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=DC|VISA|MAST&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'DROPSUB001',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'drop_category' => 'DC|VISA|MAST',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'DROPSUB001',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        drop_category => 'DC|VISA|MAST',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```

    **Mixed sub-category drops (`CC|AMEX, DC|VISA, EMI|EMI6`)**

    ```curl
    curl -X POST "https://test.payu.in/_payment" \
          -H "accept: application/json" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "key=JP***g&txnid=DROPSUB002&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=CC|AMEX, DC|VISA, EMI|EMI6&hash=REPLACE_WITH_GENERATED_HASH"
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'key': 'JP***g', 'txnid': 'DROPSUB002', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'drop_category': 'CC|AMEX, DC|VISA, EMI|EMI6', 'hash': 'REPLACE_WITH_GENERATED_HASH'}

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Collections.Generic;
    using System.Threading.Tasks;

    class Program
    {
        static async Task Main(string[] args)
        {
            using var client = new HttpClient();
            
            var url = "https://test.payu.in/_payment";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");
            
            var payload = new Dictionary<string, string>
            {
                { "key", "JP***g" },
                { "txnid", "DROPSUB002" },
                { "amount", "10.00" },
                { "firstname", "PayU User" },
                { "email", "test@gmail.com" },
                { "phone", "9876543210" },
                { "productinfo", "iPhone" },
                { "surl", "https://apiplayground-response.herokuapp.com/" },
                { "furl", "https://apiplayground-response.herokuapp.com/" },
                { "drop_category", "CC|AMEX, DC|VISA, EMI|EMI6" },
                { "hash", "REPLACE_WITH_GENERATED_HASH" }
            };
            
            var content = new FormUrlEncodedContent(payload);
            
            var response = await client.PostAsync(url, content);
            var result = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine(result);
        }
    }
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const url = 'https://test.payu.in/_payment';

    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    const payload = {
        'key': 'JP***g',
        'txnid': 'DROPSUB002',
        'amount': '10.00',
        'firstname': 'PayU User',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'drop_category': 'CC|AMEX, DC|VISA, EMI|EMI6',
        'hash': 'REPLACE_WITH_GENERATED_HASH'
    };

    axios.post(url, qs.stringify(payload), { headers: headers })
        .then(response => {
            console.log(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    ```
    ```java
    import java.io.*;
    import java.net.*;
    import java.net.http.*;

    public class PayUPayment {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpClient client = HttpClient.newHttpClient();
            
            String formData = "key=JP***g&txnid=DROPSUB002&amount=10.00&firstname=PayU%20User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&drop_category=CC|AMEX, DC|VISA, EMI|EMI6&hash=REPLACE_WITH_GENERATED_HASH";
            
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            System.out.println(response.body());
        }
    }
    ```
    ```php
    <?php
    $url = 'https://test.payu.in/_payment';

    $headers = array(
        'accept: application/json',
        'Content-Type: application/x-www-form-urlencoded'
    );

    $payload = array(
        'key' => 'JP***g',
        'txnid' => 'DROPSUB002',
        'amount' => '10.00',
        'firstname' => 'PayU User',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'drop_category' => 'CC|AMEX, DC|VISA, EMI|EMI6',
        'hash' => 'REPLACE_WITH_GENERATED_HASH'
    );

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;
    ?>
    ```
    ```perl
    use strict;
    use warnings;
    use LWP::UserAgent;
    use HTTP::Request::Common;

    my $url = 'https://test.payu.in/_payment';

    my $ua = LWP::UserAgent->new;

    my %payload = (
        key => 'JP***g',
        txnid => 'DROPSUB002',
        amount => '10.00',
        firstname => 'PayU User',
        email => 'test@gmail.com',
        phone => '9876543210',
        productinfo => 'iPhone',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        drop_category => 'CC|AMEX, DC|VISA, EMI|EMI6',
        hash => 'REPLACE_WITH_GENERATED_HASH'
    );

    my $response = $ua->post(
        $url,
        'accept' => 'application/json',
        'Content-Type' => 'application/x-www-form-urlencoded',
        Content => \%payload
    );

    print $response->content;
    ```
  </Accordion>
</Accordion>

## Change the Language

To change the display language in PayU Hosted Checkout, add the `language` parameter to the payment request API call. The following video shows how vernacular support can improve your business:

<Embed url="https://www.youtube.com/watch?v=7UCT0jFbB90" href="https://www.youtube.com/watch?v=7UCT0jFbB90" typeOfEmbed="youtube" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252F7UCT0jFbB90%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253D7UCT0jFbB90%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252F7UCT0jFbB90%252Fhqdefault.jpg%26key%3D7788cb384c9f4d5dbbdbeffd9fe4b92f%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

The `display_lang` parameter should be set to one of the following values (same as corresponding language spelling):

* English
* Hindi
* Tamil
* Telugu
* Kannada
* Gujarati
* Marathi

Here is an example payment request API call with the `display_lang` parameter set to Hindi:

```curl
curl -X POST "https://test.payu.in/_payment" \
      -H "accept: application/json" \
      -H "Content-Type: application/x-www-form-urlencoded" \
      -d "key=JP***g&txnid=PQI6MqpYrjEefU&amount=10.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&display_lang=Hindi&hash=05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072"
```
```python
import requests

url = "https://test.payu.in/_payment"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = {'key': 'JP***g', 'txnid': 'PQI6MqpYrjEefU', 'amount': '10.00', 'firstname': 'PayU User', 'email': 'test@gmail.com', 'phone': '9876543210', 'productinfo': 'iPhone', 'surl': 'https://apiplayground-response.herokuapp.com/', 'furl': 'https://apiplayground-response.herokuapp.com/', 'display_lang': 'Hindi', 'hash': '05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072'}

response = requests.post(url, headers=headers, data=payload)
print(response.text)
```
```csharp
using System;
using System.Net.Http;
using System.Collections.Generic;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        using var client = new HttpClient();
        
        var url = "https://test.payu.in/_payment";
        
        client.DefaultRequestHeaders.Add("accept", "application/json");
        
        var payload = new Dictionary<string, string>
        {
            { "key", "JP***g" },
            { "txnid", "PQI6MqpYrjEefU" },
            { "amount", "10.00" },
            { "firstname", "PayU User" },
            { "email", "test@gmail.com" },
            { "phone", "9876543210" },
            { "productinfo", "iPhone" },
            { "surl", "https://apiplayground-response.herokuapp.com/" },
            { "furl", "https://apiplayground-response.herokuapp.com/" },
            { "display_lang", "Hindi" },
            { "hash", "05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072" }
        };
        
        var content = new FormUrlEncodedContent(payload);
        
        var response = await client.PostAsync(url, content);
        var result = await response.Content.ReadAsStringAsync();
        
        Console.WriteLine(result);
    }
}
```
```javascript
const axios = require('axios');
const qs = require('querystring');

const url = 'https://test.payu.in/_payment';

const headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
};

const payload = {
    'key': 'JP***g',
    'txnid': 'PQI6MqpYrjEefU',
    'amount': '10.00',
    'firstname': 'PayU User',
    'email': 'test@gmail.com',
    'phone': '9876543210',
    'productinfo': 'iPhone',
    'surl': 'https://apiplayground-response.herokuapp.com/',
    'furl': 'https://apiplayground-response.herokuapp.com/',
    'display_lang': 'Hindi',
    'hash': '05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072'
};

axios.post(url, qs.stringify(payload), { headers: headers })
    .then(response => {
        console.log(response.data);
    })
    .catch(error => {
        console.error(error);
    });
```
```java
import java.io.*;
import java.net.*;
import java.net.http.*;

public class PayUPayment {
    public static void main(String[] args) throws IOException, InterruptedException {
        HttpClient client = HttpClient.newHttpClient();
        
        String formData = "key=JP***g&txnid=PQI6MqpYrjEefU&amount=10.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&display_lang=Hindi&hash=05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072";
        
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://test.payu.in/_payment"))
            .header("accept", "application/json")
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formData))
            .build();
        
        HttpResponse<String> response = client.send(request, 
            HttpResponse.BodyHandlers.ofString());
        
        System.out.println(response.body());
    }
}
```
```php
<?php
$url = 'https://test.payu.in/_payment';

$headers = array(
    'accept: application/json',
    'Content-Type: application/x-www-form-urlencoded'
);

$payload = array(
    'key' => 'JP***g',
    'txnid' => 'PQI6MqpYrjEefU',
    'amount' => '10.00',
    'firstname' => 'PayU User',
    'email' => 'test@gmail.com',
    'phone' => '9876543210',
    'productinfo' => 'iPhone',
    'surl' => 'https://apiplayground-response.herokuapp.com/',
    'furl' => 'https://apiplayground-response.herokuapp.com/',
    'display_lang' => 'Hindi',
    'hash' => '05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072'
);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```
```perl
use strict;
use warnings;
use LWP::UserAgent;
use HTTP::Request::Common;

my $url = 'https://test.payu.in/_payment';

my $ua = LWP::UserAgent->new;

my %payload = (
    key => 'JP***g',
    txnid => 'PQI6MqpYrjEefU',
    amount => '10.00',
    firstname => 'PayU User',
    email => 'test@gmail.com',
    phone => '9876543210',
    productinfo => 'iPhone',
    surl => 'https://apiplayground-response.herokuapp.com/',
    furl => 'https://apiplayground-response.herokuapp.com/',
    display_lang => 'Hindi',
    hash => '05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072'
);

my $response = $ua->post(
    $url,
    'accept' => 'application/json',
    'Content-Type' => 'application/x-www-form-urlencoded',
    Content => \%payload
);

print $response->content;
```

The PayU payment page is displayed with the display language as "Hindi" similar to the following screenshot:

![](https://files.readme.io/3aae0ef-hindipage.png)

## Configure Checkout Payment Methods and Settings

By default, the following payment methods are enabled for merchants on PayU Payment page (with PayU Hosted Checkout integration):

* NetBanking
* Debit Card
* Credit Card
* UPI
* Wallet

You can enable the following modes if you are eligible using Dashboard:

* BNPL
* EMI
* International Payments

<Callout icon="📘" theme="info">
  **Note**: You can enable or activate any of the above payment modes only if your are eligible or you have signed an agreement with PayU. If you are unable to raise request using Dashboard, contact your PayU Key Account Manager.
</Callout>

The following procedures describes how to enable payment mode or a feature.

<Accordion title="Enable a payment method" icon="fa-table">
  To configure the Dashboard to enable payment method:

  1. Navigate to **Dashboard > Settings > Payment Methods.**

     The *Manage Payment Methods* page is displayed with **Debit Card** tab selected by default.

  <Image align="center" border={true} src="https://files.readme.io/30b21d8-Screenshot_2024-07-19_at_10.34.10_AM.png" width="722px" />

  2. Select any of the payment method tab that you wish to configure.

     If you are eligible for the payment method, the **Activate Now** button is displayed. For example, the **Activate Now** button is enabled in the **International Payments** tab.

  <Image align="center" border={true} src="https://files.readme.io/87d81fd-Screenshot_2024-07-19_at_10.35.59_AM.png" width="722px" />

  3. Click **Activate Now**.

     A pop-up dialog box is displayed similar to the following screenshot and this will vary according to the payment method:

  <Image align="center" src="https://files.readme.io/6d9c81f-Screenshot_2024-07-19_at_10.37.45_AM.png" width="622px" />

  4. Click **Proceed** to activate.

     A confirmation message is displayed.
</Accordion>

<Accordion title="Activate PayPal wallet" icon="fa-table">
  To activate PayPal wallet and start collecting payments with PayPal:

  1. Follow the steps as in [Enable a payment method](#enable-a-payment-method).
  2. Click **Link PayPal account**.

  You are redirected to the PayPal page similar to the following screenshot.

  <Image align="center" border={true} src="https://files.readme.io/15f4290-Screenshot_2024-03-14_at_2.22.56_PM.png" width="320px" />

  3. Enter your email address that you want to use in future with PayPal.

  <Image align="center" border={true} src="https://files.readme.io/fc21647-Screenshot_2024-03-14_at_2.23.12_PM.png" width="320px" />

  4. Select your country as **India**.
  5. Click **Next**.
  6. Enter the password to create the account.

  <Image align="center" src="https://files.readme.io/c498645-Screenshot_2024-03-14_at_2.23.36_PM.png" width="320px" />

  7. Select your nature of your business and PAN details, name to displayed on statement and website URL as required and click **Next**.

  <Image align="center" border={true} src="https://files.readme.io/5d0d968-Screenshot_2024-03-14_at_5.07.28_PM.png" width="320px" />

  8. Enter your name, date of birth and contact details.

  <Image align="center" border={true} src="https://files.readme.io/e137009-paypal_name_dob.png" width="320px" />

  9. Scroll down and enter the business contact phone number and primary

  <Image align="center" border={true} src="https://files.readme.io/2e3e74f-paypal_details_mobile_currency.png" width="320px" />

  10. Click **Next**.

  <Image align="center" border={true} src="https://files.readme.io/32522a2-paypal_details_thanks_signup.png" width="320px" />

  <Callout icon="📘" theme="info">
    **Note**:  Contact your PayU Key Account Manager to remove a payment mode from the Checkout page.
  </Callout>
</Accordion>

## Configure Checkout Settings

The **Checkout Customisation** page on PayU Dashboard lets you tailor your checkout page to match your brand identity and prioritise the payment methods that are most relevant to your customers.

You can perform the following tasks from this page:

* Add your brand logo and apply your brand colours.
* Set a default language for the checkout page.
* Add an owner signature that appears on invoices and customer-facing pages.
* Choose the order in which payment methods appear at checkout, or let PayU recommend the order automatically.

A live preview on the right-hand side of the page shows how your checkout page will appear on **Desktop** and **Mobile** devices as you make changes.

> <Callout icon="👍" theme="okay">
>   **Reference**: For more information on PayU hosted Checkout integration, refer to [PayU Hosted Checkout](doc:prebuilt-checkout-payu-hosted).
> </Callout>

<Accordion title="Configure Brandings" icon="fa-table">
  To update your brand settings:

  1. Navigate to **Dashboard > Settings > Checkout Settings.**

     The *Set up your brand* page is displayed.

  <Image align="center" border={true} src="https://files.readme.io/eb8cf99-Screenshot_2024-07-19_at_10.43.53_AM.png" />

  2. Select or enter the details as described in the following table:

  <Table align={["left","left"]}>
    <thead>
      <tr>
        <th>
          Field
        </th>

        <th>
          Description
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          Brand Logo
        </td>

        <td>
          Enter the location or URL of the brand logo.

          **Note**: You need to that the size of the logo image is 90×90 and format of the logo image is PNG
        </td>
      </tr>

      <tr>
        <td>
          Secondary Color
        </td>

        <td>
          Click the color chooser to choose the color theme for the checkout page.
        </td>
      </tr>

      <tr>
        <td>
          Language
        </td>

        <td>
          Select the language from the **Language** drop-down list that has to be displayed on the Checkout page.
        </td>
      </tr>

      <tr>
        <td>
          Owner Signature
        </td>

        <td>
          Click **Select the file from your library** to select the signature file and click **Upload** to complete the action.
        </td>
      </tr>
    </tbody>
  </Table>

  <Callout icon="📘" theme="info">
    **Note**: While you configure each field above on the ,  you can see the preview in the right pane. For example, if you add or update the brand logo URL, it will be updated in the right pane preview.
  </Callout>
</Accordion>

<Accordion title="Customize the Payment Order" icon="fa-list">
  <Accordion title="Set a Custom Payment Method Orde" icon="fa-cash">
    Set a custom order if you want to control exactly which payment method appears first, second, and so on at checkout.

    To set a custom payment method order:

    1. Select **Manage Checkout** >  *Checkout Customisation* from the menu on left pane.
    2. Select the **Features for Website platform** tab.
   The  **Features for Website platform** tab is displayed.
<Image align="center" border={true} src="https://files.readme.io/07ec42d3ae1c1192e90fd79bc6f1de2e85c6bb8aa886131ce55e11cca666c7dd-Features_for_Website_platform_tab.png" className="border" />

    3. Under **Payment Methods Order**, select **Set Order**.

    The `Payment Method Order` pop-up page is displayed with the list of your integrated payment methods..

    <Image align="center" border={true} src="https://files.readme.io/721753e89db5f00f6bef65082da4a6b5ba42b3477cc9da91352fa42acb6b3580-Order_of_Payment_Modes.png" />

    4. To reorder the list, drag a payment method by the handle on the left and drop it in the position where you want it to appear.

       For example, to show **UPI** at the top of the checkout page, drag it above **Cards (Credit/Debit)**.

    5. Repeat the previous step until the payment methods appear in the order you want.

    6. Select **Save Changes** to apply the new order.

       The custom order is reflected immediately in the preview pane.
  </Accordion>

  <Accordion title="Enable PayU Recommended Order" icon="fa-cash">
    Enable PayU Recommended Order if you want PayU to automatically prioritise payment methods based on real-time signals such as customer behaviour and cart value. This option helps to improve conversion without requiring you to manage the order manually.

    To enable PayU Recommended Order:

    1. Select **Manage Checkout** >  *Checkout Customisation* from the menu on left pane.
    2. Select the **Features for Website platform** tab.

   The  **Features for Website platform** tab is displayed.
<Image align="center" border={true} src="https://files.readme.io/07ec42d3ae1c1192e90fd79bc6f1de2e85c6bb8aa886131ce55e11cca666c7dd-Features_for_Website_platform_tab.png" className="border" />

    3. Under **Payment Methods Order**, turn on the **PayU Recommended Order** toggle.

       When this toggle is turned on, PayU automatically determines the order of payment methods at checkout, and the **Set Order** option is disabled.

    4. Select **Apply Changes** to save your settings.

    > **Note:** To switch back to a custom order, turn off the **PayU Recommended Order** toggle, and then follow the steps in [Set a Custom Payment Method Order](#set-a-custom-payment-method-order).
  </Accordion>
</Accordion>
