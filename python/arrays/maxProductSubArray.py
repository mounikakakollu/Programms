'''
Find maximum product subArray
'''

class maxProductSubArray:
    def findMaxProductSubArray(self,arr):
        maxValue = arr[0]
        minValue = arr[0]
        maxProd = arr[0]
        for i in range(1, len(arr),1):
            if(arr[i]<0):
                maxValue, minValue = minValue, maxValue
            if(maxValue * arr[i] > arr[i]):
                maxValue *=arr[i]
            else:
                maxValue = arr[i]
            if(minValue * arr[i] < arr[i]):
                minValue *=arr[i]
            else:
                minValue = arr[i]
            if(maxProd < maxValue):
                maxProd = maxValue
        return maxProd



if __name__ == '__main__':
    # array = [6, -3, -10, 0, 2]
    # array = [2, 3, 4, 5, -1, 0]
    obj = maxProductSubArray()
    array = [9, 0, 8, -1, -2 ,-2, 6]
    print(obj.findMaxProductSubArray(array))

