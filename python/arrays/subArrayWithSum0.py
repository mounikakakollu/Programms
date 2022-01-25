'''
find if there is any subarray with sum equal to 0
'''

class subArrayWIthSum0:
    def subArrayWithSum0(self, arr):
        arr.sort()
        i = 0;
        j = len(arr)-1
        while(i<j):
            if(arr[i]+arr[j] == 0):
                return True
            elif(arr[i]+arr[j] <0):
                i+=1
            else:
                j-=1
        return False

if __name__ == '__main__':
    array = [-5,1,2,3,4,5,6,7]
    # array = [48, 24, 99, 51, 33, 39, 29, 83, 74, 72, 22, 46, 40, 51, 67, 37, 78, 76, 26, 28, 76, 25, 10, 65, 64, 47, 34, 88, 26, 49, 86, 73, 73, 36, 75, 5, 26, 4, 39, 99, 27, 12, 97, 67, 63, 15, 3 ,92, 90]
    obj = subArrayWIthSum0()
    print(obj.subArrayWithSum0(array))