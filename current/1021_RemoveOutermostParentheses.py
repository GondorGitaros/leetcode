class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        counter = 0
        for i in range(len(s)):
            try:
                if s[i] == "(":
                    if s[i+1] == ")":
                        counter += 1
            except:
                pass
        return counter*"()"