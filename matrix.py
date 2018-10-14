#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 00:32:58 2018

@author: shashi
"""
import os
import numpy
from numpy import array
from os import listdir
from PIL import Image
data = []
inpath = os.getcwd() + '/Data/Resized_Data/Notes/'
i = 1
all_files = listdir(inpath)
for img_file in all_files:
    print('loading: ' + img_file)
    img = Image.open(inpath + img_file)
    imgarray = array(img).flatten()
    imgarray = numpy.append(imgarray,1)
    data.append(imgarray)
    i = i + 1
inpath = os.getcwd() + '/Data/Resized_Data/Not_Notes/'
i = 1
all_files = listdir(inpath)
for img_file in all_files:
    print('loading: ' + img_file)
    img = Image.open(inpath + img_file)
    imgarray = array(img).flatten()
    imgarray = numpy.append(imgarray,0)
    data.append(imgarray)
    i = i + 1
numpy.save('Data',data)