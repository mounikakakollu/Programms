'''
Matrix Chain Multiplication
Given a sequence of matrices, find the most efficient way to multiply these matrices together.
The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications.
We have many options to multiply a chain of matrices because matrix multiplication is associative.
In other words, no matter how we parenthesize the product, the result will be the same.
For example, if we had four matrices A, B, C, and D, we would have:
(ABC)D = (AB)(CD) = A(BCD) = ....

Example
Input: p[] = {40, 20, 30, 10, 30}
Output: 26000
There are 4 matrices of dimensions 40x20, 20x30, 30x10 and 10x30.
Let the input 4 matrices be A, B, C and D.  The minimum number of
multiplications are obtained by putting parenthesis in following way
(A(BC))D --> 20*30*10 + 40*20*10 + 40*10*30

Input: p[] = {10, 20, 30, 40, 30}
Output: 30000
There are 4 matrices of dimensions 10x20, 20x30, 30x40 and 40x30.
Let the input 4 matrices be A, B, C and D.  The minimum number of
multiplications are obtained by putting parenthesis in following way
((AB)C)D --> 10*20*30 + 10*30*40 + 10*40*30

Input: p[] = {10, 20, 30}
Output: 6000
There are only two matrices of dimensions 10x20 and 20x30. So there
is only one way to multiply the matrices, cost of which is 10*20*30
'''
class MatrixChainMultiplication:
    def findMinNumofMultiplications(self, p,m, n, matrix, memory = {}):
        if(m == n):
            return 0
        key = str(m) + "*" + str(n)
        for k in range(m, n):
            if(key in memory):
                tmp = min(memory[key], self.findMinNumofMultiplications(p, m, k, memory)+self.findMinNumofMultiplications(p, k+1, n, memory) + p[m-1]*p[k]*p[n])
            else:
                tmp = self.findMinNumofMultiplications(p, m, k, memory)+self.findMinNumofMultiplications(p, k+1, n, memory) + p[m-1]*p[k]*p[n]

            memory[key] = tmp
        return memory[key]


    def MinNumofMultiplications(self, p):
        n = len(p)
        matrix = [[0 for _ in range(n+1)] for i in range(n+1)]
        return self.findMinNumofMultiplications(p, 1, n-1, matrix)



def isValidSubsequence(array, sequence):
    array.sort()
    sequence.sort()
    print(array, sequence)
    l1 = len(array)-1
    l2 = len(sequence)-1
    if(l2 > l1):
        return False
    if(array == sequence):
        return False
    while(l2>=0 and l1>=0):
        if(array[l1] == sequence[l2]):
            print(l1, l2)
            l1-=1
            l2-=1
        elif(array[l1]>sequence[l2]):
            l1-=1
        else:
            return False
    print(l1, l2)
    if(l1<0 and l2>=0) :
        return False
    return True


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [5, 1, 25, 22, 6, -1, 8, 10]
print(isValidSubsequence(array, sequence))

# if __name__ == "__main__":
#     p = [40, 20, 30, 10, 30]
#     obj = MatrixChainMultiplication()
#     print(obj.MinNumofMultiplications(p))
