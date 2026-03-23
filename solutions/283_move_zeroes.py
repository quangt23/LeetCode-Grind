class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        
        for num in nums:
            if num != 0:
                nums[l] = num
                l += 1
        
        for i in range(l, len(nums)):
            nums[i] = 0