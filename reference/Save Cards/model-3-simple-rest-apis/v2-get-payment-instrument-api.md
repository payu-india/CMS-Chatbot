---
title: v2 Get Payment Instrument API
deprecated: false
hidden: false
metadata:
  robots: index
---
The v2 **Get Payment Instrument** API allows merchants to fetch all saved cards for a specific user. This API returns comprehensive card details including tokenized information, expiry status, and network tokens for secure transactions.

**Environment**

|            |                                                 |
| :--------- | :---------------------------------------------- |
| Production | \<info.storecard.service.url>/storecard/card/v2 |

## Request header

<Table>
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
        mid
        `mandatory`
      </td>

      <td>
        Merchant ID provided by PayU. Use the value provided in your PayU dashboard.
      </td>
    </tr>
  </tbody>
</Table>

## Request body

None

## Sample Request and Response

### Request

```bash
curl --location '<info.storecard.service.url>/storecard/card/v1' \
--header 'Content-Type: application/json' \
--header 'mid: 2' \
```

### Response

```json
{
    "status": 1,
    "msg": "Cards fetched Successfully",
    "user_cards": {
        "a52aa1c09e11ac56926005": {
            "card_type": "CC",
            "expiry_year": "2030",
            "expiry_month": "11",
            "is_expired": 0,
            "card_mode": "CC",
            "card_no": "XXXXXXXXXXXX6937",
            "card_name": "raghu_visa",
            "name_on_card": "DUMMY",
            "card_brand": "VISA",
            "card_bin": "439040",
            "isDomestic": "Y",
            "card_cvv": 0,
            "PAR": "V0010013022526170404000072387",
            "network_token": {
                "token_bin": "439040",
                "is_expired": 0,
                "token_exp_yr": "2030",
                "token_exp_mon": "11",
                "token_value": "4390406210204342"
            }
        }
    }
}
```

## Response parameters

| Field       | Description                                                                       | Example                    |
| ----------- | --------------------------------------------------------------------------------- | -------------------------- |
| status      | Status indicator: `1` for success, `0` for failure.                               | 1                          |
| msg         | Human-readable response message indicating if card fetching was successful.       | Cards fetched Successfully |
| user\_cards | Contains saved card details for the user, with unique card tokens as object keys. |                            |

### User Cards Object

| Field          | Description                                                                                                                           | Example                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| card\_type     | Type of card: either `CC` (Credit Card) or `DC` (Debit Card).                                                                         | CC                                                                             |
| expiry\_year   | Expiry year of the card.                                                                                                              | 2030                                                                           |
| expiry\_month  | Expiry month of the card.                                                                                                             | 11                                                                             |
| is\_expired    | Shows whether the card has expired or not: `0` for active, `1` for expired.                                                           | 0                                                                              |
| card\_mode     | Either `CC` (Credit Card) or `DC` (Debit Card).                                                                                       | CC                                                                             |
| card\_no       | Masked card number showing only the last four digits.                                                                                 | `XXXXXXXXXXXX6937`                                                             |
| card\_name     | User-defined name for the card.                                                                                                       | raghu\_visa                                                                    |
| name\_on\_card | Cardholder name.                                                                                                                      | DUMMY                                                                          |
| card\_brand    | Network or brand name for the card (e.g., VISA, MASTERCARD).                                                                          | VISA                                                                           |
| card\_bin      | Bank Identification Number of the card (first 6-9 digits).                                                                            | `439040`                                                                       |
| isDomestic     | Indicates if the card is domestic or international: `Y` for domestic, `N` for international.                                          | Y                                                                              |
| card\_cvv      | Indicates if the CVV is required: `0` for Not Required, `1` for Required.                                                             | 0                                                                              |
| PAR            | Payment Account Reference – unique identifier for the card across environments for transaction checks.                                | V0010013022526170404000072387                                                  |
| network\_token | Contains network token details for secure transactions. For more information, refer to[ Network token object](#network-token-object). | For more information, refer to[ Network token object](#network-token-object) . |

### Network token object

| Field           | Description                                                    | Example          |
| --------------- | -------------------------------------------------------------- | ---------------- |
| token\_bin      | Bank Identification Number for the network token.              | 439040           |
| is\_expired     | Indicates the token's status: `0` for active, `1` for expired. | 0                |
| token\_exp\_yr  | Expiry year of the network token.                              | 2030             |
| token\_exp\_mon | Expiry month of the network token.                             | 11               |
| token\_value    | The actual token value used for secure transactions.           | 4390406210204342 |