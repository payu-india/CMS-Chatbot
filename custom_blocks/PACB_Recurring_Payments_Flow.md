---
name: PACB_Recurring_Payments_Flow
---
## Recurring Payments Flow

### Workflow

<Image align="center" src="https://files.readme.io/ffac22445b558dd93d085536bb1065ab818e716c50e6839ce4569427dde92275-UPI_Autopay_-_Recurring_Payment_flow.png" />

### Step 1: Pre-Debit SI Notification

Use the **Pre-Debit SI** API to send pre-debit notifications for upcoming recurring debits with parallel sequencing support. This notification mandator for Cards and UPI recurring only and not required for ENACH recurring.

| Environment | URL                                                    |
| :---------- | :----------------------------------------------------- |
| Test        | `https://test.payu.in/merchant/postservice.php?form=2` |
| Production  | `https://info.payu.in/merchant/postservice.php?form=2` |

<Accordion title="Request Parameters" icon="fa-info-circle">
  | Parameter                             | Description                                                                                                                                                   | Example               |
  | :------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------- |
  | key <br /> <code>mandatory</code>     | <code>String</code> Your merchant key provided by PayU.                                                                                                       | JP\*\*\*g             |
  | command <br /> <code>mandatory</code> | <code>String</code> The API command name.                                                                                                                     | pre\_debit\_SI        |
  | hash <br /> <code>mandatory</code>    | <code>String</code> The hash value generated using the hash logic.                                                                                            | abc0ada2e12           |
  | var1 <br /> <code>mandatory</code>    | <code>JSON String</code> JSON object containing the pre-debit details. For more information refer to [var1 Object Parameters](#var1-object-parameters) table. | See var1 Object below |

  ##### Hash logic

  The hash is generated using the following formula:

  ```
  hash = sha512(key|command|var1|salt)
  ```

  ### var1 Object Parameters

  <Table align={["left","left","left"]}>
    <thead>
      <tr>
        <th>
          Parameter
        </th>

        <th>
          Description
        </th>

        <th>
          Example
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          authpayuid <br /> <code>mandatory</code>
        </td>

        <td>
          <code>String</code> The mihpayid received during the successful consent transaction.
        </td>

        <td>
          999000000000826
        </td>
      </tr>

      <tr>
        <td>
          requestid <br /> <code>mandatory</code>
        </td>

        <td>
          <code>String</code> Unique request ID for tracking the pre-debit request.
        </td>

        <td>
          RCS0123459PD
        </td>
      </tr>

      <tr>
        <td>
          debitdate <br /> <code>mandatory</code>
        </td>

        <td>
          <code>String</code> The date when the debit will occur in YYYY-MM-DD format.
        </td>

        <td>
          2024-11-22
        </td>
      </tr>

      <tr>
        <td>
          amount <br /> <code>mandatory</code>
        </td>

        <td>
          <code>String</code> The amount to be debited.
        </td>

        <td>
          125
        </td>
      </tr>

      <tr>
        <td>
          invoiceDisplayNumber <br /> <code>mandatory for cards</code>
        </td>

        <td>
          <code>String</code> Invoice number to display to the customer.
        </td>

        <td>
          12345678910
        </td>
      </tr>

      <tr>
        <td>
          action
          <code>optional</code>
        </td>

        <td>
          Pass "Retrieve" or "Delete" according to the action need to be performed. For more information, refer to Additional Information table..
        </td>

        <td>
          Retrieve
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
  ```bash
  curl --location 'https://test.info.payu.in/merchant/postservice.php?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'command=pre_debit_SI' \
  --data-urlencode 'var1={"authpayuid":"999000000000826","requestid":"RCS0123459PD","debitdate":"2024-11-22","amount":"125","invoiceDisplayNumber":"12345678910"}' \
  --data-urlencode 'key=JP***g' \
  --data-urlencode 'hash=abc0ada2e12'
  ```
  ```python
  import requests

  url = "https://test.info.payu.in/merchant/postservice.php?form=2"

  payload = {
      "command": "pre_debit_SI",
      "var1": '{"authpayuid":"999000000000826","requestid":"RCS0123459PD","debitdate":"2024-11-22","amount":"125","invoiceDisplayNumber":"12345678910"}',
      "key": "JP***g",
      "hash": "abc0ada2e12"
  }

  headers = {
      "Content-Type": "application/x-www-form-urlencoded"
  }

  response = requests.post(url, data=payload, headers=headers)
  print(response.json())
  ```
  ```csharp
  using System;
  using System.Net.Http;
  using System.Collections.Generic;
  using System.Threading.Tasks;

  class Program
  {
      static async Task Main()
      {
          using var client = new HttpClient();
          
          var content = new FormUrlEncodedContent(new[]
          {
              new KeyValuePair<string, string>("command", "pre_debit_SI"),
              new KeyValuePair<string, string>("var1", "{\"authpayuid\":\"999000000000826\",\"requestid\":\"RCS0123459PD\",\"debitdate\":\"2024-11-22\",\"amount\":\"125\",\"invoiceDisplayNumber\":\"12345678910\"}"),
              new KeyValuePair<string, string>("key", "JP***g"),
              new KeyValuePair<string, string>("hash", "abc0ada2e12")
          });
          
          var response = await client.PostAsync("https://test.info.payu.in/merchant/postservice.php?form=2", content);
          var result = await response.Content.ReadAsStringAsync();
          Console.WriteLine(result);
      }
  }
  ```
  ```javascript
  const sendPreDebitRequest = async () => {
      const url = "https://test.info.payu.in/merchant/postservice.php?form=2";
      
      const params = new URLSearchParams();
      params.append("command", "pre_debit_SI");
      params.append("var1", JSON.stringify({
          authpayuid: "999000000000826",
          requestid: "RCS0123459PD",
          debitdate: "2024-11-22",
          amount: "125",
          invoiceDisplayNumber: "12345678910"
      }));
      params.append("key", "JP***g");
      params.append("hash", "abc0ada2e12");
      
      const response = await fetch(url, {
          method: "POST",
          headers: {
              "Content-Type": "application/x-www-form-urlencoded"
          },
          body: params
      });
      
      const data = await response.json();
      console.log(data);
  };

  sendPreDebitRequest();
  ```
  ```java
  import java.io.*;
  import java.net.*;
  import java.nio.charset.StandardCharsets;

  public class PreDebitSI {
      public static void main(String[] args) throws Exception {
          String url = "https://test.info.payu.in/merchant/postservice.php?form=2";
          
          String params = "command=pre_debit_SI" +
              "&var1=" + URLEncoder.encode("{\"authpayuid\":\"999000000000826\",\"requestid\":\"RCS0123459PD\",\"debitdate\":\"2024-11-22\",\"amount\":\"125\",\"invoiceDisplayNumber\":\"12345678910\"}", StandardCharsets.UTF_8) +
              "&key=JP***g" +
              "&hash=abc0ada2e12";
          
          HttpURLConnection conn = (HttpURLConnection) new URL(url).openConnection();
          conn.setRequestMethod("POST");
          conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
          conn.setDoOutput(true);
          
          try (OutputStream os = conn.getOutputStream()) {
              os.write(params.getBytes(StandardCharsets.UTF_8));
          }
          
          try (BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()))) {
              String line;
              while ((line = br.readLine()) != null) {
                  System.out.println(line);
              }
          }
      }
  }
  ```
  ```php
  <?php
  $url = "https://test.info.payu.in/merchant/postservice.php?form=2";

  $data = array(
      "command" => "pre_debit_SI",
      "var1" => json_encode(array(
          "authpayuid" => "999000000000826",
          "requestid" => "RCS0123459PD",
          "debitdate" => "2024-11-22",
          "amount" => "125",
          "invoiceDisplayNumber" => "12345678910"
      )),
      "key" => "JP***g",
      "hash" => "abc0ada2e12"
  );

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array("Content-Type: application/x-www-form-urlencoded"));

  $response = curl_exec($ch);
  curl_close($ch);

  echo $response;
  ?>
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-reply">
  **Success Response**

  ```json
  {
      "status": "1",
      "action": "MANDATE_PRE_DEBIT",
      "message": "Request Processed Successfully"
  }
  ```

  **Error Responses**

  | Scenario                              | Response                                                                                                                               |
  | :------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------- |
  | Invalid mandateSeqNo                  | `{"status":"0","message":"Invalid value for mandateSeqNo","action":"MANDATE_PRE_DEBIT"}`                                               |
  | Pre-debit already sent for sequence   | `{"status":"E9254","action":"MANDATE_PRE_DEBIT","message":"Predebit notification already sent for the mandate sequence no. 2"}`        |
  | Execution already exists for sequence | `{"status":"E9256","action":"MANDATE_PRE_DEBIT","message":"Execution already sent for the mandate sequence no.:2"}`                    |
  | Debit date exceeds 30 days            | `{"status":"E9260","action":"MANDATE_PRE_DEBIT","message":"Predebit notification can only be sent for a maximum 30 days in advance."}` |
  | Pre-debit sent for past sequence      | `{"status":"E9263","action":"MANDATE_PRE_DEBIT","message":"Predebit for calculated sequence sent during incorrect period"}`            |
</Accordion>

#### Response Parameters

| Parameter | Description                                                                                            | Example                        |
| :-------- | :----------------------------------------------------------------------------------------------------- | :----------------------------- |
| status    | <code>String</code> Status of the request. `1` indicates success, `0` or error code indicates failure. | 1                              |
| action    | <code>String</code> The action performed.                                                              | MANDATE_PRE_DEBIT              |
| message   | <code>String</code> Description of the response status.                                                | Request Processed Successfully |

### Step 2: Recurring Payment Transaction

Use the **Recurring Payment Transaction** API to execute recurring payment transactions for customers who have already completed a successful mandate/registration transaction with Net Banking, UPI, or Cards. For detailed API reference, refer to [Recurring Payment Transaction API - PACB](ref:recurring-payment-transaction-api-pacb).

| Environment | URL                                                |
| :---------- | :------------------------------------------------- |
| Production  | `https://info.payu.in/merchant/postservice?form=2` |
| Test        | `https://test.payu.in/merchant/postservice?form=2` |

<Accordion title="Request Parameters" icon="fa-info-circle">
  | Parameter                             | Description                                                                                  | Example                           |        |         |               |
  | :------------------------------------ | :------------------------------------------------------------------------------------------- | :-------------------------------- | ------ | ------- | ------------- |
  | key <br /> <code>mandatory</code>     | <code>String</code> Merchant Key provided by PayU                                            | JPM7Fg                            |        |         |               |
  | command <br /> <code>mandatory</code> | <code>String</code> API command. Must be `si_transaction`                                    | si\_transaction                   |        |         |               |
  | var1 <br /> <code>mandatory</code>    | <code>JSON Object</code> Transaction details object containing mandatory and optional fields | Refer to var1 Object Fields below |        |         |               |
  | hash <br /> <code>mandatory</code>    | <code>String</code> SHA512 hash: \`sha512(key\\                                              | command\\                         | var1\\ | salt)\` | 9f5faabedb... |

  ### var1 Object Fields

  | Parameter                                                       | Description                                                                                                                                                               | Example                                             |
  | :-------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------- |
  | authpayuid <br /> <code>mandatory</code>                        | <code>String</code> The mihpayid returned in the payment response of the Registration/Consent transaction when transaction is successfully completed.                     | 6611192557                                          |
  | amount <br /> <code>mandatory</code>                            | <code>String</code> The transaction amount which will be deducted from the customer's payment instrument.                                                                 | 10.00                                               |
  | txnid <br /> <code>mandatory</code>                             | <code>String</code> Unique Transaction ID (Order ID) generated by the merchant for this recurring transaction.                                                            | REC15113506209                                      |
  | firstname <br /> <code>mandatory</code>                         | <code>String</code> First name of the buyer/customer.                                                                                                                     | John                                                |
  | lastname <br /> <code>mandatory</code>                          | <code>String</code> Last name of the buyer/customer.                                                                                                                      | Doe                                                 |
  | address1 <br /> <code>optional but recommended for higher approval rate</code>                          | <code>String</code> Address line 1 of the buyer.                                                                                                                          | 123 Main Street                                     |
  | city <br /> <code>optional but recommended for higher approval rate</code>                              | <code>String</code> City of the buyer.                                                                                                                                    | Mumbai                                              |
  | state <br /> <code>optional but recommended for higher approval rate</code>                             | <code>String</code> State of the buyer.                                                                                                                                   | Maharashtra                                         |
  | country <br /> <code>optional but recommended for higher approval rate</code>                           | <code>String</code> Country of the buyer. Allowed values: `IN` or `India` only.                                                                                           | IN                                                  |
  | zipcode <br /> <code>mandatory</code>                           | <code>String</code> ZIP/PIN code of the buyer. Must be a valid 6-digit Indian PIN code.                                                                                   | 400001                                              |
  | phone <br /> <code>optional</code>                              | <code>String</code> The phone number of the customer.                                                                                                                     | 9999999999                                          |
  | email <br /> <code>optional</code>                              | <code>String</code> The email address of the customer.                                                                                                                    | [customer@example.com](mailto:customer@example.com) |
  | invoiceDisplayNumber <br /> <code>mandatory for Cards SI</code> | <code>String</code> A unique display number by merchant for every subsequent invoice/recurring charge. This must be the same value passed during `pre_debit_si` API call. | 12345678910                                         |
  | udf5 <br /> <code>mandatory</code>                              | <code>String</code> Invoice ID for every merchant. This field is mandatory during or after the transaction.                                                               | INV789012                                           |
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
  ```bash
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JPM7Fg&command=si_transaction&var1={
    \"authpayuid\": \"6611192557\",
    \"amount\": \"100.00\",
    \"txnid\": \"REC15113506209\",
    \"phone\": \"9999999999\",
    \"email\": \"customer@example.com\",
    \"firstname\": \"John\",
    \"lastname\": \"Doe\",
    \"address1\": \"123 Main Street\",
    \"city\": \"Mumbai\",
    \"state\": \"Maharashtra\",
    \"country\": \"IN\",
    \"zipcode\": \"400001\",
    \"invoiceDisplayNumber\": \"12345678910\",
    \"udf1\": \"ABCDE1234F\",
    \"udf2\": \"\",
    \"udf3\": \"15-08-1990\",
    \"udf4\": \"\",
    \"udf5\": \"INV789012\"
  }&hash=jbUS07Og8BToVZ..."
  ```
  ```python
  import requests

  url = "https://test.payu.in/merchant/postservice?form=2"

  payload = {
      "key": "JPM7Fg",
      "command": "si_transaction",
      "var1": '{"authpayuid":"6611192557","amount":"100.00","txnid":"REC15113506209","phone":"9999999999","email":"customer@example.com","firstname":"John","lastname":"Doe","address1":"123 Main Street","city":"Mumbai","state":"Maharashtra","country":"IN","zipcode":"400001","invoiceDisplayNumber":"12345678910","udf1":"ABCDE1234F","udf2":"","udf3":"15-08-1990","udf4":"","udf5":"INV789012"}',
      "hash": "jbUS07Og8BToVZ..."
  }

  headers = {
      "accept": "application/json",
      "Content-Type": "application/x-www-form-urlencoded"
  }

  response = requests.post(url, data=payload, headers=headers)
  print(response.json())
  ```
  ```csharp
  using System;
  using System.Net.Http;
  using System.Collections.Generic;
  using System.Threading.Tasks;

  class Program
  {
      static async Task Main()
      {
          using var client = new HttpClient();
          
          var content = new FormUrlEncodedContent(new[]
          {
              new KeyValuePair<string, string>("key", "JPM7Fg"),
              new KeyValuePair<string, string>("command", "si_transaction"),
              new KeyValuePair<string, string>("var1", "{\"authpayuid\":\"6611192557\",\"amount\":\"100.00\",\"txnid\":\"REC15113506209\",\"phone\":\"9999999999\",\"email\":\"customer@example.com\",\"firstname\":\"John\",\"lastname\":\"Doe\",\"address1\":\"123 Main Street\",\"city\":\"Mumbai\",\"state\":\"Maharashtra\",\"country\":\"IN\",\"zipcode\":\"400001\",\"invoiceDisplayNumber\":\"12345678910\",\"udf1\":\"ABCDE1234F\",\"udf2\":\"\",\"udf3\":\"15-08-1990\",\"udf4\":\"\",\"udf5\":\"INV789012\"}"),
              new KeyValuePair<string, string>("hash", "jbUS07Og8BToVZ...")
          });
          
          var response = await client.PostAsync("https://test.payu.in/merchant/postservice?form=2", content);
          var result = await response.Content.ReadAsStringAsync();
          Console.WriteLine(result);
      }
  }
  ```
  ```javascript
  const executeRecurringPayment = async () => {
      const url = "https://test.payu.in/merchant/postservice?form=2";
      
      const params = new URLSearchParams();
      params.append("key", "JPM7Fg");
      params.append("command", "si_transaction");
      params.append("var1", JSON.stringify({
          authpayuid: "6611192557",
          amount: "100.00",
          txnid: "REC15113506209",
          phone: "9999999999",
          email: "customer@example.com",
          firstname: "John",
          lastname: "Doe",
          address1: "123 Main Street",
          city: "Mumbai",
          state: "Maharashtra",
          country: "IN",
          zipcode: "400001",
          invoiceDisplayNumber: "12345678910",
          udf1: "ABCDE1234F",
          udf2: "",
          udf3: "15-08-1990",
          udf4: "",
          udf5: "INV789012"
      }));
      params.append("hash", "jbUS07Og8BToVZ...");
      
      const response = await fetch(url, {
          method: "POST",
          headers: {
              "accept": "application/json",
              "Content-Type": "application/x-www-form-urlencoded"
          },
          body: params
      });
      
      const data = await response.json();
      console.log(data);
  };

  executeRecurringPayment();
  ```
  ```java
  import java.io.*;
  import java.net.*;
  import java.nio.charset.StandardCharsets;

  public class RecurringPaymentTransaction {
      public static void main(String[] args) throws Exception {
          String url = "https://test.payu.in/merchant/postservice?form=2";
          
          String params = "key=JPM7Fg" +
              "&command=si_transaction" +
              "&var1=" + URLEncoder.encode("{\"authpayuid\":\"6611192557\",\"amount\":\"100.00\",\"txnid\":\"REC15113506209\",\"phone\":\"9999999999\",\"email\":\"customer@example.com\",\"firstname\":\"John\",\"lastname\":\"Doe\",\"address1\":\"123 Main Street\",\"city\":\"Mumbai\",\"state\":\"Maharashtra\",\"country\":\"IN\",\"zipcode\":\"400001\",\"invoiceDisplayNumber\":\"12345678910\",\"udf1\":\"ABCDE1234F\",\"udf2\":\"\",\"udf3\":\"15-08-1990\",\"udf4\":\"\",\"udf5\":\"INV789012\"}", StandardCharsets.UTF_8) +
              "&hash=jbUS07Og8BToVZ...";
          
          HttpURLConnection conn = (HttpURLConnection) new URL(url).openConnection();
          conn.setRequestMethod("POST");
          conn.setRequestProperty("accept", "application/json");
          conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
          conn.setDoOutput(true);
          
          try (OutputStream os = conn.getOutputStream()) {
              os.write(params.getBytes(StandardCharsets.UTF_8));
          }
          
          try (BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()))) {
              String line;
              while ((line = br.readLine()) != null) {
                  System.out.println(line);
              }
          }
      }
  }
  ```
  ```php
  <?php
  $url = "https://test.payu.in/merchant/postservice?form=2";

  $data = array(
      "key" => "JPM7Fg",
      "command" => "si_transaction",
      "var1" => json_encode(array(
          "authpayuid" => "6611192557",
          "amount" => "100.00",
          "txnid" => "REC15113506209",
          "phone" => "9999999999",
          "email" => "customer@example.com",
          "firstname" => "John",
          "lastname" => "Doe",
          "address1" => "123 Main Street",
          "city" => "Mumbai",
          "state" => "Maharashtra",
          "country" => "IN",
          "zipcode" => "400001",
          "invoiceDisplayNumber" => "12345678910",
          "udf1" => "ABCDE1234F",
          "udf2" => "",
          "udf3" => "15-08-1990",
          "udf4" => "",
          "udf5" => "INV789012"
      )),
      "hash" => "jbUS07Og8BToVZ..."
  );

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      "accept: application/json",
      "Content-Type: application/x-www-form-urlencoded"
  ));

  $response = curl_exec($ch);
  curl_close($ch);

  echo $response;
  ?>
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-reply">
  **Success Response**

  ```json
  {
    "status": 1,
    "message": "Transaction Processed successfully",
    "details": {
      "REC15113506209": {
        "transactionid": "REC15113506209",
        "amount": "100.00",
        "payuid": "6611427463",
        "status": "captured",
        "field9": "Transaction Completed Successfully",
        "phone": "9999999999",
        "email": "customer@example.com",
        "udf1": "ABCDE1234F",
        "udf2": "",
        "udf3": "15-08-1990",
        "udf4": "",
        "udf5": "INV789012"
      }
    }
  }
  ```

  **Failure Responses**

  | Scenario                    | Response                                                                                                                                                            |
  | :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | Invalid Hash                | `{"status": 0, "msg": "Invalid Hash."}`                                                                                                                             |
  | Basic Authentication Failed | `{"status": 1, "message": "Transaction Processed successfully", "details": {"REC9812123123": {"status": "failed", "field9": "Basic authentication check failed"}}}` |
  | Invalid Country             | `{"status": 0, "message": "Invalid country. Only 'IN' or 'India' is allowed."}`                                                                                     |
  | Missing Mandatory Fields    | `{"status": 0, "message": "Missing mandatory field: firstname/lastname/address1/city/state/country/zipcode"}`                                                       |
