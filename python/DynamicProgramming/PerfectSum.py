'''
Perfect Sum Problem (Print all subsets with given sum)
Difficulty Level : Hard
Last Updated : 02 Mar, 2021
Given an array of integers and a sum, the task is to print all subsets of the given array with a sum equal to a given sum.
Examples:

Input : arr[] = {2, 3, 5, 6, 8, 10}
        sum = 10
Output : 5 2 3
         2 8
         10

Input : arr[] = {1, 2, 3, 4, 5}
        sum = 10
Output : 4 3 2 1
         5 3 2
         5 4 1


Algorithm (recursion in Dynamic Programming)
1. Consider that ele and call recursion
2. Don't consider that ele and call recustion
3. If sum == currSum then Count+=1
'''

class PerfectSum:
    count = 0
    def printPossibleSubSets(self, arr, sum, i, curSum):
        if(curSum == sum):
            self.count+=1
            return self.count
        if(curSum < sum  and i<len(arr)):
            self.printPossibleSubSets(arr, sum, i+1, curSum+arr[i])
            self.printPossibleSubSets(arr, sum, i+1, curSum)

if __name__ == '__main__':
    arr = [2, 3, 5, 6, 8, 10]
    sum = 10
    obj = PerfectSum()
    obj.printPossibleSubSets(arr, sum, 0, 0)
    print(obj.count)
