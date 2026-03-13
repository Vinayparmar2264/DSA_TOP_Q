
# memoization
# class Solution:
#     def func(self,coins,amount,idx,dp):
#         if amount==0:
#             return 0     
#         elif idx<0 or amount<0:
#             return float("inf")

#         if dp[amount]!=-1:
#             return dp[amount]

#         pick = 1 + self.func(coins,amount-coins[idx],idx,dp)

#         not_pick = self.func(coins,amount,idx-1,dp)

#         dp[amount] = min(pick,not_pick)
#         return dp[amount]

#     def coinChange(self, coins: List[int], amount: int) -> int:
#         idx = len(coins)
#         dp = [-1 for _ in range(amount+1)]
#         ans = self.func(coins,amount,idx-1,dp)
#         if ans==float("inf"):
#             return -1
#         return ans
        


# tabulation


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])


        if dp[amount] == float('inf'):
            return -1

        return dp[amount]

