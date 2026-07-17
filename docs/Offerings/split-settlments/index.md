---
title: Split Settlements
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Split Settlements Introduction
  description: >-
    PayU Split Settlements APIs enable businesses to make, collect, and receive
    payments using bank accounts. The Split Settlements API allows customers to
    split a transaction based on the number of sellers involved in the
    particular transaction. This page from the PayU Developer Documentation
    Portal provides information on how to use the Split Settlements API,
    including authentication requirements and use cases such as taxi aggregators
    and eCommerce platforms.
  keywords:
    - PayU Split Settlements
    - ' payment distribution platform'
    - ' multi-vendor payment processing'
    - ' marketplace payment solutions'
    - ' automated payment splitting'
    - ' automated payment distribution system'
    - ' custom payment allocation rules'
    - ' vendor payment management'
    - ' payment reconciliation for marketplaces'
    - ' multi-party transaction processing'
    - ' e-commerce marketplace payment solutions'
    - ' service aggregator payment distribution'
    - ' subscription revenue splitting'
    - ' franchise payment management'
    - ' event platform payment distribution'
    - ' payment split API integration'
    - ' sub-merchant settlement system'
    - ' merchant payout automation'
    - ' payment distribution workflow'
    - ' settlement cycle configuration'
    - ' simplified payment reconciliation system'
    - ' reduce payment operations overhead'
    - ' compliant payment distribution'
    - ' streamlined vendor payments'
    - ' automated commission settlement'
  robots: index
next:
  description: ''
---
In today's dynamic e-commerce landscape, marketplaces and aggregator platforms face unique challenges when managing payments between multiple stakeholders. Whether you're running an online marketplace with numerous sellers, a taxi aggregation service connecting drivers with passengers, or an insurance platform working with multiple providers, the complexity of settling payments accurately and efficiently can be daunting.

PayU's Split Settlements feature offers a comprehensive solution to these challenges, empowering businesses to automate payment distributions while offering the same best-in-class payments experience.

## What is PayU Split Settlements?

PayU Split Settlements is an advanced payment distribution system that enables businesses to automatically divide transaction amounts between multiple parties involved in a single transaction.

This powerful feature allows marketplace owners, aggregators, and multi-vendor platforms to efficiently manage revenue sharing, commission structures, and disbursements to various stakeholders without manual intervention. The system supports both real-time splitting during transactions and post-transaction splits, giving businesses the flexibility to implement the workflow that best suits their operational needs.

With PayU's robust API integration and user-friendly dashboard, merchants can seamlessly incorporate Split Settlements into their existing payments infrastructure.

## Key Features and Benefits

### 1. Flexible Payment Distribution

PayU Split Settlements offers unparalleled flexibility in how payments are distributed:

- **Multiple Split Methods**: Divide payments using absolute amounts or percentage-based allocations.
- **Real-Time and Post-Transaction Splits**: Choose to split funds during the transaction or afterward.
- **Customizable Commission Structures**: Implement complex revenue-sharing models with ease.
- **Automated Settlements and Reconciliation**: Eliminate time-consuming manual payment settlements and reconciliations.

### 2. Improved Transparency and Stakeholder Satisfaction

Split Settlements creates a transparent ecosystem that benefits all participants:

- **Clear Visibility**: All parties can track their portion of transactions through their respective dashboards.
- **Faster Disbursements**: Accelerate payments to vendors and service providers.
- **Detailed Reporting**: Access comprehensive split transaction records.
- **Refund Management**: Support for complex refund scenarios involving multiple parties.

## Industry Applications

PayU Split Settlements serves diverse industries with specific payment distribution needs:

### E-Commerce Marketplaces

- Automatically split customer payments between the platform and multiple sellers while managing commissions, discounts, and taxes in a single transaction.

### Travel Aggregators

- Split payments between hotels, airlines, and experience providers while retaining platform fees.

### Insurance Aggregators

- Manage premium distributions between multiple insurance providers and the platform seamlessly.

### TSPs/ERPs/SaaS Providers

- Handle payments for your clients and route them seamlessly.

## Getting Started with Split Settlements

Implementing PayU Split Settlements is straightforward:

1. **Account Setup**: Register for a PayU merchant account and complete KYC requirements. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
2. **Feature Activation**: Enable Split Settlements through the PayU dashboard. For more information, refer to [Activate Split Settlements](doc:activate-split-settlements).
3. **Sub-Account Configuration**: Add and manage child merchants or sub-accounts. For more information, refer to the following:
   - [Adding Sub-Accounts](doc:adding-sub-accounts)
   - [Manage Sub-Accounts](doc:manage-sub-accounts)
