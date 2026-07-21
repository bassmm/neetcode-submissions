class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sum_set = set()
        nums = sorted(nums)
        for pos, num in enumerate(nums):
            start = pos + 1
            end = len(nums) - 1
            while start < end:
                if nums[start] + nums[end] == -(num):
                    sum_set.add((num, nums[start], nums[end]))
                if nums[start] + nums[end] < -(num):
                    start += 1
                else:
                    end -= 1
        return list(sum_set)