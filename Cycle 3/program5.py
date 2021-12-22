#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 11:49:56 2021

@author: sjcet
"""

import matplotlib.pyplot as plt
import numpy as np

plt.title("Students transportation")
plt.xlabel("Mode of Transport")
plt.ylabel("Frequency")



x = np.array(["walking","cycling","car","bus","train"])
y = np.array([29,15,35,18,3])

plt.bar(x, y, color = "#4CAF50",width = 0.1)
plt.show()