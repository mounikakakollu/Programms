'''
Merge 2 sorted arrays without using Extra space.
'''

def merge(a1, a2):
    i = 0
    j = 0
    while(i<len(a1) and j<len(a2)):
        if(a1[i] <= a2[j]):
            i+=1
        else:
            a1.insert(i, a2[j])
            del a2[j]
    while(j<len(a2)):
        a1.append(a2[j])
        del a2[j]
    return a1

if __name__ == '__main__':
    ar1 = [1,3,5,7]
    ar2 = [0,2,6,8,9]

    print(merge(ar1, ar2))