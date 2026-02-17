---
title: Proof Of Concept
excerpt: This page is to try custom codes in Readme (DO NOT PUBLISH)
deprecated: false
hidden: true
metadata:
  robots: index
---
<br />

Accelerate your integration workflow with our net banking Postman collection for PayU Hosted Checkout. Click the Download Postman Collection button below to download and get started.

<HTMLBlock>{`
                <style>
                .tooltip-btn {
                    position: relative;
                    background-color: #d85947;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-weight: bold; /* Added this line */
                }
                .tooltip-btn:hover::after {
                    content: attr(data-tooltip);
                    position: absolute;
                    bottom: 125%;
                    left: 50%;
                    transform: translateX(-50%);
                    background-color: #333;
                    color: white;
                    padding: 5px 10px;
                    border-radius: 4px;
                    white-space: nowrap;
                    font-size: 12px;
                    z-index: 1;
                }
                </style>

                <button onclick="window.open('https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/overview', '_blank')" 
                        class="tooltip-btn" 
                        data-tooltip="Click to download the Postman collection and explore APIs.">
                    Download Postman Collection
                </button>
`}</HTMLBlock>
