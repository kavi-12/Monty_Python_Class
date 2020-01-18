import os
import re
import shutil

mylist = list(os.walk("../../../Task_2/My_Files"))
pattern = r'.\w+'
from os import path

for i in mylist[0][2]:
    extensions = re.findall(pattern, i)
    file_name = extensions[1][1:].upper()
    if path.exists(file_name):
        shutil.move(os.getcwd()+"\\My_Files\\"+i, os.getcwd()+ "\\" + file_name)
    else:
        os.mkdir(file_name)
        shutil.move(os.getcwd() + "\\My_Files\\" +i, os.getcwd() + "\\" + file_name)