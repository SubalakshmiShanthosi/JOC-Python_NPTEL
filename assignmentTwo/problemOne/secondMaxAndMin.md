# Programming Assignment-1: Max and Min

Due on 2019-08-22, 23:59 IST

Given a list of numbers (integers), find second maximum and second minimum in this list.

# Input Format:

The first line contains numbers separated by a space.

# Output Format:

Print second maximum and second minimum separated by a space

Example:

Input:

1 2 3 4 5

Output:

4 2

# Test Cases

| Test Cases 	| Input 	| Output 	|
|-------------	|----------------------	|--------	|
| Test Case 1 	| 2 3 4 5 6 	| 5 3 	|
| Test Case 2 	| 1 3 5 7 	| 5 3 	|
| Test Case 3 	| 10 11 4 1 6 7 2 9 	| 10 2 	|
| Test Case 4 	| 10 11 100 200 300 34 	| 200 11 	|

# Solution


Optimal : Using heapq methods

1. nthlargest(number,list)
2. nthsmallest(number,list)

Those functions return a List - first n largest or smallest number
Pick the last element in the list (here 2nd largest at index 1 of array[2] as number in method signature is 2)
