class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        maxHeap = []
        for n in nums:
            maxHeap.append(-n)
        heapq.heapify(maxHeap)

        maxElement = 0
        while maxHeap and k > 0:
            maxElement = -heapq.heappop(maxHeap)
            k -= 1
        
        return maxElement