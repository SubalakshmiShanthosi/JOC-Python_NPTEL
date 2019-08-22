import heapq

array_Nos = list(map(int,input().split()))

secondLargest = heapq.nlargest(2,array_Nos)

secondSmallest = heapq.nsmallest(2,array_Nos)

print(str(secondLargest[1])+" "+str(secondSmallest[1]),end='')
