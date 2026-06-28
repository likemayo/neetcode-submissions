from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for i in strs:
            key = "".join(sorted(i))
            anagram[key].append(i)
        return([i for i in anagram.values()])

        