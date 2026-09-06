class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        


        queue =  collections.deque()
        res = []
        
        for r in range(len(nums)):
            
            while queue and queue[0] < (r - k + 1):
                queue.popleft()
            
            while queue and nums[queue[-1]] <= nums[r]:
                queue.pop()
            
            queue.append(r)

            if r >= k - 1:
                res.append(nums[queue[0]])
            
        return res


