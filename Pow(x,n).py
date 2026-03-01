class Solution:
  def myPow(self, x: float, n: int) -> float:
    def rec(x,n):
      if n == 0: return 1
      if n == 1: return x

      t = rec(x, n//2)
      if n % 2 == 0:
        return t*t
      return x*t*t
    if n < 0:
      return 1 / rec(x, abs(n))
    return rec(x, n)
    
