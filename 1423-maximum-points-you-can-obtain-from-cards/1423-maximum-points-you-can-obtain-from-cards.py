class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        if not cardPoints:
            return 0

        sumi = sum(cardPoints[:k])
        total = sumi

        for i in range(1,k+1):
            sumi = sumi - cardPoints[k-i] + cardPoints[n-i]
            total = max(total,sumi)

        return total