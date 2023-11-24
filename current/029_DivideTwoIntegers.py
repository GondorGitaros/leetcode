dividend = int(input("Dividend: "))
divisor = int(input("Divisor: "))

def dividetwonums(dividend, divisor):
    rv = len(range(0, dividend, divisor))
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        return -rv
    else:
        return rv

print(dividetwonums(dividend, divisor))