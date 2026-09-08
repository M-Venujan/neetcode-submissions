class Solution:
    def findMin(self, nums: List[int]) -> int:
        sol = nums[0]
        l , h = 0 , len(nums) -1
        while h >= l:
            if nums[l] < nums[h]:
                sol = min(nums[l] , sol)
                break

            mid = (l+h)//2
            sol = min(nums[mid] , sol)
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                h = mid - 1
        return sol