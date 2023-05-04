import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W+', "", s).lower()
        s = s.replace('_', '').strip()

        is_palidrome = False
        
        start = 0
        end = len(s) - 1

        while start <= end:

            if s[start] != s[end]:
                return is_palidrome
            
            start += 1
            end -= 1
            
        is_palidrome = True
        return True
        

        

sol = Solution()

print(sol.isPalindrome("ab`a"))