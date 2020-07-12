from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort

FRAME_BG = '#2E4054'
CANVAS_BG = '#E3E2E3'
BAR_BG = '#588DF6'
TEXT_COLOR = '#fff'

data = []

root = Tk()
root.title('Sorting Algorithm Visualisation')
root.iconbitmap(r'Sort.ico')
root.minsize(1300, 702)
root.maxsize(1300, 702)	
root.config(bg='black')
seleted_alg = StringVar()

def drawData(data, barColors):
	canvas.delete("all")
	c_height = 600
	c_width = 1300
	x_width = c_width / (len(data) + 1)
	offset = 20
	spacing = 2
	normalizeData = [i / max(data) for i in data]
	for i, height in enumerate(normalizeData):
		#top left
		x0 = i * x_width + offset + spacing
		y0 = c_height - height * 580
		#bottom right
		x1 = (i + 1) * x_width + offset
		y1 = c_height
		canvas.create_rectangle(x0, y0, x1, y1, fill=barColors[i], outline="")
		canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
	root.update_idletasks()

def Generate():
	global data
	
	minVal = int(minEntry.get())

	maxVal = int(maxEntry.get())

	size = int(sizeEntry.get())

	data = []
	for i in range(size):
		random1 = random.randrange(minVal, maxVal)
		data.append(random1+1)
		print(random1+1, end=" ")
	print('\n')
	drawData(data, [BAR_BG for x in range(len(data))])

#To make text disable in the dropdown
def validate():
    return False
validatecmd = (root.register(validate))

def get_value(val):
	return val

def startSorting():
	global data
	print('startSorting')
	if not data:
		print('in not data')
		return

	if algMenu.get() == 'Quick Sort':
		print('in quicksort')
		quick_sort(data, 0, len(data)-1, drawData, SeleteSpeed.get())
	
	elif algMenu.get() == 'Bubble Sort':
		print('bubble_sort')
		bubble_sort(data, drawData, SeleteSpeed.get())
	
	elif algMenu.get() == 'Merge Sort':
		print('Merge Sort')
		merge_sort(data, drawData, SeleteSpeed.get())


	drawData(data, ['green' for x in range(len(data))])	

#frame / base layout
UI_frame = Frame(root, width=1, bg=FRAME_BG)
UI_frame.grid(row=0, column=0)

canvas = Canvas(root, width=1300, height=600,bg=CANVAS_BG)
canvas.grid(row=1, column=0)

#User Interface Area
#Row[0]
Label(UI_frame, text="Size: ", bg=FRAME_BG, fg=TEXT_COLOR, font=("Helvetica", 16)).grid(row=0, column=0, padx=8, pady=5)
sizeEntry = Scale(UI_frame, from_=2, to=35, orient=HORIZONTAL, bg=FRAME_BG, fg=TEXT_COLOR, cursor="hand2", command=get_value)
sizeEntry.grid(row=0, column=1, padx=8, pady=5)

Label(UI_frame, text="Min Value: ", bg=FRAME_BG, fg=TEXT_COLOR, font=("Helvetica", 16)).grid(row=0, column=2, padx=8, pady=5)
minEntry = Scale(UI_frame, from_=0, to=20, orient=HORIZONTAL, bg=FRAME_BG, fg=TEXT_COLOR, cursor="hand2", command=get_value)
minEntry.grid(row=0, column=3, padx=8, pady=5)

Label(UI_frame, text="Max Value: ", bg=FRAME_BG, fg=TEXT_COLOR, font=("Helvetica", 16)).grid(row=0, column=4, padx=8, pady=5)
maxEntry = Scale(UI_frame, from_=21, to=100, orient=HORIZONTAL, bg=FRAME_BG, fg=TEXT_COLOR, cursor="hand2", command=get_value)
maxEntry.grid(row=0, column=5 , padx=8, pady=5)

#Row[0]
Label(UI_frame, text="Algorithms: ", bg=FRAME_BG, fg=TEXT_COLOR, font=("Helvetica", 16)).grid(row=0, column=6, padx=8, pady=5)
algMenu = ttk.Combobox(UI_frame, textvariable=seleted_alg, values=['Bubble Sort', 'Quick Sort', 'Merge Sort'], validatecommand=validatecmd)
algMenu.update()
algMenu.configure(validate="key")
algMenu.grid(row=0, column=7, padx=8, pady=5)
algMenu.current(0)

Label(UI_frame, text="Select Speed: ", bg=FRAME_BG, fg=TEXT_COLOR, font=("Helvetica", 16)).grid(row=0, column=8, padx=8, pady=5)
SeleteSpeed = Scale(UI_frame, from_=0.0, to=2.0, length=100, digits=2, resolution=0.2, orient=HORIZONTAL, bg=FRAME_BG, fg=TEXT_COLOR, cursor="hand2", command=get_value)
SeleteSpeed.grid(row=0, column=9 , padx=8, pady=5)
SeleteSpeed.set(1.0)

Button(UI_frame, text="Generate Array", relief=RAISED, command=Generate, cursor="hand2", bg=FRAME_BG, fg=TEXT_COLOR, font=("Helvetica", 16)).grid(row=1, column=5, padx=1, pady=5 )
Button(UI_frame, text="Sort", relief=RAISED, command=startSorting, cursor="hand2", bg=FRAME_BG, fg=TEXT_COLOR, font=("Helvetica", 16)).grid(row=1, column=6, padx=1, pady=5 )


root.mainloop()