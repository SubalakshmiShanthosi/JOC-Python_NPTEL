def printDict():

  # Accept a positive integer n
	n=int(input())
  # Dictionary with value for each key x between 1 and n as x^2
	dict= {x: x**2 for x in range(1,n+1)}
	print(dict,end='')

# Invoke user defined function

printDict()
