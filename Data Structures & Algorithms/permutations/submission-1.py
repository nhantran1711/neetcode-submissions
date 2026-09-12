class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtrack(i, used, arr):
            if len(arr) == len(nums):
               res.append(arr.copy())
               return

            for j in range(len(nums)):
                if used[j]:
                    continue
                
                used[j] = True
                arr.append(nums[j])
                backtrack(i + 1, used, arr)

                arr.pop()
                used[j] = False
        
        used = [False] *  len(nums)
        backtrack(0, used, [])
        return res