from .login import start
from colorama import Fore


@start
def order(data,api):
    response_place_order = api.place_order(buy_or_sell=data['side'], product_type=data['productType'],
                                    exchange=data["exchange"], tradingsymbol=data["symbol"],quantity=data["qty"],
                                    discloseqty=data['disclosedQty'],price_type=data['type'], price=data['limitPrice'],
                                    trigger_price=data['triggerPrice'],retention=data["validity"], remarks='order',trail_price=data['trailPrice'],bookprofit_price=data['bookProfit'])
    
    try:
        if response_place_order['emsg']:
            exit(Fore.RED+f'{response_place_order["emsg"]}')
    except KeyError:
        if (response_place_order['stat']).lower() == 'ok':
            exit(Fore.GREEN + f'============Order Placed =============')
    return response_place_order
