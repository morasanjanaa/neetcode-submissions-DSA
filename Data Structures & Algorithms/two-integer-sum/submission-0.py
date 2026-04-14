class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = dict()
        for i in range(0,len(nums)):
            x = target - nums[i]
            if x in dict1:
                return [dict1[x],i]
            else:
                dict1[nums[i]] = i
        return None

                