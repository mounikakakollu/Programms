'''
Given an array of integers. Find the Inversion Count in the array.

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted.
If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order
then the inversion count is the maximum.
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5
has three inversions (2, 1), (4, 1), (4, 3).
'''

def search(ele, array, start, end):
    if(start>end):
        return -1
    mid = int((start+end)/2)
    if(array[mid] == ele):

        return mid
    elif(array[mid]< ele):
        return search(ele, array, mid+1, end)
    else:
        return search(ele, array, start, mid-1)

def countInversions(array):
    count = 0
    tmp = sorted(array)
    inversionsCount = 0
    i=0
    if (array == tmp):
        return 0
    elif (array == tmp[::-1]):
        return int((len(tmp) * (len(tmp) - 1)) / 2)
    while(i<len(array)):
        # index = search(array[i], tmp, 0, len(tmp))
        index = tmp.index(array[i])
        array.remove(array[i])
        if(index >=0):
            del tmp[index]
            inversionsCount +=index

    return inversionsCount

def countInversionsBruteForce(array):
    inversionsCount = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if(array[i]>array[j]):
                inversionsCount+=1
        print( inversionsCount, array[i])
    return inversionsCount


if __name__ == '__main__':
    # array = [6,5,4,3,2,1] #[1,3,5]
    array = [2,4,1,3,5]
    # array = [468, 335, 1, 170, 225, 479, 359, 463, 465, 206, 146, 282, 328, 462, 492, 496, 443, 328, 437, 392, 105, 403, 154, 293, 383, 422, 217, 219, 396, 448, 227, 272, 39, 370, 413, 168, 300, 36, 395, 204, 312, 323]
    print(countInversions(array))
    # print(countInversionsBruteForce(array))