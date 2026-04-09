class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # number_set = set(numbers)
        # for i, num in enumerate(numbers):
        #     other_half = target - num
        #     if other_half in number_set:
        #         j = 0
        #         while other_half != numbers[j]:
        #             j += 1

        #         return [i + 1, j + 1]
        l, r = 0, len(numbers) - 1 
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                return [l + 1, r + 1]
            elif curr_sum > target:
                r -= 1
            else:
                l += 1
