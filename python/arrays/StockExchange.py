'''
Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Algo
1. track minprice and maxprofit
if price[i]<minprice:
    minprice = price[i]
maxprofit = max(maxprofit, price[i]-minprice)
'''


class StockExchange:
    def getMaxPrice(self, prices):
        if (len(prices) < 0):
            return 0
        minprice = prices[0]
        maxprofit = 0
        for i in prices:
            if (minprice > i):
                minprice = i
            if (maxprofit < i - minprice):
                maxprofit = i - minprice
        return maxprofit


if __name__ == '__main__':
    obj = StockExchange()
    # prices = [7, 1, 5, 3, 6, 4]
    prices = [7,6,4,3,1]
    print(obj.getMaxPrice(prices))
