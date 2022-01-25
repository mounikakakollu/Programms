'''
Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].Input : arr[] = {10, 20, 80, 30, 60, 50,
                     110, 100, 130, 170}
          x = 110;
Output : 6
Element x is present at index 6

Input : arr[] = {10, 20, 80, 30, 60, 50,
                     110, 100, 130, 170}
           x = 175;
Output : -1
Element x is not present in arr[].
'''

def LinearSearch(arr, ele):
    for i in arr:
        if(i == ele):
            return True
    return False

arr = [10, 20, 80, 30, 60, 50,110, 100, 130, 170]
ele = 170
print(LinearSearch(arr, ele))