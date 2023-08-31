import requests

#TODO Add additional checks based on research
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

def check_token_honeypot():
    token_address= input("Enter Token Address: ")
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
        is_honeypot = data['honeypotResult']['isHoneypot']
        honeypot_reason = data['honeypotResult'].get('honeypotReason', None)

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
            "EXTREMELY HIGH TAX HOLDERS": data['holderAnalysis']['highTaxWallets'],
        }

        column_width = 30

        if is_honeypot:
            print(style.RED + f"EXECUTION REVERTED\n{honeypot_reason}\n" + style.RESET)
            if float(simulation_results["BUY TAX"][:-1]) > 50 or float(simulation_results["SELL TAX"][:-1]) > 50:
                print("WARNINGS")
                print(
                    "The taxes on this token are extremely high. You will get significantly less from a trade than expected, be careful!")
                print("The average tax is very high. Be careful!\n")
            print("SIMULATION RESULTS")
            for key, value in simulation_results.items():
                print(f"{key:{column_width}}{value:{column_width}}")
            print(f"BUY LIMIT:{'NONE DETECTED':{column_width}}SELL LIMIT:{'NONE DETECTED':{column_width}}")
            print("EXTREMELY HIGH TAX HOLDERS\n" + data['holderAnalysis']['highTaxWallets'])
            print("\nRECENT HOLDERS ANALYSIS")
            for key, value in recent_holders_analysis.items():
                print(f"{key:{column_width}}{value:{column_width}}")
        else:
            print(style.GREEN + "NOT A HONEYPOT" + style.RESET)
            print("SIMULATION RESULTS")
            for key, value in simulation_results.items():
                print(f"{key:{column_width}}{value:{column_width}}")
            print(f"BUY LIMIT:{'NONE DETECTED':{column_width}}SELL LIMIT:{'NONE DETECTED':{column_width}}")
            print("EXTREMELY HIGH TAX HOLDERS\n" + data['holderAnalysis']['highTaxWallets'])
            print("\nRECENT HOLDERS ANALYSIS")
            for key, value in recent_holders_analysis.items():
                print(f"{key:{column_width}}{value:{column_width}}")


check_token_honeypot()
