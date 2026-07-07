class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=len(set(nums))
        # return a
        if(a<len(nums)):
            return True
        else:
            return False
