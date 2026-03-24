---
title: '          Install and Configure Odoo Plugin'
deprecated: false
hidden: false
metadata:
  title: Install and Configure Odoo Plugin
  keywords:
    - Install Odoo Plugin
    - Configure Odoo Plugin
    - Odoo Plugin
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
  **Notes**:

  * **Developer** mode must be enabled in Odoo to proceed with eCommerce and PayU module setup.
  * This plugin has been developed and tested on Odoo 18, so it is recommended using version 18 or above for optimal compatibility and performance.
</Callout>

## Install on Linux OS

To install the PayU custom add-on on Linux-based servers:

1. Create the directory structure for custom add-ons:

```bash
mkdir /opt/odoo/custom_addons
```

2. Clone the GitHub repository into the newly created folder:

```bash
cd /opt/odoo/custom_addons
git clone https://github.com/boxpay-tech/payu-connectors.git
```

After cloning, verify that the `Payment_payu` folder exists in the directory.

3. Modify the `odoo.conf` file to include the path to the custom addons folder:

```bash
sudo nano /etc/odoo/odoo.conf
```

4. Add the custom add-ons path to the `addons_path` configuration:

```bash
addons_path = /usr/lib/python3/dist-packages/odoo/addons,/opt/odoo/custom_addons
```

<Image align="center" src="https://files.readme.io/0274ecf079523191036c2916f11369ecefca17034db284abc05cec8322eb9717-odoo_setup_image_1_page_3.png" />

5. Restart the Odoo service to apply the changes:

```bash
sudo systemctl restart odoo
```

## Install on Windows OS

Follow these steps to install the PayU Custom Addon on Windows systems:

1. Create a folder in the same drive where Odoo is installed (preferably in the `C:/` drive):

```
C:/custom_addons
```

<Image align="center" src="https://files.readme.io/969cfc877faafafe1a3afa8306174742c8259b13f16854d2342be6c6bcbdbbff-odoo_setup_image_2_page_4.png" />

2. Open Odoo's installed folder and navigate to the `server` folder inside the installation directory.

<Image align="center" src="https://files.readme.io/bbf6d1cf1e13450733b682013d0a4dcfec3af9bd6f9d7911a71fb276deb39814-odoo_setup_image_3_page_4.png" />

3. Clone the PayU repository in your custom add-ons folder:

```bash
cd C:/custom_addons
git clone https://github.com/boxpay-tech/payu-connectors.git
```

4. Modify the `odoo.conf` file located in the `server` folder to include the path of the custom_addons folder under the `addons_path`:

```
addons_path = C:/Program Files/Odoo/server/addons,C:/custom_addons
```

<Image align="center" src="https://files.readme.io/dae70cd244f868df1765d4ef118b99759c054ee8669ad0f3e0f048b373495f2c-odoo_setup_image_6_page_6.png" />

5. Save the changes to the `odoo.conf` file.
6. Restart the Odoo service using Microsoft Windows Services:
   * Open **Services** from the **Start** menu.
   * Search and select the **Odoo** service.
   * Right-click and select **Restart**

<Image align="center" className="border" border={true} src="https://files.readme.io/7188a3579e8445d4422323fe8bf57915a19d16f3288f45e7d61ca951024bd2cf-odoo_setup_image_7_page_6.png" />

## Setup Odoo for eCommerce

After installing the PayU custom add-on, configure Odoo for eCommerce function:

### Step 1: Enable Developer Mode

1. Open Odoo service hosted locally or on a remote server.

The **Apps** section is displayed on the Dashboard.

<Image align="center" className="border" border={true} src="https://files.readme.io/4b0594bed1ce7a961e2309d100de443677ceb51d3da665ca4c55a3b369281955-odoo_setup_image_8_page_7.png" />

2. Select the **Home** menu and choose **Settings** in the upper left-corner.

<Image align="center" className="border" border={true} src="https://files.readme.io/b00bf1271cd915cab1f83053fc523607cdea7ffcd6583c354f0df28bae702e7a-odoo_setup_image_9_page_7.png" />

