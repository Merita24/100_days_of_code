import requests

def get_binance():
  url="https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
  response=requests.get(url)
  data=response.json()
  return float(data['price'])

def get_coinbase():
    url="https://api.coinbase.com/v2/prices/BTC-USD/spot"
    response=requests.get(url)
    data=response.json()
    return float(data['price'])

def get_kraken():
    url="https://api.kraken.com/0/public/Ticker?pair=XXBTZUSD"
    response=requests.get(url)
    data=response.json
    return float(data['price'])

def aggregate_prices():
    price1=get_binance()
    price2=get_coinbase()
    price3=get_kraken()
    av=sum(price1,price2,price3)/3
    
    print(f"Binance price is {price1}")
    print(f"Coinbase price is {price2}")
    print(f"Kraken price is {price3}")
    print(f"Average price is {av}")
    