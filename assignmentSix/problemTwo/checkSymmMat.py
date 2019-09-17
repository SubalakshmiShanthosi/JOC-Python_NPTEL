# @Author: subalakshmi
# @Date:   2019-09-17T14:02:30+05:30
# @Last modified by:   subalakshmi
# @Last modified time: 2019-09-17T14:08:48+05:30

def checkIfSymmMatrix(aMatrix,sqMatSize):
    for i in range(0,sqMatSize):
        for j in range(0,sqMatSize):
            if aMatrix[i][j]!=aMatrix[j][i]:
                return "NO"
    return "YES"




sqMatSize=int(input())
sqMatrix = []
# Filling squareMatrix with zeros
for i in range(0,sqMatSize):
    sqMatrix.append([])
    for j in range(0,sqMatSize):
        sqMatrix[i].append(0)

# Accepting values of square matrix
for i in range(sqMatSize):
    sqMatrix[i]=input().split(" ")
# Check if given square matrix is symmetric or not
print(checkIfSymmMatrix(sqMatrix,sqMatSize),end='')
