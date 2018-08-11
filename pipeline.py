#create functions that make different api calls and return the data as an object
#this will make it easier to reference when the function is called
#eg
#
#
#def company_info(symbol, data):
#   url = 'https://ws-api.iextrading.com/1.0/stock/{symbol}/company' ---->synbol is passed in as an argument when function is called
#   r = requests.get(url)
#   data = r.json()
#   json_data_parsed = json.dumps(data, indent=2)
#   json_data = json.loads(json_data_parsed)
#   
#   create object with the info required
#   return that object.data                  #will look like json_data.symbol ----> this should return AAPL  |  data is passed in when the function is called
#
#
# when the function is called it will look like:
#   import pipeline as PL
#   
#   symbol = AAPL #company symbol
#   data = symbol #data to be requested
#   PL.company_info(symbol, data) -----> should return AAPL
#   PL.company_info(AAPL, sector) -----> should return Technology
#
#


import requests
import json
import random


def get_listed_companies():
    url = 'https://api.iextrading.com/1.0/ref-data/symbols'
    r = requests.get(url)
    data = r.json()
    json_data_parsed = json.dumps(data, indent=2)
    json_data = json.loads(json_data_parsed)

    #generating the random stocks
    aux = json_data
    random.shuffle(aux)
    data_json_format = json.dumps(aux[0:10], indent=2)
    print(data_json_format)


def current_price(symbol):
    url = 'https://ws-api.iextrading.com/1.0/stock/{symbol}/price'.format(symbol=symbol)
    r = requests.get(url)
    json_data = json.dumps(r.json())
    return(json_data)
