# Programming Assignment-3: Digits

Due on 2019-08-22, 23:59 IST

You are given a number A which contains only digits 0's and 1's. Your task is to make all digits same by just flipping one digit (i.e. 0 to 1 or 1 to 0 ) only. If it is possible to make all the  digits same by just flipping one digit then print 'YES' else print 'NO'.

# Input Format:

The first line contains a number made up of 0's and 1's.

# Output Format:

Print 'YES' or 'NO' accordingly without quotes.

Example:

Input:

101

Output:
YES

Explanation:
If you flip the middle digit from 0 to 1 then all the digits will become same. Hence output is YES.

# Test Cases

| Test Cases 	| Input 	| Output 	|
|-------------	|-------	|--------	|
| Test Case 1 	| 10 	| YES 	|
| Test Case 2 	| 1011 	| YES 	|
| Test Case 3 	| 0011 	| NO 	|


# Solution


Count number or zeros and ones
if either of them is 1 return YES else return NO
