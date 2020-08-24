class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count_global = 0
        count_cur = 0
        for i in nums:
            if i == 1:
                count_cur += 1
            else:
                if count_cur > count_global:
                    count_global = count_cur
                count_cur = 0
        return max(count_global, count_cur)
