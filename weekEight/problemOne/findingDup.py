# @Author: subalakshmi
# @Date:   2019-09-25T20:45:51+05:30
# @Last modified by:   subalakshmi
# @Last modified time: 2019-09-25T20:45:53+05:30

def findDuplicates(aList):

  uniqueEleList=[]

  for aElement in aList:

      if aElement not in uniqueEleList:

          	uniqueEleList.append(aElement)

  return uniqueEleList



list_with_dup = [int(i) for i in input().split()]

uniqueList=findDuplicates(list_with_dup)

uniqueList = [str(a) for a in uniqueList]

print(" " . join(uniqueList),end=' ')
