#create functions that make different api calls and return the data as an object
#this will make it easier to reference when the function is called
#eg
#
#


import requests
import json
import random

#this function returns the details about the companies listed on the site
def get_company_info():
    url = 'https://api.iextrading.com/1.0/ref-data/symbols'
    r = requests.get(url)
    data = r.json()
    json_data_parsed = json.dumps(data, indent=2)
    json_data = json.loads(json_data_parsed)

    #generating the random stock symbols
    aux = json_data
    random.shuffle(aux)
    listed_companies_data = json.dumps(aux[0:10], indent=2)
    listed_companies_details = json.loads(listed_companies_data)
    company_info_list = []
    for i in listed_companies_details:
        company_symbol = i['symbol']
        url = 'https://ws-api.iextrading.com/1.0/stock/{symbol}/company'.format(symbol=company_symbol)
        url2 = 'https://api.iextrading.com/1.0/stock/{symbol}/chart'.format(symbol=company_symbol)
        r = requests.get(url)
        r2 = requests.get(url2)
        company_info = json.dumps(r.json())
        company_chart = json.dumps(r2.json())
        json_object = json.loads(company_info)
        json_object_chart = json.loads(company_chart)
        items = {
                'symbol': json_object['symbol'],
                'company_name': json_object['companyName'],
                'industry': json_object['industry'],
                'website': json_object['website'],
                'sector': json_object['sector'],
                'exchange': json_object['exchange'],
                'close': json_object_chart[-1]['close'],
                'change': json_object_chart[-1]['change'],
                'change_percentage': json_object_chart[-1]['changePercent']
            }
        company_info_list.append(items)
    return(company_info_list)

#this function returns the top 5 gainers
def get_top_gainsers():
    url = 'https://api.iextrading.com/1.0/stock/market/list/gainers'
    r = requests.get(url)
    data = r.json()
    json_data_parsed = json.dumps(data, indent=2)
    json_data = json.loads(json_data_parsed)
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
    url = 'https://api.iextrading.com/1.0/stock/market/list/losers'
    r = requests.get(url)
    data = r.json()
    json_data_parsed = json.dumps(data, indent=2)
    json_data = json.loads(json_data_parsed)
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
    url = 'https://api.iextrading.com/1.0/stock/market/list/mostactive'
    r = requests.get(url)
    data = r.json()
    json_data_parsed = json.dumps(data, indent=2)
    json_data = json.loads(json_data_parsed)
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

#def get_news():
#    symbols = get_company_info()
#    news_articles_list = []
#    for i in symbols:
#        symbol = i['symbol']
#        print(symbol)
#        url = 'https://api.iextrading.com/1.0/stock/{symbol}/news/last/2'.format(symbol=symbol)
#        r = requests.get(url)
#        data = r.json()
#        json_data_parsed = json.dumps(data, indent=2)
#        json_data = json.loads(json_data_parsed)
#        
#        for d in json_data:
#            items = {
#                'datetime': d['datetime'],
#                'headline': d['headline'],
#                'source': d['source'],
#                'url': d['url'],
#                'summary': d['summary'],
#                'image': d['image']
#            }
#            news_articles_list.append(items)
#    
#    return(news_articles_list)