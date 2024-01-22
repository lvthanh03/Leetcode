class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left: int, right: int):
            cnt = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
            return cnt
            
        palindromes = 0
        for i in range(len(s)):
            palindromes += expand(i,i)
            palindromes += expand(i,i+ 1)
        return palindromes