The _Settings_ page is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/5a5fa04583e17c8e863bf617046f77a83fac227d7df66d8386e1f90ef301bc53-odoo_setup_image_10_page_8.png" />

3. Clicl **Activate the Developer Mode**.

<Callout icon="📘" theme="info">
  **Note**: Developer Mode is required to access advanced configuration options.
</Callout>

### Step 2: Install required modules

Return to the **Apps** section and activate the following modules:

* **Website** module
* **eCommerce** module

<Image align="center" className="border" border={true} src="https://files.readme.io/93825dd138e2818c9f3228a10d80229a3c592c386d2738238cfd21a2a004e955-odoo_setup_image_11_page_8.png" />

After activating these apps, your customers will be able access the **Shop** section similar to the following screenshot.

<Image align="center" className="border" border={true} src="https://files.readme.io/793fbf8a759bb246166e605cf88db9f8e0719b06060c8e6a07ed6881d0bd81c4-odoo_setup_image_12_page_9.png" />

<br />

### Step 3: Install PayU plugin

1. In the **Apps** section, search for "payu" and select it.

<Image align="center" className="border" border={true} src="https://files.readme.io/248806062e9dcf87a1bb7a0e2a1a75e0bfa3b6851c5a8c01b8dff02bb5f95b6c-odoo_setup_image_13_page_9.png" />

2. Click **Activate** on the **PayU Payment Provider** tile.

### Step 4: Configure PayU as payment provider

To configure PayU as the payment provider:

3. From the **Home** page, navigate to **Configuration > Payment Providers**.

<Image align="center" className="border" border={true} src="https://files.readme.io/9f16337e2485d220d1610f26daa4dd67cc7930f8478a9274dfc573f2dd0fc628-odoo_setup_image_15_page_10.png" />

<br />

4. Find **PayU** and click **Activate** on the **PayU** tile to activate as the payment provider.

<Image align="center" className="border" border={true} src="https://files.readme.io/2142b4864cb65e4aaeb2bf7260d3387de724d3467c3c7c88cbfb1052a1f1b973-odoo_setup_image_16_page_11.png" />

You will be redirected to PayU Configuration page on Odoo.

<Image align="center" className="border" border={true} src="https://files.readme.io/9dca27d8c89421df35160711c39585c38cc98bf81c1db7c38efc7f25efc0bc33-odoo_setup_image_17_page_11.png" />

### Step 5: Configure Key and Salt credentials

To configure credentials for payment transactions:

1. Select **Enabled** from the **State** field.
2. Perform any of the following procedures as per the environment you wish to configure and then click **Save Credentials**.

* [For Test Transactions](#for-test-transactions)
* [For Live Transaction](#for-live-transactions)

<Callout icon="📘" theme="info">
  **Reference**: You can obtain your merchant keys and Salt from your PayU Merchant Dashboard. For more information, refer to any of the following based on the Test or Production environment:

  * [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
  * [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)

  If you do not have a PayU account, sign up for a merchant account. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Callout>

#### For Test Transactions

To configure the key/Salt for testing the transactions in Test or Sandbox environment:

1. Select state: **"Test Mode"**
2. Enter your Test merchant key.
3. Enter your Test merchant Salt.
4. Click **Save** to enable test payment transactions

<Image align="center" className="border" border={true} src="https://files.readme.io/55cd20c088e5615b7bad9b736d9bb0ef47f30f84f0dab292bd855ab5d21e0649-odoo_setup_image_19_page_12.png" />

#### For Live Transactions

To configure the key/Salt for collecting payments or live transactions or production environment:

1. Select state: **"Enabled"**
2. Enter your Production merchant key.
3. Enter your Production merchant Salt.
4. Click **Save** to enable live payment transactions.

## Verification

To verify the installation:

1. Ensure the PayU module is displayed in your installed apps.
2. Check that PayU is available as a payment option in your eCommerce checkout.
3. Perform a test transaction to confirm functionality.