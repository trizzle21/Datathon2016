"""
This is the first example of a predictive algorithm where we test by day.


We will be predicting total usage of data per day.

We will have two data sets for this, a training set and an already calculated set.

Training set will be the basis for the linear predictive equation (using the least square)
the training set will be a dictionary of days and their respective t,y points

Will be using a 3 pt training set to make things easier at first.

Two main calculations will be made, the actual change of data consumption per day from already calculated data, and the predicted data change from test data set

The prediction will either be positive or negative, and start from the last value of test data.

"""





def dailyDataUsage(xValues, yValues):
	# 
	# uses the trapazoidal rule to calculate data usage over the day
	if(len(xValues) != len(yValues)):
		raise ValueError
	counter,usage = 0,0
	while counter < len(dataArray):
		usage += (xValues[counter+1] - xValues[counter])*((yValues[counter] + yValues[counter+1])/2)
		counter += 2
	return usage




#Build TestData time series
def buildTrainingData(trainingData):
	timeSeries = {}
	day = 0 
	for i in trainingData:
		timeSeries[day] = dailyDataUsage(i[0],i[1]);
	return timeSeries	

 
def incrementSeries(dailyUsage):
	r = {0: dailyUsage.pop(0)}
	for key, value in timeSeries.iteritems():
		r[key] = value - r[key-1]
	return r

 def ARcoefficient(incrementSeriesData):
	# 
	#
	#
	g, k = [],1
	while k < len(dailyUsage):
		dailyUsage[k] + dailyUsage[k-1] - dailyUsage[k]
		g.append()




#Predictive Equation 