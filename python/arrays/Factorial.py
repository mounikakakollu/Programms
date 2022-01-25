'''
Find factorial of a large number

Given an integer N, find its factorial.

Input: N = 5
Output: 120
Explanation : 5! = 1*2*3*4*5 = 120
'''

class Factorial:
    def factorial(self,n):
        result = 1
        for i in range(2,n,1):
            result*=i
        return result*n

if __name__ == '__main__':
    obj = Factorial()
    print(obj.factorial(5))

