import pandas as pd
import numpy as np

def maxDrawDown(perf):
	# TO DO
	return(0)

def sharpRatio(perf,n):
    return(np.nanmean(perf)/np.nanstd(perf)*(n ** 0.5))

def summaryPerformance(perf,n):
    avg_return = np.nanmean(perf)
    sharp = sharpRatio(perf,n)
	max_drawdown = maxDrawDown(perf)
    return(avg_return,sharp,max_drawdown)

def appendPerfVol(sd_data):
    sd_data['prev_close'] = sd_data.groupby(['ticker'])['close'].shift(1)
    sd_data['past_perf_1d'] = (sd_data['close']/sd_data['prev_close'])-1
    sd_data['future_perf_1d'] = sd_data.groupby(['ticker'])['past_perf_1d'].shift(-1)
    sd_data['volatility'] = sd_data.groupby(['ticker'])['past_perf_1d'].rolling(30).std().values * (252 ** 0.5)
    return(sd_data)
