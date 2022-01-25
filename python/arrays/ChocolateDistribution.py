'''
Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet.
Each packet can have a variable number of chocolates. There are M students,
the task is to distribute chocolate packets among M students such that :
1. Each student gets exactly one packet.
2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum.

Input:
N = 8, M = 5
A = {3, 4, 1, 9, 56, 7, 9, 12}
Output: 6
Explanation: The minimum difference between
maximum chocolates and minimum chocolates
is 9 - 3 = 6 by choosing following M packets :
{3, 4, 9, 7, 9}.

Input:
N = 7, M = 3
A = {7, 3, 2, 4, 9, 12, 56}
Output: 2
Explanation: The minimum difference between
maximum chocolates and minimum chocolates
is 4 - 2 = 2 by choosing following M packets :
{3, 2, 4}.

Algorithm
1. Sort the array
2. traverse the array from 0 to i+m<len(array)
3. track minimum from array[n-i]-array[i] (subArray with size M and take diff of first and last ele)
4. Return minimum diff
'''

class ChololateDistribution:
    def findMinDiff(self, array, m):
        array.sort()
        n = len(array)
        if(n<m):
            return 0
        min = array[-1]
        min_index = 0 # will hold start index of the min diff
        i = 0;
        while(i+m <= n):
            print(i+m-1)
            if(array[i+m-1] - array[i] < min):
                min = array[i+m-1] - array[i]
                min_index = i
            i+=1
        print(array[min_index:min_index+m])
        return min

if __name__ == '__main__':
    m = 9
    # array = [3, 4, 1, 9, 56, 7, 9, 12]
    array = [17, 83, 59, 25, 38, 63, 25, 1, 37]
    obj = ChololateDistribution()
    print(obj.findMinDiff(array, m))

