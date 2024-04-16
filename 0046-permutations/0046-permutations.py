class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final_result = []
        permutation = []
        list_length = len(nums)
        visited = [False] * list_length
        
        def back_track(permutation, visited):
            if len(permutation) == list_length:
                final_result.append(list(permutation))
                return
            for x in range(list_length):
                if not visited[x]:
                    permutation.append(nums[x])
                    visited[x] = True
                    back_track(permutation, visited)
                    permutation.pop()
                    visited[x] = False
        
        back_track(permutation, visited)
        return final_result

