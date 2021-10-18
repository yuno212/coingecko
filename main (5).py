from pycoingecko import CoinGeckoAPI
import webbrowser 
import pyperclip
import datetime as dt
cg = CoinGeckoAPI() 

availableCrypto = {
                "bitcoin":"BTC",
                "ethereum":"ETH",
                "litecoin":"LTC",
                "bitcoin-cash":"BCH",
                "binancecoin":"BNB",
                "eos":"EOS",
                "ripple":"XRP",
                "stellar":"XLM",
                "chainlink":"LINK",
                "polkadot":"DOT",
                "yearn-finance":"YFI"
                }

availableCurrencies = {
                "usd":"USD",
                "aed":"AED",
                "ars":"ARS",
                "aud":"AUD",
                "bdt":"BDT",
                "bhd":"BHD",
                "bmd":"BMD",
                "brl":"BRL",
                "cad":"CAD",
                "chf":"CHF",
                "clp":"CLP",
                "cny":"CNY",
                "czk":"CZK",
                "dkk":"DKK",
                "eur":"EUR",
                "gbp":"GBP",
                "hkd":"HKD",
                "huf":"HUF",
                "idr":"IDR",
                "ils":"ILS",
                "inr":"INR",
                "jpy":"JPY",
                "krw":"KRW",
                "kwd":"KWD",
                "lkr":"LKR",
                "mmk":"MMK",
                "mxn":"MXN",
                "myr":"MYR",
                "ngn":"NGN",
                "nok":"NOK",
                "nzd":"NZD",
                "php":"PHP",
                "pkr":"PKR",
                "pln":"PLN",
                "rub":"RUB",
                "sar":"SAR",
                "sek":"SEK",
                "sgd":"SGD",
                "thb":"THB",
                "try":"TRY",
                "twd":"TWD",
                "uah":"UAH",
                "vef":"VEF",
                "vnd":"VND",
                "zar":"ZAR",
                "xdr":"XDR",
                "xag":"XAG",
                "xau":"XAU",
                "bits":"BITS",
                "sats":"SATS"
                }
                       
def getListing():
  out = cg.get_coins_list()
  return out
def findCoin(coin):
  url = 'https://www.coingecko.com/en/coins/' + coin
  webbrowser.open(url, new=2)
  return(url)

def valeurAbs(x):
  if x>=0:
    return(x)
  if x<0:
    return((-1) * x)

def tauxVariation(vA,vD):
  out = ((vA - vD) / valeurAbs(vD))*100
  return out

def lower(s):
  out = s.lower()
  return out

def getInfos(coin,currency):
  coin,currency = lower(coin),lower(currency)
  out = cg.get_price(ids = coin,vs_currencies= currency)
  return(out)

def getPrice(coin,currency):
  coin,currency = lower(coin),lower(currency)
  out = getInfos(coin,currency)
  out = out[coin][currency]
  return out

def priceOutput(coin,currency):
  coin,currency = lower(coin),lower(currency)
  out = getPrice(coin,currency)
  out = str(out)
  out = coin + ' is worth '  + out + availableCurrencies[currency]
  return out

def getCurrentDate():
  date = dt.date.today()
  return date

def currentDateOutput():
  date = dt.date.today()
  date = str(date)
  y,m,d = date[0:4],date[5:7],date[8:10]
  out = d + '-' + m + '-' + y
  return out

def date_nDaysAgo(n):
  now = getCurrentDate()
  evolution = now - dt.timedelta(days=n)
  return evolution

def currentDateOutputForEvolution(n):
  date = date_nDaysAgo(n)
  date = str(date)
  y,m,d = date[0:4],date[5:7],date[8:10]
  out = d + '-' + m + '-' + y
  return out

def historical(coin,currency,date):
  coin,currency = lower(coin),lower(currency)
  if date==currentDateOutput():
    out = getPrice(coin,currency)
  else:
    out = cg.get_coin_history_by_id(coin,date)
    out = out["market_data"]["current_price"][currency]

  return out

#Converts a given amount of crypto to a regular
def cryptoToCurrency(coin,currency):
  coin,currency = lower(coin),lower(currency)
  amount = float(input("what's the amount in CC? : "))
  print()
  n = getPrice(coin,currency)
  out = n * amount
  return out #float

def currencyToCrypto(coin,currency):
  coin,currency = lower(coin),lower(currency)
  amount = float(input("What's the amount in RC ? : "))
  print()
  n = getPrice(coin,currency)
  out = amount / n
  out = round(out, 3)
  return out #float

def cryptoToCurrencyOutput(coin,currency):
  coin,currency = lower(coin),lower(currency)
  amount = float(input("what's the amount in CC? : "))
  print()
  n = getPrice(coin,currency)
  out = n * amount
  out = str(out)
  out = out + suffix
  out = 'coin is worth '  + out
  return out #string

def currencyToCryptoOutput(coin,currency):
  coin,currency = lower(coin),lower(currency)
  amount = float(input('whats the amount in RC, ' + '(' + availableCurrencies[currency] + ') ?: '))
  print()
  n = getPrice(coin,currency)
  out = amount / n
  out = round(out,3)
  out = str(out)
  amount = str(amount)
  out = amount + ' is worth ' + out + ' ' + availableCrypto[coin]
  return out #string

def evolution(coin,currency):
  #Date format : DD-MM-YYYY.
  coin,currency = lower(coin),lower(currency)
  date1 = input('first date to compare ? : ')
  date2 = input('second date to compare ? : ')
  one = historical(coin,currency,date1)
  two = historical(coin,currency,date2)
  out = tauxVariation(two,one)
  out = round(out, 2)
  print(coin,'à evoluer de', out , '%')


funcs = {
        1 : 'getInfos(coin,currency)',
        2 : 'getPrice(coin,currency)',
        3 : 'priceOutput(coin,currency)',
        4 : 'historical(coin,currency,date)',
        5 : 'evolution(coin,currency)',
        6 : 'cryptoToCurrency(coin,currency)',
        7 : 'currencyToCurrency(coin,currency)',
        8 : 'cryptoToCurrencyOutput(coin,currency)',
        9 : 'currencyToCryptoOutput(Coin,Currency)',
        }

def main():
  Coin = input('Coin ?: ')
  print()
  link = findCoin(Coin)
  print(link)
  print()
  #pyperclip.copy(link)
  print('link copied to clipboard !')
  Coin = lower(Coin)
  print()
  Currency = input('Currency ?: ')
  print()
  Currency = lower(Currency)
  print(availableCurrencies[Currency])
  listing = input("do you want to see all the functions available (y/n) ?: ")
  if listing == 'y':
    print()
    print(funcs)
    print()
  else:
    print()
  method = int(input('what function do you want to use ? : '))
  print()

  if method == 1:
    print(getInfos(Coin,Currency))
    print()
  if method == 2:
    print(getPrice(Coin,Currency))
    print()
  if method == 3:
    print(priceOutput(Coin,Currency))
    print()
  if method == 4:
    print()
    date = input('Date ? (format :DD-MM-YYYY) : ')
    print(historical(Coin,Currency,date))
    print()
  if method == 5:
    print(evolution(Coin,Currency))
    print()
  if method == 6:
    print(cryptoToCurrency(Coin,Currency))
    print()
  if method == 7:
    print(currencyToCrypto(Coin,Currency))
    print()
  if method == 8:
    print(cryptoToCurrencyOutput(Coin,Currency))
    print()
  if method == 9:
    print(currencyToCryptoOutput(Coin,Currency))
    print()

main()