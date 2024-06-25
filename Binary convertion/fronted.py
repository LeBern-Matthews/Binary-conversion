from Backend import binary_convo
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
# Function for getting Input 
# from textbox and printing it 
# at label widget 


def printOuput(): 
	base10=float(inputtxt.get(1.0, "end-1c"))
	lbl.config(text = binary_convo(base10))
	lbl.pack() 


# TextBox Creation 
inputtxt = tk.Text(frame, 
				height = -15,
				width = 55,
    			bg=GREY,
       			highlightcolor="GREEN") 
inputtxt.insert("1.0","Enter a number to convert to binary")  

inputtxt.pack(fill="both") 

# Button Creation 
printButton = tk.Button(frame, 
						text = "Enter", 
						command = printOuput) 
printButton.pack()  

frame['background']=DARK_GREY

# Label Creation 
lbl = tk.Label(frame, text = "") 

frame.mainloop() 