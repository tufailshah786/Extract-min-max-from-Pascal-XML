import numpy as np
import cv2
import math  
import os
import xml.etree.ElementTree as ET
import json
for filename in os.listdir("path of folder"): 
    filename=os.path.splitext(os.path.basename(filename))[0]
    print(filename)
    tree = ET.parse("path of folder"+filename+'.xml')
    root = tree.getroot()
    for objects in tree.iter('object'):
      #robndbox = objects.find('robndbox')
       #robndbox = objects.find('type').text
       #print(robndbox)
      
       for doc in objects.findall('bndbox'):
         xmin=float(doc.find('xmin').text)
         ymin=float(doc.find('ymin').text)
         xmax=float(doc.find('xmax').text)
         ymax=float(doc.find('ymax').text)
       print(xmin)
       print(ymin)
       print(xmax)
       print(ymax)