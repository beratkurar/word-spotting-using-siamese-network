# -*- coding: utf-8 -*-
"""
Created on Thu May 04 17:38:25 2017

@author: B
"""

import os
book='3368132segr'
#os.chdir(book+'set/'+book+'seg10')
os.chdir(book)
label=0
for foldername in sorted(os.listdir(str(os.getcwd()))):
    l=len(str(label))
    z=5-l
    a=''
    for i in range(z):
        a+='0'
    os.rename(foldername,a+str(label))
    label=label+1
    
