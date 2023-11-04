class Solution:
    def maxArea(self, height: list[int]) -> int:
        curr_max = 0
        for i in range(len(height)):
            for j in range(len(height)):
                h = min(height[i], height[j])
                area = h * (j-i)
                if curr_max < area:
                    curr_max = area
        print(curr_max)
        return curr_max
    
s = Solution()
s.maxArea([1,8,6,2,5,4,8,3,7])