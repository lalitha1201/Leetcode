class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        
        low = 0
        hi = len(nums) - 1   
        while low < hi:
            
            mid = low + (hi - low) // 2
            halves_are_even = (hi - mid) % 2 == 0
            if nums[mid + 1] == nums[mid]:
                if halves_are_even:
                    low = mid + 2
                else:
                    hi = mid - 1
            elif nums[mid - 1] == nums[mid]:
                if halves_are_even:
                    hi = mid - 2
                else:
                    low = mid + 1
            else:
                return nums[mid]
        return nums[low]
