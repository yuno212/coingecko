# Crypto scraping tool

### For given data returns relevant information, (Using coingecko's wrapper)

# Requirements : 

```python
pip install pycoingecko
from pycoingecko import CoinGeckoAPI
import webbrowser
import datetime as dt
```
# Features / Perks :

### -  Useful.
### -  Could be used for data science / analysis purposes.
### -  Beginner friendly (understandable code).
### -  Clean UI.
### -  Could be improved by deploying a web app.
### -  All variables type explained.
### -  Video tutorial to see how to use the program (Link : Comming soon...).

# Infos / Input types / Functions : 

### -  ***coin*** is a string (example : 'Bitcoin').
### -  ***currency*** is a string (example : 'USD').
### -  ***date*** is a string (Date format : DD-MM-YYYY) , (example : "03-05-2021").
### -  *When running the code program will ask you what function you'll use , please refer to the numbers in front of the functions name below, if you have any issues using program consider contacting me on my discord in the contact section*

##   Usable functions : 
###  **1) getInfos(coin,currency) | returns raw partial information about a given crypto, output type dict** 
###  **2) getPrice(coin,currency) | returns coin price given coin and currency, output type float**        
###  **3) priceOutput(coin,currency) | returns a more clean output still about the price of a given coin, output type string**     
###  **4) historical(coin,currency,date) | returns the price of a given coin with given currency where date has to be inputted, output type float**
###  **5) evolution(coin,currency) | returns the rate of change of given crypto between two dates, also asking for dict where output is summed up in a dict, output type string** 
###  **6) cryptoToCurrency(coin,currency) | returns amount of currency related to given crypto, output type float**  
###  **7) currencyToCurrency(coin,currency) | returns amount of crypto related to given currency, output type float**
###  **8) cryptoToCurrencyOutput(coin,currency) | returns amount of currency related to given crypto, output type string**
###  **9) currencyToCryptoOutput(coin,currency) | returns amount of crypto related to given currency, output type string**
###  **10) getSymbol(coin) | returns the symbol of a given crypto** 
###  **11) cryptoConverter() | returns the equivalent of two asked crypto's**
###  **12) getProjectDescription(coin) | returns a partial project description of a given coin**


### -**historical** and **evolution** functions **aren't working** for a **1 month old** date example (assuming we're the **19-10-2021**) you can't get the price of the (**20-09-2021**)

### - To get a specific coin id please consider searching your coin on https://www.coingecko.com/en , and copy the circled content who's basically getting the id of the coin
![InkedpageWhenRedirected_LI](https://user-images.githubusercontent.com/91159949/138499503-d716f371-fc0a-40df-95f2-5fdd7971ac73.jpg)


# Contact : 

### discord : **yuno#0283** .
### Request new features or ask for collaboration.
