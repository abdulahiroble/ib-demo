from ib_insync import *

ib = IB()
ib.connect("127.0.0.1", 7497, clientId=1)

stock = Stock("AMD", "SMART", "USD")

ib.qualifyContracts(stock)

chains = ib.reqSecDefOptParams("AAPL", "stock")
