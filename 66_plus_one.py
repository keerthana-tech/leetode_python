class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r=0
        z=[]
        for i in range(len(digits)):
            r=r*10+digits[i]
            
        r=r+1
        r=str(r)
        for i in r:
            z.append(int(i))
        return z
