class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=1
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                nums[j]=nums[i+1]
                j+=1
        return nums

    
    class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while i <len(nums)-2:
            if nums[i]==nums[i+1]==nums[i+2]:
                del nums[i]
            else:
                i+=1
        return len(nums)
            
