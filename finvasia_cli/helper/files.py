import os 
import json
from colorama import Fore

def cred():
    uid = input("uer id: ")
    pwd = input("pasword: ")
    otp_token = input("otp token: ")
    vc = uid+"_U"
    app_key = input("app key: ")
    imei = "abc123"

    data = {"uid":uid,"pwd": pwd,"otp_token": otp_token,"vc": vc, "app_key":app_key, "imei":imei}
    try:
        with open(os.path.join(os.getcwd(),'helper','cred.json'),'w') as cr:
            json.dump(data,cr)
    except Exception as err:
        exit(Fore.RED+err)
    
    return 1

def credFetch():
    with open(os.path.join(os.getcwd(),'helper','cred.json'),'r') as cr:
        data = json.load(cr)

    return data
            