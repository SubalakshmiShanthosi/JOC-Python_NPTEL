list_Nos = list(map(int,input().split()))

is_notDivByFive = lambda x: x % 5 != 0


listNew=list(filter(is_notDivByFive, list_Nos))

print(*listNew,end='')
