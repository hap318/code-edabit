class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            l = i+1
            while l < len(nums):
                if nums[i] + nums[l] == target:
                    return [i,l]
                l+=1
    
    def twoSumN(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i
            print(seen)


s = Solution()
print(s.twoSumN(nums = [3,2,4], target = 6))
