'''
In this challenge, you will be given an array  and must determine an array . There is a special rule: For all , .
That is,  can be any number you choose such that . Your task is to select a series of  given  such that
the sum of the absolute difference of consecutive pairs of  is maximized. This will be the array's cost, and
will be represented by the variable  below.


For example, if the array B = [1,2,3], we know that 1<=A[0]<=1,1<=A[1]<=2 ,1<=A[2]<=3 and . Arrays meeting those guidelines are:

[1,1,1], [1,1,2], [1,1,3]
[1,2,1], [1,2,2], [1,2,3]
Our calculations for the arrays are as follows:

|1-1| + |1-1| = 0	|1-1| + |2-1| = 1	|1-1| + |3-1| = 2
|2-1| + |1-2| = 2	|2-1| + |2-2| = 1	|2-1| + |3-2| = 2
'''

def cost(B):
    # Write your code here
    a = b=0
    for i in range(1, len(B)):
        newA = max((abs(B[i] - B[i-1])+a), (abs(B[i] - 1)+b))
        newB = max(abs(B[i-1] - 1)+a, b)
        a = newA
        b = newB
    return max(a, b)

# B = [69,19,15,81,93,100,35,18,81,16,65,20,4,45,81,83,90,14,82,85,43,7,64,76,33,47,95,12,78,93,14,22,97,36,65,66,36,26,59,81,81,82,44,79,89,94,32,94,22,33,19,46,46,62,19,47,70,91,97,62,17,43,11,25,74,73,64,98,73,7,40,8,2,96,89,81,80,17,88,13,31,44,64]
B = [52,60,50,90,84,35,56,64,52,20,43,19,12,73,48,93,43,78,22,53,60,100,26,54,84]
print(cost(B))