class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]+nums[j] == target:
                    return [j,i]
        #what if er were ti find the the list pf pairs of such indices
        # in that case we would write result = []and then appens result.append([j, i])this way it will help i think?
        # what our instructor think is more important even though
        