import requests
import pandas as pd

#####################################################################
# Populate BTC prices in different fiat currencies
#####################################################################
# List of fiat currencies we want to query
# You can expand this list, but CryptoCompare does not have
# a comprehensive fiat list on their site
fiatList = ['AUD', 'CAD', 'CNY', 'EUR', 'GBP', 'GOLD', 'HKD',
'ILS', 'INR', 'JPY', 'KRW', 'PLN', 'RUB', 'SGD', 'UAH', 'USD', 'ZAR']


def get_crypto_data(df):
    df = pd.DataFrame()
    for fiat in fiatList:
    # get data for bitcoin price in that fiat
        URL = 'https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym='+fiat+'&allData=true' 
        res = requests.get(URL)
        res_json = res.json()
        data= res_json['Data']
        temp_df= pd.DataFrame(data)
        temp_df['conversionSymbol']= fiat
        df = df.append(temp_df, ignore_index=True)
        #df['time'] = pd.to_datetime(df['time'],unit='s')
    return df        


# this defines the columns and data types going back out to Prep
def get_output_schema():
    print('Getting output schema...\n')
    return pd.DataFrame({
        'time' : prep_int(),
        'high' : prep_decimal(),
        'low' : prep_decimal(),
        'open' : prep_decimal(),
        'volumefrom' : prep_decimal(),
        'volumeto' : prep_decimal(),
        'close' : prep_decimal(),
        'conversionType' : prep_string(),
        'conversionSymbol' : prep_string(),
        })




