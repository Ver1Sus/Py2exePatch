When I compiled project with py2exe, I use main.py, that contain all functional code, and, for example, myProgram.py that contain only 1 string: "from main import *".

After the compiling with py2exe, result is myProgram.exe and main.pyc in library.zip.
When I updated the code in main.py, I don't need to recompile with py2exe, I just put main.pyc in folder "files", run PythonPatch, choose folder where myProgram.exe and profit!!! - the programm was updated!

This solution wery comfortable and simple when the working code is located in remoute server, and recompile with py2exe and update files in the server too long. Using PythonPatch helps me save my time, I hope it save your time too))

dependencies:
  1. zipfile - need to open library.zip
  2. Tkinter - to fast choosing folder
  3. tkFileDialog - find and recognize library.zip
  


1. Put *.pyc files which need to update in the "files" directory
2. Run main.py
3. Choose dir where are *.exe file compiled with py2exe and where consist library.zip
4. library.zip will updated and old library.zip was backup'ed



1.Положи *.pyc файлы в папку files которые нужно обновить
2.Запусти main.py
3.Укажи где находится скомпилированный py2exe-шником скрипт, в котором нужно обновить library.zip
4.Обновится + сделает бэкап старого library.zip
