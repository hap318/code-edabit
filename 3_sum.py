class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        combos = []
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        triple = [nums[i], nums[j], nums[k]]
                        triple.sort()
                        if triple not in combos:
                            combos.append(triple)
        return combos

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))