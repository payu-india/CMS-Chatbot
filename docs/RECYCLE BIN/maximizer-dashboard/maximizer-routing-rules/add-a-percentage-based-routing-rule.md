---
title: Add a Percentage-Based Routing Rule
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
You can add a percentage-based routing rule involving single or multiple payment methods. This section describes how to add a routing rule with examples.

## Add a rule for Net Banking

1. Select the **Routing Rules** tab on the Maximizer Dashboard.

   The **Routing Rules** tab is displayed similar to the following screenshot (without any existing rules).

<Image align="center" className="border" border={true} src="https://files.readme.io/6022c93-Screenshot_2024-06-19_at_10.18.01_AM.png" />

<Image align="center" width="00px" src="https://files.readme.io/3e1f65b-Screenshot_2024-06-19_at_10.18.01_AM.png" />

2. Click **Create rule now**.

The *Create Custom Rule* page with the *Rule Configuration* screen is displayed.

3. Select the **Debit Cards** tab.

The **Debit Cards** tab is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/e8d27a3e354873bb690d08bb64dec1760e5a96ebb73105d3a6c10887c4a894ff-maximiser_percentage_based_routing_cards.png" />

4. Perform the steps in in the **Card Based** or **BIN based** tab:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Tab
      </th>

      <th>
        Steps
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Card Based
      </td>

      <td>
        a. Click the **Issuer Bank**drop-down list in and select the banks for which routing rules apply.\
        b. Click the**Card type**drop-down list and select the card type.\
        c. In **Rule 1** pane, enter the condition using the **When** and**Is** drop-down lists.\
        d. . In **Rule 1** pane, enter the amount range in the **Transaction Amount Range** field. For more information, refer to [Include an Amount Range with a Routing Rule](doc:include-an-amt-range-with-routing-rule) .\
        e. Click the **Add Another Rule** button to add another rule and repeat step c and d.\
        ![](https://files.readme.io/19eb874dd78bc12e79d134917006d605e999494feedf8d967fc23151d831f094-maximiser_percentage_based_routing_cards.png)
      </td>
    </tr>

    <tr>
      <td>
        BIN based
      </td>

      <td>
        a. Click the Upload button.  

        * \*Not&#x65;**: Click the Download button in the Sample File pane and include the BIN list.\
          ![](https://files.readme.io/4a190d95f781f98500a7b0bc88bae8bbb67b798feb004dc8b756933261a9c793-maximiser_percentage_based_routing_cards_bin.png)\
          b. Click the **&#x41;dd Another Rule\*\* button to add another rule.\
            

        > �![](https://files.readme.io/0b0362640594519e0bb83187187bb6ed5cbe6862692143649c4ecf236ea2f297-maximizer_cards_bin_add_another_rule.png)g)\
        > c. In **Rule 1** pane, enter the condition using the **When**, **Is**  and **Then**drop-down lists.  
      </td>
    </tr>
  </tbody>
</Table>

<Maximizer_Alert />

5. Click **Next** after you have selected the banks for Debit Cards routing.

The *Payment Aggregator* screen is displayed.

6. Select the **Percentage Based Routing** tab.

<Image align="center" className="border" border={true} src="https://files.readme.io/734eae81cf028f754f485e3a2ac6cbbb1c90f8693e32dc9da0472b8d9f03652c-maximiser_percentage_based_routing.png" />

7. Enter the percentage for each payment aggregator must have atleast 1 as value.

> **Notes**: 
>
> * Enter only whole number (without decimals)
> * Enter atleast 1% for an aggregator
> * Cumulative of all the aggregator must sum too 100.

8. Select the **Set Custom Baseline** check box to configure custom baseline for this rule.

> 📘 Baseline Reference:
>
> For detailed understanding on baseline, refer to [Understanding Baseline Logic](doc:understanding-baseline-logic).

9. Click **Next**.

The *Rule Guidelines* screen is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/bf1d084abe54423a78ad5246ecd1eb20309c66473368c507ea80e5cfe222cf3a-image_3.png" />

10. Enter the name for the rule in the **Title** field.
11. Select the date range in the **Activation duration** field for which the rule will be active.
12. Click **Publish Now** to create the rule.

   The rule is added to the **Routing Rules** tab of Maximizer dashboard.

<Image align="center" className="border" border={true} src="https://files.readme.io/df9389a-Screenshot_2024-06-19_at_11.00.27_AM.png" />

1. Click the rule to view the details of the rule.

<Image align="center" className="border" border={true} src="https://files.readme.io/f56667eceba21815def4a52cf216892b8f0611a8ff35628f7da151adcad2fb55-dashboard-maximizer-rule-details.png" />