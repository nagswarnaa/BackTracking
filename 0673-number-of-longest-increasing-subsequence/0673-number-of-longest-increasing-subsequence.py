from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        lengths = {}  
        counts = {}   
        for i in range(n):
            lengths[i] = 1
            counts[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
        
        longest = max(lengths.values())
        return sum(counts[i] for i in lengths if lengths[i] == longest)
