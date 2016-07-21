#takes in pd.dataframe and builds a frequency of the data
import datetime as dt
import panda as pd
import numpy as np


def frequency_calc(pdDataframe, dictionary):
	"""Builds frequency based on a data frame formatted as the following
	Cols: "timestamp", "device_id", "base_station_id" "device_id", "data_all"
	
	Probably write this recursively

	Input pdDataframe

	Returns dictionary with data mapped to frequency
	"""
	freq_dict= dict()
	for index, device_id, data_all in df.iterrows():
		try freq_dict[data_all]:
			freq_dict[data_all] = freq_dict[data_all] + 1
		except:
			freq_dict[data_all] = 1
	return freq_dict

def totalCalc(freq_dict)
	#takes in a frequency dictionary and returns the total number of frequency
	total = 0
	for key in freq_dict:
		total += freq_dict[key]
	return total 


def probability_calc(freq_dict):
	"""
		Arguments: freq dictionary
		returns a list of probabilities for time t_0 to t_n-1

	"""
	prob_list = []
	totalValue = totalCalc(freq_dict) 
	for key in freq_dict:
		prob_list.append(freq_dict[key]/totalValue)
	return prob_list
