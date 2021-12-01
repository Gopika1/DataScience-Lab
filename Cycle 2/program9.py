#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:27:54 2021

@author: sjcet
"""

import numpy as np

a= np.array([[3, 6,7,8]])
print("1D Array \n",a) 
b=np.array([[3, 6,8,7], [4, 2,1,0],[3,1,3,3],[1,1,2,2]])
print("2D Array \n",b) 
x=np.diag(a)
print("Diagonal elements of  1D array \n",x)
y=np.diag(b)
print("Diagonal elements of  2D array \n",y)

