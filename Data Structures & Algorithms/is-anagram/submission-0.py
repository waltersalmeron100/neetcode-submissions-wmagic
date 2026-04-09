class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = dict()
        t_map = dict()

        for c in s:
            if c in s_map:
                s_map.update({c: s_map.get(c) + 1})
            else:
                s_map.setdefault(c, 1)

        for c in t:
            if c in t_map:
                t_map.update({c: t_map.get(c) + 1})
            else:
                t_map.setdefault(c, 1)

        return s_map == t_map

        