import time
BAR_BG = '#588DF6'

def bubble_sort(data, drawData, clockTime):
	for _ in range(len(data)-1):
		for j in range(len(data)-1):
			if data[j] > data[j+1]:
				data[j], data[j+1] = data[j+1], data[j]
				drawData(data, ['#A36CCF' if x ==j or x==j+1 else BAR_BG for x in range(len(data))])
				time.sleep(2.0-clockTime)
	drawData(data, ['green' for x in range(len(data))])