import math

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dictonary to have value and count
        numbers = dict()
        for num in nums:
            if num in numbers:
                numbers[num] += 1
            else:
                numbers.setdefault(num, 1)
        result = []
        i = 0
        while i < k:
            current_max = max(numbers, key=numbers.get)
            result.append(current_max)
            numbers.pop(current_max)
            i += 1

        return result
        
        