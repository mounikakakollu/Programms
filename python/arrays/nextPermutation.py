'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.
Input: nums = [1,2,3]
Output: [1,3,2]
Input: nums = [3,2,1]
Output: [1,2,3]
'''

def nextpermutationNum(array):
    for i in range(len(array)-1, 0, -1):
        if(array[i] >= array[i-1]):
            minn = i
            for j in range(i+1, len(array),1):
                if(array[minn] > array[j] and array[i-1]<array[j]):
                    minn = j
            array[i-1], array[minn] = array[minn], array[i-1]
            array[i:] = sorted(array[i:])
            return array
    array.sort()
    return array


if __name__ == '__main__':
    # array = [1,2,3]
    array = [1,4,3,2]
    print(nextpermutationNum(array))