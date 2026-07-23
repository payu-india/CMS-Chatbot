---
title: Configure Refunds for Offer Transactions
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
You can configure refunds for transactions involving offers (created using PayU Dashboard).

<Callout icon="📘" theme="info">
  **Activate this feature**: Contact your PayU Key Account Manager (KAM) to activate this feature so that you can configure refunds for Offer transactions.
</Callout>

For the amount to be refunded your customer transactions involving offers, you can configure any of the following adjustment rule using Dashboard:

* **No adjustment on offer**: You will decide the amount to be adjusted to the customer and PayU will process the refund without making any calculations.
* **Recalculation of offer amount**: PayU will do the recalculation of the offer amount based on the discount or cashback provided. You have to **post the MRP** amount (before offer) to PayU so that refund is calculated accordingly. For the recalculation of the offer amount details, refer to [Refunds for Offers](doc:refunds-for-offers).

<Callout icon="📘" theme="info">
  **Note**: Currently, PayU offers transaction-level refunds. SKU-level refunds is not supported with the **Recalculation of offer amount** option described in [Procedure to configure](#procedure-to-configure).
</Callout>

## Procedure to configure

To configure the refunds for payments with offers:

1. Navigate to **Dashboard > Settings > Offers & Promotions.**

      The _Configure offers and promotions_ page is displayed.

<Image align="center" border={true} src="https://files.readme.io/aee9f43-Screenshot_2024-07-19_at_10.28.44_AM.png" className="border" />

2. In the **Adjustment Rule** field, select any of the following:

* **No adjustment on offer**: You will decide the amount to be adjusted or PayU will not make the calculation.
* **Recalculation of offer amount**: PayU will do the recalculation of the offer amount based on the discount or cashback provided.

## Comparison of Adjustment Rules

For example, consider you have the following transaction listing on the Transactions Dashboard where the amount paid by customer is Rs.1.00 with a discount of Rs.9:

<Image align="center" border={true} src="https://files.readme.io/d7457ee6c61a4c48dc7675a94a2c43b93db85f7ad896855db8d8d240be28559b-offer-refunds-transaction-listing.png" className="border" />

The details of this transaction is similar to the following:

<Image align="center" border={true} src="https://files.readme.io/dabd3b793ac14b53867e20ad2c8eb3041d54224b9e4287d5cd7cc0f9a32b5e43-offer-refunds-transaction-details.png" className="border" />

The following  compares the adjustment rules when trying to initiate refund the above transaction

* **No adjustment on offer**: You can specify the refund amount that you wish to, where it can be greater the amount you received after discount. In this example, the amount received after discount of Rs.9 is Rs.1, but net refund amount that can refunded is Rs.10.

<Image align="center" border={true} width="350px" src="https://files.readme.io/5505a787c36f1a36950dbf7b9419fde527dc97a9dc310d4a504acaa30ce583fb-Screenshot_2024-09-04_at_5.53.01_PM.png" className="border" />

* **Recalculation of offer amount**: You can specify the refund amount that can be less than/equal to the amount you received after discount. In this example, the amount received after discount is Rs.10, but net refund amount is Rs.1.

<Image align="center" border={true} width="350px" src="https://files.readme.io/2d26262a94498704bb64ee80f03d9877079b54038fd8fcecb9057c30f4193c74-Screenshot_2024-09-04_at_5.50.23_PM.png" className="border" />
