#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 12:55:01 2021

@author: mhit
"""

import numpy as np
from mmapnpz import NpzMMap
from tqdm import tqdm


#Writing XSS dataset to a text file
xss = open('XSS/XSS.txt', 'w')
with NpzMMap("XSS/XSS.npz") as zfile:
            with zfile.mmap("arr_0") as data:
                for d in tqdm(data):
                    xss.write("%s\n" % d)
                    
xss.close()

#Writing SQLi dataset to a text file
sqli = open('SQL injection/SQLi.txt', 'w')                    
with NpzMMap("SQL injection/SQLi.npz") as zfile:
            with zfile.mmap("arr_0") as data:
                for d in tqdm(data):
                    sqli.write("%s\n" % d[0])
sqli.close()
