---
api:
  file: cards-si-api.yaml
  operationId: post_payment
hidden: true
link:
  new_tab: false
metadata:
  robots: noindex
---
Initiates a card payment request and begins the 3DS authentication process for mandate creation. PayU selects the acquiring bank, submits the authentication initiation request, and returns an `acsTemplate` (Base64-encoded HTML) to redirect the customer to the OTP page.

After the customer submits the OTP, use the `bankData` from the OTP response (plus `siTokenDetails`) as `authentication_info` in the [`AuthorizeTransaction` API](doc:cards-si-step2-authorize-transaction).

***

## Authentication Flows

<Cards>
  <Card title="Flow 1 — New Card via PayU" icon="fa-credit-card">
    Send `auth_only=1`, `txn_s2s_flow=4`, `authentication_flow=REDIRECT`, and plain card details (`ccnum`, `ccname`, etc.).
  </Card>

  <Card title="Flow 2 — Saved Card via PayU" icon="fa-bookmark">
    Send `auth_only=1`, `txn_s2s_flow=4`, and `storecard_token_type=1` with a stored network token (`store_card_token`). `siTokenDetails` in the subsequent `AuthorizeTransaction` call is optional for this flow.
  </Card>

  <Card title="Flow 3 — Authentication Not via PayU" icon="fa-server">
    Send `txn_s2s_flow=3` with `authentication_info` already containing the 3DS result (`cavv`, `eci`, etc.) and `additional_info` with network token details. The mandate is registered in this single call.
  </Card>
</Cards>

***

## Hash Formula

```text Logic
SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|SALT)
```

<Callout icon="far fa-triangle-exclamation" theme="warn">
  ### **Important!**

  Use empty strings for any `udf` fields not included in the request. The serialised `si_details` JSON string occupies position 16 — after six trailing pipes following `udf5`.
</Callout>

***

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /merchant/postservice.php?form=2
  </Card>
</Cards>

***

## Environments

| Environment    | URL                               |
| :------------- | :-------------------------------- |
| **Test**       | `https://test.payu.in/_payment`   |
| **Production** | `https://secure.payu.in/_payment` |

***

## Flow 1: New Card Authentication via PayU

The merchant sends plain card details. PayU selects the acquirer, initiates 3DS authentication, and returns an `acsTemplate` for OTP redirect.

### Sample Requests