4. **API Integration**: Choose between dashboard-based management or API integration. For more information, refer to [Integration APIs for Split Settlements](doc:api-integration-for-split-settlements).
5. **Testing**: Validate your implementation in the PayU sandbox environment.
6. **Go Live**: Launch your integrated Split Settlements solution with confidence.

## APIs used in Split Settlements integration

<Table>
  <thead>
    <tr>
      <th>
        API
      </th>

      <th>
        Purpose
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ### Child Merchant Onboarding
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Get Client Token API](ref:get-client-token-api)
      </td>

      <td>
        Generate a Hub OAuth token with `refer_child_merchant` or `fetch_child_merchants` scope for child-merchant onboarding and listing.
      </td>
    </tr>

    <tr>
      <td>
        [Create Child Merchant API](ref:create-child-merchant-api)
      </td>

      <td>
        Onboard child merchants (sub-accounts) and update their bank details.
      </td>
    </tr>

    <tr>
      <td>
        [Sub Account Listing API](ref:sub-account-listing-api)
      </td>

      <td>
        Fetch all child merchant details linked to a parent merchant. **Used in:** [Fetch Child Merchants Details](doc:fetch-child-merchants-details-1), [Integration APIs for Split Settlements](doc:api-integration-for-split-settlements).
      </td>
    </tr>

    <tr>
      <td>
        ### \_payment API Split Payment
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Absolute Split During Transaction](ref:absolute-split-during-transaction)
      </td>

      <td>
        Split a payment by fixed amount among child merchants at transaction time using the `_payment` API. **Used in:** [Absolute Split During Transaction Integration](doc:absolute-split-during-transaction-integration), [Create the Split](doc:create-the-split).
      </td>
    </tr>

    <tr>
      <td>
        [Split by Percentage During Transaction](ref:split-by-percentage-during-transaction)
      </td>

      <td>
        Split a payment by percentage among child merchants at transaction time using the `_payment` API. **Used in:** [Split by Percentage During Transaction Integration](doc:split-by-percentage-during-transaction-integration), [Create the Split](doc:create-the-split).
      </td>
    </tr>
    <tr>
      <td>
        [Absolute Split After Transaction](ref:absolute-split-after-transaction)
      </td>

      <td>
        Split a completed transaction by fixed amount using the `payment_split` command.
      </td>
    </tr>

    <tr>
      <td>
        [Split by Percentage after Transaction](ref:split-by-percentage-after-transaction)
      </td>

      <td>
        Split a completed transaction by percentage using the `payment_split` command.
      </td>
    </tr>

    <tr>
      <td>
        ### Release Settlement&#x20;
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Release Settlement API](ref:release_settlement_api)
      </td>

      <td>
        Release blocked settlement amounts for child merchants in the aggregator workflow.
      </td>
    </tr>

    <tr>
      <td>
        [Settlement Reconciliation API](ref:settlement-reconciliation-api)
      </td>

      <td>
        Retrieve settlement details for a given date range.
      </td>
    </tr>

    <tr>
      <td>
        ### Get Transaction  Info&#x20;
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Get Aggregator/Parent Transaction Info API](ref:get_aggregator_parent_transaction_info_api)
      </td>

      <td>
        Retrieve split allocation details for a parent transaction.
      </td>
    </tr>

    <tr>
      <td>
        [Get Child/Parent Split Transaction Info API](ref:get_child_parent_split_transactions_info_api)
      </td>

      <td>
        Retrieve split transaction details for child or parent merchants.
      </td>
    </tr>

    <tr>
      <td>
        [Get Split Info API](ref:get_split_info_api)
      </td>

      <td>
        Fetch split information for a given transaction. **Used in:** [Integration APIs for Split Settlements](doc:api-integration-for-split-settlements), [Create the Split](doc:create-the-split).
      </td>
    </tr>

    <tr>
      <td>
        ### Refund  Info
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Refund Transaction API](ref:refund_transaction_api)
      </td>

      <td>
        Process refunds with `var8` JSON specifying per-child refund amounts.
      </td>
    </tr>

    <tr>
      <td>
        [Refund Status API for Split Payments](ref:refund-status-api-for-split-payments)
      </td>

      <td>
        Check refund status for split-payment transactions.
      </td>
    </tr>

    <tr>
      <td>
        [Get All Refunds from Transaction IDs](ref:get_all_refunds_from_transaction_ids_api)
      </td>

      <td>
        Retrieve all refunds associated with given transaction IDs.
      </td>
    </tr>
  </tbody>
</Table>

<br />