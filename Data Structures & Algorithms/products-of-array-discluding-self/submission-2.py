class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []

        for i, num in enumerate(nums):
            entry = 1
            for j, num_2 in enumerate(nums):
                if i != j:
                    entry *= num_2
            results.append(entry)

        return results

        