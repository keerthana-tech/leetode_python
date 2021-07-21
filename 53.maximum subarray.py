class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur=nums[0]
        m=nums[0]
        for i in range(1,len(nums)):
            cur = max(nums[i],nums[i]+cur)
            m = max(cur,m)
        return m
