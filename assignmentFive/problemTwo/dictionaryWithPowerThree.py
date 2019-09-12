# Accept a positive integer n
n=int(input())
dict= {x: x**3 for x in range(1,n+1)}
print(dict,end='')
