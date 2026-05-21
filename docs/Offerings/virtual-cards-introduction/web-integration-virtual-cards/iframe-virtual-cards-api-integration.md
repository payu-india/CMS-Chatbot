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

<Cards cols={3}>
  <Card title="Construct Hash" icon="fa-key">
    Create a JSON request and SHA-512 authorization header using the request data and a secure merchant salt.
  </Card>
  <Card title="Include Header" icon="fa-code">
    Add the inline JS script to your header and call `ppi.launch()` when customers click the card button.
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

## Step 1: Construct Hash

Create a JSON request and Authorization header. Authorization header also contains hash.

**Hash string** can be created by using below formula and then convert it to **SHA-512** hash.

<Accordion title="Hash String Format" icon="fa-hashtag">

```plaintext
<RequestJsonString>|<Current Date>|<Secure Merchant salt>
```

</Accordion>

To create JSON request String and Authorisation header, use the following functions:

<Accordion title="Sample Code" icon="fa-code">

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

</Accordion>

## Step 2: Include Header

Merchant can open an iFrame within its page itself. Add the inline JS script to your website's header section, then call the `ppi.launch()` function and pass the request data objects when your customers click the card button. PayU will take care of showing the card and returns to your page when it is done.

## Step 3: Add Meta-tags & Scripts in the HTML Header

Add the following meta-tag & JS script in the HTML header section of your website:

<Accordion title="Code Snippet" icon="fa-code">

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://jssdk.payu.in/ppi/ppi.min.js"></script>
```

</Accordion>

> 📘
>
> Test Script
>
> Replace the script mentioned in the earlier code snippet with [https://jssdk-uat.payu.in/ppi/ppi.min.js](https://jssdk-uat.payu.in/bolt/bolt.min.js) to test the integration.

## Step 4: Pass Request Objects

The `ppi.launch()` function takes two arguments.

- In the first argument, the data objects contain the request data. The format of the data object is as shown below:

<Accordion title="Request Object Format" icon="fa-code">

```javascript
var data = {
    "data": <JsonString created by createRequestData>
    "Authorization": <Authorisation header created by getAuthHeader>
    "Date": <Current Date in UTC Format>
}
```

</Accordion>

- The second argument is the Handler which contains two functions. The `responseHandler()` function and the `catchException()` function.

## Step 5: Catch Exception

The `catchException()` function captures the error message in case of any exceptions.

<Accordion title="Sample Code" icon="fa-code">

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

</Accordion>

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

# 🧩 Setting Up a Custom IFrame Container

To ensure a stable integration with resize iframe, merchants are advised to create their own reusable iframe container.
This iframe will remain hidden until the SDK is launched, and can be reused for subsequent transactions.

<Accordion title="Container HTML" icon="fa-code">

```html
<iframe
  id="payuppiFrame"
  name="payuppiFrame"
  class="iFrameContainer"
></iframe>
```

</Accordion>

<Accordion title="Container CSS" icon="fa-code">

```css
.iFrameContainer {
    display: block;
    position: fixed;
    visibility: hidden;
    width: 100%;
    height: 80%;
    min-height: 90vh;
    left: 0;
    bottom: 0;
    z-index: 10000;
    overflow: hidden;
    background: rgba(255, 255, 255, 1) none repeat scroll 0 0;
}
```

</Accordion>

<Accordion title="Note" icon="fa-info-circle">

The iframe should be present in your page markup before SDK initialization.
The SDK will use this iframe to render the payment or OTP view when `useExistingIFrame` is set to `true`.

</Accordion>

<Accordion title="Passing the IFrame Reuse Parameter" icon="fa-recycle">

When initializing your iframe request, include the `useExistingIFrame` parameter as `true`.
This ensures that the SDK uses your existing container instead of creating a new iframe.

  <Accordion title="Sample Code" icon="fa-code">

  ```javascript
  function getIframeRequest() {
    const date = new Date();
    const header = getAuthHeader(date);
    return {
      data: header[1],
      Authorization: header[0],
      Date: date.toUTCString(),
      useExistingIFrame: true // enables iframe reuse
    };
  }
  ```

  </Accordion>

Before launching the SDK, make the iframe visible:

  <Accordion title="Sample Code — Show IFrame" icon="fa-code">

  ```javascript
  const iframe = document.getElementById("payuppiFrame");
  if (iframe) {
    iframe.style.visibility = "visible";
  }
  window.ppi.launch(getIframeRequest(), handlers);
  ```

  </Accordion>

</Accordion>

<Accordion title="Handling Callbacks and Hiding the IFrame" icon="fa-reply">

After the SDK flow completes or the user cancels the operation, hide the iframe again.
This keeps your UI clean and ensures a smooth re-launch experience for future transactions.

  <Accordion title="Sample Code" icon="fa-code">

  ```javascript
  var handlers = {
    onCancel: function () {
      console.log("Transaction cancelled by user");
      const iframe = document.getElementById("payuppiFrame");
      if (iframe) iframe.style.visibility = "hidden";
    },
    catchException: function (error) {
      console.log("Exception:", error);
      const iframe = document.getElementById("payuppiFrame");
      if (iframe) iframe.style.visibility = "hidden";
    }
  };
  ```

  </Accordion>

</Accordion>

<br />
