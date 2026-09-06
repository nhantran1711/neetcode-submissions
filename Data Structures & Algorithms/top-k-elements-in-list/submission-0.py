class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        res = []

        sorted_counter = sorted(counter.items(), key = lambda x:x[1], reverse = True)
        
        for key, value in sorted_counter:
            if k > 0:
                res.append(key)
            k -= 1
        return res
