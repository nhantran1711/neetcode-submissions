class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def backtrack(i, arr, total):
            if total == target:
                res.append(arr.copy())
                return

            if i == len(candidates) or total > target:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                if total + candidates[j] > target:
                    break

                arr.append(candidates[j])
                backtrack(j + 1, arr, total + candidates[j])

                arr.pop()


        backtrack(0, [], 0)
        return res