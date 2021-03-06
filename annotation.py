__author__ = "kdhht5022@gmail.com"
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import subprocess
import os

import argparse

app = argparse.ArgumentParser()
app.add_argument("-n", "--directory", type=str, default="box1",
                 help="Which categories want to select among 10 classes.")
app.add_argument("-start", "--start_no", type=int, default=1,
                 help="Start number of .jpg files.")
app.add_argument("-end", "--end_no", type=int, default=10,
                 help="End number of .jpg files.")
args = vars(app.parse_args())

dr = args["directory"]
start_no = args["start_no"]
end_no = args["end_no"]

directory = str(dr)
start_no = int(start_no)
end_no = int(end_no)

path = str(directory)
files = os.listdir(path)
i = int(start_no)

for file in files:
    if 10 <= i < 100:
        name = '0000' + str(i)
    elif 100 <= i < 1000:
        name = '000' + str(i)
    elif i >= 1000:
        name = '00' + str(i)
    else:
        name = '00000' + str(i)
    os.rename(os.path.join(path, file), os.path.join(path, str(name) + '.JPG'))
    i = i + 1

for i in range(start_no,end_no+1,1):
    if 10 <= i < 100:
        name = '0000' + str(i)
    elif 100 <= i < 1000:
        name = '000' + str(i)
    elif i >= 1000:
        name = '00' + str(i)
    else:
        name = '00000' + str(i)
        
    img1 = cv2.imread(str(directory) +'/' + str(name) + '.JPG')
    img1 = cv2.resize(img1, (600, 400), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(str(directory) +'/' + str(name) + '.jpg', img1)
