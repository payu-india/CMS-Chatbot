---
title: Integrate Parallel Sequencing for UPI AutoPay
deprecated: false
hidden: true
metadata:
  title: Integrate Parallel Sequencing for UPI Autopay
  robots: index
---
This section explains how to integrate parallel sequencing for UPI AutoPay transactions. Parallel sequencing allows you to run pre-debits and executions simultaneously for different sequence numbers.

<Callout icon="📘" theme="info">
  **Enable Parallel Sequencing**: To enable the Parallel Sequencing for UPI Autopay, contact your PayU Account Manager (KAM).
</Callout>

<Cards columns={2}>
  <Card title="1. Send Pre-Debit Notification" href="#step-1-send-pre-debit-notification">
    Send a pre-debit notification to the customer for an upcoming debit with a specific sequence number.

    <br />
  </Card>

  <Card title="2. Post the SI Transaction Request" href="#step-2-post-the-transaction-request">
    Execute the recurring transaction using the si\_transaction API with the corresponding sequence number.

    <br />
  </Card>
</Cards>

***

## Step 1: Send Pre-Debit Notification

Use the **Pre-Debit Notification** API to send pre-debit notifications for upcoming debits. The `mandateSeqNo` parameter enables parallel processing of multiple sequences. For more information on Pre-Debit Notification API, refer to  [Pre-Debit SI API](ref:pre-debit-si-apii).

| Environment | URL                                                         |
| ----------- | ----------------------------------------------------------- |
| Test        | `https://test.info.payu.in/merchant/postservice.php?form=2` |
| Production  | `https://info.payu.in/merchant/postservice.php?form=2`      |

<Accordion title="Sample Request" icon="fa-code">
  ```bash
  curl --location 'https://test.info.payu.in/merchant/postservice.php?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'command=pre_debit_SI' \
  --data-urlencode 'var1={"authpayuid":"999000000000826","requestid":"RCS0123459PD","debitdate":"2024-11-22","amount":"125","invoiceDisplayNumber":"12345678910","mandateSeqNo":2}' \
  --data-urlencode 'key=JP***g' \
  --data-urlencode 'hash=abc0ada2e12'
  ```
  ```python
  import requests

  url = "https://test.info.payu.in/merchant/postservice.php?form=2"

  payload = {
      "command": "pre_debit_SI",
      "var1": '{"authpayuid":"999000000000826","requestid":"RCS0123459PD","debitdate":"2024-11-22","amount":"125","invoiceDisplayNumber":"12345678910","mandateSeqNo":2}',
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
              new KeyValuePair<string, string>("var1", "{\"authpayuid\":\"999000000000826\",\"requestid\":\"RCS0123459PD\",\"debitdate\":\"2024-11-22\",\"amount\":\"125\",\"invoiceDisplayNumber\":\"12345678910\",\"mandateSeqNo\":2}"),
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
          invoiceDisplayNumber: "12345678910",
          mandateSeqNo: 2
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
              "&var1=" + URLEncoder.encode("{\"authpayuid\":\"999000000000826\",\"requestid\":\"RCS0123459PD\",\"debitdate\":\"2024-11-22\",\"amount\":\"125\",\"invoiceDisplayNumber\":\"12345678910\",\"mandateSeqNo\":2}", StandardCharsets.UTF_8) +
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
          "invoiceDisplayNumber" => "12345678910",
          "mandateSeqNo" => 2
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

<Accordion title="Sample Response" icon="fa-check">
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
  | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
  | Invalid mandateSeqNo                  | `{"status":"0","message":"Invalid value for mandateSeqNo","action":"MANDATE_PRE_DEBIT"}`                                               |
  | Pre-debit already sent for sequence   | `{"status":"E9254","action":"MANDATE_PRE_DEBIT","message":"Predebit notification already sent for the mandate sequence no. 2"}`        |
  | Execution already exists for sequence | `{"status":"E9256","action":"MANDATE_PRE_DEBIT","message":"Execution already sent for the mandate sequence no.:2"}`                    |
  | Debit date exceeds 30 days            | `{"status":"E9260","action":"MANDATE_PRE_DEBIT","message":"Predebit notification can only be sent for a maximum 30 days in advance."}` |
  | Pre-debit sent for past sequence      | `{"status":"E9263","action":"MANDATE_PRE_DEBIT","message":"Predebit for calculated sequence sent during incorrect period"}`            |
</Accordion>

***

## Step 2: Post the Transaction Request

Use the **SI Transaction** API to execute the recurring transaction. The `mandateSeqNo` parameter allows parallel execution of multiple sequences. For more information, refer to [SI Transaction API](ref:si-transaction-api).

| Environment | URL                                                |
| ----------- | -------------------------------------------------- |
| Test        | `https://test.payu.in/merchant/postservice?form=2` |
| Production  | `https://info.payu.in/merchant/postservice?form=2` |

