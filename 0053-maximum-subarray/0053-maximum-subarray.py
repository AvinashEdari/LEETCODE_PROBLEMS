class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max1=nums[0]
        cs=nums[0]
        for i in range(1,len(nums)):
            cs=max(nums[i]+cs,nums[i])
            max1=max(cs,max1)
        return max1
        