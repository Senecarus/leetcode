class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        m = 0
        n = 0
        for i in range(len(prices) - 1):
            m = min(prices[i], m)
            n = max (prices[i + 1] - m, n)
            

        return n

sol = Solution
print("Max profit: ", sol.maxProfit(sol, [7,1,5,3,6,4]))
print("Max profit: ", sol.maxProfit(sol, [7,6,4,3,1]))
print("Max profit: ", sol.maxProfit(sol, [1]))
