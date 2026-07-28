class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for a in range(len(nums)-1) :
            if nums[a] == nums[a+1]:
                return True
        return False
