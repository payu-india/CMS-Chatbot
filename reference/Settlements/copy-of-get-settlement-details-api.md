---
title: Copy of Get Settlement Details API
deprecated: false
hidden: false
metadata:
  title: Get Settlement Details API
  description: >-
    This document provides information on using an API to retrieve settlement
    details from a bank based on a specified date or Unique Transaction
    Reference number. The API can be posted with version 1 or 2 parameters.
  robots: index
---
---
title: Get Settlement Details API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Get Settlement Details API
  description: >-
    This document provides information on using an API to retrieve settlement
    details from a bank based on a specified date or Unique Transaction
    Reference number. The API can be posted with version 1 or 2 parameters.
  robots: index
next:
  description: ''
---

You can use the **Get Settlement Details** API to retrieve settlement details which the bank has to settle for you. The input is the date for which settlement details are required, where the var1 parameter is the date you want to know the settlement status or UTR (Unique Transaction Reference number). This API can be posted with version (1 or 2) in the var5 parameter.

<Callout icon="📮" theme="default">
  **Postman Collection**: Access the **Get Settlement Details API Postman Collection** from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/bbccd36/getsettlementdetailsapi](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/bbccd36/getsettlementdetailsapi)
</Callout>

<br />

## Environment

| Environment            | URL                                                                                                        |
| :--------------------- | :--------------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://apitest.payu.in/merchant/postservice?form=2](https://apitest.payu.in/merchant/postservice?form=2) |
| Production Environment | [https://info.payu.in/merchant/postservice?form=2](https://info.payu.in/merchant/postservice?form=2)       |

## Request parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Reference
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key
        `mandatory`
      </td>

      <td>
        This parameter must contain the key provided by PayU. For more information on how to generate the Key and Salt, refer to [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard).
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        command
        `mandatory`
      </td>

      <td>
        This parameter must contain the API command as **get_settlement_details**.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        var1 `mandatory`
      </td>

      <td>
        This parameter must either contain either date for the settlement or UTR (Unique Transaction Reference number).
      </td>

      <td>
        2023-09-26
      </td>
    </tr>

    <tr>
      <td>
        var2 `mandatory`
      </td>

      <td>
        This parameter must contain the page number to be fetched.
      </td>

      <td>
        5
      </td>
    </tr>

    <tr>
      <td>
        var3 `mandatory`
      </td>

      <td>
        This parameter must contain the number of records to be paginated on each page is specified in this parameter. If not specified, 2000 records will be fetched.
      </td>

      <td>
        1000
      </td>
    </tr>

    <tr>
      <td>
        var4
        `optional`
      </td>

      <td>
        This parameter must contain either L or leave it blank.
      </td>

      <td>
        L
      </td>
    </tr>

    <tr>
      <td>
        var5
        `optional`
      </td>

      <td>
        This parameter must contain the version of the API that can be either 1 or 2.
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        hash `mandatory`
      </td>

      <td>
        Hash logic for this API is:
        sha512(key|command|var1|salt)sha512
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

## Example values

Use the following sample values while trying out the API:

* `var1` (date of the transaction/UTR number): 2020-10-26
* `var2`: 5
* `var3`: 2000 or more

## Sample request

### For version 1

```bash
curl -X POST "https://apitest.payu.in/merchant/postservice?form=2" \
-H "accept: application/json" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "key=JP***g&command=get_settlement_details&var1=2021-08-10&hash=259ded5457ad8d078b3c06294413680d0b9eb341682a4f0eecad17256388c2e096f37f5077480e3a56000cc0a3585f7cd73a7d2d10d8225a05b3b93cd27fd5f8"
```

### For version 2

```bash
curl -X POST "https://apitest.payu.in/merchant/postservice?form=2" \
-H "accept: application/json" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "key=JP***g&command=get_settlement_details&var1=2021-08-10&hash=259ded5457ad8d078b3c06294413680d0b9eb341682a4f0eecad17256388c2e096f37f5077480e3a56000cc0a3585f7cd73a7d2d10d8225a05b3b93cd27fd5f8&var2&var3&var4=L&var5=2"
```

<Callout icon="📘" theme="info">
  **Note**: The dates queried in the above requests using version 1 or version 2 are the same. The second sample request (under Sample Request for Version 2) includes the var5 parameter with the value 2 to indicate that it is for version 2.
</Callout>

## Response parameters description

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **Field**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        payuid
      </td>

      <td>
        This parameter contains a unique sale transaction id generated by Payu for every sale transaction.
      </td>

      <td>
        403993715521937565
      </td>
    </tr>

    <tr>
      <td>
        txn_id
      </td>

      <td>
        This parameter contains the sale transaction ID (merchant reference ID for sale).
      </td>

      <td>
        13818
      </td>
    </tr>

    <tr>
      <td>
        txn_date
      </td>

      <td>
        This parameter contains the date of the transaction.
      </td>

      <td>
        2021-08-10 23:46:25
      </td>
    </tr>

    <tr>
      <td>
        mode
      </td>

      <td>
        This parameter contains the mode of the transaction such as credit card, debit card, etc. For more information, refer to [Payment Mode Codes](doc:payment-mode-codes).
      </td>

      <td>
        CC
      </td>
    </tr>

    <tr>
      <td>
        amount
      </td>

      <td>
        This parameter contains the original amount which was sent in the transaction request by the merchant.
      </td>

      <td>
        100
      </td>
    </tr>

    <tr>
      <td>
        request_id
      </td>

      <td>
        This parameter contains the unique request id generated from PayU with any of the following transaction actions: capture/refund/chargeback/refundReversal/chargebackreversal actions actions.
      </td>

      <td>
        131278418
      </td>
    </tr>

    <tr>
      <td>
        requestdate
      </td>

      <td>
        This parameter contains the request date and time stamp.
      </td>

      <td>
        2021-08-10 23:49:16
      </td>
    </tr>

    <tr>
      <td>
        requestaction
      </td>

      <td>
        This parameter contains the action taken on the transaction. The action can be any of the following:

        * capture
        * refund
        * cancel
        * chargeback
        * chargeback reversal
        * refundreversal
      </td>

      <td>
        refund
      </td>
    </tr>

    <tr>
      <td>
        requestamount
      </td>

      <td>
        The parameter contains the amount requested by the merchant to the bank.
      </td>

      <td>
        100
      </td>
    </tr>

    <tr>
      <td>
        mer_UTR
      </td>

      <td>
        This parameter contains the merchant Unique Transaction Reference (UTR) number.
      </td>

      <td>
        N223211598444659
      </td>
    </tr>

    <tr>
      <td>
        mer_service_fee
      </td>

      <td>
        This parameter contains the service fee paid by the merchant to the bank. for the transaction
      </td>

      <td>
        239.6000
      </td>
    </tr>

    <tr>
      <td>
        mer_service_tax
      </td>

      <td>
        This parameter contains the tax on service fee paid by the merchant to the bank. for the transaction
      </td>

      <td>
        43.1300
      </td>
    </tr>

    <tr>
      <td>
        mer_net_amount
      </td>

      <td>
        This parameter contains the net amount to be settled by bank to merchant.
      </td>

      <td>
        100
      </td>
    </tr>

    <tr>
      <td>
        bank_name
      </td>

      <td>
        This parameter contains the bank name or the card type based on the transaction.
      </td>

      <td>
        MAST
      </td>
    </tr>

    <tr>
      <td>
        issuing_bank
      </td>

      <td>
        This parameter contains the card issuing bank name is displayed.
      </td>

      <td>
        SBI
      </td>
    </tr>

    <tr>
      <td>
        merchant_subvention_amount
      </td>

      <td>
        This parameter contains merchant subvention amount.
      </td>

      <td>
        100
      </td>
    </tr>

    <tr>
      <td>
        cgst
      </td>

      <td>
        This parameter contains the CGST (Central GST) for the transaction.
      </td>

      <td>
        43.13000
      </td>
    </tr>

    <tr>
      <td>
        igst
      </td>

      <td>
        This parameter contains the IGST (Integrated GST) for the transaction.
      </td>

      <td>
        43.13000
      </td>
    </tr>

    <tr>
      <td>
        sgst
      </td>

      <td>
        This parameter contains the SGST (State GST) for the transaction where the supplier or merchant is from a different state of the customer.
      </td>

      <td>
        43.13000
      </td>
    </tr>

    <tr>
      <td>
        PG_TYPE
      </td>

      <td>
        This parameter contains the payment gateway type is displayed in this transaction.
      </td>

      <td>
        HDFC_Internal_Plus
      </td>
    </tr>

    <tr>
      <td>
        Card Type
      </td>

      <td>
        This parameter indicates whether the card is international or domestic
      </td>

      <td>
        Domestic.
      </td>
    </tr>

    <tr>
      <td>
        SettlementType
      </td>

      <td>
        This describes about the charges whether its regular processing fee or instant charges
      </td>

      <td>
        Regular or Instant
      </td>
    </tr>

    <tr>
      <td>
        Scheme
      </td>

      <td>
        This parameter contains the scheme.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        FeeType
      </td>

      <td>
        This parameter contains fee type if the fee is collected for instant settlements or refunds.
      </td>

      <td>
        tdrFee
      </td>
    </tr>

    <tr>
      <td>
        InstantSettlementTDR
      </td>

      <td>
        This parameter contains the TDR collected for instant settlement.
      </td>

      <td>
        0.0
      </td>
    </tr>

    <tr>
      <td>
        InstantSettlementTDRTax
      </td>

      <td>
        This parameter contains the tax for the TDR collected for instant settlement.
      </td>

      <td>
        0.0
      </td>
    </tr>

    <tr>
      <td>
        InstantSettlementTdrType
      </td>

      <td>
        This parameter contains the TDR type for instant settlement.
      </td>

      <td>
        0.0
      </td>
    </tr>

    <tr>
      <td>
        InstantRefundTDR
      </td>

      <td>
        This parameter contains the TDR collected for instant refunds.
      </td>

      <td>
        0.0
      </td>
    </tr>

    <tr>
      <td>
        InstantRefundTDRTax
      </td>

      <td>
        This parameter contains the tax for the TDR collected for instant refunds.
      </td>

      <td>
        0.0
      </td>
    </tr>

    <tr>
      <td>
        InstantRefundTdrType
      </td>

      <td>
        This parameter contains the TDR type for instant refund.
      </td>

      <td>
        0.0
      </td>
    </tr>

    <tr>
      <td>
        perDayServiceFee
      </td>

      <td>
        This parameter contains the per day service fee for instant settlement or refunds.
      </td>

      <td>
        0,0
      </td>
    </tr>

    <tr>
      <td>
        perDayServiceTax
      </td>

      <td>
        This parameter contains the per day service tax for instant settlement or refunds.
      </td>

      <td>
        0,0
      </td>
    </tr>

    <tr>
      <td>
        pricingDays
      </td>

      <td>
        This parameter contains the pricing days for instant settlement or refunds.
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        offerServiceFee
      </td>

      <td>
        This parameter contains the service fee for offer.
      </td>

      <td>
        0,0
      </td>
    </tr>

    <tr>
      <td>
        offerServiceTax
      </td>

      <td>
        This parameter contains the tax for offer service fee.
      </td>

      <td>
        0,0
      </td>
    </tr>
  </tbody>
</Table>

## Sample response

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