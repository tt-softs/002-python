from datetime import datetime

from iexfinance.stocks import get_historical_data

start = datetime(2019, 7, 1)

end = datetime(2019, 7, day=3)

df = get_historical_data("TSLA", start, end, output_format='pandas')
print(df)
