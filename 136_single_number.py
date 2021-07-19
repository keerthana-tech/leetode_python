class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        n={}
        for i in nums:
            if i in n:
                del n[i]
            else:
                n[i]=True
        return list(n.keys())[0]
      
      
      
      class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[0]^=nums[i]
        return nums[0]
            
            
            
