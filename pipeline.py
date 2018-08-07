#create functions that make different api calls and return the data as an object
#this will make it easier to reference when the function is called
#eg
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