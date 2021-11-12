from pycoingecko import *
import webbrowser
import datetime as dt
import sys


cg = CoinGeckoAPI()

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

possibleYes = ['Y','y','yes','Yes','YES']
possibleNo = ['N','n','No','NO','no']

def findCoin(coin):
  url = 'https://www.coingecko.com/en/coins/' + coin
  webbrowser.open(url, new=2)
  out = 'Done' +'Redirected on ' + url
  return(out)

def absVal(x):
    if x>=0:
        return(x)
    if x<0:
        return((-1) * x)

def rateOfChange(vA,vD):
    out = ((vA - vD) / absVal(vD))*100
    return out

def lower(s):
    out = s.lower()
    return out

def Upper(s):
    out = s.upper()
    return out

def getSymbol(coin):
    coin = lower(coin)
    listing = cg.get_coins_list()
    for i in listing:
        find = i
        if find['id'] == coin:
            out = find['symbol']
            return(Upper(out))

    return('Coin not found')

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

def getProjectDescription(coin):
  coin = lower(coin)
  out = cg.get_coin_by_id(coin)
  out = out['description']['en']
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
    if date == currentDateOutput():
        out = getPrice(coin,currency)
    else:
        out = cg.get_coin_history_by_id(coin,date)
        out = out["market_data"]["current_price"][currency]

    return out

def cryptoToCurrency(coin,currency,amount): #amount is crypto (5BTC)
    coin,currency = lower(coin),lower(currency)
    amount = int(input(f'amount of {coin} : '))
    print()
    n = getPrice(coin,currency)
    out = n * amount
    return round(out,2)

def currencyToCrypto(coin,currency,amount): #Amount is currency (ex : yes1000 USD)
    coin,currency = lower(coin),lower(currency)
    print()
    n = getPrice(coin,currency)
    out = amount / n
    out = round(out, 3)
    return out #float

def funcListing():
    githubLink = 'https://github.com/yun0dev/coingecko'
    webbrowser.open(githubLink,new = 2)
    return githubLink

def cryptoToCurrencyOutput(coin,currency):
    coin,currency = lower(coin),lower(currency)
    amount = float(input("Amount in" + getSymbol(coin)))
    print()
    n = getPrice(coin,currency)
    out = n * amount
    out = round(out,3)
    out = str(out)
    amount = str(amount)
    out = amount  + ' ' + getSymbol(coin) + ' is worth ' + out + availableCurrencies[currency]
    return out

def currencyToCryptoOutput(coin,currency):  #
    coin,currency = lower(coin),lower(currency)
    amount = float(input('whats the amount in RC, ' + '(' + availableCurrencies[currency] + ') ?: '))
    print()
    n = getPrice(coin,currency)
    out = amount / n
    out = round(out,3)
    out = str(out)
    amount = str(amount)
    out = amount + ' is worth ' + out + ' ' + getSymbol(coin)
    return out

def evolution(coin,currency):
    #Date format : DD-MM-YYYY.
    #Input must be valid.
    coin,currency = lower(coin),lower(currency)
    date1 = input('first date to compare ? : ')
    print()
    date2 = input('second date to compare ? : ')
    one = historical(coin,currency,date1)
    two = historical(coin,currency,date2)
    one,two = round(one,2),round(two,2)
    out = rateOfChange(two,one)
    out = round(out, 2)
    ev = ''
    if out>0:
        ev +='increased by :'
        evo = 'Increase'
    elif out<0:
        ev += 'decreased by :'
        out = (-1) * out
        evo = 'Decrease'

    print()
    print(coin+' '+ev , out , '%')
    print()
    listOrNot = input('Want a dictionary where output is summed up ?: ')

    if listOrNot in possibleYes:
      sumUp = {
        'first price the : ' + date1: str(one) + availableCurrencies[currency],
                'second price the : '+ date2: str(two) +
                availableCurrencies[currency] ,
                'evolution' : str(out) +' %',
                'type of evolution' : evo
                }
      print()
      return sumUp

    elif listOrNot in possibleNo:
      return()

