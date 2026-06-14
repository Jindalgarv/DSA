from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq=Counter(hand)
        for num in sorted(freq):
            while freq[num]>0:
                for nxt in range(num,num+groupSize):
                    if freq[nxt]==0:
                        return False
                    else:
                        freq[nxt]-=1
        return True
    