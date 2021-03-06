import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

handleineff = open("./Efficiencies/inlab.csv", 'rb')
handleouteff = open("./Efficiencies/outlab.csv", 'rb')
handleintimes = open("./Efficiencies/inlabtimes.csv", 'rb')
handleouttimes = open("./Efficiencies/outlabtimes1.csv", 'rb')

inlabeff = []
outlabeff = []
inlabtimes = []
outlabtimes = []


with handleineff as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabeff = np.array(list(row)).astype(np.float)


with handleouteff as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabeff = np.array(list(row)).astype(np.float)

with handleintimes as infile:
	parsed = csv.reader(infile)
	for row in parsed:
		inlabtimes = np.array(list(row)).astype(np.float)

with handleouttimes as infile:
	parsed = csv.reader(infile)
	for row in parsed:
		outlabtimes = np.array(list(row)).astype(np.float)

bins = np.arange(0, 1.005, 0.005)

#print len(inlabeff)
#print len(outlabeff)
#print len(inlabtimes)
#print len(outlabtimes)

'''
sdvinlab = np.std(inlabeff)
meaninlab = np.mean(inlabeff)
label1 = ["$\mu$: " + str(meaninlab) + "\n" + "$\sigma$: " + str(sdvinlab)]
plt.hist(inlabeff, bins, normed = True, weights = inlabtimes, label = label1)
#plt.hist(inlabeff, bins, label = label1)
plt.title("Probability density $f(x)$ of in-lab mousepath efficiency \n weighted by duration of mouse sequence")
#plt.title("Histogram of in-lab mousepath efficiency")
plt.xlabel("Efficiency (Optimal mousepath length / Actual mousepath length)")
#plt.ylabel("# of mouse path sequences")
plt.ylabel("Weighted probability density $f(x)$")
plt.xticks(np.arange(0, 1.1, 0.1), rotation = 'vertical')
plt.legend(loc="best")
#plt.show()
#plt.savefig('./EfficiencyGraphs/' + "inLabPDFexcl" + '.png')
#plt.savefig('./EfficiencyGraphs/' + "PDFinLab" + '.png')
#plt.savefig('./EfficiencyGraphs/' + "WeightedinLabHist" + '.png')
plt.savefig('./EfficiencyGraphs/' + "WeightedinLabPDF" + '.png')
plt.clf()

sdvoutlab = np.std(outlabeff)
meanoutlab = np.mean(outlabeff)
label2 = ["$\mu$: " + str(meanoutlab) + "\n" + "$\sigma$: " + str(sdvoutlab)]
plt.hist(outlabeff, bins, normed = True, weights = outlabtimes, label = label2)
#plt.hist(outlabeff, bins, label = label2)
plt.title("Probability density $f(x)$ of out-of-lab mousepath efficiency \n weighted by duration of mouse sequence")
#plt.title("Histogram of out-of-lab mousepath efficiency")
plt.xlabel("Efficiency (Optimal mousepath length / Actual mousepath length)")
#plt.ylabel("# of mouse path sequences")
plt.ylabel("Weighted probability density $f(x)$")
plt.xticks(np.arange(0, 1.1, 0.1), rotation = 'vertical')
plt.legend(loc="best")
#plt.show()
#plt.savefig('./EfficiencyGraphs/' + "OutOfLabPDFexcl" + '.png')
#plt.savefig('./EfficiencyGraphs/' + "PDFOutOfLab" + '.png')
#plt.savefig('./EfficiencyGraphs/' + "WeightedOutOfLabHist" + '.png')
plt.savefig('./EfficiencyGraphs/' + "WeightedOutOfLabPDF" + '.png')
plt.clf()



print sdvinlab
print meaninlab
print sdvoutlab
print meanoutlab

'''

data = [inlabeff, outlabeff]
plt.boxplot(data, 1)
plt.title("Total in lab efficiency (left) vs. Total out of lab efficiency (right)")
plt.ylabel('Efficiency (optimal/actual path lengths')
#plt.savefig('./EfficiencyGraphs/' + "TotalBoxPlot" + '.png')
plt.show()
plt.clf()
