---
title: Check is Domestic Card API
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Check is Domestic** or **Card BIN** API is used to detect whether a particular BIN number is international or domestic. It is also useful to determine:

* Card's issuing bank
* Card type such as, Visa, Master, etc.
* Card category such as Credit/Debit, etc.
* bin number is the first 6 digits of a Credit/Debit card.

**Environment**

| Environment            | URL                                                                                  |
| :--------------------- | :----------------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/issuing-bank/v1/bin](https://test.payu.in/issuing-bank/v1/bin) |
| Production Environment | [https://info.payu.in/issuing-bank/v1/bin](https://info.payu.in/issuing-bank/v1/bin) |

## Request header

<V2_payment_header_params />

## Request body

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>bin<br/><code>mandatory</code></td>
      <td><code>Integer/String</code> The first 6 digits of the card (i.e., the BIN number).</td>
      <td>462273</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Sample request

```bash
curl --location 'https://info.payu.in/issuing-bank/v1/bin?is_domestic=true' \
--header 'Content-Type: application/json' \
--header 'date: {{date}}' \
--header 'Authorization: {{authorization}}' \
--data '{
  "bin": "512345"
}'
```

<br />

## Sample response

<br />

### If the card is domestic

```
{
  "isDomestic": "Y",
  "issuingBank": "SCB",
  "cardType": "VISA",
  "cardCategory": "CC"
}
```

<br />

### If the card is international

```
{
  "isDomestic": "N",
  "issuingBank": "UNKNOWN",
  "cardType": "Unknown",
  "cardCategory": "CC"
}
```

## Response parameters

| Parameter    | Description                                                                                                                                                                     |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| isDomestic   | Response value can contain any of the following: • **Y** signifies that the particular BIN is domestic. • **N** signifies that the particular BIN is International.             |
| cardType     | Response value can contain any of the following: • MAST • VISA • MAES • AMEX • DINER • Unknown                                                                                  |
| issuingBank  | The issuing bank of the card used for the transaction.                                                                                                                          |
| cardCategory | Response value can contain any of the following: • **CC** signifies that the particular bin is a credit card BIN • **DC** signifies that the particular bin is a debit card BIN |

To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes) .

<br />

<br />

**Important Notes:**

<br />

1. **BIN Number**: The var1 parameter should contain exactly the first 6 digits of the card number
   2. **Domestic vs International**:- Domestic cards (isDomestic: "Y") will show detailed issuing bank information
   * International cards (isDomestic: "N") typically show "UNKNOWN" for issuing bank
   3. **Card Types**: The API supports detection of major card types including VISA, MAST, AMEX, MAES, DINER
      4. **Card Categories**: Distinguishes between Credit Cards (CC) and Debit Cards (DC)
         5. **Hash Calculation**: Use the sha512 algorithm with the format: key|command|var1|salt\
            \</Accordion>