class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m
                r = m
                while l > 0 and nums[l-1] == target:
                        l -= 1
                while r < len(nums)-1 and nums[r+1] == target:
                        r += 1
                return [l, r]
        return [-1,-1]

s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))