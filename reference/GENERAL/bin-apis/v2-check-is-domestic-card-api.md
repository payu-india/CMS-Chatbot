---
title: v2 Check is Domestic Card API
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Check is Domestic** or **Card BIN** API is used to detect whether a particular BIN number is international or domestic. It is also useful to determine:

* Card's issuing bank
  * Card type such as, Visa, Master, etc.
    * Card category such as Credit/Debit, etc.
      * var1 is bin number which is the first 6 digits of a Credit/Debit card.
        <br />

## Request header

## Request body

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

<br />

```
```

<br />

### If the card is international

<br />

```
```

## Response parameters

<br />

To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes) .

<br />

<br />

**Important Notes:**

<br />

1. **BIN Number**: The var1 parameter should contain exactly the first 6 digits of the card number
   2. **Domestic vs International**:- Domestic cards (isDomestic: "Y") will show detailed issuing bank information
      - International cards (isDomestic: "N") typically show "UNKNOWN" for issuing bank
      3. **Card Types**: The API supports detection of major card types including VISA, MAST, AMEX, MAES, DINER
         4. **Card Categories**: Distinguishes between Credit Cards (CC) and Debit Cards (DC)
            5. \*\*Hash Calculation\*\*: Use the sha512 algorithm with the format: key|command|var1|salt &#x20;
               \</Accordion>