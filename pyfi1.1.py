import yfinance as yf

#TICKR symbols for microsoft
microsoft = yf.Ticker("MSFT")
microsoft.info
print(microsoft.info)

#TICKR symbols for Google
google = yf.Ticker("GOOGL")
google.info
google = yf.Ticker("GOOG")
google.info
print(google.info)

#TICKR symbols for tesla
tesla = yf.Ticker("TSLA")
tesla.info
print(tesla.info)
