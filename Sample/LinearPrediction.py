"""
This is the first example of a predictive algorithm where we test by day.


We will be predicting total usage of data per day.


"""


def dailyDataUsage(xValues, yValues):
	# yValues comes in 
	# uses the trapazoidal rule to calculate data usage over the day
	if(len(xValues) != len(yValues)):
		raise ValueError
	counter,usage = 0,0
	while counter < len(dataArray):
		usage += (xValues[counter+1] - xValues[counter])*((yValues[counter] + yValues[counter+1])/2)
		counter += 2
	return usage
	