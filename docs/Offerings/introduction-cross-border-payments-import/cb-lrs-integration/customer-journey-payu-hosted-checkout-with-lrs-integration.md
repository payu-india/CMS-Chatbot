---
title: Customer Journey - PayU Hosted Checkout with LRS Integration
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  title: Customer Journey - PayU Hosted Checkout with LRS Integration
  keywords:
    - Customer Journey - PayU Hosted Checkout with LRS Integration
    - Customer Journey for PayU Hosted Checkout with LRS Integration
    - Customer Journey for LRS
  robots: index
---
This section outlines the customer journey for Cross Border Liberalised Remittance Scheme (LRS) transactions using PayU Hosted Checkout (non-seamless integration). The journey incorporates the mandatory LRS declarations that customers must acknowledge before completing their payment.

The typical customer journey for PayU Hosted Checkout with LRS checks involves the following sequence:

1. Customer selects products/services on the merchant website and proceeds to checkout
2. Merchant prepares the payment request including the **LRS Service Type**
3. Merchant initiates the API call to PayU with these parameters.
4. Customer is redirected to the PayU Hosted Checkout page where they begin the payment process.
5. Customer provides the additional details and declarations for making the purchase under LRS:

   * Selects the **Individual Buyer**
   * Fills their personal details (Name as on PAN, PAN, DOB, pin-code) (required only for Individuals)
   * Selects the mandatory **LRS Declaration** check box (at the bottom of the page) declaring that they are under the LRS limit of $250K USD in current financial year & agree to the buyer T&Cs.

   <br />

   <Image align="center" border={true} src="https://files.readme.io/df74b10d4fb401c9658c26ff593905ee625cc2bde4720d127293d8786ec9a74c-cb-lrs-payu-hosted-amt-declaration.png" className="border" />
6. Customer provides the tax details and tax limit declaration for LRS:

   * Shows TCS (Tax Collected at Source) options. As per the <Anchor label="latest tax rules" target="_blank" href="https://www.hdfcbank.com/personal/useful-links/important-messages/revision-in-tcs-on-lrs-transactions">latest tax rules</Anchor> (effective April '25), an additional tax needs to be collected for individuals who have remitted more than INR 10 lacs 1 million in current financial year.
   * The applicable tax rate is based on the **LRS Service Type** passed in the payment request.
     <HTMLBlock>{`
     <HTMLBlock>
     <table>
         <tbody>
             <tr>
                 <td>
                     <strong>lrs_service_type</strong>&nbsp;
                 </td>
                 <td>
                     <strong>Txn Amount &lt;= INR 10 lacs</strong>&nbsp;
                 </td>
                 <td>
                     <strong>Txn Amount &gt; INR 10 lacs</strong>&nbsp;
                 </td>
             </tr>
             <tr>
                 <td>
                     education_loan&nbsp;
                 </td>
                 <td>
                     0&nbsp;
                 </td>
                 <td>
                     0&nbsp;
                 </td>
             </tr>
             <tr>
                 <td>
                     education_non_loan&nbsp;
                 </td>
                 <td>
                     0&nbsp;
                 </td>
                 <td>
                     5%&nbsp;
                 </td>
             </tr>
             <tr>
                 <td>
                     medical&nbsp;
                 </td>
                 <td>
                     0&nbsp;
                 </td>
                 <td>
                     5%&nbsp;
                 </td>
             </tr>
             <tr>
                 <td>
                     travel&nbsp;
                 </td>
                 <td>
                     0&nbsp;
                 </td>
                 <td>
                     20%&nbsp;
                 </td>
             </tr>
             <tr>
                 <td>
                     others&nbsp;
                 </td>
                 <td>
                     0&nbsp;
                 </td>
                 <td>
                     20%&nbsp;
                 </td>
             </tr>
         </tbody>
     </table>
     </HTMLBlock>
     `}</HTMLBlock>
     If the transaction amount itself is greater than INR 10 lacs, the tax will be automatically added.
   * For transactions lower than INR 10 lacs, the buyer can declare that they are under the spend limit and pay no TCS.
   * Alternatively, they can declare that they are over the INR 10 lacs limit and a TCS rate will be applied on the transaction amount

> 📘 Tax remittance:
>
> PayU will collect the tax amount and get it deposited to local tax authorities via our partner AD-1 bank. This amount cannot be refunded, A receipt or proof of payment (challan) can also be shared on request basis.
>
> This payment does not increase the tax liability of the buyer, it is only an advance tax payment and can be adjusted against the actual tax liability of the payer at the end of the financial year.

<Image align="center" border={true} src="https://files.readme.io/db14893cec45b3b796b2a6932703001c95b2caec1a63f4889485a8553bc79e8c-cb-lrs-payu-hosted-tax-declaration.png" className="border" />

7. The rest of workflow involves the collecting payment details. For more information, refer to[ PayU Hosted Checkout > Customer Journey](doc:prebuilt-checkout-payu-hosted#customer-journey).
