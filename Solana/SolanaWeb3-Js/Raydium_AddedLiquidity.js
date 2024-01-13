/**
 *
 * SCANNING FOR NEW LIQUIDITY POOLS CREATED ON RAYDIUM DEX
 */


const {Connection,PublicKey} = require('@solana/web3.js');

const RAYDIUM_PUBLIC_KEY = ('675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8');
const SESSION_HASH='TIRLA'+ Math.ceil(Math.random()*1e9);
let credits=0;
const raydium = new PublicKey(RAYDIUM_PUBLIC_KEY);
const connection = new Connection('https://api.mainnet-beta.solana.com',{
    wsEndpoint: 'wss://api.mainnet-beta.solana.com',
    httpHeaders: {"x-session": SESSION_HASH}
    // commitment: 'confirmed',
});

//monitor logs
async function main(connection,raydium){
    console.log('Monitoring logs...',raydium.toString());
    //console.log(connection.logs(raydium));
    connection.onLogs(raydium,({logs,err,signature})=>{
        if(err) return;
        if(logs && logs.some(log=> log.includes('initialize2'))){
            console.log('Signature for Initialize2:',signature);
            fetchRaydiumAccounts(signature,connection);
        }
    }, "finalized");
}

async function fetchRaydiumAccounts(signature,connection){
    const txId = signature;

    const tx = await connection.getParsedTransaction(
        txId,
        {maxSupportedTransactionVersion:0,
        commitment:"confirmed"});
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
    console.log("New LP Found");
    console.log(generateExplorerUrl(txId));
    console.table(displayData);
}

function generateExplorerUrl(txId){
    return `https://solscan.io/tx/${txId}?cluster=mainnet`;
}

main(connection,raydium).catch(console.error);