'''
Given a 3 x n board, find the number of ways to fill it with 2 x 1 dominoes.
Example 1
Following are all the 3 possible ways to fill up a 3 x 2 board.
'''
n = 3
a = [0]*(n+1)
b = [0]*(n+1)
for i in range(n)