'''
Longest consecutive subsequence

Given an array of positive integers.
Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers,
the consecutive numbers can be in any order.

Input:
N = 7
a[] = {2,6,1,9,4,5,3}
Output:
6
Explanation:
The consecutive numbers here
are 1, 2, 3, 4, 5, 6. These 6
numbers form the longest consecutive
subsquence.
'''

class LongestConsecutiveSubSequence:
    def findLongestConsecutiveSubSequence(self, arr):
        arr.sort()
        print(arr)
        maxSubSequence = 1
        currSubSequence = 1
        for i in range(1,len(arr)):
            if(arr[i] == arr[i-1]):
                continue;
            elif(arr[i]-1 == arr[i-1]):
                currSubSequence += 1
            else:
                currSubSequence = 1
            if(maxSubSequence < currSubSequence):
                maxSubSequence = currSubSequence
        return maxSubSequence

if __name__ == '__main__':
    # arr = [2,6,1,9,4,5,3]
    arr = [6, 6, 2, 3, 1, 4, 1, 5, 6, 2, 8, 7, 4, 2, 1, 3, 4, 5, 9, 6]
    obj = LongestConsecutiveSubSequence()
    print(obj.findLongestConsecutiveSubSequence(arr))
