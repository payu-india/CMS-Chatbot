---
title: PayU Hosted Checkout Integration
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

To achieve PCI DSS compliance, merchants can utilize the PayU Card Management SDK solution for both Web and Mobile platforms.

<Cards cols={3}>
  <Card title="Construct JSON for Hashing" icon="fa-key">
    Create a JSON request and SHA-512 authorization header using the request data and a secure merchant salt.
  </Card>
  <Card title="Post the Request" icon="fa-paper-plane">
    FORM-POST the request to the PayU API endpoint to redirect customers to the Virtual Cards OTP page.
  </Card>
  <Card title="Add Meta-tags & Scripts" icon="fa-file-code">
    Add the PayU PPI JS script and viewport meta-tag to the HTML header section of your website.
  </Card>
  <Card title="Pass Request Objects" icon="fa-layer-group">
    Use `ppi.launch()` with the data object containing request data, authorization header, and date.
  </Card>
  <Card title="Catch Exception" icon="fa-exclamation-triangle">
    Handle errors and user cancellations using `catchException()` and `onCancel()` handler functions.
  </Card>
</Cards>

## Step 1: Construct JSON for Hashing

Create a JSON request and authorization header. Authorization header also contains hash.

**Hash string** can be created by using the following string and then convert it to **SHA-512** hash.

```plaintext
<RequestJsonString>|<Current Date>|<Secure Merchant salt>
```

To create RequestJsonString (JSON request String) in the above hash string and authorisation header, use the following code:

```javascript
function createRequestData() {
    return {
        "referenceId": "<String>",
        "redirectUrl": "<String>",
        "mobileNumber": "<String>",
        "walletUrn": "<String>",
        "walletIdentifier": "<String>"
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

<Accordion title="Description of Parameters" icon="fa-table">

| Parameter        | Description                                                      |
| :--------------- | :--------------------------------------------------------------- |
| referenceId      | Post any unique reference ID.                                    |
| redirectUrl      | Post the last page URL from where merchant is redirect to cards. |
| mobileNumber     | Post the customer mobile number.                                 |
| walletUrn        | Post the customer wallet URN linked with above mobile number.    |
| walletIdentifier | Post your wallet identifier.                                     |

</Accordion>

## Step 2: Post the Request

You can FORM-POST the request with appropriate parameters and it will be redirected to the [PayU Virtual Cards OTP](https://myaccount.payu.in/wallet/votp) page.

Create request using above functions and submit it as FORM-POST and it will redirected to PayU Hosted Checkout Card page.

```javascript
const url = 'https://api.payu.in/loyalty-points/olw/user/card/v1';
const data = <JsonString created by createRequestData>;
const authorization = <Authorisation header created by getAuthHeader>;
const formData = new FormData();
formData.append('data', data);
formData.append('Authorization', authorization);
formData.append('Date', <Current Date>.toUTCString());
fetch(url, {
        method: 'POST',
        body: formData
    }).then(response => {
            if (response.status === 500) {
                console.error('Server returned a 500 error');
            } else if (response.ok || response.status === 302) {
                const redirectUrl = response.url;
                if (redirectUrl) { window.location.href = redirectUrl; }
            } else {
                console.error('Error occurred:', response.status);
            }
    }).catch(error => { console.error('Network error:', error); });
```

<Callout icon="📘" theme="info">
  **Note**: Date and json request string in hash and post request must be identical.
</Callout>

## Step 3: Add Meta-tags & Scripts in the HTML Header

Add the following meta-tag & JS script in the HTML header section of your website:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://jssdk.payu.in/ppi/ppi.min.js"></script>
```

<Callout icon="📘" theme="info">
  **Test Script**: Replace the script mentioned in the earlier code snippet with [https://jssdk-uat.payu.in/ppi/ppi.min.js](https://jssdk-uat.payu.in/bolt/bolt.min.js) to test the integration.
</Callout>

## Step 4: Pass Request Objects

The `ppi.launch()` function takes two arguments.

* In the first argument, the data objects contain the request data. The format of the data object is as shown below:

```javascript
var data = {
    "data": <JsonString created by createRequestData>
    "Authorization": <Authorisation header created by getAuthHeader>
    "Date": <Current Date in UTC Format>
}
```

* The second argument is the Handler which contains two functions. The `responseHandler()` function and the `catchException()` function.

## Step 5: Catch Exception

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

<Accordion title="Sample Request" icon="fa-code">

```javascript
$(document).on('click', '#submit', function() {
    var data = {
        "data": '{
            "referenceId": "123abc",
            "redirectUrl": "https://www.google.co.in/",
            "mobileNumber": "9528340384",
            "walletUrn": "102233",
            "walletIdentifier": "OLW"
        }'
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

<Callout icon="📘" theme="info">
  **Note**: Here, when your customer clicks on the card button (#submit), this code triggers the `ppi.launch()` function that passes the parameters along with the `responseHandler()` and `catchException()` functions as arguments.
</Callout>

</Accordion>
