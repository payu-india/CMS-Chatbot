---
title: Frequently Asked Questions (FAQs)
deprecated: false
hidden: true
metadata:
  robots: index
---
## Getting started

1. ### Where should I start with PayU APIs?
   <Accordion title="Answer" icon="fab fa-adn">
     Start with [API Introduction](doc:api-introduction), then [Choose](doc:which-api-should-i-use) Your API, then [Making Your First API Request](doc:making-your-first-api-request). You can then go through specific endpoint pages.
   </Accordion>
2. ### What is the difference between Integration Guides and API Reference?
   <Accordion title="Answer" icon="fab fa-adn">
     Integration Guides explain end-to-end product setup and UX flows. Whereas, API Reference documents request/response contracts and Try It calls. API Introduction explains shared concepts used by both.
   </Accordion>

***

## Authentication

1. ### Do all PayU APIs use the same authentication?
   <Accordion title="Answer" icon="fab fa-adn">
     No. Most Payment Gateway APIs use merchant `key` + `salt` + SHA-512 hash. Payouts and Partner APIs typically use OAuth. Some product APIs use HMAC headers. Refer to [API Authentication and Security](doc:api-authentication-and-security) for more information.
   </Accordion>
2. ### Where do I get key and salt?
   <Accordion title="Answer" icon="fab fa-adn">
     You can <Anchor target="_blank" href="doc:generate-merchant-key-and-salt-on-payu-dashboard">generate merchant key and salt</Anchor> from the dashboard.
   </Accordion>
3. ### Can I generate a hash value in the browser?
   <Accordion title="Answer" icon="fab fa-adn">
     You can prototype there, however, you should generate a production hash on your server so the salt is never exposed.
   </Accordion>

***

## Environments and URLs

1. ### Is there one base URL for all PayU APIs?
   <Accordion title="Answer" icon="fab fa-adn">
     No. Collect Payment, General APIs, OAuth products, BBPS, and others use different hosts. Refer to the [API Environments and Base URLs](doc:api-environments-and-base-urls) document for more information.
   </Accordion>
2. ### Can I use the Test key with the Production URL?
   <Accordion title="Answer" icon="fab fa-adn">
     No. Keep environment, key, and salt matched as a set.
   </Accordion>

***

## Payments and verification

1. ### Why do I need to verify the payment using the API or any other method if I already got a success callback?
   <Accordion title="Answer" icon="fab fa-adn">
     Callbacks can be delayed, duplicated, or manipulated in the browser channel. Verify Payment API (or an equivalent server API) is the reliable source of truth.
   </Accordion>
2. ### What should I do if the customer closes the app before redirect?
   <Accordion title="Answer" icon="fab fa-adn">
     Store the `txnid`, check webhooks, and call Verify Payment/transaction detail APIs to reconcile.
   </Accordion>

***

## Webhooks

1. ### Are webhooks mandatory?
   <Accordion title="Answer" icon="fab fa-adn">
     Webhooks are recommended for production-grade reliability, especially for async payment modes and refunds. Refer to the [Webhooks and Callbacks](doc:webhooks-and-callbacks) document for more information.


   </Accordion>

***

## Versioning

1. ### What is `api_version`?
   <Accordion title="Answer" icon="fab fa-adn">
     A request parameter used by many Collect Payment/feature flows to select a capability set. It can change required fields and hash input. Refer to the [API Versioning](doc:api-versioning) document for more information.
   </Accordion>

***

## Tools

1. ### Why does Try It fail for my API?
   <Accordion title="Answer" icon="fab fa-adn">
     Some APIs/flows are not supported in Test or in the Try It playground.
   </Accordion>

***

## Support

1. ### How do I get help?
   <Accordion title="Answer" icon="fab fa-adn">
     1. Use [API Troubleshooting](doc:api-troubleshooting)
     2. Check [Error Codes](ref:error-codes)
     3. Raise a ticket at [https://help.payu.in](https://help.payu.in) with `txnid`/request IDs and sanitized logs
   </Accordion>
