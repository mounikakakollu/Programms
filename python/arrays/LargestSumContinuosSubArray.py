'''Kadane's Algorithm
Given an array Arr[] of N integers.
Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.
'''

def kadanesAlgo(array):
    i = 0;
    maxSum = array[0]
    currSum = 0
    start = 0
    end = 0
    for i in range(len(array)):
        if(currSum+array[i] > array[i]):
            currSum+=array[i]
        else:
            currSum = array[i]
            start = i
        if(maxSum < currSum):
            maxSum = currSum
            end = i
    print(array[start:end+1])
    return maxSum
if __name__ == '__main__':
    array = [1,2,3,-2,5]
    print(kadanesAlgo(array))
