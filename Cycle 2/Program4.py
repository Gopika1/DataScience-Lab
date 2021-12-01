#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 11:30:01 2021

@author: sjcet
"""

import numpy as np

a = np.arange(1, 11, 1)
print("The original array : ",a)
print("First 4 elements")
first_element = a[:4]
print(first_element)
print("Last 6 elements")
first_element1 = a[5:]
print(first_element1)
print("Elements from index 2 to 7")
first_element2 = a[1:7]
print(first_element2)