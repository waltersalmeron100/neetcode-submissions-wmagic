class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for c in range(len(nums)):

            if c > 0 and nums[c] == nums[c - 1]:
                continue
            
            l, r = c + 1, len(nums) - 1
            while l < r:
                current_sum = nums[l] + nums [c] + nums[r]
                if current_sum == 0:
                    result.append([nums[l], nums[c], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif current_sum < 0:
                    l += 1
                else:
                    r -= 1

        return result

