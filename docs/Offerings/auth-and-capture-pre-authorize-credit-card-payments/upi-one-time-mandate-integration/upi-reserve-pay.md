---
title: UPI Reserve Pay
deprecated: false
hidden: true
metadata:
  robots: index
---
**UPI Reserve Pay** enables customers to securely block funds in their account for up to **90 days** at the time of transaction. The actual payment is deducted only when the merchant initiates a debit request. If the transaction is not completed, the reserved amount is automatically released back to the customer’s account.

Merchants can perform **multiple debits** from the reserved amount until it is fully utilized, offering flexibility for both businesses and customers. Plus, customers don’t need to enter their UPI PIN for every payment.

## Use Cases

UPI Reserve Pay is ideal for scenarios where payment flexibility and fund assurance are critical:

### E-commerce

* Block the full price at checkout and charge only for items kept after delivery or trial period.
* Eliminates complex refund processes and reduces risk in **Pay-on-Delivery** workflows.

### Travel & Hospitality

* **Hotel Bookings:** Block estimated stay cost during reservation; debit final charges at checkout. Cancelled bookings instantly release funds.
* **Flight Bookings:** Manage fare changes without requiring customers to re-authenticate or re-enter payment details.

### Healthcare

* Block estimated treatment cost upfront.
* Hospitals can debit actual charges for services rendered throughout the care period, simplifying billing.

## How It Works

1. **Authorization:** At order placement, a specified amount is blocked in the customer’s account.
2. **Capture:** Merchant debits all or part of the blocked amount as needed until the reserve expires.
3. **Cancellation:** Cancel within the allowed timeframe to instantly release funds back to the customer.

## Key Features

* **Extended Fund Hold:** Unlike cards (7 days) and standard OTM (60 days), UPI Reserve Pay allows funds to remain blocked for up to **90 days**.
* **Instant Refunds:** Cancelled transactions immediately credit the amount back to the customer’s account.
* **Seamless Merchant Experience:** Block funds at order placement and capture payment when required. Real-time confirmation ensures confidence for both parties—perfect for pre-orders, reservations, and delayed deliveries.

<Callout icon="👍">
  **Reference:** All the other API integrations will remain same for One time mandate. For more information, refer to [APIs used in Auth and Capture](doc:apis-used-in-auth-and-capture).
</Callout>

## Next Steps

UPI Reserve Pay is supported on the following integrations:

* **Merchant Hosted Checkout**: For more information, refer to [UPI Reserve Pay One-Time Mandate - Merchant Hosted](ref:upi-reserve-pay-one-time-mandate-merchant-hosted)
* **PayU Hosted Checkout**: For more information, refer to [UPI Reserve Pay One-Time Mandate - PayU Hosted](ref:upi-reserve-pay-one-time-mandate-payu-hosted)
