import pyupbit

ticker = pyupbit.get_tickers(fiat='KRW')

print("=====================")

for i in range(0, len(ticker)):
    data = pyupbit.get_ohlcv(ticker[i])
    live_price = pyupbit.get_current_price(ticker[i])
    close_avg = data['close'].tail(5).mean()

    if live_price > close_avg:
        print("현재가: {}원".format(int(live_price)))
        print("종가 이동 평균: {}원".format(int(close_avg)))
        print(ticker[i] + " 상승장!")
        print("=====================")
    else:
        print("현재가: {}원".format(int(live_price)))
        print("종가 이동 평균: {}원".format(int(close_avg)))
        print(ticker[i] + " 하락장!")
        print("=====================")