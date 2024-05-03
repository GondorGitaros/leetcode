class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s[::-1]
        t = False
        st = ""
        for c in s:
            if c == " " and t == False:
                pass
            elif c == " ":
                break
            else:
                st += c
                t = True
        return len(st)