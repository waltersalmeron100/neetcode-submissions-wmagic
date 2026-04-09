import math

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}

        for num in nums:
            numbers[num] = numbers.get(num, 0) + 1

        result = []

        for _ in range(k):
            current_max = max(numbers, key=numbers.get)
            result.append(current_max)
            numbers.pop(current_max)

        return result
        
        