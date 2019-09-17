# @Author: subalakshmi
# @Date:   2019-09-17T14:18:28+05:30
# @Last modified by:   subalakshmi
# @Last modified time: 2019-09-17T14:30:52+05:30

def checkIfBinaryMatrix(aMatrix,noOfRows,noOfColumns):
    for i in range(0,noOfRows):
        for j in range(0,noOfRows):
            if int(aMatrix[i][j])>1 or int(aMatrix[i][j])<0:
                return "NO"
    return "YES"




noOfRows,noOfColumns=input().split(" ")
noOfRows=int(noOfRows)
noOfColumns=int(noOfColumns)
aMatrix=[]
# Fill a N*M matrix with zeros
for i in range(0,noOfRows):
    aMatrix.append([])
    for j in range(0,noOfColumns):
        aMatrix[i].append(0)

# Accepting entries of N*M matrix

for i in range(0,noOfRows):
    aMatrix[i]=input().split(" ")

print(checkIfBinaryMatrix(aMatrix,noOfRows,noOfColumns),end='')
