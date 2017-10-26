def findMaxMin(list):
	#Check if max and min are equal first
	if min(list) == max(list):
		return [min(list)]
	return [min(list),max(list)]

myList = [0,3,7,88,95,105,9555]

if __name__ == "__main__":
	print (findMaxMin (myList))