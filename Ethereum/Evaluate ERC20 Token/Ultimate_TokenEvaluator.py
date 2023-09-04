from goplus.token import Token
from dateutil import parser
import requests
from web3 import Web3

class style():
    # Class of different text colours - default is white
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def analyze_token(token_address):
    #web3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/lTlatSTYDZmCv6wVLRIDff7S3kZhL2dq"))

    # token_address = input("Enter Token Address: ")
    # token_address = "0x4Ed4a9047401617B83891bE7b63e5B229B67e6DC"
    data = Token(access_token=None).token_security(
        chain_id="1", addresses=[token_address]
    )

    if float(data.result[token_address.lower()].is_open_source) != 1:
        print(style.RED + "Contract not verified" + style.RESET)
        return "CONTRACT NOT VERIFIED"

    def check_token_honeypot(token_address):


        # API endpoint URL

        url = "https://api.honeypot.is/v2/IsHoneypot"

        # Construct the query parameters
        params = {
            "address": token_address,
        }

        # Make the GET request
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            # print(data)

            flags = data['flags']
            liquidity = data['pair']['liquidity']

            pair_address = data['pair']['pair']['address']
            creation_timestamp = int(data['pair']['createdAtTimestamp'])

            # get_liquidity_lock_info(pair_address)

            is_honeypot = data['honeypotResult']['isHoneypot']

            honeypot_reason = data['honeypotResult'].get('honeypotReason', None)

            token_name = data['token']['name']
            token_symbol = data['token']['symbol']
            token_decimals = data['token']['decimals']
            token_total_holders = data['token']['totalHolders']

            column_width = 20

            simulation_results = {
                "BUY TAX": f"{data['simulationResult']['buyTax']:.2f}%",
                "SELL TAX": f"{data['simulationResult']['sellTax']:.2f}%",
                "TRANSFER TAX": f"{data['simulationResult']['transferTax']:.2f}%",
                "BUY GAS": data['simulationResult']['buyGas'],
                "SELL GAS": data['simulationResult']['sellGas'],
                "SOURCE CODE": "OPEN SOURCE",
            }

            recent_holders_analysis = {
                "HOLDERS ANALYSED": data['holderAnalysis']['holders'],
                "CAN SELL": data['holderAnalysis']['successful'],
                "CAN'T SELL": data['holderAnalysis']['failed'],
                "SIPHONED": data['holderAnalysis']['siphoned'],
                "AVERAGE TAX": f"{data['holderAnalysis']['averageTax']:.1f}%",
                "HIGHEST TAX": f"{data['holderAnalysis']['highestTax']:.1f}%",
                "AVERAGE GAS": f"{data['holderAnalysis']['averageGas']:,}",
            }

            if is_honeypot:
                print(style.RED + f"EXECUTION REVERTED\n{honeypot_reason}\n" + style.RESET)
                print(style.RED + f"{flags}")
                if float(simulation_results["BUY TAX"][:-1]) > 50 or float(simulation_results["SELL TAX"][:-1]) > 50:
                    print("WARNINGS")
                    print(
                        "The taxes on this token are extremely high. You will get significantly less from a trade than expected, be careful!")
                    print("The average tax is very high. Be careful!\n" + style.RESET)
            else:
                print(style.GREEN + "NOT A HONEYPOT" + style.RESET)
                print(f"TOKEN INFORMATION")
                print("============================================")
                print(f"{'Token Name:':{column_width- 18}}{token_name:{column_width- 18}}")
                print(f"{'Token Symbol:':{column_width- 18}}{token_symbol:{column_width- 18}}")
                print(f"{'Token Decimals:':{column_width - 18}}{token_decimals:{column_width - 18}}")
                print(f"{'Token Total Holders:':{column_width - 20}}{token_total_holders:{column_width - 20}}")
                print(f"Current Liquidity ${round(liquidity, 2)}")

    def check_security_checks(result):
        owner_address = result.owner_address
        creator_address = result.creator_address

        expected_outcomes = {
            "Open Source": 1,
            "Buy Tax": round(float(0.01) * 100, 1),
            "Sell Tax": round(float(0.01) * 100, 1),
            "Proxy Contract": 0,
            "Mintable": 0,
            "Can Take Back Ownership": 0,
            "Owner Change Balance": 0,
            "Hidden Owner": 0,
            "Has External Calls": 0,
            "Transfer Pausable": 0,
            "Cannot Sell All": 0,
            "Tax Modifiable": 0,
            "Is Honeypot": 0,
            "Has Blacklist": 0,
            "Has Whitelist": 0,
            #"Is Anti-Whale": 1,
            "Trading Cooldown": 0,
            "Personal Slippage Modifiable": 0,
            "Owner Balance Percent": 0.000000,
            "Creator Balance Percent": 0.000000
        }

        security_checks = [
            ("Open Source", result.is_open_source),
            ("Buy Tax", round(float(result.buy_tax) * 100, 1)),
            ("Sell Tax", round(float(result.sell_tax) * 100, 1)),
            ("Proxy Contract", result.is_proxy),
            ("Mintable", result.is_mintable),
            ("Can Take Back Ownership", result.can_take_back_ownership),
            ("Owner Change Balance", result.owner_change_balance),
            ("Hidden Owner", result.hidden_owner),
            ("Has External Calls", result.external_call),
            ("Transfer Pausable", result.transfer_pausable),
            ("Cannot Sell All", result.cannot_sell_all),
            ("Tax Modifiable", result.slippage_modifiable),
            ("Is Honeypot", result.is_honeypot),
            ("Has Blacklist", result.is_blacklisted),
            ("Has Whitelist", result.is_whitelisted),
            # ("Is Anti-Whale", result.is_anti_whale),
            ("Trading Cooldown", result.trading_cooldown),
            ("Personal Slippage Modifiable", result.personal_slippage_modifiable),
            ("Owner Balance Percent", round(float(result.owner_percent) * 100, 2)),
            ("Creator Balance Percent", round(float(result.creator_percent) * 100, 2))
        ]
        print(style.CYAN + "ANALYZING SMART CONTRACT", style.RESET)
        criteria_met = True

        if owner_address == creator_address:
            print(style.RED, "Deployer Address Owns Contract", style.RESET)


        for check_name, check_result in security_checks:
            expected_value = float(expected_outcomes[check_name])
            actual_value = float(check_result)

            if expected_outcomes[check_name] != float(check_result):
                print(style.RED + f"{check_name}: {check_result}" + style.RESET)
                criteria_met = False

        if criteria_met:
            print(style.GREEN + "TOKEN MEETS OUR CRITERIA-----Good to BUY?" + style.RESET)

        print(style.CYAN + "ANALYZING LP TOKENS", style.RESET)

        if int(result.lp_holder_count) > 0:
            for lp_holder in result.lp_holders:
                tag = lp_holder.tag
                locked_percentage = float(lp_holder.percent) * 100
                formatted_percentage = round(locked_percentage, 2)

                if lp_holder.is_locked == 1 and float(lp_holder.percent) > 0.05 and result.lp_holders[0].is_contract == 1:
                    end_time_str = result.lp_holders[0].locked_detail[0].end_time
                    opt_time_str = result.lp_holders[0].locked_detail[0].opt_time
                    end_time = parser.isoparse(end_time_str)
                    opt_time = parser.isoparse(opt_time_str)
                    time_difference = end_time - opt_time
                    days_locked = time_difference.days
                    seconds = time_difference.seconds
                    hours, remainder = divmod(seconds, 3600)
                    minutes, _ = divmod(remainder, 60)
                    print(f"Number of days locked: {days_locked} days, {hours} Hours, {minutes} minutes")
                    print(f"Locked Percentage: {formatted_percentage}  Provider : {tag}")
                elif lp_holder.is_locked == 1 and float(lp_holder.percent) > 0.05:
                    null_address = "0x0000000000000000000000000000000000000000"
                    dead_address = "0x000000000000000000000000000000000000dead"
                    if lp_holder.address == owner_address:
                        print(style.RED + f"Owner owns {formatted_percentage} of LP TOKENS", style.RESET)
                    elif lp_holder.address == creator_address:
                        print(style.RED + f"Creator owns {formatted_percentage} of LP TOKENS", style.RESET)
                    elif lp_holder.address == null_address:
                        print(f"NUll Address Owns {formatted_percentage} of LP TOKESN")
                    elif lp_holder.address == dead_address:
                        print(f"DEAD  Address Owns {formatted_percentage} of LP TOKESN")
                elif lp_holder.is_locked == 0 and float(lp_holder.percent) > 0.05:
                    null_address = "0x0000000000000000000000000000000000000000"
                    dead_address = "0x000000000000000000000000000000000000dead"
                    if lp_holder.address == owner_address:
                        print(style.RED + f"Owner owns {formatted_percentage} of LP TOKENS", style.RESET)
                    elif lp_holder.address == creator_address:
                        print(style.RED +f"Creator owns {formatted_percentage} of LP TOKENS", style.RESET)
                    elif lp_holder.address == null_address:
                        print(f"NUll Address Owns {formatted_percentage} of LP TOKESN")
                    elif lp_holder.address == dead_address:
                        print(f"DEAD  Address Owns {formatted_percentage} of LP TOKESN")
        else:
            print("UNKNOWN ADDRESS OWNS LP TOKENS")

    check_token_honeypot(token_address)
    result = data.result[token_address.lower()]
    check_security_checks(result)

if __name__ == "__main__":
    token_address = input("Enter Token Address: ")
    analyze_token(token_address)
