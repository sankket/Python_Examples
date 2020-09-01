class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        count = 0
        for i in range(len(nums)-1):
            if nums[i] != val:
                nums[count] = nums[i]
                count = count + 1
        return count
        '''
        while val in nums:
            nums.remove(val)
