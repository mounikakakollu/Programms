'''
find common elements In 3 sorted arrays
'''

class Unionin3Sortedarrays:
    def findUnion(self, a1, a2, a3):
        union = []
        i = 0
        j = 0
        k = 0
        while(i<len(a1) and j<len(a2) and k<len(a3)):
            if(a1[i] == a2[j] == a3[k]):
                if(a1[i] not in union):
                    union.append(a1[i])
                i+=1
                j+=1
                k+=1
            elif(a1[i]<=a2[j] and a1[i]<=a3[k]):
                i+=1
            elif(a2[j]<=a1[i] and a2[j]<=a3[k]):
                j+=1
            elif(a3[k]<=a1[i] and a3[k]<=a2[j]):
                k+=1
        if(len(union) ==0):
            return -1
        return union

if __name__ == '__main__':
    # a1 = [1,3,5,7,9]
    # a2 = [-1,0,1,3,4,6,8]
    # a3 = [0,1,2,3,4]
    a1 = [3,3,3]
    a2 = [3,3,3]
    a3 = [3,3,3]
    obj = Unionin3Sortedarrays()
    print(obj.findUnion(a1, a2, a3))