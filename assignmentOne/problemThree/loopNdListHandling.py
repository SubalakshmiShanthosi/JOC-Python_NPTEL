import sys
def reverseArr(lst):
    new_lst = lst[::-1]
    return new_lst



noOfEle=input()

array_Nos = list(map(int,input().split()))

rev_Array=reverseArr(array_Nos)

result=[]

for arrEle,revEle in zip(array_Nos,rev_Array):
	result.append(arrEle+revEle)

print(*result,end='')
