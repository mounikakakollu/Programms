'''

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.


'''

def RepeatedNum(array):
    n = len(array)-1
    totalSum = n*(n+1)/2
    currArraySum = sum(array)
    return int(currArraySum-totalSum)

if __name__=='__main__':
    array = [1,2,3,4,4,5,6,7,8]
    print(RepeatedNum(array))