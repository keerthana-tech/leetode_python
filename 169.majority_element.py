class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m=len(nums)//2
        c=Counter(nums)
        for k,v in c.items():
            if v > m:
                return k
        return None
        
        
        class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m=len(nums)//2
        c=0
        
        lst=list(set(nums))
        
        for i in lst:
            if nums.count(i) > m:
                a=i
        return a
        
