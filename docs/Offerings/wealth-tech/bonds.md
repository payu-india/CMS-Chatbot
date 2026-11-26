---
title: Bonds
excerpt: >-
  Collect bond payments as an Online Bond Platform Provider (OBPP) through PayU.
  Send bond details in a product object. PayU settles to NSE Clearing.
deprecated: false
hidden: true
metadata:
  robots: index
---
## Overview

Collect bond payments as an Online Bond Platform Provider (OBPP). With each payment request, you send the bond details in a `products` object. PayU uses these details to report the payment to NSE Clearing Ltd (NCL).

<Callout icon="⚠️" theme="warning">
  ### Settlement goes to NSE Clearing, not to your account

  PayU settles every bond payment directly to NSE Clearing Ltd (NCL). You do not receive the funds in your merchant bank account.
</Callout>

1. You place the bond order on the exchange.
2. You send the payment request to PayU with the customer's bank account details and the `products` object.
3. PayU collects the payment from the verified bank account of the customer (TPV).
4. PayU settles the funds to NSE Clearing Ltd (NCL). PayU supports bond payments through NSE only.

<Callout icon="⚠️" theme="warning">
  ### Before you start

  - Ask your PayU Key Account Manager (KAM) to set your merchant type to **Bonds (OBPP)**.
  - Register a validated UPI handle on the SEBI portal. Use the `.brk` suffix with the `@valid` handle. Example: `<merchant>.payu1.brk@validaxis`.
  - Use a separate UPI handle for UPI Autopay — the same handle cannot be used for both.
  - **Accepted payment modes:** UPI, UPI Autopay, eNACH, and Net Banking only.
  - **TPV is mandatory.** Send the customer's bank account and IFSC in `beneficiarydetail` with every request.
  - **Refunds are not available.** Direct customers with a dispute to the [PayU care channel](https://help.payu.in/query).
</Callout>

***

## Payment Request (Lump Sum)

Send a `POST` request with form data (`application/x-www-form-urlencoded`).

**Environments**

| Environment | Endpoint                          |
| ----------- | --------------------------------- |
| Test        | `https://test.payu.in/_payment`   |
| Production  | `https://secure.payu.in/_payment` |

<Accordion title="Request Parameters" icon="far fa-table">
  | Parameter                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
  | :----------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | key<br />`mandatory`                       | `String` This parameter is the unique merchant key provided by PayU for your merchant account. For more information, refer to [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard).                                                                                                                                                                                                                                                                                                                                                                                                                        |
  | txnid<br />`mandatory`                     | `Varchar` This parameter is known as Transaction ID (or OrderID). It is the order reference number generated at your (Merchant's) end. It is an identifier which you(merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of same Transaction ID again would fail. Hence, it is essential that you post us a unique transaction ID for every new transaction (Please make sure that the transaction ID being sent to us hasn't been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID'). |
  | amount<br />`mandatory`                    | `float` This parameter should contain the payment amount of the particular transaction. Note: Type-cast the amount to float type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  | productinfo<br />`mandatory`               | `Varchar` This parameter should contain a brief product description. It should be a string describing the product (The description type is entirely your choice).                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
  | firstname<br />`mandatory`                 | `Varchar` This parameter must contain the first name of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
  | email<br />`mandatory`                     | `Varchar` This parameter must contain the email of the customer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
  | phone<br />`mandatory`                     | `Integer` Merchant needs to take the customer's GPay registered phone number and pass in this field. This field will be used for further mapping the customer VPA and initiate a collect request.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
  | surl<br />`mandatory`                      | `string` The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                             |
  | furl<br />`mandatory`                      | `String` The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
  | api_version <br /> `mandatory`             | API version must be posted as `21`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
  | hash<br />`mandatory`                      | `String` The hash calculated by the merchant using the key and salt provided by PayU. The format for calculating the hash: sha(key\\\|txnid\\\|amount\\\|productinfo\\\|firstname\\\|email\\\|udf1\\\|udf2\\\|udf3\\\|udf4\\\|udf5\\\|\\\|\\\|\\\|\\\|                                                                                                                                                                                                                                                                                                                                                                                       |
  | products <br />`mandatory for Wealth Tech` | `JSON` This parameter contains various fields including the Wealth Tech object (**wtParams**). For more information on wtParams object field, refer to the [Bond Product Object](https://docs.payu.in/docs/bonds#bond-product-object) section.                                                                                                                                                                                                                                                                                                                                                                                               |
  | beneficiarydetail<br />`mandatory `        | `String` String JSON object that contains account numbers and corresponding IFSC codes (max 4 accounts) in the same order                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
  | lastname<br />`optional`                   | `String` The last name of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
  | address1<br />`optional`                   | `String` The first line of the billing address                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  | address2<br />`optional`                   | `String` The second line of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  | city<br />`optional`                       | `String` The city where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
  | state<br />`optional`                      | `String` The state where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  | country<br />`optional`                    | `String` The country where your customer resides.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
  | zipcode<br />`optional`                    | `String` Billing address zip code is mandatory for the cardless EMI option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
  | udf1<br />`optional`                       | `String` This parameter has been made for you to keep any information corresponding to the transaction.<br /> **Note**: This parameter must contain buyer's PAN number for Cross-Border Payments.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
  | udf2<br />`optional`                       | `string` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
  | udf3<br />`optional`                       | `String` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
  | udf4<br />`optional`                       | `String` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
  | udf5<br />`optional`                       | `String` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
</Accordion>

### Hash Formula

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|beneficiarydetail|si_details|user_token|offer_key|offer_auto_apply|cart_details|products|SALT)
```

Leave a field empty in the hash string if you do not send it. Keep the `|` separators.

### `beneficiarydetail` Format

Send up to 4 bank accounts. Separate multiple account numbers with `|` and send the IFSC codes in the same order.

```json
{
  "beneficiaryAccountNumber": "1579105002472|50100650144897",
  "ifscCode": "HDFC0001579|HDFC0000145"
}
```

### Sample Request

```curl
curl -i 'https://test.payu.in/_payment' \
-H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \
-H 'content-type: application/x-www-form-urlencoded' \
--data-urlencode 'key=KOEfPI' \
--data-urlencode 'txnid=7f41f520f71b' \
--data-urlencode 'amount=50000' \
--data-urlencode 'productinfo=Mutual Fund' \
--data-urlencode 'firstname=John' \
--data-urlencode 'email=john@example.com' \
--data-urlencode 'phone=9876543210' \
--data-urlencode 'surl=https://apiplayground-response.herokuapp.com/' \
--data-urlencode 'furl=https://apiplayground-response.herokuapp.com/' \
--data-urlencode 'api_version=21' \
--data-urlencode 'hash=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0' \
--data-urlencode 'products={"wtParams":[{"type":"bond","amount":"101.00","receipt":"1234556789012","mf_member_id":"12345","mf_user_id":"77407","mf_partner":"nse_bonds","mf_investment_type":"L"}]}'
```

***

## Recurring Debit (UPI Autopay or eNACH)

Use this call to debit a registered mandate. Mandate registration and pre-debit notification follow the standard PayU SI flow — no changes are needed for bonds.

**Environments**

| Environment | Endpoint                                               |
| ----------- | ------------------------------------------------------ |
| Test        | `https://test.payu.in/merchant/postservice.php?form=2` |
| Production  | `https://info.payu.in/merchant/postservice.php?form=2` |

<Accordion title="Request Parameters" icon="far fa-table">
  | Parameter | Required | Description                                                                           |
  | --------- | -------- | ------------------------------------------------------------------------------------- |
  | `key`     | Yes      | Your merchant key.                                                                    |
  | `command` | Yes      | Set to `si_transaction`.                                                              |
  | `var1`    | Yes      | JSON with the debit details. Place the product object inside `more_info[0].wtParams`. |
  | `hash`    | Yes      | `sha512(key\|command\|var1\|SALT)`                                                    |
</Accordion>

### `var1` Sample

```json
{
  "authpayuid": "999990000005920",
  "amount": "101.00",
  "txnid": "a79d6318-afcb-4a87-820c-681b53215866",
  "invoiceDisplayNumber": "f53edcd3-7c08-49d6-9a2f-e67e4dc4eea7",
  "more_info": [
    {
      "wtParams": [
        {
          "type": "bond",
          "amount": "101.00",
          "receipt": "1234556789012",
          "mf_member_id": "12345",
          "mf_user_id": "77407",
          "mf_partner": "nse_bonds",
          "mf_investment_type": "L"
        }
      ]
    }
  ]
}
```

### Sample Response

```json
{
  "status": 1,
  "message": "Transaction Processed successfully",
  "details": {
    "a79d6318-afcb-4a87-820c-681b53215866": {
      "authpayuid": "999990000005920",
      "transactionid": "a79d6318-afcb-4a87-820c-681b53215866",
      "amount": "101.00",
      "payuid": "999990000006473",
      "status": "captured",
      "field9": "Transaction is Successful",
      "addedon": "2025-09-03 10:40:19"
    }
  }
}
```

***

## Bond Product Object

Send exactly one product object per payment request. PayU rejects a request with more than one object for bonds. All values are case-sensitive.

| Parameter                                          | Required | Format                                    | Description                                    |
| -------------------------------------------------- | -------- | ----------------------------------------- | ---------------------------------------------- |
| `type`                                             | Yes      | String                                    | Must be `bond`.                                |
| `mf_partner`                                       | Yes      | String                                    | Must be `nse_bonds`.                           |
| `amount`                                           | Yes      | Numeric string — e.g. `5000` or `5000.50` | Must be equal to the order `amount`.           |
| `receipt`                                          | Yes      | Alphanumeric, max. 25 characters          | Your unique reference number for this payment. |
| `mf_member_id`                                     | Yes      | Max. 20 characters                        | Your member ID on the exchange.                |
| `mf_user_id`                                       | Yes      | Alphanumeric, max. 10 characters          | Unique client code (UCC) of the customer.      |
| `mf_investment_type`                               | Yes      | `L`                                       | Send `L` (lump sum).                           |
| `plan`, `option`, `scheme`, `folio`, `mf_amc_code` | No       | String                                    | Not used for bonds. You can omit these fields. |

```json Products Object Sample
{
   "wtParams":[
      {
         "type":"bond",
         "amount":"1000.00",
         "receipt":"77407",
         "mf_member_id":"12345",
         "mf_user_id":"77407",
         "mf_partner":"nse_bonds",
         "mf_investment_type":"L"
      }
   ]
}
```

***

## Check Response from PayU

<Accordion title="Success Response" icon="fa-exchange">
  ```plaintext
  mihpayid=403993715537000168&mode=UPI&status=success&key=j6Bb3k&txnid=txn_7798908nnm008&amount=50000.00&addedon=2026-03-17 14:48:25&productinfo=iphone&firstname=Sumit&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test@gmail.com&phone=7715995865&udf1=&udf2=&udf3=&udf4=Executed Callback&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&card_token=&card_no=&field0=&field1=9999999999@upi&field2=&field3=ps@paytm&field4=&field5=403993715537000168&field6=&field7=00|APPROVED OR COMPLETED SUCCESSFULLY&field8=&field9=Transaction Successful|Completed Using Callback&payment_source=sist&cardToken=&authenticaticationMethod=&PG_TYPE=NB-PG&error=E000&error_Message=No Error&net_amount_debit=50000&discount=0.00&offer_key=&offer_availed=&unmappedstatus=captured&hash=833ca55940bf5fa7ef6d334872848d4ad2ec775966aba23a8c3e82ecf5292ea7bd3e9573202ee093fdbc91dedd1cd6ff919411d84bce76c8cb676921cc997191&bank_ref_no=ICI9TI0Y06S0HCGA1DDHTN3ZH7YL0MPYBRUQ&bank_ref_num=ICI9TI0Y06S0HCGA1DDHTN3ZH7YL0MPYBRUQ&bankcode=INTENT&surl=https://test.payu.in/admin/test_response&curl=https://test.payu.in/admin/test_response&furl=https://test.payu.in/admin/test_response&IsStandingInstructionSet=1
  ```
</Accordion>

<Accordion title="Hash Verification" icon="fa-key">
  Verify response using reverse hash calculation:

  ```
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  <Callout icon="fad fa-toolbox" theme="okay">
    ### **PayU Hash Verification Tool**

    PayU recommends you to use the PayU Hash Verification Tool to validate the reverse hashing. For more information, refer to [Using PayU Hash Verification Tool](doc:using-payu-hash-verification-tool)
  </Callout>
</Accordion>

<Callout icon="📘" theme="info">
  ### **Tips:**

  Do not include `beneficiarydetail` in the response hash formula.
</Callout>

### Verify the Payment

<Verify_Payment_Tabs />

***

## Errors

PayU stops at the first failed check and returns one error. For a payment request, PayU sends the error to your `furl`. For a recurring debit, PayU returns the error in the response.

| Condition                                              | Error message                                                                               |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| A required field is missing                            | `Mandatory parameter '<field>' is missing`                                                  |
| `type` is not a valid value                            | `Type must be one of: mutual_fund, bond`                                                    |
| `mf_partner` is not a valid value                      | `mf_partner '<value>' is invalid. Allowed values: bse, bse2, nse_mf, nse_bonds, kfin, cams` |
| `mf_partner` is not `nse_bonds` for your merchant type | `"mf_partner" value is not allowed for this merchant`                                       |
| More than one product object                           | `Multi-product array is not allowed for this merchant`                                      |
| Product `amount` does not equal order `amount`         | `Sum of product amounts (<total>) does not match order amount (<order_amount>)`             |