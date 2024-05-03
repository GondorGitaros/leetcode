class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        while needle in haystack:
            haystack = haystack[:len(haystack) - 1]
        
        return len(haystack) - len(needle) + 1 