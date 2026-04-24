class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        indexes = []

        for i, temp in enumerate(temperatures):
            while indexes and temp > temperatures[indexes[-1]]:
                prev_i = indexes.pop()
                result[prev_i] = i - prev_i

            indexes.append(i)

        return result