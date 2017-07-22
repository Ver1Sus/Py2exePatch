'''
some important text

'''

from zipfile import ZipFile
import os, tkFileDialog
from Tkinter import *

##---- where need update library.zip
dirName = "./"

##---- set in dirName path to directory which you choose
def searchFolder():
	root.directory = tkFileDialog.askdirectory()
	dirName = (root.directory)
	iptBox.delete(0, 999)
	iptBox.insert(0, dirName)
	
def searchDone():
    global dirName
    dirName = iptBox.get()
    root.destroy()	
	
##---- window with field to open dir with libwitch need patched
root = Tk()

iptBox = Entry(root, width='30')
iptBox.pack(side=LEFT)
btnOk = Button(root, text="OK", command = searchDone).pack(side=RIGHT)
btnSearch = Button(root, text="Search...", command=searchFolder).pack(side=RIGHT)

root.mainloop()

dirName = dirName.replace('/','\\')
print dirName

##---- contain library.zip in this folder?
checkZip = 'library.zip' in os.listdir(dirName)
if not(checkZip):
	raw_input('There no library.zip, programm was exit...')
	exit()
else:
	print 'I see file library.zip'

	

##---- get name of all files in dir FILES
newFiles = os.listdir('files')
print("Files, wich need update: ")
print(newFiles)

##---- create new zip-file without files which need to remove
ZipOut = ZipFile(dirName + '\\library2.zip','w')
ZipIn = ZipFile(dirName +'\\library.zip','r')
for item in ZipIn.infolist():
	buf = ZipIn.read(item.filename)
	if not(item.filename in newFiles):
		ZipOut.writestr(item, buf)		
		
ZipIn.close()

##------ add new files in ZIP-file
for itemName in newFiles:
	ZipOut.write(r'files\\'+itemName, itemName)
	
ZipOut.close()

##----- delete old ZipFile and Rename New

##--- try to backup. If file library_Backup.zip exist - need remove it
try:
	os.rename(dirName + '\\library.zip',dirName + '\\library_Backup.zip')
	print 'Backuping is good'
except:
	print 'Backup was recreated...'
	os.remove(dirName + '\\library_Backup.zip')
	os.rename(dirName + '\\library.zip',dirName + '\\library_Backup.zip')
	print 'Backuping is good'

##--- rename new zip file. If file library.zip is exist - remove it
try:
	os.rename(dirName + '\\library2.zip',dirName + '\\library.zip')
	print 'Rename good'
except:
	print 'library.zip recreated'
	os.remove(dirName + '\\library.zip')
	os.rename(dirName + '\\library2.zip',dirName + '\\library.zip')
	print 'Rename good'

	
print "Done"
raw_input("Print enter to exit...")





























