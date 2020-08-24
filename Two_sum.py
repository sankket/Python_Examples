class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in table:
                table[nums[i]] = i
            else:
                return [table[complement], i]
