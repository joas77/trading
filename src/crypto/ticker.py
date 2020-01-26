import time
import bitso

api = bitso.Api()

for _ in range(100):
    time.sleep(1)
    print(api.ticker("btc_mxn"))
