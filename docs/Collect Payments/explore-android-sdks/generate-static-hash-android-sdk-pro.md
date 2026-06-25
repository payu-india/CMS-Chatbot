---
title: Generate Static Hash
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
The static hashes can be passed to SDK during integration and do not change. Unlike dynamic hashing, it is static.

The following table describes all static hashes:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Hash Name
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>

      <th style={{ textAlign: "left" }}>
        Hash Formula
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `payment_related_`<br/>`details_for_`<br/>`mobile_sdk`
      </td>

      <td style={{ textAlign: "left" }}>
        Used to fetch enabled payment options. If not passed, checkout screen will not appear.
      </td>

      <td style={{ textAlign: "left" }}>
        `<key>`<br/>`|payment_related_details_for_mobile_sdk|`<br/>`<userCredential>|`<br/>`<salt>`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `eligibleBins`<br/>`ForEMI`
      </td>

      <td style={{ textAlign: "left" }}>
        Used to fetch the eligible bins for EMI when EMI is enabled. If not passed, EMI payment will not work.
      </td>

      <td style={{ textAlign: "left" }}>
        `<key>|`<br/>`eligibleBinsForEMI|`<br/>`default|`<br/>`<salt>`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `getEmi`<br/>`AmountAccording`<br/>`ToInterest`
      </td>

      <td style={{ textAlign: "left" }}>
        Used to fetch EMI details like amount, interest rate, etc. If not passed, EMI payment will not work.
      </td>

      <td style={{ textAlign: "left" }}>
        `<key>|`<br/>`vas_for_mobile_sdk|`<br/>`<amount>|`<br/>`<salt>`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `Payment`
      </td>

      <td style={{ textAlign: "left" }}>
        Used for making payment. If not passed, payment will not happen.
      </td>

      <td style={{ textAlign: "left" }}>
        `<key>|`<br/>`txnid|`<br/>`amount|`<br/>`productinfo|`<br/>`firstname|`<br/>`email|`<br/>`udf1|`<br/>`udf2|`<br/>`udf3|udf4|udf5||||||`<br/>`salt`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `delete_payment_`<br/>`instrument`
      </td>

      <td style={{ textAlign: "left" }}>
        Used to delete the tokenised card
      </td>

      <td style={{ textAlign: "left" }}>
        `<key>|`<br/>`delete_payment_instrument`<br/>`|<userCredential>|`<br/>`<salt>`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `get_payment_`<br/>`instrument`
      </td>

      <td style={{ textAlign: "left" }}>
        Used to get all stored tokenised cards
      </td>

      <td style={{ textAlign: "left" }}>
        `<key>|`<br/>`get_payment_`<br/>`instrument|`<br/>`<userCredential>|`<br/>`<salt>`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `get_payment_`<br/>`details`
      </td>

      <td style={{ textAlign: "left" }}>
        Used to get the payment details of an existing card stored on PayU Vault
      </td>

      <td style={{ textAlign: "left" }}>
        `<key>\|`<br/>`get_payment_`<br/>`details\|`<br/>`<userCredential>\|`<br/>`<salt>`
      </td>
    </tr>
  </tbody>
</Table>

After setting the values in the above formula, generate `sha512` over it and pass the same in additional parameters

### Payment Hash

For the Hash required to make payment as described in the above table:

```plaintext
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
```

The following sample code can be used to integrate:

