# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:36:13 2020

@author: ADMIN
"""
"""
Amit Caspi
"""

import numpy as np


def NewFilter():
    filt=np.random.rand(3,3)
    for row in range(filt.shape[0]):
        for column in range (filt.shape[1]):
             filt[row][column] = (filt[row][column])*5
    return filt


def MultiplyFunction (newMatrix,filt):
    res=np.zeros((newMatrix.shape[0]-2, newMatrix.shape[1]-2)) 
    for row in range(res.shape[0]):
        for column in range (res.shape[1]):
            filt2=np.array(newMatrix[row:row+3,column:column+3]) 
            res[row][column]=SumTheResults(np.dot(filt2,filt)) 
    print(res)
    return res


def SumTheResults(mul):
    matSum=0
    for ro in range (mul.shape[0]):
        for co in range (mul.shape[1]):
            matSum += mul[ro][co]
    return matSum


def RepeatTilEnd(newMatrix):
    filt= NewFilter()
    while(newMatrix.shape[0]>=filt.shape[0] and newMatrix.shape[1]>=filt.shape[1]):
        newMatrix=MultiplyFunction(newMatrix,filt)
        filt=NewFilter()
    return newMatrix
    

def main():
    filt=NewFilter()
    bigArray= np.array([[4, 0, 2, 1, 3, 2, 1.25, 4.5], [1.65, 3.245, 4, 2.89, 0.11, 3, 4, 1],
                       [1.78, 4, 0.2564, 2.8789, 0.24, 1.4, 4.23, 4], [1, 4.23, 1.45, 3.23, 2.56, 4.2, 1.2, 0], 
                       [4.2001, 3.25, 2, 2.78965, 0, 0.125, 4.352, 1], [0.1456, 2.256, 4, 3, 1, 0.25, 1.25663, 4.99],
                       [3.256, 4.25, 1.36, 3.2563, 4, 2.365, 3.256, 2.745], [1, 2.56, 2.789, 3, 0, 4.6359, 1.554845, 1]]) 
    res=MultiplyFunction(bigArray,filt)
    res=RepeatTilEnd(res)   
    print("The final result:")
    print(res)


if __name__ == '__main__':
    main()
