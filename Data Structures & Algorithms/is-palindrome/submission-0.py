class Solution:
    def isPalindrome(self, s: str) -> bool:

        normalized = ''.join(c.lower() for c in s if c.isalnum())

        length = len(normalized)

        for i in range(0, length):
            if normalized[i] != normalized[-1 - i]:
                return False

        return True
        