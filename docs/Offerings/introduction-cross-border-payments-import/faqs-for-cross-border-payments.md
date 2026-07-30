---
title: FAQs for Cross-Border Payments
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
---
title: FAQs for Cross-Border Payments
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
## General

<Accordion title="1. What is the purpose of Cross-Border Payments Import?" icon="fa-info-circle">
  Cross-Border Payments Import enables you to accept and process cross-border payments from customers around the world. This feature allows your business to expand its reach and tap into new international markets.
</Accordion>

<Accordion title="2. What is the OPGSP Integration and why is it important for cross-border payments?" icon="fa-info-circle">
  The OPGSP (Online Payment Gateway Service Providers) Integration is the process of connecting your website or online store to the PayU payment gateway for cross-border payments. It is important for cross-border payments because it enables merchants to accept and process payments from customers in different countries and currencies.
</Accordion>

<Accordion title="3. What are the requirements for integrating with PayU for cross-border payments?" icon="fa-info-circle">
  To integrate with PayU for cross-border payments, you will need to have a website or online store that is capable of accepting payments through the PayU payment gateway and follow the RBI guidelines. For more information on RBI guidelines, refer to [RBI Guidelines](doc:rbi-guidelines-for-cross-border-payments).
</Accordion>

<Accordion title="4. What currencies does PayU accept for Cross-Border Payments?" icon="fa-info-circle">
  PayU supports a wide range of currencies, including the following:

  * U.S. Dollar (USD)
  * European Dollar (EUR)
  * Pound Sterling (GBP)
  * Indian Rupee (INR)
</Accordion>

<Accordion title="5. How does PayU handle currency conversion for cross-border payments?" icon="fa-info-circle">
  PayU uses real-time exchange rates to convert currencies for cross-border payments. The exchange rates are updated regularly to ensure accuracy and transparency for both merchants and customers.
</Accordion>

<Accordion title="6. How does PayU ensure the security of my transactions?" icon="fa-info-circle">
  PayU uses state-of-the-art security measures to ensure the safety and security of all transactions processed through its platform. This includes encryption, fraud detection and prevention, and compliance with industry standards and regulations.
</Accordion>

<Accordion title="7. What fees does PayU charge for its Cross-Border Payment services?" icon="fa-info-circle">
  PayU charges a processing fee for each transaction processed through its platform. The exact fee varies depending on a number of factors, including the type of payment, the currency, and the country in which the transaction takes place. You can contact your PayU Key Account Manager (KAM) for more details.
</Accordion>

