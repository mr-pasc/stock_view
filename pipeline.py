#create functions that make different api calls and return the data as an object
#this will make it easier to reference when the function is called


import requests
import json
import random

#takes an argument end_url passed in by the function that calls it and returns a json object
def api_call(url_end):
    url = 'https://api.iextrading.com/1.0/{url_end}'.format(url_end=url_end)
    r = requests.get(url)
    data = r.json()
    json_data_parsed = json.dumps(data, indent=2)
    json_data = json.loads(json_data_parsed)
    return(json_data)

def get_symbols_list():
    url_end = 'ref-data/symbols'
    json_data = api_call(url_end)

    #generating the random stock symbols
    aux = json_data
    random.shuffle(aux)
    listed_companies_data = json.dumps(aux[0:10], indent=2)
    listed_companies_details = json.loads(listed_companies_data)
    company_symbols_list = []
    for symbols in listed_companies_details:
        s = symbols['symbol']
        company_symbols_list.append(s)
    return(company_symbols_list)
    #returns ['AAPL', 'ASRE', 'ERC', 'GTSS', 'TDSF', 'SBERF']

def company_info(symbol):
    url_end = 'stock/{symbol}/company'.format(symbol=symbol)
    json_object = api_call(url_end)
    item = {
            'symbol': json_object['symbol'],
            'company_name': json_object['companyName'],
            'industry': json_object['industry'],
            'website': json_object['website'],
            'sector': json_object['sector'],
            'exchange': json_object['exchange'],
            
        }
    return(item)
#returns 
#
#{
#   "symbol": "AAPL",
#   "companyName": "Apple Inc.",
#   "exchange": "Nasdaq Global Select",
#   "industry": "Computer Hardware",
#   "website": "http://www.apple.com",
#   "sector": "Technology",
#}





def company_chart(symbol):
    url_end = 'stock/{symbol}/chart'.format(symbol=symbol)
    json_object_chart = api_call(url_end)
    item = {
        'close': json_object_chart[-1]['close'],
        'change': json_object_chart[-1]['change'],
        'change_percentage': json_object_chart[-1]['changePercent'],
    }
    return(item)

#returns
#{
#   "close": 217.58,   
#   "change": 4.26,
#   "changePercent": 1.997,
#}


def company_news(symbol):
    url_end = 'stock/{symbol}/news/last/3'.format(symbol=symbol)
    json_object_news = api_call(url_end)
    news_list = []
    for d in json_object_news:
        item = {
            'datetime': d['datetime'],
            'headline': d['headline'],
            'source': d['source'],
            'url': d['url'],
            'summary': d['summary'],
        }
        news_list.append(item)
    return(news_list)
#returns

#{
#   "datetime": "2018-08-20T15:59:00-04:00",
#   "headline": "Trump says it's 'very dangerous' when Twitter, Facebook self-regulate content",
#   "source": "CNBC",
#   "url": "https://api.iextrading.com/1.0/stock/aapl/article/6385698940042211",
#   "summary": "No summary available.",
#   "related": "AAPL,FB,TWTR",
#   "image": "https://api.iextrading.com/1.0/stock/aapl/news-image/6385698940042211"   - this will be implemented soon
#},


def stock_object_list():
    stocks = []
    for symbol in get_symbols_list():
        stock = {
            'company_info' : company_info(symbol),
            'company_chart' : company_chart(symbol),
            'company_news' : company_news(symbol)
        }
        stocks.append(stock)
    return(stocks)

#returns

#stocks = [
#       {
#           'company_info': {
#                   "symbol": "AAPL",
#                   "companyName": "Apple Inc.",
#                   "exchange": "Nasdaq Global Select",
#                   "industry": "Computer Hardware",
#                   "website": "http://www.apple.com",
#                   "sector": "Technology",
#               },
#           'company_chart': {
#                   "close": 217.58,   
#                   "change": 4.26,
#                   "changePercent": 1.997,
#               },
#           'company_news': {
#                   "datetime": "2018-08-20T15:59:00-04:00",
#                   "headline": "Trump says it's 'very dangerous' when Twitter, Facebook self-regulate content",
#                   "source": "CNBC",
#                   "url": "https://api.iextrading.com/1.0/stock/aapl/article/6385698940042211",
#                   "summary": "No summary available.",
#                   "related": "AAPL,FB,TWTR",
#                   "image": "https://api.iextrading.com/1.0/stock/aapl/news-image/6385698940042211"
#               }
#       },
# 
# ]


#this function returns the top 5 gainers
def get_top_gainsers():
    url_end = 'stock/market/list/gainers'
    json_data = api_call(url_end)
    top_gainers_list = []
    for items in json_data[0:5]:
        items = {
            'symbol': items['symbol'],
            'company_name': items['companyName'],
            'close': items['close'],
            'change': items['change'],
            'change_percentage': items['changePercent'],
            'sector': items['sector'],
            'exchange': items['primaryExchange']       
        }
        top_gainers_list.append(items)
    return(top_gainers_list)

#this function will return the top 5 losers
def get_top_losers():
    url_end = 'stock/market/list/losers'
    json_data = api_call(url_end)
    top_losers_list = []
    for items in json_data[0:5]:
        items = {
            'symbol': items['symbol'],
            'company_name': items['companyName'],
            'close': items['close'],
            'change': items['change'],
            'change_percentage': items['changePercent'],
            'sector': items['sector'],
            'exchange': items['primaryExchange']
        }
        top_losers_list.append(items)
    return(top_losers_list)

def get_most_active():
    url_end = 'stock/market/list/mostactive'
    json_data = api_call(url_end)
    mostactive_list = []
    for items in json_data[0:5]:
        items = {
            'symbol': items['symbol'],
            'company_name': items['companyName'],
            'close': items['close'],
            'change': items['change'],
            'change_percentage': items['changePercent'],
            'sector': items['sector'],
            'exchange': items['primaryExchange']
        }
        mostactive_list.append(items)
    return(mostactive_list)
