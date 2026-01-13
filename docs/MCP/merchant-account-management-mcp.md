---
title: Merchant Account Management - MCP
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Merchant Account Management
deprecated: false
hidden: false
metadata:
  title: Remote MCP for Merchants - Merchant Account Management
  keywords:
    - Merchant Accounts
    - Multi-Merchant
    - Account Switching
    - MCP Account Management
  robots: index
---

PayU Remote MCP supports both single and multiple merchant account configurations. This page explains how to manage your merchant accounts.

## Single Account (Automatic)

If you have access to **one merchant account**, it's automatically selected.

**No action required!**

All your requests will automatically use your single merchant account.

## Multiple Accounts (Manual Selection)

If you have access to **multiple merchant accounts**, you need to select which one to use for your operations.

### Why Selection Is Required

When you have multiple merchant accounts:

* Each account may have different transaction histories
* Refunds and operations are account-specific
* Reports are generated per merchant account

### Available Commands

Use these natural language commands to manage your merchant accounts:

| Command                                        | Description                |
| ---------------------------------------------- | -------------------------- |
| "What merchant accounts do I have access to?"  | List all accounts          |
| "Which merchant account am I currently using?" | Check current account      |
| "Switch to merchant account 180012"            | Switch to specific account |
| "Clear my current merchant selection"          | Clear selection            |

### Example Workflow

**Step 1: List Your Accounts**

```
User: "What merchant accounts do I have access to?"

Response: You have access to the following merchant accounts:
- 180012 (Primary Store)
- 180045 (Online Shop)
- 180078 (Mobile App)
```

**Step 2: Select an Account**

```
User: "Switch to merchant account 180012"

Response: Successfully switched to merchant account 180012 (Primary Store).
All subsequent operations will use this account.
```

**Step 3: Verify Selection**

```
User: "Which merchant account am I currently using?"

Response: You are currently using merchant account 180012 (Primary Store).
```

## Account Selection Caching

> 📘 Note
>
> Your merchant account selection is cached for 1 hour.

### Cache Behavior

* **Duration**: 1 hour from selection
* **Scope**: Per user session
* **Expiration**: Automatic after 1 hour
* **Override**: You can switch accounts anytime

### When Cache Expires

After the cache expires:

1. Your next request will prompt for account selection (if you have multiple accounts)
2. Simply select your preferred account again
3. The selection is cached for another hour

## Clearing Selection

If you want to change accounts before the cache expires:

```
User: "Clear my current merchant selection"

Response: Your merchant selection has been cleared. 
Please select a merchant account for your next operation.
```

## Error: Merchant Selection Required

If you see this error:

```
Error: Merchant selection required. You have multiple merchant accounts.
Please select which account to use.
```

**Solution**: Use the account switching command:

```
"Switch to merchant account [YOUR_MERCHANT_ID]"
```

## Best Practices

1. **Know Your Account IDs** - Keep a list of your merchant account IDs for quick reference
2. **Verify Before Operations** - Check which account is selected before processing refunds or sensitive operations
3. **Use Descriptive Queries** - Include account context in your queries when working with specific accounts

## Next Steps

* [Example Tool Usage](doc:remote-mcp-example-tool-usage) - See examples of operations across accounts
* [Troubleshooting](doc:remote-mcp-troubleshooting) - Get help with account-related issues