# -*- coding: utf-8 -*-
"""
Created on Thu May 04 17:38:25 2017

@author: B
"""

import os

os.chdir('gwo5')

for foldername in os.listdir(unicode(os.getcwd())):
    os.chdir(foldername)
    label=0
    for filename in os.listdir(unicode(os.getcwd())):
        os.rename(filename, str(label)+'.tif')
        label=label+1
    os.chdir('..')
