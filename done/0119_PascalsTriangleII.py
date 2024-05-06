class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex += 1
        pascal = [[1], [1,1]]
        for i in range(rowIndex - 2):
            latest = pascal[-1]
            new = [1]
            for i in range(len(latest) - 1):
                new.append(latest[i] + latest[i+1])
            new.append(1)
            pascal.append(new)
        return pascal[rowIndex - 1]