---
title: CURL Walkthrough
description: This recipe provides a walkthrough of the various parts of a cURL request.
hidden: false
recipe:
  color: '#018FF4'
  icon: 🦉
---
```curl cURL
curl --request POST \
     --url https://uat-partner.payu.in/api/v3/merchants \
     --header 'Content-Type: application/x-www-form-urlencoded' \
     --header 'accept: application/json' \
     --header 'authorization: Bearer 67545abc1c953416624038c643b44739e152e4d1106389ecb9876fa8f4557fce' \
     --data-urlencode merchant%5Bdisplay_name%5D=test \
     --data-urlencode merchant%5Bemail%5D=test@payu.in \
     --data-urlencode merchant%5Bmobile%5D=9876543210 \
     --data-urlencode merchant%5Bbusiness_details%5D%5Bbusiness_entity_type%5D=Society \
     --data-urlencode merchant%5Bbusiness_details%5D%5Bpan%5D=ABCDG1234J \
     --data-urlencode merchant%5Bsigning_authority_details%5D%5Bpancard_number%5D=EFGHG1234J
```

```json Response Example
{"success":true}
```

# HTTP Methods

<!-- curl@1 -->

REST APIs use standard HTTP methods to perform operations on resources. The most commonly used methods are:
  - **GET**: Retrieves the representation of a resource.
  - **POST**: Creates a new resource.
  - **PUT**: Updates an existing resource.
  - **DELETE**: Deletes a resource.

# Environment or Endpoint

<!-- curl@2 -->

Endpoints are the URLs (Uniform Resource Locators) through which clients can access the resources. Each endpoint corresponds to a specific resource or a collection of resources.

# Header

<!-- curl@3-5 -->

The header contains the following:
* Content-Type: The Content-Type header in a REST API cURL request is used to indicate the media type of the resource being sent or requested1. It is an essential part of the HTTP header and is used to specify the format of the data being transmitted. The value of the Content-Type header can be set to various media types such as application/json, application/xml, text/html, etc23. 
* The Accept header in a REST API cURL request is used to specify the media type of the response that the client expects to receive from the server12. It is an optional part of the HTTP header and is used to indicate the format in which the client wants to receive the response data. The value of the Accept header can be set to various media types such as application/json, application/xml, text/html, etc13.
* authorization: The Authorization: Bearer header in a REST API cURL request is used to include an access token in the request header123. It is a common method of authentication and authorization in RESTful APIs. The Bearer authentication scheme is defined in the OAuth 2.0 specification1. In PayU India APIs, it is used Partner Integration APIs

# Request payload

<!-- curl@6-11 -->

The Request payload in a REST API cURL request is the data that is sent to the server as part of the HTTP request body123. It is used to send data to the server when creating or updating a resource. The request payload can be in various formats such as application/json, application/xml, text/plain, etc24.

To include the request payload in a cURL request, you can use the -d or --data option followed by the data you want to send. For example, to send a POST request with JSON data, you can use the following command:

curl -X POST -H "Content-Type: application/json" -d '{"name":"John Doe","age":30}' [URL]
Copy
Replace [URL] with the URL of the REST API endpoint5.