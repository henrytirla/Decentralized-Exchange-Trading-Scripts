from web3 import Web3

# Replace 'YOUR_NODE_URL' with the URL of your Ethereum node
web3 = Web3(Web3.HTTPProvider('Enter your Node URL'))
latest_block = web3.eth.get_block('latest')

# Ensure connection to the node
if web3.is_connected():
    # Get the latest block
    latest_block = web3.eth.get_block('latest')
    #latest_block= 18792112
    gas_used = 300000  # Replace with the actual gas used by your transaction

    # Extract gas limit and base fee
    gas_limit = latest_block['gasLimit']
    base_fee = latest_block['baseFeePerGas']
    print(f"Latest Block: {latest_block['number']}")
    print(f"Gas Limit: {gas_limit}")
    print(f"Base Fee: {base_fee}")
    base_fee_gwei = base_fee / 10**9
    print(f"Base Fee (GWEI): {base_fee_gwei}")
    # Calculate transaction cost in Ether
    transaction_cost_ether = (gas_used * base_fee_gwei) / 10 ** 9
    print(f"Transaction Cost (Ether): {transaction_cost_ether}")
    gas_price_estimate = web3.eth.gas_price
    print(f"Gas Price Estimate (Wei): {gas_price_estimate}")

    # Convert gas price to Gwei for a more readable output
    gas_price_gwei = web3.from_wei(gas_price_estimate, 'gwei')
    print(f"Gas Price Estimate (Gwei): {gas_price_gwei}")
    print(f"Block status: {len(latest_block['transactions'])}")