```java
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>



 <%@ page import="java.security.MessageDigest" %>
<%@ page import="java.security.NoSuchAlgorithmException" %> 
 <%@ page import="org.json.simple.JSONObject" %>

<%
//fetch all required params
String txnid=request.getParameter("txnid");
String amount=request.getParameter("amount");
String email=request.getParameter("email");
String productinfo=request.getParameter("productinfo");
String firstname=request.getParameter("firstname");
String udf1=request.getParameter("udf1");
String udf2=request.getParameter("udf2");
String udf3=request.getParameter("udf3");
String udf4=request.getParameter("udf4");
String udf5=request.getParameter("udf5");
String user_credentials=request.getParameter("user_credentials");

response.getWriter().print(getHashes(txnid, amount, productinfo, firstname, email, user_credentials, udf1, udf2, udf3, udf4, udf5));

%>

<%!
              //PUT YOUR LIVE CREDENTIALS HERE          

private final String key = "gtKFFx";      //put your merchant key value 
private final String salt = "eCwWELxi";   //put your merchant salt value 

private final String PAYMENT_HASH = "payment_hash";
private final String GET_MERCHANT_IBIBO_CODES_HASH = "get_merchant_ibibo_codes_hash";
private final String VAS_FOR_MOBILE_SDK_HASH = "vas_for_mobile_sdk_hash";
private final String PAYMENT_RELATED_DETAILS_FOR_MOBILE_SDK_HASH = "payment_related_details_for_mobile_sdk_hash";
private final String DELETE_USER_CARD_HASH = "delete_user_card_hash";
private final String GET_USER_CARDS_HASH = "get_user_cards_hash";
private final String EDIT_USER_CARD_HASH = "edit_user_card_hash";
private final String SAVE_USER_CARD_HASH = "save_user_card_hash";
private final String CHECK_OFFER_STATUS_HASH = "check_offer_status_hash";
private final String CHECK_ISDOMESTIC_HASH = "check_isDomestic_hash";
private final String VERIFY_PAYMENT_HASH = "verify_payment_hash";
/**
* This function generates a JSON String of required mandatory hashes.
*/
public String getHashes(String txnid, String amount, String productInfo, String firstname, String email,
		String user_credentials, String udf1, String udf2, String udf3, String udf4, String udf5 
		) { 
	JSONObject response = new JSONObject();

	String ph = checkNull(key) + "|" + checkNull(txnid) + "|" + checkNull(amount) + "|" + checkNull(productInfo)
			+ "|" + checkNull(firstname) + "|" + checkNull(email) + "|" + checkNull(udf1) + "|" + checkNull(udf2)
			+ "|" + checkNull(udf3) + "|" + checkNull(udf4) + "|" + checkNull(udf5) + "||||||" + salt;
	String paymentHash = getSHA(ph);
	System.out.println("Payment Hash "+paymentHash);
	response.put(PAYMENT_HASH, paymentHash);
	response.put(VAS_FOR_MOBILE_SDK_HASH, generateHashString("vas_for_mobile_sdk", "default"));
			
	//Use var1 as user_credentials if user_credential is not empty
	if (!checkNull(user_credentials).isEmpty()) {
	
		response.put(PAYMENT_RELATED_DETAILS_FOR_MOBILE_SDK_HASH,
				generateHashString("payment_related_details_for_mobile_sdk", user_credentials));
		
		response.put(DELETE_USER_CARD_HASH, generateHashString("delete_user_card", user_credentials));
		response.put(GET_USER_CARDS_HASH, generateHashString("get_user_cards", user_credentials));
		response.put(EDIT_USER_CARD_HASH, generateHashString("edit_user_card", user_credentials));
		response.put(SAVE_USER_CARD_HASH, generateHashString("save_user_card", user_credentials));
	}
	else{
		response.put(PAYMENT_RELATED_DETAILS_FOR_MOBILE_SDK_HASH, 
				generateHashString("payment_related_details_for_mobile_sdk","default")); 
		
	}
	System.out.println("Vas_for _mobile_sdk  "+generateHashString("vas_for_mobile_sdk", "default"));
	System.out.println("payment_related_details_sdk_hash  "+ generateHashString("payment_related_details_for_mobile_sdk", user_credentials));
	
	System.out.println("delete_user_card Hash"+generateHashString("delete_user_card", user_credentials));
	
	
	return response.toJSONString(); 

}

// This method generates hash string 

private String generateHashString(String command, String var1) {
	return getSHA(key + "|" + command + "|" + var1 + "|" + salt);
}

private String checkNull(String value) {
	if (value == null) {
		return "";
	} else {
		return value;
	}
}

private String getSHA(String str) {

	 MessageDigest md;
	String out = "";
	try {
		md = MessageDigest.getInstance("SHA-512");
		md.update(str.getBytes());
		byte[] mb = md.digest();

		for (int i = 0; i < mb.length; i++) {
			byte temp = mb[i];
			String s = Integer.toHexString(new Byte(temp));
			while (s.length() < 2) {
				s = "0" + s;
			}
			s = s.substring(s.length() - 2);
			out += s;
		}

	} catch (NoSuchAlgorithmException e) {
		e.printStackTrace();
	}
	return out; 

}


%>

</body>
</html>

```

