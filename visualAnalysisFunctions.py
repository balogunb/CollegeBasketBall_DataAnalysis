import pandas as pd
import matplotlib.pyplot as plt





#returns a list of conferences and the average of the column given
def visualizedataSet(df,title):

	plt.title(title)
	plt.xlabel('Year')
	plt.ylabel('Power Rank')
	columns = list(df.columns.values)
	confName = columns.pop(0)
	df = df.sort_values(by = columns[-1],ascending = False)
	print(df)
	print(confName)
	df2 = df.drop(confName,axis = 1)
	#print(df)
	#"""
	

	
	#only show the top 10 performing divisions in the graph
	num = 10
	for x in range(num):
		line = plt.plot(columns, df2.iloc[x,:])
	newDF = df.iloc[0:num]
	plt.legend(list(newDF[confName]), loc=3)
	plt.grid()
	plt.show()