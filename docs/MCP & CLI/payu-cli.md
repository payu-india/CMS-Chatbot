---
title: PayU CLI
deprecated: false
hidden: false
metadata:
  robots: index
---
The PayU CLI lets you interact with PayU dashboard APIs directly from your terminal. Use it to create payment links, look up transactions, check settlements, generate reports, and more — without opening the dashboard.

## Prerequisites

Before you install the PayU CLI, keep the following credentials ready:

| Credential    | Where to find it                                           |
| :------------ | :--------------------------------------------------------- |
| Client ID     | PayU Dashboard > **Developer** > **API Details**           |
| Client Secret | PayU Dashboard > **Developer** > **API Details**           |
| Merchant ID   | Your PayU merchant identifier (MID) shown on the dashboard |

For step-by-step instructions to retrieve your client ID and client secret, see [Get Client ID and Secret from Dashboard](doc:get-client-id-and-secret-from-dashboard).

## Install the PayU CLI

### Install on macOS and Linux

To install the PayU CLI on macOS or Linux:

1. Open a terminal window.
2. Run the following command:

   ```plaintext CLI
   > curl -fsSL https://payu-intrepos.github.io/payu-cli/install.sh | bash
   Downloading payu-cli for darwin/arm64...
   Installed to /Users/you/.local/bin/payu
   ```

   The installer downloads the correct binary for your operating system and architecture and installs it to `~/.local/bin`.

### Install on Windows

To install the PayU CLI on Windows:

1. Open PowerShell.
2. Run the following command:

   ```plaintext CLI
   > irm https://payu-intrepos.github.io/payu-cli/install.ps1 | iex

   Downloading payu-cli for windows/amd64...
   Installed to C:\Users\you\AppData\Local\payu-cli\payu.exe
   Added to user PATH.
   ```

   The installer extracts the binary to `%LOCALAPPDATA%\payu-cli` and adds it to your PATH.

### Verify the Installation

To confirm that the PayU CLI is installed correctly, run:

```plaintext CLI
> payu version

payu-cli 1.0.0
```

## Configure Your API Credentials

Configure the CLI with your API credentials before you make requests.

### Configure on macOS and Linux

To set your credentials on macOS or Linux:

1. Run the following command, replacing the placeholder values with your credentials:

   ```plaintext CLI
   > payu config set \
   --client-id YOUR_CLIENT_ID \
   --client-secret YOUR_CLIENT_SECRET \
   --merchant-id YOUR_MERCHANT_ID

   Configuration saved for profile: default
   Environment: production
   ```

2. If you omit the flags, the CLI prompts you for each value interactively.

### Configure on Windows

To set your credentials on Windows in PowerShell:

```plaintext CLI
> payu config set `
--client-id YOUR_CLIENT_ID `
--client-secret YOUR_CLIENT_SECRET `
--merchant-id YOUR_MERCHANT_ID

Configuration saved for profile: default
Environment: production
```

### Verify Your Setup

To confirm that your credentials are configured correctly, run:

```plaintext CLI
> payu config show

Profile:     default
Environment: production
Merchant ID: 8235901
Client ID:   abc123def456
Client Secret: ••••a1b2
```

> 📘 **Note:**&#x20;
>
> Your client secret is displayed masked (for example, `••••a1b2`).

## Command Reference

Run any command without arguments to see its help text and available subcommands.

### Account Management

| Command                      | Description                      |
| :--------------------------- | :------------------------------- |
| `payu account list`          | List all saved merchant accounts |
| `payu account show`          | Show active account details      |
| `payu account add`           | Add a new merchant account       |
| `payu account switch <name>` | Switch the active account        |
| `payu account remove <name>` | Remove a merchant account        |

### Payment Links

| Command                 | Description                          |
| :---------------------- | :----------------------------------- |
| `payu pay create-link`  | Create a new payment link            |
| `payu pay send <id>`    | Send a payment link via email or SMS |
| `payu pay status <id>`  | Get payment link details             |
| `payu pay list`         | List all payment links               |
| `payu pay update <id>`  | Update a payment link                |
| `payu pay invoice <id>` | Get invoice transactions             |

### Transactions

| Command                        | Description                          |
| :----------------------------- | :----------------------------------- |
| `payu txn get <id>`            | Get details of a single transaction  |
| `payu txn list --from --to`    | List transactions with filters       |
| `payu txn summary --from --to` | Get aggregated transaction analytics |

### Refunds

| Command               | Description                  |
| :-------------------- | :--------------------------- |
| `payu refund search`  | Search refunds with filters  |
| `payu refund summary` | Get refund analytics summary |

### Settlements

| Command               | Description            |
| :-------------------- | :--------------------- |
| `payu settlement get` | Get settlement details |

### Reports

| Command                     | Description                                                            |
| :-------------------------- | :--------------------------------------------------------------------- |
| `payu report create <type>` | Generate a CSV report (transactions, settlements, refunds, or payouts) |
| `payu report get <id>`      | Download a generated report                                            |

## Examples

### Create a Payment Link

To create a payment link for a customer:

```plaintext CLI
> payu pay create-link \
--amount 1500 \
--desc 'Invoice #1042' \
--name 'Rahul Sharma' \
--email 'rahul@example.com' \
--phone '+919876543210'

