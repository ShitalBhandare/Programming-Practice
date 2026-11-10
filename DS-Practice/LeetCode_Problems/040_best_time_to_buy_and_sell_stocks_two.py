'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

Find and return the maximum profit you can achieve.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculate maximum profit from multiple stock transactions.
        Buy and sell whenever there's a price increase from one day to the next.
      
        Args:
            prices: List of stock prices where prices[i] is the price on day i
          
        Returns:
            Maximum profit achievable from multiple buy-sell transactions
        """
        # Initialize total profit
        total_profit = 0
      
        # Iterate through consecutive price pairs
        for i in range(1, len(prices)):
            # Calculate profit from buying on day i-1 and selling on day i
            daily_profit = prices[i] - prices[i-1]
          
            # Only add positive profits (buy low, sell high on consecutive days)
            if daily_profit > 0:
                total_profit += daily_profit
      
        return total_profit
