import numpy as np
import cv2
I=cv2.imread("normal.tif",cv2.IMREAD_GRAYSCALE)
Hist=np.zeros(256,dtype=int)
w, h = I.shape
for v in range(h):
    for u in range(w):
        i = I[u, v]
        Hist[i] += 1
for i in range(256):
    print(i,':',Hist[i])

