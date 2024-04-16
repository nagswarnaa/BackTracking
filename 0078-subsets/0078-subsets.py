class Solution:
    global res
    def subsets(self, nums: List[int]) -> List[List[int]]:
        global res
        res=[]
        self.backtrack(nums,[],0,len(nums))
        return res

    def backtrack(self,input_list,permutation,start_index,list_length):
        if start_index>=list_length:
            res.append(list(permutation))
            return 
        self.backtrack(input_list,list(permutation),start_index+1,list_length)
        permutation.append(input_list[start_index])
        self.backtrack(input_list,list(permutation),start_index+1,list_length)