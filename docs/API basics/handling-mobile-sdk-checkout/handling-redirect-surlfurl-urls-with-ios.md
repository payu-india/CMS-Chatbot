---
title: Handling Redirect (surl/furl) URLs with iOS
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
Redirect URLs are where PayU redirects the user after the transaction is completed. PayU sends the data related to transactions while redirecting so that you can check the status of the transaction. The `surl` and `furl` refer to the success and failure URLs (page) respectively. These URLs are used to return the customer to your website after a successful or failed transaction.  
The `surl` or `furl` page is hosted on your server to communicate back to the client application when the transaction is completed. You may check the status of the transaction and take action accordingly. In mobile applications, your customer must return to the app whenever a transaction is completed. After the transaction is complete, PayU posts the response to the surl / furl.

> 🚧 Keep in mind
> 
> Surl(success url), Furl(failure url) are two urls (https POST) should be given by merchant as post param while making payment. As soon as the transaction completes payu post the data back to surl/furl depends on the transaction status.
> 
> SURL/FURL must implement a javascript interface function named
> 
> `PayU.onSuccess(“data”) or PayU.onFailure(“data”);`

## Success URL

You can use the PayU Checkout Pro SDK to handle **furl** callback similar to the following sample code:

```php
<?php

error_reporting(0);

$salt = "<SALT Value>"; # pass your salt value in this variable


$amount = $_POST["amount"]; # amount need to be picked up from your database


$reverseHash = generateReverseHash();

if ($_POST["hash"] == $reverseHash)
{
    # transaction Succeeded
    # do the required javascript task
    echo ("Transaction Succeeded & Verified");
    successCallbackToApp($_POST);
}
else
{
    # transaction is tempered
    # handle it as required
    echo ("<br>");
    echo "\nInvalid transaction--";
}

# For iOS Success
function successCallbackToApp($payuResponse)
{
	$appResponse->response = http_build_query($payuResponse);
    $appResponseInJSON = json_encode($appResponse);

    
    $res= "" . http_build_query($payuResponse);
    $res= strval($res);

    echo '<script type="text/javascript">';
    // For WKWebview
    echo'if (typeof window.webkit.messageHandlers.observe.postMessage == "function")';
    echo "{ window.webkit.messageHandlers.observe.postMessage({'onSuccess':JSON.stringify($appResponseInJSON)}); }";
    // For UIWebView
    echo 'else { function payu_merchant_js_callback() { PayU.onSuccess("' .$res.'");  } }';
    echo '</script>';
}

# Function to generate reverse hash
function generateReverseHash()
{
    global $salt;
    global $amount;
    if ($_POST["additional_charges"] != null)
    {

        $reversehash_string = $_POST["additional_charges"] . "|" . $salt . "|" . $_POST["status"] . "||||||" . $_POST["udf5"] . "|" . $_POST["udf4"] . "|" . $_POST["udf3"] . "|" . $_POST["udf2"] . "|" . $_POST["udf1"] . "|" . $_POST["email"] . "|" . $_POST["firstname"] . "|" . $_POST["productinfo"] . "|" . $amount . "|" . $_POST["txnid"] . "|" . $_POST["key"];

    }
    else
    {
        $reversehash_string = $salt . "|" . $_POST["status"] . "||||||" . $_POST["udf5"] . "|" . $_POST["udf4"] . "|" . $_POST["udf3"] . "|" . $_POST["udf2"] . "|" . $_POST["udf1"] . "|" . $_POST["email"] . "|" . $_POST["firstname"] . "|" . $_POST["productinfo"] . "|" . $amount . "|" . $_POST["txnid"] . "|" . $_POST["key"];

    }

    //  echo($reversehash_string);
    $reverseHash = strtolower(hash("sha512", $reversehash_string));

    return $reverseHash;
}

?>
```

## Failure URL

You can use the PayU Checkout Pro SDK to handle **furl** callback similar to the following sample code:

```php
<?php

error_reporting(0);

$salt ="<SALT Value>"; # pass your salt value in this variable


$amount = $_POST["amount"]; # amount need to be picked up from your database


$reverseHash = generateReverseHash();

if ($_POST["hash"] == $reverseHash)
{
    # transaction failed
    # do the required javascript task
    echo ("Transaction Failed & Verified");
    failureCallbackToApp($_POST);
}
else
{
    # transaction is tempered
    # handle it as required
    echo ("<br>");
    echo "\nInvalid transaction--";
}

# For iOS Failure
function failureCallbackToApp($payuResponse)
{
	$appResponse->response = http_build_query($payuResponse);
    $appResponseInJSON = json_encode($appResponse);

    
    $res= "" . http_build_query($payuResponse);
    $res= strval($res);

    echo '<script type="text/javascript">';
    // For WKWebview
    echo'if (typeof window.webkit.messageHandlers.observe.postMessage == "function")';
    echo "{ window.webkit.messageHandlers.observe.postMessage({'onFailure':JSON.stringify($appResponseInJSON)}); }";
    // For UIWebView
    echo 'else { function payu_merchant_js_callback() { PayU.onFailure("' .$res.'");  } }';
    echo '</script>';
}

# Function to generate reverse hash
function generateReverseHash()
{
    global $salt;
    global $amount;
    if ($_POST["additional_charges"] != null)
    {

        $reversehash_string = $_POST["additional_charges"] . "|" . $salt . "|" . $_POST["status"] . "||||||" . $_POST["udf5"] . "|" . $_POST["udf4"] . "|" . $_POST["udf3"] . "|" . $_POST["udf2"] . "|" . $_POST["udf1"] . "|" . $_POST["email"] . "|" . $_POST["firstname"] . "|" . $_POST["productinfo"] . "|" . $amount . "|" . $_POST["txnid"] . "|" . $_POST["key"];

    }
    else
    {
        $reversehash_string = $salt . "|" . $_POST["status"] . "||||||" . $_POST["udf5"] . "|" . $_POST["udf4"] . "|" . $_POST["udf3"] . "|" . $_POST["udf2"] . "|" . $_POST["udf1"] . "|" . $_POST["email"] . "|" . $_POST["firstname"] . "|" . $_POST["productinfo"] . "|" . $amount . "|" . $_POST["txnid"] . "|" . $_POST["key"];

    }

    //  echo($reversehash_string);
    $reverseHash = strtolower(hash("sha512", $reversehash_string));

    return $reverseHash;
}

?>
```

In the above code, you need to replace the placeholders with your actual values. The default values for `surl` and `furl` are:

- **surl**: <https://cbjs.payu.in/sdk/success>
- **furl**: <https://cbjs.payu.in/sdk/failure>

> 📘 Note:
> 
> These URLs are for temporary use. PayU recommends you to design or use your own surl and furl after testing is completed.