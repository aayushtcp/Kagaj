from tkinter import *
# from tkmacosx import Button

root = Tk()


def changethemetoblack():
    root.config(bg="#000000")


def changethemetowhite():
    root.config(bg="#ffffff")


def changethemetored():
    root.config(bg="#ff0000")


themeblackbutton = Button(root, text="Change Theme To Black", command=changethemetoblack, bg="#000000", fg="#ffffff")
themewhitebutton = Button(root, text="Change Theme To White", command=changethemetowhite)
themeredbutton = Button(root, text="Change Theme To Red", command=changethemetored, bg="#ff0000", fg="#ffffff")

themeblackbutton.pack()
themewhitebutton.pack()
themeredbutton.pack()

root.mainloop()
