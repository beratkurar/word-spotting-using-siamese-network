# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 15:45:46 2017

@author: B
"""

import os
import shutil
book='3368132segr'
#folder=book+'set/'+book+u'seg'
folder='3368132segr20'
for foldername in os.listdir(folder):
    if not foldername.startswith('.'):
        if len(os.listdir(folder+'/'+foldername))>=100:
            shutil.move(folder+'/'+foldername,book+'100/'+foldername )