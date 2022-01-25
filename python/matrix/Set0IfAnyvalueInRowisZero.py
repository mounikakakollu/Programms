class Set0IfAnyValueInRowisZeor:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        isCol = False
        for i in range(len(A)):
            if(A[i][0] == 0):
                isCol = True
            for j in range(1, len(A[i])):
                if(A[i][j] == 0):
                    A[i][0] = 0
                    A[0][j] = 0
        for i in range(1,len(A)):
            for j in range(1,len(A[i])):
                if(A[i][0] ==0 or A[0][j] == 0):
                    A[i][j] = 0
        if(A[0][0] == 0):
            for j in range(1, len(A[0])):
                A[0][j] = 0;
        if(isCol):
            for i in range(1, len(A)):
                A[i][0] = 0
        return A



A = [[1,0,1,1],[0,1,1,1],[1,1,1,1],[1,1,0,1]]
obj = Set0IfAnyValueInRowisZeor()
print(obj.setZeroes(A))