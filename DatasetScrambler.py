# -*- coding: utf-8 -*-
"""
Created on Thu May 04 17:38:25 2017

@author: B
"""

import os
import random


book='3157556'
os.chdir(book+'set/'+book+'seg20')

folders=[]

for foldername in os.listdir(unicode(os.getcwd())):
    folders.append(foldername)
    

random.shuffle(folders)
label=200
for foldername in folders:
    os.rename(foldername, str(label))
    label=label+1

label=0   
for foldername in os.listdir(unicode(os.getcwd())):
    os.rename(foldername, str(label))
    label=label+1
    
    
