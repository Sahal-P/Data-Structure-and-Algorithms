class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq = []

        for i in nums:
            sq.append(i**2)

        return sorted(sq)