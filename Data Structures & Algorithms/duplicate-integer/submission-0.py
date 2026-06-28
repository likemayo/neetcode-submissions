from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for value in freq.values():
            if value >= 2:
                return True
        return False        
            


        