class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        if not nums:
            return False

        low =0
        high = len(nums) - 1
        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target :
                return True

            
            
            while low < mid and nums[low] == nums[mid]:  # Skip duplicates on the left side
                low += 1
            while mid < high and nums[mid] == nums[high]:  # Skip duplicates on the right side
                high -= 1
            
            #if left half is sorted
            if nums[low] <= nums[mid]:
                #if target is in left half
                if nums[low] <= target <= nums[mid]:
                    high = mid-1
                else:
                    low = mid + 1
            elif nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return False

        
