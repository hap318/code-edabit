class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = str(x)
            x = x[:0:-1]
            x = int(x)
            x = -x
        else:
            x = str(x)
            x = x[::-1]
            x = x.strip()
            x = int(x)
        return x
    
s = Solution()
print(s.reverse(-120))