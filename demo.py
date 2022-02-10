from ib_insync import *

ib = IB()
ib.connect("127.0.0.1", 7497, clientId=1)

# contract = Forex("EURUSD")
stock = Stock("AMD", "SMART", "USD")

# Historical data
bars = ib.reqHistoricalData(
    stock,
    endDateTime="",
    durationStr="30 D",
    barSizeSetting="1 hour",
    whatToShow="MIDPOINT",
    useRTH=True,
)

# convert to pandas dataframe:
# df = util.df(bars)
# print(df)

# Realtime Market data
market_data = ib.reqMktData(stock, "", False, False)

print(market_data)


def onPendingTicker(ticker):
    print("pending ticker event recieved")
    print(ticker)


ib.pendingTickersEvent += onPendingTicker

ib.run()
