---
title: APIs used in Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used in Split Settlements integration
  robots: index
---
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