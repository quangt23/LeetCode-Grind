class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        occurences = {}
        n = len(nums)
        res = []
        for num in nums:
            occurences[num] = occurences.get(num, 0) + 1
        
        for i in range(1, n + 1):
            if i not in occurences:
                    res.append(i)
        return res