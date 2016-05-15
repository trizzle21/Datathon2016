#Prepares data for classification
import datetime
import pandas as pd
import numpy as np




LOG_DATA = "log_data_septermber_1st.csv"
MOBILE_INFO_SEPTEMBER = "mobile_info_all_september.csv"
MOBILE_INFO_SEPT_1ST = "mobile_info_all_sept_1.csv"
LOG_DATA_COL = ["deviceid", "log_timestamp", "data_all"]
MOBILE_INFO_COL = ["device_id", "timestamp", "base_station_id"]
BASE_STATION_PRACTICE = 452
Merged_Group_Col = ["device_id", "data_all", "timestamp", "base_station_id" ]

def parse_date(date_str):
	""""takes in a date_str and returns a 

	arguments: date_str
	outputs: time formated in date_format

	example:
	parse_date("9-1-16 3:10:56", "%b/%d/%Y %H")
	"9/1/16 3:10"
	"""
	newTime = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
	return [newTime.year, newTime.month, newTime.day, newTime.hour, newTime.minute]

def createDate(date_str):
	timeStampArray = parse_date(date_str)
	newstr = ""
	newstr = str(timeStampArray[1]) +'-' + str(timeStampArray[2]) + '-' + str(timeStampArray[0]) + ' ' + str(timeStampArray[3]) + ':' + str(timeStampArray[4])
	return newstr



def filterCellTower(pddp, cell_tower):
	"""Takes a pdDataFrame and filters celltower
		args
			pddataframe
			cell tower string
		outputs new dataframe
	"""
	newlog = pddp[pddp['base_station_id'].isin([452])]
	return newlog

def filterDay(pdFrame, col_name):
	pdFrame = pddataframe[col_name]




def main():
	#read_csv returns a pdDataframe. Whoop de doo
	mobile = pd.read_csv(MOBILE_INFO_SEPT_1ST, usecols=["device_id", "timestamp", "base_station_id"])	
	log = pd.read_csv(LOG_DATA, usecols=["log_timestamp", "device_id", "data_all"])

	#mobile = filterCellTower(mobile, BASE_STATION_PRACTICE)
	#mobile.index = mobile.index.map(createDate)
	mobile = mobile["timestamp"].apply(createDate)
	log = log["log_timestamp"].apply(createDate)
	#log.columns= ["device_id", "timestamp", "data_all"]
	MergedGroup =  pd.merge(log, mobile, how="left",on=['device_id','device_id'])
	MergedGroup.groupby('timestamp')
	return MergedGroup


print main()



