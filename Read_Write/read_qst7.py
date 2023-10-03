# 7. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?

from pathlib import Path
import os

p=Path(r'C:\Users\mayur\Python_3oct\Read_Write\read_qst6.py')
print('Dir Name :',os.path.dirname(p))
print('Base Name :',os.path.basename(p))
print('Hello')