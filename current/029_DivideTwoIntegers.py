dividend = int(input("Dividend: "))
divisor = int(input("Divisor: "))

def dividetwonums(dividend, divisor):
    if dividend == 0:
        return 0
    elif dividend >= 2**31:
        return 2**31 -1
    elif dividend <= -2**31:
        return 2**31 - 1
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        rv = len(range(0, dividend, -divisor))
        if dividend % divisor == 0:
            return -rv
        else:
            return -rv + 1
    else:
        rv = len(range(0, dividend, divisor))
        if dividend % divisor == 0:
            return rv
        else:
            return rv - 1

print(dividetwonums(dividend, divisor))