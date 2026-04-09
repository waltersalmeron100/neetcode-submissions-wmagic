class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for string in strs:
            length = len(string)
            result += str(length) + "#" + string

        return result

    def decode(self, s: str) -> List[str]:
        strings = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1
            strings.append(s[i: i + length])
            i += length

        return strings


