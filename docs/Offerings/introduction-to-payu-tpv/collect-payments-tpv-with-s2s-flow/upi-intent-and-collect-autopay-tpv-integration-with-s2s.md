---
title: UPI Intent and Collect Autopay - TPV Integration with S2S
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: UPI Intent and Collect Autopay - TPV Integration
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
For recurring payment use-case, you can use UPI as a payment instrument. It requires, registration of the mandate and then doing the debit in the customer's account. During registration, customer validates the billing details of the mandate on the respective application, enters their MPIN (Mobile PIN) and authorizes the mandate. After the registration transaction is successful, you can then use the **Recurring Payment Transaction** API to charge the customer without requiring further intervention. For more information on Recurring Payment API, refer to  [Recurring Payment Transaction API](ref:recurring_payment_api)

The Third-Party Verification (TPV) functionality is now being added to the UPI Autopay too.

> 📘 Notes:
>
> - Currently, PayU supports UPI Autopay only with Seamless integration.
> - Contact your PayU Key Account Manager (KAM) or [PayU Support ](https://help.payu.in)to activate this feature.

**Steps to integrate**

<Cards columns={2}>
  <Card title="1. Validate VPA" href="#step-1-validate-vpa">
    Validate customer's Virtual Payment Address (UPI handle)

    <br />
  </Card>

  <Card title="2. Post Parameters" href="#step-2-post-the-parameters-to-payu">
    Post transaction request with SI and beneficiary details

    <br />
  </Card>

  <Card title="3. Authentication Flow" href="#step-3-authentication-flow">
    Authenticate the payment with the customer's bank for Intent Autopay

    <br />
  </Card>

  <Card title="4. Authorize Payment" href="#step-4-authorize-charge-the-payment">
    Authorize and charge the authenticated payment for Intent Autopay

    <br />
  </Card>

  <Card title="5. Check Response" href="#step-5-check-the-response-from-payu">
    Validate the response and reverse hash from PayU

    <br />
  </Card>

  <Card title="6. Verify Payment" href="#step-6-verify-the-payment">
    Verify the payment using verify\_payment API
  </Card>
</Cards>

## Use Cases

Merchants have use cases, which requires the transactions to be allowed only for selected accounts only. These accounts are provided by the customer before hand (during customer registration on merchant platform). Few merchant use cases are:

- Mutual Funds (SEBI guidelines)
- Loan Repayment

However, as part of UPI, customer has the flexibility to link multiple accounts under the same VPA and on run-time, change the account for authorization. So using TPV services, merchant makes sure that customer authorizes the transaction using pre-registered accounts only.

## Steps to Integrate

Refer any of the following tabs based on the Intent or Collect Autopay Flow integration:

<Tabs>
  <Tab title="Intent Autopay TPV">
    ### Intent Autopay Workflow

    The merchant initiates the call to PayU with SI details, **bankcode** as **INTTPV**, and account number + IFSC details. PayU then initiates a mandate call to the bank, including all the SI and account-related parameters. The bank responds to PayU with a reference-Id, which PayU passes to the merchant in an Intent URL. When the customer authorizes the transaction, the bank will validate the account. If the account details match, a success message will be sent to PayU. However, if the account details do not match, Bank will pass validation error to PayU. Internally, Bank will cancel the mandate that has been set up on customer's account.

    <Callout icon="📘" theme="info">
      **Note**: Validation is done only in the registration step of the mandate. If the account matches, rest of the journey for UPI Autopay will remain as-is.
    </Callout>

    <Callout icon="📘" theme="info">
      **Prerequisites**

      S2S (Seamless) integration has to be done as per the standard kit. For more information, refer to [UPI Integrations - S2S](doc:upi-integrations-s2s).

      **Supported only in Seamless integration**: Currently, PayU supports UPI Intent Autopay only with Seamless integration.
    </Callout>

    ## Step 1: Validate VPA

    When your customer makes payment through UPI, you can validate the customer's Virtual Payment Address (VPA) and then initiate payment. The **validateVpa** API is used to validate the UPI handle. Validate the VPA (UPI handle) using the **validateVpa** API. For Try-It experience of **validateVpa** API, refer to [Validate VPA Handle API](ref:validate_vpa_api).

    ## Environments

    |                        |                                                        |
    | :--------------------- | :----------------------------------------------------- |
    | Test Environment       | `https://test.payu.in/merchant/postservice.php?form=2` |
    | Production Environment | `https://info.payu.in/merchant/postservice.php?form=2` |

    <Accordion title="Sample request" icon="fa-code">
      **Validate VPA**

      ```curl
      curl -X POST "https://test.payu.in/merchant/postservice?form=2" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&command=validateVPA&var1=9999999999@upi&hash=75bb573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472fff9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e"
      ```
    </Accordion>

    <Accordion title="Sample response" icon="fa-reply">
      **Success scenario**

      if successfully validated:

      ```plaintext
      {
         "status":"SUCCESS",
         "vpa":"9999999999@upi",
         "isVPAValid":1,
         "isAutoPayVPAValid":1,
         "isAutoPayBankValid":"NA",
         "payerAccountName":"ABC"
      }
      ```

      > 📘 Notes:
      >
      > * The **payerAccountName** parameter can be empty or NA or will have a payer name based on the value given by the bank.
      > * If both **isVPAValid** and **isAutoPayVPAValid** is 1, you must initiate payment for Recurring Payments.
      > * Ignore the **isAutoPayBankValid** parameter in the response.

      **Failure scenarios**

      * If invalid VPA, the response is similar to the following:

      ```plaintext
      {
       "status":"SUCCESS","vpa":"abc@upi","isVPAValid":0,"payerAccountName":"NA"
      }  
      ```

      * Invalid VPA but handle supporting SI (Autopay):

      ```plaintext
      {
       "status":"SUCCESS","vpa":"abc@upi","isVPAValid":0,"isAutoPayVPAValid":1,"isAutoPayBankValid":"NA","payerAccountName":"NA"
      }
      ```

      * Customer valid but handle not supporting SI (Autopay):

      ```plaintext
      {
        "status":"SUCCESS","vpa":"xyz@freecharge","isVPAValid":1,"isAutoPayVPAValid":0,"isAutoPayBankValid":"NA","payerAccountName":"XYZ"
      }
      ```

      * Neither customer valid nor handle supporting Autopay:

      ```plaintext
      {
        "status":"SUCCESS","vpa":"xyz@freecharge","isVPAValid":0,"isAutoPayVPAValid":0,"isAutoPayBankValid":"NA","payerAccountName":"NA"
      }
      ```
    </Accordion>

    <Accordion title="Sample validation JS code" icon="fa-reply">
      ```javascript
      	// JavaScript example for VPA validation before payment submission
      // This should be run on your server, not client-side

      async function validateVpa(vpa) {
          try {
              // Get hash from server endpoint
              const hashResponse = await fetch('/generate-vpa-hash', {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/json' },
                  body: JSON.stringify({ vpa })
              });
              const { hash } = await hashResponse.json();
              
              // Validate VPA with PayU
              const response = await fetch('https://test.payu.in/merchant/postservice?form=2', {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                  body: new URLSearchParams({
                      key: 'YOUR_MERCHANT_KEY',
                      command: 'validateVPA',
                      var1: vpa, // VPA to validate
                      hash: hash
                  })
              });
              
              const result = await response.json();
              
              // Sample response:
              // {"status":1,"msg":"VPA is valid","isVPAValid":1,"isUPIBarredBank":0}
              // OR
              // {"status":0,"msg":"VPA is invalid","isVPAValid":0}
              
              return {
                  isValid: result.isVPAValid === 1,
                  message: result.msg
              };
          } catch (error) {
              console.error('VPA validation error:', error);
              return { isValid: false, message: 'Validation service error' };
          }
      }

      ```
      ```curl
      # Once you have the hash, make the API call

      curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -d "key=YOUR_MERCHANT_KEY" \
        -d "command=validateVPA" \
        -d "var1=customer@upi" \
        -d "hash=$HASH"

      ```
    </Accordion>

    ## Step 2: Post the parameters to PayU

    With the following parameters, make the transaction request with the customer's bank account number to the PayU using the Collect Payment (**\_payment**) API.

    **Environment**

    | Environment            | URL                                                                 |
    | ---------------------- | ------------------------------------------------------------------- |
    | Test Environment       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
    | Production Environment | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |

    <Accordion title="Request parameters" icon="fa-table">
      In the merchant-initiated POST REQUEST, Hash is a mandatory parameter. It is critical to calculate the hash correctly and post it to PayU in the request.

      | Parameter                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Value                                                                                                                                           |
      | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
      | key <br /> `mandatory`               | `String` The merchant key is a unique identifier for a merchant account in PayU's database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Your Test Key                                                                                                                                   |
      | api\_version <br /> `optional`       | `String` The API version for this API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 7                                                                                                                                               |
      | txnid <br /> `mandatory`             | `String` The transaction ID is a reference number for a specific order that is generated by the merchant. It is used to track the order and must be unique. PayU's system will not accept duplicate transaction IDs.                                                                                                                                                                                                                                                                                                                                                                                                                   | s7hhDQVWvbhBdN                                                                                                                                  |
      | amount <br /> `mandatory`            | `String` This field should contain the payment amount for the transaction. The limit for recurring payments using UPI payment mode: \* **Auto-debit** is Rs.15000 (the auto-debit limit is higher for below listed purpose) \* **With PIN** is Rs.1,00,00 \* **Note**: The auto-debit limit for the following UPI recurring payments is one lakh rupees (Rs.1,00,000): \* Insurance premiums \* Credit card bill payments \* Insurance premium                                                                                                                                                                                         | 10.00                                                                                                                                           |
      | productinfo <br /> `mandatory`       | `String` It should be a string containing a brief description of the product. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | iPhone                                                                                                                                          |
      | firstname <br /> `mandatory`         | `String` The first name of the customer. `Character Limit-60`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Ashish                                                                                                                                          |
      | email <br /> `mandatory`             | `String` The email of the customer. `Character Limit-50`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [test@gmail.com](mailto:test@gmail.com)                                                                                                         |
      | phone <br /> `mandatory`             | `String` The phone number of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 9876543210                                                                                                                                      |
      | lastname <br /> `mandatory`          | `String` The last name of the customer. `Character Limit-60`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Verma                                                                                                                                           |
      | address1 <br /> `optional`           | `String` The first line of the billing address. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai                                                                                         |
      | address2 <br /> `optional`           | `String` The second line of the billing address. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 34 Saikripa-Estate, Tilak Nagar                                                                                                                 |
      | city <br /> `optional`               | `String` The city where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Mumbai                                                                                                                                          |
      | state <br /> `optional`              | `String` The state where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Maharashtra                                                                                                                                     |
      | country <br /> `optional`            | `String` The country where your customer resides. `Character Limit-50`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | India                                                                                                                                           |
      | zipcode <br /> `optional`            | `String` Billing address zip code is mandatory for the cardless EMI option. `Character Limit-20`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 400004                                                                                                                                          |
      | surl  <br /> `mandatory`             | `String` The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                       | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                  |
      | furl <br /> `mandatory`              | `String` The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                           | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                  |
      | hash <br /> `mandatory`              | `String` It is used to avoid the possibility of transaction tampering. For the hash checksum logic, refer to [Checksum Logic for Hash](#checksum-logic-for-hash).                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `eabec285da28fd 0e3054d41a4d24fe 9f7599c9d0b6664 6f7a9984303fd612 4044b6206daf831 e9a8bda28a6200d 318293a13d6c193 109b60bd4b4f8b09 c90972`      |
      | pg <br /> `mandatory`                | `varchar` The **pg** parameter for UPI must be UPI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | UPI                                                                                                                                             |
      | bankcode <br /> `mandatory`          | `varchar` This parameter contains INTTPV for UPI Intent TPV Autopay.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | INTTPV                                                                                                                                          |
      | s2s_client_ip <br /> `mandatory`     | `String` This parameter must have the source IP of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                 |
      | s2s_device_info <br /> `mandatory`   | `String` This parameter must have the customer agent's device.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                 |
      | txn_s2s_flow <br /> `mandatory`      | `String` This parameter must be passed with the value as **4** for Legacy Decoupled flow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 4                                                                                                                                               |
      | si <br /> `mandatory`                | This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                 |
      | si\_details <br /> `mandatory`       | This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU. \* **Note**: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers (for more details refer – [https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0)) This is a JSON object and it includes a set of fields. For more information, refer to [SI Parameter JSON Details](ref:si-parameter-json-details) |                                                                                                                                                 |
      | beneficiarydetail <br /> `mandatory` | This is a JSON format text and there should be key named **beneficiaryAccountNumber** with the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key). You can post up to five account details in this parameter.                                                                                                                                                                                                                                                                                                                  | Refer to [beneficiarydetail JSON Object Fields](https://docs.payu.in/docs/net-banking-integration-for-tpv#beneficiarydetail-json-object-fields) |
    </Accordion>

    <Accordion title="beneficiarydetail JSON Object Fields" icon="fa-code">
      It must contain the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key). You can post up to five account details in this parameter. For example:

      ```
      {"beneficiaryAccountNumber":"002001600674|00000031957292212|00000035955239352|00000035955239352",  
      "ifscCode":"KTKB0000046|KTKB0000023|KTKB0000035|KTKB0000035"}
      ```

      **Checksum Logic for Hash**

      The following hash logic must be used for the parameters posted:

      > 📘 si\_details parameter in Hashing:
      >
      > The **si\_details** parameter value will be at last or the last value to be appended.
      >
      > ```plaintext
      > key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3
      > |udf4|udf5||||||si_details|SALT
      > ```
    </Accordion>

    <Accordion title="Sample Request" icon="fa-code">
    ```curl
    curl --request POST 'https://test.payu.in/_payment' \
      --header 'Content-Type: application/x-www-form-urlencoded' \
      --data-urlencode 'key=JP***g' \
      --data-urlencode 'txnid=upi_intent_autopay_tpv_12345' \
      --data-urlencode 'amount=10.00' \
      --data-urlencode 'productinfo=UPI Autopay Mandate' \
      --data-urlencode 'firstname=Ashish' \
      --data-urlencode 'lastname=Verma' \
      --data-urlencode 'email=test@payu.in' \
      --data-urlencode 'phone=9876543210' \
      --data-urlencode 'pg=UPI' \
      --data-urlencode 'bankcode=INTTPV' \
      --data-urlencode 'si=1' \
      --data-urlencode 'si_details={"billingAmount":"10.00","billingCurrency":"INR","billingCycle":"MONTHLY","billingInterval":1,"paymentStartDate":"2026-08-01","paymentEndDate":"2027-07-31"}' \
      --data-urlencode 'beneficiarydetail={"beneficiaryAccountNumber":"002001600674","ifscCode":"KTKB0000046"}' \
      --data-urlencode 'api_version=7' \
      --data-urlencode 'surl=https://example.com/payment/success' \
      --data-urlencode 'furl=https://example.com/payment/failure' \
      --data-urlencode 's2s_client_ip=192.0.2.1' \
      --data-urlencode 's2s_device_info=Mozilla/5.0' \
      --data-urlencode 'txn_s2s_flow=4' \
      --data-urlencode 'hash=YOUR_CALCULATED_HASH'
    ```
    ```python
    import json
    import requests

    data = {
        "key": "JP***g",
        "txnid": "upi_intent_autopay_tpv_12345",
        "amount": "10.00",
        "productinfo": "UPI Autopay Mandate",
        "firstname": "Ashish",
        "lastname": "Verma",
        "email": "test@payu.in",
        "phone": "9876543210",
        "pg": "UPI",
        "bankcode": "INTTPV",
        "si": "1",
        "si_details": json.dumps({
            "billingAmount": "10.00",
            "billingCurrency": "INR",
            "billingCycle": "MONTHLY",
            "billingInterval": 1,
            "paymentStartDate": "2026-08-01",
            "paymentEndDate": "2027-07-31"
        }),
        "beneficiarydetail": json.dumps({
            "beneficiaryAccountNumber": "002001600674",
            "ifscCode": "KTKB0000046"
        }),
        "api_version": "7",
        "surl": "https://example.com/payment/success",
        "furl": "https://example.com/payment/failure",
        "s2s_client_ip": "192.0.2.1",
        "s2s_device_info": "Mozilla/5.0",
        "txn_s2s_flow": "4",
        "hash": "YOUR_CALCULATED_HASH"
    }
    response = requests.post("https://test.payu.in/_payment", data=data)
    print(response.status_code, response.text)
    ```
    ```javascript
    const params = new URLSearchParams({
      key: 'JP***g',
      txnid: 'upi_intent_autopay_tpv_12345',
      amount: '10.00',
      productinfo: 'UPI Autopay Mandate',
      firstname: 'Ashish',
      lastname: 'Verma',
      email: 'test@payu.in',
      phone: '9876543210',
      pg: 'UPI',
      bankcode: 'INTTPV',
      si: '1',
      si_details: JSON.stringify({
        billingAmount: '10.00',
        billingCurrency: 'INR',
        billingCycle: 'MONTHLY',
        billingInterval: 1,
        paymentStartDate: '2026-08-01',
        paymentEndDate: '2027-07-31'
      }),
      beneficiarydetail: JSON.stringify({
        beneficiaryAccountNumber: '002001600674',
        ifscCode: 'KTKB0000046'
      }),
      api_version: '7',
      surl: 'https://example.com/payment/success',
      furl: 'https://example.com/payment/failure',
      s2s_client_ip: '192.0.2.1',
      s2s_device_info: 'Mozilla/5.0',
      txn_s2s_flow: '4',
      hash: 'YOUR_CALCULATED_HASH'
    });
    const response = await fetch('https://test.payu.in/_payment', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: params
    });
    console.log(response.status, await response.text());
    ```
    ```java
    import java.net.URI;
    import java.net.URLEncoder;
    import java.net.http.HttpClient;
    import java.net.http.HttpRequest;
    import java.net.http.HttpResponse;
    import java.nio.charset.StandardCharsets;
    import java.util.LinkedHashMap;
    import java.util.Map;
    import java.util.stream.Collectors;

    public class UpiIntentAutopayTpv {
        public static void main(String[] args) throws Exception {
            Map<String, String> data = new LinkedHashMap<>();
            data.put("key", "JP***g");
            data.put("txnid", "upi_intent_autopay_tpv_12345");
            data.put("amount", "10.00");
            data.put("productinfo", "UPI Autopay Mandate");
            data.put("firstname", "Ashish");
            data.put("lastname", "Verma");
            data.put("email", "test@payu.in");
            data.put("phone", "9876543210");
            data.put("pg", "UPI");
            data.put("bankcode", "INTTPV");
            data.put("si", "1");
            data.put("si_details", "{\"billingAmount\":\"10.00\",\"billingCurrency\":\"INR\",\"billingCycle\":\"MONTHLY\",\"billingInterval\":1,\"paymentStartDate\":\"2026-08-01\",\"paymentEndDate\":\"2027-07-31\"}");
            data.put("beneficiarydetail", "{\"beneficiaryAccountNumber\":\"002001600674\",\"ifscCode\":\"KTKB0000046\"}");
            data.put("api_version", "7");
            data.put("surl", "https://example.com/payment/success");
            data.put("furl", "https://example.com/payment/failure");
            data.put("s2s_client_ip", "192.0.2.1");
            data.put("s2s_device_info", "Mozilla/5.0");
            data.put("txn_s2s_flow", "4");
            data.put("hash", "YOUR_CALCULATED_HASH");

            String body = data.entrySet().stream()
                .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "="
                    + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
                .collect(Collectors.joining("&"));
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(body))
                .build();
            HttpResponse<String> response = HttpClient.newHttpClient()
                .send(request, HttpResponse.BodyHandlers.ofString());
            System.out.println(response.statusCode() + " " + response.body());
        }
    }
    ```
    ```php
    <?php
    $data = [
        'key' => 'JP***g',
        'txnid' => 'upi_intent_autopay_tpv_12345',
        'amount' => '10.00',
        'productinfo' => 'UPI Autopay Mandate',
        'firstname' => 'Ashish',
        'lastname' => 'Verma',
        'email' => 'test@payu.in',
        'phone' => '9876543210',
        'pg' => 'UPI',
        'bankcode' => 'INTTPV',
        'si' => '1',
        'si_details' => json_encode([
            'billingAmount' => '10.00',
            'billingCurrency' => 'INR',
            'billingCycle' => 'MONTHLY',
            'billingInterval' => 1,
            'paymentStartDate' => '2026-08-01',
            'paymentEndDate' => '2027-07-31'
        ]),
        'beneficiarydetail' => json_encode([
            'beneficiaryAccountNumber' => '002001600674',
            'ifscCode' => 'KTKB0000046'
        ]),
        'api_version' => '7',
        'surl' => 'https://example.com/payment/success',
        'furl' => 'https://example.com/payment/failure',
        's2s_client_ip' => '192.0.2.1',
        's2s_device_info' => 'Mozilla/5.0',
        'txn_s2s_flow' => '4',
        'hash' => 'YOUR_CALCULATED_HASH'
    ];
    $ch = curl_init('https://test.payu.in/_payment');
    curl_setopt_array($ch, [
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => http_build_query($data),
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPHEADER => ['Content-Type: application/x-www-form-urlencoded']
    ]);
    $response = curl_exec($ch);
    echo curl_getinfo($ch, CURLINFO_HTTP_CODE) . ' ' . $response;
    curl_close($ch);
    ?>
    ```
    </Accordion>

    ## Step 3: Authentication Flow

    On basis of a successful response of the Collect Payment (**\_payment**) API, you need to redirect the user to the bank page using **acsTemplate**. In case of Bank page authentication (Non-Native OTP), ACS server will redirect the customer to termUrl passed in the payment request during initiation and authenticationResult will be posted along "cres" over the termUrl.

    > 📘 Notes:
    >
    > - All callbacks POST form data on the merchant's `termUrl` that is passed in Initiate Transaction API.
    > - Validation of the response happens on the basis of the hash value being returned in the hash value of the response.

    <Accordion title="Response parameters over termURL" icon="fa-table">
      | Parameter                                        | Description | Example |
      | ------------------------------------------------ | ----------- | ------- |
      | rawBankData<br /><code>mandatory</code>          | <code>String</code> This parameter contains the raw response that is received from bank after authentication. The response is urlencoded and in query string format. | bankRespId=123\&status=success\&amount=1000 |
      | referenceId<br /><code>mandatory</code>          | <code>String</code> This parameter contains the reference id being returned for the transaction. | TXN\_REF\_123456789 |
      | bankData<br /><code>mandatory</code>             | <code>JSON</code> This parameter contains the JSON string that is to be used for authorization call. This parameter is received in case of successful OTP submission of decoupled transactions. The postToBank contains messageDigest and pares that is to be posted back for authorization. For more information on the fields in this JSON, refer to [bankData JSON Fields Description](#bankdata-json-fields-description). | |
      | authenticationStatus<br /><code>mandatory</code> | <code>String</code> This parameter contains the authentication status of the transaction. | SUCCESS |
      | hash<br /><code>mandatory</code>                 | <code>String</code> This parameter contains the calculated hash of the data that is posted to the merchant. For security purpose it is recommended to validate the hash value before consuming the response. The hash calculation logic is: <code>sha512(authenticationStatus\\\|bankData\\\|rawBankData\\\|referenceId\\\|salt)</code> | 5d41402abc4b2a76b9719d911017c592b2d4c3ef45d0b9e1c9b5a7b2c8f9e0d3 |
    </Accordion>

    <Accordion title="bankData JSON fields description" icon="fa-table">
      #### bankData JSON Fields Description

      | Field                                        | Description | Applicable for EMV 3DS |
      | -------------------------------------------- | ----------- | ---------------------- |
      | cres<br /><code>mandatory</code>             | This field contains the Base64 encoded value received from ACS as part of the authentication response. <code>String</code> | Yes |
      | referenceId<br /><code>mandatory</code>      | This field is returned in case of decoupled flow. This field contains the reference id for the transaction. <code>String</code> | REF\_12345 |
      | messageDigest<br /><code>mandatory</code>    | This field is returned in case of decoupled flow. This field contains the MD value being returned by the bank. <code>String</code> | d41d8cd98f00b204e9800998ecf8427e |
      | pares<br /><code>mandatory</code>            | This field is returned in case of decoupled flow. This field contains the pares being returned by the bank. <code>String</code> | eJyrVkosLcmIz8nPS1WyUorPTFGyMjJQUkoD8ZNrAQytCFn |
      | additionalInfo<br /><code>mandatory</code>   | This field is returned in case of decoupled flow. This field contains the data that is being used for the gateways that do not return pares. <code>String</code> | transaction\_id=12345\&status=pending |
      | authorizationUrl<br /><code>mandatory</code> | This integration document assumes that you have opted out for the particular configuration. The authorization URL in legacy integrations is present based on the configuration at PayU. Contact your PayU Key Account Manager (KAM) to know more. <code>String</code> | [https://secure.payu.in/merchant/postservice?form=5ea3a2d](https://secure.payu.in/merchant/postservice?form=5ea3a2d) |
    </Accordion>

    ## Step 4: Authorize (charge) the payment

    The authorization request is the final step of transaction processing. This again needs to be an S2S call from the merchant's server to PayU server.

    > 📘
    >
    > **Note:**
    >
    > - **For Redirection Based authentication from termUrl (if being sent by PayU)**: If `authenticationStatus=success`, use the `bankData` parameter value as it is under the **authentication\_info** parameter of the **Authorize Transaction API**.
    > - **For Native OTP based Authentication**: If **metaData.txnStatus** is "Authenticated", use the `result.postToBank` object value in the authentication\_info parameter of the **Authorize Transaction API**.

    #### Environment

    |            |                                                                                                    |
    | ---------- | -------------------------------------------------------------------------------------------------- |
    | Test       | [https://test.payu.in/AuthorizeTransaction.php](https://test.payu.in/AuthorizeTransaction.php)     |
    | Production | [https://secure.payu.in/AuthorizeTransaction.php](https://secure.payu.in/AuthorizeTransaction.php) |

    <Accordion title="Request parameters" icon="fa-code">
      **Post URL**: The data to be posted has to be exactly the same as the JSON response received in the authentication response in [Step 3](#step-3-authentication-flow). The data must include the following parameters.

      | Parameter                                        | Description | Example |
      | ------------------------------------------------ | ----------- | ------- |
      | key<br /><code>mandatory</code>                  | The merchant key is provided by PayU and acts as a unique identifier for a specific merchant account in PayU's database. <code>String</code> | gtKFFx |
      | txnid<br /><code>mandatory</code>                | The transaction ID is the order reference number generated by the merchant to track a particular order. It can be used only once and PayU's system does not accept a duplicate Transaction ID. <code>String</code> | ORD\_123456789 |
      | amount<br /><code>mandatory</code>               | It should contain the payment amount of the particular transaction. The amount must be greater than Rs. 8000 for the cardless EMI option. <code>String</code> | 10000.00 |
      | hash<br /><code>mandatory</code>                 | It is used to avoid the possibility of transaction tampering. The hash must be in the following structure: <code>valueOf(key)\\\|valueOf(txnid)\\\|valueOf(amount)\\\|valueOf(authentication\_info)\\\|valueOf(salt)</code> <code>String</code> | 3af7c2b8e6f9d4e1a9b7c5e2f8d3a6b9e1c4f7a2d5e8b1c3f6a9d2e5b8c1a4f7 |
      | authentication\_info<br /><code>mandatory</code> | The JSON value received in the bankData on the Term URL, or pass the fields as in the JSON example. <code>JSON</code> | |

      #### Example for authentication\_info JSON

      ```json
      {
        "referenceId": "4b6dcb255093a92dc38599b82ac0f796619410e322a2b68ba69a6c7aa5dfb78d",
        "cres": "eyJtZXNzYWdlVHlwZSI6IkNSZXMiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIiwidGhyZWVEU1NlcnZlclRyYW5zSUQiOiIxMDY3ZjkyNi00YTJjLTE2MGMtOWU0ZS1lZmIxNjBiNjkwMGYiLCJUcmFuc2FjdGlvbklkIjoiNWU4NDE4ZDYtMWI4Ny01NzVhLWJkMzUtYjRkOWU0NjUiLCJjcmVzIjoiZXlKMGFISmxaVVJUVTJWeWRtVnlWSEpoYm5OSlJDSTZJakV3TmpkbU9USTJMVFJoTW1NdE1UWXdZeTA1WlRSbExXVm1ZakUyTUdJMk9UQXdaaUlzSW1GamMxUnlZVzV6U1VRaU9pSm1Zems1WkdJNU1pMWhOVGczTFRNek5qUXRNRFEzTXkxaE1HUTVPR1kwTnpReFptTWlMQ0p0WlhOellXZGxWSGx3WlNJNklrTlNaWE1pTENKdFpYTnpZV2RsVm1WeWMybHZiaUk2SWpJdU1pNHdJaXdpWTJoaGJHeGxibWRsUTI5dGNHeGxkR2x2YmtsdVpDSTZJbGtpTENKMGNtRnVjMU4wWVhSMWN5STZJbGtpTENKbFkya2lPaUl3TWlKOSJ9",
        "additionalInfo": {
          "authUdf1": "",
          "authUdf2": "",
          "authUdf3": "",
          "authUdf4": "",
          "authUdf5": "",
          "authUdf6": "",
          "authUdf7": "",
          "authUdf8": "",
          "authUdf9": "",
          "authUdf10": ""
        }
      }
      ```

      #### authentication\_info JSON Fields Description

      | **Field**      | **Description**                                                                                        | **Applicable to EMV 3DS** |
      | -------------- | ------------------------------------------------------------------------------------------------------ | ------------------------- |
      | cres           | This field contains the Base 64 encoded value received from ACS as part of the authentication response | Yes                       |
      | referenceId    | This field contains the same referenceId which was sent in response to the first call                   |                           |
      | additionalInfo | This field can be used in the case of schemes where different parameters may be needed from the merchant side. |                    |
      | messageDigest  | This field includes the Base 64 encoding of the SHA-256 hash of the JSON data posted to the server.     |                           |
      | pares          | This parameter contains the pares being returned by the bank.                                           |                           |
    </Accordion>

    <Accordion title="Sample request" icon="fa-code">
      ```
      curl POST 'https://test.payu.in/AuthorizeTransaction' \
        --header 'Cookie: PHPSESSID=ca4slgf2hlcc3a80tauvnh96cr; PHPSESSID=69c3e6c6a9ee8' \
        --form 'key=PRiQvJ' \
        --form 'txnid=my_order_75942' \
        --form 'amount=2' \
        --form 'authentication_info={
          "referenceId": "4b6dcb255093a92dc38599b82ac0f796619410e322a2b68ba69a6c7aa5dfb78d",
          "cres": "eyJtZXNzYWdlVHlwZSI6IkNSZXMiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIiwidGhyZWVEU1NlcnZlclRyYW5zSUQiOiIxMDY3ZjkyNi00YTJjLTE2MGMtOWU0ZS1lZmIxNjBiNjkwMGYiLCJUcmFuc2FjdGlvbklkIjoiNWU4NDE4ZDYtMWI4Ny01NzVhLWJkMzUtYjRkOWU0NjUiLCJjcmVzIjoiZXlKMGFISmxaVVJUVTJWeWRtVnlWSEpoYm5OSlJDSTZJakV3TmpkbU9USTJMVFJoTW1NdE1UWXdZeTA1WlRSbExXVm1ZakUyTUdJMk9UQXdaaUlzSW1GamMxUnlZVzV6U1VRaU9pSm1Zems1WkdJNU1pMWhOVGczTFRNek5qUXRNRFEzTXkxaE1HUTVPR1kwTnpReFptTWlMQ0p0WlhOellXZGxWSGx3WlNJNklrTlNaWE1pTENKdFpYTnpZV2RsVm1WeWMybHZiaUk2SWpJdU1pNHdJaXdpWTJoaGJHeGxibWRsUTI5dGNHeGxkR2x2YmtsdVpDSTZJbGtpTENKMGNtRnVjMU4wWVhSMWN5STZJbGtpTENKbFkya2lPaUl3TWlKOSJ9",
          "additionalInfo": {
            "authUdf1": "",
            "authUdf2": "",
            "authUdf3": "",
            "authUdf4": "",
            "authUdf5": "",
            "authUdf6": "",
            "authUdf7": "",
            "authUdf8": "",
            "authUdf9": "",
            "authUdf10": ""
          }
        }'
      ```
    </Accordion>

    ## Step 5: Check the response from PayU

    <Accordion title="Hash Validation Logic for Payment Response (Reverse Hashing)" icon="fa-code">
      While sending the response, PayU takes the exact same parameters that were sent in the request (in reverse order) to calculate the hash and returns it to you. You must verify the hash and then mark a transaction as a success or failure. This is to make sure the transaction has not tampered within the response.

      The order of the parameters is similar to the following code block:

      ```
      sha512(SALT|si_details|status||||||udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
      ```
    </Accordion>

    <Accordion title="Response parameters" icon="fa-code">
      For the response parameter description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis#response-for-initial-server-to-server-request).

      > 📘 Store the mihpayid and txnid parameter values in response:
      >
      > PayU recommends you to make provisions to store the **mihpayid** and **txnid** parameter values (in the response) in your server as proof that TPV has been completed for a customer.
    </Accordion>

    <Accordion title="Sample response" icon="fa-code">
      * Success scenario

      On receiving valid request over PayU's payment interface (\_payment), PayU returns JSON object as response object similar to the following in INTENT:

      ```
      {
         "metaData":{
            "message":null,
            "referenceId":"c5161bae370de1bd4fb886c6c66567a8",
            "statusCode":null,
            "txnId":"a7440cc636e747b635df",
            "txnStatus":"pending",
            "unmappedStatus":"pending"
         },
         "result":{
            "postToBank":{
               "useMethodGet":true
            },
            "issuerUrl":"https://api.payu.in/public/#/c5161bae370de1bd4fb886c6c66567a8/upiLoader"
         }
      }
      ```

      * Failure scenario

      ```
      {
         "metaData":{
            "message":"Transaction failed due to invalid params shared by the merchant",
            "referenceId":"dde7096af9db932a9fd09b9b4383d8be",
            "statusCode":"E1101",
            "txnId":"0c4931ddee7a4f69227f",
            "txnStatus":"failed",
            "unmappedStatus":"failure"
         },
         "result":{
            
         }
      }
      ```
    </Accordion>

    ## Step 6. Verify the payment

    Upon receiving the response, PayU recommends you performing a reconciliation step to validate all transaction details.

    You can verify your payments using either of the following methods:

    ### 1. Verify using Webhooks

    Configure the webhooks to monitor the status of payments. Webhooks enable a server to communicate with another server by sending an HTTP callback or message. These callbacks are triggered by specific events or instances and operate at the server-to-server (S2S) level.

    Know how to manage [Webhooks for Payments](https://docs.payu.in/reference/webhooks).

    ### 2. Verify using Verify Payments API

    **Environment**

    |                        |                                                                                                              |
    | :--------------------- | :----------------------------------------------------------------------------------------------------------- |
    | Test Environment       | [https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2) |
    | Production Environment | [https://info.payu.in/merchant/postservice.php?form=2](https://info.payu.in/merchant/postservice.php?form=2) |

    > Note: The hash logic for Verify Payment API is:
    > `sha512(key|command|var1|salt)`

    <Accordion title="Sample request" icon="fa-code">
      ```curl
      curl --request POST \
        --url 'https://test.payu.in/merchant/postservice?form=2' \
        --header 'Content-Type: application/x-www-form-urlencoded' \
        --data key=JPM7Fg \
        --data command=verify_payment \
        --data var1=IhfgcZnXR4o4nB \
        --data hash=a0ae79fdd66c875af6e9b21c4a67f1822deb00f2df5e9f0b1948f3222f536a9bf741b24efbb1874ca0f84f76b036e6c0d641581d0100f7abe4aeed2f3264f5c9
      ```
    </Accordion>
  </Tab>

  <Tab title="Collect Autopay TPV">
    ### Collect Autopay Workflow

    The merchant initiates the call to PayU with SI details, **bankcode** as **UPITPV**, and account number + IFSC details. PayU then initiates a mandate call with all the SI and account-related parameters to the bank. After the customer authorizes the mandate, the bank will validate the account. If the account details match, only then will the success notification be sent to PayU. However, if the account details do not match, Bank will pass validation error to PayU. Internally, Bank will cancel the mandate that has been set up on customer's account.

    > 📘 **Prerequisites**:
    >
    > S2S (Seamless) integration has to be done as per the standard kit. For more information, refer to [UPI Integrations - S2S](doc:upi-integrations-s2s).
    > **PayU Hosted Checkout note supported** Currently, PayU supports UPI Collect Autopay TPV Integration with Seamless integration only.

    ## Step 1: Validate VPA

    When your customer makes payment through UPI, you can validate the customer's Virtual Payment Address (VPA) and then initiate payment. The **validateVpa** API is used to validate the UPI handle. Validate the VPA (UPI handle) using the **validateVpa** API.  For Try-It experience of **validateVpa** API, refer to <Anchor label="Validate VPA Handle API" target="_blank" href="ref:validate_vpa_api">Validate VPA Handle API</Anchor>.

    <GENERALAPIsEnvironment />

    <Accordion title="Sample request" icon="fa-code">
      **Validate VPA**

      ```curl
      curl -X POST "https://test.payu.in/merchant/postservice?form=2" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&command=validateVPA&var1=9999999999@upi&hash=75bb573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472fff9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e"
      ```
    </Accordion>

    <Accordion title="Sample response" icon="fa-reply">
      **Success scenario**

      if successfully validated:

      ```plaintext
      {
         "status":"SUCCESS",
         "vpa":"9999999999@upi",
         "isVPAValid":1,
         "isAutoPayVPAValid":1,
         "isAutoPayBankValid":"NA",
         "payerAccountName":"ABC"
      }
      ```

      > 📘 Notes:
      >
      > * The **payerAccountName** parameter can be empty or NA or will have a payer name based on the value given by the bank.
      > * If both **isVPAValid** and **isAutoPayVPAValid** is 1, you must initiate payment for Recurring Payments.
      > * Ignore the **isAutoPayBankValid** parameter in the response.

      **Failure scenarios**

      * If invalid VPA, the response is similar to the following:

      ```plaintext
      {
       "status":"SUCCESS","vpa":"abc@upi","isVPAValid":0,"payerAccountName":"NA"
      }  
      ```

      * Invalid VPA but handle supporting SI (Autopay):

      ```plaintext
      {
       "status":"SUCCESS","vpa":"abc@upi","isVPAValid":0,"isAutoPayVPAValid":1,"isAutoPayBankValid":"NA","payerAccountName":"NA"
      }
      ```

      * Customer valid but handle not supporting SI (Autopay):

      ```plaintext
      {
        "status":"SUCCESS","vpa":"xyz@freecharge","isVPAValid":1,"isAutoPayVPAValid":0,"isAutoPayBankValid":"NA","payerAccountName":"XYZ"
      }
      ```

      * Neither customer valid nor handle supporting Autopay:

      ```plaintext
      {
        "status":"SUCCESS","vpa":"xyz@freecharge","isVPAValid":0,"isAutoPayVPAValid":0,"isAutoPayBankValid":"NA","payerAccountName":"NA"
      }
      ```
    </Accordion>

    <Accordion title="Sample validation JS code" icon="fa-reply">
      ```javascript
      	// JavaScript example for VPA validation before payment submission
      // This should be run on your server, not client-side

      async function validateVpa(vpa) {
          try {
              // Get hash from server endpoint
              const hashResponse = await fetch('/generate-vpa-hash', {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/json' },
                  body: JSON.stringify({ vpa })
              });
              const { hash } = await hashResponse.json();
              
              // Validate VPA with PayU
              const response = await fetch('https://test.payu.in/merchant/postservice?form=2', {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                  body: new URLSearchParams({
                      key: 'YOUR_MERCHANT_KEY',
                      command: 'validateVPA',
                      var1: vpa, // VPA to validate
                      hash: hash
                  })
              });
              
              const result = await response.json();
              
              // Sample response:
              // {"status":1,"msg":"VPA is valid","isVPAValid":1,"isUPIBarredBank":0}
              // OR
              // {"status":0,"msg":"VPA is invalid","isVPAValid":0}
              
              return {
                  isValid: result.isVPAValid === 1,
                  message: result.msg
              };
          } catch (error) {
              console.error('VPA validation error:', error);
              return { isValid: false, message: 'Validation service error' };
          }
      }

      ```
      ```curl
      # Once you have the hash, make the API call

      curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -d "key=YOUR_MERCHANT_KEY" \
        -d "command=validateVPA" \
        -d "var1=customer@upi" \
        -d "hash=$HASH"

      ```
    </Accordion>

    ## Step 2: Post the parameters to PayU

    With the following parameters, make the transaction request with the customer's bank account number to the PayU using the Collect Payment (**\_payment**) API.

    **Environment**

    | Environment            | URL                                                                 |
    | ---------------------- | ------------------------------------------------------------------- |
    | Test Environment       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
    | Production Environment | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |

    <Accordion title="Request parameters" icon="fa-code">
      In the merchant-initiated POST REQUEST, Hash is a mandatory parameter. It is critical to calculate the hash correctly and post it to PayU in the request.

      | Parameter                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Value                                                                                                                                           |
      | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
      | key <br /> `mandatory`               | `String` The merchant key is a unique identifier for a merchant account in PayU's database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Your Test Key                                                                                                                                   |
      | api\_version <br /> `optional`       | `String` The API version for this API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 7                                                                                                                                               |
      | txnid <br /> `mandatory`             | `String` The transaction ID is a reference number for a specific order that is generated by the merchant. It is used to track the order and must be unique. PayU's system will not accept duplicate transaction IDs.                                                                                                                                                                                                                                                                                                                                                                                                                   | s7hhDQVWvbhBdN                                                                                                                                  |
      | amount <br /> `mandatory`            | `String` This field should contain the payment amount for the transaction. The limit for recurring payments using UPI payment mode: \* **Auto-debit** is Rs.15000 (the auto-debit limit is higher for below listed purpose) \* **With PIN** is Rs.1,00,00 \* **Note**: The auto-debit limit for the following UPI recurring payments is one lakh rupees (Rs.1,00,000): \* Insurance premiums \* Credit card bill payments \* Insurance premium                                                                                                                                                                                         | 10.00                                                                                                                                           |
      | productinfo <br /> `mandatory`       | `String` It should be a string containing a brief description of the product. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | iPhone                                                                                                                                          |
      | firstname <br /> `mandatory`         | `String` The first name of the customer. `Character Limit-60`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Ashish                                                                                                                                          |
      | email <br /> `mandatory`             | `String` The email of the customer. `Character Limit-50`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [test@gmail.com](mailto:test@gmail.com)                                                                                                         |
      | phone <br /> `mandatory`             | `String` The phone number of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 9876543210                                                                                                                                      |
      | lastname <br /> `mandatory`          | `String` The last name of the customer. `Character Limit-60`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Verma                                                                                                                                           |
      | address1 <br /> `optional`           | `String` The first line of the billing address. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai                                                                                         |
      | address2 <br /> `optional`           | `String` The second line of the billing address. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 34 Saikripa-Estate, Tilak Nagar                                                                                                                 |
      | city <br /> `optional`               | `String` The city where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Mumbai                                                                                                                                          |
      | state <br /> `optional`              | `String` The state where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Maharashtra                                                                                                                                     |
      | country <br /> `optional`            | `String` The country where your customer resides. `Character Limit-50`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | India                                                                                                                                           |
      | zipcode <br /> `optional`            | `String` Billing address zip code is mandatory for the cardless EMI option. `Character Limit-20`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 400004                                                                                                                                          |
      | surl  <br /> `mandatory`             | `String` The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                       | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                  |
      | furl <br /> `mandatory`              | `String` The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                           | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                  |
      | hash <br /> `mandatory`              | `String` It is used to avoid the possibility of transaction tampering. For the hash checksum logic, refer to [Checksum Logic for Hash](#checksum-logic-for-hash).                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `eabec285da28fd 0e3054d41a4d24fe 9f7599c9d0b6664 6f7a9984303fd612 4044b6206daf831 e9a8bda28a6200d 318293a13d6c193 109b60bd4b4f8b09 c90972`      |
      | pg <br /> `mandatory`                | `varchar` The **pg** parameter for UPI must be UPI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | UPI                                                                                                                                             |
      | bankcode <br /> `mandatory`          | `varchar` This parameter contains UPITPV for UPI TPV Collect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | UPITPV                                                                                                                                          |
      | si <br /> `mandatory`                | This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                 |
      | si\_details <br /> `mandatory`       | This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU. \* **Note**: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers (for more details refer – [https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0)) This is a JSON object and it includes a set of fields. For more information, refer to [SI Parameter JSON Details](ref:si-parameter-json-details) |                                                                                                                                                 |
      | vpa <br /> `mandatory`               | `varchar` This parameter contains the customer's VPA handle. For the list UPI handles supported, refer to [UPI Handles](doc:upi-handles) The merchant is advised to check the validity of the VPA through using the VPA Validation API. PayU extends support for the same if required. For more information on using VPA Validation API, refer to [Validate VPA Handle API](ref:validate_vpa_api).                                                                                                                                                                                                                                     | abc\@upi                                                                                                                                        |
      | beneficiarydetail <br /> `mandatory` | This is a JSON format text and there should be key named **beneficiaryAccountNumber** with the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key). You can post up to five account details in this parameter.                                                                                                                                                                                                                                                                                                                  | Refer to [beneficiarydetail JSON Object Fields](https://docs.payu.in/docs/net-banking-integration-for-tpv#beneficiarydetail-json-object-fields) |
    </Accordion>

    <Accordion title="beneficiarydetail JSON Object Fields" icon="fa-code">
      It must contain the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key). You can post up to five account details in this parameter. For example:

      ```
      {"beneficiaryAccountNumber":"002001600674|00000031957292212|00000035955239352|00000035955239352",  
      "ifscCode":"KTKB0000046|KTKB0000023|KTKB0000035|KTKB0000035"}
      ```

      **Checksum Logic for Hash**

      The following hash logic must be used for the parameters posted:

      > 📘 si\_details parameter in Hashing:
      >
      > The **si\_details** parameter value will be at last or the last value to be appended.
      >
      > ```plaintext
      > key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3
      > |udf4|udf5||||||si_details|SALT
      > ```
    </Accordion>

    ## Step 3: Check the response from PayU

    <Accordion title="Hash Validation Logic for Payment Response (Reverse Hashing)" icon="fa-code">
      While sending the response, PayU takes the exact same parameters that were sent in the request (in reverse order) to calculate the hash and returns it to you. You must verify the hash and then mark a transaction as a success or failure. This is to make sure the transaction has not tampered within the response.

      The order of the parameters is similar to the following code block:

      ```
      sha512(SALT|si_details|status||||||udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
      ```
    </Accordion>

    <Accordion title="Response parameters" icon="fa-code">
      For the response parameter description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis#response-for-initial-server-to-server-request).

      > 📘 Store the mihpayid and txnid parameter values in response:
      >
      > PayU recommends you to make provisions to store the **mihpayid** and **txnid** parameter values (in the response) in your server as proof that TPV has been completed for a customer.
    </Accordion>

    <Accordion title="Sample response" icon="fa-code">
      * Success scenario

      On receiving valid request over PayU's payment interface (\_payment), PayU returns JSON object as response object similar to the following in COLLECT:

      ```
      {
         "metaData":{
            "message":null,
            "referenceId":"c5161bae370de1bd4fb886c6c66567a8",
            "statusCode":null,
            "txnId":"a7440cc636e747b635df",
            "txnStatus":"pending",
            "unmappedStatus":"pending"
         },
         "result":{
            "postToBank":{
               "useMethodGet":true
            },
            "issuerUrl":"https://api.payu.in/public/#/c5161bae370de1bd4fb886c6c66567a8/upiLoader"
         }
      }
      ```

      * Failure scenario

      ```
      {
         "metaData":{
            "message":"Transaction failed due to invalid params shared by the merchant",
            "referenceId":"dde7096af9db932a9fd09b9b4383d8be",
            "statusCode":"E1101",
            "txnId":"0c4931ddee7a4f69227f",
            "txnStatus":"failed",
            "unmappedStatus":"failure"
         },
         "result":{
            
         }
      }
      ```
    </Accordion>

    ## Step 4. Verify the payment

    <Verify_Payment_Tabs />
  </Tab>
</Tabs>

<br />