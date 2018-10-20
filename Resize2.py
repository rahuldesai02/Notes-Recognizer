# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 20:01:49 2018

@author: rahul
"""
import cv2
import glob

images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized"+image,re)
