from helper.files import cred , credFetch
from helper.orderBook import orderBook
from helper.holding import Holdings
from helper.login import checking
from helper.cancel import cancel
from helper.modify import modify
from helper.order import order
from colorama import Fore
import argparse


def OrderOptionCheck():
    if args.symbol == None:
        exit(Fore.RED + "Refer to manual , usage using -h OR --help")
    if args.qty == None:
        exit(Fore.RED + "Refer to manual , usage using -h OR --help")
    if args.type == None:
        exit(Fore.RED + "'type' option needs value Refer to manual")
    if args.validity == None:
        exit(Fore.RED +"'validity' option needs value Refer to manual")




if __name__ == '__main__':

    usage='''%(prog)s <command> [options]

    Commands:
    1. --gen                            Generate something
    2. <symbol> <product> <validity> [--qty <QTY> --type <TYPE> --buy/--sell]       order placement.
    3. --modify <orderId> --symb <symbol>[--qty <QTY> --type <TYPE> --limitPrice <PRICE> --stopPrice <PRICE>]   modifing order.
    4. --history <orderID>|--history    specific or history | retrives orders placed current trading day.              
    5. --cancel <orderID>               to cancel an order.
    6. --holding <product>              to fetch holding using product type.
    
    Options:
    
    --qty <QTY>                     Specify quantity. for *Modified Its Open Qty/Pending Qty plus Filled Shares (cumulative for the order) for the order.
                                    * Please do not send only the pending qty in this field 
    --type <TYPE>                   Specify order type.
    --buy                           Buy option.
    --sell                          Sell option.
    --limitPrice <PRICE>            Specify limit price.
    --stopPrice <PRICE>             Specify stop price.
    --offlineOrder                  Include it for When placing AMO order.
    --disclosed                     disclosedQty Allowed only for Equity.

    Choices & Discription:
    1. <product>   ["C","I","M","H","B"]                    C => For equity only
                                                            M => NRML.
                                                            I => MIS.
                                                            H => Cover Order
                                                            B => Bracket Order
    
    2. <validity>    ["IOC","DAY"]                          IOC => Immediate or Cancel
                                                            DAY => Valid till the end of the day

    3. --offlineOrder ["True", "False"]                     False => When market is open
                                                            True => When placing AMO order
                            
    4. --type                                               LMT => Limit Order
                                                            MKT => Market Order
                                                            SL-MKT => Stop Order (SL-M)
                                                            SL-LMT => Stoplimit Order (SL-L)
                                                            DS 
                                                            2L 
                                                            3L 

    5. --limitPrice                                         Default => 0
                                                            Provide valid price for Limit and Stoplimit orders
                                                            *leave empty if dont want to use 
    
    6. --stopPrice                                          Default => 0
                                                            Provide valid price for Stop and Stoplimit orders
                                                            *leave empty if dont want to use .
                                                            
    7. --disclosed                                          disclosedQty*
                                                            Default => 0
                                                            Allowed only for Equity
                                                            *leave empty if dont want to use 
    
    8. --stopLoss                                           Default => 0
                                                            Provide valid price for H and B orders

    9. --takeProfit                                         Default => 0
                                                            Provide valid price for B orders
    
    10. --buy                                               *does't need value

    11. --sell                                              *does't need value


    '''
    parser = argparse.ArgumentParser(prog="finvasia", usage=usage)
    
    group = parser.add_mutually_exclusive_group(required=False)
    group1 = parser.add_mutually_exclusive_group(required=True)  


    #generating everything first time
    group1.add_argument("-gen","--generate",action="store_true",default=None,help="for generating new auth_code and access token")

    group1.add_argument('symbol',nargs='?',help="Example: '[symbol] NSE:SBIN-EQ' OR '-s NSE:SBIN-EQ'")
    
    group1.add_argument('--modify',nargs='?',help="Example: 'orderID --type --qty --limit(limitPrice)/--stop(stopLoss)' OR 'orderID --type Limit --qty 100 --limit 12.12'")

    group1.add_argument('--history',nargs='?',const=True,default=None,action='store',help="Example: --history orderId OR --history")

    group1.add_argument('--cancel',nargs='?',help="Example: --cancel <orderId>")

    group1.add_argument('--holding',nargs='?',choices=["C","I","M","H","B"] ,help="Example: --holding <product_type>")

    parser.add_argument('product',nargs='?',choices=["C","I","M","H","B"] ,help="Example: '[product] CNC' ")
    
    parser.add_argument('validity',nargs='?',choices=["IOC","DAY"],help="Example: '[validity] IOC'")
    
    parser.add_argument('--qty',nargs='?', help="Example: '--qty [quantity] 100'",type=int)
    parser.add_argument('--type',nargs='?',choices=["LMT","MKT","SL-MKT","SL-LMT","DS","2L","3L"],help="Example: '[type] limit'",type=str)
    group.add_argument('--buy', action='store_true', help='Buy option')
    group.add_argument('--sell', action='store_true', help='Sell option')

  
    parser.add_argument('--offlineOrder',default="False",help="Example: '--offlineOrder True'",choices=["True","False"])
    parser.add_argument('--trailPrice',default=0,help="Example: '--stopLoss 12.12'",type=float)
    parser.add_argument('--bookProfit',default=0,help="Example: '--takeProfit 12.5'",type=float)
    parser.add_argument('--limitPrice',default=0, help="Example: '--limit 12.1'",type=float)
    parser.add_argument('--triggerPrice',default=None, help="Example: '--stop 1222.1'",type=float)
    parser.add_argument('--disclosed',default=0, help="Example: '--disclosed 12" ,type=int)
    parser.add_argument('--bookLoss',default=0,help="Example: '--takeProfit 12.5'",type=float)
    parser.add_argument('--symb',help='example: --symb "NSE:M&M"')
    
    
    args = parser.parse_args()

    if args.generate:
        cred()
        try:
            tick = checking(credFetch)
            if  tick:
                print(Fore.GREEN+'================GENERATED=================')
        except:
            print(Fore.RED+'================UNABLE GENERATED=================')  
        
            
    elif args.modify:
        exchange_trade = [None,None]
        if args.symb:
            exchange_trade = args.symb.lstrip(':')
        data={"orderno":args.modify,'exchange':exchange_trade[0],'symbol':exchange_trade[1],'limitPrice':0.0,'bookLoss':0.0,'trail_price':0.0,'triggerPrice':None,'trailPrice':0.0,'bookProfit':0.0}
        if args.limitPrice:
            data["limitPrice"] = args.limitPrice
        if args.bookLoss:
            data["bookLoss"] = args.stopPrice
        if args.type:
            data["type"] = args.type
        if args.qty:
            data["qty"] = args.qty
        if args.triggerPrice:
            data['triggerPrice'] = args.triggerPrice
        if args.bookProfit:
            data['bookProfit'] = args.bookProfit
        if args.trailPrice:
            data['trailPrice'] = args.trailPrice
        response = modify(data)
    elif args.history:
        if isinstance(args.history,str):
            print(Fore.BLUE + args.history)
            print(Fore.GREEN+ '-------------------------------------------------------{orderBook=={OrderID}}---------------------------------------------------------------------------\n')
            orderBook(args.history)   
        else:
            print(Fore.GREEN+ '---------------------------------------------------------orderBook-----------------------------------------------------------------------------\n')
            orderBook_response = orderBook(data=None)
            #orderTemplate.template(orderBook_response)
    elif args.cancel:
        cancel_response = cancel(data=args.cancel)
        print(cancel_response)
        
    elif args.holding:
        Holdings(data=args.holding)
    else:
        OrderOptionCheck()
        if args.buy or args.sell:
            if args.buy:
                value = 'B'
            else:
                value = 'S'
                
        else:
            parser.error('any of the buy OR sell needed')
        
        exchange_trade = args.symbol.lstrip(':')
        data = {
        "exchange":exchange_trade[0],
        "symbol": exchange_trade[1], 
        "qty": args.qty,
        "type": args.type,
        "side": value,
        "productType": args.product,
        "limitPrice": args.limitPrice,
        "validity": args.validity,
        "disclosedQty": args.disclosed,
        "bookLoss": args.bookLoss,
        "bookProfit":args.bookProfit,
        "triggerPrice":args.triggerPrice,
        "trailPrice":args.trailPrice,
        "offlineOrder": args.offlineOrder
        }
        order(data)
