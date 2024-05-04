class Solution:
    def mySqrt(self, x: int) -> int:
        root = 0
        while True:
            if root * root == x:
                return root
            elif root * root > x:
                return root - 1
            else:
                root += 1