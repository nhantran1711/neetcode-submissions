class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-f for f in freq.values()]
        heapq.heapify(maxHeap)

        time = 0
        queue = deque() # [remainder, time] or idle time

        while maxHeap or queue:
            time += 1

            if not maxHeap:
                time = queue[0][1]
            else:
                remainder = heapq.heappop(maxHeap) + 1
                if remainder:
                    queue.append([remainder, time + n])
            
            if queue and queue[0][1] == time:
                rem, _ = queue.popleft()
                heapq.heappush(maxHeap, rem)
        return time