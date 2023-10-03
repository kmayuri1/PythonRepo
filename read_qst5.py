#5. What do the os.getcwd() and os.chdir() functions do?

from pathlib import Path
import os
print(os.getcwd())
os.chdir(r'C:\D Drive\New folder')
print(Path.cwd())
os.chdir(r'C:\Users\mayur\Python_3oct\Read_Write')
print(Path.cwd())