<Accordion title="8. How do I get started with PayU Cross-Border Payments?" icon="fa-info-circle">
  If you are having a merchant account with PayU, contact your PayU Key Account Manager (KAM) to enable Cross-Border Payments.

  If you do not have a merchant account, you will need to create an account on the PayU website and complete the necessary registration and verification steps. For more information, refer to [Register for a Merchant Account](https://devguide.payu.in/dashboard/getting-started-with-payu-dashboard/register-for-a-merchant-account/).
</Accordion>

<Accordion title="9. By when we can update the UDFs if the invoice number was not available before the successful payment?" icon="fa-info-circle">
  The Invoice ID needs to be shared with the ICICI bank on the same day of the transaction to initiate settlements with the merchant. Hence, if the Invoice ID is not available at the time of the transaction, it is mandatory to be passed through the [UDF Update API](https://devguide.payu.in/cross-border-payments-import/udf-update-api/) or [Invoice Upload API](https://devguide.payu.in/cross-border-payments-import/invoice-upload-api/) on the same day (IST).
  The invoice file must be shared with PayU within 10 days of the transaction since the bank requires the same as per the Govt and RBI guidelines.
</Accordion>

<Accordion title="10. Which payment modes for which PayU supports cross-border payments?" icon="fa-info-circle">
  PayU supports the following payment methods for cross-border payments:

  * Credit/Debit Cards
  * Net Banking
</Accordion>

## APIs

<Accordion title="1. What is the purpose of Invoice Upload API?" icon="fa-info-circle">
  According to the RBI guidelines, the invoice file must be shared with PayU within 10 days of the transaction. The **Invoice Upload** API allows you to easily upload invoices for cross-border payments.
</Accordion>

<Accordion title="2. Which invoice or AWB file formats can be uploaded through the Invoice Upload API?" icon="fa-info-circle">
  The **Invoice Upload API** supports a variety of invoice types, including commercial invoices, proforma invoices, and purchase orders. Merchants can upload invoices in the following file formats:

  * PDF (.pdf)
  * Document (.doc or.docx)
  * Image (.jpg, .jpeg)
</Accordion>

<Accordion title="3. Can I upload multiple AWBs and AWB file using the Invoice Upload API?" icon="fa-info-circle">
  If a merchant are shipping multiple physical goods through various vendors on an invoice, you need to post multiple requests. For example, you have a customer ordered from two vendors, where vendorA is shipping the product from Gurgaon and vendorB is shipping the product from Bengaluru. Here, the AWB no. and corresponding AWB file are different for both the vendors. Hence, you need to post three requests using the **Invoice Upload** API. Where, the first request contains the invoice, the second request contains vendorA AWB & AWB file, and third request contains vendorB AWB & AWB file.
</Accordion>

<Accordion title="4. What is the UDF Update API in PayU Cross-Border Payments Integration?" icon="fa-info-circle">
  UDFs are the user-defined fields used for the specific purpose in the cross-border import payment flows to collect the various buyer's information such as:

  * invoice\_id (UDF5 - mandatory)
  * buyer's PAN (UDF1 - optional)
  * buyer's DOB (UDF3 - optional)
  * buyer's Import Export Code or IE Code (UDF4 - optional)
</Accordion>

<Accordion title="5. What is the format of the UDF data that can be uploaded using the UDF Update API?" icon="fa-info-circle">
  The UDF data in PayU Biz integration is being used in the JSON request body similar to:

  ```plaintext
  { "udf1": "value1", "udf2": "value2" }
  ```

  UDF data in PayU Hub integration is being used in the JSON request body similar to:

  ```plaintext
  "provider_specific_data": {
          "payu_india": {
              "additional_details": {
                  "invoice_id":"123456789", (UDF5)
                  "additionalDescription1": "AAAP*****", (UDF1)
                  "additionalDescription3": "22/08/1972", (UDF3)
                  "additionalDescription4": "IE_CODE_TESTING" (UDF4)
              }
          }
      },
  ```
</Accordion>

<Accordion title="6. What is the maximum size of UDF data that can be uploaded using the UDF Update API?" icon="fa-info-circle">
  The maximum size of UDF data that can be uploaded using the **UDF Upload** API is 4 KB.
</Accordion>

<Accordion title="7. Can I update the UDF data after it has been uploaded?" icon="fa-info-circle">
  Yes, you can update the UDF data for a transaction using the **UDF Upload** API multiple times. The latest UDF data uploaded will replace the existing data.
</Accordion>

<Accordion title="8. Is there any limit on the number of times I can update the UDF data for a transaction?" icon="fa-info-circle">
  There is no limit on the number of times you can update the UDF data for a transaction using the **UDF Update** API. However, the latest UDF data uploaded will replace the existing data.
</Accordion>

<Accordion title="9. Why the buyer's full information such as name, address, and other details are mandatory?" icon="fa-info-circle">
  As per RBI Guidelines, it is mandatory for the merchant to submit the buyer's name, address, and other details. The buyer's full information is required to comply with KYC (Know Your Customer) and AML (Anti-Money Laundering) regulations. It also helps in addressing fraud prevention, ensuring transaction security, and facilitating smoother delivery of purchased goods or services.
</Accordion>

<Accordion title="10. By when we can upload the invoices?" icon="fa-info-circle">
  Generally, invoices should be uploaded as soon as possible after the transaction has been completed.
</Accordion>

## Settlements

<Accordion title="Does PayU calculate the forex rates at the time of the transaction or at the time of settlements?" icon="fa-info-circle">
  Forex rates are calculated at the time of the transaction.
</Accordion>

<Accordion title="How can we get the Settlement details?" icon="fa-info-circle">
  Settlement files are available through the PayU Dashboard or using the **Settlement Details** API. For more information on the **Settlement Details** API, refer to [Retrieve Bank Settlement Details APIs](https://devguide.payu.in/api/settlement-details-api/settlement-apis/).
</Accordion>

<Accordion title="When will the Settlement process start?" icon="fa-info-circle">
  The settlement process typically starts after successfully processing the transaction. The exact timeline may vary based on factors such as the type of transaction and the payment method.
</Accordion>

<Accordion title="How much time the funds will reach my native bank account?" icon="fa-info-circle">
  The time taken for funds to reach your native bank account may vary depending on factors like the bank's processing times, and the settlement process. It will take **one or two days** but can take as long as five depending on the currency.
</Accordion>

<Accordion title="How can we get the Settlement details?" icon="fa-info-circle">
  Settlement details can typically be obtained through the PayU Dashboard or using the **Settlement Details** API. Follow PayU's specific guidelines and requirements to access settlement files. For more information on the Settlement Details API, refer to [Retrieve Bank Settlement Details APIs](https://devguide.payu.in/api/settlement-details-api/settlement-apis/).
</Accordion>
