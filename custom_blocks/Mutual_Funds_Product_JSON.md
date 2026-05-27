---
name: Mutual_Funds_Product_JSON
---
  <Accordion title="Sample JSON" icon="fa-code">
    ```json
    "product": {
        "wtParams": [
          {
            "type": "mutual_fund",
            "plan": "GD",
            "amount": "50000",
            "option": "G",
            "scheme": "LT",
            "receipt": "77407",
            "mf_member_id": "123445",
            "mf_user_id": "77407",
            "mf_partner": "cams",
            "mf_investment_type": "L",
            "mf_amc_code": "UTB"
          }
        ]
      }
    ```
  </Accordion>

  <Accordion title="Wealth Tech object (wtParams) fields Description" icon="fa-cog">
    These parameters are included within the `product` field as a JSON array under the fiedl `wtParams`:
| Field | Description | Example |
|---|---|---|
| type<br/><code>mandatory</code> | <code>string</code> - Transaction type, must be "mutual_fund" | `"mutual_fund"` |
| amount<br/><code>mandatory</code> | <code>float</code> - The transaction amount, must match order amount | `50000` |
| receipt<br/><code>mandatory</code> | <code>string</code> - Unique PG reference number (max 25 chars) | `"77407"` |
| mf_member_id<br/><code>mandatory</code> | <code>numeric</code> - Member ID issued by mutual fund platform (5-20 chars) | `"123445"` |
| mf_user_id<br/><code>mandatory</code> | <code>string</code> - Unique mutual fund user/client ID (max 10 chars) | `"77407"` |
| mf_partner<br/><code>mandatory</code> | <code>string</code> - Mutual fund platform: cams, kfin, bse, nse (max 4 chars) | `"cams"` |
| mf_investment_type<br/><code>mandatory</code> | <code>string</code> - Investment type: L (Lump Sum) or S (SIP) (single char) | `"L"` |
| plan<br/><code>optional</code> | <code>string</code> - Mutual fund plan name | `"GD"` |
| folio<br/><code>optional</code> | <code>string</code> - Unique mutual fund account identifier | `"12345678"` |
| option<br/><code>optional</code> | <code>string</code> - Mutual fund plan option | `"G"` |
| scheme<br/><code>optional</code> | <code>string</code> - Mutual fund type/scheme | `"LT"` |
| mf_amc_code<br/><code>optional</code> | <code>string</code> - Asset Management Company code (max 5 chars) | `"UTB"` |
  </Accordion>

 <Accordion title="Validation Rules" icon="fa-code">

| Field | Description | Example |
|---|---|---|
| type | Must always be `"mutual_fund"` | `"mutual_fund"` |
| amount | Must match the overall order amount and be in paise | - |
| receipt | Must be unique across transactions | - |
| mf_member_id | Must be numeric with length between 5-20 characters | - |
| mf_user_id | Maximum 10 characters allowed | - |
| mf_partner | Must be one of: `"cams"`, `"kfin"`, `"bse"`, `"nse"` | `"cams"` |
| mf_investment_type | Only `"L"` (Lump Sum) or `"S"` (SIP) allowed | `"L"` |
| **Optional Field Validations**| |
| mf_amc_code | Maximum 5 characters | - |
| receipt | Maximum 25 characters for SIP registration ID | - |

</Accordion>

<br />