'''
Given an array of size n and a number k, find all elements that appear more than n/k times

Given an array of size n, find all elements in array that appear more than n/k times. For example,
if the input arrays is {3, 1, 2, 2, 1, 2, 3, 3} and k is 4, then the output should be [2, 3]. Note that size of array is 8 (or n = 8),
so we need to find all elements that appear more than 2 (or 8/4) times. There are two elements that appear more than two times, 2 and 3.
'''

class frequency:
    def findFrequency(self, arr, k):
        count = 0
        freqCheck = int(len(arr)/k)
        arr.sort()
        i = 0;
        currCount = 0
        while(i<len(arr)):
            currCount = 0
            i+=1
            while(i<len(arr)):
                if(arr[i] == arr[i-1]):
                    currCount+=1
                    i+=1
                else:
                    break
            if(currCount >= freqCheck):
                count+=1
        return count

if __name__ == '__main__':
    arr = [3, 1, 2, 2, 1, 2, 3, 3]
    k = 4
    obj = frequency()
    print(obj.findFrequency(arr, k))
