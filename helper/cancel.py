from .login import start
from colorama import Fore


@start
def cancel(data,api):
    cancel_response = api.cancel_order(orderno=data)
    try:
        if cancel_response['emsg']:
            exit(Fore.RED+f'{cancel_response["emsg"]}')
    except KeyError:
        if (cancel_response['stat']).lower() == 'ok':
            exit(Fore.GREEN + f'============Order Caneled =============')
    return cancel_response
