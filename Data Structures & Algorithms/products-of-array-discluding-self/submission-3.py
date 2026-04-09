class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # results = []

        # for i, num in enumerate(nums):
        #     entry = 1
        #     for j, num_2 in enumerate(nums):
        #         if i != j:
        #             entry *= num_2
        #     results.append(entry)

        # return results

        n = len(nums)
        left = [1] * n
        right = [1] * n
        result = [1] * n

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(n):
            result[i] = left[i] * right[i]

        return result