from .login import start
from colorama import Fore

@start
def orderBook(data,api):
    #data = no need
    if data == None:
        response_orderBook = api.get_order_book()
        for num,n in enumerate(response_orderBook):
            print(Fore.RED+f'{num}',Fore.GREEN + f'{n}')
            print()
    else:
        response_orderBook = api.single_order_history(data)
        try:
            if response_orderBook['emsg']:
                print(response_orderBook)
                exit(Fore.RED+f'{response_orderBook["emsg"]}')
        except KeyError:
            if (response_orderBook['stat']).lower() == 'ok':
                exit(Fore.GREEN+f'{response_orderBook}')
    return response_orderBook