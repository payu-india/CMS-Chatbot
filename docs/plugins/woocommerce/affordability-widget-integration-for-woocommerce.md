---
title: Affordability Widget Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Affordability Widget Integration for WooCommerce
  description: >-
    The document provides a step-by-step guide to integrating the PayU
    Affordability Widget into WooCommerce product and cart pages by installing
    the WPCode Lite plugin and modifying specific WooCommerce template files.
  keywords:
    - Affordability Widget Integration for WooCommerce
    - WooCommerce Affordability Widget Integration
  robots: index
next:
  description: ''
---
You can integrate the PayU Affordability Widget into your WooCommerce website for both product and cart pages by modifying the code blocks in the **price.php**, **short-description.php**, and **cart-totals.php** files as described in this procedure.

## Step 1: Install the WPCode Lite WordPress Plugin

1. Install the **WPCode Lite** plugin from the WooCommerce admin panel and activate it.

<Image align="center" src="https://files.readme.io/14a19184355ee54c18b290cf307479285ad97732e42d7dd0267553bbef5a160f-snapedit_1728537692521.jpeg" />

2. Navigate to **Code Snippets > Header & Footer**.
3. In the **Header** block, insert the following lines of code:

```html
<!-- PayU Affordability Widget-->
<script defer src="https://jssdk.payu.in/widget/affordability-widget.min.js"></script>
```

4. Save the changes.

## Step 2: Modify the config files

1. Navigate to the following folder of your WordPress installation:

**&lt;Wordpress root&gt;/wp-content/plugins/woocommerce/templates/single-product**

> 📘 Note:
>
> You require the **CPanel** access is required for these configuration file change and it cannot be done from the WordPress admin panel.

2. In the **price.php**, insert the following code at the end of the file. Replace `<key>` with your Merchant Key.

```javascript
<script type="text/javascript">
window.onload = function() {
  const widgetConfig = {
      "key": '<key>',
      "amount": <?php echo $product->get_price(); ?>,
  };
  payuAffordability.init(widgetConfig);
}
</script>
```

3. In the **short-description.php** file, insert the following HTML at the end of the file.

```html
<div id="payuWidget"></div>
```

4. Upload and replace the modified files in the specified path. (Files can be directly modified using the edit option).
5. View the product details in your browser to see the widget on the Product Page.

## Step 3: Add affordability widget on the Cart Page

1. Navigate to the following folder of your WordPress installation:

**&lt;wordpress root&gt;/wp-content/plugins/woocommerce/templates/cart**

> 📘 Note:
>
> You require the **CPanel** access is required for these configuration file change and it cannot be done from the WordPress admin panel.

2. In the **cart-totals.php** file, insert the following code block before the `div` block containing `do_action('woocommerce_proceed_to_checkout');`. Replace `{key}` with your Merchant Key.

```javascript
<script type="text/javascript">
window.onload = function() {
  const widgetConfig = {
      "key": 'key',
      "amount": <?php echo WC()->cart->cart_contents_total; ?>,
  };
  payuAffordability.init(widgetConfig);
}
</script>
<div id="payuWidget"></div>
```

3. View the cart details in your browser to see the widget on the Cart page.