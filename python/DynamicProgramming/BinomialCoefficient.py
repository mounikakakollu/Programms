'''
Given two integers n and r, find nCr. Since the answer may be very large, calculate the answer modulo 109+7.

nCr = n!/r!*(n-r)!
'''

class BinomialCoefficient:
    def factorial(self, n, factorials={}):
        fact = 1
        for i in range(2, n+1):
            fact*=i
            factorials[i] = fact
        return factorials

    def binomialCoefficientForSmallerValues(self, n, r):
        round = (10**9)+7
        if(r>n):
            return 0
        if(r == n):
            return 1
        factorials = {}
        factorials[1] = 1
        factorials = self.factorial(n, factorials)
        ncr = (factorials[n] /(factorials[r]*factorials[n-r]))
        print(factorials[n])
        return ncr

    def binomialCoefficientForLargerValues(self, n, r, p):
        parscalTriangle = [0 for i in range(r+1)]
        parscalTriangle[0] = 1
        for i in range(1, n+1):
            for j in range(min(i, r), 0, -1):
                parscalTriangle[j] = (parscalTriangle[j]+parscalTriangle[j-1])%p
        return parscalTriangle[r]

if __name__ == '__main__':
    obj = BinomialCoefficient()
    p = (10**9)+7
    # print(obj.binomialCoefficientForSmallerValues(778,116))
    print(obj.binomialCoefficientForLargerValues(778, 116,p))
