'''
Given a n*n matrix where all numbers are distinct, find the maximum length path (starting from any cell)
such that all cells along the path are in increasing order with a difference of 1.
We can move in 4 directions from a given cell (i, j), i.e., we can move to (i+1, j) or (i, j+1) or (i-1, j) or (i, j-1)
with the condition that the adjacent cells have a difference of 1.

Input:  mat[][] = {{1, 2, 9}
                   {5, 3, 8}
                   {4, 6, 7}}
Output: 4
The longest path is 6-7-8-9.
'''

def findLargestPath(mat, row, col, memory, track):
    up = row-1
    down = row+1
    right = col+1
    left = col-1
    key = str(row) + "*" + str(col)
    path_right = path_left = path_up = path_down =0
    if(key in memory):
        return memory[key]
    if(0<= row < len(mat) and right < len(mat[row]) and not track[row][right] and mat[row][col]+1 == mat[row][right]):
        track[row][right] = 1
        path_right += findLargestPath(mat, row, right, memory, track);
    else:
        path_right += 1
    if(0<= row < len(mat) and left >=0 and  not track[row][left] and mat[row][col]+1 == mat[row][left]):
        track[row][left] = 1
        path_left += findLargestPath(mat, row, left, memory, track);
    else:
        path_left += 1
    if(0<=col<len(mat[0]) and up >=0 and not track[up][col] and mat[row][col]+1 == mat[up][col]):
        track[up][col] = 1
        path_up += findLargestPath(mat, up, col, memory, track);
    else:
        path_up += 1
    if(0<=col<len(mat[0]) and  down< len(mat) and mat[row][col]+1 == mat[down][col]):
        track[down][col] = 1
        path_down += findLargestPath(mat, down, col, memory, track);
    else:
        path_down += 1

    maxpath = max(path_down, path_up, path_left, path_right)
    memory[key] = maxpath
    print(memory)
    return maxpath

mat = [
    [1,2,9],
    [5,3,8],
    [4,6,7]
]

maxPath = 0
memory = {}
track = [[0 for _ in range(len(mat[0]))] for i in range(len(mat))]
for i in range(len(mat)):
    for j in range(len(mat[i])):
        track = [[0 for _ in range(len(mat[0]))] for i in range(len(mat))]
        path = 1+findLargestPath(mat, i, j, memory, track)
        if(maxPath < path):
            maxPath = path
print(maxPath)