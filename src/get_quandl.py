import quandl
import pandas as pd
import numpy as np

quandl.ApiConfig.api_key="_Hi22UWDBu6vwiBhsLpS"


def get_quandl_futures_ticker(root,start_year,end_year)
	month_code = ['F','G','H','J','K','M','N','Q','U','V','X','Z']
	futures_ticker_list = []
	for year in range(start_year,end_year):
		for month in month_code:
			futures_ticker_list.append(root+month+str(year))
	return(futures_ticker_list)

def get_data_quandl(tickers):
	data_list = []
	for ticker in tickers:
		data = quandl.get(ticker)
		data['ticker'] = ticker
		data_list.append(data)
	all_data = pd.concat(data_list)
	return(all_data)
		