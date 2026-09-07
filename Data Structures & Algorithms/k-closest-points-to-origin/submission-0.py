class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        for i, (x, y) in enumerate(points):
            minHeap.append([math.sqrt(x ** 2 + y ** 2), i])
        heapq.heapify(minHeap)
        
        res = []
        for _ in range(k):
            _, i = heapq.heappop(minHeap)
            res.append(points[i])
        return res
