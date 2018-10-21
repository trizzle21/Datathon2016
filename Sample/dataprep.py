""" Prepares data for classification

    Move into 
"""
import sys
import os
from datetime import datetime
#import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import lagrange as lg
from .. import settings

#from sklearn.decomposition import PCA

DIR_NAME = settings.BASE_DIR



LOG_DATA = os.path.join(DIR_NAME, 'Data', "log_data_september_1st" + ".csv")
MOBILE_INFO_SEPT_1ST = os.path.join(DIR_NAME, 'Data', "mobile_info_all_sept_1" + ".csv")


LOG_DATA_COL = ["deviceid", "log_timestamp", "data_all"]
MOBILE_INFO_COL = ["device_id", "timestamp", "base_station_id"]

#in case one wasn't selected. returns
try:
    BASE_STATION_PRACTICE = sys.argv[1]
except:
    BASE_STATION_PRACTICE = 452

MERGED_GROUP_COL = ["device_id", "data_all", "timestamp", "base_station_id"]

def parse_date(date_str):
    """takes in a date_str and returns a string

	arguments: date_str
	outputs: time formated in date_format

	example:
	parse_date("9-1-16 3:10:56", "%b/%d/%Y %H")
	9/1/16 3:10"
	"""
    new_time = datetime.strptime(date_str, "%m/%d/%Y %H:%M")
    return new_time.strftime("%y-%m-%d %H:%M")


	#[newTime.year, newTime.month, newTime.day, newTime.hour, newTime.minute]
	#%Y-%m-%d %H:%M:%S


def create_date(date_str):
    """ Re"""
    time_stamp_array = parse_date(date_str)
    newstr = ""
    newstr = str(time_stamp_array[1]) +'-' + str(time_stamp_array[2]) + '-' \
    + str(time_stamp_array[0]) + ' ' + str(time_stamp_array[3]) + ':' + str(time_stamp_array[4])
    return newstr



def date_filter(date_str):
    """ TODO """
    return date_str

def filter_cell_tower(pddp, cell_tower):
    """Takes a pdDataFrame and filters celltower
		args
			pddataframe
			cell tower string
		outputs new dataframe
	"""
    newlog = pddp[pddp['base_station_id'].isin([BASE_STATION_PRACTICE])]
    return newlog


def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')

# def project_data(data: 'DataFrame', dims: int) -> '[matrix, matrix]':
#     """
#     :param data: The data as a DataFrame object, assuming from pandas.
#     :param dims: The preferred number of dimensions to project the data onto - the minimum and ideal k, to project onto R^k.
#     :return: An array [result, precision], result being the output data,
#         precision being a single element array with value [0,1], 1 meaning all the variance was accounted for (good).
#     """
#     pca = PCA(n_components=dims)
#     pca.fit(data)
#     return [pca.components_, pca.explained_variance_ratio_]

def main():
	#read_csv returns a pdDataframe.
    mobile = pd.read_csv(MOBILE_INFO_SEPT_1ST, usecols=["device_id", "base_station_id"])
    log = pd.read_csv(LOG_DATA, usecols=["log_timestamp", "device_id", "data_all"])
    mobile = mobile[mobile['base_station_id'].notnull()]
    mobile = filterCellTower(mobile, BASE_STATION_PRACTICE)

	#Filter the data
	#mobile.index = mobile.index.map(createDate)
	#mobile["timestamp"] = mobile["timestamp"].apply(dateFilter)
	#log["log_timestamp"] = log["log_timestamp"].apply(dateFilter)
	#log.columns= ["device_id", "timestamp", "data_all"]
    MergedGroup = pd.merge(log, mobile, how="left", on=['device_id','device_id'])
    MergedGroup = MergedGroup[MergedGroup['base_station_id'].notnull()]

	#Set to index by timestamp, then group by the hour and sum data_all.
    MergedGroup['log_timestamp'] = pd.to_datetime(MergedGroup['log_timestamp'])
    MergedGroup = MergedGroup.set_index('log_timestamp')
    return [np.unique(MergedGroup.index.map(lambda t: t.hour)), MergedGroup['data_all'].groupby(MergedGroup.index.map(lambda t: t.hour)).sum().values]



def lagrange(xdata, ydata):
    """ Generates a list of lagrange (x,y) endpoints"""
    l = []
    for i in range(0, 24):
        l.append(lg.lagrange_generator(xdata, ydata, i))

    return l




data = main()


def secondary():
    """
	The Point of this is to

	"""

    v = [5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 23]
    xhat = [i for i in range(7, 24)]
	#This data
    prelg = [8901482, 898952, 1107098, 554078, 365004, 427394, 406668,
             525004, 477256, 571558, 1107482, 909442, 784612, 696754,
             3112642, 3258892]
    yhat = []

    for r in xhat:
        yhat.append(lg.lagrange_generator(v, prelg, r))

    return [np.array(xhat), np.array(yhat)]



data2 = secondary()











plt.grid(True)
plt.title('Data usage over September 1st')
plt.xlabel('Time (hrs)')
plt.ylabel('Summed data usage (bytes)')
#plt.plot(data[0],data[1], '-')
plt.plot(data2[0], data2[1], data[0], data[1], linewidth=2.0)

plt.show()
#print_full(main())


#print_full(main())

main()



#plt.axes = data['data_all'].plot(kind='line')
plt.show()


#os.system("prediction.py")
