import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

#handle1 = open("./metricstest/outlabtimes.csv", 'rb')

handle1 = open("./metricstest/outlabeff.csv", 'rb')
handle2 = open("./metricstest/inlabeff.csv", 'rb')

handle3 = open("./metricstest/outlabtimes.csv", 'rb')
handle4 = open("./metricstest/inlabtimes.csv", 'rb')

handle5 = open("./metricstest/outlabspeed.csv", 'rb')
handle6 = open("./metricstest/inlabspeed.csv", 'rb')

handle7 = open("./metricstest/outlabovershoot.csv", 'rb')
handle8 = open("./metricstest/inlabovershoot.csv", 'rb')

#handle7 = open("./metrics/outlabclickwaittimes.csv", 'rb')
#handle8 = open("./metrics/inlabclickwaittimes.csv", 'rb')


inlabeff = []
outlabeff = []
inlabtimes = []
outlabtimes = []
inlabspeed = []
outlabspeed = []
inlabover = []
outlabover = []

'''
with handle1 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		print len(row)
		for place in range(0, len(row)):
			#print row[place]
			if(float(row[place]) <= float(0.0)):
				print row[place]
				
			else:
				outlabtimes.append(row[place])
				
'''

with handle1 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		print len(row)

with handle2 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		print len(row)

with handle3 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		print len(row)

with handle4 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		print len(row)

with handle5 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		print len(row)

with handle6 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		print len(row)

with handle7 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		print len(row)

with handle8 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		print len(row)


#print len(outlabtimes)

#c1 = csv.writer(handle2, delimiter = ',')

#c1.writerow(outlabtimes)