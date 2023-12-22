class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for i in range(len(t)):
                if i == len(t) -1:
                        return t[-1]
                elif s[i] != t[i]:
                        return t[i]