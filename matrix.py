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
inpath = os.getcwd() + '/Data/Resized_Data/Not_Notes/'
outpath = os.getcwd() + '/Data/Resized_Data/Not_Notes/'
Not_Notes = []
i = 1
all_files = listdir(inpath)
for img_file in all_files:
    print('loading: ' + img_file)
    img = Image.open(inpath + img_file)
    Not_Notes.append(array(img).flatten())
    i = i + 1
numpy.save('negative',Not_Notes)