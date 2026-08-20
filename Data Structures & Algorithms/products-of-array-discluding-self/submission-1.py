class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = 1
        post= 1
        result= [1]*(len(nums))
        
        for num in range (len(nums)):
            result[num] = pre
            pre*= nums[num]

        for num in range (len(nums)-1,-1,-1):
            result[num] *= post
            post *= nums[num]     

        return result