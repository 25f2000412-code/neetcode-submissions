class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for k in nums:
            d[k] = d.get(k, 0) + 1
        
        return max(d, key = d.get)
        