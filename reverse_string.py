class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1
        print(s)


s = Solution()
s.reverseString([1,2,3,4,5])
        