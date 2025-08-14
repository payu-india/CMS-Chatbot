---
title: Install and Configure Odoo Plugin
deprecated: false
hidden: false
metadata:
  robots: index
---
After installing Odoo on your local machine or server, follow these steps for each operating system to configure the PayU custom add-on or plugin.

## Prerequisites

Before you begin, ensure that:

* Odoo is installed and running on your local machine or server
* You have administrative access to the server (Linux/Windows)
* You have access to Odoo's configuration files
* You have a PayU merchant account (or can create one during setup)

<Callout icon="📘" theme="info">
  **Note**: Developer Mode must be enabled in Odoo to proceed with eCommerce and PayU module setup.
</Callout>

## Installation Guide for Linux-based Servers

To install the PayU custom add-on on Linux-based servers:

### Step 1: Create custom add-ons directory structure

Create the directory structure for custom add-ons:

```bash
mkdir /opt/odoo/custom_addons
```

### Step 2: Clone the PayU repository

Clone the GitHub repository into the newly created folder:

```bash
cd /opt/odoo/custom_addons
git clone https://github.com/boxpay-tech/payu-connectors.git
```

After cloning, verify that the `Payment_payu` folder exists in the directory.

### Step 3: Configure Odoo

Modify the `odoo.conf` file to include the path to the custom addons folder:

```bash
sudo nano /etc/odoo/odoo.conf
```

Add the custom addons path to the `addons_path` configuration:

```bash
addons_path = /usr/lib/python3/dist-packages/odoo/addons,/opt/odoo/custom_addons
```

### Step 4: Restart Odoo service

Restart the Odoo service to apply the changes:

```bash
sudo systemctl restart odoo
```

## Installation Guide for Windows

Follow these steps to install the PayU Custom Addon on Windows systems:

### Step 1: Create custom add-ons folder

Create a folder in the same drive where Odoo is installed (preferably in the `C:/` drive):

```
C:/custom_addons
```

### Step 2: Navigate to Odoo Installation

Open Odoo's installed folder and navigate to the `server` folder inside the installation directory.

### Step 3: Clone PayU repository

Clone the PayU repository in your custom add-ons folder:

```bash
cd C:/custom_addons
git clone https://github.com/boxpay-tech/payu-connectors.git
```

### Step 4: Configure Odoo

Modify the `odoo.conf` file located in the `server` folder to include the path of the custom\_addons folder under the `addons_path`:

```
addons_path = C:/Program Files/Odoo/server/addons,C:/custom_addons
```

### Step 5: Save Configuration

Save the changes to the `odoo.conf` file.

### Step 6: Restart Odoo service

Restart the Odoo service using Microsoft Windows Services:

1. Open **Services** from the **Start** menu.
2. Search and select the **Odoo** service.
3. Right-click and select **Restart**

## Setup Odoo for eCommerce

After installing the PayU custom add-on, configure Odoo for eCommerce function:

### Step 1: Enable Developer Mode

1. Open Odoo service hosted locally or on a remote server. The **Apps** section is on the Dashboard.
2. Go to the **Home Menu** in the upper left-corner.
3. Navigate to the **Settings** section.
4. Activate **Developer Mode**.

<Callout icon="📘" theme="info">
  **Note**: Developer Mode is required to access advanced configuration options.
</Callout>

### Step 2: Install Required Modules

Return to the **Apps** section and activate the following modules:

* **Website** module
* **eCommerce** module

### Step 3: Install PayU Payment Provider

1. In the **Apps** section, search for "payu" and select it.
2. Activate the **PayU Payment Provider** module

### Step 4: Configure PayU Payment Provider

Configure Pay\U as the payment provider:

1. Use the **Home Menu** to navigate to **Configuration > Payment Providers**
2. Find and activate **PayU** as the Payment Provider
3. A credential configuration page will appear

### Step 5: Configure Transaction Credentials

Configure credentials for payment transactions:

<Callout icon="📘" theme="info">
  **Reference**: You can obtain your merchant keys and Salt from your PayU Merchant Dashboard. For more information, refer to any of the following based on the Test or Production environment:

  * [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
  * [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
</Callout>

#### For Test Transactions

1. Select state: **"Test Mode"**
2. Enter your Test merchant key.
3. Enter your Test merchant Salt.
4. Click **Save** to enable test payment transactions

#### For Live Transactions

1. Select state: **"Enabled"**
2. Enter your Production merchant key.
3. Enter your Production merchant Salt.
4. Click **Save** to enable live payment transactions.

## Verification

To verify the installation:

1. Ensure the PayU module is displayed in your installed apps.
2. Check that PayU is available as a payment option in your eCommerce checkout.
3. Perform a test transaction to confirm functionality.

## Next Steps

After successful installation and configuration:

* [Configure Payment Methods](https://docs.payu.in/docs/payment-methods)
* [Set Up Webhooks](https://docs.payu.in/docs/webhooks)
* [Test Your Integration](https://docs.payu.in/docs/testing)