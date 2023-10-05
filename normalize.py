import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

img = cv2.imread('PDR2.jpg')

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow

lower = np.array([60,60,60])
upper = np.array([250,250,250])

mask = cv2.inRange(img,lower,upper)

plt.imshow(mask,'gray')