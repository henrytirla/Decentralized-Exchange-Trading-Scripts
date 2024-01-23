// Convert Solana private key from/to base58/uint8array


const web3 = require("@solana/web3.js");
const bs58 = require('bs58');
let keypairString = "Privatekey String";

let secretKey = bs58.decode(keypairString);
console.log(`[${web3.Keypair.fromSecretKey(secretKey).secretKey}]`);