---
title: IMPL Mapping List
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
| Event ID | Event Name    | Customer use case description                                                                                                                                              | Fund Flow Type | IMPL Type        | IMPL ID                     |
| -------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ---------------- | :-------------------------- |
| 303014   | ICC UNLOAD    | Customer pays Merchant at checkout                                                                                                                                         | O              | P2M\_W2A\_O      | 0\|70000                    |
| 303003   | ICC RECHARGE  | Merchant refunds customer wallet payment                                                                                                                                   | OR             | P2M\_W2A\_O\_R   | OIR\|70000                  |
| 303014   | ICC UNLOAD    | Customer transfers funds to self -Bank A/C or peer Bank A/C                                                                                                                | O              | P2P\_W2A\_O      | 0\|70010                    |
| 303003   | ICC RECHARGE  | Self-Bank A/C or peer Bank A/C refunds the transaction made from the customer wallet (Rare)                                                                                | OR             | P2P\_W2A\_O\_R   | OR\|70010                   |
| 303014   | ICC UNLOAD    | Customer pays peer wallet through wallet linked mobile no                                                                                                                  | O              | P2P\_W2W\_O      | O\|70020                    |
| 303003   | ICC RECHARGE  | Customer receives money from peer wallet through wallet linked mobile no                                                                                                   | I              | P2P\_W2W\_I      | I\|70020                    |
| 303003   | ICC RECHARGE  | Client requests Wibmo prepaid to Load customer wallet with Just-in-Time funding to pay Merchant (Load+Unload API)                                                          | I,IO           | P2M\_A2W\_I      | I\|70130,IO\|70030          |
| 303014   | ICC UNLOAD    | Client requests Wibmo prepaid to Unload the wallet once Just-in-Time funding is done (Load+Unload API) to pay Merchant                                                     | O,IO           | P2M\_W2A\_O      | O\|70020                    |
| 303003   | ICC RECHARGE  | Merchant refunds customer wallet payment which was loaded with Just-in-time funding (Load+Unload API)                                                                      | OR,IOR         | P2M\_W2A\_O\_R   | I\|70020                    |
| 303014   | ICC UNLOAD    | Client wants merchant refund to customer wallet to be loaded back into client A/C or Pool A/C (Since it was just-in-time funding & funds belong to client)                 | OR,IOR         | P2M\_A2W\_O\_R   | OR\|70130 , IOR\|70040      |
| 303003   | ICC RECHARGE  | Client requests Wibmo prepaid to Load customer wallet with Just-in-Time funding to transfer funds to friend/family A/C (Load+Unload API)                                   | I,IO           | P2P\_A2W\_I      | I\|70130,IO\|70030          |
| 303003   | ICC RECHARGE  | Client requests Wibmo prepaid to Unload customer wallet once Just-in-Time funding is done to transfer funds to friend/family A/C (Load+Unload API)                         | O,IO           | P2P\_W2A\_O      | O\|70150 , IO\|70050        |
| 303003   | ICC RECHARGE  | Family/Friend refunds the funds transferred by customer which was loaded with Just-in Time funding                                                                         | OR,IOR         | P2P\_W2A\_O\_R   | OR\|70150,      IOR\|70050  |
| 303014   | ICC UNLOAD    | Client wants refund of fund transferred back to customer wallet to be loaded back into client A/C or Pool A/C (Since it was just-in-time funding & funds belong to client) | IR,IOR         | P2P\_A2W\_I\_R   | IR\|70140,       IOR\|70050 |
| 303014   | ICC UNLOAD    | Customer pays Merchant with wallet through Merchant UPI VPA/QR Code (Or Client requests post Just-in time funding of wallet)                                               | O,IO           | P2M\_W2A\_O\_UPI | O\|70160 , IO\|70060        |
| 303003   | ICC RECHARGE  | Client requests Wibmo prepaid to Load customer wallet with Just-in-Time funding to pay Merchant (Load+Unload API) UPI VPA/QR Code                                          | I,IO           | P2M\_A2W\_I\_UPI | I\|70170 ,   IO\|70060      |
