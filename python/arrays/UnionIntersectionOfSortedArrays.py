'''
Find the Union and Intersection of the two sorted arrays.
'''
def Intersection(ar1, ar2):
    intersection = []
    i = 0;
    j =0
    while(i< len(ar1) and j<len(ar2)):
        if(ar1[i] == ar2[j]):
            intersection.append(ar1[i])
            i+=1
            j+=1
        elif(ar1[i]<ar2[j]):
            i+=1
        else:
            j+=1
    return intersection

def Union(ar1, ar2):
    union = []
    i = 0;
    j = 0;
    while (i < len(ar1) and j < len(ar2)):
        if(ar1[i] == ar2[j]):
            union.append(ar1[i])
            i+=1
            j+=1
        elif(ar1[i] < ar2[j]):
            union.append(ar1[i])
            i+=1
        else:
            union.append(ar2[j])
            j+=1
    while(i<len(ar1)):
        union.append(ar1[i])
        i+=1
    while(j<len(ar2)):
        union.append(ar2[j])
        j+=1
    return union


arr1 = [1,2,3,4,5,6]
arr2 = [2,4,6,7,8]

print("Union : ", Union(arr1, arr2))

print("Intersection : ", Intersection(arr1, arr2))