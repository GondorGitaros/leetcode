class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        pascal = [[1], [1,1]]
        for i in range(numRows - 2):
            latest = pascal[-1]
            new = [1]
            for i in range(len(latest) - 1):
                new.append(latest[i] + latest[i+1])
            new.append(1)
            pascal.append(new)
        return pascal
        