```php
<?php

function getHashes($txnid, $amount, $productinfo, $firstname, $email, $user_credentials, $udf1, $udf2, $udf3, $udf4, $udf5,$offerKey,$cardBin)
{
      // $firstname, $email can be "", i.e empty string if needed. Same should be sent to PayU server (in request params) also.
      $key = 'XXXXXX';
      $salt = 'YYYYY';

      $payhash_str = $key . '|' . checkNull($txnid) . '|' .checkNull($amount)  . '|' .checkNull($productinfo)  . '|' . checkNull($firstname) . '|' . checkNull($email) . '|' . checkNull($udf1) . '|' . checkNull($udf2) . '|' . checkNull($udf3) . '|' . checkNull($udf4) . '|' . checkNull($udf5) . '||||||' . $salt;
      $paymentHash = strtolower(hash('sha512', $payhash_str));
      $arr['payment_hash'] = $paymentHash;

      $cmnNameMerchantCodes = 'get_merchant_ibibo_codes';
      $merchantCodesHash_str = $key . '|' . $cmnNameMerchantCodes . '|default|' . $salt ;
      $merchantCodesHash = strtolower(hash('sha512', $merchantCodesHash_str));
      $arr['get_merchant_ibibo_codes_hash'] = $merchantCodesHash;

      $cmnMobileSdk = 'vas_for_mobile_sdk';
      $mobileSdk_str = $key . '|' . $cmnMobileSdk . '|default|' . $salt;
      $mobileSdk = strtolower(hash('sha512', $mobileSdk_str));
      $arr['vas_for_mobile_sdk_hash'] = $mobileSdk;

// added code for EMI hash
      $cmnEmiAmountAccordingToInterest= 'getEmiAmountAccordingToInterest';
      $emi_str = $key . '|' . $cmnEmiAmountAccordingToInterest . '|'.checkNull($amount).'|' . $salt;
      $mobileEmiString = strtolower(hash('sha512', $emi_str));
     $arr['emi_hash'] = $mobileEmiString;


      $cmnPaymentRelatedDetailsForMobileSdk1 = 'payment_related_details_for_mobile_sdk';
      $detailsForMobileSdk_str1 = $key  . '|' . $cmnPaymentRelatedDetailsForMobileSdk1 . '|default|' . $salt ;
      $detailsForMobileSdk1 = strtolower(hash('sha512', $detailsForMobileSdk_str1));
      $arr['payment_related_details_for_mobile_sdk_hash'] = $detailsForMobileSdk1;

      //used for verifying payment(optional)
      $cmnVerifyPayment = 'verify_payment';
      $verifyPayment_str = $key . '|' . $cmnVerifyPayment . '|'.$txnid .'|' . $salt;
      $verifyPayment = strtolower(hash('sha512', $verifyPayment_str));
      $arr['verify_payment_hash'] = $verifyPayment;

      if($user_credentials != NULL && $user_credentials != '')
      {
            $cmnNameDeleteCard = 'delete_user_card';
            $deleteHash_str = $key  . '|' . $cmnNameDeleteCard . '|' . $user_credentials . '|' . $salt ;
            $deleteHash = strtolower(hash('sha512', $deleteHash_str));
            $arr['delete_user_card_hash'] = $deleteHash;

            $cmnNameGetUserCard = 'get_user_cards';
            $getUserCardHash_str = $key  . '|' . $cmnNameGetUserCard . '|' . $user_credentials . '|' . $salt ;
            $getUserCardHash = strtolower(hash('sha512', $getUserCardHash_str));
            $arr['get_user_cards_hash'] = $getUserCardHash;

            $cmnNameEditUserCard = 'edit_user_card';
            $editUserCardHash_str = $key  . '|' . $cmnNameEditUserCard . '|' . $user_credentials . '|' . $salt ;
            $editUserCardHash = strtolower(hash('sha512', $editUserCardHash_str));
            $arr['edit_user_card_hash'] = $editUserCardHash;

            $cmnNameSaveUserCard = 'save_user_card';
            $saveUserCardHash_str = $key  . '|' . $cmnNameSaveUserCard . '|' . $user_credentials . '|' . $salt ;
            $saveUserCardHash = strtolower(hash('sha512', $saveUserCardHash_str));
            $arr['save_user_card_hash'] = $saveUserCardHash;

            $cmnPaymentRelatedDetailsForMobileSdk = 'payment_related_details_for_mobile_sdk';
            $detailsForMobileSdk_str = $key  . '|' . $cmnPaymentRelatedDetailsForMobileSdk . '|' . $user_credentials . '|' . $salt ;
            $detailsForMobileSdk = strtolower(hash('sha512', $detailsForMobileSdk_str));
            $arr['payment_related_details_for_mobile_sdk_hash'] = $detailsForMobileSdk;
      }


      // if($udf3!=NULL && !empty($udf3)){
            $cmnSend_Sms='send_sms';
            $sendsms_str=$key . '|' . $cmnSend_Sms . '|' . $udf3 . '|' . $salt;
            $send_sms = strtolower(hash('sha512',$sendsms_str));
            $arr['send_sms_hash']=$send_sms;
      // }


      if ($offerKey!=NULL && !empty($offerKey)) {
                  $cmnCheckOfferStatus = 'check_offer_status';
                        $checkOfferStatus_str = $key  . '|' . $cmnCheckOfferStatus . '|' . $offerKey . '|' . $salt ;
                  $checkOfferStatus = strtolower(hash('sha512', $checkOfferStatus_str));
                  $arr['check_offer_status_hash']=$checkOfferStatus;
            }


            if ($cardBin!=NULL && !empty($cardBin)) {
                  $cmnCheckIsDomestic = 'check_isDomestic';
                        $checkIsDomestic_str = $key  . '|' . $cmnCheckIsDomestic . '|' . $cardBin . '|' . $salt ;
                  $checkIsDomestic = strtolower(hash('sha512', $checkIsDomestic_str));
                  $arr['check_isDomestic_hash']=$checkIsDomestic;
            }



    return $arr;
}

function checkNull($value) {
            if ($value == null) {
                  return '';
            } else {
                  return $value;
            }
      }

$output=getHashes($_POST["txnid"], $_POST["amount"], $_POST["productinfo"], $_POST["firstname"], $_POST["email"], $_POST["user_credentials"], $_POST["udf1"], $_POST["udf2"], $_POST["udf3"], $_POST["udf4"], $_POST["udf5"],$_POST["offerKey"],$_POST["cardBin"]);

echo json_encode($output);

?>


```

