import csv
import sys
import json
import FECDataPullLib2 as lib

filenames = lib.prompt()
numFiles = len(filenames)

if (numFiles == 1):

	#List of all rows in the csv.
	CSVList = lib.openFile(filenames[0])
	#Keys are transaction_ids
	keyList = lib.getKeyList(CSVList)
	#RowVals are the entire csv's values divided into rows, without the column headers.
	RowValList = lib.getRowValList(CSVList)
	#First row within csv.
	columnHeaderList = lib.getColumnHeaderList(CSVList)

	#Zips transaction_ids with associated row.
	CSVListDict = dict(zip(keyList, RowValList))

	fullDict = lib.getFullDict(keyList, columnHeaderList, CSVListDict)

	indDict = lib.getTypeDict(fullDict, "IND")

	#for key in fullDict.keys():
	#	if (fullDict[key]["entity_type"] == "IND"):
	#		indDict[key] = fullDict[key]


	lib.printDictionary(indDict)