import requests
import datetime
from goplus.token import Token
from dateutil import parser


# API endpoint URL
url = "https://api.honeypot.is/v2/IsHoneypot"

class style():  # Class of different text colours - default is white
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
    null_address = "0x0000000000000000000000000000000000000000"
    dead_address = "0x000000000000000000000000000000000000dead"
    ##GOPLUS SECURITY####
    data1 = Token(access_token=None).token_security(
        chain_id="1", addresses=[token_address])
    result = data1.result[token_address.lower()]
    params = {"address": token_address}
    response = requests.get(url, params=params)

    if result.is_open_source == str(1):
        print("============================================")
        print(style.GREEN + f" CONTRACT OPEN SOURCE ✅" + style.RESET)
    else:
        print(style.RED + f"NOT OPEN SOURCE" + style.RESET)
        return

    if response.status_code == 200:
        data = response.json()
        simulation_Success= data['simulationSuccess']
        column_width = 20
        pair_address = data['pair']['pair']['address']
        creation_timestamp = int(data['pair']['createdAtTimestamp'])
        datetime_obj = datetime.datetime.utcfromtimestamp(creation_timestamp)
        current_time = datetime.datetime.utcnow()
        # Calculate the time difference
        time_difference = current_time - datetime_obj
        days = time_difference.days
        hours, remainder = divmod(time_difference.seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        # Combine measures into a single variable
        formatted_time_difference = f"{days} days, {hours} hours, {minutes} minutes ago"
        tokenAddress= data['token']['address']
        token_name = data['token']['name']
        token_symbol = data['token']['symbol']
        token_decimals = data['token']['decimals']
        token_total_holders = data['token']['totalHolders']
        liquidity = data['pair']['liquidity']
        highest_tax= data['holderAnalysis']['highestTax']
        average_tax= data['holderAnalysis']['averageTax']




        if simulation_Success:
           is_honeypot= data['honeypotResult']['isHoneypot']

           if  is_honeypot:
               flags = data['flags']
               honeypot_reason = data['honeypotResult'].get('honeypotReason', None)
               print(style.RED + f"EXECUTION REVERTED\n{honeypot_reason}\n   {flags}" + style.RESET)
               return




           else:
                print("============================================")
                print(style.YELLOW+f"TOKEN INFORMATION",style.RESET)
                print("============================================")
                print(f"{'Token Address:':{column_width - 18}}{tokenAddress:{column_width - 18}}")
                print(f"{'Token Name:':{column_width - 18}}{token_name:{column_width - 18}}")
                print(f"{'Token Symbol:':{column_width - 18}}{token_symbol:{column_width - 18}}")
                print(f"{'Token Decimals:':{column_width - 18}}{token_decimals:{column_width - 18}}")
                print(f"{'Current Holders:':{column_width - 20}}{style.GREEN}{token_total_holders:{column_width - 20}}",
                      style.RESET)
                print(f"{'AverageTax:':{column_width - 20}}{style.RED}{round(average_tax,2):{column_width - 20}}", style.RESET)
                print(f"{'Highest Tax:':{column_width - 20}}{style.RED}{highest_tax:{column_width - 20}}", style.RESET)
                print(f"Current Liquidity {style.GREEN} ${round(liquidity, 2)}", style.RESET)
                print(f"Token Created :{style.BLUE} {formatted_time_difference}", style.RESET)

        owner_address = result.owner_address
        creator_address = result.creator_address
       

        expected_outcomes = {
            "Open Source": 1,
            "Buy Tax": round(float(0.02) * 100, 1),
            "Sell Tax": round(float(0.02) * 100, 1),
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
            # "Is Anti-Whale": 1,
            "Trading Cooldown": 0,
            "Personal Slippage Modifiable": 0,
            "Owner Balance Percent": 2.000000,
            "Creator Balance Percent": 2.000000
        }

        buy_tax_value = result.buy_tax
        sell_tax_value = result.sell_tax

        if isinstance(buy_tax_value, str) and buy_tax_value == "Unknown" or buy_tax_value == '':
            print(buy_tax_value)  # This will print "Unknown"
            buy_tax_value = "Unknown"
        else:
            #buy_tax_value = int(buy_tax_value)
            buy_tax_value = round(float(buy_tax_value) * 100, 1)

        if isinstance(sell_tax_value, str) and sell_tax_value == "Unknown" or sell_tax_value == '':
            print(sell_tax_value)  # This will print "Unknown"
            sell_tax_value = "Unknown"
        else:
            sell_tax_value = round(float(sell_tax_value) * 100, 1)



        security_checks = [
            ("Open Source", result.is_open_source),
            ("Buy Tax", buy_tax_value),
            ("Sell Tax", sell_tax_value),
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
        print("============================================")

        print(style.YELLOW+"SMART CONTRACT SECURITY CHECKS",style.RESET)

        print("============================================")
     

        if owner_address == creator_address:
            print(style.RED, "🚨 Deployer Address Owns Contract 🚨", style.RESET)
            # return

        
        for check_name, check_result in security_checks:
            expected_value = float(expected_outcomes[check_name])

            if check_result is None or check_result == '':
                actual_value = "Unknown"
            elif isinstance(check_result, str) and check_result != "Unknown":
                #actual_value = check_result
                actual_value = float(check_result)
            elif isinstance(check_result, str) and check_result == "Unknown":
                #actual_value = check_result
                actual_value = check_result
            else:
                actual_value = float(check_result)
            if isinstance(actual_value, float):
                if expected_outcomes[check_name] != actual_value:
                    print(style.RED + f"{check_name}: {actual_value} -{style.GREEN}Expected <= {expected_outcomes[check_name]}" + style.RESET)
            elif isinstance(actual_value, str) and str(actual_value) != str(expected_outcomes[check_name]):
                print(style.RED + f"{check_name}: {actual_value} -{style.GREEN}Expected <= {expected_outcomes[check_name]}" + style.RESET)


        print("============================================")

        print(style.YELLOW + "ANALYZING LIQUIDITY POOL TOKENS", style.RESET)
        print("============================================")

        if  result.lp_holders != None:
            for lp_holder in result.lp_holders:
                tag = lp_holder.tag
                locked_percentage = float(lp_holder.percent) * 100
                formatted_percentage = round(locked_percentage, 2)

                if lp_holder.is_locked == 1 and float(lp_holder.percent) > 0.05 and result.lp_holders[
                    0].is_contract == 1:
                   
                    if result.lp_holders[0].locked_detail != None:
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
                    else:
                       
                        print(f"Locked Percentage: {formatted_percentage}  Provider : {tag}")
                elif lp_holder.is_locked == 0 and lp_holder.address!= creator_address and lp_holder.address != creator_address:
                  
                    print(style.RED + f"UNKNOWN Address {lp_holder.address} OWNS {formatted_percentage} of LP TOKENS",style.RESET)


                elif lp_holder.is_locked == 1 and float(lp_holder.percent) > 0.05:

                    if lp_holder.address == owner_address:
                        

                        print(style.RED + f"Owner owns {formatted_percentage} of LP TOKENS", style.RESET)
                    elif lp_holder.address == creator_address:
                   
                        print(style.RED + f"Creator owns {formatted_percentage} of LP TOKENS", style.RESET)
                    elif lp_holder.address == null_address:
                        
                        print(f"NUll Address Owns {formatted_percentage} of LP TOKESN")
                    elif lp_holder.address == dead_address:
                        
                        print(f"DEAD  Address Owns {formatted_percentage} of LP TOKESN")
                elif lp_holder.is_locked == 0 and float(lp_holder.percent) > 0.05:

                    if lp_holder.address == owner_address:
                        

                        print(style.RED + f"Owner owns {formatted_percentage} of LP TOKENS", style.RESET)
                    elif lp_holder.address == creator_address:
                        
                        print(style.RED + f"Creator owns {formatted_percentage} of LP TOKENS", style.RESET)
                elif lp_holder.is_locked == 0 and float(lp_holder.percent) > 0.05:

                    if lp_holder.address == owner_address and owner_address == null_address:
                        
                        print(style.GREEN + f"NULL ADDRESS  owns {formatted_percentage} of LP TOKENS", style.RESET)
                    elif lp_holder.address == creator_address and owner_address == null_address:

                        
                        print(
                            style.RED + f"Creator owns {formatted_percentage} of LP TOKENS ---This might be actually locked",
                            style.RESET)
                        
                    elif lp_holder.address == null_address:
                      
                        print(f"NUll Address Owns {formatted_percentage} of LP TOKESN")
                    elif lp_holder.address == dead_address:
                        
                        print(f"DEAD Address Owns {formatted_percentage} of LP TOKESN")
                
        else:
            print("UNKNOWN ADDRESS OWNS LP TOKENS")
        #### CHECKING BUYING CONDITION####
        #PREMIUM SERVICE
        #############################
       




if __name__ == "__main__":
   token_address = input("Enter Token Address: ")
   analyze_token(token_address)
