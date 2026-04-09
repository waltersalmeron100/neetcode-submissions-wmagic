class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        left = 0
        tracker = set()

        for right in range(len(s)):

            while s[right] in tracker:
                tracker.remove(s[left])
                left += 1

            tracker.add(s[right])
            result = max(result, right - left + 1)

        return result
        