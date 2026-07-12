class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        idx=[]
        while(l<r):
            if(numbers[l]+numbers[r]==target):
                idx=[l+1, r+1]
                return idx
            elif(numbers[l]+numbers[r]>target):
                r-=1
            else:
                l+=1
        return idx