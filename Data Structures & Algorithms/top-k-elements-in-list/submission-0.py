from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequence = Counter(nums)
        ans = [num for num,cnt in frequence.most_common(k)]
        return ans
        


        