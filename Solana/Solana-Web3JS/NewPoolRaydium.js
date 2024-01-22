import { Connection,PublicKey } from "@solana/web3.js";
const RAYDIUM_PUBLIC_KEY = ('675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8');
const raydium = new PublicKey(RAYDIUM_PUBLIC_KEY);
const connection = new Connection('https://api.mainnet-beta.solana.com',{
    wsEndpoint: 'wss://api.mainnet-beta.solana.com'

});

let processedSignatures = new Set();

async function main(connection,raydium){
    console.log('Monitoring logs...',raydium.toString());
    connection.onLogs(raydium,({logs,err,signature})=>{
        if(err) return;
        if(logs && logs.some(log=> log.includes('initialize2') && !processedSignatures.has(signature))){
            processedSignatures.add(signature);
            console.log('Signature for Initialize2:',signature);
            fetchRaydiumAccounts(signature,connection);
        }
    }, "finalized");
}

async function fetchRaydiumAccounts(signature,connection){
    const txId = signature;
    const tx = await connection.getParsedTransaction(txId, {maxSupportedTransactionVersion:0, commitment:"confirmed"});
    const accounts = tx?.transaction?.message?.instructions.find(ix=>ix.programId.toBase58()===RAYDIUM_PUBLIC_KEY).accounts;

    if(!accounts){
        console.log('No accounts found');
        return;
    }
    const tokenAIndex=8;
    const tokenBIndex=9;

    const tokeAAccount = accounts[tokenAIndex];
    const tokenBAccount = accounts[tokenBIndex];
    const displayData=[
        {Token:'Token A',account:tokeAAccount},
        {Token:'Token B',account:tokenBAccount},
    ];
    console.log("New Raydium  Liquidity Pool Created Found");
    console.log(generateExplorerUrl(txId));
    console.table(displayData);
    // await sleep(2000);
}

function generateExplorerUrl(txId){
    return `https://solscan.io/tx/${txId}?cluster=mainnet`;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


// main(connection,raydium).catch(console.error);
async function runProgram() {
    try {
        await main(connection, raydium);
    } catch (error) {
        console.error(`Error occurred: ${error}`);
        console.log('Restarting the program...');
        runProgram();
    }
}

runProgram().catch(console.error);