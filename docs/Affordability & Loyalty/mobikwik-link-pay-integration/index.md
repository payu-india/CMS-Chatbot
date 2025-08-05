---
title: Mobikwik Link & Pay Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
This section describes step-by-step integration procedure for Mobikwik Link & Pay, designed to offer a seamless, one-click payment experience for users and merchants.

It provides a **seamless, one-click payment experience** for Mobikwik wallet users on PayU’s S2S integration. This streamlined flow aims to simplify the checkout process and enhance the overall payment experience for all parties. By introducing Link & Pay, Mobikwik seeks to offer merchants an efficient and scalable solution that improves conversion rates and customer satisfaction, reinforcing PayU's leadership in payment innovation.

This integration is expected to deliver **measurable value** to merchants by reducing friction at checkout, increasing transaction success, and improving customer retention. For users, it promises a faster, more convenient, and secure payment process, making digital wallet payments more appealing.

## Advantages for Merchants

1. **Increased Conversion Rates**: The frictionless one-click payment process minimizes cart abandonment, leading to more completed transactions.
2. **Enhanced Customer Retention**: A smoother payment experience boosts customer satisfaction, encouraging repeat purchases and fostering long-term loyalty.
3. **Simplified Integration**: Merchants can implement Link & Pay with minimal changes, simplifying payment workflows and reducing operational complexity.

## Advantages for Users

1. **Faster, Simplified Payments**: Users can complete transactions with a single click, eliminating the need to log into their wallet, resulting in a quicker and more convenient checkout.
2. **Greater Flexibility**: Link & Pay allows secure storage of payment information, enabling instant and seamless payments across various platforms.
3. **Enhanced Security**: Users benefit from Mobikwik’s encryption and authentication processes, ensuring their payment information is protected.

This solution aims to drive higher user engagement, improved conversion rates, and reinforce PayU's position at the forefront of payment innovation, ultimately leading to increased transaction success, better customer retention, and stronger merchant relationships.

## Prerequisites

The development of the Link & Pay wallet feature spans multiple key areas, from Checkout to Core Payments. The entire ecosystem is designed for flexibility and scalability, serving the needs of both **S2S4 merchants** (where the checkout and Wallet link/OTP page are managed by the merchant or PayU) and **PayU hosted merchants** (where these pages are managed by PayU). For Phase 1, implementation is planned for S2S4 merchants like MakeMyTrip and Myntra.

The integration utilizes the existing BNPL Link & Pay Generic API Stack, with customisation for S2S and PayU hosted Checkout merchants.

## Workflow