## For SI Payment

Payment hash is calculated with the following formula for SI transaction:

`SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|SALT)`

**Example**

```
SHA512(<Your Test Env. Key>|fa3359f205d621c07383|2|Product Info|Payu-Admin|test@example.com|||||||||||{"billingAmount": "150.00","billingCurrency": "INR","billingCycle": "WEEKLY","billingInterval": 1,"paymentStartDate": "2019-09-18","paymentEndDate": "2020-10-20"}|dEvD9ABD)

```

**Free Trial Transaction**

For free trial transactions, free trial value should be used in hash calculation as follows:

`SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|si_details|free_trial|SALT)`

**Example**

```
SHA512(<Your Test Env. Key>|fa3359f205d621c07383|2|Product Info|Payu-Admin|test@example.com|||||||||||{"billingAmount": "150.00","billingCurrency": "INR","billingCycle": "WEEKLY","billingInterval": 1,"paymentStartDate": "2019-09-18","paymentEndDate": "2020-10-20"}|1|<Please_add_salt_here>)  
```

## For Split Payment

Payment hash is calculated with the following formula for Split transaction:

`sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT|splitRequest)`

Where, splitRequest will be at the end of the hash pattern string.

**Example**

```
SHA512(<Your Key>|payment-txnid-1|10|Product Info|Payu-Admin|test@example.com|||||||||||<Your Salt>|{"type":"absolute","splitInfo":{"P41sCY":{"aggregatorSubTxnId":"0e7411799c9f0e96620c11","aggregatorSubAmt":"3","aggregatorCharges":"2"},"P41sCK":{"aggregatorSubTxnId":"0e7411799c9f0e96620c22","aggregatorSubAmt":"5"}}}

```