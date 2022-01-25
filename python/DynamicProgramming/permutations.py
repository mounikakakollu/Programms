'''
Find permutations of given n, k
P(n,k) = n!/(n-k)!
'''

class Permutations:
    def permutations(self, n, k):
        if(k>n):
            return 0
        factorials = []
        factorials.append(0)
        fact = 1
        for i in range(1,n+1):
            fact*=i
            if(i<=n-k):
                factorials.append(fact)
        return int(fact/factorials[n-k])

if __name__ == '__main__':
    obj = Permutations()
    print(obj.permutations(10,2))
    print(obj.permutations(10, 3))
    print(obj.permutations(10, 0))
    print(obj.permutations(10, 1))
