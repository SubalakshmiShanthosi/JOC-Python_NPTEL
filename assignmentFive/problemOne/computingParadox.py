# empty list to hold array elements
inpArr = []

# number of elements in array
n = int(input())

# Accept playlist  elements one by one

playlist = [int(i) for i in input().split()]


# Sort playlist

sortPlaceholder=sorted(playlist)

# Accept the value of k - computing Paradox

k=int(input())


# Find the fav playlist at a particular index
paradoxElement = playlist[k-1]

if paradoxElement in sortPlaceholder:
    index=sortPlaceholder.index(paradoxElement)+1
    print(index,end='')
