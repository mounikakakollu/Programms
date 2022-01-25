'''
Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to .

Example


There are two subarrays meeting the criterion:  and . The maximum length subarray has  elements.
'''

def pickingNumbers(a):
    a.sort()
    i = 0
    maxLen = 0
    while(i< len(a)):
        j = i+1
        count = 1
        print(a[j], j)
        while(j<len(a)):
            if(a[i] == a[j] or a[i]+1 == a[j]):
                count+=1
                j+=1
            else:
                break
        if (maxLen < count):
            maxLen = count
        i = j
    return maxLen

a = [66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66]
print(pickingNumbers(a))