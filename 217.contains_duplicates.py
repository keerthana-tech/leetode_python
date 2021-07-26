class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset=set()
        for i in nums:
            if i not in myset:
                myset.add(i)
            else:
                return True
        return False
    
    class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
        
