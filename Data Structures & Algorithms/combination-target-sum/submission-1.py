class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(i, arr, total):

            if total == target:
                res.append(arr[:])
                return
            
            if i == len(nums) or total > target:
                return 
            
            arr.append(nums[i])
            backtrack(i, arr, total + nums[i])

            arr.pop()
            backtrack(i + 1, arr, total)
        
        backtrack(0, [], 0)
        return res
