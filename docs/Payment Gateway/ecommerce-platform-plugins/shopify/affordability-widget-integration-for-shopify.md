---
title: Affordability Widget Integration for Shopify
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
PayU Affordability Widget can be introduced into themes in Liquid template files, sections, blocks, and snippets.

To configure the Affordability Widget for Shopify:

1. [Duplicate the Existing Theme](#step-1-duplicate-the-existing-theme)
2. [Add Snippet for PayU](#step-2-add-snippet-for-payu)
3. [Update the Templates](#step-3-update-the-templates)
4. [Update Theme](#step-4-update-theme)

<Callout icon="📘" theme="info">
  **Note**: If you are using themes created in 2020 or before, where product.json is not present, [Step 1](#step-1-duplicate-the-existing-theme) must be followed.
</Callout>

## Step 1: Duplicate the Existing Theme

<Accordion title="Duplicate the Existing Theme" icon="fa-info-circle">
  To duplicate the existing theme:

  <Callout icon="📘" theme="info">
    Note: If you are using themes created in 2020 or before, where product.json is not present, step in this section can be skipped and proceed to [Step 2: Add Snippet for PayU](#step-2-add-snippet-for-payu).
  </Callout>

  1. Log in to Shopify Admin portal.
  2. Select **Themes** under **Online Stores** on the left navigation pane.

  <Image align="center" src="https://files.readme.io/af2247c-Screenshot_2023-11-29_at_2.36.02_PM.png" width="222px" />

  3. Select the hamburger menu for which you wish configure the widget and  select **Duplicate Theme**.

  <Image align="center" src="https://files.readme.io/253fdf6-Screenshot_2023-11-28_at_3.22.51_PM.png" />

  4. Select the hamburger menu for which you wish to configure the widget and select **Edit Code** to open the *Code*  page for the current theme.

     The following folders are displayed on *Code* page of the current theme.

  <Image align="center" border={true} src="https://files.readme.io/f2ec0d7-Screenshot_2023-11-28_at_3.28.37_PM.png" width="222px" />

  5. Navigate to **Layout** >  **theme.liquid** file.

  <Image align="center" border={true} src="https://files.readme.io/aad2727-Screenshot_2023-11-29_at_2.53.51_PM.png" width="222px" />

  6. Add the below script before completing the head tag:

  ```
  <script defer src="https://jssdk.payu.in/widget/affordability-widget.min.js"></script>
  ```
</Accordion>

## Step 2: Add an affordability snippet on your website

<Accordion title="Non SKU-based offer" icon="fa-info-circle">
  To add a snippet to your website for a non SKU-based offer:

  > 📘 Note:
  >
  > Add a non-SKU based offer on PayU Dashboard before performing this procedure. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer).

  1. Select **Add a new Snippet** under the **Snippet** folder on the left pane.

  <Image align="center" border={true} src="https://files.readme.io/df73655-Screenshot_2023-11-29_at_2.55.02_PM.png" width="222px" />

  2. Create and add a new snippet with the name “payu-block” as filename under the **Snippets** folder.

     The \_Add a new snippet \_dialog box is displayed.

  3. Enter the name of the snippet as **payu-block** and then click **Done**.

  <Image align="center" src="https://files.readme.io/f64623a-Screenshot_2023-11-29_at_2.58.58_PM.png" width="322px" />

  4. Add the following snippet inside the payu-block file:

  ```
  <script>
      window.addEventListener("load", (event) => {
          var widgetConfig = {
              "key": "MERCHANT_KEY",
              "amount": {{ payu_amount | divided_by: 100.00 }},
          };
          payuAffordability.init(widgetConfig);
      });
  </script>
  <div id="payuWidget"></div>
  ```

  This is to view UI on the webpage, **key** is the merchant key.
</Accordion>

<Accordion title="SKU-based offer" icon="fa-info-circle">
  To add a snippet to your website for a SKU-based offer:

  > 📘 Note:
  >
  > Add a SKU based offer on PayU Dashboard before performing this procedure. For more information, refer to [Create a SKU-Based Offer](doc:create-a-sku-based-offer).

  1. Select **Add a new Snippet** under the **Snippet** folder on the left pane.

  <Image align="center" border={true} src="https://files.readme.io/df73655-Screenshot_2023-11-29_at_2.55.02_PM.png" width="222px" />

  2. Create and add a new snippet with the name “payu-block” as filename under the **Snippets** folder.

     The \_Add a new snippet \_dialog box is displayed.

  3. Enter the name of the snippet as **payu-block** and then click **Done**.

  <Image align="center" src="https://files.readme.io/f64623a-Screenshot_2023-11-29_at_2.58.58_PM.png" width="322px" />

  4. Add the following snippet inside the payu-block file:

  ```
  <script>
       window.onload = function() {
          // Initialize an empty array for SKU details
          var skusDetail = [];
          var payuAmount;
          
          // Check if the product object exists
          {% if product %}
            // Set payu_amount to the product price in rupees
            payuAmount = {{ product.selected_or_first_available_variant.price | divided_by: 100.00 }};
            
          
            {% if product.selected_or_first_available_variant.sku != blank %}  // Check if the variant SKU exists
              skusDetail.push({
                skuId: "{{ product.selected_or_first_available_variant.sku }}",              // Get the variant SKU ID
                skuAmount: {{ product.selected_or_first_available_variant.price | divided_by: 100.00 }},  // Convert price to rupees
                quantity: 1
              });
            {% endif %}
          
            console.log("SKU Details from Product Variants:", skusDetail);
          {% else %}
            // If product does not exist, set payu_amount to the cart amount
            payuAmount = {{ cart.total_price | divided_by: 100.00 }};

            
            // If product does not exist, create skusDetail from line items of the cart
            {% for line_item in cart.items %}
              {% if line_item.sku != blank %}  // Check if the line item SKU exists
                skusDetail.push({
                  skuId: "{{ line_item.sku }}",              // Get the line item SKU ID
                  skuAmount: {{ line_item.price | divided_by: 100.00 }},  // Convert line item price to rupees
                  quantity: {{ line_item.quantity }}  // Get the line item quantity
                });
              {% else %}
                console.log('One or more items does not have SKU info')
                skusDetail = []
                {% break %} 
              {% endif %}
            {% endfor %}
          
            console.log("SKU Details from Cart Line Items:", skusDetail);
          {% endif %}
         
         const widgetConfig = {
            "key": "smsplus",
            "amount": payuAmount,
            "skusDetail": skusDetail
          };
       payuAffordability.init(widgetConfig);
     }
  </script>
  <div id="payuWidget"></div>
  ```

  This is to view UI on the webpage, **key** is the merchant key.

  ##
</Accordion>

<br />

## Step 3: Update the Templates

<Accordion title="Update the Templates" icon="fa-info-circle">
  To update the templates:

  1. Check the following files under the **Templates** folder:

  * Product.json
  * Cart.json

  <Image align="center" border={true} src="https://files.readme.io/bf396d0-Screenshot_2023-11-29_at_3.04.51_PM.png" width="222px" />

  2. Edit the **Product.json** file.
  3. Search the main section and observe the **type** defined.

  <Image align="center" border={true} src="https://files.readme.io/e9a30db-Screenshot_2023-11-29_at_3.08.19_PM.png" />

  4. Open the corresponding liquid file mentioned in step 3, that is, under **Sections** folder, navigate to  the **main-product.liquid** file. This file is used is to render Widget on the webpage.
  5. Search for the following code:

  ```
  {%- for block in section.blocks -%} 
  {%- case block.type -%}
  ```

  6. Add the following code after the code specified in step 5.

  ```
  {%- when 'payu_widget' -%}
  {% render 'payu-block',payu_amount: product.price %}
  ```

  7. Search for word **schema** and add the following code under **blocks**.

  ```
  {

  “type":"payu_widget”, ”name”:”payu_widget”

  },
  ```

  8. Repeat the step 5 to step 7 for the **main-cart.footer.liquid** if you want to show widget on your  **Add to Cart** page.
  9. Open the **Product.json**  file under the **Templates** folder.
  10. Add in the **blocks** of **main section** in the Product.json file

  ```
  "payu_block": {
  "type": "payu_widget",

  "settings": { }

  },
  ```

  11. Add “payu\_block” in **order** of main section to define order and placeholder of the PayU Widget. Save the changes.

  ```
  "payu_block": {
          "type": "payu_widget",
          "settings": {}
      }
  ```

  12. Repeat the above step 9 to step 11 for the **Cart.json** file.
</Accordion>

## Step 4: Update Theme

<Accordion title="Update Theme" icon="fa-info-circle">
  To update the theme:

  1. Navigate to Shopify theme editor,
  2. Click **Add block** in the **Product information** section,
  3. Select the **PayU Widget** to drag and place where you want to place the widget.

  > 📘 Note:
  >
  > Search for **Product.liquid** or **product-info.liquid** file and add the following line of code anywhere or before `endif`.    This code is to render the page.
  >
  > ```
  > _{% render 'payu-block',payu\_amount: product.price %}_
  > ```

  4. Click **Done**.
  5. Repeat step 2 to step 4 for **cart.json** in case you want to show widget on Add to cart page. Main-cart.footer
</Accordion>

<br />
