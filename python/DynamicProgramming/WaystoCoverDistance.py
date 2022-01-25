'''
Given a distance ‘dist’, count total number of ways to cover the distance with 1, 2 and 3 steps.

Input: n = 3
Output: 4
Explanation:
Below are the four ways
 1 step + 1 step + 1 step
 1 step + 2 step
 2 step + 1 step
 3 step

Input: n = 4
Output: 7
'''

def findWays(dist, memory={}):
    if(dist<0):
        return 0
    if dist in memory:
        return memory[dist]
    if(dist == 0):
        return 1
    tmp = findWays(dist-1)
    memory[dist] = tmp
    tmp += findWays(dist-2)
    memory[dist] = tmp
    tmp += findWays(dist-3)
    memory[dist] = tmp
    return tmp
n = 4

print(findWays(n))
