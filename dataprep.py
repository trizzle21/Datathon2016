#Prepares data for classification
import datetime
import pandas as pd
import numpy as np

LOG_DATA = "log_data_2015_09_01.csv"
MOBILE_INFO_SEPTEMBER = "mobile_info_all_sept_1.csv"

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
	newTime = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
	return [newTime.year, newTime.month, newTime.day, newTime.hour]

def createDate(date_str):
	timeStampArray = parse_date(date_str)
	newstr =""
	for i in timeStampArray:
		newstr = newstr + " " + str(i)
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

def main():
	#read_csv returns a pdDataframe. Whoop de doo
	mobile = pd.read_csv(MOBILE_INFO_SEPTEMBER, usecols=["device_id", "base_station_id"])
	log = pd.read_csv(LOG_DATA, usecols= ["log_timestamp", "device_id", "data_all"])
	mobile = filterCellTower(mobile, BASE_STATION_PRACTICE)
	MergedGroup = pd.merge(mobile,log,how="left",on=["device_id","device_id"])

	return MergedGroup


