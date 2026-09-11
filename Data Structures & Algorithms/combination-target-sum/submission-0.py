class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(i, total, arr):
            if i == len(nums) or total > target:
                return
            
            if total == target:
                res.append(arr.copy())
                return
            
            arr.append(nums[i])
            backtrack(i, total + nums[i], arr)

            arr.pop()
            backtrack(i + 1, total, arr)
        backtrack(0, 0, [])
        return res


