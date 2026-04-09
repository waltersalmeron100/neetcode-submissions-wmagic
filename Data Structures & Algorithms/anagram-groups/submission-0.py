class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        words = {} # key: alphabetically sorted word & val: list of indices
        result = []

        for i, word in enumerate(strs):
            alpha = "".join(sorted(word))
            if alpha in words:
                words[alpha].append(i)
            else:
                words[alpha] = [i]

        for indices in words.values():
            temp = []
            for index in indices:
                temp.append(strs[index])
            result.append(temp)

        return result