# 5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?


import logging
logging.basicConfig(file='programLog.txt',level=logging.DEBUG,format='%(asctime)s - %(levelname)s- %(message)s')


