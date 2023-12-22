class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hm = {}
        for key, val in enumerate(nums):
            searchfor = target - val
            if searchfor in hm:
                return [hm[searchfor], key]
            hm[val] = key
