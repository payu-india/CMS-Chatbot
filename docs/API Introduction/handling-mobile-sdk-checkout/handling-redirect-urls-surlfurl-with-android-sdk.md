---
title: Handling Redirect URLs (surl/furl) with Android SDK
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
Redirect URLs are where PayU redirects the user after the transaction is completed. PayU sends the data related to transactions while redirecting so that you can check the status of the transaction. The `surl` and `furl` refer to the success and failure URLs (page) respectively. These URLs are used to return the customer back to your website after a successful or failed transaction.\
The `surl` or `furl` page is hosted on your server to communicate back to the client application when the transaction is completed. You may check the status of the transaction and take action accordingly. In mobile applications, it is important that your customer return back to app whenever a transaction is completed. After the transaction is complete, PayU posts the response to the surl / furl.

> 🚧 Keep in mind
>
> Surl(success url), Furl(failure url) are two urls (https POST) should be given by merchant as post param while making payment. As soon as the transaction completes payu post the data back to surl/furl depends on the transaction status.
>
> SURL/FURL must implement a javascript interface function named
>
> `PayU.onSuccess(“data”) or PayU.onFailure(“data”);`

## Success URL

You can use the PayU Checkout Pro SDK to handle **surl** callbacks similar to the following sample code:

```php
<?php 
error_reporting(0); 
$salt ="<SALT Value>"; # pass your salt value in this variable
$amount = $_POST["amount"]; # amount need to be picked up from your database 

$reverseHash = generateReverseHash(); 

if ($_POST["hash"] == $reverseHash) 
{ 
  # transaction is successful 
  # do the required javascript task 
  echo("Transaction Success & Verified"); 
  AndroidSuccess($_POST["amount"]); 
} 
else
{ 
  # transaction is tampered 
  # handle it as required 
  echo("<br>"); 
  echo "\nInvalid transaction"; 
} 

# For Android Success 
function AndroidSuccess($input) 
{ 
  echo '<script type="text/javascript">'; 
  echo 'PayU.onSuccess("Amount =" +'.$_POST["amount"].')'; 
  echo "</script>"; 
} 

# Function to generate a reverse hash 
function generateReverseHash() 
{ 
  global $salt; 
  global $amount; 

  if ($_POST["additional_charges"] != null) 
  { 
    $reversehash_string = $_POST["additional_charges"] . "|" . $salt . 
    "|" . $_POST["status"] . "||||||" . $_POST["udf5"] . "|" . $_POST["udf4"] . "|" . $_POST["udf3"] . "|" . $_POST["udf2"] . "|" . $_POST["udf1"] . "|" . $_POST["email"] . "|" . $_POST["firstname"] . "|" . $_POST["productinfo"] . "|" . $amount . "|" . $_POST["txnid"] . "|" . $_POST["key"] ; 
  } 
  else
  { 
    $reversehash_string = $salt . "|" . $_POST["status"] . "||||||" . $_POST["udf5"] . "|" . $_POST["udf4"] . "|" . $_POST["udf3"] . "|" . $_POST["udf2"] . "|" . $_POST["udf1"] . "|" . $_POST["email"] . "|" . $_POST["firstname"] . "|" . $_POST["productinfo"] . "|" . $amount . "|" . $_POST["txnid"] . "|" . $_POST["key"] ; 
  } 

  // echo($reversehash_string); 

  $reverseHash = strtolower(hash("sha512", $reversehash_string)); 
  return $reverseHash; 
} 
?>
```
```java

 CALCULATED_REVERSE_HASH=  getReverseHash(key,txnid,amount,productinfo,firstname,email,udf1,udf2,udf3,udf4,udf5,status);
 
 System.out.println("key is "+key+" txn id is "+txnid+" amount is "+amount+" productinfo is "+productinfo+" firstName is "+firstname+ " email is "+email+ " udf1 "+udf1+" udf2 "+udf2+" udf3 "+udf3+ " udf4 "+udf4+ " udf5 "+udf5);
	
 System.out.println("calcu ret hash"+CALCULATED_REVERSE_HASH);
 System.out.println("Received reverse hash : "+received_Reverse_Hash);
 
 if(CALCULATED_REVERSE_HASH.equals(received_Reverse_Hash)){
	 
	 System.out.println("Hash Successfully Matched ");
	 response.getWriter().print("Please Wait");
	 
	 
	/*   Enumeration<String> parameterList = request.getParameterNames();
	  while( parameterList.hasMoreElements() )
	  {
	    String sName = parameterList.nextElement().toString();
	    
	      out_Params.put(sName.toString(), request.getParameter( sName ).toString());
	      
	      
	    }
	  
	  response.getWriter().print(out_Params.toJSONString());
	  
	  System.out.println(out_Params.toJSONString());
	  
	  android_Data=out_Params;
	  System.out.println(android_Data.toString());
	  
	  setResponseData(android_Data); // Setting data as */
	  
	  
	  Enumeration<String> kayParams = request.getParameterNames();
		String result = "";
		
		while (kayParams.hasMoreElements()) {
			key = (String) kayParams.nextElement();
			result += key + "=" + request.getParameter(key) + (kayParams.hasMoreElements() ? "," : "");
		}
		
		setResponseData(result);  // setting result as String 
 }
 
 
 
 else{
	 
	 response.getWriter().print("Invalid Transaction");
	 
	setResponseData("Invalid Transaction");
	 
 }
 
 
 %>
 
 
 <%!    // Decleration Tag
 
 
 private final String salt="";  // Pass your salt in this variable
 private JSONObject out_Params = new JSONObject();
 private  String CALCULATED_REVERSE_HASH="reverse_hash";
 public String android_Data="";
 public String test_data2="test2";
 
 
 public String getReverseHash(String key,String txnid, String amount, String productinfo,String firstname,String email,String udf1,String udf2,String udf3,String udf4,String udf5, String status){
	 
	 System.out.println("udf1 "+udf1);
	 System.out.println("udf1 "+udf2);
	 System.out.println("udf1 "+udf3);
	 System.out.println("udf1 "+udf4);
	 System.out.println("udf1 "+checkNull(udf5));
	 
	 String r_h= checkNull(salt)+"|"+checkNull(status)+"||||||"+checkNull(udf5)+"|"+checkNull(udf4)+"|"+checkNull(udf3)+"|"+checkNull(udf2)+"|"+checkNull(udf1)+"|"+checkNull(email)+"|"+checkNull(firstname)+"|"+checkNull(productinfo)+"|"+checkNull(amount)+"|"+checkNull(txnid)+"|"+checkNull(key);
	 
	 System.out.println("r_h   "+r_h);
	 
	 String calculated_reverse_hash=getSHA(r_h);
	 
	 System.out.println("calculated return hash   "+calculated_reverse_hash);
	 
	 
	 
	 return calculated_reverse_hash; // return generated reverse hash
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
 
 public void setResponseData(String data){
	 android_Data=data;
	 System.out.println("android data "+android_Data);
 }
 
 
 
 %>


<script type="text/javascript">
	
	//for Android Success
	function AndroidSuccess(input) {
		//alert(input);
		PayU.onSuccess(input);
	}
	
	AndroidSuccess("<%= android_Data %>");
	
</script>


</body>
</html>
```

