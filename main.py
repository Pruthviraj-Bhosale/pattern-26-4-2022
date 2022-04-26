# var = [[0, 2, 4], [1, 2, 3]]
# data = pandas.DataFrame(var)
# print(len(data))
# import sys
# print(sys.path)
#      *
#    * * *
#   ** * **
#  *** * ***


# import Pillow as pi
import time
from tkinter import filedialog
import pyautogui as pya
import os
from datetime import datetime

n = int(input())
for i in range(n):
    for j in range((n * 2 - 1) // 2):
        if j == (n * 2 + 1) // 2 - i:
            print("*" * i, end="")
        else:
            print("", end="")
    print("*" + i * "*")
time.sleep(5)
screen = pya.screenshot()
folder=filedialog.askdirectory()
current_time=datetime.now().replace(microsecond=0)
print(type(current_time))
format ="%y_%B_%d_%H_%M_%S"
new_time= datetime.strftime(current_time,format)
file_name="pattern"+new_time+".png"
files= os.path.join(folder,file_name)
screen.save(files)

