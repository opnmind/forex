from tvDatafeed import TvDatafeed, Interval

tv = TvDatafeed()

data = tv.get_hist(symbol="EURUSD", exchange = "OANDA",interval=Interval.in_5_minute, n_bars=5000)

data.to_csv('EURUSD_M5_2023-12-22.csv')