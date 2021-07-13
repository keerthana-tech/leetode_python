class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sortedArray=[0]*len(nums)
        start=0
        end=len(nums)-1
        for i in reversed(range(len(nums))):
            if abs(nums[start]) < abs(nums[end]):
                square=nums[end]
                end-=1
            else :
                square=nums[start]
                start+=1
            sortedArray[i]=square*square
        return sortedArray
