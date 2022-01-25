'''
Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower
either by increasing or decreasing them by K only once. After modifying, height should be a non-negative integer.
Find out what could be the possible minimum difference of the height of shortest and longest towers after you have modified each tower.
'''

def MinimizeHeightDiff(array, k):
    if(len(array) <=1):
        return 0
    array.sort()
    diff = array[len(array)-1] - array[0]
    min = array[0]+k
    max = array[len(array)-1]-k
    if(min>max):
        min, max = max, min
    print(array)
    for i in range(1, len(array)-1, 1):
        currEleSum = array[i] + k
        currEleDiff = array[i] -k
        # print(currEleSum, currEleDiff)
        if(currEleSum<= max or currEleDiff >=min):
            continue;
        if(currEleSum-min<= max-currEleDiff):
            # print(currEleSum-min)
            max = currEleSum
        elif(currEleDiff>=0):
            min = currEleDiff
        print(max, min, array[i])
    # print(max, min)
    if(max-min <= diff):
        return max-min
    else:
        return diff

if __name__ == '__main__':
    k = 2
    # array = [6 ,1 ,9 ,1 ,1 ,7 ,9 ,5, 2, 10]
    array = [1, 2, 3]
    # array = [2 ,6 ,3 ,4 ,7 ,2 ,10 ,3 ,2 ,1]
    print(MinimizeHeightDiff(array, k))