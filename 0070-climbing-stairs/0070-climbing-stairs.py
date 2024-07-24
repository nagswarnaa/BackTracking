class Solution:
    def climbStairs(self, n: int) -> int:
        before_last_step = 1
        last_step = 2
        if n == before_last_step:
            return before_last_step 
        if n == last_step:
            return last_step 
        for x in range(3, n+1):
            num = last_step + before_last_step
            before_last_step = last_step
            last_step = num
        return last_step