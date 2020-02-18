"""
@author: Amit Caspi ya4
"""

import numpy as np

def mathmul (array1, array2):
    array3=np.zeros([array1.shape[0], array2.shape[1]], dtype = int)
    columns = array2.shape[1]
    lines = array1.shape[0]
    for line in range(lines): 
        for column in range(columns): 
           for numbers in range(array2.shape[0]): 
                array3[line][column] += array1[line][numbers] * array2[numbers][column]
    return array3

def AddMatrixMax(array1,array2):
    rows3=max(len(array1),len(array2))
    columns3=max(len(array1[0]),len(array2[0]))
    array3 = np.zeros([rows3, columns3], dtype = int)
    for index1 in range(len(array1)):
        for index2 in range(len(array1[0])):
            array3[index1,index2]=array1[index1,index2]
    for index1 in range(len(array2)):
        for index2 in range(len(array2[0])):
            array3[index1,index2]+=array2[index1,index2]  
    return(array3)


def AddMatrixMin(array1,array2):
    rows3=min(len(array1),len(array2))
    columns3=min(len(array1[0]),len(array2[0]))
    array3 = np.zeros([rows3, columns3], dtype = int)
    for index1 in range(rows3):
        for index2 in range(columns3):
            array3[index1,index2]=array1[index1,index2]+array2[index1,index2]
    return(array3)


def main():
     array1 = np.array([[5, 8, 7], [1, 2, 3]])
     print ("First matrix: \n" , array1)
     array2= np.array([[1, 2], [3, 4], [5, 6]])
     print ("Second matrix: \n" , array2)
     arrayMul=mathmul(array1,array2)
     print("multiplied matrix: \n", arrayMul)
     arrayMax = AddMatrixMax(array1,array2)
     print ("max matrix: \n", arrayMax )
     arrayMin = AddMatrixMin(array1,array2)
     print ("min matrix: \n", arrayMin )


if __name__ == '__main__':
    main()