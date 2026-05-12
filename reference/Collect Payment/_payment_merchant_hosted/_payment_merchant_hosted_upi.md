---
api:
  file: updated_upi_merchant_hosted.json
  operationId: MerchantHostedCheckout-UPI
hidden: false
metadata:
  title: Collect Payment using UPI - Merchant Hosted Checkout
  description: >-
    Discover comprehensive integration guides and API references for Merchant
    Hosted UPI payments with PayU. Learn how to seamlessly integrate UPI payment
    solutions into your website or app, enabling secure and efficient
    transactions for your customers.
  keywords:
    - UPI Merchant Hosted Checkout Collect Payment API
    - Simulator for PayU payment collection
    - UPI Custom Checkout integration with PayU
    - Collect payments using PayU API
    - Collect Payment API for UPI Merchant Hosted Checkout
    - _payment API for UPI Merchant Hosted Checkout
    - _payment API simulation for UPI Custom Checkout
    - _payment API simulation for UPI Merchant Hosted Checkout
---
PayU allows you to collect payments using UPI handles. For the list of UPI providers supported, refer to [UPI Handles](doc:upi-handles).

<NPCI_Mandate />

<Callout icon="👍" theme="okay">
  Experience the end-to-end **Merchant Hosted Checkout** > **UPI** flow and instantly generate the complete code for seamless, zero-coding integration into your website.

  <HTMLBlock>{`
                          <style>
                          .tooltip-btn {
                              position: relative;
                              background-color: #4CAF50;
                              color: white;
                              padding: 10px 20px;
                              border: none;
                              border-radius: 5px;
                              cursor: pointer;
                              font-weight: bold; /* Added this line */
                          }
                          .tooltip-btn:hover::after {
                              content: attr(data-tooltip);
                              position: absolute;
                              bottom: 125%;
                              left: 50%;
                              transform: translateX(-50%);
                              background-color: #333;
                              color: white;
                              padding: 5px 10px;
                              border-radius: 4px;
                              white-space: nowrap;
                              font-size: 12px;
                              z-index: 1;
                          }
                          </style>

                          <button onclick="window.open('https://payu.in/integrationlab/seamless/sm-upiflow', '_blank')" 
                                  class="tooltip-btn" 
                                  data-tooltip="Click here to see the Merchant Hosted Checkout >  UPI end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">
                              Experience the flow and get the code
                          </button>
  `}</HTMLBlock>
</Callout>

## Postman Collection

<Postman_collection />

<br />

### Recommended prerequisite before initiating payment

When your customer makes payment through UPI, you can validate the customer's Virtual Payment Address (VPA) and then initiate payment. The validateVpa API is used to validate the UPI handle.

Validate the VPA (UPI handle) using the validateVpa API.  For more information, refer to [Validate VPA Handle API](ref:validate_vpa_api).

<PaymentAPIEnvironment />

## Request parameters

### Additional info for request parameters

<Additional_paymentRequestParams />

> 📘 Reference
>
> For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

> 🚧 You can test UPI only with the anything@payu or [9999999999@payu.in](mailto:9999999999@payu.in) as VPA.

> ❗️ Error handling
>
> If any error message is displayed with an error code, refer to the <a href="error-codes" target="_blank">Error Codes</a> section to understand the reason for these error codes.
