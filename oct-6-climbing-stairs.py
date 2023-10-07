# https://leetcode.com/problems/climbing-stairs/
# simple solution

class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(n):
            if n <= 0:
                return 0
            elif n == 1:
                return 1
    
            fib = [0, 1]
            for i in range(2, n + 1):
                fib.append(fib[i - 1] + fib[i - 2])
            return fib[n]
        return fib(n + 1)
