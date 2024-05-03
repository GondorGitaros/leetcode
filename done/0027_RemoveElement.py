class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for n in nums:
            if n == val:
                counter += 1
        for i in range(counter):
            nums.remove(val)

        return len(nums)