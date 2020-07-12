import time

def merge_sort(data, drawData, clockTime):
	merge_sort_alg(data, 0, len(data)-1, drawData, clockTime)

def merge_sort_alg(data, left, right, drawData, clockTime):
	if left < right:
		middle = (left + right) // 2
		merge_sort_alg(data, left, middle, drawData, clockTime)
		merge_sort_alg(data, middle+1, right, drawData, clockTime)
		merge_sorted_list(data, left, middle, right, drawData, clockTime)

def merge_sorted_list(data, left, middle, right, drawData, clockTime):
	drawData(data, getColorArray(len(data), left, middle, right))
	time.sleep(0.12)

	leftPart = data[left:middle+1]
	rightPart = data[middle+1:right+1]

	leftIndex = rightIndex = 0

	for dataIndex in range(left, right+1):
		if leftIndex < len(leftPart) and rightIndex < len(rightPart):
			if leftPart[leftIndex] <= rightPart[rightIndex]:
				data[dataIndex] = leftPart[leftIndex]
				leftIndex += 1
			else:
				data[dataIndex] = rightPart[rightIndex]
				rightIndex += 1
		elif leftIndex < len(leftPart):
			data[dataIndex] = leftPart[leftIndex]
			leftIndex += 1
		else:
			data[dataIndex] = rightPart[rightIndex]
			rightIndex += 1
		drawData(data, ['#A36CCF' if x ==(leftIndex+left) or x ==(rightIndex+middle+1) else '#588DF6' for x in range(len(data))])
		time.sleep(0.12)

	drawData(data, ['green' if x >=left and x <=right else '#588DF6' for x in range(len(data))])
	time.sleep(0.12)

def getColorArray(length, left, middle, right):
	colorArray = []

	for i in range(length):
		colorArray.append('#588DF6')

	return colorArray