class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        edge = ["IV", "IX", "XL", "XC", "CD", "CM"]
        total = 0
        i=0
        while i < (len(s)):
            if i < len(s)-1 and s[i] + s[i+1] in edge:
                total += (m[s[i+1]] - m[s[i]])
                i += 2
            else:
                total += m[s[i]]
                i += 1
            print(total)
        return total

s = Solution()
print(s.romanToInt("MCMXCIV"))