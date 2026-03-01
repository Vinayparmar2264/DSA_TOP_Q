class Solution:
    #most optimal way that is tabulation with space optimization
    # def climbStairs(self, n: int) -> int:
    #     prev = 1
    #     prev2 = 1
    #     for i in range(2,n+1):
    #         curr = prev+prev2
    #         prev2=prev
    #         prev=curr
    #     return prev


    # recursion will take maximum time complexity and it will give t.l.e., its s.c. =O(n) and t.c. = O(2^n)
    # def func(self,n:int)->int:
    #     if n==1 or n==0:
    #         return 1
    #     return self.func(n-1) + self.func(n-2)
    # def climbStairs(self, n: int) -> int:
    #     return self.func(n)


# this is a dp approach : memoiztion, its s.c. = 2O(n) and t.c. ==O(n)
    # def func(self,n:int,dp)->int:
    #     if n==1 or n==0:
    #         return 1
    #     if dp[n]!=-1:
    #         return dp[n]
    #     dp[n]=self.func(n-1,dp) + self.func(n-2,dp)
    #     return dp[n]
    # def climbStairs(self, n: int) -> int:
    #     dp =[-1]*(n+1)
    #     return self.func(n,dp)


# this is a tabulation method of dp, it is good compare to recursion and memoization its s.c. = O(n) and t.c.= O(n)
    def climbStairs(self, n: int) -> int:
        dp =[-1]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
