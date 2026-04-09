class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # length = len(nums)

        # for i in range(0, length - 1):
        #     j = i + 1
        #     while j != length:
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        #         else:
        #             j += 1
        #     i += 1
        seen = dict()

        for i, num in enumerate(nums):
            other_half = target - num

            if other_half in seen:
                return [seen[other_half], i]
                
            seen[num] = i
        