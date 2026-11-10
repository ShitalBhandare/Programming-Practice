'''
Given an array prices[] of non-negative integers, representing the prices of the stocks on different days, return the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

Note: Stock must be bought before being sold.
'''
# 2 passes
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        if not prices:
            return

        min = float('inf')
        profit = float('-inf')
        for i in range(prices):
            if prices[i] < min:
                min = prices[i] # 1
                index = i # 1

        for i in range(index, len(prices)):
            if prices[i] - min > profit:
                profit = prices[i] - min

        if profit == float('-inf'):
            return 0
        return profit

# 1 pass

def maxProfit(prices):
    minSoFar = prices[0]
    res = 0

    
    for i in range(1, len(prices)):
        
        # Update the minimum value seen so far  
        minSoFar = min(minSoFar, prices[i])
        
        # Update result if we get more profit                
        res = max(res, prices[i] - minSoFar)
    
    return res

if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    print(maxProfit(prices))
