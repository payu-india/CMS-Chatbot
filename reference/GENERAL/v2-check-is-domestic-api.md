---
title: v2 Check is Domestic API
deprecated: false
hidden: true
metadata:
  robots: index
---
This API allows merchants to check whether a card BIN (first 6 digits of a card) is domestic or international, along with details like card type, issuing bank, and card category.

HTTP Method: POST

**Endpoint**

* **Test Environment**: `https://test.payu.in/merchant/postservice.php?form=2`
* **Production Environment**: `https://info.payu.in/merchant/postservice?form=2`

## Request headers

<HeaderAuthentication />

<br />

## Request parameters

| Parameter                         | Description                                                                 | Example |
| --------------------------------- | --------------------------------------------------------------------------- | ------- |
| `key`<br /><code>mandatory</code> | <code>String</code> The merchant key provided by PayU.                      | JPM7Fg  |
| `bin`<br /><code>mandatory</code> | <code>String</code> The first six digits (BIN) of the credit or debit card. | 462273  |

## Sample Request (cURL)

```bash
curl --location 'https://info.payu.in/issuing-bank/v1/bin' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Date: Thu, 17 Feb 2022 08:17:59 GMT' \
--header 'Digest: vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=' \
--header 'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI="' \
--header 'platformId: 1' \
--data-urlencode 'key=JPM7Fg' \
--data-urlencode 'bin=462273'
```

## Sample Response

### If the card is domestic

```json
{
  "isDomestic": "Y",
  "issuingBank": "SCB",
  "cardType": "VISA",
  "cardCategory": "CC"
}
```

### If the card is international

```json
{
  "isDomestic": "N",
  "issuingBank": "UNKNOWN",
  "cardType": "Unknown",
  "cardCategory": "CC"
}
```

## Response Parameters

| Parameter      | Description                                                                                  | Example |
| -------------- | -------------------------------------------------------------------------------------------- | ------- |
| `isDomestic`   | Indicates if the card is domestic or international. `Y` for domestic, `N` for international. | `Y`     |
| `issuingBank`  | The name of the card's issuing bank.                                                         | `SCB`   |
| `cardType`     | Type of card: `MAST`, `VISA`, `MAES`, `AMEX`, `DINER`, or `Unknown`.                         | `VISA`  |
| `cardCategory` | Indicates card category: `CC` for Credit Card, `DC` for Debit Card.                          | `CC`    |