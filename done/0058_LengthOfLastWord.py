class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        for i in range(len(s), 0,-1):
            if s[i - 1] == " " and counter == 0:
                continue
            elif s[i - 1] == " ":
                return counter
            elif s[i - 1] != " " and i == 1:
                counter += 1
                return counter
            else:
                counter += 1
