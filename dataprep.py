#Prepares data for classification
import datetime as dt
import panda as pd
import numpy as np


DATE_FORMAT = "%b/%d/%Y %H"

LOG_DATA = "log_data_september.csv"
MOBILE_INFO_SEPTEMBER = "mobile_info_all_septermber_1st.csv"
LOG_DATA_COL= ["deviceid", "log_timestamp", "data_all"]
MOBILE_INFO_COL= ["device_id", "timestamp", "base_station_id"]

def convert_date(date_str, date_format):
	""""takes in a date_str and returns a 

	arguments: date_str
	outputs: time formated in date_format

	example:
	parse_date("9/1/16 3:10:56", "%b/%d/%Y %H")
	"9/1/16 3:10"



	"""
	newTime = dt.striptime(datetime, date_format)
	return newTime.toString()




def convertingDates(pdDataframe, colName):
	""" Takes in a data frame and applies 
	Args:
	pdDateframe: PandaData_frame
	colName: Will include the name of the time stamp column

	Returns
	newpdDataFrame with converted date column
	"""



def main():
	#read_csv returns a pdDataframe. Whoop de doo
	Log = pd.read_csv(LOG_DATA, LOG_DATA_COL)
	Mobile = pd.read_csv(MOBILE_INFO_SEPTEMBER, MOBILE_INFO_COL)
