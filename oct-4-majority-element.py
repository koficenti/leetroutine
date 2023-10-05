# https://leetcode.com/problems/majority-element/description/
# Time O(n) - Space O(k) where k is the amount of unique elements
# Can be improved

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x = Counter(nums)
        return [*filter(lambda key: x[key] > (len(nums) // 3) , x)]
