from helper.login import start
from colorama import Fore
@start
def Holdings(data,api):
    #data = product_type
    response_holding = api.get_holdings(data)
    try:
        for n in response_holding:
            print(Fore.GREEN +f'{n}')
    except Exception as err:
        print(response_holding)
        exit(Fore.RED+f"{err}")
    return response_holding
