#Prepares data for classification
import datetime as dt
import pandas as pd
import numpy as np




LOG_DATA = "log_data_septermber_1st.csv"
MOBILE_INFO_SEPTEMBER = "mobile_info_all_september.csv"

LOG_DATA_COL = ["deviceid", "log_timestamp", "data_all"]
MOBILE_INFO_COL = ["device_id", "timestamp", "base_station_id"]
BASE_STATION_PRACTICE = 452
Merged_Group_Col = ["device_id", "data_all", "timestamp", "base_station_id" ]

def parse_date(date_str):
	""""takes in a date_str and returns a 

	arguments: date_str
	outputs: time formated in date_format

	example:
	parse_date("9/1/16 3:10:56", "%b/%d/%Y %H")
	"9/1/16 3:10"
	"""
	newTime = dt.dt.strptime(datetime, "%Y-%m-%d %H:%M:%S")
	return [newTime.year, newTime.month, newTime.day, newTime.hour]

def createDate(date_str):
	timeStampArray = parse_date(date_str)
	newstr =""
	for i in timeStampArray:
		newstr = newstr + " " + str(i)
	return newstr



def filterCellTower(pdDataFrame, cell_tower):
	"""Takes a pdDataFrame and filters celltower
		args
			pddataframe
			cell tower string
		outputs new dataframe
	"""
	newpdDataFrame = pddataframe[pdDataframe['base_station_id'].isin([cell_tower_string])]
	return newpdDataFrame





def main():
	#read_csv returns a pdDataframe. Whoop de doo
	mobile = pd.read_csv(MOBILE_INFO_SEPTEMBER, index_col=0, usecols=["device_id", "timestamp", "base_station_id"])
	log = pd.read_csv(LOG_DATA,index_col=0, usecols=["device_id", "log_timestamp", "data_all"])
	mobile = filterCellTower(Log, BASE_STATION_PRACTICE)
	mobile = mobile["timestamp"].apply(createDate)
	log = log["log_timestamp"].apply(createDate)
	MergedGroup = mobile.join(log, on = 'log_timestamp')

	MergedGroup.groupby('timestamp').sum()

	return MergedGroup


main()


