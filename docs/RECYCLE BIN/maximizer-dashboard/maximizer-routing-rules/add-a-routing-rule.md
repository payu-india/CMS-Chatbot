---
title: Add a SRT Routing Rule
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
You can add a Success Rate Based Routing (SRT) involving single or multiple payment methods. This section describes how to add a routing rule with examples.

## Add a rule for Net Banking

1. Select the **Routing Rules** tab on the Maximizer Dashboard.

   The **Routing Rules** tab is displayed similar to the following screenshot.

<Image align="center" className="border" border={true} src="https://files.readme.io/8ad253e1178c09d9f6923be153fb80c7e6df77ada73e148bb2ef398c1a0e34a7-Screenshot_2024-12-18_at_2.15.05_PM.png" />

<Image align="center" width="00px" src="https://files.readme.io/3e1f65b-Screenshot_2024-06-19_at_10.18.01_AM.png" />

2. Click **Create rule now**.

The *Create Custom Rule* page with the *Rule Configuration* screen is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/7e25a5fd7d942b6132e5f624be952808364281cb6899a01d5f362c5e3d1347b6-Screenshot_2024-12-18_at_2.16.54_PM.png" />

3. Select the **Netbanking** tab.

The **Netbanking** tab is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/af1ee8fcf3215bdf6f161d76e9328415fff32c920d760b9f45cf00204e8412f5-Screenshot_2024-12-18_at_2.17.40_PM.png" />

4. Click the **Select Issuer Bank** drop-down list select the banks for which routing rules.
5. Enter the amount range in the **Transaction Amount Range** field. For more information, refer to [Include an Amount Range with a Routing Rule](doc:include-an-amt-range-with-routing-rule).

<Maximizer_Alert />

<Image align="center" className="border" border={true} src="https://files.readme.io/df5d54349c0111131efb4c77bdbfeef2611be04d1dc9fa0b01cf483de92bfc86-maximiser_dashboard_rule_amt_range.jpg" />

5. Click **Next** after you have selected the banks for Net Banking routing.

The *Payment Aggregator* screen is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/d2ba32823bee06da358eaa66d52f8da52915aa9da464bb8f2453ff8821e4f6ad-maximizer_uccess_rate_routing_rule.png" />

6. Select **Success Based Routing** tab (if required).
7. Remove the payment aggregators using the remove button (**X**) and then click **Next**.

The *Rule Guidelines* screen is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/e24c174-Screenshot_2024-06-19_at_11.00.09_AM.png" />

8. Enter the name for the rule in the **Title** field.
9. Click **Create Rule** to create the rule.

   The rule is added to the **Routing Rules** tab of Maximizer dashboard.

<Image align="center" className="border" border={true} src="https://files.readme.io/df9389a-Screenshot_2024-06-19_at_11.00.27_AM.png" />

## Add a rule involving multiple payment methods

1. Select the **Routing Rules** tab on the Maximizer Dashboard.

   The **Routing Rules** tab is displayed.
2. Click **Create rule now**.

The *Create Custom Rule* page with the *Rule Configuration* screen is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/a64fb402d2982e56bd4cd9604234cde42f94fe0ad37893fbd2710676133ba73b-Screenshot_2024-12-18_at_2.16.54_PM.png" />

3. Select the **Wallet** tab.
4. Click the **Select Issuers**drop-down list select the wallets for which routing rules.

   <Image align="center" className="border" border={true} src="https://files.readme.io/7be74f83d9b1a88d794c5626f18d7e19adc1b994e62804985b448005397eb4f5-Screenshot_2024-12-18_at_2.19.50_PM.png" />
5. Select the **Netbanking** tab.

The **Netbanking** tab is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/2c7acaa3dfad2201e45fc2f7aadda30b39fc943eafdc793f7b91100733a94ab8-Screenshot_2024-12-18_at_2.17.40_PM.png" />

4. Click the **Select Issues Bank** drop-down list select the banks for which routing rules.
5. Enter the amount range in the . For more information, refer to [Include an Amount Range with a Routing Rule](doc:include-an-amt-range-with-routing-rule).

<Image align="center" className="border" border={true} src="https://files.readme.io/df5d54349c0111131efb4c77bdbfeef2611be04d1dc9fa0b01cf483de92bfc86-maximiser_dashboard_rule_amt_range.jpg" />

4. Click **Next**.

The *Payment Aggregator* screen is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/00ba2eb24804b541485ec9f10363261465bc0477d7b86056ee69d2efb47014f1-maximizer_uccess_rate_routing_rule.png" />

8. Select **Success Based Routing** tab (if required).
9. Remove the payment aggregators using the remove button (**X**) and then click **Next**.

   The *Rule Guidelines* screen is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/e24c174-Screenshot_2024-06-19_at_11.00.09_AM.png" />

10. Enter the name for the rule in the **Title** field.
11. Click **Create Rule** to create the rule.

   The rule is added to the **Routing Rules** tab of Maximizer dashboard.

<Image align="center" className="border" border={true} src="https://files.readme.io/df9389a-Screenshot_2024-06-19_at_11.00.27_AM.png" />

## Add a rule for all payment methods

1. Select the **Routing Rules** tab on the Maximizer Dashboard.

   The **Routing Rules** tab is displayed.
2. Click **Create rule now**.

The *Create Custom Rule* page with the *Rule Configuration* screen is displayed with the **All Payment Methods** tab selected (by default).

<Image align="center" className="border" border={true} src="https://files.readme.io/715e6856d0311f51c9b525db5891f15066bcb0de83d46d83802153d960e1c757-Screenshot_2024-12-18_at_2.20.40_PM.png" />

3. Select the **All Payment** tab (if required).
4. Click **Next**.

The *Payment Aggregator* screen is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/23c0057cf125fc4317ee1020a682be5462d33571ac67d72fcc8aa3126653d53b-maximizer_uccess_rate_routing_rule.png" />

5. Select **Success Based Routing** tab (if required).
6. Remove the payment aggregators using the remove button (**X**) and then click **Next**.

   The *Rule Guidelines* screen is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/e24c174-Screenshot_2024-06-19_at_11.00.09_AM.png" />

7. Enter the name for the rule in the **Title** field.
8. Click **Create Rule** to create the rule.

   The rule is added to the **Routing Rules** tab of Maximizer dashboard.

<Image align="center" className="border" border={true} src="https://files.readme.io/df9389a-Screenshot_2024-06-19_at_11.00.27_AM.png" />