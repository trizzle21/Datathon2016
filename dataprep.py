#Prepares data for classification
import datetime
import pandas as pd
import numpy as np




LOG_DATA = "log_data_2015_09_01.csv"
MOBILE_INFO_SEPT_1ST = "mobile_info_2015_09_01.csv"


LOG_DATA_COL = ["deviceid", "log_timestamp", "data_all"]
MOBILE_INFO_COL = ["device_id", "timestamp", "base_station_id"]


BASE_STATION_PRACTICE = 8759.0
Merged_Group_Col = ["device_id", "data_all", "timestamp", "base_station_id" ]

def parse_date(date_str):
	""""takes in a date_str and returns a 

	arguments: date_str
	outputs: time formated in date_format

	example:
	parse_date("9-1-16 3:10:56", "%b/%d/%Y %H")
	"9/1/16 3:10"
	"""
	newTime = datetime.datetime.strptime(date_str, "%m/%d/%Y %H:%M")
	return newTime.strftime("%y-%m-%d %H:%M")


	#[newTime.year, newTime.month, newTime.day, newTime.hour, newTime.minute]
	#%Y-%m-%d %H:%M:%S


def createDate(date_str):
	timeStampArray = parse_date(date_str)
	newstr = ""
	newstr = str(timeStampArray[1]) +'-' + str(timeStampArray[2]) + '-' + str(timeStampArray[0]) + ' ' + str(timeStampArray[3]) + ':' + str(timeStampArray[4])
	return newstr



def dateFilter(date_str):
	return date_str

def filterCellTower(pddp, cell_tower):
	"""Takes a pdDataFrame and filters celltower
		args
			pddataframe
			cell tower string
		outputs new dataframe
	"""
	newlog = pddp[pddp['base_station_id'].isin([8759.0])]
	return newlog


def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')


def main():
	#read_csv returns a pdDataframe. Whoop de doo
	mobile = pd.read_csv(MOBILE_INFO_SEPT_1ST, usecols=["device_id", "base_station_id"])	
	log = pd.read_csv(LOG_DATA, usecols=["log_timestamp", "device_id", "data_all"])
	mobile = mobile[mobile['base_station_id'].notnull()]
	mobile = filterCellTower(mobile, BASE_STATION_PRACTICE)
	
	#mobile.index = mobile.index.map(createDate)
	#mobile["timestamp"] = mobile["timestamp"].apply(dateFilter)
	#log["log_timestamp"] = log["log_timestamp"].apply(dateFilter)
	#log.columns= ["device_id", "timestamp", "data_all"]
	MergedGroup =  pd.merge(log, mobile, how="left", on=['device_id','device_id'])
	MergedGroup = MergedGroup[MergedGroup['base_station_id'].notnull()]
	#MergedGroup.groupby('device_id')
	return MergedGroup



print main()
#print_full(main())






