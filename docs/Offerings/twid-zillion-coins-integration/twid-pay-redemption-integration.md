---
title: TWID Pay Redemption Integraiton
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
Integrate TWID pay to enable customers to redeem their TWID loyalty points during checkout. Follow these sequential steps to implement a complete TWID pay solution.

> 📘 Header-based authentication
>
> All the APIs mentioned in this section uses the following header-based authentication. Include the following headers in all API requests:
>
> ```http
> Authorization: Bearer {API_KEY}
> Content-Type: application/json
> X-Merchant-Key: {MERCHANT_KEY}
> ```

## API Integration Steps

<Accordion title="1. Fetch Balance API" icon="fa-search">
  Retrieve TWID points balance for a customer.
  **Endpoint**: `POST {{loyalty-service-url}}/v1/balance`

  <Accordion title="Request Parameters" icon="fa-table">
    | Parameter                 | Description                                                         | Example                                    |
    | ------------------------- | ------------------------------------------------------------------- | ------------------------------------------ |
    | loyaltyProvider           | `String` - The loyalty provider for the response                    | `"TWID"`                                   |
    | usableAmount              | `Number` - Maximum monetary amount that can be saved                | `500.0`                                    |
    | usablePoints              | `Number` - Required reward points for maximum savings               | `500`                                      |
    | title                     | `String` - Display title of the reward offer                        | `"Save Rs 500 using 500 TWID Cash Points"` |
    | earnConfig.points         | `Number` - Points that can be earned in this transaction            | `0`                                        |
    | issuerDetailDTO.brandName | `String` - Brand name of the issuer                                 | `"TWID Cash"`                              |
    | issuerDetailDTO.logo      | `String` - Logo URL of the brand or issuer                          | `"https://cdn.twidpay.com/..."`            |
    | holdApplicable            | `Boolean` - Indicates if points can be held/reserved for the reward | `false`                                    |
  </Accordion>

  <Accordion title="Sample Request" icon="fa-code">
    ```json
    {
      "loyaltyProvider": "TWID",
      "mobileNumber": "88001085**",
      "fetchRevisedEarn": true,
      "orderAmount": 1000
    }
    ```
  </Accordion>

  <Accordion title="Sample Response" icon="fa-reply">
    ```json
    {
      "loyaltyProvider": "TWID",
      "usableAmount": 500.0,
      "usablePoints": 500,
      "title": "Save Rs 500 using 500 twid Cash Points",
      "rewardId": 270943
    }
    ```
  </Accordion>
</Accordion>

<Accordion title="2. Hold TWID Coins API" icon="fa-lock">
  Hold/reserve TWID points for a transaction.
  **Endpoint**: `POST {{loyalty-service-url}}/payment/v1/createPayment`

  <Accordion title="Request Parameters" icon="fa-table">
    | Parameter                   | Description                                                    | Example                        |
    | --------------------------- | -------------------------------------------------------------- | ------------------------------ |
    | surl `optional`             | `String` - Success URL after holding points                    | `"http://api.payu.in/success"` |
    | furl `optional`             | `String` - Failure URL after holding points                    | `"http://api.payu.in/failure"` |
    | merchantKey `mandatory`     | `String` - PayU merchant key for authentication                | `"18001"`                      |
    | parentPayuTxnId `mandatory` | `String` - Parent transaction ID from main payment transaction | `"65646400234509041"`          |
    | totalAmount `mandatory`     | `Number` - Total monetary reward amount to be held/redeemed    | `1000`                         |
    | mobile `mandatory`          | `String` - User's mobile number                                | `"9304204**"`                  |
    | loyaltyProvider `mandatory` | `String` - Loyalty provider identifier                         | `"TWID"`                       |
    | orderAmount `mandatory`     | `Number` - Total order/bill amount for transaction             | `10000`                        |
  </Accordion>

  <Accordion title="Sample Request" icon="fa-code">
    ```json
    {
      "surl": "http://api.payu.in/success",
      "furl": "http://api.payu.in/failure",
      "merchantKey": "18001",
      "parentPayuTxnId": "65646400234509041",
      "totalAmount": 1000,
      "mobile": "9304204**",
      "email": "test@gmail.com",
      "loyaltyProvider": "TWID",
      "rewardId": 270940,
      "currency": "INR",
      "orderAmount": 10000
    }
    ```
  </Accordion>

  <Accordion title="Sample Response" icon="fa-reply">
    ```json
    {
      "statusCode": 1,
      "status": "PENDING",
      "loyaltyTxnId": "d1dce98d-98ec-4b90-a7d8-853fee82a113"
    }
    ```
  </Accordion>
</Accordion>

<Accordion title="3. Redeem TWID Points API" icon="fa-check-circle">
  Complete the redemption of held TWID points.
  **Endpoint**: `POST {{loyalty-service-url}}/payment/v1/continue`

  <Accordion title="Request Parameters" icon="fa-table">
    | Parameter                   | Description                                                                            | Example                                  |
    | --------------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------- |
    | loyaltyTxnId `mandatory`    | `String` - Reference ID provided by the Loyalty-Service during the Create Payment call | `"bd1a77b6-1596-46e1-b79f-2770bcb636c7"` |
    | loyaltyProvider `mandatory` | `String` - The loyalty provider identifier (e.g., TWID)                                | `"TWID"`                                 |
  </Accordion>

  <Accordion title="Sample Request" icon="fa-code">
    ```json
    {
      "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
      "loyaltyProvider": "TWID"
    }
    ```
  </Accordion>

  <Accordion title="Sample Response" icon="fa-reply">
    ```json
    {
      "status": "SUCCESS",
      "loyaltyTxnId": "1821b1e2-34dd-47e3-9b54-b56b9d352a6b",
      "rewardPartnerRefId": "7251637276230479872"
    }
    ```
  </Accordion>
</Accordion>

<Accordion title="4. Transaction Enquiry API (Optional)" icon="fa-search-plus">
  Query the status and details of TWID transactions.
  **Endpoint**: `POST {{loyalty-service-url}}/payment/v1/enquiry`

  <Accordion title="Request Parameters" icon="fa-table">
    | Parameter               | Description                                                                         | Example                                  |
    | ----------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------- |
    | loyaltyTxnId `optional` | `String` - Reference ID generated during Create Payment or Redeem TWID Points calls | `"bd1a77b6-1596-46e1-b79f-2770bcb636c7"` |
    | payuTxnId `optional`    | `String` - PayU transaction ID                                                      | `"89887897898"`                          |

    **Note**: At least one parameter must be provided
  </Accordion>

  <Accordion title="Sample Request" icon="fa-code">
    ```json
    {
      "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
      "payuTxnId": "89887897898"
    }
    ```
  </Accordion>

  <Accordion title="Sample Response" icon="fa-reply">
    ```json
    {
      "status": "SUCCESS",
      "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
      "payuTxnId": "89887897898"
    }
    ```
  </Accordion>
</Accordion>

<br />
