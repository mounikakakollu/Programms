'''
Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum.
If there is a set S with n elements, then if we assume Subset1 has m elements,
Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.

Input:  arr[] = {1, 6, 11, 5}
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12
Subset2 = {11}, sum of Subset2 = 11
'''

a = [3, 1, 4, 2, 2, 1]
a.sort()
totalSum = 0
for i in a:
    totalSum +=i
curSum = 0
minDiff = totalSum
subset = []
print(a)
for i in a:
    curSum +=i
    rem = totalSum - curSum
    # print(abs(curSum - rem), minDiff, end = " ")
    if(abs(curSum - rem) < minDiff):
        minDiff = abs(curSum - rem)
        # print(i, minDiff)
        subset.append(i)
print(minDiff)

