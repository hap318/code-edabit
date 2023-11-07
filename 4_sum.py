class Solution:

     def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        combos = []
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range (k + 1, n):
                        if (nums[i] + nums[j] + nums[k] + nums[l]) == target:
                            quad = [nums[i], nums[j], nums[k], nums[l]]
                            quad.sort()
                            if quad not in combos:
                                combos.append(quad)
        return combos

s = Solution()
print(s.fourSum([1,0,-1,0,-2,2]))