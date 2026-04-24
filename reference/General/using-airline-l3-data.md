---
title: Using Airline L3 Data
deprecated: false
hidden: true
metadata:
  robots: index
---
This section includes the following:

* [Using L3 fields in _payment API ](#using-l3-fields-in-_payment-api)section provides JSON object format to include the L3 fields
* [ L3 field descriptions](#l3-field-descriptions) table provides the list of fields with their length, type and description.

## Using L3 fields in _payment API

You must use the L3 fields in **_payment** API, where the airline data is collected (JSON only):

```json
l3_details = {
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
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RECORD_TYPE</td>
      <td>3</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>RECORD_NUMBER</td>
      <td>8</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 8 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>TRANSACTION_<br/>IDENTIFIER</td>
      <td>15</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 15 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>FORMAT_CODE</td>
      <td>2</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>ADDENDA_<br/>TYPE_CODE</td>
      <td>2</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>TRANSACTION_<br/>TYPE</td>
      <td>3</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>TICKET_<br/>NUMBER</td>
      <td>14</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 14 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>DOCUMENT_TYPE</td>
      <td>2</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>AIRLINE_<br/>PROCESS_<br/>IDENTIFIER</td>
      <td>3</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>IATA_<br/>NUMERIC_<br/>CODE</td>
      <td>8</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 8 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>TICKETING_<br/>CARRIER_<br/>NAME</td>
      <td>25</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 25 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>TICKET_<br/>ISSUE_<br/>CITY</td>
      <td>18</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 18 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>TICKET_<br/>ISSUE_<br/>DATE</td>
      <td>8</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 8 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>NUMBER_<br/>IN_PARTY</td>
      <td>3</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 3 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>PASSENGER_<br/>NAME</td>
      <td>25</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 25 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>CONJUNCTION_<br/>TICKET_<br/>INDICATOR</td>
      <td>1</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 1 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>RESERVED</td>
      <td>3</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 3 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>ORIGINAL_<br/>TRANSACTION_<br/>AMOUNT</td>
      <td>12</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 12 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>ORIGINAL_<br/>CURRENCY_<br/>CODE</td>
      <td>3</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>ELECTRONIC_<br/>TICKET_<br/>INDICATOR</td>
      <td>1</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 1 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>TOTAL_NUMBER_OF_<br/>AIR_SEGMENTS</td>
      <td>1</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 1 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>STOPOVER_<br/>INDICATOR_1</td>
      <td>1</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 1 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>DEPARTURE_<br/>LOCATION_<br/>CODE_SEGMENT_1</td>
      <td>3</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>DEPARTURE_<br/>DATE_SEGMENT_1</td>
      <td>8</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 8 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>ARRIVAL_<br/>LOCATION_CODE_<br/>SEGMENT_1</td>
      <td>3</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>SEGMENT_<br/>CARRIER_CODE_1</td>
      <td>2</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>SEGMENT_1_<br/>FARE_BASIS</td>
      <td>15</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 15 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>CLASS_OF_<br/>SERVICE_CODE_<br/>SEGMENT_1</td>
      <td>2</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>FLIGHT_NUMBER_<br/>SEGMENT_1</td>
      <td>4</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 4 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>RESERVED</td>
      <td>3</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 3 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>SEGMENT_1_FARE</td>
      <td>12</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 12 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>STOPOVER_INDICATOR_2</td>
      <td>1</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 1 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>DEPARTURE_LOCATION_<br/>CODE_SEGMENT_2</td>
      <td>3</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>DEPARTURE_<br/>DATE_SEGMENT_2</td>
      <td>8</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 8 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>ARRIVAL_LOCATION_<br/>CODE_SEGMENT_2</td>
      <td>3</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>SEGMENT_<br/>CARRIER_CODE_2</td>
      <td>2</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>SEGMENT_2_<br/>FARE_BASIS</td>
      <td>15</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 15 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>CLASS_OF_<br/>SERVICE_<br/>CODE_SEGMENT_2</td>
      <td>2</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>FLIGHT_<br/>NUMBER_SEGMENT_2</td>
      <td>4</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 4 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>RESERVED</td>
      <td>3</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 3 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>SEGMENT_2_FARE</td>
      <td>12</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 12 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>STOPOVER_<br/>INDICATOR_3</td>
      <td>1</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 1 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>DEPARTURE_<br/>LOCATION_<br/>CODE_SEGMENT_3</td>
      <td>3</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>DEPARTURE_<br/>DATE_SEGMENT_3</td>
      <td>8</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 8 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>ARRIVAL_LOCATION_<br/>CODE_SEGMENT_3</td>
      <td>3</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>SEGMENT_<br/>CARRIER_CODE_3</td>
      <td>2</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>SEGMENT_3_<br/>FARE_BASIS</td>
      <td>15</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 15 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>CLASS_OF_SERVICE_<br/>CODE_SEGMENT_3</td>
      <td>2</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>FLIGHT_NUMBER_<br/>SEGMENT_3</td>
      <td>4</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 4 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>RESERVED</td>
      <td>3</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 3 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>SEGMENT_3_<br/>FARE</td>
      <td>12</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 12 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>STOPOVER_<br/>INDICATOR_4</td>
      <td>1</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 1 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>DEPARTURE_LOCATION_<br/>CODE_SEGMENT_4</td>
      <td>3</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>DEPARTURE_DATE_<br/>SEGMENT_4</td>
      <td>8</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 8 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>ARRIVAL_<br/>LOCATION_<br/>CODE_SEGMENT_4</td>
      <td>3</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 3 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>SEGMENT_<br/>CARRIER_<br/>CODE_4</td>
      <td>2</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>SEGMENT_4_<br/>FARE_BASIS</td>
      <td>15</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 15 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>CLASS_OF_<br/>SERVICE_CODE_<br/>SEGMENT_4</td>
      <td>2</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 2 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>FLIGHT_NUMBER_<br/>SEGMENT_4</td>
      <td>4</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 4 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>RESERVED</td>
      <td>3</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 3 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>SEGMENT_<br/>4_FARE</td>
      <td>12</td>
      <td><code>Numeric</code> - Numeric field with maximum length of 12 characters. Can only contain digits.</td>
    </tr>
    <tr>
      <td>STOPOVER_<br/>INDICATOR_5</td>
      <td>1</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 1 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>EXCHANGED/ORIGINAL_<br/>TICKET_NUMBER</td>
      <td>14</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 14 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
    <tr>
      <td>RESERVED</td>
      <td>313</td>
      <td><code>Alphanumeric</code> - Alphanumeric field with maximum length of 313 characters. Can contain letters, numbers, and special characters.</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>
