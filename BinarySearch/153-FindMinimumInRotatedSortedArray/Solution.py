import sys
class Solution:
    def findMin(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) - 1

        tmin = sys.maxsize

        while low <= high:

            mid = (low+high)//2

            if nums[low] <=nums[mid]:
                tmin = min(tmin,nums[low])
                low = mid+1
            else:
                tmin = min(tmin,nums[mid])
                high = mid -1


        return tmin
        
