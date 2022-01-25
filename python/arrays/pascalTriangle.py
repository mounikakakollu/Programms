'''
Generate pascalTriangle
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
 1 5 10 10 5 1
'''

class pascalTriangle:
    def generatePascalTriangle(self, n):
        triangle = []
        startIndexes = []
        startIndex = 0
        startIndexes.append(0)
        triangle.append(1)
        for i in range(1,n+1,1):
            startIndexes.append(startIndexes[i-1] + i)
            startIndex = startIndexes[i-1]
            for j in range(i+1):
                if(j == 0 or j==i):
                    triangle.append(1)
                else:
                    triangle.append(triangle[startIndex] + triangle[startIndex-1])
                startIndex+=1
        self.printPascalTriangle(triangle,n)

    def printPascalTriangle(self, triangle, n):
        startIndex = 0;
        for i in range(n+1):
            print((n-i)*" ", end=' ')
            for j in range(i+1):
                print(triangle[startIndex],  end=' ')
                startIndex+=1
            print(" ")

if __name__ == '__main__':
    n = 5
    obj = pascalTriangle();
    obj.generatePascalTriangle(n)