<Tabs>
  <Tab title="Request Payload">
    ```curl
    curl --location 'https://test.payu.in/_payment' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'key=vqpS7W' \
    --data-urlencode 'txnid=Txn080720261125' \
    --data-urlencode 'amount=100' \
    --data-urlencode 'productinfo=iPhone' \
    --data-urlencode 'firstname=Test User' \
    --data-urlencode 'email=test@gmail.com' \
    --data-urlencode 'phone=9876543210' \
    --data-urlencode 'surl=https://test.payu.in/admin/test_response' \
    --data-urlencode 'furl=https://test.payu.in/admin/test_response' \
    --data-urlencode 'api_version=7' \
    --data-urlencode 'hash=4a4074485ceacdb1093e7089655e327bd9a987f59daeab26d71a6f5011f6bb780c9a1fd26febcc00c091689887d8e0dbb0e17da16de9892658867a3d4deaa699' \
    --data-urlencode 'auth_only=1' \
    --data-urlencode 'termUrl=https://test.payu.in/admin/test_response' \
    --data-urlencode 's2s_client_ip=66.15.149.87' \
    --data-urlencode 's2s_device_info=Mozilla' \
    --data-urlencode 'authentication_flow=REDIRECT' \
    --data-urlencode 'txn_s2s_flow=4' \
    --data-urlencode 'pg=CC' \
    --data-urlencode 'bankcode=CC' \
    --data-urlencode 'ccnum=4761360079851258' \
    --data-urlencode 'ccname=test' \
    --data-urlencode 'ccexpmon=05' \
    --data-urlencode 'ccexpyr=28' \
    --data-urlencode 'ccvv=123' \
    --data-urlencode 'si=1' \
    --data-urlencode 'si_details={"billingAmount":"200.00","billingCurrency":"INR","billingCycle":"ADHOC","billingInterval":1,"paymentStartDate":"2026-07-08","paymentEndDate":"2099-01-01"}'
    ```
  </Tab>

  <Tab title="Parameter Description">
    Refer to the [Form Data](https://docs.payu.in/reference/post_merchant-webservice-service-php#body-params) section for request parameter description.
  </Tab>
</Tabs>

***

### Sample Response

<Tabs>
  <Tab title="Response Payload">
    PayU returns a JSON object with `txnStatus: "Enrolled"` and an `acsTemplate` field.<br />

    ```json
    {
        "metaData": {
          "message": null,
          "referenceId": "4e0d4a1b8f093f9bb03ed6e5605071b62ce39a9d136698d703862953a0106c24",
          "statusCode": null,
          "txnId": "Txn080720261125",
          "txnStatus": "Enrolled",
          "unmappedStatus": "pending"
        },
        "result": {
          "otpPostUrl": "",
          "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0Ii4uLg==",
          "binData": {
            "pureS2SSupported": false,
            "issuingBank": "YES",
            "category": "creditcard",
            "cardType": "VISA",
            "isDomestic": true
          }
        }
      }
    ```

    #### Handling the `acsTemplate`&#x20;

    Base64-decode the `acsTemplate` value to get an HTML page. Open this page in the customer's browser to redirect them to the card network OTP/authentication screen.<br />

    After the customer submits the OTP, a response is returned containing `bankData`. You will need this in [Step 2 — Authorization](doc:cards-si-step2-authorize-transaction).

    ```json Post-OTP response structure (bankData)
    {
          "referenceId": "4e0d4a1b8f093f9bb03ed6e5605071b62ce39a9d136698d703862953a0106c24",
          "cres": "eyJtZXNzYWdlVHlwZSI6IkNSZXMi...",
          "additionalInfo": {
            "authUdf1": "", "authUdf2": "", "authUdf3": "", "authUdf4": "", "authUdf5": "",
            "authUdf6": "", "authUdf7": "", "authUdf8": "", "authUdf9": "", "authUdf10": ""
          }
        }
    ```

    Add `siTokenDetails` to this object before passing it as `authentication_info` in Step 2.
  </Tab>

  <Tab title="Parameter Description">
    Refer to the [Responses](https://docs.payu.in/reference/post_merchant-webservice-service-php#response-schemas) section for response parameter description.
  </Tab>
</Tabs>

***

## Flow 2: Saved Card Authentication via PayU

The customer's card is already stored at the merchant's end from a previous transaction. The merchant uses the associated network token directly — the customer does not need to enter card details again.

### Sample Request

<Tabs>
  <Tab title="Request Payload">
    ```curl
    curl --location 'https://test.payu.in/_payment' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'key=vqpS7W' \
    --data-urlencode 'txnid=Txn030720261622' \
    --data-urlencode 'amount=100' \
    --data-urlencode 'productinfo=iPhone' \
    --data-urlencode 'firstname=Test User' \
    --data-urlencode 'email=test@gmail.com' \
    --data-urlencode 'phone=9876543210' \
    --data-urlencode 'surl=https://test.payu.in/admin/test_response' \
    --data-urlencode 'furl=https://test.payu.in/admin/test_response' \
    --data-urlencode 'api_version=7' \
    --data-urlencode 'hash=f2791c938b60cd7f06534d8efa296107c66c3a6f5116268d777d1f1d65d6c827ece56ff3517d09641dafaa88b157ecca2bbb1e4e6faca8f13e980628e204e034' \
    --data-urlencode 'auth_only=1' \
    --data-urlencode 'termUrl=https://test.payu.in/admin/test_response' \
    --data-urlencode 's2s_client_ip=66.15.149.87' \
    --data-urlencode 's2s_device_info=Mozilla' \
    --data-urlencode 'txn_s2s_flow=4' \
    --data-urlencode 'pg=CC' \
    --data-urlencode 'bankcode=CC' \
    --data-urlencode 'storecard_token_type=1' \
    --data-urlencode 'store_card_token=4761360079851258' \
    --data-urlencode 'additional_info={"last4Digits":"1234","tavv":"ABCDEFGH","trid":"1234567890","tokenRefNo":"abcde123456"}' \
    --data-urlencode 'ccexpmon=05' \
    --data-urlencode 'ccexpyr=28' \
    --data-urlencode 'si=1' \
    --data-urlencode 'si_details={"billingAmount":"200.00","billingCurrency":"INR","billingCycle":"ADHOC","billingInterval":1,"paymentStartDate":"2026-07-08","paymentEndDate":"2099-01-01"}'
    ```
  </Tab>

  <Tab title="Paramter Description">
    All parameters from Flow 1 apply. The following replaces or adds to the card-specific parameters:

    <Table align={["left","left"]}>
      <thead>
        <tr>
          <th>
            Parameter
          </th>

          <th>
            Description
          </th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td>
            `storecard_token_type` <br /> `mandatory`
          </td>

          <td>
            `Integer` Specifies the type of stored card token being used. Possible values:

            - `0`: PayU token&#x20;
            - `1`: Network token&#x20;
            - `2`: Issuer token&#x20;

              Set to `1` for network tokens.
          </td>
        </tr>

        <tr>
          <td>
            `store_card_token` <br /> `mandatory`
          </td>

          <td>
            `varchar` The stored network token value. Replaces the plain card number for saved card transactions. For example `4761360079851258`
          </td>
        </tr>

        <tr>
          <td>
            `additional_info` <br /> `mandatory`
          </td>

          <td>
            `JSON Object` Additional token metadata: `{"last4Digits":"1234","tavv":"ABCDEFGH","trid":"1234567890","tokenRefNo":"abcde123456"}`&#x20;

            - `last4Digits`: Last 4 digits of the original card. Mandatory for all transactions.&#x20;
            - `tavv`: Token Authentication Verification Value (cryptogram) from the network/scheme.&#x20;
            - `trid`: Token Requestor ID assigned by the network. Required for Diners and recommended for other networks.
            - `tokenRefNo`: Token Reference Number generated with the network token. Required for Diners.
          </td>
        </tr>

        <tr>
          <td>
            `ccnum` <br /> `not required`
          </td>

          <td>
            Omit this parameter for the saved card flow. Use `store_card_token` instead.
          </td>
        </tr>
      </tbody>
    </Table>
  </Tab>
</Tabs>

### Sample Response

The response for the saved card flow is identical in structure to Flow 1 — you receive a `txnStatus: "Enrolled"` response with an `acsTemplate`. Proceed to redirect the customer for OTP.<br />

The remaining steps (OTP page, `bankData` handling, and `AuthorizeTransaction`) are the same as Flow 1. Note that `siTokenDetails` is **optional** in the `AuthorizeTransaction` call when authentication is done via PayU for a saved card.

***

## Flow 3: Authentication Not via PayU

The merchant has already performed 3DS authentication externally (e.g., through their own ACS integration or a third-party). The merchant passes the 3DS result directly in the `_payment` request. The mandate is registered in this single call — no separate `AuthorizeTransaction` call is required.

### Sample Request

<Tabs>
  <Tab title="Sample Payload">
    ```curl
    curl --location 'https://test.payu.in/_payment' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'key=vqpS7W' \
    --data-urlencode 'txnid=1234455566111111' \
    --data-urlencode 'amount=100' \
    --data-urlencode 'productinfo=YOUR_REFERENCE_NUMBER' \
    --data-urlencode 'firstname=John' \
    --data-urlencode 'lastname=Smith' \
    --data-urlencode 'email=s.hopper@test.com' \
    --data-urlencode 'phone=1234567890' \
    --data-urlencode 'surl=https://test.adyen.com' \
    --data-urlencode 'furl=https://test.adyen.com' \
    --data-urlencode 'api_version=7' \
    --data-urlencode 'hash=8f158ff319ff023e92cc990d607c2e6a8ec725e799f31692320092f12904a1a081a705799b347c104220111b05dd0bd3d882b111eb01daf74c3a766a62f23b19' \
    --data-urlencode 'txn_s2s_flow=3' \
    --data-urlencode 'pg=CC' \
    --data-urlencode 'bankcode=CC' \
    --data-urlencode 'ccexpmon=05' \
    --data-urlencode 'ccexpyr=2028' \
    --data-urlencode 'ccvv=123' \
    --data-urlencode 'ccname=test' \
    --data-urlencode 'udf2=TestMerchant:355:visa' \
    --data-urlencode 'udf5=YOUR_REFERENCE_NUMBER' \
    --data-urlencode 'authentication_info={"cavv":"MTAwMjMyMDI2MTUxNzAwMDAwMDA5","eci":"02","flowType":"challenge","threeDSTransID":"2c75dd4a-c899-2f42-9081-19c4be594f97","threeDSServerTransID":"2c75dd4a-c899-2f42-9081-19c4be594f97","threeDSTransStatus":"Y"}' \
    --data-urlencode 'threeDS2RequestData={"deviceChannel":"BRW","threeDSVersion":"2.1.0"}' \
    --data-urlencode 'additional_info={"tavv":"ADcBA4ZHFQAgJRImEjklAAAAAAE=","par":"PN07d26452cf9a1696e2744f470377ec48d5","last4digits":"2656"}' \
    --data-urlencode 'store_card_token=5506900480000008' \
    --data-urlencode 'storecard_token_type=1' \
    --data-urlencode 'si=1' \
    --data-urlencode 'si_details={"billingAmount":"1000.00","billingCurrency":"INR","billingCycle":"ADHOC","billingInterval":1,"paymentStartDate":"2026-07-08","paymentEndDate":"2028-12-01"}'
    ```
  </Tab>

  <Tab title="Parameter Description">
    All base parameters (key, txnid, amount, productinfo, firstname, email, phone, surl, furl, api_version, hash, pg, bankcode, si, si_details) apply. The following are added or changed:

    <Table align={["left","left"]}>
      <thead>
        <tr>
          <th>
            Parameter
          </th>

          <th>
            Description
          </th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td>
            `txn_s2s_flow` <br /> `mandatory`
          </td>

          <td>
            `String` Set to **3** to indicate authentication was handled externally by the merchant.
          </td>
        </tr>

        <tr>
          <td>
            `authentication_info` <br /> `mandatory`
          </td>

          <td>
            `JSON Object` 3DS authentication result from the merchant's external authentication.&#x20;

            - `cavv`: Cardholder Authentication Verification Value.&#x20;
            - `eci`: Electronic Commerce Indicator.
            - `flowType`: 3DS flow type (e.g., `challenge`).
            - `threeDSTransID`: 3DS transaction ID from the ACS.
            - `threeDSServerTransID`: 3DS server transaction ID.&#x20;
            - `threeDSTransStatus`: Authentication status. `Y` = successful.
          </td>
        </tr>

        <tr>
          <td>
            `threeDS2RequestData` <br /> `mandatory`
          </td>

          <td>
            `JSON Object` 3DS2 device channel data.&#x20;

            - `deviceChannel`: `BRW` (browser).&#x20;
            - `threeDSVersion`: 3DS version used, e.g., `2.1.0`.
          </td>
        </tr>

        <tr>
          <td>
            `storecard_token_type` <br /> `mandatory`
          </td>

          <td>
            `Integer` Set to **1** for network token.
          </td>
        </tr>

        <tr>
          <td>
            `store_card_token` <br /> `mandatory`
          </td>

          <td>
            `varchar` The network token value for the card.
          </td>
        </tr>

        <tr>
          <td>
            `additional_info` <br /> `mandatory`
          </td>

          <td>
            `JSON Object` Network token metadata for the non-PayU auth flow.&#x20;

            - `tavv`: Token Authentication Verification Value.&#x20;
            - `par`: Payment Account Reference.&#x20;
            - `last4digits`: Last 4 digits of the tokenised card.
          </td>
        </tr>

        <tr>
          <td>
            `auth_only` <br /> `not required`
          </td>

          <td>
            Do not send `auth_only` for this flow. The mandate is registered directly in this call.
          </td>
        </tr>
      </tbody>
    </Table>
  </Tab>
</Tabs>

### Sample Response

<Tabs>
  <Tab title="Sample Payload">
    For Flow 3, the mandate is registered in this single call. The response contains the final transaction authorization result directly — check `IsStandingInstructionSet: "1"` and save `mihpayid` as your `authPayuId`.

    ```json
    {
        "status": "success",
        "result": {
          "mihpayid": "403993715537854832",
          "mode": "DC",
          "status": "success",
          "txnid": "1234455566111111",
          "amount": "100.00",
          "addedon": "2026-07-08 12:00:56",
          "productinfo": "YOUR_REFERENCE_NUMBER",
          "firstname": "John",
          "card_no": "XXXXXXXXXXXX2656",
          "error": "E000",
          "error_Message": "No Error",
          "issuing_bank": "AXIS",
          "card_type": "MAST",
          "AuthCode": "729577",
          "net_amount_debit": "100",
          "IsStandingInstructionSet": "1",
          "bank_ref_no": "519813603159458050",
          "PG_TYPE": "DC-PG",
          "payment_source": "sist"
        }
      }
    ```
  </Tab>

  <Tab title="Tab 2">

  </Tab>
</Tabs>
