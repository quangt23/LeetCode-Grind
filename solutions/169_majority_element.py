class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        occurences = {}

        for num in nums:
            occurences[num] = occurences.get(num, 0) + 1
        
        times = n/2
        for num, count in occurences.items():
            if count > times:
                return num
        return 0