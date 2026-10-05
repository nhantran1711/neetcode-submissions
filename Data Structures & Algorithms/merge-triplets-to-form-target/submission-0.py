class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        

        valid_trip = []
        for i, j, k in triplets:
            if i <= target[0] and j <= target[1] and k <= target[2]:
                valid_trip.append((i, j, k))
        

        res = [0, 0, 0]
        for i in range(len(valid_trip)):
            res[0] = max(res[0], valid_trip[i][0])
            res[1] = max(res[1], valid_trip[i][1])
            res[2] = max(res[2], valid_trip[i][2])
        return res == target