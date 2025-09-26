---
title: Test
deprecated: false
hidden: true
metadata:
  robots: index
---
|                                                                                                                   |                                                                                                              |                                                                                                             |
| :---------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- |
| ![](https://files.readme.io/852ff36002aae339313722c8832cc7b5443c1bf7e5ca47571e9dd6971d51a2ae-netbanking_icon.png) | ![](https://files.readme.io/049c1e19c22dc0dee8f0f2b0a7facd89231c96a6b86d188af824cf1e87154d8e-cards_icon.png) | ![](https://files.readme.io/f5fe8045de9902d7ed2d1bb0a31568151638acaba086331df01826e0a4ebe1f2-upi_icon.png)  |
| ![](https://files.readme.io/0af7178db0a6130d39fb7b5270109e4251b0fd1b1455e54a936f29c145a97c87-wallets_icon.png)    | ![](https://files.readme.io/e32726065ea0eb0243a5c47583c54908d2f0732ea259206bae93f113f5284d52-emi_icon.png)   | ![](https://files.readme.io/04bb870171161dcaaa5363972d8d0277441ed578ce84d3c62c7bda91a421643d-bnpl_icon.png) |
| ![](https://files.readme.io/9392c375fc2fccecae588e5c287466be6cda1b0f039ace7a6f4139959e991189-neft_icon.png)       |                                                                                                              |                                                                                                             |

<br />

# Merchant Hosted Parameters — Simplified, Skimmable MDX

> **Environments**
> Test: `https://test.payu.in/_payment` · Production: `https://secure.payu.in/_payment`

<Accordion title="Step 1.2 · Prepare the Request Parameters" icon="fa-list-check" defaultOpen>
  ## Quick payload (minimum to charge)

  * `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`
  * `pg` (payment method) + `bankcode` (where applicable)
  * `surl`, `furl`
  * `hash` (server-side SHA-512 only)

  > **Tip:** Generate the `hash` **on your server**. Never compute it client-side.

  ***

  ## Common parameters (for all modes)

  | Field         | Required    | Type / Limits                | When required                                    | Example                          |
  | ------------- | ----------- | ---------------------------- | ------------------------------------------------ | -------------------------------- |
  | `key`         | Yes         | String                       | Always                                           | `JPG****.k`                      |
  | `txnid`       | Yes         | String (≤25)                 | Always                                           | `TXN_12345`                      |
  | `amount`      | Yes         | Decimal string               | Always                                           | `10.00`                          |
  | `productinfo` | Yes         | String (≤100)                | Always                                           | `iPhone 13`                      |
  | `firstname`   | Yes         | String (≤60 prod / ≤20 test) | Always                                           | `Ashish`                         |
  | `email`       | Yes         | String (≤50)                 | Always                                           | `user@example.com`               |
  | `phone`       | Yes         | String (≤50)                 | Always                                           | `9876543210`                     |
  | `pg`          | Yes         | Enum                         | Always; selects payment method                   | `CC`, `NB`, `UPI`, `EMI`, `BNPL` |
  | `bankcode`    | Conditional | String                       | Required by methods that need provider/bank code | `VISA`, `HDFC`, `UPI`            |
  | `surl`        | Yes         | URL (≤50)                    | Always                                           | `https://yoursite.com/success`   |
  | `furl`        | Yes         | URL (≤50)                    | Always                                           | `https://yoursite.com/failure`   |
  | `hash`        | Yes         | SHA-512                      | Always (server-computed)                         | *(server value)*                 |
  | `udf1`…`udf5` | No          | String                       | Optional metadata you can echo back              | `channel=web`                    |

  ***

  ## pg / bankcode quick mapping

  | Method     | `pg`   | Example `bankcode` values                          |
  | ---------- | ------ | -------------------------------------------------- |
  | Cards      | `CC`   | `VISA`, `MAST`, `AMEX`, `DINERS`, `RUPAY`, `MAES`  |
  | NetBanking | `NB`   | Bank short codes (e.g., `HDFC`, `ICIC`, `SBIN`, …) |
  | UPI        | `UPI`  | `UPI` (provider-specific when applicable)          |
  | EMI        | `EMI`  | Issuer/bank short codes + tenure per issuer        |
  | BNPL       | `BNPL` | Provider/tenure codes per BNPL partner             |
</Accordion>

***

<Tabs items={['Cards','NetBanking','UPI','EMI','BNPL']}>
  <Tab value="Cards">
    ### Additional parameters

    | Field      | Required | Notes                 |
    | ---------- | -------- | --------------------- |
    | `ccnum`    | Yes      | 13–19 digits          |
    | `ccname`   | Yes      | Name on card          |
    | `ccvv`     | Yes      | 3 digits (4 for AMEX) |
    | `ccexpmon` | Yes      | `MM`                  |
    | `ccexpyr`  | Yes      | `YYYY`                |

    #### Minimal payload diff

    * `pg=CC`
    * `bankcode=<card_network>` (e.g., `VISA`)
    * Add `ccnum`, `ccexpmon`, `ccexpyr`, `ccvv`, `ccname`

    #### Sample request (cURL)

    ```bash
    curl -X POST "https://test.payu.in/_payment" \
      -H "Content-Type: application/x-www-form-urlencoded" \
      -d "key=YOUR_KEY" \
      -d "txnid=TXN_12345" \
      -d "amount=1000.00" \
      -d "productinfo=Product" \
      -d "firstname=Name" \
      -d "email=user@example.com" \
      -d "phone=9988776655" \
      -d "pg=CC" \
      -d "bankcode=VISA" \
      -d "ccnum=4111111111111111" \
      -d "ccexpmon=12" \
      -d "ccexpyr=2026" \
      -d "ccvv=123" \
      -d "ccname=JOHN DOE" \
      -d "surl=https://merchant.site/success" \
      -d "furl=https://merchant.site/failure" \
      -d "hash=SERVER_COMPUTED_HASH"
    ```
  </Tab>

  <Tab value="NetBanking">
    ### Additional parameter

    * `bankcode` (Mandatory): bank short code (e.g., `HDFC`, `ICIC`, …)

    #### Minimal payload diff

    * `pg=NB`
    * `bankcode=<BANK_SHORT_CODE>`
  </Tab>

  <Tab value="UPI">
    ### Notes

    * Use `bankcode=UPI`.
    * Depending on sub-flow (collect, intent, in-app), additional fields may apply per your enablement.

    #### Minimal payload diff

    * `pg=UPI`
    * `bankcode=UPI`
  </Tab>

  <Tab value="EMI">
    ### Notes

    * Use `pg=EMI`.
    * `bankcode` denotes issuer/bank and may encode tenure depending on configuration.

    #### Minimal payload diff

    * `pg=EMI`
    * `bankcode=<EMI_ISSUER/TENURE_CODE>`
  </Tab>

  <Tab value="BNPL">
    ### Notes

    * Use `pg=BNPL`.
    * `bankcode` is the BNPL provider code; some partners require tenure in the code.

    #### Minimal payload diff

    * `pg=BNPL`
    * `bankcode=<BNPL_PROVIDER/_TENURE>`
  </Tab>
</Tabs>

***

### Validation & security checklist

* Always compute `hash` on the server before POSTing to PayU.
* Validate success by verifying the response `hash` on your server before fulfilling the order.
* Use HTTPS return URLs (`surl`, `furl`) and handle idempotency on success callbacks.

***

### Troubleshooting tips

* **Payment method not showing?** Ensure `pg` and a valid `bankcode` are posted and that the method is enabled on your MID.
* **Invalid hash?** Check field order and delimiter; verify that you’re using the correct Salt for the environment.
* **UPI in Test?** Some UPI flows may be limited or unavailable in Test environment.
