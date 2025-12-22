---
name: PayU_Labs
---
<Callout icon="👍" theme="okay">
  Experience the flow, generate code for the website to integrate PayU Hosted Checkout with zero coding knowledge. 

  <HTMLBlock>{`
            <style>
            .tooltip-btn {
                position: relative;
                background-color: #4CAF50;
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

            <button onclick="window.open('https://payu.in/integrationlab/payu-hosted', '_blank')" 
                    class="tooltip-btn" 
                    data-tooltip="Automatically generate code including hashing for your eCommerce website to integrate PayU Hosted Checkout with zero coding knowledge.">
                Click Here to Generate Code
            </button>
  `}</HTMLBlock>
</Callout>
