from .api_helper import ShoonyaApiPy
from .files import credFetch
from .totp import totp
import logging

def checking(data):
    #enable dbug to see request and responses
    api = ShoonyaApiPy()
    #start of our program
    c_data = credFetch()
    #credentials
    
    uid     =  c_data['uid'] #<uid>
    pwd     = c_data['pwd']#<password>
    otp     = totp(c_data['otp_token'])
    factor2 = otp
    vc      = c_data['vc']#<uid_U>
    app_key = c_data['app_key']#<secret key>
    imei    = c_data['imei']#<mac>
    #make the api call
    ret = api.login(userid=uid, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)
    return ret

def start(func):
    def Login(data):
        #enable dbug to see request and responses
        api = ShoonyaApiPy()
        #start of our program
        c_data = credFetch()
        #credentials
        
        uid     =  c_data['uid'] #<uid>
        pwd     = c_data['pwd']#<password>
        otp     = totp(c_data['otp_token'])
        factor2 = otp
        vc      = c_data['vc']#<uid_U>
        app_key = c_data['app_key']#<secret key>
        imei    = c_data['imei']#<mac>
        #make the api call
        ret = api.login(userid=uid, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)
        func(data,api=api)
        return ret
    return Login
