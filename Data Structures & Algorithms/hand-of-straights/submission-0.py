class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        

        counter = Counter(hand)
        hand.sort()

        for n in hand:
            if counter[n]:
                for i in range(n, n + groupSize):
                    if not counter[i]:
                        return False
                    counter[i] -= 1
        return True