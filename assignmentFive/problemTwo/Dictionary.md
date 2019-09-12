# Week 6  - Programming Assignment-2: Dictionary

Given a positive integer number n, you have to write a program that generates a dictionary d which contains (i, i*i*i) such that i is the key and i*i*i is its value, where i is from 1 to n (both included).
Then you have to just print this dictionary d.

Example:
Input: 4

will give output as
{1: 1, 2: 8, 3: 27, 4: 64}

# Input Format:
Take the number n in a single line.

# Output Format:
Print the dictionary d in a single line.


# Example:

Input:
8

Output:
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512}

# Explanation:

Here n is 8, we will start from i=1, hence the first element of the dictionary is (1: 1), as i becomes 2, the second element of the dictionary becomes (2: 8) and so on.
Hence the output will be {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512}.

# Test Cases

| Test Cases 	| Input 	| Output 	|
|-------------	|-------	|------------------------------------	|
| Test Case 1 	| 3 	| {1: 1, 2: 8, 3: 27} 	|
| Test Case 2 	| 4 	| {1: 1, 2: 8, 3: 27, 4: 64} 	|
| Test Case 3 	| 5 	| {1: 1, 2: 8, 3: 27, 4: 64, 5: 125} 	|
