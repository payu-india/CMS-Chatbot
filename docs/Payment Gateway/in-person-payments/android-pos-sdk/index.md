---
title: Android POS SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Android POS SDK Integrations with payU
  description: >-
    Learn how to integrate your Android POS terminal with payU’s SDK for
    seamless transactions
  robots: index
next:
  description: ''
---
The PayU SDK API document provides detailed API information of PayU POS Solutions.

The PayU API suite provides programmatic access to card transaction. In designing the API, this is made simple, intuitive, and predictable. It adheres to common open and widely accepted standards, including REST for access, JSON format for the data and basic Authentication and Authorization.

This API suite assumes a good working knowledge of the payment application UI, concepts and terminology.

***

## Restful Architecture

Everything in PayU is represented as an object with a defined structure.

***

## HTTP Methods and Response Codes

All actions taken through the API are done via HTTP POST methods. HTTP Response codes are used to indicate success and error conditions.

***

## Input and Output Format

Request body data is expected to be in JSON, and the response body data is returned as JSON.

***

## Handler

A Handler allows you to send and process Message and Runnable objects associated with a thread’s MessageQueue. Each Handler instance is associated with a single thread and that thread’s message queue. When you create a new Handler, it is bound to the thread / message queue of the thread that is creating it from that point on, it will deliver messages and runnables to that message queue and execute them as they come out of the message queue. For more information on Message and MessageQueue, Message and MessageQueue of Android Developer Documentation.

***

## Activity

An activity is a single, focused thing that the user can do. Almost all activities interact with the user, so the Activity class takes care of creating a window for you in which you can place your UI with setContentView(View). While activities are often presented to the user as full-screen windows, they can also be used in other ways: as floating windows (using a theme with windowIsFloating set) or embedded inside another activity (using ActivityGroup).  For more information on these view and theme, refer to the following from Android Developer Documentation:

* setContentView(View)
* windowIsFloating set
* ActivityGroup

***

## Bluetooth

Provides classes that manage Bluetooth functionality, such as scanning for devices, connecting with devices, and managing data transfer between devices. The Bluetooth API supports both “ClassicBluetooth” and Bluetooth Low Energy. To perform Bluetooth communication using these API’s, an application must declare the BLUETOOTH permission. Some additional functionality, such as requesting device discovery, also requires the `BLUETOOTH_ADMIN` permission. For more information on these permissions, refer to BLUETOOTH and `BLUETOOTH_ADMIN` from the Android Developer Documentation.
