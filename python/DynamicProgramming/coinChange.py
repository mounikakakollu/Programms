'''
Given a value N, find the number of ways to make change for N cents,
if we have infinite supply of each of S = { S1, S2, .. , SM } valued coins.

Input:
n = 4 , m = 3
S[] = {1,2,3}
Output: 4
Explanation: Four Possible ways are:
{1,1,1,1},{1,1,2},{2,2},{1,3}.

Algorithms(tablulation of DynamicProgramming)
1. Table table with length target+1 and insert 0's
2. for each element in given array (coins)
    1. Traverse each element in the table
        1. If index of table >= coin
            table[index] += table[index-coin]
return table[target]

Here we are following tabulation by remembering previous solutions(without recursion)
'''
import copy


class coinChange:
    def coinChange(self, array, target, possibilities={}):
        if(target<0):
            return None
        if(target == 0):
            return [[]]
        count = []
        for i in array:
            if(target-i in possibilities):
                tmp1 = possibilities[target-i]
            else:
                tmp1 = self.coinChange(array, target-i, possibilities)
            if(tmp1 is None):
                continue
            tmp = copy.deepcopy(tmp1)
            if(len(tmp) == 1 and len(tmp[0]) == 0):
                tmp[0].append(i)
            # if(target in possibilities):
            else:
                for j in tmp:
                    j.append(i)
                    j.sort()
            # else:
            if target not in possibilities:
                possibilities[target] = tmp
            else:
                for j in tmp:
                    if(j not in possibilities[target]):
                        possibilities[target].append(j)

        if target in possibilities:
            return possibilities[target]
        else:
            possibilities[target] = None
            return None
    def noOfSols(self, array, target): # using DP
        table = [0]*(target+1)
        table[0] = 1
        for i in array:
            for j in range(target+1):
                if(j>=i):
                    table[j]+=table[j-i]
        return table[target]

if __name__== '__main__':
    # array = [1,2,3]
    # array = [5, 6 ,7 ,9, 11, 12, 13, 15]
    array = [1, 5, 10]
    obj = coinChange()
    # tmp = obj.coinChange(array, 3)
    # print(tmp)
    # if(tmp):
    #     print(len(tmp))
    print(obj.noOfSols(array, 12))
