class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = ""
        for num in digits:
            n += str(num)
        n = str(int(n) + 1)
        digits = []
        for num in n:
            digits.append(int(num))

        return digits
        