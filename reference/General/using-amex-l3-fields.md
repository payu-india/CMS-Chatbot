---
title: Using AMEX L3 Fields
deprecated: false
hidden: false
metadata:
  robots: index
---
The[ L3 field descriptions](#l3-field-descriptions) table provides the list of fields with their length, type and description.

You must use the L3 fields with **\_payment** API similar to the JSON:

```
{
  "bookingReference": "MC12D8",
  "documentType": "PASSENGER_TICKET",
  "itinerary": {
    "leg": [
      {
        "carrierCode": "MA",
        "departureAirport": "STL",
        "departureDate": "2019-06-07",
        "destinationAirport": "ORD"
      },
      {
        "carrierCode": "MA",
        "departureAirport": "ORD",
        "departureDate": "2019-06-09",
        "destinationAirport": "STL"
      }
    ],
    "numberInParty": "2"
  },
  "passenger": [
    {
      "firstName": "JOHN",
      "lastName": "SMITH"
    },
    {
      "firstName": "JANE",
      "lastName": "SMITH"
    }
  ],
  "ticket": {
    "issue": {
      "carrierCode": "MA",
      "carrierName": "MastercardAirlines",
      "city": "Purchase",
      "country": "USA",
      "date": "2019-06-06"
    },
    "conjunctionTicketIndicator": false,
    "eTicket": true,
    "ticketNumber": "A01234567890",
    "totalFare": "50.00",
    "totalFees": "15.00",
    "totalTaxes": "10.00"
  },
  "transactionType": "TICKET_PURCHASE"
}
```

## L3 field descriptions

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Field Name</th>
      <th>Field Length</th>
      <th>Field Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RECORD_TYPE</td>
      <td>3</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>RECORD_NUMBER</td>
      <td>8</td>
      <td>Numeric</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 8 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>TRANSACTION_IDENTIFIER</td>
      <td>15</td>
      <td>Numeric</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 15 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>FORMAT_CODE</td>
      <td>2</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>ADDENDA_TYPE_CODE</td>
      <td>2</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>TRANSACTION_TYPE</td>
      <td>3</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>TICKET_NUMBER</td>
      <td>14</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 14 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>DOCUMENT_TYPE</td>
      <td>2</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>AIRLINE_PROCESS_IDENTIFIER</td>
      <td>3</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>IATA_NUMERIC_CODE</td>
      <td>8</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 8 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>TICKETING_CARRIER_NAME</td>
      <td>25</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 25 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>TICKET_ISSUE_CITY</td>
      <td>18</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 18 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>TICKET_ISSUE_DATE</td>
      <td>8</td>
      <td>Numeric</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 8 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>NUMBER_IN_PARTY</td>
      <td>3</td>
      <td>Numeric</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 3 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>PASSENGER_NAME</td>
      <td>25</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 25 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>CONJUNCTION_TICKET_INDICATOR</td>
      <td>1</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 1 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>RESERVED</td>
      <td>3</td>
      <td>Numeric</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 3 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>ORIGINAL_TRANSACTION_AMOUNT</td>
      <td>12</td>
      <td>Numeric</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 12 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>ORIGINAL_CURRENCY_CODE</td>
      <td>3</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>ELECTRONIC_TICKET_INDICATOR</td>
      <td>1</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 1 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>TOTAL_NUMBER_OF_AIR_SEGMENTS</td>
      <td>1</td>
      <td>Numeric</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 1 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>STOPOVER_INDICATOR_1</td>
      <td>1</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 1 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>DEPARTURE_LOCATION_CODE_SEGMENT_1</td>
      <td>3</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>DEPARTURE_DATE_SEGMENT_1</td>
      <td>8</td>
      <td>Numeric</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 8 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>ARRIVAL_LOCATION_CODE_SEGMENT_1</td>
      <td>3</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>SEGMENT_CARRIER_CODE_1</td>
      <td>2</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>SEGMENT_1_FARE_BASIS</td>
      <td>15</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 15 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>CLASS_OF_SERVICE_CODE_SEGMENT_1</td>
      <td>2</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>FLIGHT_NUMBER_SEGMENT_1</td>
      <td>4</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 4 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>RESERVED</td>
      <td>3</td>
      <td>Numeric</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 3 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>SEGMENT_1_FARE</td>
      <td>12</td>
      <td>Numeric</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 12 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>STOPOVER_INDICATOR_2</td>
      <td>1</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 1 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>DEPARTURE_LOCATION_CODE_SEGMENT_2</td>
      <td>3</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>DEPARTURE_DATE_SEGMENT_2</td>
      <td>8</td>
      <td>Numeric</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 8 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>ARRIVAL_LOCATION_CODE_SEGMENT_2</td>
      <td>3</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>SEGMENT_CARRIER_CODE_2</td>
      <td>2</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>SEGMENT_2_FARE_BASIS</td>
      <td>15</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 15 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>CLASS_OF_SERVICE_CODE_SEGMENT_2</td>
      <td>2</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>FLIGHT_NUMBER_SEGMENT_2</td>
      <td>4</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 4 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>RESERVED</td>
      <td>3</td>
      <td>Numeric</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 3 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>SEGMENT_2_FARE</td>
      <td>12</td>
      <td>Numeric</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 12 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>STOPOVER_INDICATOR_3</td>
      <td>1</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 1 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>DEPARTURE_LOCATION_CODE_SEGMENT_3</td>
      <td>3</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>DEPARTURE_DATE_SEGMENT_3</td>
      <td>8</td>
      <td>Numeric</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 8 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>ARRIVAL_LOCATION_CODE_SEGMENT_3</td>
      <td>3</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>SEGMENT_CARRIER_CODE_3</td>
      <td>2</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>SEGMENT_3_FARE_BASIS</td>
      <td>15</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 15 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>CLASS_OF_SERVICE_CODE_SEGMENT_3</td>
      <td>2</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>FLIGHT_NUMBER_SEGMENT_3</td>
      <td>4</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 4 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>RESERVED</td>
      <td>3</td>
      <td>Numeric</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 3 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>SEGMENT_3_FARE</td>
      <td>12</td>
      <td>Numeric</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 12 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>STOPOVER_INDICATOR_4</td>
      <td>1</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 1 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>DEPARTURE_LOCATION_CODE_SEGMENT_4</td>
      <td>3</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>DEPARTURE_DATE_SEGMENT_4</td>
      <td>8</td>
      <td>Numeric</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 8 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>ARRIVAL_LOCATION_CODE_SEGMENT_4</td>
      <td>3</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>SEGMENT_CARRIER_CODE_4</td>
      <td>2</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>SEGMENT_4_FARE_BASIS</td>
      <td>15</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 15 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>CLASS_OF_SERVICE_CODE_SEGMENT_4</td>
      <td>2</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>FLIGHT_NUMBER_SEGMENT_4</td>
      <td>4</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 4 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>RESERVED</td>
      <td>3</td>
      <td>Numeric</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 3 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>SEGMENT_4_FARE</td>
      <td>12</td>
      <td>Numeric</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 12 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>STOPOVER_INDICATOR_5</td>
      <td>1</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 1 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>EXCHANGED/ORIGINAL_TICKET_NUMBER</td>
      <td>14</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 14 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>RESERVED</td>
      <td>313</td>
      <td>Alphanumeric</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 313 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>