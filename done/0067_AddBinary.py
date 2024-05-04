class Solution:
    def addBinary(self, a: str, b: str) -> str:
        primary = []
        secondary = []
        returnlist = []
        carry = 0
        if len(a) >= len(b):
            for c in a:
                primary.append(int(c))
            for c in b:
                secondary.append(int(c))
        else:
            for c in b:
                primary.append(int(c))
            for c in a:
                secondary.append(int(c))

        for i in range(len(secondary)):
            p = primary[-i-1]
            s = secondary[-i-1]
            if p + s + carry == 2:
                returnlist.append(0)
                if p + s > 1:
                    carry = 1
            elif p+s+carry == 3:
                returnlist.append(1)
                if p + s > 1:
                    carry = 1
            else:
                returnlist.append(p+s+carry)
                carry = 0
        
        for i in range(len(primary) - len(secondary)):
            c = primary[len(primary) - len(secondary) - (i+1)]
            if c + carry == 2:
                returnlist.append(0)
                if p > 1:
                    carry = 1
            elif c + carry == 3:
                returnlist.append(1)
                if p > 1:
                    carry = 1
            else:
                returnlist.append(c+carry)
                carry = 0

        if carry == 2:
            returnlist.append(0)
            returnlist.append(1)
        elif carry == 1:
            returnlist.append(1)
        c = ""
        for i in returnlist[::-1]:
            c+=str(i)

        return c