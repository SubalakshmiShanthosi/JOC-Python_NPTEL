# @Author: subalakshmi
# @Date:   2019-09-17T12:35:49+05:30
# @Last modified by:   subalakshmi
# @Last modified time: 2019-09-17T13:55:13+05:30


def lowerTrianMat(matrix,sqMatSize):
    for i in range(0, sqMatSize):

        for j in range(0, sqMatSize):

            if (i < j and j!=sqMatSize-1):

                print("0",end=" ");

            elif (i < j and j== sqMatSize-1):
              	print("0",end='');

            else:
                print(int(matrix[i][j]),end=" ");

        if (i!=sqMatSize-1):
        	print();




sqMatSize=int(input())
sqMatrix = []
# Initialising sqMatrix with all zeros (N*N)
for i in range(0,sqMatSize):
    sqMatrix.append([])
    for j in range(0,sqMatSize):
        sqMatrix[i].append(0)

# Accepting entries of matrix
for i in range(sqMatSize):
    # A for loop for getting row entries
    sqMatrix[i]=input().split(" ")

lowerTrianMat(sqMatrix,sqMatSize)
