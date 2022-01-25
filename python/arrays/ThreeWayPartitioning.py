'''
Given an array of size n and a range [a, b]. The task is to partition the array around the range such that array is divided into three parts.
1) All elements smaller than a come first.
2) All elements in range a to b come next.
3) All elements greater than b appear in the end.
The individual elements of three sets can appear in any order. You are required to return the modified array.

n = 5
A[] = {1, 2, 3, 3, 4}
[a, b] = [1, 2]
Output: 1
Explanation: One possible arrangement is:
{1, 2, 3, 3, 4}. If you return a valid
arrangement, output will be 1.

Input:
n = 3
A[] = {1, 2, 3}
[a, b] = [1, 3]
Output: 1
Explanation: One possible arrangement
is: {1, 2, 3}. If you return a valid
arrangement, output will be 1.
'''

class ThreeWayPartitioning:
    def threeWayPartitioning(self, array, range):
        start = range[0]
        end = range[1]
        i = 0
        currIndex = 0
        while(i<len(array)):
            while(i < len(array) and array[i]< start):
                i += 1
            j = i+1
            while(j < len(array) and array[j] > start):
                j += 1
            if(i < len(array) and j<len(array)):
                array[i], array[j] = array[j], array[i]
                currIndex = i
                i+=1
                j+=1
            i+=1
        i = currIndex
        while(i< len(array)):
            while(i< len(array) and array[i] > start and array[i] < end ):
                i +=1
            j = i+1
            while(j< len(array) and array[i] <= end):
                j +=1
            if( i< len(array) and j< len(array)):
                array[i], array[j] = array[j], array[i]
                currIndex = i
                i +=1
                j +=1
            i +=1
        i = currIndex

        print(array)


if __name__ == '__main__':
    array = [1, 2, 4,3,3]
    obj = ThreeWayPartitioning()
    print(obj.threeWayPartitioning(array, [1,3]))