'''
The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence
such that all elements of the subsequence are sorted in increasing order.
For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.
'''

def findLongestSubSequence(arr):
    tmp = sorted(arr)
    print(tmp)
    n = len(arr)-1
    j = n
    count = 0
    while(n>=0):
        if(tmp[j] == arr[n]):
            count+=1
            print(arr[n], end=" ")
            n-=1
            j-=1
        elif(n > j):
            n-=1
        else:
            j-=1
    return count

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(findLongestSubSequence(arr))
