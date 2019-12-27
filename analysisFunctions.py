"""
//---------------------------------------------------------------
// File: analysisFunctions.py
// Purpose: Holds functions used for analysing dataframes
// Programming Language: Python
// Author: Basit Balogun
// Version: 1.0
//---------------------------------------------------------------
"""






import pandas as pd




#returns a list of conferences and the average of the column given
def getConfAverages(df, colNam,year):
	confList = [] #list which would hold conferences and their avarages
	confNames = df['CONF'].unique()
	confNames.sort()
	#print(len(confNames))
	

	#for each conference determine the col average and add to confList
	for x in range(len(confNames)):
		newDf = df[df['CONF'].str.match(confNames[x])] 
		newDf = newDf[newDf['YEAR'].astype(str).str.contains(year)]
		confMean = newDf[colNam].mean() #calc mean of req columns
		#print(confNames[x] + " " + str(confMean))
		obj = {"name":confNames[x],"stat":colNam,"val":confMean}
		confList.append(obj)
		#print(" ")


	return confList



#MORE TO COME