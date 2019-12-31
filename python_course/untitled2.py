# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:15:30 2019

@author: EGLOBAL
"""

import numpy as np
from os import listdir
from os.path import isfile, join
import os
from pathlib import Path


pathh = 'D:\WUDownloadCache\faces94' #input("enter your file path : ")
filess = []
folders = []
p = Path(pathh)


for root, dirs, files in os.walk(path):
    print(files)
    if os.path.isdir(root):  
        print("\nIt is a directory")  
        folders.append(root)
    if os.path.isfile(root):  
        print("\nIt is a normal file")  
#        filess.append(files)
    
#    if Path(root).is_dir():
#        folders.append(root.cwd())
#    filess.append(root.cwd())
#        
    
#    print(Path(root).is_dir())
#    if Path(root).is_file():
#        filess.append(Path(root))
#    elif Path(root).is_dir():
        
        #        folders.append(Path(root))
    
    
    
#    p = Path(root)
#    for entry in os.scandir(root):
#        if root.is_file():
#            files.append(root)
#        filess.append(root)
#    
#    for file_name  in path:
#    print(root)
#    print(dirs, files)

#p = Path(pathh)


#import os  
#path=r'D:\WUDownloadCache\faces94'
#if os.path.isdir(path):  
#    print("\nIt is a directory")  
#elif os.path.isfile(path):  
#    print("\nIt is a normal file")  
#else:  
#    print("It is a special file (socket, FIFO, device file)" )
#print()

#
#
#only_file = [f for f in listdir(pathh)  ]
#print(only_file)