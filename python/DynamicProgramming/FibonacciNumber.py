'''
Find fibonacci number of n
'''

class FibonacciNumber:
    def fibonacciNumWithRecursion(self, n):
        if(n<=2):
            return 1
        return self.fibonacciNumWithRecursion(n-1) + self.fibonacciNumWithRecursion(n-2)

    def fibonacciNum(self, n):
        result = 1
        first = 1
        second = 1
        if(n<=2):
            return 1
        for i in range(3,n+1):
            first, second = second, first+second
        return second

    def fibonacciNumWithMemorization(self, n, fibSeries=[0,1,1]):
        if(n < len(fibSeries)):
            return fibSeries[n]
        first = self.fibonacciNumWithMemorization(n - 1, fibSeries)
        second = self.fibonacciNumWithMemorization(n - 2, fibSeries)
        fibSeries.append(first + second)
        # print(fibSeries)
        return  fibSeries[-1]




if __name__ == '__main__':
    obj = FibonacciNumber()
    # print(obj.fibonacciNumWithRecursion(6))
    # print(obj.fibonacciNumWithRecursion(7))
    # print(obj.fibonacciNumWithRecursion(8))
    # print(obj.fibonacciNumWithRecursion(50))

    # print(obj.fibonacciNum(6))
    # print(obj.fibonacciNum(7))
    # print(obj.fibonacciNum(8))
    print(obj.fibonacciNum(50))
    fibSeries = [0,1,1]
    # print(obj.fibonacciNumWithMemorization(6,fibSeries))
    # print(obj.fibonacciNumWithMemorization(7,fibSeries))
    # print(obj.fibonacciNumWithMemorization(8,fibSeries))
    print(obj.fibonacciNumWithMemorization(50,fibSeries))