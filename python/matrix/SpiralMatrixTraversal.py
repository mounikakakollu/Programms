'''
Spiral Matrix traversal

'''

class SpiralMatrixTraversal:
    def traversal(self, matrix):
        # columnSize = len(matrix[0]) -1
        # rowSize = len(matrix) -1
        # row = 0
        # col = 0
        # r = rowSize
        # c= columnSize
        # while(row<=rowSize and col <= columnSize):
        #
        #     print(matrix[row][col:columnSize+1]) # 00 01 02 03 04 05 06 07
        #     row+=1
        #
        #     print(list(zip(*matrix))[columnSize][row:rowSize+1])
        #     columnSize-=1
        #     if(row<=rowSize and r%2 == 0):
        #         print((matrix[rowSize][col:columnSize+1])[::-1])
        #         rowSize-=1
        #     if (col <= columnSize and c % 2 == 0):
        #         print((list(zip(*matrix))[col][row:rowSize+1])[::-1])
        #         col += 1

        row = 0
        col = 0
        rowSize = len(matrix) -1
        colSize = len(matrix[0]) -1
        r = rowSize
        c= colSize
        result = []
        while (row <= rowSize and col <= colSize):
            result += matrix[row][col:colSize + 1]
            row += 1
            result += list(zip(*matrix))[colSize][row:rowSize + 1]
            colSize -= 1
            if (row <= rowSize and r % 2 == 0):
                result += (matrix[rowSize][col:colSize + 1])[::-1]
                rowSize -= 1
            if (col <= colSize and c % 2 == 0):
                result += (list(zip(*matrix))[col][row:rowSize + 1])[::-1]
                col += 1
        print(result)
        return result

if __name__ == '__main__':
    obj = SpiralMatrixTraversal()
    # matrix = [
    #     [00,1,2,3,4,5,6,7],
    #     [10,11,12,13,14,15,16,17],
    #     [20,21,22,23,24,25,26,27],
    #     [30,31,32,33,34,35,36,37],
    #     [40,41,42,43,44,45,46,47],
    #     [50,51,52,53,54,55,56,57]
    #     ]

    matrix = [
        [6,6,2,28,2],
        [12,26,3,28,7],
        [22,25,3,4,23]
    ]

    # matrix = [
    #     [5,11,30],
    #     [5,19,19]
    # ]
    obj.traversal(matrix)