'''
Trapping Rain water problem

ALGORITHM WITH EXTRA SPACE
1. take two arrays left and right
2. Traverse from left and insert maximum element in ith position
3. Traverse from right and insert minimum element in the ith position
4. Traverse the given array and add min(left[i], right[i]) - array[i] to the result

ALGORITHM WITH out EXTRA SPACE
1. initialise left_max to the 0th ele and right_max to the n-1th ele
2. Consider two variables i = 0 and j = n-1
3. add max(left_max, array[i]) to the result if array[i]<array[j]
4. add max(right_max, array[j]) to the result if array[i]>array[j]
return result
'''

class TrappingRainWater:
    def trappingRainWaterWithExtraSpace(self, array):
        if(len(array)==0):
            return 0
        left = []
        right = []
        max = array[0]
        for i in array:
            if(i > max):
                max = i
            left.append(max)
        max = array[-1]
        for i in range(len(array)-1, -1, -1):
            if (array[i] > max):
                max = array[i]
            right.append(max)
        result = 0
        for i in range(len(array)):
            if(left[i] < right[i]):
                result += left[i] - array[i]
            else:
                result += right[i] - array[i]
        return result

    def trappingRainWater(self, array):
        if(len(array)==0):
            return 0
        left_max = array[0]
        right_max = array[-1]
        i = 0;
        j = len(array)-1
        result = 0
        while(i<j):
            if(array[i] < array[j]):
                if(left_max < array[i]):
                    left_max = array[i]
                result += left_max - array[i]
                i+=1
            else:
                if(right_max < array[j]):
                    right_max = array[j]
                result += right_max - array[j]
                j-=1
        return result;

if __name__ == '__main__':
    array = [3,0,0,2,0,4]
    obj = TrappingRainWater()
    print(obj.trappingRainWaterWithExtraSpace(array))
    print(obj.trappingRainWater(array))
