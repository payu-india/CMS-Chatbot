---
title: Liberalised Remittance Scheme (LRS) for Travel & Education
deprecated: false
hidden: false
metadata:
  robots: index
---
The Liberalised Remittance Scheme (LRS) is a framework established by the Reserve Bank of India (RBI) that enables Indian residents, to send money internationally up to USD 250,000 per financial year. These remittances can cover various purposes like education fees, travel expenses, investments, and more.

Key features of LRS:

- Annual limit of USD 250,000 per person per financial year
- Available only to individual residents (not businesses, HUFs, or trusts)
- Requires collection & validation of PAN (Permanent Account Number)
- Involves Tax Collected at Source (TCS) based on purpose & transaction amount as per applicable government regulations

> 📘
>
> **Note**: All transactions under LRS require PAN verification and proper declarations regarding the annual limit of USD 250,000. PayU automates these compliance requirements, making international payments simple for both merchants and customers.

## Advantages of LRS with PayU

### For Merchants

- **Simplified International Payments:** Accept payments from Indian customers without establishing an Indian entity
- **Higher Success Rates:** Optimized payment flows ensure better transaction completion rates
- **Multiple Payment Options:** Offer local payment methods like UPI, NetBanking, and Cards for international transactions
- **Automated Compliance:** Built-in verification systems for PAN, TCS calculations, and legal declarations as per local regulations
- **Real-time Tracking:** Monitor remittance status with instant updates
- **Flexible Integration:** Choose between seamless and non-seamless integration options

### For Customers

- **Convenience:** Use familiar Indian payment methods for international transactions
- **Digital Process:** Complete the entire remittance process online without visiting banks
- **Transparency:** Clear visibility of exchange rates, fees, and TCS amounts
- **Regulatory Compliance:** Automatic handling of necessary declarations and tax requirements for buyers

## Use Cases

### Travel

#### International Travel Bookings

Indian travellers can seamlessly book and pay for international flights, hotels, and vacation packages using their preferred payment methods. The LRS framework ensures regulatory compliance while providing a smooth payment experience.

**Example:** An Indian customer books a hotel in Thailand for a family vacation. Instead of complicated wire transfers, they can complete the payment using UPI or Net Banking through your platform, with PayU handling all compliance requirements.

#### Foreign Travel Services

Travel agencies and Online Travel Aggregators (OTAs) can accept payments for international services like guided tours, transportation, and experience packages without payment friction.

**Example:** Your travel platform sells European tour packages to Indian customers. With PayU's LRS solution, customers can pay directly using familiar payment methods, while PayU manages PAN verification and TCS collection.

#### Applicability of PACB-Import & LRS Guidelines for Travel Sector

For merchants belonging to the following categories, a view of applicable regulations based on the type of service being sold:

- International OTA & Travel aggregators
- International Airlines
- International Hotel Chains

| **Type of Service**                                                        | **Sub-type of Service**                                                                | **Applicability of PACB-Import & LRS** | Implication on Payment Journey                                                                                                                                                             |
| :------------------------------------------------------------------------- | :------------------------------------------------------------------------------------- | :------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Travel                                                                     | Domestic Flight Booking                                                                | Only PACB-Import                       | PAN collection & validation is not required                                                                                                                                                |
| Travel                                                                     | International Flight Booking (all legs outside India)                                  | Both PACB - Import & LRS               | Payer's PAN details need to be collected and validated. Governed by "[lrs\_service\_type"](https://docs.payu.in/?isFramePreview=true#request-parameters) parameter in the payment request. |
| Travel                                                                     | Mixed Flight Booking (One or more legs in India as well as International destinations) | Both PACB - Import & LRS               | Payer's PAN details need to be collected and validated. Governed by "[lrs\_service\_type"](https://docs.payu.in/?isFramePreview=true#request-parameters) parameter in the payment request. |
| Hospitality                                                                | International Hotel Booking                                                            | Both PACB - Import & LRS               | Payer's PAN details need to be collected and validated. Governed by "[lrs\_service\_type"](https://docs.payu.in/?isFramePreview=true#request-parameters) parameter in the payment request. |
| Hospitality                                                                | Indian Hotel Booking                                                                   | Only PACB-Import                       | PAN collection & validation is not required.                                                                                                                                               |
| Others Services (Cabs, Airport transfers, Tours & Attraction Tickets etc.) | Located Outside in India                                                               | Both PACB - Import & LRS               | Payer's PAN details need to be collected and validated. Governed by "[lrs\_service\_type"](https://docs.payu.in/?isFramePreview=true#request-parameters) parameter in the payment request. |
| Others Services (Cabs, Airport transfers, Tours & Attraction Tickets etc.) | Located in India                                                                       | Only PACB-Import                       | PAN collection & validation is not required.                                                                                                                                               |

<br />

### Education

#### International University Fees

Indian students pursuing education abroad can pay their application fees, tuition, and accommodation costs directly to foreign universities through your platform.

> **Example:** A student gains admission to a university in the UK and needs to pay the first semester fees. Through your platform integrated with PayU's LRS solution, they can make the payment using their preferred method while meeting all regulatory requirements.

#### Education Consultancy Services

Consultants helping students with international education can streamline fee payments for application processing, visa services, and university deposits.

> **Example:** Your education consultancy helps students apply to multiple universities abroad. PayU's LRS solution enables you to collect consultation fees, application fees, and university deposits in a compliant manner while providing students with flexible payment options.

<br />

#### Applicability of PACB-Import & LRS Guidelines for Education Sector

| **Type of Service**                                 | **Applicability of PACB-Import & LRS** |
| :-------------------------------------------------- | :------------------------------------- |
| Online Education (MOOCs, degree certifications etc) | Only PACB-Import                       |
| Foreign School / University fees Payment            | Both PACB - Import & LRS               |

<br />
