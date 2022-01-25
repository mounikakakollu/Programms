'''
Count pairs with given sum
Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.

Input:
N = 4, K = 6
arr[] = {1, 5, 7, 1}
Output: 2
Explanation:
arr[0] + arr[1] = 1 + 5 = 6
and arr[1] + arr[3] = 5 + 1 = 6.

Input:
N = 4, X = 2
arr[] = {1, 1, 1, 1}
Output: 6
Explanation:
Each 1 will produce sum 2 with any 1.
'''

class PariWithSum:
    def countParisWithGivenSum(self, array, k):
        array.sort()
        pairs = []
        print(array)
        i = 0;
        j = len(array)-1
        while(i<j):
            if(array[i]+array[j] == k):
                pairs.append([array[i], array[j]])
                tmp = j-1;
                while(tmp>i):
                    if(array[tmp]+array[i] == k):
                        pairs.append([array[tmp], array[i]])
                    tmp-=1
                i+=1
            elif(array[i]+array[j]<k):
                i+=1
            else:
                j-=1
        print(pairs)
        return len(pairs)

if __name__ == '__main__':
    array = [1,5,7,1] #[1,1,5,7]
    k = 6
    # array = [1,1,1,1]
    obj = PariWithSum()
    # array = [48, 24, 99, 51, 33, 39, 29, 83, 74, 72, 22, 46, 40, 51, 67, 37, 78, 76, 26, 28, 76, 25, 10, 65, 64, 47, 34, 88, 26, 49, 86, 73, 73, 36, 75, 5, 26, 4, 39, 99, 27, 12, 97, 67, 63, 15, 3 ,92, 90]

    print(obj.countParisWithGivenSum(array, k))