class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)

        for i in range(0, length - 1):
            j = i + 1
            while j != length:
                if nums[i] + nums[j] == target:
                    return [i, j]
                else:
                    j += 1
            i += 1
        