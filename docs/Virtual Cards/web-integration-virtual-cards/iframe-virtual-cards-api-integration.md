---
title: iFrame Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
PayU provides GPR cards as a solution for PayU partners. This offering includes a comprehensive suite of features such as Min-KYC, Full-KYC, Card Management and Limit Management.

## Step 1: Construct hash

Create a JSON request and Authorization header. Authorization header also contains hash.

**Hash string** can be create by using below formula and then convert it to **SHA-512** hash.

```plaintext
<RequestJsonString>|<Current Date>|<Secure Merchant salt>
```

To create JSON request String and Authorisation header, can use the following functions:

```javascript
function createRequestData() {
    return {
        "referenceId": "<String - Any unique reference id>",
        "redirectUrl": "<String - Last page URL from where merchant is redirect to Cards>",
        "mobileNumber": "<String - User Mobile number>",
        "walletUrn": "<String - User wallet urn linked with above mobile number>",
        "walletIdentifier": "<String - Merchant wallet identifier>"
    }
}

function getAuthHeader(date) {
    var data = createRequestData();
    data = JSON.stringify(data);
    date = date.toUTCString();
    var hash_string = data + '|' + date + '|' + salt;
    var hash = CryptoJS.SHA512(hash_string).toString(CryptoJS.enc.Hex);
    var authHeader = 'hmac username="' + values.key + '", ' + 'algorithm=sha512, headers="date", signature="' + hash + '"'
    return authHeader;
}

function getDate() {
    let date = new Date() return date.toUTCString()
}
```

## Step 2: Include header

Merchant can open a iFrame within its page itself. Add the inline JS script to your website’s header section, then call the `ppi.launch()` function and pass the request data objects when your customers click the card button. PayU will take care of showing the card and returns to your page when it is done.

## Step 3: Add meta-tags & scripts in the HTML header

Add the following meta-tag & JS script in the HTML header section of your website:

```javascript
<meta name="viewport" content="width=device-width, initial-scale=1">
 <script src="https://jssdk.payu.in/ppi/ppi.min.js"></script>`
```

> 📘
>
> Test Script
>
> Replace the script mentioned in the earlier code snippet with [https://jssdk-uat.payu.in/ppi/ppi.min.js](https://jssdk-uat.payu.in/bolt/bolt.min.js) to test the integration.

## Step 4: Pass request objects

The `ppi.launch()` function takes two arguments.

* In the first argument, the data objects contain the  request data. The format of the data object is as shown below:

```javascript
var data = {
    "data": < JsonString created by createRequestData > "Authorization": < Authorisation header created by getAuthHeader > "Date": < Current Date in UTC Format >
}
```

* The second argument is the Handler which contains two functions. The `responseHandler()` function and the `catchException()` function.

## Step 5: Catch exception

The `catchException()` function captures the error message in case of any exceptions.

```javascript
var handlers = {
    onCancel: function() {
        console.log("Canceled by user");
    },
    catchException: function(ppi) {
        console.log(ppi);
    }
};
window.ppi.launch(getIframeRequest(), handlers);
```

#### Sample request

```javascript
$(document).on('click', '#submit', function() {
    var data = {
        "data": '{            "referenceId": "123abc",            "redirectUrl": "https://www.google.co.in/",            "mobileNumber": "9528340384",            "walletUrn": "102233",            "walletIdentifier": "OLW"           }'
        "Authorization": 'hmac username="<merchant key>", algorithm="sha512", headers="date", signature="<hash>"'
        "Date": "Wed, 28 Jun 2023 11:25:19 GMT"
    };
    var handlers = {
        onCancel: function() {
            console.log("Canceled by user");
        },
        catchException: function(ppi) {
            console.log(ppi);
        }
    };
    window.ppi.launch(getIframeRequest(), handlers);
});
```

> 📘 Note:
>
> Here, when your customer clicks on the card button (#submit), this code triggers the `ppi.launch()` function that passes the parameters along with the `responseHandler()` and `catchException()`functions as arguments.
