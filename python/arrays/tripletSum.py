'''
Find the triplet that sum to a given value
'''

class tripletSum:

    def findTripletSum(self, array, x):
        array.sort()
        print(array)
        for i in range(len(array)):
            k = i+1;
            j = len(array) - 1
            while(k<j):
                if(array[i] + array[k] + array[j] == x):
                    print(i, array[k], array[j])
                    return True
                elif(array[k] + array[j] < x-array[i]):
                    k+=1
                else:
                    j-=1
        return False



if __name__ == '__main__':
    obj = tripletSum();
    x = 182
    # array = [1, 4 ,45, 6, 10, 8] #[1,4,6,8,10,45]
    # array = [557, 217, 627, 358, 527, 358, 338, 272, 870, 362, 897, 23, 618, 113, 718, 697, 586, 42, 424, 130, 230, 566, 560, 933]
    array = [589, 343, 609, 61 ,222, 759, 955, 889, 147, 691, 950, 844, 431, 621, 749, 68, 537 ,784, 36, 227, 186, 39, 854, 630, 225, 749, 924, 360, 258, 767, 945, 956, 319 ,727 ,412, 26, 356 ,2 ,550, 497, 585, 516, 965, 343, 76, 914, 143, 197, 949, 73]
    print(obj.findTripletSum(array, x))