Payment link created successfully.
Link ID:    PL_abc123xyz
Short URL:  https://payu.in/l/abc123
Amount:     ₹1500.00
Status:     active
```

### List Today's Transactions

To list all captured transactions for the current day:

```plaintext CLI
> payu txn list \
--from '2025-05-29 00:00:00' \
--to '2025-05-29 23:59:59' \
--status captured

TXN_ID              AMOUNT    MODE   STATUS    DATE
403993715534343565  ₹1500.00  UPI    captured  2025-05-29 14:32:11
403993715534343566  ₹2500.00  CC     captured  2025-05-29 16:05:44
Total: 2 transactions
```

### Filter by Payment Mode and Amount

To list transactions within a date range, filtered by payment mode and amount:

```plaintext CLI
> payu txn list \
--from '2025-05-01 00:00:00' \
--to '2025-05-29 23:59:59' \
--mode UPI,CC \
--min-amount 500 --max-amount 10000

TXN_ID              AMOUNT    MODE   STATUS    DATE
403993715534343567  ₹750.00   UPI    captured  2025-05-12 09:15:22
403993715534343568  ₹3200.00  CC     captured  2025-05-18 11:40:03
Total: 2 transactions
```

### Generate a Transactions Report

To create and download a transactions report:

```plaintext CLI
> payu report create transactions \
--from '2025-05-01 00:00:00' \
--to '2025-05-31 23:59:59'

Report created successfully.
Report ID: RPT_abc123
Status:    processing

payu report get RPT_abc123

Report downloaded to: ./transactions_2025-05.csv
Rows: 1,248
```

### Look Up a Transaction

To retrieve details for a specific transaction:

```plaintext CLI
> payu txn get 403993715534343565

<command result>
Transaction ID: 403993715534343565
Amount:         ₹1500.00
Mode:           UPI
Status:         captured
Customer:       Rahul Sharma
Email:          rahul@example.com
Date:           2025-05-29 14:32:11
```

## Global Flags

The following flags are available across commands:

| Flag               | Description                                              |
| :----------------- | :------------------------------------------------------- |
| `--profile <name>` | Use a specific credential profile instead of the default |
| `--help`           | Show help for any command                                |

## Environments

By default, the CLI connects to PayU production APIs. To use the test (sandbox) environment, configure a separate profile:

```plaintext CLI
> payu config set --env test \
--client-id TEST_ID \
--client-secret TEST_SECRET \
--merchant-id TEST_MID \
--profile test

Configuration saved for profile: test
Environment: test
```

To run a command against the test profile, pass the `--profile` flag:

```plaintext CLI
> payu txn list --profile test --from '2025-05-29 00:00:00' --to '2025-05-29 23:59:59'

TXN_ID              AMOUNT    MODE   STATUS    DATE
403993715534343999  ₹1.00     UPI    captured  2025-05-29 10:00:00
Total: 1 transaction
```

## Troubleshooting

### macOS or Linux: Command not found

If your terminal reports that `payu` is not found, make sure `~/.local/bin` is in your PATH. Add the following line to your shell profile (`~/.bashrc` or `~/.zshrc`):

```plaintext CLI
> export PATH="$HOME/.local/bin:$PATH"
```

Reload your shell profile, and then verify the installation:

```plaintext CLI
> source ~/.zshrc
payu version

payu-cli 1.0.0
```

### Windows: Command not found

The PowerShell installer adds the install directory to your user PATH automatically. If the `payu` command is still not recognized, restart your terminal. You can also manually add `%LOCALAPPDATA%\payu-cli` to your PATH through **System Settings** > **Environment Variables**.

### macOS Keychain Prompt

On first use, macOS might ask for Keychain access permission. Select **Always Allow** to avoid repeated prompts.

### Windows SmartScreen Warning

Windows might show a SmartScreen warning because the binary is not code-signed. Select **More info** > **Run anyway** to proceed with the installation.

### Authentication Errors

If you receive a `401` error, verify that your credentials are correct:

```plaintext CLI
> payu config show

Profile:     default
Environment: production
Merchant ID: 8235901
Client ID:   abc123def456
Client Secret: ••••a1b2
```

<br />