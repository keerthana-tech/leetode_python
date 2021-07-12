class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return binaryhelp(nums,target,0,len(nums)-1)
def binaryhelp(nums,target,left,right):
        while left <= right:
            middle=(left+right)//2
            if nums[middle]==target:
                return middle
            elif target<nums[middle]:
                right=middle-1
            else:
                left=middle+1
        if target > nums[middle]:
            return middle+1
        else:
            return middle
       
        
