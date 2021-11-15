import os

for i in range(1,51,1):
    os.mkdir(str(i))
    os.mkdir(str(i)+"/mon")
    os.mkdir(str(i)+"/tue")
    os.mkdir(str(i)+"/wed")
    os.mkdir(str(i)+"/thu")
    os.mkdir(str(i)+"/fri")