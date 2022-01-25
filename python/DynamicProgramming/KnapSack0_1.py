'''
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively.
Also given an integer W which represents knapsack capacity,
find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.
 You cannot break an item, either pick the complete item or don’t pick it (0-1 property).

 Example
 wt = [1,2,3], val = [10,15,40] capacity = 6
 consider a matrix of len(wt)*capacity (3*6)
    0   1   2   3   4   5   6   => Capacity of knapsack (i)
0   0   0   0   0   0   0   0
1   0  10  10  10  10  10  10    => matrix[1][2] = max(matrix[1-1][2](10), val(j 10)+matrix[1-1][2-wt[i 1]]) = 10+0
2   0  10   15  25  25  25  25
3   0   10  15  40  50  55  65
Wt(j)

matrix[i][j] = max(matrix[i-1][j], val[j]+matrix[i-1][j-wt[i]]

return matrix[len(wt)][capacity] -> 65
'''

class KnapSack0_1:
    def knapSack(self, wt, val, capacity):
        matrix = []
        for i in range(len(wt)+1):
            matrix.append([])
            for j in range(capacity+1):
                matrix[i].append(0)
        for i in range(1,len(wt)+1):
            for j in range(1,capacity +1):
                if(j>=wt[i-1]):
                    curVal = val[i-1]+matrix[i-1][j-wt[i-1]]
                    if(matrix[i-1][j] < curVal):
                        matrix[i][j] = curVal
                    else:
                        matrix[i][j] = matrix[i-1][j]
                else:
                    matrix[i][j] = matrix[i-1][j]
        return matrix[len(wt)][capacity]

if __name__ == '__main__':
    obj = KnapSack0_1()
    # wt = [1,2,3]
    # val = [10,15,40]
    wt = [83, 84, 85, 76, 13, 87, 2, 23, 33, 82, 79, 100, 88, 85, 91, 78, 83, 44, 4, 50, 11, 68, 90, 88, 73, 83, 46, 16, 7, 35, 76, 31, 40, 49, 65, 2, 18, 47, 55, 38, 75, 58, 86, 77, 96, 94, 82, 92, 10, 86, 54, 49, 65, 44, 77, 22, 81, 52]
    val = [57,95,13,29,1,99,34,77,61,23,24,70,73,88,33,61,43,5,41,63,8,67,20,72,98,59,46,58,64,94,97,70,46,81,42,7,1,52,20,54,81,3,73,78,81,11,41,45,18,94,24,82,9,19,59,48,2,72]
    print(obj.knapSack(wt, val, 41))
