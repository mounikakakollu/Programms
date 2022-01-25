'''
Given a gold mine of n*m dimensions. Each field in this mine contains a positive integer which is the amount of gold in tons.
Initially the miner is at first column but can be at any row. He can move only (right->,right up /,right down\) that is from a given cell,
the miner can move to the cell diagonally up towards the right or right or diagonally down towards the right.
 Find out maximum amount of gold he can collect.

 Input: mat[][] = { {1, 3, 1, 5},
                   {2, 2, 4, 1},
                   {5, 0, 2, 3},
                   {0, 6, 1, 2}};
Output : 16
(2,0) -> (1,1) -> (1,2) -> (0,3) OR
(2,0) -> (3,1) -> (2,2) -> (2,3)

Input : mat[][] = {{10, 33, 13, 15},
                  {22, 21, 04, 1},
                  {5, 0, 2, 3},
                  {0, 6, 14, 2}};
Output : 83
'''
def countAmountOfGold(mat, m, n, memory = {}):
    rowSize = len(mat)
    colSize = 0
    if(rowSize>0):
        colSize = len(mat[0])
    if (m < 0 or m>=rowSize):
        return 0
    if(n+1 == colSize):
        return mat[m][n]
    key = str(m) + "*" + str(n)
    if(key in memory):
        return memory[key]
    amount = max(countAmountOfGold(mat, m-1,n+1, memory), countAmountOfGold(mat, m+1, n+1, memory), countAmountOfGold(mat, m,n+1,memory)) + mat[m][n]
    # print(key, amount)
    memory[key] = amount
    return amount



# mat = [
#     [1, 3, 1, 5],
#     [2, 2, 4, 1],
#     [5, 0, 2, 3],
#     [0, 6, 1, 2]
# ]
# output = 16
# mat = [[1, 3, 3],
#         [2, 1, 4],
#         [0, 6, 4]
#         ]
# output = 12

mat = [[10, 33, 13, 15],
        [22, 21, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 14, 2]]
# output = 83
maxGold = 0
memory = {}
for i in range(4):
    gold = countAmountOfGold(mat, i,0, memory)
    print(memory)
    if(maxGold < gold):
        maxGold = gold
print(maxGold)
