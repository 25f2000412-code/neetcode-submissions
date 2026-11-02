class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nList = []
        vList = []
        for i in range(len(nums)):
            if val != nums[i]:
                nList.append(nums[i])
            else:
                vList.append(nums[i])
        nums[:] = nList+vList
        return len(nList)