<Accordion title="Sample Request" icon="fa-code">
  ```bash
  curl --location 'https://test.payu.in/merchant/postservice?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=JP***g' \
  --data-urlencode 'command=si_transaction' \
  --data-urlencode 'var1={"authpayuid":"6611192557","invoiceDisplayNumber":"2345678910","amount":"3","txnid":"REC15113506209","phone":"9999999999","email":"abc@email.com","udf2":"","udf3":"","udf4":"","udf5":"","mandateSeqNo":3}' \
  --data-urlencode 'hash=jbUS07Og8BToVZ'
  ```
  ```python
  import requests

  url = "https://test.payu.in/merchant/postservice?form=2"

  payload = {
      "key": "JP***g",
      "command": "si_transaction",
      "var1": '{"authpayuid":"6611192557","invoiceDisplayNumber":"2345678910","amount":"3","txnid":"REC15113506209","phone":"9999999999","email":"abc@email.com","udf2":"","udf3":"","udf4":"","udf5":"","mandateSeqNo":3}',
      "hash": "jbUS07Og8BToVZ"
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
              new KeyValuePair<string, string>("key", "JP***g"),
              new KeyValuePair<string, string>("command", "si_transaction"),
              new KeyValuePair<string, string>("var1", "{\"authpayuid\":\"6611192557\",\"invoiceDisplayNumber\":\"2345678910\",\"amount\":\"3\",\"txnid\":\"REC15113506209\",\"phone\":\"9999999999\",\"email\":\"abc@email.com\",\"udf2\":\"\",\"udf3\":\"\",\"udf4\":\"\",\"udf5\":\"\",\"mandateSeqNo\":3}"),
              new KeyValuePair<string, string>("hash", "jbUS07Og8BToVZ")
          });
          
          var response = await client.PostAsync("https://test.payu.in/merchant/postservice?form=2", content);
          var result = await response.Content.ReadAsStringAsync();
          Console.WriteLine(result);
      }
  }
  ```
  ```javascript
  const executeTransaction = async () => {
      const url = "https://test.payu.in/merchant/postservice?form=2";
      
      const params = new URLSearchParams();
      params.append("key", "JP***g");
      params.append("command", "si_transaction");
      params.append("var1", JSON.stringify({
          authpayuid: "6611192557",
          invoiceDisplayNumber: "2345678910",
          amount: "3",
          txnid: "REC15113506209",
          phone: "9999999999",
          email: "abc@email.com",
          udf2: "",
          udf3: "",
          udf4: "",
          udf5: "",
          mandateSeqNo: 3
      }));
      params.append("hash", "jbUS07Og8BToVZ");
      
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

  executeTransaction();
  ```
  ```java
  import java.io.*;
  import java.net.*;
  import java.nio.charset.StandardCharsets;

  public class SITransaction {
      public static void main(String[] args) throws Exception {
          String url = "https://test.payu.in/merchant/postservice?form=2";
          
          String params = "key=JP***g" +
              "&command=si_transaction" +
              "&var1=" + URLEncoder.encode("{\"authpayuid\":\"6611192557\",\"invoiceDisplayNumber\":\"2345678910\",\"amount\":\"3\",\"txnid\":\"REC15113506209\",\"phone\":\"9999999999\",\"email\":\"abc@email.com\",\"udf2\":\"\",\"udf3\":\"\",\"udf4\":\"\",\"udf5\":\"\",\"mandateSeqNo\":3}", StandardCharsets.UTF_8) +
              "&hash=jbUS07Og8BToVZ";
          
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
  $url = "https://test.payu.in/merchant/postservice?form=2";

  $data = array(
      "key" => "JP***g",
      "command" => "si_transaction",
      "var1" => json_encode(array(
          "authpayuid" => "6611192557",
          "invoiceDisplayNumber" => "2345678910",
          "amount" => "3",
          "txnid" => "REC15113506209",
          "phone" => "9999999999",
          "email" => "abc@email.com",
          "udf2" => "",
          "udf3" => "",
          "udf4" => "",
          "udf5" => "",
          "mandateSeqNo" => 3
      )),
      "hash" => "jbUS07Og8BToVZ"
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

<Accordion title="Sample Response" icon="fa-check">
  **Success scenario**

  ```json
  {
      "status": 1,
      "message": "Transaction Processed successfully",
      "details": {
          "CLPOP-VNQKTR_2": {
              "authpayuid": "999000000000826",
              "transactionid": "SITXN03",
              "amount": "125.00",
              "user_credentials": "",
              "card_token": "",
              "payuid": "999000000000828",
              "status": "in progress",
              "udf1": null,
              "field9": "92|Transaction Initiated",
              "udf2": "",
              "udf3": "",
              "udf4": "Executed",
              "udf5": "999000000000826",
              "phone": "",
              "email": ""
          }
      }
  }
  ```
</Accordion>