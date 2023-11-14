# Import library 
import tkinter as tk 

# Create Tkinter window 
frame = tk.Tk() 
frame.title('GFG Cursors') 
frame.geometry('200x200') 

# Specify dot cursor with blue color for frame 
frame.config(cursor="dot blue") 

# Specify various cursor icons with colors 
# for label and buttons 
tk.Label(frame, text="Text cursor", 
		cursor="xterm #0000FF").pack() 

tk.Button(frame, text="Circle cursor", 
		cursor="circle #FF00FF").pack() 

tk.Button(frame, text="Plus cursor", 
		cursor="plus red").pack() 

# Specify cursor icon and color using 
# config() method 
a = tk.Button(frame, text='Exit') 
a.config(cursor="dot green red") 
a.pack() 

frame.mainloop() 
