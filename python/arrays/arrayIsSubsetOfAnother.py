'''
Array Subset of another array
Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m.
Task is to check whether a2[] is a subset of a1[] or not.
Both the arrays can be sorted or unsorted. It may be assumed that elements in both array are distinct.

Input:
a1[] = {11, 1, 13, 21, 3, 7}
a2[] = {11, 3, 7, 1}
Output:
Yes
Explanation:
a2[] is a subset of a1[]

Input:
a1[] = {1, 2, 3, 4, 5, 6}
a2[] = {1, 2, 4}
Output:
Yes
Explanation:
a2[] is a subset of a1[]
'''

class arrayIsSubsetOfAnother:
    def IsArrayisSubSetOfAnotherArray(self, a1, a2):
        if(len(a1)<len(a2)):
            return False
        a1.sort()
        a2.sort()
        i = 0;
        j = 0
        while(i<len(a1)):
            if(j>=len(a2)):
                return True
            if(a1[i] == a2[j]):
                i+=1
                j+=1
            else:
                i+=1
        if(j==len(a2)):
            return True
        else:
            return False

if __name__ == '__main__':
    a1 = [11,1,13,21,3,7]
    a2 = [11,3,7,12]
    obj = arrayIsSubsetOfAnother();
    print(obj.IsArrayisSubSetOfAnotherArray(a1,a2))