</Accordion>

<Callout icon="📘" theme="info">
  **Transaction Status Values**

  | Status      | Description                                                                  |
  | :---------- | :--------------------------------------------------------------------------- |
  | captured    | Transaction successful                                                       |
  | pending     | Payment initiated with bank/NPCI. Final status will be notified via webhook. |
  | failed      | Transaction failed                                                           |
  | in-progress | Transaction is being processed                                               |
</Callout>

### Step 3: Update Invoice ID [Optional]

If the Invoice ID value was unavailable when posting the transaction at [Step 1](#step-1-make-payment-using-web-checkout-integration), it can be updated using the **UDF Update** API by posting it in the UDF5 parameter.

<GENERALAPIsEnvironment />

<Accordion title="Sample request other then UPI AutoPay" icon="fa-code">
  ```
    curl --location --globoff 'https://test.payu.in/merchant/postservice.php?form=2' \
    --form 'key="PRiQvJ"' \
    --form 'command="udf_update"' \
    --form 'var1="my_order_642"' \
    --form 'var2="AAAPZ1234C"' \
    --form 'var4="22/08/1972"' \
    --form 'var5="SellerName"' \
    --form 'var6="INV000000005"' \
    --form 'hash="{{hash}}"'
  ```
</Accordion>

<Accordion title="Sample request for UPI AutoPay" icon="fa-code">
  ```
  curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
  --form 'key="PRiQvJ"' \
  --form 'command="udf_update"' \
  --form 'var1="my_order_642"' \
  --form 'var2="AAAPZ1234C||22-08-1972"' \
  --form 'var4="INV_121312||SellerName"' \
  --form 'hash="{{hash}}"'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  ### Success Scenario

  * If successfully updated for cards

  ```JSON
  {
      "status": "UDF values updated",
      "transaction_id": "my_order_64240",
      "udf1": "AAAPZ1234C",
      "udf2": "",
      "udf3": "22/08/1972",
      "udf4": "SellerName",
      "udf5": "INV000000005"
  }
  ```

  * If successfully updated for UPI autopay:

  ```JSON
  {
    "status": "UDF values updated",
    "transaction_id": "my_order_64240",
    "udf1": "AAAPZ1234C||22-08-1972",
    "udf2": "",
    "udf3": "INV_121312||SellerName"
  }
  ```

  ### Failure Scenarios

  * If the transaction ID is empty

  ```JSON
  ( 
  [status] => 0 
  [msg] => Parameter missing 
  ) 
  ```

  * If the transaction ID is invalid

  ```JSON
  ( 
  [status] => 0 
  [msg] => Invalid TXN ID 
  ) 
  ```

  * If Hash is invalid:

  ```JSON
  {
      "status": 0,
      "msg": "Invalid Hash."
  }
  ```

  * If the merchant is not enabled for UDF updates:

  ```JSON
  {
    "status": "0",
    "msg": "Update not allowed on provided Field"
  }
  ```

  * If no data found in the transaction ID:

  ```JSON
  {
    "status": "0",
    "msg": "No Data Found for txnid: 3424"
  }
  ```

  * If the merchant is inactive:

  ```JSON
  {
    "msg": "Merchant is not authorized to use PayU API",
    "status": 0
  }
  ```
</Accordion>
