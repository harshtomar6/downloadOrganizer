@echo


echo %~dp0 > directory.txt

copy %~dp0auto.bat 'C:\Users\yashaswiraj007\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\auto.bat'
copy %~dp0directory.txt 'C:\Users\yashaswiraj007\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\directory.txt'

pythonw downloadOrganizer.py
