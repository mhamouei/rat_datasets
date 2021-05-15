#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 12:55:01 2021

@author: mhit
"""

import numpy as np
from mmapnpz import NpzMMap
from tqdm import tqdm

items_per_file = 25000
counter = items_per_file
#Writing XSS dataset to a text file
#xss = open('XSS/XSS.txt', 'w')
print("Please be patient as it may take several minutes...")
with NpzMMap("XSS/XSS.npz") as zfile:
            with zfile.mmap("arr_0") as data:
                fid = 1
                for d in tqdm(data):
                    if items_per_file == counter:
                      xss = open('XSS/XSS_'+str(fid)+'.txt', 'w')
                    xss.write("%s\n" % d)
                    counter -= 1
                    if counter == 0:
                        xss.close()
                        fid += 1
                        counter = items_per_file
if counter > 0:                
    xss.close()
    counter = items_per_file

#Writing SQLi dataset to a text file
#sqli = open('SQL injection/SQLi.txt', 'w')                    
with NpzMMap("SQL injection/SQLi.npz") as zfile:
            with zfile.mmap("arr_0") as data:
                fid = 1
                for d in tqdm(data):
                    if items_per_file == counter:
                      sqli = open('SQL injection/SQLi_'+str(fid)+'.txt', 'w')
                    sqli.write("%s\n" % d[0])
                    counter -= 1
                    if counter == 0:
                        sqli.close()
                        fid += 1
                        counter = items_per_file

if counter > 0:
    sqli.close()
