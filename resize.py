#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 16:50:55 2018

@author: shashi
"""
import os
from os import listdir
import PIL
from PIL import Image
inpath = os.getcwd() + '/Data/Raw_Data/Notes/'
outpath = os.getcwd() + '/Data/Resized_Data/Notes/'
i = 1
all_files = [x for x in listdir(inpath) if ('.jpeg' in x or'.jpg' in x) and 'resized_note_' not in x]
for img_file in all_files:
    print('resizing: ' + img_file)
    img = Image.open(inpath + img_file)
    width, height = img.size
    if height < width:
        img = img.rotate(270,0,True)
    basewidth = 180
    baseheight = 320
    img = img.resize((basewidth, baseheight), PIL.Image.ANTIALIAS)
    img.save(outpath + 'resized_note_' + str(i) +'.jpg')
    i = i + 1