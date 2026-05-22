---
title: APIs to Manage Subscriptions and Plans
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
## Manage Subscriptions

Subscription is the heart of the Zion. It provides consolidated view of all the services opted by customer for given merchant.

It combines billing plans at one place and associates them with preferred payment instrument (Credit Card / Debit Card / Net Banking) of the customer, so that future recurring payments can be completely automated with total flexibility

Also, subscription provides a foundation to manage complete billing cycle for the customer by providing different touch points like -

* Smart Retries
* Change of payment instrument
* Payment link generation
* Auto completion of billing plan
* Association of billing plan with specific start and end dates
* Comprehensive Subscription management panel

The following APIs are used to manage subscriptions:

* [Define Subscription API](ref:create-a-subscription)
* [Update Subscription API](ref:update-subscription-api)
* [Get List of Subscriptions API](ref:get-list-of-subscriptions-api)
* [Cancel Subscription API](ref:cancel-subscription-api)
* [Get Subscription Details API](ref:get-subscription-details-api)

The following APIs are used to link or de-link plans with a subscription:

* [Subscription Life Cycle and role of Webhooks](ref:subscription-life-cycle-and-role-of-webhooks-)

## Manage Plans

Merchant can create subscription plan with combination of billing cycles and billing amount and keep associating with subscription. Merchant needs to leverage Subscription interface directly.

## Manage Invoice

Charge requests triggered automatically by Zion against customer’s preferred payment instrument on the billing date are known as invoices. For every plan associated with subscription, Invoices are triggered specific to individual plans and run independently as per the schedule mentioned for that plan. The APIs to manage invoice are:

* [Get Invoice API](ref:get-invoice-interfaces-api-zion)
* [Create Invoice API](ref:create-invoice-api-zion)
