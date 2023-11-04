class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pre = ""
        r = 1
        flag = True
        first = strs.pop(0)
        while flag:
            for i in strs:
                if first[:r] != i[:r]:
                    flag = False
                    break
            if flag == True:
                pre += first[r-1]
                r += 1
        return pre

    
s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))