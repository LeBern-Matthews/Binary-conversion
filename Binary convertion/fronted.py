from Backend import *
import tkinter as tk 

#Colors
DARK_GREY='#222222'
GREY="#3b3b3b"
LIGHT_GREY="#636363"
RED="#B22222"

# Top level window 
frame = tk.Tk() 
frame.title("Binary Cobvertion") 
frame.geometry('350x200')

# function for getting information entered in entry
def printOuput():
    
	while True:
		try:
			base10=float(inputtxt.get())
			lbl.config(text = binary_convo(base10))
			break
		except ValueError:
			inputtxt.delete(0, tk.END)
			inputtxt.insert(0,"Please enter a number:")
			base10=float(inputtxt.get())
			continue
	lbl.pack() 

#Entry creation
inputtxt=tk.Entry(frame, width=55,bg=LIGHT_GREY)

# Setting the default value to be displayed
inputtxt.insert(0,"Enter a number to convert to binary")  

inputtxt.pack(fill="both") 

# Button Creation 
printButton = tk.Button(frame, text = "Enter", command = printOuput) 
printButton.pack()  

frame['background']=DARK_GREY

# Label Creation 
lbl = tk.Label(frame, text = "",bg=LIGHT_GREY) 

frame.mainloop() 