## Faliure URL

You can use the PayU Checkout Pro SDK to handle **furl** callbacks similar to the following sample code:

```Text PHP
<?php 
error_reporting(0); 
$salt = "<SALT Value>"; # pass your salt in this variable
$amount = $_POST["amount"]; # amount need to be picked up from your database 

$reverseHash = generateReverseHash(); 

if ($_POST["hash"] == $reverseHash) 
{ 
  # transaction is successful 
  # do the required javascript task 
  echo("Transaction Success & Verified"); 
  AndroidSuccess($_POST["amount"]); 
} 
else
{ 
  # transaction is tampered 
  # handle it as required 
  echo("<br>"); 
  echo "\nInvalid transaction"; 
} 

# For Android Success 
function AndroidSuccess($input) 
{ 
  echo '<script type="text/javascript">'; 
  echo 'PayU.onFaliure("Amount =" +'.$_POST["amount"].')'; 
  echo "</script>"; 
} 

# Function to generate a reverse hash 
function generateReverseHash() 
{ 
  global $salt; 
  global $amount; 

  if ($_POST["additional_charges"] != null) 
  { 
    $reversehash_string = $_POST["additional_charges"] . "|" . $salt . 
    "|" . $_POST["status"] . "||||||" . $_POST["udf5"] . "|" . $_POST["udf4"] . "|" . $_POST["udf3"] . "|" . $_POST["udf2"] . "|" . $_POST["udf1"] . "|" . $_POST["email"] . "|" . $_POST["firstname"] . "|" . $_POST["productinfo"] . "|" . $amount . "|" . $_POST["txnid"] . "|" . $_POST["key"] ; 
  } 
  else
  { 
    $reversehash_string = $salt . "|" . $_POST["status"] . "||||||" . $_POST["udf5"] . "|" . $_POST["udf4"] . "|" . $_POST["udf3"] . "|" . $_POST["udf2"] . "|" . $_POST["udf1"] . "|" . $_POST["email"] . "|" . $_POST["firstname"] . "|" . $_POST["productinfo"] . "|" . $amount . "|" . $_POST["txnid"] . "|" . $_POST["key"] ; 
  } 

  // echo($reversehash_string); 

  $reverseHash = strtolower(hash("sha512", $reversehash_string)); 
  return $reverseHash; 
} 
?>
```
```Text JAVA

 CALCULATED_REVERSE_HASH=  getReverseHash(key,txnid,amount,productinfo,firstname,email,udf1,udf2,udf3,udf4,udf5,status);
 
 System.out.println("key is "+key+" txn id is "+txnid+" amount is "+amount+" productinfo is "+productinfo+" firstName is "+firstname+ " email is "+email+ " udf1 "+udf1+" udf2 "+udf2+" udf3 "+udf3+ " udf4 "+udf4+ " udf5 "+udf5);
	
 System.out.println("calcu ret hash"+CALCULATED_REVERSE_HASH);
 System.out.println("Received reverse hash : "+received_Reverse_Hash);
 
 if(CALCULATED_REVERSE_HASH.equals(received_Reverse_Hash)){
	 
	 System.out.println("Hash Successfully Matched ");
	 response.getWriter().print("Please Wait");
	 
	 
	/*   Enumeration<String> parameterList = request.getParameterNames();
	  while( parameterList.hasMoreElements() )
	  {
	    String sName = parameterList.nextElement().toString();
	    
	      out_Params.put(sName.toString(), request.getParameter( sName ).toString());
	      
	      
	    }
	  
	  response.getWriter().print(out_Params.toJSONString());
	  
	  System.out.println(out_Params.toJSONString());
	  
	  android_Data=out_Params;
	  System.out.println(android_Data.toString());
	  
	  setResponseData(android_Data); // Setting data as */
	  
	  
	  Enumeration<String> kayParams = request.getParameterNames();
		String result = "";
		
		while (kayParams.hasMoreElements()) {
			key = (String) kayParams.nextElement();
			result += key + "=" + request.getParameter(key) + (kayParams.hasMoreElements() ? "," : "");
		}
		
		setResponseData(result);  // setting result as String 
 }
 
 
 
 else{
	 
	 response.getWriter().print("Invalid Transaction");
	 
	setResponseData("Invalid Transaction");
	 
 }
 
 
 %>
 
 
 <%!    // Decleration Tag
 
 
 private final String salt="";  // Pass your salt in this variable
 private JSONObject out_Params = new JSONObject();
 private  String CALCULATED_REVERSE_HASH="reverse_hash";
 public String android_Data="";
 public String test_data2="test2";
 
 
 public String getReverseHash(String key,String txnid, String amount, String productinfo,String firstname,String email,String udf1,String udf2,String udf3,String udf4,String udf5, String status){
	 
	 System.out.println("udf1 "+udf1);
	 System.out.println("udf1 "+udf2);
	 System.out.println("udf1 "+udf3);
	 System.out.println("udf1 "+udf4);
	 System.out.println("udf1 "+checkNull(udf5));
	 
	 String r_h= checkNull(salt)+"|"+checkNull(status)+"||||||"+checkNull(udf5)+"|"+checkNull(udf4)+"|"+checkNull(udf3)+"|"+checkNull(udf2)+"|"+checkNull(udf1)+"|"+checkNull(email)+"|"+checkNull(firstname)+"|"+checkNull(productinfo)+"|"+checkNull(amount)+"|"+checkNull(txnid)+"|"+checkNull(key);
	 
	 System.out.println("r_h   "+r_h);
	 
	 String calculated_reverse_hash=getSHA(r_h);
	 
	 System.out.println("calculated return hash   "+calculated_reverse_hash);
	 
	 
	 
	 return calculated_reverse_hash; // return generated reverse hash
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
 
 public void setResponseData(String data){
	 android_Data=data;
	 System.out.println("android data "+android_Data);
 }
 
 
 
 %>


<script type="text/javascript">
	
	//for Android Success
	function AndroidSuccess(input) {
		//alert(input);
		PayU.onFailure(input);
	}
	
	AndroidFailure("<%= android_Data %>");
	
</script>


</body>
</html>
```

In the above code, you need to replace the placeholders with your actual values. The default values for `surl` and `furl` are:

* **surl**: [https://cbjs.payu.in/sdk/success](https://cbjs.payu.in/sdk/success)
* **furl**: [https://cbjs.payu.in/sdk/failure](https://cbjs.payu.in/sdk/failure)

> 📘 Note:
>
> These URLs are for temporary use. PayU recommends you to design or use your own surl and furl after testing is completed.
