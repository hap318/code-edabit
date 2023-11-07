class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l, r  = 0, 0
        if len(x) % 2 == 0:
            l = (len(x)//2)-1
            r = (len(x)//2)
            pal = True
            while l >= 0 and r < len(x):
                if x[l] != x[r]:
                    pal = False
                l -= 1
                r += 1

        else:
            l, r = (len(x)//2), (len(x)//2)
            pal = True
            while l >= 0 and r < len(x):
                if x[l] != x[r]:
                    pal = False
                l -= 1
                r += 1
        return pal

s = Solution()
print(s.isPalindrome(1001))
            
