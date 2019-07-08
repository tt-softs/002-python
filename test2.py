# from iexfinance.stocks import Stock
#
# aapl = Stock("AAPL")
#
# aapl.get_price()

from iexfinance.stocks import Stock

# a = Stock("AAPL", token="sk_f280b00195434cae97cfba1993b8265c") # pk_84f41691aceb46d2b6ef5e2909f9affd
a = Stock("AAPL") #

print(a.get_quote())
print(a.get_price())
