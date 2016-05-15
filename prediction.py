#Predictive Markov models
#Backwards Forwards is really hard exhauasted
from pykalman import KalmanFilter



import panda as pd
import numpy as np
from dataprep import REVELANT_DATA #file with important data

PREDICTION_LIST = []


def convertDataFrameTime(pdData):
	#returns array of indexs of data set
	return pdData.pd.index


# def KalmanFilter1(pdData, index):
# 	"""
# 		args: PDdata, index

# 		returns Vector

# 	"""
# 	if index < 3:
# 		print 'Needs more than 4'
# 		break
# 	indexList = convertDataFrameTime(pdData) 
# 	observation_matrices = [[index-3, pdData["data_all"][index-3]],[index-2, pdData["data_all"][index-2]], [index-1, pdData["data_all"][index-1]]]
# 	transition_matrix = [  [(index-3)- (index-2), pdData["data_all"][index-3] - pdData["data_all"][index-2] ],[(index-2)- (index-1), pdData["data_all"][index-2] - pdData["data_all"][index-1], [(index-1) - (index), pdData["data_all"][index-1] - pdData["data_all"][index]]
# 	KalmanFilter1(observation_matrices, transition_matrix, n_dim_obs=2)
# 	return kf

def kalmanfilter2(pdData, index):
	kf = KalmanFilter(initial_state_mean=0, n_dim_obs=2)

	if index < 3:
		print 'Needs more than 4'
		break
	indexList = convertDataFrameTime(pdData)
	measurements = [[index-3, pdData["data_all"][index-3],[[index-2, pdData["data_all"][index-2]], [index-1, pdData["data_all"][index-1]]]
	
	return kf.em(measurements).smooth([[2,0], [2,1], [2,2]])[0]

	

def main():
	i = 4
	index_length = len(convertDataFrameTime(REVELANT_DATA))
	while i <= index_length
		PREDICTION_LIST.append(kalmanfilter2(REVELANT_DATA, i))
	print PREDICTION_LIST





if __name__ == '__main__':
    main()  # Run the main method.


