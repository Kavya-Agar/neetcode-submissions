class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s))
        n = len(s) - 1
        s = s.lower()
        print(s)

        for i in range(n):
            if s[i] != s[n]:
                return False
            else:
                n -= 1
        
        return True