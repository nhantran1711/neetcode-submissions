class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = defaultdict(int)
        
        for n in nums:
            mp[n] += 1

            if mp[n] == 2:
                return True
        return False