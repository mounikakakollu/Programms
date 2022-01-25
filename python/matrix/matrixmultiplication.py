'''
Given two matrices, we need to multiply them
'''

class MatrixMultiplication:
    def matrixMultiplication(self, m1, m2):
        c = []
        for i in range(len(m1)):
            c.append([0]*len(m2[0]))
        for i in range(len(m1)):
            for col in range(len(m2[0])):
                for j in range(len(m1[i])):
                    c[i][col] +=m1[i][j] * m2[j][i]
                print()
        print(c)

if __name__ == '__main__':
    obj = MatrixMultiplication()
    m1 = [[1,2],[3,4]]
    m2 = [[5,6,7],[8,9,10]]
    obj.matrixMultiplication(m1,m2)

