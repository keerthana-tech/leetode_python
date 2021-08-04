class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op=[1]*len(nums)
        post=1
        pre=1
        for i in range(len(nums)):
            op[i]=pre
            pre*=nums[i]
        for i in reversed(range(len(nums))):
            op[i]=op[i]*post
            post*=nums[i]
        return op
