class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_dict = {}

        for char in s1:
            s1_dict[char] = s1_dict.get(char, 0) + 1

        window_dict = {}
        left = 0

        for right in range(len(s2)):
            window_dict[s2[right]] = window_dict.get(s2[right], 0) + 1

            # Shrink window when it exceeds s1 length
            if right - left + 1 > len(s1):
                if window_dict[s2[left]] == 1:
                    del window_dict[s2[left]]
                else:
                    window_dict[s2[left]] -= 1
                left += 1

            if window_dict == s1_dict:
                return True

        return False
                



        