class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for k in nums:
            d[k] =d.get(k,0)+1 #check key exists, if not add 0
        if d[k]>1:
                return True
        else:
            return False