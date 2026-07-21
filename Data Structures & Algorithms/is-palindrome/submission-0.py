class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(char for char in s if char.isalnum())
        clean_s = clean_s.lower()
        p1 = 0
        p2 = len(clean_s) -1
        while p1 < p2:
            if clean_s[p1] != clean_s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True