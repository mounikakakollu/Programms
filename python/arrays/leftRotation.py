'''
Write a program to cyclically rotate an array by one.
Left rotation by one using reversal algorithm
'''
def reverse(array, start, end):
    while(start< end):
        array[start], array[end] = array[end], array[start]
        start+=1
        end-=1
def leftRotation(array, k):
    reverse(array, 0, len(array)-1)
    reverse(array, 0, k-1)
    reverse(array, k, len(array)-1)
array = [1,2,3,4,5]
leftRotation(array, 1)
print(array)