import time

def quick_sort(data, head, tail, drawData, clockTime):

	if head > tail:
		return
	partitionIndex = partition(data, head, tail, drawData, clockTime)

	quick_sort(data, head, partitionIndex-1, drawData, clockTime)
	quick_sort(data, partitionIndex+1, tail, drawData, clockTime)


def  partition(data, head, tail, drawData, clockTime):
	border = head
	pivot = data[tail]

	drawData(data, getColorArray(len(data), head, tail, border, border))
	time.sleep(2.0 - clockTime)

	for i in range(head, tail):
		if(data[i]<pivot):
			drawData(data, getColorArray(len(data), head, tail, border, i, True))
			time.sleep(2.0 - clockTime)
	
			data[border], data[i] = data[i], data[border]
			border += 1


		drawData(data, getColorArray(len(data), head, tail, border, i))
		time.sleep(2.0 - clockTime)


	drawData(data, getColorArray(len(data), head, tail, border, tail, True))
	time.sleep(2.0 - clockTime)

	data[tail], data[border] = data[border], data[tail]

	return border

def getColorArray(dataLen, head, tail, border, currIndex, isSwapping = False):
	colorArray = []
	for i in range(dataLen):
		if i>=head and i<=tail:
			colorArray.append('#588DF6')
		else:
			colorArray.append('#588DF6')

		if i==tail:
			colorArray[i] = 'yellow'
		elif i==border:
			colorArray[i] = '#A36CCF'
		elif i==currIndex:
			colorArray[i] = '#A36CCF'

		if isSwapping:
			if i==border or i==currIndex:
				colorArray[i] = 'green'

	return colorArray