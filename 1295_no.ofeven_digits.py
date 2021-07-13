class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        l=0
        for i in nums:
            c=0
            while i!=0:
                i //= 10
                c+=1
            if c%2==0:
                l+=1
                
                
                
        return l
                
            
 class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                n += 1
        
        return n
