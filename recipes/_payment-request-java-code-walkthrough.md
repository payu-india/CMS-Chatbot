---
title: _payment Request Java Code Walkthrough
description: >-
  This recipe provides code walkthrough of _payment request with PayU Hosted
  Integration with the Java language binding.
hidden: false
recipe:
  color: '#018FF4'
  icon: 🦉
---
```java Java
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

```json Response Example
{"success":true}
```

# importing the necessary libraries

<!-- java@1-4 -->

The script begins by importing the necessary libraries for making HTTP requests and handling the responses.

# Creating the Request

<!-- java@8 -->

The Request.Post() method is used to create a new HTTP POST request to the specified URL.

# Setting the Body

<!-- java@10-12 -->

The bodyString() method is used to set the body of the request. The body contains the necessary parameters required by PayU to process the payment. These include the merchant key, transaction ID, amount, customer details, product information, success and failure URLs, and a security hash.

# Setting the Header

<!-- java@13 -->

The setHeader() method is used to set the Content-Type header of the request to application/x-www-form-urlencoded.

# Executing the Request

<!-- java@15 -->

The execute().returnResponse() methods are used to send the request and get the response from the server.

# Printing the Status Line

<!-- java@17 -->

The getStatusLine() method is used to get the status line from the response. This is then printed to the console.

# Printing the Response Body

<!-- java@19-22 -->

If the response contains an entity (i.e., the body of the response), the EntityUtils.toString() method is used to convert this to a string. This is then printed to the console.