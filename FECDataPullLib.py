import csv
import sys
import json

def prompt():
	"""
	Expected Input: none
	Expected Output: List of csv filename(s).
	"""
	file1 = raw_input("Enter first CSV filename (required): ")
	file2 = raw_input("Enter second CSV filename (optional): ")

	if (file1 and file2):
		#2 files input.
		print("You have entered 2 filenames, " + file1 + " and " + file2 + ".")
		return [file1, file2]
	elif (file1 and not file2):
		#1 file input.
		print("You have entered 1 filenames, " + file1 + ".")
		return [file1]
	else:
		#Rerun script.
		print("Error... Retype filenames.")
		prompt()

def printDictionary(dictionary):
	"""
	Prints input dictionary.
	"""
	print(json.dumps(dictionary, indent = 4))

def getKeyList(CSVList):
	"""
	Expected Input: List of all rows within CSV file.
	Expected Output: List of keys (transaction_id) within CSVList.
	"""

	keyList = []

	for row in CSVList:
		keyList.append(row[6])

	#Pop the column header.
	keyList.pop(0)

	return(keyList)

def getRowValList(CSVList):
	"""
	Expected Input: List of all rows within CSV file.
	Expected Output: List of columns within CSVList.
	"""
	valList = []

	for row in CSVList:
		valList.append(row)

	valList.pop(0)

	return(valList)

def getColumnHeaderList(CSVList):
	"""
	Expected Input: List of all rows within CSV file.
	Expected Output: List of column headers (first row) within CSVList.
	"""
	columnHeaderList = CSVList[0]

	return(columnHeaderList)

def getTransactionDict(columnHeaderList, valueList):
	"""
	Expected Input: List of all column headers. Values of a single transaction.
	Expected Output: Dictionary for single transaction.
	"""
	transactionDict = dict(zip(columnHeaderList, valueList))
	return(transactionDict)

def getFullDict(keyList, columnHeaderList, CSVListDict):
	"""
	Expected Input: List of transaction_ids. List of column headers. Dictionary of lists.
	Expected Output: Dictionary for all transactions.
	"""
	fullDict = {}
	#For each transaction_id, add a new key to the full dictionary whose value is a dictionary of data associated with that transaction_id.
	for i in range(len(keyList)):
		key = keyList[i]
		fullDict[key] = getTransactionDict(columnHeaderList, CSVListDict.get(key))

	return(fullDict)

def getTypeDict(fullDict, entityType):
	"""
	Expected Input: Full dictionary. EntityType tag to look up for each transaction_id.
	Expected Output: Dictionary filtered by entityType.
	"""
	typeDict = {}

	for key in fullDict.keys():
		if(fullDict[key]["entity_type"] == entityType):
			typeDict[key] = fullDict[key]

	return(typeDict)

def openFile(filename):
	"""
	Expected Input: CSV File
	Expected Output: List of all rows within CSV file.
	"""
	with open(filename) as CSVFile:

		CSVReader = csv.reader(CSVFile, delimiter = ",")
		CSVList = list(CSVReader)

		print("csv file " + filename + " now loaded.")

		return CSVList