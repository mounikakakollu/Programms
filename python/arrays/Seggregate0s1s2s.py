'''
Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
'''

def arraySeggregation(array, ele, start, end):

    while (start < end):
        while (array[start] == ele):
            start += 1
        while (array[end] != ele):
            end -= 1
        if (start < end):
            array[start], array[end] = array[end], array[start]
    return start

array = [1,2,0,2,0,1,2,0,1,1,2,0]
index = arraySeggregation(array, 0, 0,len(array)-1)
arraySeggregation(array, 1, index, len(array)-1)
print(array)