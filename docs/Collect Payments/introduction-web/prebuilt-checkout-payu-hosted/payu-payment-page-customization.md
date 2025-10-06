---
title: Customize PayU Payment Page
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Customize PayU Payment Page or Checkout Page
  description: ''
  robots: index
next:
  description: ''
---
After you complete PayU Hosted Checkout integration, you will be able to see the PayU Payment page similar to the following screenshot when calling the **Collect Payment** API:

<Image align="center" border={true} width="400px" src="https://files.readme.io/1ee3893480e6e3d3c1e28d6ecffc4c52d1b3e8f2aba0247c9eb486dfef0fafc5-Screenshot_2024-09-06_at_11.54.02_AM.png" className="border" />

You can customize the following in the Checkout page:

* [Enforce Pay Method or Remove Category](https://docs.payu.in/docs/enforce-pay-method-or-remove-category)
* [Change the Language](https://docs.payu.in/docs/changing-the-language)
* [Configure Checkout Settings](doc:configure-checkout-settings)
* [Configure Checkout Payment Methods](doc:checkout-payment-modes)
* [Enable Pluxee on Checkout](https://docs.payu.in/docs/integrate-with-payu-hosted-checkout-sodexo)

## Enforce Pay Method or Remove Category

<Callout icon="📘" theme="info">
  **Note**: Before implementing on your Production environment, PayU strongly recommends you to enforce the payment parameters described in this section on the Test environment.
</Callout>

You can append the parameter names in your transaction request to opt for all or some of the payment modes.

<Accordion title="Enforce payment customization" icon="fa-code">
  
  Parameter name: **enforce_paymethod**
  
  This parameter allows you to customize the payment options for each transaction. You can enforce specific payment modes, cards scheme, and specific banks under Net Banking using this method.
  
  You need to include the necessary payment options in this parameter and POST them to PayU at the transaction time. All the categories and sub-categories have specific values that need to be included in this string.
  
  The categories and sub-categories are as follows:
  
  | Category    | Sub-category                              |
  | :---------- | :---------------------------------------- |
  | Credit Card | MasterCard, Amex, Diners, etc.            |
  | Debit Card  | Visa, MasterCard, Maestro, etc.           |
  | Net Banking | SBI Net Banking, HDFC Net Banking, etc    |
  | EMI         | CITI 3 Months EMI, HFC 6 Months EMI, etc. |
  | Wallet      | Airtel Money, YPay, ITZ, Cash Card, etc.  |
  | UPI         | GooglePay, PhonePe, UPI, etc.             |
  
  To enforce complete categories, use the values as described in the following table:
  
  | Category    | Value of enforced_payment |
  | :---------- | :------------------------ |
  | Credit Card | creditcard                |
  | Debit Card  | debitcard                 |
  | Net Banking | netbanking                |
  | NEFT/RTGS   | neftrtgs                  |
  | EMI         | emi                       |
  | UPI         | upi                       |
  | Wallet      | cashcard                  |
  | Sodexo      | SODEXO                    |
  | BNPL        | bnpl                      |
  | QR          | qr                        |
  
  To enforce sub-categories, use the respective bank codes for them. Contact PayU Support or at help.payu.in to get the respective bank codes.
  
  <Callout icon="📘" theme="info">
    **Note**: Ensure that you are using the delimiter as pipe (|) character between the values in these examples.
  </Callout>
  
</Accordion>
<Accordion title="Usage examples" icon="fa-code">
  
  #### creditcard|debitcard
  
  All the credit card and debit card options are displayed (as the whole category is enforced). The rest of the categories will not be displayed, that is, EMI, cash card, credit card, debit card, etc. – as they are not being mentioned in the string.
  
  #### creditcard|netbanking|cashcard
  
  All the credit card, Net Banking, and cash card options are displayed (as the whole category is enforced for these).
  
  <Callout icon="📘" theme="info">
    **Note**: Ensure you use this parameter only after testing properly as an incorrect string will lead to undesirable payment options being displayed.
  </Callout>
  
  For an example procedure on how to enforce payment with a credit card, refer to Enforce Payment with Credit Card.
  
</Accordion>
<Accordion title="Hide Specific Payment Modes" icon="fa-code">
  
  **Parameter name : drop_category**
  
  The **drop_category** parameter can be used if you want to hide one or multiple payment options. For example, if you consider the payment options such as credit card, debit card, and net banking, you can hide the credit card mode of payment.
  
  If 30 Net Banking options are available and you want to drop two of those net banking options (that is, do not display those two options on the PayU page), the **drop_category** parameter can be used effectively.
  
  To drop the whole category, use the following values:
  
  | Category    | Category Value |
  | :---------- | :------------- |
  | Credit Card | CC             |
  | Debit Card  | DC             |
  | Net Banking | NB             |
  | NEFT/RTGS   | NEFTRTGS       |
  | EMI         | EMI            |
  | Wallet      | CASH           |
  | BNPL        | BNPL           |
  | Sodexo      | SODEXO         |
  
  To drop sub-categories mentioned in the above table, use the respective bank codes for them. For the list bankcodes, refer to [Bank and Card Codes for Integration](doc:bank-and-card-codes-for-integration).
  
</Accordion>
<Accordion title="Checkout customization examples" icon="fa-code">
  
  **drop_category – DC|VISA|MAST**
  
  In this example:
  
  * For the debit card category, only Visa and Master Card options will be dropped, so they are not displayed on the PayU page.
  * All other active payment options are displayed.
  
  **drop_category – CC|AMEX, DC|VISA, EMI|EMI6**
  
  In this example:
  
  * For the credit card category, only the AMEX option is dropped and not displayed on the PayU page.
  * In the debit card category, only the VISA option would be dropped.
  * In the EMI category, only HDFC 6 months EMI option (bank code – EMI6) will be dropped.
  * All the other active payment options will be displayed on the PayU page.
  
  <Callout icon="📘" theme="info">
    **Note**: Use this parameter only after proper testing as an incorrect string will display undesirable payment modes.
  </Callout>
  
</Accordion>
## Change the Language

To change the display language in PayU Hosted Checkout, add the `language` parameter to the payment request API call. The following video shows how vernacular support can improve your business:

The `display_lang` parameter should be set to one of the following values (same as corresponding language spelling):

* English
* Hindi
* Tamil
* Telugu
* Kannada
* Gujarati
* Marathi

Here is an example payment request API call with the `display_lang` parameter set to Hindi:

```curl
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&txnid=PQI6MqpYrjEefU&amount=10.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&display_lang=Hindi&hash=05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072"
```

The PayU payment page is displayed with the display language as "Hindi" similar to the following screenshot:

<Image border={false} src="https://files.readme.io/3aae0ef-hindipage.png" />

## Configure Checkout Payment Methods

By default, the following payment methods are enabled for merchants on PayU Payment page (with PayU Hosted Checkout integration):

* NetBanking
* Debit Card
* Credit Card
* UPI
* Wallet

You can enable the following modes if you are eligible using Dashboard:

* BNPL
* EMI
* International Payments

<Callout icon="📘" theme="info">
  **Note**: You can enable or activate any of the above payment modes only if your are eligible or you have signed an agreement with PayU. If you are unable to raise request using Dashboard, contact your PayU Key Account Manager.
</Callout>

The following procedures describes how to enable payment mode or a feature.

## Enable a payment method

To configure the Dashboard to enable payment method:

1. Navigate to **Dashboard > Settings > Payment Methods.**

   The _Manage Payment Methods_ page is displayed with **Debit Card** tab selected by default.

<Image align="center" border={true} width="722px" src="https://files.readme.io/30b21d8-Screenshot_2024-07-19_at_10.34.10_AM.png" className="border" />

2. Select any of the payment method tab that you wish to configure.

   If you are eligible for the payment method, the **Activate Now** button is displayed. For example, the **Activate Now** button is enabled in the **International Payments** tab.

<Image align="center" border={true} width="722px" src="https://files.readme.io/87d81fd-Screenshot_2024-07-19_at_10.35.59_AM.png" className="border" />

3. Click **Activate Now**.

   A pop-up dialog box is displayed similar to the following screenshot and this will vary according to the payment method:

<Image align="center" border={false} width="622px" src="https://files.readme.io/6d9c81f-Screenshot_2024-07-19_at_10.37.45_AM.png" />

4. Click **Proceed** to activate.

   A confirmation message is displayed.

## Activate PayPal wallet

To activate PayPal wallet and start collecting payments with PayPal:

1. Follow the steps as in [Enable a payment method](#enable-a-payment-method).
2. Click **Link PayPal account**.

You are redirected to the PayPal page similar to the following screenshot.

<Image align="center" border={true} width="320px" src="https://files.readme.io/15f4290-Screenshot_2024-03-14_at_2.22.56_PM.png" className="border" />

3. Enter your email address that you want to use in future with PayPal.

<Image align="center" border={true} width="320px" src="https://files.readme.io/fc21647-Screenshot_2024-03-14_at_2.23.12_PM.png" className="border" />

4. Select your country as **India**.
5. Click **Next**.
6. Enter the password to create the account.

<Image align="center" border={false} width="320px" src="https://files.readme.io/c498645-Screenshot_2024-03-14_at_2.23.36_PM.png" />

7. Select your nature of your business and PAN details, name to displayed on statement and website URL as required and click **Next**.

<Image align="center" border={true} width="320px" src="https://files.readme.io/5d0d968-Screenshot_2024-03-14_at_5.07.28_PM.png" className="border" />

8. Enter your name, date of birth and contact details.

<Image align="center" border={true} width="320px" src="https://files.readme.io/e137009-paypal_name_dob.png" className="border" />

9. Scroll down and enter the business contact phone number and primary

<Image align="center" border={true} width="320px" src="https://files.readme.io/2e3e74f-paypal_details_mobile_currency.png" className="border" />

10. Click **Next**.

<Image align="center" border={true} width="320px" src="https://files.readme.io/32522a2-paypal_details_thanks_signup.png" className="border" />

<Accordion title="Disable Checkout payment modes" icon="fa-code">
  
  Contact your PayU Key Account Manager to remove a payment mode from the Checkout page.
  
</Accordion>
## Configure Checkout Settings

You can customize your customer-facing checkout page that is displayed when you are using PayU Hosted Checkout integration. For more information on PayU hosted Checkout integration, refer to [PayU Hosted Checkout](doc:prebuilt-checkout-payu-hosted).

To update your brand settings:

1. Navigate to **Dashboard > Settings > Checkout Settings.**

   The _Set up your brand_ page is displayed.

<Image align="center" border={true} src="https://files.readme.io/eb8cf99-Screenshot_2024-07-19_at_10.43.53_AM.png" className="border" />

2. Select or enter the details as described in the following table:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Brand Logo
      </td>

      <td>
        Enter the location or URL of the brand logo.

        **Note**: You need to that the size of the logo image is 90×90 and format of the logo image is PNG
      </td>
    </tr>

    <tr>
      <td>
        Secondary Color
      </td>

      <td>
        Click the color chooser to choose the color theme for the checkout page.
      </td>
    </tr>

    <tr>
      <td>
        Language
      </td>

      <td>
        Select the language from the **Language** drop-down list that has to be displayed on the Checkout page.
      </td>
    </tr>

    <tr>
      <td>
        Owner Signature
      </td>

      <td>
        Click **Select the file from your library** to select the signature file and click **Upload** to complete the action.
      </td>
    </tr>
  </tbody>
</Table>

<Callout icon="📘" theme="info">
  **Note**: While you configure each field above on the ,  you can see the preview in the right pane. For example, if you add or update the brand logo URL, it will be updated in the right pane preview.
</Callout>

## Enable Pluxee Card on Checkout

Pay Hosted Checkout (non-seamless) integration provides you to collect payments from customers using Pluxee (earlier Sodexo BRS) meal card on specific merchant categories such as restaurants, groceries etc.

<Callout icon="📘" theme="info">
  **Note**: PayU supports only PayU Hosted Checkout (non-seamless) and Merchant Hosted Checkout integration (seamless) using this API. Server-to-Server (S2S) integration is not be supported for Sodexo.
</Callout>

This section describes the parameters required to collect payments using the Pluxee card with PayU Hosted Checkout integration (using the **_payment** API) with parameters to enforce only the Pluxee card in the **mealcard** category or hide it.

***

<Accordion title="Steps to Integrate:" icon="fa-code">
  
  1. [Post the transaction request to PayU](#step-1-post-the-transaction-request-to-payu)
  2. [Customer submits payment details on PayU Page](#step-2-customer-submits-payment-details-on-payu-page)
  3. [Check the response from PayU](#step-3-check-the-response-from-payu)
  
</Accordion>
## Pluxee using PayU Hosted Integration workflow

The following describe the characteristics and workflow involved using PayU Hosted Checkout Integration with Pluxee:

* The existing **_payment** API used to initiate payments for online transactions will be used to initiate payments for Pluxee payment option.
* In case the merchant wants to enforce Pluxee payment option on our check out page, **enforce_paymethod** value should be passed as **SODEXO**.
* In case merchant wants to drop the Pluxee payment option under the **mealcard** category on the PayU checkout page, then **drop_category** value should be passed as **MC|SODEXO**. In case the **entire mealcard category** need to be dropped, then value should be passed as **MC**. Currently, PayU only supports the Sodexo payment option in the **mealcard** category.

For more information enforcing or hiding Pluxee payment option, refer to [Collect Payment API - PayU Hosted Checkout](https://docs.payu.in/reference/_payment_payu_hosted_checkout).

<Accordion title="Workflow on PayU Payment Page" icon="fa-code">
  
  1. Merchant initiates payment & redirects the customer to PayU's check out page to choose a payment option of their choice.
  2. Customer selects the Pluxee payment option available on the PayU's check out page & either enters new card details or selects already saved Pluxee card.
  3. In case customer want's to use an already saved Pluxee card, PayU will only allow that, provided the balance available in the card is greater than or equal to transaction amount.
  4. The customer is then re-directed to Pluxee ACS page, where the customer can enter the PIN and complete the payment.
  5. Once PayU receives a successful confirmation from Sodexo, we will provide a confirmation to merchant via webhook or merchant can use our status check API to fetch the transaction status.
  
</Accordion>
## Step 1: Post the transaction request to PayU

The parameters for the Sodexo card remain the same for as mentioned in the [Collect Payment API - PayU Hosted Checkout](https://docs.payu.in/reference/_payment_payu_hosted_checkout).

#### Enforcing Sodexo Card payment

If you wish to enforce the Sodexo card payment and hide other cards, you can use the following parameters and other PayU Hosted Checkout parameters according to your requirements.

| **Parameter**     | **Description**                                                                                                                                               | **Example** |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| enforce_paymethod | This parameter allows you to customize the payment options for each individual transaction. To enforce Sodexo card as the payment method, specify **SODEXO**. | SODEXO      |

#### Dropping the Sodexo Card payment

If you wish to hide the Sodexo card payment in the **mealcard** category, you can use the following parameters and other PayU Hosted Checkout parameters according to your requirements.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **Parameter**
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
        drop_category
        **optional**
      </td>

      <td>
        This parameter is used to customize the payment options for each individual transaction. To drop the Sodexo card payment with PayU Hosted Checkout integration, specify **mealcard|SODEXO**.
      </td>

      <td>
        mealcard|SODEXO
      </td>
    </tr>
  </tbody>
</Table>

**Note**: Currently, PayU India only supports the Sodexo payment option under the **mealcard** category.

#### Sample request

For a sample request, refer to [Collect Payment API - PayU Hosted Checkout](https://docs.payu.in/reference/_payment_payu_hosted_checkout) under API Reference.

***

<Accordion title="Step 2: Customer submits payment details on PayU page" icon="fa-code">
  
  The customer selects the Sodexo payment option on PayU's page.
  
  After the customer selects the **Sodexo** payment mode, PayU gets the Sodexo card details from the customer.
  
  The customer performs the authorization or authentication process on the bank's login page, and the bank communicates the success or failure response back to PayU.
  
</Accordion>
<Accordion title="Step 3: Check the response from PayU" icon="fa-code">
  
  PayU marks the transaction status based on the response received from the bank. PayU communicates the success URL to you if the payment is successful. Verify the authenticity of the hash value before accepting or rejecting the invoice order. For the list of parameters in the response body for the PayU Hosted integration, refer to [Collect Payment API - PayU Hosted Checkout](https://docs.payu.in/reference/_payment_payu_hosted_checkout) under API Reference.
  
  ***
</Accordion>