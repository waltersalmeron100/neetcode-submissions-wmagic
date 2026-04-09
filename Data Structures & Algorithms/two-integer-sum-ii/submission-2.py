class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        number_set = set(numbers)
        for i, num in enumerate(numbers):
            other_half = target - num
            if other_half in number_set:
                j = 0
                while other_half != numbers[j]:
                    j += 1

                return [i + 1, j + 1]


        