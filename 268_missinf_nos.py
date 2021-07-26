class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sumexp=n*(n+1)//2
        acsum=sum(nums)
        return sumexp-acsum
            
