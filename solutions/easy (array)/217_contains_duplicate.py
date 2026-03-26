class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        occurences = {}
        for num in nums:
            if num in occurences and occurences[num] >= 1:
                return True
            occurences[num] = occurences.get(num, 0) + 1
        return False