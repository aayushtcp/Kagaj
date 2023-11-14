from tkinter import *
from tkinter import colorchooser
import tkinter.messagebox as msg
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import ttk
import os
# Function section Starts =====================================================
# =================Functions for Menu m1 (File Menu)====================

def quitApp():
    root.destroy()
    
def newFile():
    global file
    root.title("Untitled - Kagaj")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file =None
    else:
        root.title(os.path.basename(file))
        TextArea.delete(1.0, END)
        f= open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()    

def saveFile():
    global file
    if file == None:
        file =asksaveasfilename(initialfile="Kagaj.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        
        if file == "":
            file =None
        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0,END))
            f.close()
            
            root.title(os.path.basename(file)+ " - Kagaj")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0,END))
        f.close()
        

def saveasFile():
    global file
    if file == None:
        file =asksaveasfilename(initialfile="Kagaj.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        
        if file == "":
            file =None
        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0,END))
            f.close()
            
            root.title(os.path.basename(file)+ " - Kagaj")


# =================Functions for Menu m2 (Edit Menu)====================
def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))
    
def paste():
    TextArea.event_generate(("<<Paste>>"))
# =================Functions for Menu m3 (Advanced Menu)====================
def bcolor():
    c= colorchooser.askcolor()
    TextArea.configure(background=c[1])
    # Making foreground auto white when bg is black
    if c[1] == "#000000":
        TextArea.configure(foreground="#FFFFFF")
        
def fcolor():
    c= colorchooser.askcolor()
    TextArea.configure(foreground=c[1])
    
# =================Functions for Menu m4 (Advanced Menu)====================
def about():
    msg.showinfo("About US","We are good boys! Please don't kill us!")


# Function section Ends =========================================== ==========
if __name__ == '__main__':
    # GUI Settings
    root = Tk()
    root.title("Untitled - Kagaj")
    root.geometry('644x788')
    # root.wm_iconbitmap('file.png')
    # root.iconphoto(False,PhotoImage(file='notes.png'))
    
    
    # Adding ScrollBar area======================================================
    style=ttk.Style()
    style.theme_use('alt')
    style.configure("Vertical.TScrollbar", background="grey", bordercolor="grey", arrowcolor="grey")

    scrollbar = ttk.Scrollbar(root)
    scrollbar.pack(fill=Y, side=RIGHT)
    
    
    # Adding text area======================================================
    TextArea = Text(root, font="lucida 13", yscrollcommand=scrollbar.set, undo=True)
    file = None
    TextArea.pack(expand=True, fill=BOTH)
    
    scrollbar.config(command=TextArea.yview) #Syncronizing with TextArea

    # Menubar
    filemenu = Menu(root)
    # =============================m1 is for File Menu Starts==============================
    m1 = Menu(filemenu, tearoff=0)
    m1.add_command(label="New", command=newFile)
    m1.add_command(label="Open", command=openFile)
    m1.add_command(label="Save", command=saveFile)
    m1.add_command(label="Save As", command=saveasFile)
    m1.add_separator()
    m1.add_command(label="Exit", command=quitApp)
    # =============================m1 is for File Menu Ends==============================
    
    
    # =============================m2 is for Edit Menu Starts==============================
    m2 = Menu(filemenu, tearoff=0)
    m2.add_command(label="Cut", command=cut)
    m2.add_command(label="Copy", command=copy)
    m2.add_command(label="Paste", command=paste)
    m2.add_separator()
    m2.add_command(label="Undo", command=TextArea.edit_undo)
    m2.add_command(label="Redo", command=TextArea.edit_redo)
    # =============================m2 is for Edit Menu Ends==============================
    
    
    # =============================m3 is for View Menu Starts==============================
    m3 = Menu(filemenu, tearoff=0)
    m3.add_command(label="Background Color", command=bcolor)
    m3.add_command(label="Foreground Color", command=fcolor)
    m3.add_command(label="View3")
    # =============================m3 is for View Menu Ends==============================
    
    
    # =============================m4 is for Help Menu Starts==============================
    m4 = Menu(filemenu, tearoff=0)
    m4.add_command(label="About", command=about)
    # =============================m4 is for Help Menu Ends==============================
    
    
    # Configure the main menu and adding cascate names in it
    root.config(menu=filemenu)
    filemenu.add_cascade(label="File", menu=m1)
    filemenu.add_cascade(label="Edit", menu=m2)
    filemenu.add_cascade(label="Advanced", menu=m3)
    filemenu.add_cascade(label="Help", menu=m4)
        
        
    # Event Loop
    root.mainloop()