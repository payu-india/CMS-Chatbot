---
title: Manage Virtual Accounts
deprecated: false
hidden: true
metadata:
  robots: index
---
Use these APIs to create and manage **Virtual Accounts (VAs)** for [Virtual-Account Based Local Wire Transfers](doc:virtual-account-based-local-wire-transfers). Each VA is a dedicated collection account that payers in India can credit through NEFT, RTGS, or IMPS.

Authenticate every request with a salt-based **Authorization** header. For the hash construction, refer to the **Authorization Logic in Header** section on each API page.

## APIs

| API                                                                        | Method | Endpoint              | Purpose                                     |
| -------------------------------------------------------------------------- | ------ | --------------------- | ------------------------------------------- |
| [Create Virtual Account API](ref:create-virtual-account-api-pacb)          | POST   | `/v2/virtualAccounts` | Provision a VA for a sub-merchant MID       |
| [Get Virtual Accounts API](ref:get-virtual-accounts-api-pacb)              | GET    | `/v2/virtualAccounts` | List VAs for a sub-merchant MID (paginated) |
| [Update Virtual Account API](ref:update-virtual-account-api-pacb)          | PATCH  | `/v2/virtualAccounts` | Rename a VA or set `isActive` to deactivate |
| [List Virtual Account Deposits API](ref:list-virtual-account-deposits-api) | GET    | `/v2/virtualAccounts` | List the VA deposits                        |

## Environment

| Environment | Base URL                                              |
| ----------- | ----------------------------------------------------- |
| Test        | `https://uatoneapi.payu.in/payout/v2/virtualAccounts` |
| Production  | `https://oneapi.payu.in/payout/v2/virtualAccounts`    |

For [Update Virtual Account API](ref:update-virtual-account-api-pacb), pass `virtualAccountId` as a query parameter on the base URL.

## Common query parameters

| Parameter          | Required    | Description                                                                                                                                                       |
| ------------------ | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `virtualAccountId` | Conditional | PayU-assigned VA identifier or virtual account number (for example `PURW2231266`). Required for [Update Virtual Account API](ref:update-virtual-account-api-pacb) |
| `pageOffset`       | Optional    | Page number (1-based). Default: `1`                                                                                                                               |
| `pageSize`         | Optional    | Records per page. Default: `10`. Maximum: `50`                                                                                                                    |

## Common response fields

| Field    | Description                                                                |
| -------- | -------------------------------------------------------------------------- |
| `status` | `0` for success, `1` for failure                                           |
| `data`   | Response payload object or array                                           |
| `msg`    | Human-readable message (for example on create or update success)           |
| `code`   | Error code when `status` is `1` (for example `1001` for validation errors) |

<br />
