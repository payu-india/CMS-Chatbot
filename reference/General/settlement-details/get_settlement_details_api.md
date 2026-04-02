---
title: Get Settlement Details API
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  title: '[OLD]Get Settlement Details API'
  description: >-
    This document provides information on using an API to retrieve settlement
    details from a bank based on a specified date or Unique Transaction
    Reference number. The API can be posted with version 1 or 2 parameters.
  robots: index
---
You can use the **Get Settlement Details** API to retrieve settlement details which the bank has to settle for you. The input is the date for which settlement details are required, where the var1 parameter is the date you want to know the settlement status or UTR (Unique Transaction Reference number). This API can be posted with version (1 or 2) in the var5 parameter.

<Callout icon="📮" theme="default">
  **Postman Collection**: Access the **Get Settlement Details API Postman Collection** from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/bbccd36/getsettlementdetailsapi](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/bbccd36/getsettlementdetailsapi)
</Callout>

<br />

### Environment

| Environment            | URL                                                                                                  |
| :--------------------- | :--------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/merchant/postservice?form=2](https://test.payu.in/merchant/postservice?form=2) |
| Production Environment | [https://info.payu.in/merchant/postservice?form=2](https://info.payu.in/merchant/postservice?form=2) |

<Accordion title="Request parameters" icon="fa-table">
  <Table align={["left","left","left"]}>
    <thead>
      <tr>
        <th style={{ textAlign: "left" }}>
          Parameter
        </th>

        <th style={{ textAlign: "left" }}>
          Reference
        </th>

        <th style={{ textAlign: "left" }}>
          Example
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td style={{ textAlign: "left" }}>
          key
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter must contain the key provided by PayU. For more information on how to generate the Key and Salt, refer to [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard).
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          command
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter must contain the API command as **get\_settlement\_details**.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          var1 `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter must either contain either date for the settlement or UTR (Unique Transaction Reference number).
        </td>

        <td style={{ textAlign: "left" }}>
          2023-09-26
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          var2 `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter must contain the page number to be fetched.
        </td>

        <td style={{ textAlign: "left" }}>
          5
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          var3 `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter must contain the number of records to be paginated on each page is specified in this parameter. If not specified, 2000 records will be fetched.
        </td>

        <td style={{ textAlign: "left" }}>
          1000
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          var4
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter must contain either L or leave it blank.
        </td>

        <td style={{ textAlign: "left" }}>
          L
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          var5
          `optional`
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter must contain the version of the API that can be either 1 or 2.
        </td>

        <td style={{ textAlign: "left" }}>
          1
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          hash `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          Hash logic for this API is:
          sha512(key|command|var1|salt) sha512
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>
    </tbody>
  </Table>
</Accordion>

<Accordion title="Example values" icon="fa-list">
  Use the following sample values while trying out the API:

  * `var1` (date of the transaction/UTR number): 2020-10-26
  * `var2`: 5
  * `var3`: 2000 or more
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ### Simple Request

  ```curl
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&command=get_settlement_details&var1=2021-08-10&hash=259ded5457ad8d078b3c06294413680d0b9eb341682a4f0eecad17256388c2e096f37f5077480e3a56000cc0a3585f7cd73a7d2d10d8225a05b3b93cd27fd5f8"
  ```
  ```python
  import requests

  url = "https://test.payu.in/merchant/postservice?form=2"

  headers = {
      'accept': 'application/json',
      'Content-Type': 'application/x-www-form-urlencoded'
  }

  data = {
      'key': 'JP***g',
      'command': 'get_settlement_details',
      'var1': '2021-08-10',
      'hash': '259ded5457ad8d078b3c06294413680d0b9eb341682a4f0eecad17256388c2e096f37f5077480e3a56000cc0a3585f7cd73a7d2d10d8225a05b3b93cd27fd5f8'
  }

  response = requests.post(url, headers=headers, data=data)
  print(response.json())
  ```
  ```javascript
  const axios = require('axios');

  const url = 'https://test.payu.in/merchant/postservice?form=2';

  const data = new URLSearchParams({
    key: 'JP***g',
    command: 'get_settlement_details',
    var1: '2021-08-10',
    hash: '259ded5457ad8d078b3c06294413680d0b9eb341682a4f0eecad17256388c2e096f37f5077480e3a56000cc0a3585f7cd73a7d2d10d8225a05b3b93cd27fd5f8'
  });

  axios.post(url, data, {
    headers: {
      'accept': 'application/json',
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
  .then(response => console.log(response.data))
  .catch(error => console.error(error));
  ```
  ```java
  import java.io.*;
  import java.net.http.*;
  import java.net.*;

  public class PayURequest {
      public static void main(String[] args) throws Exception {
          HttpClient client = HttpClient.newHttpClient();
          
          String formData = "key=JP***g&command=get_settlement_details&var1=2021-08-10&hash=259ded5457ad8d078b3c06294413680d0b9eb341682a4f0eecad17256388c2e096f37f5077480e3a56000cc0a3585f7cd73a7d2d10d8225a05b3b93cd27fd5f8";
          
          HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create("https://test.payu.in/merchant/postservice?form=2"))
              .header("accept", "application/json")
              .header("Content-Type", "application/x-www-form-urlencoded")
              .POST(HttpRequest.BodyPublishers.ofString(formData))
              .build();
          
          HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
          System.out.println(response.body());
      }
  }
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
          var client = new HttpClient();
          
          var data = new FormUrlEncodedContent(new[]
          {
              new KeyValuePair<string, string>("key", "JP***g"),
              new KeyValuePair<string, string>("command", "get_settlement_details"),
              new KeyValuePair<string, string>("var1", "2021-08-10"),
              new KeyValuePair<string, string>("hash", "259ded5457ad8d078b3c06294413680d0b9eb341682a4f0eecad17256388c2e096f37f5077480e3a56000cc0a3585f7cd73a7d2d10d8225a05b3b93cd27fd5f8")
          });
          
          client.DefaultRequestHeaders.Add("accept", "application/json");
          
          var response = await client.PostAsync("https://test.payu.in/merchant/postservice?form=2", data);
          var result = await response.Content.ReadAsStringAsync();
          
          Console.WriteLine(result);
      }
  }
  ```
  ```perl
  use strict;
  use warnings;
  use LWP::UserAgent;
  use HTTP::Request::Common qw(POST);

  my $ua = LWP::UserAgent->new;

  my $url = 'https://test.payu.in/merchant/postservice?form=2';

  my $response = $ua->request(
      POST $url,
      'accept' => 'application/json',
      'Content-Type' => 'application/x-www-form-urlencoded',
      Content => {
          key => 'JP***g',
          command => 'get_settlement_details',
          var1 => '2021-08-10',
          hash => '259ded5457ad8d078b3c06294413680d0b9eb341682a4f0eecad17256388c2e096f37f5077480e3a56000cc0a3585f7cd73a7d2d10d8225a05b3b93cd27fd5f8'
      }
  );

  print $response->content;
  ```

  ### Sample Request with all the optional parameters

  ```bash
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&command=get_settlement_details&var1=2021-08-10&hash=259ded5457ad8d078b3c06294413680d0b9eb341682a4f0eecad17256388c2e096f37f5077480e3a56000cc0a3585f7cd73a7d2d10d8225a05b3b93cd27fd5f8&var2&var3&var4=L&var5=2"
  ```
  ```python
  import requests

  url = "https://test.payu.in/merchant/postservice?form=2"

  headers = {
      'accept': 'application/json',
      'Content-Type': 'application/x-www-form-urlencoded'
  }

  data = {
      'key': 'JP***g',
      'command': 'get_settlement_details',
      'var1': '2021-08-10',
      'hash': '259ded5457ad8d078b3c06294413680d0b9eb341682a4f0eecad17256388c2e096f37f5077480e3a56000cc0a3585f7cd73a7d2d10d8225a05b3b93cd27fd5f8',
      'var2': '',
      'var3': '',
      'var4': 'L',
      'var5': '2'
  }

  response = requests.post(url, headers=headers, data=data)
  print(response.json())
  ```
  ```javascript
  const axios = require('axios');

  const url = 'https://test.payu.in/merchant/postservice?form=2';

  const data = new URLSearchParams({
    key: 'JP***g',
    command: 'get_settlement_details',
    var1: '2021-08-10',
    hash: '259ded5457ad8d078b3c06294413680d0b9eb341682a4f0eecad17256388c2e096f37f5077480e3a56000cc0a3585f7cd73a7d2d10d8225a05b3b93cd27fd5f8',
    var2: '',
    var3: '',
    var4: 'L',
    var5: '2'
  });

  axios.post(url, data, {
    headers: {
      'accept': 'application/json',
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
  .then(response => console.log(response.data))
  .catch(error => console.error(error));
  ```
  ```java
  import java.io.*;
  import java.net.http.*;
  import java.net.*;

  public class PayURequest {
      public static void main(String[] args) throws Exception {
          HttpClient client = HttpClient.newHttpClient();
          
          String formData = "key=JP***g&command=get_settlement_details&var1=2021-08-10&hash=259ded5457ad8d078b3c06294413680d0b9eb341682a4f0eecad17256388c2e096f37f5077480e3a56000cc0a3585f7cd73a7d2d10d8225a05b3b93cd27fd5f8&var2=&var3=&var4=L&var5=2";
          
          HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create("https://test.payu.in/merchant/postservice?form=2"))
              .header("accept", "application/json")
              .header("Content-Type", "application/x-www-form-urlencoded")
              .POST(HttpRequest.BodyPublishers.ofString(formData))
              .build();
          
          HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
          System.out.println(response.body());
      }
  }
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
          var client = new HttpClient();
          
          var data = new FormUrlEncodedContent(new[]
          {
              new KeyValuePair<string, string>("key", "JP***g"),
              new KeyValuePair<string, string>("command", "get_settlement_details"),
              new KeyValuePair<string, string>("var1", "2021-08-10"),
              new KeyValuePair<string, string>("hash", "259ded5457ad8d078b3c06294413680d0b9eb341682a4f0eecad17256388c2e096f37f5077480e3a56000cc0a3585f7cd73a7d2d10d8225a05b3b93cd27fd5f8"),
              new KeyValuePair<string, string>("var2", ""),
              new KeyValuePair<string, string>("var3", ""),
              new KeyValuePair<string, string>("var4", "L"),
              new KeyValuePair<string, string>("var5", "2")
          });
          
          client.DefaultRequestHeaders.Add("accept", "application/json");
          
          var response = await client.PostAsync("https://test.payu.in/merchant/postservice?form=2", data);
          var result = await response.Content.ReadAsStringAsync();
          
          Console.WriteLine(result);
      }
  }
  ```
  ```perl
  use strict;
  use warnings;
  use LWP::UserAgent;
  use HTTP::Request::Common qw(POST);

  my $ua = LWP::UserAgent->new;

  my $url = 'https://test.payu.in/merchant/postservice?form=2';

  my $response = $ua->request(
      POST $url,
      'accept' => 'application/json',
      'Content-Type' => 'application/x-www-form-urlencoded',
      Content => {
          key => 'JP***g',
          command => 'get_settlement_details',
          var1 => '2021-08-10',
          hash => '259ded5457ad8d078b3c06294413680d0b9eb341682a4f0eecad17256388c2e096f37f5077480e3a56000cc0a3585f7cd73a7d2d10d8225a05b3b93cd27fd5f8',
          var2 => '',
          var3 => '',
          var4 => 'L',
          var5 => '2'
      }
  );

  print $response->content;
  ```

  <Callout icon="📘" theme="info">
    **Note:** The dates queried in the above requests simple request or request with all the optional parameters are the same. The second sample request (under Sample Request for Version 2) includes the var5 parameter with the value 2 to indicate that it is for version 2.
  </Callout>
</Accordion>

<Accordion title="Response parameters description" icon="fa-table">
  <Table align={["left","left","left"]}>
    <thead>
      <tr>
        <th style={{ textAlign: "left" }}>
          **Field**
        </th>

        <th style={{ textAlign: "left" }}>
          **Description**
        </th>

        <th style={{ textAlign: "left" }}>
          **Example**
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td style={{ textAlign: "left" }}>
          payuid
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains a unique sale transaction id generated by Payu for every sale transaction.
        </td>

        <td style={{ textAlign: "left" }}>
          403993715521937565
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          txn\_id
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the sale transaction ID (merchant reference ID for sale).
        </td>

        <td style={{ textAlign: "left" }}>
          13818
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          txn\_date
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the date of the transaction.
        </td>

        <td style={{ textAlign: "left" }}>
          2021-08-10 23:46:25
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          mode
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the mode of the transaction such as credit card, debit card, etc. For more information, refer to [Payment Mode Codes](doc:payment-mode-codes).
        </td>

        <td style={{ textAlign: "left" }}>
          CC
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          amount
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the original amount which was sent in the transaction request by the merchant.
        </td>

        <td style={{ textAlign: "left" }}>
          100
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          request\_id
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the unique request id generated from PayU with any of the following transaction actions: capture/refund/chargeback/refundReversal/chargebackreversal actions actions.
        </td>

        <td style={{ textAlign: "left" }}>
          131278418
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          requestdate
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the request date and time stamp.
        </td>

        <td style={{ textAlign: "left" }}>
          2021-08-10 23:49:16
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          requestaction
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the action taken on the transaction. The action can be any of the following:

          * capture
          * refund
          * cancel
          * chargeback
          * chargeback reversal
          * refundreversal
        </td>

        <td style={{ textAlign: "left" }}>
          refund
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          requestamount
        </td>

        <td style={{ textAlign: "left" }}>
          The parameter contains the amount requested by the merchant to the bank.
        </td>

        <td style={{ textAlign: "left" }}>
          100
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          mer\_UTR
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the merchant Unique Transaction Reference (UTR) number.
        </td>

        <td style={{ textAlign: "left" }}>
          N223211598444659
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          mer\_service\_fee
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the service fee paid by the merchant to the bank. for the transaction
        </td>

        <td style={{ textAlign: "left" }}>
          239.6000
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          mer\_service\_tax
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the tax on service fee paid by the merchant to the bank. for the transaction
        </td>

        <td style={{ textAlign: "left" }}>
          43.1300
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          mer\_net\_amount
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the net amount to be settled by bank to merchant.
        </td>

        <td style={{ textAlign: "left" }}>
          100
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          bank\_name
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the bank name or the card type based on the transaction.
        </td>

        <td style={{ textAlign: "left" }}>
          MAST
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          issuing\_bank
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the card issuing bank name is displayed.
        </td>

        <td style={{ textAlign: "left" }}>
          SBI
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          merchant\_subvention\_amount
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains merchant subvention amount.
        </td>

        <td style={{ textAlign: "left" }}>
          100
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          cgst
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the CGST (Central GST) for the transaction.
        </td>

        <td style={{ textAlign: "left" }}>
          43.13000
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          igst
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the IGST (Integrated GST) for the transaction.
        </td>

        <td style={{ textAlign: "left" }}>
          43.13000
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          sgst
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the SGST (State GST) for the transaction where the supplier or merchant is from a different state of the customer.
        </td>

        <td style={{ textAlign: "left" }}>
          43.13000
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          PG\_TYPE
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the payment gateway type is displayed in this transaction.
        </td>

        <td style={{ textAlign: "left" }}>
          HDFC\_Internal\_Plus
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          Card Type
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter indicates whether the card is international or domestic
        </td>

        <td style={{ textAlign: "left" }}>
          Domestic.
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          SettlementType
        </td>

        <td style={{ textAlign: "left" }}>
          This describes about the charges whether its regular processing fee or instant charges
        </td>

        <td style={{ textAlign: "left" }}>
          Regular or Instant
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          Scheme
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the scheme.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          FeeType
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains fee type if the fee is collected for instant settlements or refunds.
        </td>

        <td style={{ textAlign: "left" }}>
          tdrFee
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          InstantSettlementTDR
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the TDR collected for instant settlement.
        </td>

        <td style={{ textAlign: "left" }}>
          0.0
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          InstantSettlementTDRTax
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the tax for the TDR collected for instant settlement.
        </td>

        <td style={{ textAlign: "left" }}>
          0.0
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          InstantSettlementTdrType
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the TDR type for instant settlement.
        </td>

        <td style={{ textAlign: "left" }}>
          0.0
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          InstantRefundTDR
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the TDR collected for instant refunds.
        </td>

        <td style={{ textAlign: "left" }}>
          0.0
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          InstantRefundTDRTax
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the tax for the TDR collected for instant refunds.
        </td>

        <td style={{ textAlign: "left" }}>
          0.0
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          InstantRefundTdrType
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the TDR type for instant refund.
        </td>

        <td style={{ textAlign: "left" }}>
          0.0
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          perDayServiceFee
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the per day service fee for instant settlement or refunds.
        </td>

        <td style={{ textAlign: "left" }}>
          0,0
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          perDayServiceTax
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the per day service tax for instant settlement or refunds.
        </td>

        <td style={{ textAlign: "left" }}>
          0,0
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          pricingDays
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the pricing days for instant settlement or refunds.
        </td>

        <td style={{ textAlign: "left" }}>
          1
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          offerServiceFee
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the service fee for offer.
        </td>

        <td style={{ textAlign: "left" }}>
          0,0
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          offerServiceTax
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the tax for offer service fee.
        </td>

        <td style={{ textAlign: "left" }}>
          0,0
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>

<Accordion title="Sample response" icon="fa-file-code">
  ### Success Scenario

  On successful processing from PayU, the response is similar to the following:

  ```json
  {
      "status": 1,
      "msg": "1 transactions settled on 2021-08-11",
      "Txn_details": {
          "1": {
              "payuid": "13799177287",
              "txnid": "13818",
              "txndate": "2021-08-10 23:46:25",
              "mode": "DC",
              "amount": "11979.88",
              "requestid": "9586840660",
              "requestdate": "2021-08-10 23:49:16",
              "requestaction": "capture",
              "requestamount": "11979.88",
              "mer_utr": "N223211598444659",
              "mer_service_fee": "239.6000",
              "mer_service_tax": "43.1300",
              "mer_net_amount": "11697.1500",
              "bank_name": "MAST",
              "issuing_bank": "SBI",
              "merchant_subvention_amount": "0.00",
              "cgst": "0.00000",
              "igst": "43.13000",
              "sgst": "0.00000",
              "PG_TYPE": "HDFC_Internal_Plus",
              "Card Type": "",
              "token": ""
          }
      }
  }
  ```

  ### Failure scenario

  If the date format is incorrect:

  ```json
  {
      "status": 0,
      "msg": "Please check date format it should be YYYY-MM-DD"
  }
  ```

  If no data found for the particular date queried:

  ```json
  {
      "status": 1,
      "msg": "0 transactions settled on 2015-05-01",
      "Txn_details": {}
  }
  ```

  For the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).
</Accordion>
