class Solution:
    def isPalindrome(self, s: str) -> bool:

        # normalized = ''.join(c.lower() for c in s if c.isalnum())

        # length = len(normalized)

        # for i in range(0, length):
        #     if normalized[i] != normalized[-1 - i]:
        #         return False

        # return True
        l, r = 0, len(s) - 1
        
        while l < r:
            # Skip non-alphanumeric characters from left
            while l < r and not s[l].isalnum():
                l += 1
            # Skip non-alphanumeric characters from right
            while r > l and not s[r].isalnum():
                r -= 1
            # Compare characters (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True