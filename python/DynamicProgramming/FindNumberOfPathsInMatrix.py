'''
Find number of paths are there in a grid to reach bottomRight from top left

means we need to read m*n th gird from 0*0 grid
'''

class FindNumberOfPathsInMatrix:
    def numberOfPaths(self,m,n, paths={}):
        if(m == 0 or n == 0):
            return 0
        if(m == 1 == n):
            return 1
        grid = str(m) + "*" + str(n)
        if(grid in paths):
            return paths[grid]
        paths[grid] = self.numberOfPaths(m-1,n,paths) + self.numberOfPaths(m,n-1, paths)
        return paths[grid]

if __name__ == '__main__':
    obj = FindNumberOfPathsInMatrix()
    print(obj.numberOfPaths(2,3))