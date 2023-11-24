class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for key, val in enumerate(nums):
            searchfor = target - val
            if searchfor in hm:
                return [hm[searchfor], key]
            hm[val] = key
