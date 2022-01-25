'''
Smallest subArray with sum grater then the given value (Minimum length subarray with sum greater than give value)
arr[] = {1, 4, 45, 6, 0, 19}
   x  =  51
Output: 3
Minimum length subarray is {4, 45, 6}

arr[] = {1, 10, 5, 2, 7}
   x  = 9
Output: 1
Minimum length subarray is {10}

arr[] = {1, 11, 100, 1, 0, 200, 3, 2, 1, 250}
    x = 280
Output: 4
Minimum length subarray is {100, 1, 0, 200}

arr[] = {1, 2, 4}
    x = 8
Output : Not Possible
Whole array sum is smaller than 8.
'''

class SmallestSubArray:
    def findSmallestSubArray(self, array, x):
        subArray = []
        array.sort()
        subArraySum = 0
        n = len(array)
        i = n-1
        while(i>=0):
            if(subArraySum > x):
                return subArray
            if(subArraySum + array[i] <= x):
                print(array[i] , end = " ")
                subArray.append(array[i])
                subArraySum += array[i]
            i-=1
        i = 0
        while(i<n):
            if(subArray[-1] != array[i] and subArraySum + array[i] > x):
                subArray[-1] = array[i]
                return subArray
            else:
                i+=1

if __name__ == '__main__':
    array = [1, 4, 45, 6, 0, 19]
    x = 51
    obj = SmallestSubArray()
    print(obj.findSmallestSubArray(array, x))