class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 or x >= 2**31 + 1 or x <= -2**31:
             return 0
        ax = str(abs(x))
        rv = ""
        boolval = False
        for i in range(len(ax) - 1, -1, -1):
            if ax[i] == "0" and boolval == False:
                continue
            else:
                rv += ax[i]
                boolval = True
        rv = int(rv)
        if x < 0:
             rv = -rv
        if rv <= -2**31 or rv >= 2**31 + 1:
            return 0
        return rv
        