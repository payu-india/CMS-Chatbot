---
title: Include an Amount Range with a Routing Rule
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
While creating a SRT, priority or percentage rule, you can add a amount range for a payment method. This section describes how to add a routing rule with Debit Card as an example. 

> 📘 Reference:
> 
> For more information, creating a rule, refer to any of the following:
> 
> - [Add a SRT Routing Rule](https://docs.payu.in/docs/add-a-routing-rule)
> - [Add a Priority-Based Routing Rule](https://docs.payu.in/docs/add-a-routing-rule-with-srt-copy)
> - [Add a Percentage-Based Routing Rule](doc:add-a-percentage-based-routing-rule)

To include an amount range for a routing rule involving debit cards:

1. Select the **Routing Rules** tab on the Maximizer Dashboard.

   The **Routing Rules** tab is displayed similar to the following screenshot (without any existing rules).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6022c93-Screenshot_2024-06-19_at_10.18.01_AM.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3e1f65b-Screenshot_2024-06-19_at_10.18.01_AM.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "00px"
    }
  ]
}
[/block]


2. Click **Create rule now**.

The _Create Custom Rule_ page with the _Rule Configuration_ screen is displayed.

3. Select the **Debit Cards** tab.

The **Debit Cards** tab is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e8d27a3e354873bb690d08bb64dec1760e5a96ebb73105d3a6c10887c4a894ff-maximiser_percentage_based_routing_cards.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


4. Perform the steps in in the **Card Based** or **BIN based **tab:

   [block:parameters]{"data":{"h-0":"Tab","h-1":"Steps","0-0":"Card Based","0-1":"a. Click the **Issuer Bank **drop-down list in and select the banks for which routing rules apply.  \nb. Click the** Card type **drop-down list and select the card type.  \nc. In **Rule 1** pane, enter the condition using the **When** and** Is** drop-down lists.  \nd. . In **Rule 1** pane, enter the amount range in the **Transaction Amount Range** field. For more information, refer to [Include an Amount Range with a Routing Rule](doc:include-an-amt-range-with-routing-rule) .  \ne. Click the **Add Another Rule** button to add another rule and repeat step c and d.  \n![](https://files.readme.io/19eb874dd78bc12e79d134917006d605e999494feedf8d967fc23151d831f094-maximiser_percentage_based_routing_cards.png)","1-0":"BIN based","1-1":"a. Click the Upload button.  \n**Note**: Click the Download button in the Sample File pane and include the BIN list.  \n![](https://files.readme.io/4a190d95f781f98500a7b0bc88bae8bbb67b798feb004dc8b756933261a9c793-maximiser_percentage_based_routing_cards_bin.png)  \nb. Click the **Add Another Rule** button to add another rule.  \n  \n> \ud83d![](https://files.readme.io/0b0362640594519e0bb83187187bb6ed5cbe6862692143649c4ecf236ea2f297-maximizer_cards_bin_add_another_rule.png)g)  \n> c. In **Rule 1** pane, enter the condition using the **When**, ** Is**  and **Then **drop-down lists.  "},"cols":2,"rows":2,"align":["left","left"]}[/block]

> Note: If you specify an invalid amount range, an error message similar to the following is displayed:
>
> _Set the range for which this rule applies. If left blank the rule will apply to all transaction amounts. Note: Use only positive amount values that are greater than zero_

4. Click **Next** after you have selected the banks and cards for routing.

<Maximizer_Alert />

The _Payment Aggregator_ screen is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/553ab23e4a9329752f075687008fd784d1d3b6f26965089310e2676c0df92032-dashboard-maximizer-amt-based-routing.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


6. Select the **Set Custom Baseline** check box to configure custom baseline for this rule/
   > 📘 Baseline Reference:
   > 
   > For detailed understanding on baseline, refer to [Understanding Baseline Logic](doc:understanding-baseline-logic).

The_ Rule Guidelines_ screen is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/422426d590c3a2b4f079e0f641b508f77603cffba822bbf3c614bbe1fbf34bb6-image_21.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


7. Enter the name for the rule in the **Title** field.
8. Click **Next**.

The Preview page is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c25b1c2a105deca295cb78fdb821d912cd365a2d37d27f739ceb0b1ec2bb5dda-dashboard-maximizer-rule-preview.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


9. Click **Publish Now** to create the rule.

   The rule is added to the **Routing Rules **tab of Maximizer dashboard.

The rule is added to the **Routing Rules **tab of Maximizer dashboard.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/df9389a-Screenshot_2024-06-19_at_11.00.27_AM.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]