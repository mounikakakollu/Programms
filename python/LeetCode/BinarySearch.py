'''
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''

def search( nums, target, start, end) -> int:
    mid = int((start + end) / 2)
    if(start > end):
        return -1
    if (nums[mid] == target):
        return mid
    elif (nums[mid] > target):
        return search(nums, target, start, mid-1)
    else:
        return search(nums, target, mid+1, end)
arr = [-1,0,3,5,9,12]
print(search(arr, 10, 0, len(arr)-1))