def cryptoConverter():
    defCurrency = 'usd'
    coinName1 = lower(input('1st coin: '))
    coinName2 = lower(input('2nd coin: '))
    try:
        coin1 = getPrice(coinName1,defCurrency)
        amount1 = int(input('Amount of ' + getSymbol(coinName1) + ' : '))
        coin1 *= amount1
        coin2 = currencyToCrypto(coinName2,defCurrency,coin1)
        coin2 = round(coin2,3)
        out = str(amount1)+ ' ' + getSymbol(coinName1) + ' is worth ' + str(coin2) + ' ' +getSymbol(coinName2)
        return(out)
    except KeyError:
         print('No such coin as inputted')


def main():
  while True:
    listing = input('Want a listing of the available functions ? : ')
    if listing in possibleYes:
      print(funcListing())
    elif listing in possibleNo:
      print()
    method = int(input('What function you wanna use? : ')) #int between 1 and 10 inclusive

    if method == 1:
      Coin = input('Coin : ')
      Currency = input('Currency : ')
      try:
        getPrice(Coin,Currency)
        print(getInfos(Coin,Currency))
      except KeyError:
        print('Coin or currency not found or supported')


    if method == 2:
      Coin = input('Coin : ')
      Currency = input('Currency : ')
      try:
        getPrice(Coin,Currency)
        print(getPrice(Coin,Currency))
      except KeyError:
        print('Coin or currency not found or supported')


    if method ==3:
      Coin = input('Coin : ')
      Currency = input('Currency : ')
      try:
        getPrice(Coin,Currency)
        print(priceOutput(Coin,Currency))
      except KeyError:
        print('Coin or currency not found or supported')


    if method == 4:
      Coin = input('Coin : ')
      Currency = input('Currency : ')
      #Should be a valid date
      Date = input('Date (format : DD-MM-YYYY ) : ')
      try:
        getPrice(Coin,Currency)
        print(historical(Coin,Currency,Date))
      except KeyError:
        print('Coin or currency not found or supported')


    if method == 5:
      Coin = input('Coin : ')
      Currency = input('Currency : ')
      try:
        getPrice(Coin,Currency)
        print(evolution(Coin,Currency,Date))
      except KeyError:
        print('Coin or currency not found or supported')


    if method == 6:
      Coin = input('Coin : ')
      Currency = input('Currency : ')
      try:
        getPrice(Coin,Currency)
        print(cryptoToCurrency(Coin,Currency,amount))
      except KeyError:
        print('Coin or currency not found or supported')


    if method == 7:
      Coin = input('Coin : ')
      Currency = input('Currency : ')
      Amount = int(input(f'amount of {currency} : '))
      try:
        getPrice(Coin,Currency)
        print(currencyToCrypto(Coin,Currency,Amount))
      except KeyError:
        print('Coin or currency not found or supported')


    if method == 8:
      Coin = input('Coin : ')
      Currency = input('Currency : ')
      try:
        getPrice(Coin,Currency)
        print(cryptoToCurrencyOutput(Coin,Currency))
      except KeyError:
        print('Coin or currency not found or supported')

    if method == 9:
      Coin = input('Coin : ')
      Currency = input('Currency : ')
      try:
        getPrice(Coin,Currency)
        print(currencyToCryptoOutput(Coin,Currency))
      except KeyError:
        print('Coin or currency not found or supported')


    if method == 10:
      Coin = input('Coin : ')
      try:
        getPrice(Coin,Currency)
        print(getSymbol(Coin))
      except KeyError:
        print('Coin or currency not found or supported')

    if method == 11:
      print(cryptoConverter())

    if method == 12:
      Coin = input('Coin : ')
      default = 'usd'
      try:
        getPrice(Coin,default)
        print(getProjectDescription(Coin))
      except KeyError:
        print('No coin')

    if method == 13:
      Coin  = input('Coin : ')
      default = 'usd'
      try:
        getPrice(Coin,default)
        print(findCoin(Coin))
      except KeyError:
        print('Coin or currency not found or supported')

    try:
      redirect = input(f"Wanna go into coingecko's {Coin} page ? :")
      if redirect in possibleYes:
        print(findCoin(Coin))
      elif redirect in possibleNo:
        print()
    except:
      print("You didn't put a coin ...")

    break

main()
