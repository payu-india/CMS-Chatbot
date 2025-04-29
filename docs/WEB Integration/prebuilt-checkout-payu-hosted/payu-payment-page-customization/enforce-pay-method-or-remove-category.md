---
title: Enforce Pay Method or Remove Category
excerpt: >-
  For PayU Hosted Checkout integration, PayU has predefined customisations that
  suit your requirements. You can opt for all or some payment modes according to
  their requirements.
deprecated: false
hidden: false
metadata:
  title: Enforce Payment Method or Remove Category in PayU Hosted Checkout
  description: >-
    earn how to customize the payment methods or categories that are displayed
    on PayU’s hosted checkout page. This page provides examples of how to use
    the payMethods parameter to enforce a specific payment method or remove a
    payment category for your customers.
  robots: index
next:
  description: ''
---
> 📘 Note
> 
> Before implementing on your Production environment, PayU strongly recommends you to enforce the payment parameters described in this section on the Test environment.

You can append the parameter names in your transaction request to opt for all or some of the payment modes.

## Enforce payment customization

Parameter name: enforce_paymethod

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

> 📘 Note
> 
> Ensure that you are using the delimiter as pipe (|) character between the values in these examples.

## Usage examples

### creditcard|debitcard

All the credit card and debit card options are displayed (as the whole category is enforced). The rest of the categories will not be displayed, that is, EMI, cash card, credit card, debit card, etc. – as they are not being mentioned in the string.

### creditcard|netbanking|cashcard

All the credit card, Net Banking, and cash card options are displayed (as the whole category is enforced for these).

> 📘 Note:
> 
> Ensure you use this parameter only after testing properly as an incorrect string will lead to undesirable payment options being displayed.

For an example procedure on how to enforce payment with a credit card, refer to Enforce Payment with Credit Card.

## Hide Specific Payment Modes

**Parameter name : drop\_category**

The **drop\_category** parameter can be used if you want to hide one or multiple payment options. For example, if you consider the payment options such as credit card, debit card, and net banking, you can hide the credit card mode of payment.

If 30 Net Banking options are available and you want to drop two of those net banking options (that is, do not display those two options on the PayU page), the **drop\_category** parameter can be used effectively.

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

## Checkout customization examples

**drop\_category – DC|VISA|MAST**

In this example:

- For the debit card category, only Visa and Master Card options will be dropped, so they are not displayed on the PayU page.
- All other active payment options are displayed.

**drop\_category – CC|AMEX, DC|VISA, EMI|EMI6**

In this example:

- For the credit card category, only the AMEX option is dropped and not displayed on the PayU page.
- In the debit card category, only the VISA option would be dropped.
- In the EMI category, only HDFC 6 months EMI option (bank code – EMI6) will be dropped.
- All the other active payment options will be displayed on the PayU page.

> 📘 Note:
> 
> Use this parameter only after proper testing as an incorrect string will display undesirable payment modes.