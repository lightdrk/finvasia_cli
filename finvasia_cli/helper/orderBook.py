from .login import start
from colorama import Fore

@start
def orderBook(data,api):
    #data = no need
    if data == None:
        response_orderBook = api.get_order_book()
    else:
        response_orderBook = api.single_order_history(data)
        print(response_orderBook)

    try:
        if response_orderBook['emsg']:
            exit(Fore.RED+f'{response_orderBook["emsg"]}')
    except KeyError:
        if (response_orderBook['stat']).lower() == 'ok':
            exit(Fore.GREEN + f'============Order Caneled =============')
    return response_orderBook