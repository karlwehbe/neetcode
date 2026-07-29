class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        l , r = 0, 1

        while r < len(prices):
            buy_price = prices[l]
            sell_price = prices[r]
            possible_profit = sell_price - buy_price
            profit = max(profit, possible_profit)

            if buy_price > sell_price:
                l += 1
            else:
                r += 1
        
        return profit

        