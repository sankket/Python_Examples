class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums) if nums else 0
        i_minus_3 = 0
        i_minus_2 = nums[0]
        i_minus_1 = nums[1]
        
        for num in nums[2:]:
            current = max(i_minus_1,i_minus_2 + num, i_minus_3 + num)
            i_minus_3 = i_minus_2
            i_minus_2 = i_minus_1
            i_minus_1 = current
        
        return i_minus_1

