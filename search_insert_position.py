class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return l

s = Solution()
#print(s.searchInsert(nums = [1,3,5,6], target = 5))
print(s.searchInsert(nums = [1,3,5,6], target = 2))