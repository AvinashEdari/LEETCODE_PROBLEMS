class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            x=nums[i]
            for j in range(i+1,len(nums)):
                if x+nums[j]==target:
                    return [i,j]