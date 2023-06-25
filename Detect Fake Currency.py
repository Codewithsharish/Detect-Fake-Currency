import cv2
import os
import numpy as np
import pickle

img = cv2.imread(r"C:\Users\Saurabh Kadam\PycharmProjects\pythonProject2\FakeCurrency\2000front.jpeg")  
img1 = cv2.imread(r"C:\Users\Saurabh Kadam\PycharmProjects\pythonProject2\FakeCurrency\2000back.jpeg")

res1 = cv2.resize(img, (800, 300))  
res2 = cv2.resize(img1, (800, 300))  
image = np.concatenate((res1, res2), axis=0)  
img_median = cv2.medianBlur(image, 3)  
gray = cv2.cvtColor(img_median, cv2.COLOR_BGR2GRAY)  
edges = cv2.Canny(gray, 60, 180)  
th2 = cv2.adaptiveThreshold(edges, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 10)             
cv2.imshow('original image', image)  
cv2.imshow('noise filtered', img_median)   
cv2.imshow('gray scale', gray)  
cv2.imshow('edge detected', edges)  
cv2.imshow('segmented', th2)  
cv2.waitKey(0)        
cv2.destroyAllWindows()  

outfile = open('saved', 'wb')
pickle.dump(th2, outfile)
outfile.close()
