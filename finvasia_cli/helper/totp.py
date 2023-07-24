import pyotp
import datetime

def totp(token):
    totp = pyotp.TOTP(token)
    totp_code = totp.now()
    print(datetime.datetime.now())
    return totp_code
