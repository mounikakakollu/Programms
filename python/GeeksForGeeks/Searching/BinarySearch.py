'''
Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].
A simple approach is to do a linear search. The time complexity of the above algorithm is O(n).
Another approach to perform the same task is using Binary Search.
Binary Search: Search a sorted array by repeatedly dividing the search interval in half.
Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval,
narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.
'''

def BinarySearch(arr, start, end, ele):
    if(start >end):
        return False
    mid = int((start + end)/2)
    if(arr[mid] == ele):
        return True
    elif(arr[mid] > ele):
        return BinarySearch(arr, 0, mid-1, ele)
    else:
        return BinarySearch(arr, mid+1, end, ele)

arr = [2, 3, 4, 10, 40]
ele = 11
print(BinarySearch(arr, 0, len(arr)-1, ele))