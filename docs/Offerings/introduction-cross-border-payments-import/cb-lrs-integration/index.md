---
title: Liberalised Remittance Scheme (LRS) for Travel & Education
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: Liberalised Remittance Scheme (LRS) for Travel & Education
deprecated: false
hidden: false
metadata:
  robots: index
---
The Liberalised Remittance Scheme (LRS) is a framework established by the Reserve Bank of India (RBI) that enables Indian residents, to send money internationally up to USD 250,000 per financial year. These remittances can cover various purposes like education fees, travel expenses, investments, and more.

## Key features of LRS:

- Annual limit of USD 250,000 per person per financial year
- Available only to individual residents (not businesses, HUFs, or trusts)
- Requires collection & validation of PAN (Permanent Account Number)
- Involves Tax Collected at Source (TCS) based on purpose & transaction amount as per applicable government regulations

> 📘
>
> **Note**: All transactions under LRS require PAN verification and proper declarations regarding the annual limit of USD 250,000. PayU automates these compliance requirements, making international payments simple for both merchants and customers.

> 👍 Before you begin:
>
> Register for a account with PayU before you start integration. Contact your PayU Key Account Manager to enable Cross-Border Payments and LRS. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

<Accordion title="Travel" icon="fa-info-a-plane">
#### International Travel Bookings

Indian travellers can seamlessly book and pay for international flights, hotels, and vacation packages using their preferred payment methods. The LRS framework ensures regulatory compliance while providing a smooth payment experience.

**Example:** An Indian customer books a hotel in Thailand for a family vacation. Instead of complicated wire transfers, they can complete the payment using UPI or Net Banking through your platform, with PayU handling all compliance requirements.

#### Foreign Travel Services

Travel agencies and Online Travel Aggregators (OTAs) can accept payments for international services like guided tours, transportation, and experience packages without payment friction.

**Example:** Your travel platform sells European tour packages to Indian customers. With PayU's LRS solution, customers can pay directly using familiar payment methods, while PayU manages PAN verification and TCS collection.

#### Applicability of PACB-Import & LRS Guidelines for Travel Sector

For merchants belonging to the following categories, a view of applicable regulations based on the type of service being sold:

* International OTA & Travel aggregators
* International Airlines
* International Hotel Chains
Here's the cleaned-up table. I fixed: duplicate link text in the last column, the broken empty link in the first Travel row, the malformed header separator, inconsistent bold on the last column header, and "Located Outside **in** India" → "Located Outside India."

| **Type of Service** | **Sub-type of Service** | **Applicability of PACB-Import & LRS** | **Implication on Payment Journey** |
| :--- | :--- | :--- | :--- |
| Travel | Domestic Flight Booking | Only PACB-Import | PAN collection & validation is not required. |
| Travel | International Flight Booking (all legs outside India) | Both PACB-Import & LRS | Payer's PAN details need to be collected and validated. Governed by [`lrs_service_type`](https://docs.payu.in/?isFramePreview=true#request-parameters) parameter in the payment request. |
| Travel | Mixed Flight Booking (One or more legs in India as well as International destinations) | Both PACB-Import & LRS | Payer's PAN details need to be collected and validated. Governed by [`lrs_service_type`](https://docs.payu.in/?isFramePreview=true#request-parameters) parameter in the payment request. |
| Hospitality | International Hotel Booking | Both PACB-Import & LRS | Payer's PAN details need to be collected and validated. Governed by [`lrs_service_type`](https://docs.payu.in/?isFramePreview=true#request-parameters) parameter in the payment request. |
| Hospitality | Indian Hotel Booking | Only PACB-Import | PAN collection & validation is not required. |
| Others Services (Cabs, Airport transfers, Tours & Attraction Tickets etc.) | Located Outside India | Both PACB-Import & LRS | Payer's PAN details need to be collected and validated. Governed by [`lrs_service_type`](https://docs.payu.in/?isFramePreview=true#request-parameters) parameter in the payment request. |
| Others Services (Cabs, Airport transfers, Tours & Attraction Tickets etc.) | Located in India | Only PACB-Import | PAN collection & validation is not required. |

</Accordion>
<Accordion title="Education" icon="fa-graduation-cap">
  #### International University Fees

  Indian students pursuing education abroad can pay their application fees, tuition, and accommodation costs directly to foreign universities through your platform.

  > **Example:** A student gains admission to a university in the UK and needs to pay the first semester fees. Through your platform integrated with PayU's LRS solution, they can make the payment using their preferred method while meeting all regulatory requirements.

  #### Education Consultancy Services

  Consultants helping students with international education can streamline fee payments for application processing, visa services, and university deposits.

  > **Example:** Your education consultancy helps students apply to multiple universities abroad. PayU's LRS solution enables you to collect consultation fees, application fees, and university deposits in a compliant manner while providing students with flexible payment options.

  #### Applicability of PACB-Import & LRS Guidelines for Education Sector

  | **Type of Service**                                 | **Applicability of PACB-Import & LRS** |
  | :-------------------------------------------------- | :------------------------------------- |
  | Online Education (MOOCs, degree certifications etc) | Only PACB-Import                       |
  | Foreign School / University fees Payment            | Both PACB - Import & LRS               |
</Accordion>

## Integration guides

The following sections describe how to integrate LRS for travel and education with PayU:

* [Customer Journey – PayU Hosted Checkout with LRS Integration](doc:customer-journey-payu-hosted-checkout-with-lrs-integration)
* [Integrate PayU Hosted Checkout](doc:integrate-payu-hosted-checkout-cb-lrs)
* [Merchant Hosted API Integration](doc:cb-lrs-merchant-hosted-api-integration)
* Payment method integrations
  * [Cards Integration for CB LRS](doc:cards-integration-for-cb-lrs)
  * [UPI Integration for CB LRS](doc:upi-integration-for-cb-lrs)
  * [NetBanking Integration for CB LRS](doc:netbanking-integration-for-cb-lrs)

## APIs used in LRS integration

| API name | Purpose |
| --- | --- |
| [PayU Hosted Checkout – CB LRS](ref:_payment_payu_hosted_checkout_cb_lrs) | Initiate LRS transactions on PayU Hosted Checkout with `lrs_service_type` and buyer PAN details. |
| [Merchant Hosted Checkout – CB LRS](ref:_payment_merchant_hosted_cb_lrs) | Submit merchant-hosted S2S payment requests with mandatory LRS parameters (`lrs_service_type`, TCS declarations, PAN in UDF fields). |
| [Collect Payment API – UPI (Cross-Border)](ref:_payment_cross-border_merchant_hosted_upi) | Initiate UPI Intent payments for cross-border LRS transactions. |
| [Collect Payment API – NetBanking (Cross-Border)](ref:_payment_cross-border_merchant_hosted_netbanking) | Initiate NetBanking payments for cross-border LRS transactions. |
| [Get Token API – Partner Integration](ref:get_token_api) | Generate a bearer token with `get_pan_details` scope for PAN Card Status Check API authentication.  |
| [Verify Payment API](ref:verify_payment_api) | Server-side reconciliation of transaction status after payment. |