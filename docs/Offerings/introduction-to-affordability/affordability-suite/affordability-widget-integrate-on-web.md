---
title: Integrate with Javascript
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
---
title: Integrate with Javascript
excerpt: Integrate affordability widget on your website built with JavaScript
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The PayU Affordability Widget is a small, ready-made block that you embed on your product page so customers can see EMI plans, Buy Now Pay Later (BNPL) options, and offers **before** they reach checkout. Showing affordability upfront helps customers decide faster and improves your conversion rate.

To learn what the widget looks like and what it does, see [Affordability Widget overview](doc:affordability-suite) or try the [live demo](https://widget.payu.in/demo).


## Integration steps

<Accordion title="Step 1: Embed the JavaScript file into your website" icon="fa-code">

Loads PayU's widget code into your page so the browser knows how to render the widget.

Copy the following snippet and paste it inside the `<head>` section of your website's HTML:

```html HTML
<!-- Add script in head -->
<script defer src="https://jssdk.payu.in/widget/affordability-widget.min.js"></script>
```

The `defer` attribute tells the browser to download the script in the background and run it after the page has loaded, so it does not slow down your page.

</Accordion>
<Accordion title="Step 2: Add placeholder for the Widget" icon="fa-code">

Reserves the spot on your page where the widget will appear.

Paste this empty `<div>` wherever you want the widget to show up — typically right below the product price on your Product Display Page (PDP):

```html HTML
<div id="payuWidget"> </div> 
```

The widget script (loaded in Step 1) finds this `<div>` by its `id="payuWidget"` and renders the widget inside it. Do not change the id.

***

</Accordion>
<Accordion title="Step 3: Initiate the Widget" icon="fa-code">

The following code tells the widget which merchant you are and how much the product costs, then renders it inside the placeholder you added in Step 2.

Add the following snippet inside a `<script>` tag in the `<head>` section of your webpage. Replace `{key}` and `{amount}` with real values from your code.

```javascript Javascript
window.onload = function() {
  const widgetConfig = {
      "key": {key},
      "amount": {amount},
  };
  payuAffordability.init(widgetConfig);
}
```

`window.onload` makes sure the widget only initialises after the rest of the page has loaded, so the placeholder `<div>` from Step 2 already exists when the script runs.

<Table align="left">
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key
        `mandatory`
      </td>

      <td>
        `String` Your **merchant key** — the unique merchant ID PayU issues to you. Find it in your PayU dashboard under Settings → My Account → API Keys (see [Access Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)). Use your **test** key while you build, and switch to your **production** key when you go live.
      </td>
    </tr>

    <tr>
      <td>
        amount `mandatory`
      </td>

      <td>
        `String` The product price in INR, passed as a string (for example, `"6000"`). Update this value dynamically so it always matches the price of the product the customer is currently viewing.
      </td>
    </tr>
  </tbody>
</Table>

***

</Accordion>

## Customize the Widget

<Accordion title="Display specific affordability options available for a customer" icon="fa-code">

Personalises the widget so it only shows the affordability options the *signed-in customer* is actually eligible for, instead of the full list.

By default, the widget shows every affordability option PayU supports. To filter the list to a specific customer, add a `userDetails` object inside `widgetConfig`:

```json JSON
"userDetails": {                        
        "mobileNumber": {mobile number},     
        "token": {token},                    
        "timeStamp": {timestamp}             
      }
```

| Parameter      | Description                                                                                                                                                                                                                                                                                                                                                          |
| :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `mobileNumber` | `String` The customer's 10-digit mobile number. PayU uses this to look up which affordability offers that customer is eligible for.                                                                                                                                                                                                                                  |
| `timeStamp`    | `String` The current request time in **GMT**, in the exact format `Mon, 14 Feb 2022 13:06:14 GMT`. PayU uses it to ensure the request is fresh and prevent replay.                                                                                                                                                                                                   |
| `token`        | `String` A SHA-512 hash that proves the request came from you. Compute it using the formula `SHA512(merchantKey \| amount \| phone \| date \| salt)`. <br /><br />**Important:** generate this hash on your **server**, never in the browser. Your salt is a secret and must not be exposed in client-side code. See [Generate Hash](doc:hashing-request-and-response) for details. |

***

</Accordion>
<Accordion title="Display SKU based offers in the widget" icon="fa-code">

Displays offers tied to specific products (SKUs) instead of generic ones. A **SKU** (Stock Keeping Unit) is a unique code that identifies a specific product or product variant in your catalog — for example, "T-shirt, red, size M".

`skusDetail` is an optional key inside `widgetConfig` that accepts an array of SKU objects. Add one object per SKU you want to display offers for.

For each SKU, only `skuId` is required. `skuAmount` and `quantity` are optional.

> 🚧 Warning!
>
> If you do not pass a value for `skuAmount`, the widget falls back to the product price you passed in the top-level `amount` field.

```json JSON
"skusDetail": [
        {
          "skuId": "{sku1Id}",
          "skuAmount": "{sku1Amount}",
          "quantity": "{sku1quantity}"
        },
        {
          "skuId": "{sku2Id}",
          "skuAmount": "{sku2Amount}",
          "quantity": "{sku2quantity}"
        }
      ]
```

***

</Accordion>
<Accordion title="Customize the Display Color of the Widget" icon="fa-code">

Lets you change the widget's colors so it matches your website's brand.

The widget has two views: **L1** is the small, collapsed view shown on your product page; **L2** is the larger, expanded view that opens when the customer taps the widget.

`styleConfig` is an optional object inside `widgetConfig`. The accepted keys are:

* `lightColor` — the color of the EMI tab on the L1 (collapsed) view.
* `darkColor` — the color of the buttons on both the L1 and L2 views.
* `backgroundColor` — the widget's background color, useful if your page background is not white. The widget automatically adjusts the L1 text color to stay readable on your background.

Color values are CSS hex strings (for example, `"#FFC915"`).

```json JSON
"styleConfig": {
        "lightColor": "#FFFCF3",
        "darkColor": "#FFC915",
        "backgroundColor": "#FFFFFF"
      }
```

</Accordion>
<Accordion title="Sample Code" icon="fa-code">

A complete example with all optional sections enabled. Replace the placeholder values in `{ }` with your real values.

```javascript Javascript
window.onload = function() {
  const widgetConfig = {
      "key": "{key}",
      "amount": "{amount}",
      "skusDetail": [
        {
          "skuId": "{sku1Id}",
          "skuAmount": "{sku1Amount}",
          "quantity": "{sku1quantity}"
        },
        {
          "skuId": "{sku2Id}",
          "skuAmount": "{sku2Amount}",
          "quantity": "{sku2quantity}"
        }
      ],
      "styleConfig": {
        "lightColor": "#FFFCF3",
        "darkColor": "#FFC915",
        "backgroundColor": "#FFFFFF"
      },
      "userDetails": {
        "mobileNumber": "{mobile number}",
        "token": "{token}",
        "timeStamp": "{timestamp}"
      }
  };
  payuAffordability.init(widgetConfig);
}
```

</Accordion>

## Glossary

<Accordion title="Plain-English glossary of terms used on this page" icon="fa-book">

| Term | What it means |
| :--- | :--- |
| **Affordability Widget** | A small, ready-made block PayU provides that you embed on your product page. It shows EMI plans, BNPL options, and offers so customers can decide *before* checkout. |
| **EMI** | Equated Monthly Instalment. A way to pay for a purchase in equal monthly amounts (over 3, 6, 9, 12 months, etc.) instead of paying the full price upfront. |
| **BNPL** | Buy Now, Pay Later. A short-term financing option that lets a customer take the product today and pay for it later, often interest-free. |
| **PDP** | Product Display Page — the page on your website that shows a single product, its price, and the "Buy" or "Add to cart" button. This is where the widget is usually placed. |
| **SKU** | Stock Keeping Unit. A unique code in your catalog that identifies a specific product or variant (for example, "Red T-shirt, size M"). |
| **Merchant key** | A unique identifier PayU issues to your merchant account. It is safe to include in your website code. |
| **Salt** | A secret string PayU issues alongside your merchant key. **Never** put the salt in your website code; only use it on your server to compute hashes. |
| **Hash / SHA-512** | A one-way "fingerprint" of a string. PayU uses it to verify a request really came from you and was not tampered with. SHA-512 is the specific hashing algorithm. |
| **Token** | In this guide, a `token` is the SHA-512 hash you compute on your server and pass to the widget. It is *not* a long-lived API token. |
| **L1 screen / L2 screen** | The widget has two views. L1 is the small, collapsed view shown on your product page. L2 is the larger, expanded view that opens when the customer taps the widget. |
| **GMT timestamp** | The current date and time in Greenwich Mean Time, formatted exactly like `Mon, 14 Feb 2022 13:06:14 GMT`. |
| **`<head>` / `<script>` / `<div>`** | Standard HTML tags. `<head>` is the section at the top of an HTML page where scripts are loaded. A `<script>` tag loads JavaScript. A `<div>` is a generic container element — Step 2 uses one as a placeholder for the widget. |
| **PayU Key Account Manager (KAM)** | Your dedicated PayU contact for commercial questions, enablement, onboarding, and merchant account support. |

</Accordion>
