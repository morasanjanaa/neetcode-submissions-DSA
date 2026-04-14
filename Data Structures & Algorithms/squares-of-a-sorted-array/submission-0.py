class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square_list = []
        for i in nums:
            square_list.append(i*i)
        return sorted(square_list)
        