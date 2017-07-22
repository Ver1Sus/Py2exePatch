from Tkinter import *
import os, tkFileDialog

def searchFolder():
	root.directory = tkFileDialog.askdirectory()
	dirName = (root.directory)
	iptBox.delete(0, 999)
	iptBox.insert(0, dirName)
	
def searchDone():
    global dirName
    dirName = iptBox.get()
    root.destroy()


root = Tk()

iptBox = Entry(root, width='30')
iptBox.pack(side=LEFT)

btnOk = Button(root, text="OK", command = searchDone).pack(side=RIGHT)
btnSearch = Button(root, text="Search...", command=searchFolder).pack(side=RIGHT)



root.mainloop()


print dirName
