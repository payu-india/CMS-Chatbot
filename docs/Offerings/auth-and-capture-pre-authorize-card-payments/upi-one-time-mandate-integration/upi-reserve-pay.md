---
title: UPI Reserve Pay
deprecated: false
hidden: false
metadata:
  title: UPI Reserve Pay - Pre-Authorize Payments
  keywords:
    - UPI Reserve Pay - Pre-Authorize Payments
    - UPI Pre-authorize Reserve Pay
  robots: index
---
**UPI Reserve Pay** enables customers to securely block funds in their account for up to **90 days** at the time of transaction. The actual payment is deducted only when the merchant initiates a debit request. If the transaction is not completed, the reserved amount is automatically released back to the customer’s account.

Merchants can perform **multiple debits** from the reserved amount until it is fully utilized, offering flexibility for both businesses and customers. Plus, customers don’t need to enter their UPI PIN for every payment.

## Use Cases

UPI Reserve Pay is ideal for scenarios where payment flexibility and fund assurance are critical:

* **E-Commerce** (Flash Sales): During sales, ₹10,000 is blocked for products. Final charges (e.g., ₹9,200) are captured, and the balance ₹800 is released if items are unavailable. 
   
* **Prepaid Services** (Mobile Recharge): For a recharge of ₹499, ₹550 is blocked to account for plan adjustments. After finalizing the recharge (e.g., ₹499), the balance ₹51 is released. 
   
* **Tourism** (Ticket Bookings): Customers block Rs. 2,500 using UPI during ticket booking. If confirmed, funds are captured. If not, the block is released 
   
* **BFSI** (Insurance Premium): For a premium range of Rs. 2,500–4,000, Rs. 4,000 is blocked. After policy approval, the exact premium (e.g., Rs. 3,000) is captured, and the balance is released 
   
* **Healthcare** (Patient Check-ins): For an estimated Rs. 50,000 hospitalization fee, the amount is blocked. Upon final billing (e.g., Rs. 45,000), the charge is captured, and the excess Rs. 5,000 is released.

## How It Works

1. **Authorization:** At order placement, a specified amount is blocked in the customer’s account.
2. **Capture:** Merchant debits all or part of the blocked amount as needed until the reserve expires.
3. **Cancellation:** Cancel within the allowed timeframe to instantly release funds back to the customer.

## Key Features

* **Extended Fund Hold:** Unlike cards (7 days) and standard OTM (60 days), UPI Reserve Pay allows funds to remain blocked for up to **90 days**.
* **Instant Refunds:** Cancelled transactions immediately credit the amount back to the customer’s account.
* **Seamless Merchant Experience:** Block funds at order placement and capture payment when required. Real-time confirmation ensures confidence for both parties—perfect for pre-orders, reservations, and delayed deliveries.
* **Amount Unblocking**: Currently, the releasing of funds is done by remiters but PayU has built a functionality (internal)  to revoke the transactions based on end date to minimise the funds on hold.

<Callout icon="👍" theme="okay">
  **Reference:** All the other API integrations will remain same for One time mandate. For more information, refer to [APIs used in Auth and Capture](doc:apis-used-in-auth-and-capture).
</Callout>

## Next Steps

UPI Reserve Pay is supported on the following APIs:

* **Merchant Hosted Checkout**: For more information, refer to [UPI Reserve Pay One-Time Mandate - Merchant Hosted](ref:upi-reserve-pay-one-time-mandate-merchant-hosted)
* **PayU Hosted Checkout**: For more information, refer to [UPI Reserve Pay One-Time Mandate - PayU Hosted](ref:upi-reserve-pay-one-time-mandate-payu-hosted)