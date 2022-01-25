'''
Search an element in a matric which is sorted both rowwise and columnWise

'''

class Search:
    def findEle(self, matrix, ele):
        r = len(matrix)
        c = len(matrix[0])
        i = 0
        j = 0
        while(i<r and j<c):
            if(matrix[i][j] == ele):
                return True
            elif( matrix[i][c-1]< ele):
                i+=1
                j = 0
            else:
                j+=1
        return False

if __name__ == '__main__':
    # matrix = [
    #     [1, 3, 5, 7],
    #     [10, 11, 16, 20],
    #     [23, 30, 34, 60]
    # ]
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    ele = 13
    obj = Search()
    print(obj.findEle(matrix, ele))
