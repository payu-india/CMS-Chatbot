---
name: PayU Hosted Sample Request
---
```curl
curl -X POST "https://test.payu.in/_payment"
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
"key=JP***g&txnid=PQI6MqpYrjEefU&amount=10.00
&firstname=PayU User&email=test@gmail.com&phone=9876543210
&productinfo=iPhone&surl=
https://apiplayground-response.herokuapp.com/
&furl=https://apiplayground-response.herokuapp.com
&hash=05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072"
```
```python
import requests

url = "https://test.payu.in/_payment"
payload = "key=JP***g&txnid=Dnh8wYimuCRIdv&amount=10.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=&bankcode=&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=cb4b8bda5677dbe80f53735b1d0ec5d48164c3654627369268cf6bf266db994db39108ce2e0868c953e66c172f6b2d78836b253d3463d0cc40d9b6a93118ed56"
headers = { "Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded" }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

```
```php
<?php

$url = "https://test.payu.in/_payment";

$req = req_init($url);

req_setopt($req, CURLOPT_URL, $url);
req_setopt($req, CURLOPT_POST, true); 
req_setopt($req, CURLOPT_RETURNTRANSFER, true);

$headers = array(
    "Content-Type: application/x-www-form-urlencoded",
); 

req_setopt($curl, CURLOPT_HTTPHEADER, $headers);

$data = "key=JP***g&txnid=Dnh8wYimuCRIdv&amount=10.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=&bankcode=&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=&ccexpmon=&ccexpyr=&ccvv=&ccname=&txn_s2s_flow=&hash=cb4b8bda5677dbe80f53735b1d0ec5d48164c3654627369268cf6bf266db994db39108ce2e0868c953e66c172f6b2d78836b253d3463d0cc40d9b6a93118ed56";

req_setopt($curl, CURLOPT_POSTFIELDS, $data);

$resp = req_exec($req);

req_close($req);

var_dump($resp);

?>

```
```java
import org.apache.http.HttpResponse;
import org.apache.http.client.fluent.Request;
import org.apache.http.entity.ContentType;
import org.apache.http.util.EntityUtils;

public class Main {
    public static void main(String[] args) throws Exception {
        Request request = Request.Post("https://test.payu.in/_payment -H");

        String body = "key=JP***g&txnid=Dnh8wYimuCRIdv&amount=10.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=&bankcode=&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=&ccexpmon=&ccexpyr=&ccvv=&ccname=&txn_s2s_flow=&hash=cb4b8bda5677dbe80f53735b1d0ec5d48164c3654627369268cf6bf266db994db39108ce2e0868c953e66c172f6b2d78836b253d3463d0cc40d9b6a93118ed56";
        
        request.bodyString(body, ContentType.APPLICATION_FORM_URLENCODED);
        request.setHeader("Content-Type", "application/x-www-form-urlencoded");

        HttpResponse httpResponse = request.execute().returnResponse();

        System.out.println(httpResponse.getStatusLine());

        if (httpResponse.getEntity() != null) {
            String html = EntityUtils.toString(httpResponse.getEntity());
            System.out.println(html);
        }
    }
}

```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

namespace PayUExample
{
    class Program
    {
        static async Task Main(string[] args)
        {
            // Set the API endpoint URL
            string apiUrl = "https://test.payu.in/_payment";

            // Create an HttpClient instance
            using (HttpClient client = new HttpClient())
            {
                // Set request headers
                client.DefaultRequestHeaders.Add("accept", "application/json");
                client.DefaultRequestHeaders.Add("Content-Type", "application/x-www-form-urlencoded");

                // Set request parameters
                var content = new FormUrlEncodedContent(new[]
                {
                    new KeyValuePair<string, string>("key", "JP***g"),
                    new KeyValuePair<string, string>("txnid", "PQI6MqpYrjEefU"),
                    new KeyValuePair<string, string>("amount", "10.00"),
                    new KeyValuePair<string, string>("firstname", "PayU User"),
                    new KeyValuePair<string, string>("email", "test@gmail.com"),
                    new KeyValuePair<string, string>("phone", "9876543210"),
                    new KeyValuePair<string, string>("productinfo", "iPhone"),
                    new KeyValuePair<string, string>("surl", "https://apiplayground-response.herokuapp.com/"),
                    new KeyValuePair<string, string>("furl", "https://apiplayground-response.herokuapp.com"),
                    new KeyValuePair<string, string>("hash", "05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072")
                });

                // Send the POST request
                HttpResponseMessage response = await client.PostAsync(apiUrl, content);

                // Read the response content
                string responseContent = await response.Content.ReadAsStringAsync();

                // Print the response
                Console.WriteLine(responseContent);
            }
        }
    }
}

```
