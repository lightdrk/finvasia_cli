from .login import start
from colorama import Fore

@start
def modify(data,api):

    response = api.modify_order(orderno=data['orderno'], exchange=data["exchange"], tradingsymbol=data["symbol"], newquantity=data['qty'],
                                newprice_type=data['type'], newprice=data['limitPrice'], newtrigger_price=data['triggerPrice'],
                                bookloss_price = data['bookLoss'],bookprofit_price = data['bookProfit'], trail_price = data['trailPrice'])
    try:
        if response['emsg']:
            exit(Fore.RED+f'{response["emsg"]}')
    except KeyError:
        if (response['stat']).lower() == 'ok':
            exit(Fore.GREEN + f'============Order Caneled =============')
    return response

