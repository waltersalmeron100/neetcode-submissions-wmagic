class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        elif len(nums) == 1:
            return 1

        num_set = set(nums)

        longest = 1
        temp = 1

        for num in nums:
            prev = num - 1
            if prev not in num_set:
                i = 1
                temp = 1
                while num + i in num_set:
                    temp += 1
                    i += 1
                if longest < temp:
                    longest = temp


        return longest

        