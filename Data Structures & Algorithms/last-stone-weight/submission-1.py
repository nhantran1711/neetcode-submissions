class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = []
        for s in stones:
            maxHeap.append(-s)
        heapq.heapify(maxHeap)

        stone1, stone2 = 0, 0
        while len(maxHeap) > 1:
            stone1 = -heapq.heappop(maxHeap)
            stone2 = -heapq.heappop(maxHeap)


            if stone2 < stone1:
                heapq.heappush(maxHeap, -(stone1 - stone2))
        return -maxHeap[0] if len(maxHeap) == 1 else 0