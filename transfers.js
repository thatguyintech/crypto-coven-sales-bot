const { createAlchemyWeb3 } = require("@alch/alchemy-web3");
require("dotenv").config();

// Using WebSockets
const web3 = createAlchemyWeb3(
  process.env.ALCHEMY_WS_URL,
);

// Many web3.js methods return promises.
// web3.eth.getBlock("latest").then(block => {
//     /* … */
//   });
  
//   web3.eth
//     .estimateGas({
//       from: "0xge61df…",
//       to: "0x087a5c…",
//       data: "0xa9059c…",
//       gasPrice: "0xa994f8…",
//     })
//     .then(gasAmount => {
//       /* … */
//     });
  
web3.eth
  .getMaxPriorityFeePerGas().then(console.log);

web3.eth
  .getFeeHistory(4, "latest", [25, 50, 75]).then(console.log);