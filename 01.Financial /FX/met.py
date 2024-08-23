import yfinance as yf
import time
import datetime
interval = 5

def worker():
    weekday_names = ['月', '火', '水', '木', '金', '土', '日']
    dt_now = datetime.datetime.now()
    s=dt_now.strftime('%Y年%m月%d日 %H:%M:%S') +" " + weekday_names[dt_now.weekday()]+"曜日"
    print(s)
    TGT=191.906
    # 為替レートを取得
    ticker = "GBPJPY=X"
    fx_rate = yf.Ticker(ticker).history(period="1d").Close[0]
    # 結果を表示
    print(ticker)
    print(f"目標のレート: {TGT}")
    print(f"現在のレート: {fx_rate}")
    print(f"目標の差レート: {TGT-fx_rate}")
    time.sleep(15)
while True:
    worker()
    time.sleep(interval)



